# 🎓 Orientation.tn — Système d'orientation post-bac par Machine Learning

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9-F7931E?logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-5-646CFF?logo=vite&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

Application web qui recommande les **10 filières/facultés tunisiennes** les
plus adaptées à un bachelier, à partir de sa moyenne, sa section, ses notes
par matière et ses centres d'intérêt — en combinant un modèle **Random
Forest** entraîné avec scikit-learn et un moteur de proximité de score.

## ✨ Démo

> 🔗 **Démo live :** _à ajouter après déploiement (voir section Déploiement)_

<!-- Ajoutez vos captures d'écran ici une fois prêtes :
![Formulaire](docs/screenshots/form.png)
![Résultats](docs/screenshots/results.png)
-->

## 🧠 Comment ça marche

1. **Génération de données** (`generate_dataset.py`) — simule ~220 profils
   d'étudiants par filière, avec des scores répartis *autour du seuil* de
   chaque filière (un peu en dessous, un peu au-dessus) pour apprendre des
   cas réalistes plutôt que des extrêmes.
2. **Entraînement** (`train_model.py`) — pipeline scikit-learn
   (`StandardScaler` + `OneHotEncoder` + `RandomForestClassifier`, 300 arbres),
   évalué avec `accuracy`, `precision`, `recall`, `f1-score`.
   → **84.8% accuracy top-1 / 95.1% top-3** sur le jeu de test.
3. **API** (`app.py`, FastAPI) — combine la probabilité prédite par le
   modèle (affinité profil ↔ filière) avec un **filtrage par proximité de
   score**, pour ne recommander que des filières réalistes.
4. **Frontend React** — formulaire dynamique (les champs de notes changent
   selon la section choisie) + affichage des recommandations avec score,
   seuil, écart et statut (Admissible / Limite / Ambitieuse).

## 🗂️ Structure du projet

```
orientation-ml/
├── backend/
│   ├── filieres_db.py          # Base de règles : 58 filières (seuils, coefficients, tags)
│   ├── data/generate_dataset.py    # Génère un dataset synthétique labellisé
│   ├── train_model.py          # Entraîne le RandomForestClassifier
│   ├── app.py                  # API FastAPI (/api/recommend)
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
    └── package.json
```

## 🚀 Installation locale

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell
# source .venv/bin/activate       # macOS / Linux

pip install -r requirements.txt
python data/generate_dataset.py
python train_model.py
uvicorn app:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
copy .env.example .env            # Windows : copy | macOS/Linux : cp
npm run dev
```

Ouvrez **http://localhost:5173**.

## 🧪 Tester l'API directement

```bash
curl -X POST http://localhost:8000/api/recommend \
  -H "Content-Type: application/json" \
  -d '{"moyenne": 13.5, "section": "info",
       "grades": {"programmation": 15, "maths": 14},
       "interests": ["ia", "data"]}'
```

## ☁️ Déploiement

| Composant | Plateforme recommandée |
|---|---|
| Backend (FastAPI) | [Render](https://render.com) / [Railway](https://railway.app) |
| Frontend (Vite/React) | [Vercel](https://vercel.com) / [Netlify](https://netlify.com) |

Pensez à définir `VITE_API_URL` dans les variables d'environnement du
frontend pour pointer vers l'URL du backend déployé.

## ⚠️ Note importante

Les seuils de `filieres_db.py` sont **des exemples illustratifs à but
pédagogique**, pas les scores officiels du dernier orienté (publiés chaque
année sur [orientation.tn](https://www.orientation.tn)). Pour un usage réel,
remplacez les valeurs de `threshold` par les données officielles — le reste
du pipeline (génération, entraînement, API) fonctionne sans autre
modification.

## 🔭 Pistes d'amélioration

- [ ] Remplacer les seuils synthétiques par les scores officiels réels
- [ ] `GridSearchCV` pour optimiser les hyperparamètres du Random Forest
- [ ] Tests unitaires (pytest / vitest)
- [ ] Authentification + historique des simulations
- [ ] Déploiement CI/CD (GitHub Actions)

## 📄 Licence

Ce projet est sous licence MIT — voir [LICENSE](./LICENSE.txt).

---

Développé par **[Eya Dahmani](https://github.com/eyadahmani00)**