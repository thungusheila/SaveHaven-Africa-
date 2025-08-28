const API_BASE = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') ? 'http://localhost:5000' : '';

async function submitReport(payload) {
  const res = await fetch(`${API_BASE}/api/reports`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload)
  });
  if (!res.ok) {
    const err = await res.json().catch(()=>({error:res.statusText}));
    throw new Error(err.error || res.statusText);
  }
  return res.json();
}

async function fetchReports(limit=50) {
  const res = await fetch(`${API_BASE}/api/reports?limit=${limit}`);
  if (!res.ok) throw new Error('Failed to fetch reports');
  return res.json();
}

async function fetchHotspots(precision=2) {
  const res = await fetch(`${API_BASE}/api/stats/hotspots?precision=${precision}`);
  if (!res.ok) return [];
  return res.json();
}

// For browser console quick testing
window.submitReport = submitReport;
window.fetchReports = fetchReports;
window.fetchHotspots = fetchHotspots;
