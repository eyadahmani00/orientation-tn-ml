# Orientation.tn — Système d'orientation post-bac par Machine Learning

Recommande les 10 filières/facultés tunisiennes les plus adaptées à un
bachelier, à partir de sa moyenne, sa section, ses notes par matière et
ses centres d'intérêt.

**Stack :** Python · Scikit-learn · Pandas · React (Vite)

## Structure du projet

```
orientation-ml/
├── backend/
│   ├── filieres_db.py        # Base de règles : 58 filières (seuils, coefficients, tags)
│   ├── data/
│   │   └── generate_dataset.py   # Génère un dataset synthétique labellisé
│   ├── train_model.py        # Entraîne un RandomForestClassifier (scikit-learn)
│   ├── app.py                 # API FastAPI : /api/recommend
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── ProfileForm.jsx
    │   │   └── ResultCard.jsx
    │   ├── App.jsx
    │   ├── api.js
    │   ├── sections.js
    │   └── styles.css
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## Comment ça marche

1. **Génération de données** (`generate_dataset.py`) : simule ~220 profils
   d'étudiants par filière, avec des scores volontairement répartis
   *autour du seuil* de chaque filière (un peu en dessous, un peu au-dessus)
   pour que le modèle apprenne des cas réalistes plutôt que des extrêmes.
2. **Entraînement** (`train_model.py`) : pipeline scikit-learn
   (`StandardScaler` + `OneHotEncoder` + `RandomForestClassifier`,
   300 arbres), évalué avec `accuracy`, `precision`, `recall`, `f1-score`
   (voir `classification_report`).
3. **API** (`app.py`) : combine la probabilité prédite par le modèle
   (affinité profil ↔ filière) avec un **filtrage par proximité de score**
   — on ne recommande que des filières dont le seuil est proche du score
   réel de l'étudiant, pas des filières hors de portée ou trop faciles.
4. **Frontend React** : formulaire dynamique (les champs de notes changent
   selon la section) + affichage des 10 recommandations avec score, seuil,
   écart, statut (Admissible / Limite / Ambitieuse) et affinité ML.

## Lancer le projet

### 1. Backend

```bash
cd backend
pip install -r requirements.txt
python data/generate_dataset.py   # génère backend/data/dataset.csv
python train_model.py             # entraîne et sauvegarde backend/model.joblib
uvicorn app:app --reload --port 8000
```

L'API tourne sur `http://localhost:8000`. Testez avec :

```bash
curl -X POST http://localhost:8000/api/recommend \
  -H "Content-Type: application/json" \
  -d '{"moyenne": 13.5, "section": "info",
       "grades": {"programmation": 15, "maths": 14},
       "interests": ["ia", "data"]}'
```

### 2. Frontend

```bash
cd frontend
npm install
cp .env.example .env   # pointe vers l'API locale
npm run dev
```

Ouvrez `http://localhost:5173`.

## ⚠️ Important

Les seuils de `filieres_db.py` sont **des exemples illustratifs**, pas les
scores officiels du dernier orienté (ceux-ci changent chaque année et sont
publiés sur orientation.tn). Pour un usage réel, remplacez les valeurs de
`threshold` par les données officielles — le reste du pipeline (génération,
entraînement, API) fonctionne sans autre modification.

## Aller plus loin

- Remplacer les seuils synthétiques par les scores officiels réels
- Ajouter une validation croisée (`GridSearchCV`) pour optimiser les
  hyperparamètres du Random Forest
- Déployer le backend (Render, Railway) et le frontend (Vercel, Netlify)
- Ajouter l'authentification pour sauvegarder l'historique des simulations
