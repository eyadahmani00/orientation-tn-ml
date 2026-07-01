import { SECTIONS, SUBJECTS } from '../sections.js'

export default function ProfileForm({
  moyenne, setMoyenne,
  section, setSection,
  grades, setGrade,
  interests, setInterests,
  onSubmit, loading, error,
}) {
  return (
    <div className="card">
      <div className="card-inner">
        <h2 className="section-title"><span className="mark">◆</span> Profil académique</h2>
        <p className="section-sub">Vos notes et centres d'intérêt guident nos suggestions.</p>

        <div className="field-row">
          <div className="field">
            <label>Moyenne du Baccalauréat</label>
            <input
              type="number" min="0" max="20" step="0.01" placeholder="Ex : 12.35"
              value={moyenne}
              onChange={(e) => setMoyenne(e.target.value)}
            />
          </div>
          <div className="field">
            <label>Section du Baccalauréat</label>
            <select value={section} onChange={(e) => setSection(e.target.value)}>
              <option value="">-- Sélectionnez votre section --</option>
              {SECTIONS.map((s) => (
                <option key={s.value} value={s.value}>{s.label}</option>
              ))}
            </select>
          </div>
        </div>

        {section && (
          <>
            <div className="subjects-title">Notes par matière (0 – 20)</div>
            <div className="subjects-grid">
              {SUBJECTS[section].map(([key, label]) => (
                <div className="subj-field field" key={key}>
                  <label>{label}</label>
                  <input
                    type="number" min="0" max="20" step="0.01" placeholder="0.00 – 20.00"
                    value={grades[key] ?? ''}
                    onChange={(e) => setGrade(key, e.target.value)}
                  />
                </div>
              ))}
            </div>
          </>
        )}

        <div className="field interest-field">
          <label>Vos centres d'intérêt (mots-clés)</label>
          <input
            type="text" placeholder="Ex : robotique IA biologie data"
            value={interests}
            onChange={(e) => setInterests(e.target.value)}
          />
          <small>Séparez par des espaces. Plus c'est précis, meilleure est la suggestion.</small>
        </div>

        <button className="btn-primary" onClick={onSubmit} disabled={loading}>
          {loading ? 'Calcul en cours…' : 'Générer mes 10 orientations'}
          {!loading && (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
              <path d="M5 12h14M13 6l6 6-6 6" />
            </svg>
          )}
        </button>
        {error && <div className="error-msg" style={{ display: 'block' }}>{error}</div>}
      </div>
    </div>
  )
}
