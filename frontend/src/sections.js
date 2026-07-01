// Miroir de backend/filieres_db.py -> SUBJECTS
export const SECTIONS = [
  { value: 'math', label: "Mathématiques / Sciences de la Vie et de la Terre" },
  { value: 'info', label: "Sciences de l'Informatique" },
  { value: 'eco', label: 'Économie et Gestion' },
  { value: 'tech', label: 'Sciences Techniques' },
  { value: 'lettres', label: 'Lettres et Philosophie' },
  { value: 'sport', label: 'Sciences et Technologies du Sport' },
]

export const SUBJECTS = {
  math: [['maths', 'Maths'], ['physique', 'Physique'], ['svt', 'SVT'], ['francais', 'Français'], ['anglais', 'Anglais'], ['arabe', 'Arabe']],
  info: [['programmation', 'Programmation'], ['si', "Systèmes d'Information"], ['physique', 'Physique'], ['maths', 'Maths'], ['francais', 'Français'], ['anglais', 'Anglais'], ['arabe', 'Arabe']],
  eco: [['economie', 'Économie'], ['maths', 'Maths'], ['francais', 'Français'], ['anglais', 'Anglais'], ['arabe', 'Arabe']],
  tech: [['maths', 'Maths'], ['physique', 'Physique'], ['technologie', 'Technologie'], ['francais', 'Français'], ['anglais', 'Anglais'], ['arabe', 'Arabe']],
  lettres: [['francais', 'Français'], ['histoire', 'Histoire'], ['geographie', 'Géographie'], ['anglais', 'Anglais'], ['arabe', 'Arabe']],
  sport: [['sport', 'Sport'], ['svt', 'SVT'], ['maths', 'Maths'], ['francais', 'Français'], ['anglais', 'Anglais'], ['arabe', 'Arabe']],
}
