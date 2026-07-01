const STATUS_LABEL = {
  admissible: 'Admissible',
  limite: 'Limite',
  ambitieuse: 'Ambitieuse',
}

export default function ResultCard({ result, rank }) {
  const maxRef = Math.max(result.threshold, result.score, 1)
  const barPct = Math.max(4, Math.min(100, (result.score / (maxRef * 1.15)) * 100))

  return (
    <div className="result-card">
      <div className="seal">{rank}</div>
      <div className="result-body">
        <div className="result-top">
          <div>
            <p className="result-name">{result.name}</p>
            <p className="result-inst">{result.inst} · {result.city}</p>
          </div>
          <span className={`status-badge status-${result.status}`}>{STATUS_LABEL[result.status]}</span>
        </div>

        <div className="result-meta">
          <span className="meta-item">Votre score estimé : <b>{result.score}</b></span>
          <span className="meta-item">Seuil indicatif : <b>{result.threshold}</b></span>
          <span className="meta-item">Écart : <b>{result.gap >= 0 ? '+' : ''}{result.gap}</b></span>
          <span className="meta-item">Affinité ML : <b>{Math.round(result.proba * 100)}%</b></span>
        </div>

        <div className="bar-track"><div className="bar-fill" style={{ width: `${barPct}%` }} /></div>

        <div className="tags">
          {result.tags.map((t) => (
            <span key={t} className={`tag ${result.hits.includes(t) ? 'hit' : ''}`}>{t}</span>
          ))}
        </div>
      </div>
    </div>
  )
}
