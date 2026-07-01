"""
Base de données des filières universitaires tunisiennes (démo pédagogique).
Les seuils (threshold) sont des exemples ILLUSTRATIFS, pas les scores
officiels du dernier orienté publiés sur orientation.tn.
"""

SUBJECTS = {
    "math":    ["maths", "physique", "svt", "francais", "anglais", "arabe"],
    "info":    ["programmation", "si", "physique", "maths", "francais", "anglais", "arabe"],
    "eco":     ["economie", "maths", "francais", "anglais", "arabe"],
    "tech":    ["maths", "physique", "technologie", "francais", "anglais", "arabe"],
    "lettres": ["francais", "histoire", "geographie", "anglais", "arabe"],
    "sport":   ["sport", "svt", "maths", "francais", "anglais", "arabe"],
}

ALL_SUBJECTS = sorted({s for subs in SUBJECTS.values() for s in subs})

DB = [
    # ---- Mathématiques / SVT ----
    {"name": "Médecine", "inst": "Faculté de Médecine de Tunis", "city": "Tunis", "sections": ["math"], "coeffs": {"svt": 2, "physique": 1.5, "maths": 1}, "threshold": 175, "tags": ["médecine", "santé", "biologie", "soigner", "hôpital"]},
    {"name": "Médecine dentaire", "inst": "Faculté de Médecine Dentaire de Monastir", "city": "Monastir", "sections": ["math"], "coeffs": {"svt": 2, "physique": 1}, "threshold": 165, "tags": ["dentaire", "santé", "chirurgie"]},
    {"name": "Pharmacie", "inst": "Faculté de Pharmacie de Monastir", "city": "Monastir", "sections": ["math"], "coeffs": {"svt": 1.5, "physique": 1.5, "maths": 1}, "threshold": 160, "tags": ["pharmacie", "médicament", "chimie", "santé"]},
    {"name": "Cycle préparatoire ingénieur (IPEIN)", "inst": "IPEIN Nabeul", "city": "Nabeul", "sections": ["math"], "coeffs": {"maths": 2, "physique": 1.5}, "threshold": 155, "tags": ["ingénieur", "maths", "physique", "technologie"]},
    {"name": "Sciences biologiques", "inst": "Faculté des Sciences de Tunis", "city": "Tunis", "sections": ["math"], "coeffs": {"svt": 2, "physique": 1}, "threshold": 110, "tags": ["biologie", "recherche", "environnement", "laboratoire"]},
    {"name": "Génie biomédical", "inst": "ISET Nabeul", "city": "Nabeul", "sections": ["math"], "coeffs": {"physique": 1.5, "maths": 1.5, "svt": 1}, "threshold": 120, "tags": ["biomédical", "ingénierie", "santé", "technologie"]},
    {"name": "Kinésithérapie", "inst": "ISSST Tunis", "city": "Tunis", "sections": ["math"], "coeffs": {"svt": 2, "physique": 1}, "threshold": 135, "tags": ["kinésithérapie", "sport", "rééducation", "santé"]},
    {"name": "Nutrition et diététique", "inst": "ISSST Tunis", "city": "Tunis", "sections": ["math"], "coeffs": {"svt": 1.5, "physique": 0.5}, "threshold": 115, "tags": ["nutrition", "alimentation", "santé", "diététique"]},
    {"name": "Sciences agronomiques", "inst": "INAT — Institut National Agronomique", "city": "Tunis", "sections": ["math"], "coeffs": {"svt": 1.5, "maths": 1}, "threshold": 100, "tags": ["agronomie", "agriculture", "environnement", "nature"]},
    {"name": "Géologie", "inst": "Faculté des Sciences de Tunis", "city": "Tunis", "sections": ["math"], "coeffs": {"svt": 1.5, "physique": 1}, "threshold": 90, "tags": ["géologie", "terre", "environnement", "minéraux"]},

    # ---- Sciences de l'Informatique ----
    {"name": "Ingénierie informatique", "inst": "INSAT", "city": "Tunis", "sections": ["info"], "coeffs": {"programmation": 2, "maths": 1.5}, "threshold": 150, "tags": ["informatique", "programmation", "logiciel", "ia", "data"]},
    {"name": "Cycle préparatoire ingénieur informatique", "inst": "IPEIT", "city": "Tunis", "sections": ["info"], "coeffs": {"maths": 2, "programmation": 1.5}, "threshold": 155, "tags": ["ingénieur", "informatique", "maths"]},
    {"name": "Informatique appliquée", "inst": "ISI Ariana", "city": "Ariana", "sections": ["info"], "coeffs": {"programmation": 2, "si": 1}, "threshold": 120, "tags": ["informatique", "développement", "logiciel", "web"]},
    {"name": "Réseaux et systèmes", "inst": "ISI Ariana", "city": "Ariana", "sections": ["info"], "coeffs": {"si": 2, "programmation": 1}, "threshold": 115, "tags": ["réseaux", "cybersécurité", "systèmes", "infrastructure"]},
    {"name": "Informatique de gestion", "inst": "ISG Tunis", "city": "Tunis", "sections": ["info"], "coeffs": {"programmation": 1, "si": 1}, "threshold": 105, "tags": ["informatique", "gestion", "base de données"]},
    {"name": "Sciences des données & IA", "inst": "Faculté des Sciences de Tunis", "city": "Tunis", "sections": ["info"], "coeffs": {"maths": 2, "programmation": 1.5}, "threshold": 130, "tags": ["data", "intelligence artificielle", "ia", "machine learning", "statistiques"]},
    {"name": "Génie logiciel", "inst": "ISIMM Monastir", "city": "Monastir", "sections": ["info"], "coeffs": {"programmation": 2, "si": 1}, "threshold": 118, "tags": ["génie logiciel", "développement", "application"]},
    {"name": "Multimédia et développement web", "inst": "ISAMM Manouba", "city": "Manouba", "sections": ["info"], "coeffs": {"programmation": 1, "si": 1}, "threshold": 95, "tags": ["web", "design", "multimédia", "création"]},
    {"name": "Télécommunications", "inst": "SUP'COM Ariana", "city": "Ariana", "sections": ["info"], "coeffs": {"maths": 1.5, "physique": 1.5}, "threshold": 140, "tags": ["télécommunications", "réseaux", "ingénierie"]},
    {"name": "Robotique et systèmes embarqués", "inst": "ENSIT", "city": "Tunis", "sections": ["info"], "coeffs": {"programmation": 1.5, "physique": 1}, "threshold": 125, "tags": ["robotique", "embarqué", "automatisation"]},

    # ---- Économie et Gestion ----
    {"name": "Sciences économiques", "inst": "IHEC Carthage", "city": "Carthage", "sections": ["eco"], "coeffs": {"economie": 2, "maths": 1}, "threshold": 140, "tags": ["économie", "finance", "macroéconomie"]},
    {"name": "Gestion des entreprises", "inst": "ISG Tunis", "city": "Tunis", "sections": ["eco"], "coeffs": {"economie": 1.5, "maths": 1}, "threshold": 110, "tags": ["gestion", "management", "entreprise"]},
    {"name": "Commerce international", "inst": "ESSECT", "city": "Tunis", "sections": ["eco"], "coeffs": {"economie": 1.5, "maths": 1}, "threshold": 130, "tags": ["commerce", "international", "export"]},
    {"name": "Finance et banque", "inst": "FSEG Sfax", "city": "Sfax", "sections": ["eco"], "coeffs": {"economie": 1.5, "maths": 1.5}, "threshold": 105, "tags": ["finance", "banque", "investissement"]},
    {"name": "Comptabilité et audit", "inst": "ISCAE Manouba", "city": "Manouba", "sections": ["eco"], "coeffs": {"economie": 1, "maths": 1}, "threshold": 100, "tags": ["comptabilité", "audit", "fiscalité"]},
    {"name": "Actuariat et statistiques", "inst": "ISG Tunis", "city": "Tunis", "sections": ["eco"], "coeffs": {"maths": 2, "economie": 1}, "threshold": 115, "tags": ["statistiques", "actuariat", "assurance", "data"]},
    {"name": "Marketing", "inst": "IHEC Carthage", "city": "Carthage", "sections": ["eco"], "coeffs": {"economie": 1, "maths": 0.5}, "threshold": 108, "tags": ["marketing", "communication", "publicité"]},
    {"name": "Économétrie et prévision", "inst": "FSEG Tunis", "city": "Tunis", "sections": ["eco"], "coeffs": {"maths": 2, "economie": 1}, "threshold": 112, "tags": ["économétrie", "statistiques", "modélisation"]},
    {"name": "Ressources humaines", "inst": "ISG Tunis", "city": "Tunis", "sections": ["eco"], "coeffs": {"economie": 1}, "threshold": 90, "tags": ["ressources humaines", "management", "recrutement"]},
    {"name": "Douane et commerce extérieur", "inst": "ISG Bizerte", "city": "Bizerte", "sections": ["eco"], "coeffs": {"economie": 1, "maths": 0.5}, "threshold": 85, "tags": ["douane", "logistique", "commerce"]},

    # ---- Sciences Techniques ----
    {"name": "Cycle préparatoire ingénieur (IPEIS)", "inst": "IPEIS Sfax", "city": "Sfax", "sections": ["tech"], "coeffs": {"maths": 2, "physique": 1.5}, "threshold": 150, "tags": ["ingénieur", "maths", "physique"]},
    {"name": "Génie mécanique", "inst": "ISET Radès", "city": "Radès", "sections": ["tech"], "coeffs": {"technologie": 2, "physique": 1}, "threshold": 120, "tags": ["mécanique", "conception", "industrie"]},
    {"name": "Génie électrique", "inst": "ISET Nabeul", "city": "Nabeul", "sections": ["tech"], "coeffs": {"technologie": 1.5, "physique": 1.5}, "threshold": 115, "tags": ["électricité", "électronique", "énergie"]},
    {"name": "Génie civil", "inst": "ISET Sousse", "city": "Sousse", "sections": ["tech"], "coeffs": {"technologie": 1.5, "maths": 1}, "threshold": 110, "tags": ["construction", "bâtiment", "génie civil", "architecture"]},
    {"name": "Génie industriel", "inst": "ENISO Sousse", "city": "Sousse", "sections": ["tech"], "coeffs": {"technologie": 1.5, "maths": 1.5}, "threshold": 125, "tags": ["industrie", "production", "logistique"]},
    {"name": "Maintenance industrielle", "inst": "ISET Radès", "city": "Radès", "sections": ["tech"], "coeffs": {"technologie": 1.5, "physique": 1}, "threshold": 95, "tags": ["maintenance", "mécanique", "industrie"]},
    {"name": "Énergies renouvelables", "inst": "ISET Gabès", "city": "Gabès", "sections": ["tech"], "coeffs": {"physique": 2, "technologie": 1}, "threshold": 100, "tags": ["énergie", "environnement", "renouvelable"]},
    {"name": "Automatique et informatique industrielle", "inst": "ENIS Sfax", "city": "Sfax", "sections": ["tech"], "coeffs": {"technologie": 1.5, "maths": 1.5}, "threshold": 130, "tags": ["automatisation", "robotique", "industrie"]},
    {"name": "Génie des procédés", "inst": "ISET Kairouan", "city": "Kairouan", "sections": ["tech"], "coeffs": {"technologie": 1, "physique": 1}, "threshold": 90, "tags": ["chimie industrielle", "procédés", "production"]},
    {"name": "Topographie", "inst": "ISET Tozeur", "city": "Tozeur", "sections": ["tech"], "coeffs": {"technologie": 1, "maths": 1}, "threshold": 80, "tags": ["topographie", "cartographie", "géomatique"]},

    # ---- Lettres et Philosophie ----
    {"name": "Journalisme et sciences de l'information", "inst": "IPSI", "city": "Manouba", "sections": ["lettres"], "coeffs": {"francais": 1.5, "histoire": 1}, "threshold": 130, "tags": ["journalisme", "médias", "communication", "presse"]},
    {"name": "Droit", "inst": "Faculté de Droit de Tunis", "city": "Tunis", "sections": ["lettres"], "coeffs": {"francais": 1, "arabe": 1}, "threshold": 115, "tags": ["droit", "justice", "avocat", "législation"]},
    {"name": "Langues appliquées", "inst": "Institut Supérieur des Langues de Tunis", "city": "Tunis", "sections": ["lettres"], "coeffs": {"francais": 1.5, "anglais": 1.5}, "threshold": 100, "tags": ["langues", "traduction", "interprétariat"]},
    {"name": "Histoire", "inst": "Faculté des Lettres, Manouba", "city": "Manouba", "sections": ["lettres"], "coeffs": {"histoire": 2}, "threshold": 85, "tags": ["histoire", "patrimoine", "archéologie"]},
    {"name": "Géographie et aménagement", "inst": "FSHS Tunis", "city": "Tunis", "sections": ["lettres"], "coeffs": {"geographie": 2}, "threshold": 80, "tags": ["géographie", "urbanisme", "aménagement", "environnement"]},
    {"name": "Sciences politiques", "inst": "Faculté de Droit et des Sciences Politiques", "city": "Tunis", "sections": ["lettres"], "coeffs": {"histoire": 1.5, "francais": 1}, "threshold": 120, "tags": ["politique", "relations internationales", "diplomatie"]},
    {"name": "Psychologie", "inst": "FSHS Tunis", "city": "Tunis", "sections": ["lettres"], "coeffs": {"francais": 1, "arabe": 1}, "threshold": 110, "tags": ["psychologie", "comportement", "société"]},
    {"name": "Sociologie", "inst": "FSHS Sfax", "city": "Sfax", "sections": ["lettres"], "coeffs": {"francais": 1, "histoire": 1}, "threshold": 90, "tags": ["sociologie", "société", "recherche sociale"]},
    {"name": "Traduction", "inst": "ISTI Tunis", "city": "Tunis", "sections": ["lettres"], "coeffs": {"francais": 1.5, "anglais": 1.5}, "threshold": 105, "tags": ["traduction", "langues", "interprétariat"]},
    {"name": "Bibliothéconomie et documentation", "inst": "Institut Supérieur de Documentation", "city": "Tunis", "sections": ["lettres"], "coeffs": {"francais": 1, "arabe": 1}, "threshold": 75, "tags": ["documentation", "bibliothèque", "archives"]},

    # ---- Sciences et Technologies du Sport ----
    {"name": "Éducation physique et sportive", "inst": "ISSEP Ksar Saïd", "city": "Tunis", "sections": ["sport"], "coeffs": {"sport": 2, "svt": 1}, "threshold": 105, "tags": ["sport", "éducation physique", "entraînement"]},
    {"name": "Entraînement sportif", "inst": "ISSEP Le Kef", "city": "Le Kef", "sections": ["sport"], "coeffs": {"sport": 2}, "threshold": 95, "tags": ["sport", "entraînement", "coaching"]},
    {"name": "Kinésithérapie du sport", "inst": "ISSEP Gafsa", "city": "Gafsa", "sections": ["sport"], "coeffs": {"svt": 1.5, "sport": 1.5}, "threshold": 110, "tags": ["kinésithérapie", "sport", "santé", "rééducation"]},
    {"name": "Management du sport", "inst": "ISSEP Sfax", "city": "Sfax", "sections": ["sport"], "coeffs": {"sport": 1, "maths": 1}, "threshold": 90, "tags": ["management", "sport", "gestion"]},
    {"name": "Sciences et techniques des activités physiques", "inst": "ISSEP Ksar Saïd", "city": "Tunis", "sections": ["sport"], "coeffs": {"sport": 1.5, "svt": 1}, "threshold": 100, "tags": ["sport", "activités physiques", "biomécanique"]},
    {"name": "Sport et handicap", "inst": "ISSEP Le Kef", "city": "Le Kef", "sections": ["sport"], "coeffs": {"sport": 1, "svt": 1}, "threshold": 75, "tags": ["handicap", "sport adapté", "inclusion"]},
    {"name": "Sport et santé", "inst": "ISSST Tunis", "city": "Tunis", "sections": ["sport"], "coeffs": {"svt": 1.5, "sport": 1}, "threshold": 92, "tags": ["santé", "sport", "prévention"]},
    {"name": "Animation sportive et loisirs", "inst": "ISSEP Sousse", "city": "Sousse", "sections": ["sport"], "coeffs": {"sport": 1}, "threshold": 70, "tags": ["animation", "loisirs", "sport"]},
]

INTEREST_VOCAB = sorted({tag for f in DB for tag in f["tags"]})


def compute_score(filiere: dict, moyenne: float, grades: dict) -> float:
    """Score = 4 x moyenne + somme(coefficient x note), formule simplifiée
    inspirée du calcul officiel FG + FS."""
    fg = 4 * moyenne
    fs = sum(coef * grades.get(subj, 0) for subj, coef in filiere["coeffs"].items() if grades.get(subj) is not None)
    return round(fg + fs, 1)
