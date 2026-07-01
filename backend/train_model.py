"""
Entraîne un RandomForestClassifier (scikit-learn) qui prédit la filière
recommandée à partir du profil académique (moyenne, section, notes) et
des centres d'intérêt.

Usage:
    python data/generate_dataset.py
    python train_model.py
"""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, top_k_accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from filieres_db import ALL_SUBJECTS, INTEREST_VOCAB

DATA_PATH = Path(__file__).parent / "data" / "dataset.csv"
MODEL_PATH = Path(__file__).parent / "model.joblib"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"{DATA_PATH} introuvable. Lancez d'abord: python data/generate_dataset.py"
        )

    df = pd.read_csv(DATA_PATH)

    numeric_features = ["moyenne"] + [f"note_{s}" for s in ALL_SUBJECTS] + [f"int_{t}" for t in INTEREST_VOCAB]
    categorical_features = ["section"]

    X = df[numeric_features + categorical_features]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )

    model = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("clf", RandomForestClassifier(
            n_estimators=300,
            max_depth=None,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1,
        )),
    ])

    print("Entraînement du modèle...")
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    proba = model.predict_proba(X_test)
    top3_acc = top_k_accuracy_score(y_test, proba, k=3, labels=model.classes_)

    print(f"\nAccuracy (top-1)  : {acc:.3f}")
    print(f"Accuracy (top-3)  : {top3_acc:.3f}\n")
    print("Rapport de classification (precision / recall / f1) :\n")
    print(classification_report(y_test, y_pred, zero_division=0))

    joblib.dump({"pipeline": model, "feature_columns": numeric_features + categorical_features}, MODEL_PATH)
    print(f"\nModèle sauvegardé : {MODEL_PATH}")


if __name__ == "__main__":
    main()
