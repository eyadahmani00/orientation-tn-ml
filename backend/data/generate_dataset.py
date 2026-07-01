"""
Génère un dataset synthétique d'étudiants tunisiens (profil académique +
centres d'intérêt) étiquetés avec la filière la plus adaptée, à partir de
la base de règles `filieres_db.py`.

Il n'existe pas de dataset public officiel d'orientation en Tunisie -
ce script simule des profils plausibles autour du seuil de chaque filière
(un peu en dessous, un peu au-dessus) pour entraîner un classifieur qui
apprend le lien profil -> filière recommandée.
"""

import random
import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent))
from filieres_db import DB, SUBJECTS, ALL_SUBJECTS, INTEREST_VOCAB, compute_score

random.seed(42)

SAMPLES_PER_FILIERE = 220


def random_grades(section: str, target_score: float, moyenne: float, filiere: dict) -> dict:
    """Tire des notes par matière cohérentes avec un score cible pour cette filière."""
    subjects = SUBJECTS[section]
    grades = {s: round(random.uniform(max(0, moyenne - 5), min(20, moyenne + 5)), 2) for s in subjects}

    # Ajuste les matières à fort coefficient pour se rapprocher du score cible
    for _ in range(6):
        current = compute_score(filiere, moyenne, grades)
        diff = target_score - current
        if abs(diff) < 1:
            break
        coeffs = filiere["coeffs"]
        if not coeffs:
            break
        subj = random.choice(list(coeffs.keys()))
        coef = coeffs[subj]
        adjust = diff / max(coef, 0.5) * 0.4
        grades[subj] = min(20, max(0, round(grades[subj] + adjust, 2)))
    return grades


def build_row(filiere: dict, moyenne: float, grades: dict, interests: list, section: str) -> dict:
    row = {"moyenne": moyenne, "section": section}
    for s in ALL_SUBJECTS:
        row[f"note_{s}"] = grades.get(s, 0.0)
    for tag in INTEREST_VOCAB:
        row[f"int_{tag}"] = 1 if tag in interests else 0
    row["label"] = filiere["name"]
    return row


def generate():
    rows = []
    for filiere in DB:
        section = filiere["sections"][0]
        for i in range(SAMPLES_PER_FILIERE):
            # Distribution du score cible: majorité proche du seuil (+-15), quelques cas larges
            band = random.choice(["close", "close", "close", "wide"])
            if band == "close":
                target_score = filiere["threshold"] + random.uniform(-15, 20)
            else:
                target_score = filiere["threshold"] + random.uniform(-35, 45)
            target_score = max(20, min(200, target_score))

            moyenne = round(min(20, max(6, target_score / 4 + random.uniform(-2, 2))), 2)
            grades = random_grades(section, target_score, moyenne, filiere)

            # Centres d'intérêt: on pioche 0 à 3 tags de la filière + parfois du bruit
            n_tags = random.choice([0, 1, 1, 2, 2, 3])
            interests = random.sample(filiere["tags"], min(n_tags, len(filiere["tags"])))
            if random.random() < 0.2:
                noise_pool = [t for t in INTEREST_VOCAB if t not in filiere["tags"]]
                interests.append(random.choice(noise_pool))

            rows.append(build_row(filiere, moyenne, grades, interests, section))

    df = pd.DataFrame(rows)
    return df


if __name__ == "__main__":
    df = generate()
    out_path = Path(__file__).resolve().parent / "dataset.csv"
    df.to_csv(out_path, index=False)
    print(f"Dataset généré : {out_path} ({len(df)} lignes, {df['label'].nunique()} classes)")
