"""
API FastAPI - sert le modèle Random Forest entraîné et combine :
  1) la probabilité prédite par le modèle (affinité profil <-> filière)
  2) un filtrage par PROXIMITÉ de score (le point corrigé demandé) :
     on ne recommande que des filières dont le seuil est proche du score
     réel de l'étudiant - un peu en dessous ET un peu au-dessus - plutôt
     que des filières totalement hors de portée ou beaucoup trop faciles.

Lancer:
    uvicorn app:app --reload --port 8000
"""

from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from filieres_db import DB, ALL_SUBJECTS, INTEREST_VOCAB, compute_score

MODEL_PATH = Path(__file__).parent / "model.joblib"

app = FastAPI(title="Orientation.tn API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # démo - restreindre en production
    allow_methods=["*"],
    allow_headers=["*"],
)

_bundle = None


def get_model():
    global _bundle
    if _bundle is None:
        if not MODEL_PATH.exists():
            raise RuntimeError(
                "Modèle introuvable. Lancez : python data/generate_dataset.py puis python train_model.py"
            )
        _bundle = joblib.load(MODEL_PATH)
    return _bundle


class RecommendRequest(BaseModel):
    moyenne: float = Field(..., ge=0, le=20)
    section: str
    grades: dict[str, float] = {}
    interests: list[str] = []


# Bande de proximité de score : un peu en dessous, un peu au-dessus du seuil.
# On l'élargit progressivement seulement si trop peu de filières correspondent.
BAND_STEPS = [(-15, 20), (-25, 30), (-40, 45), (-1000, 1000)]


@app.post("/api/recommend")
def recommend(req: RecommendRequest):
    bundle = get_model()
    pipeline = bundle["pipeline"]
    feature_columns = bundle["feature_columns"]

    interests_lower = [i.lower() for i in req.interests]

    # --- construction du vecteur de features pour le modèle ---
    row = {"moyenne": req.moyenne, "section": req.section}
    for s in ALL_SUBJECTS:
        row[f"note_{s}"] = req.grades.get(s, 0.0)
    for tag in INTEREST_VOCAB:
        row[f"int_{tag}"] = 1 if any(tag in kw or kw in tag for kw in interests_lower) else 0

    X = pd.DataFrame([row])[feature_columns]
    proba = pipeline.predict_proba(X)[0]
    classes = pipeline.named_steps["clf"].classes_ if hasattr(pipeline, "named_steps") else pipeline.classes_
    proba_map = dict(zip(classes, proba))

    # --- calcul du score règle-métier (FG + FS) et de l'écart au seuil ---
    candidates = []
    for f in DB:
        if req.section not in f["sections"]:
            continue
        score = compute_score(f, req.moyenne, req.grades)
        gap = round(score - f["threshold"], 1)
        hits = [t for t in f["tags"] if any(t in kw or kw in t for kw in interests_lower)]
        status = "admissible" if gap >= 0 else ("limite" if gap >= -15 else "ambitieuse")
        candidates.append({
            "name": f["name"],
            "inst": f["inst"],
            "city": f["city"],
            "score": score,
            "threshold": f["threshold"],
            "gap": gap,
            "status": status,
            "tags": f["tags"],
            "hits": hits,
            "proba": round(float(proba_map.get(f["name"], 0.0)), 4),
        })

    # --- filtrage par proximité : élargit la bande seulement si besoin ---
    selected = []
    for low, high in BAND_STEPS:
        selected = [c for c in candidates if low <= c["gap"] <= high]
        if len(selected) >= 10:
            break

    def rank_key(c):
        return (-abs(c["gap"]) * 1.1) + (len(c["hits"]) * 15) + (c["proba"] * 40)

    selected.sort(key=rank_key, reverse=True)
    top = selected[:10]

    return {
        "count": len(top),
        "results": top,
    }


@app.get("/api/health")
def health():
    return {"status": "ok"}
