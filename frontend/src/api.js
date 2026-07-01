const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export async function fetchRecommendations({ moyenne, section, grades, interests }) {
  const res = await fetch(`${API_BASE}/api/recommend`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ moyenne, section, grades, interests }),
  })
  if (!res.ok) {
    const text = await res.text().catch(() => '')
    throw new Error(`Erreur API (${res.status}) ${text}`)
  }
  return res.json()
}
