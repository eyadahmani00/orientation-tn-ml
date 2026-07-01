import { useState } from 'react'
import ProfileForm from './components/ProfileForm.jsx'
import ResultCard from './components/ResultCard.jsx'
import { fetchRecommendations } from './api.js'

export default function App() {
  const [moyenne, setMoyenne] = useState('')
  const [section, setSection] = useState('')
  const [grades, setGrades] = useState({})
  const [interests, setInterests] = useState('')
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const setGrade = (key, value) => {
    setGrades((prev) => ({ ...prev, [key]: value === '' ? undefined : parseFloat(value) }))
  }

  const handleSubmit = async () => {
    setError('')
    const moyenneNum = parseFloat(moyenne)
    if (isNaN(moyenneNum) || !section) {
      setError('Merci de renseigner votre moyenne et votre section du baccalauréat.')
      return
    }

    setLoading(true)
    setResults(null)
    try {
      const keywords = interests.toLowerCase().trim().split(/\s+/).filter(Boolean)
      const cleanGrades = Object.fromEntries(
        Object.entries(grades).filter(([, v]) => v !== undefined && !isNaN(v))
      )
      const data = await fetchRecommendations({
        moyenne: moyenneNum,
        section,
        grades: cleanGrades,
        interests: keywords,
      })
      setResults(data.results)
    } catch (e) {
      setError(
        `Impossible de contacter le serveur ML (${e.message}). Vérifiez que le backend FastAPI tourne sur le port 8000.`
      )
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="wrap">
      <div className="hero">
        <div className="eyebrow">Système d'orientation post-bac · Machine Learning</div>
        <h1>Orientation.tn</h1>
        <p>Renseignez votre moyenne, votre section et vos centres d'intérêt — un modèle Random Forest
          (scikit-learn) et un moteur de proximité de score calculent vos 10 orientations les plus réalistes.</p>
      </div>

      <ProfileForm
        moyenne={moyenne} setMoyenne={setMoyenne}
        section={section} setSection={setSection}
        grades={grades} setGrade={setGrade}
        interests={interests} setInterests={setInterests}
        onSubmit={handleSubmit}
        loading={loading}
        error={error}
      />

      {results && (
        <div id="results" style={{ display: 'block' }}>
          <div className="results-head">
            <h2>Vos orientations recommandées</h2>
            <span className="results-count">{results.length} orientation{results.length > 1 ? 's' : ''} trouvée{results.length > 1 ? 's' : ''}</span>
          </div>

          {results.map((r, i) => (
            <ResultCard key={r.name} result={r} rank={i + 1} />
          ))}

          <div className="disclaimer">
            ⚠️ <b>À titre indicatif.</b> Le score règle-métier (FG + FS) et le modèle Random Forest sont
            entraînés sur des données synthétiques inspirées du système officiel. Les seuils affichés sont
            des exemples illustratifs — vérifiez toujours vos choix sur le simulateur officiel du Ministère
            de l'Enseignement Supérieur (orientation.tn) avant de valider vos vœux.
          </div>
        </div>
      )}

      <footer>
        <span className="brand">Orientation.tn</span> — Random Forest · scikit-learn · Pandas · React (démo pédagogique)
      </footer>
    </div>
  )
}
