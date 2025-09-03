// Simple tracker
const dataLayer = window.dataLayer = window.dataLayer || [];
const track = (event, params = {}) => dataLayer.push({ event, ts: Date.now(), ...params });

const state = {
  raw: null,
  filterStatus: '',
  filterTag: '',
  progress: JSON.parse(localStorage.getItem('trainer-progress') || '{}'),
};

const el = (s) => document.querySelector(s);
const cardsEl = el('#cards');

const saveProgress = () =>
  localStorage.setItem('trainer-progress', JSON.stringify(state.progress));

const questKey = (scrollId, idx) => `${scrollId}::${idx}`;

const setQuestDone = (scrollId, idx, done) => {
  state.progress[questKey(scrollId, idx)] = !!done;
  saveProgress();
  render();
  track('quest_toggled', { scrollId, idx, done: !!done });
};

const filtered = () => (state.raw || []).filter((s) => {
  const okStatus = !state.filterStatus || s.status === state.filterStatus;
  const okTag = !state.filterTag || (s.tags || [])
    .some((t) => `#${t}`.toLowerCase().includes(state.filterTag.toLowerCase().replace(/^#/, '')));
  return okStatus && okTag;
});

const pctComplete = (s) => {
  const total = (s.quests || []).length || 0;
  if (!total) return 0;
  let done = 0;
  s.quests.forEach((q, i) => { if (state.progress[questKey(s.id, i)]) done++; });
  return Math.round((done / total) * 100);
};

const render = () => {
  const list = filtered();
  cardsEl.innerHTML = list.map((s) => `
    <article class="card" data-id="${s.id}">
      <h2>${s.glyph || ''} ${s.title}</h2>
      <div class="meta">
        <div>
          <span class="pill">status: ${s.status}</span>
          <span class="pill">xp: ${s.xp || 0}</span>
        </div>
        <div>${s.start || ''} → ${s.due || ''} · ${pctComplete(s)}%</div>
      </div>
      <div style="margin-top:8px">Orbit: <strong>${s.orbit || '—'}</strong></div>
      <div style="margin-top:6px">${(s.tags || []).map((t) => `<span class="tag">#${t}</span>`).join('')}</div>
      <ul class="quests">
        ${(s.quests || []).map((q, i) => {
          const done = !!state.progress[questKey(s.id, i)];
          return `
            <li data-idx="${i}">
              <label>
                <input type="checkbox" ${done ? 'checked' : ''} data-scroll="${s.id}" data-quest="${i}" />
                <span class="${done ? 'done' : ''}">${q.label}</span>
              </label>
              ${q.timebox_min ? `<span class="pill" title="timebox">${q.timebox_min}m</span>` : ''}
              ${q.artifact ? ` · <a href="${q.artifact}" target="_blank" rel="noopener">artifact</a>` : ''}
            </li>`;
        }).join('')}
      </ul>
      ${s.ritual ? `<div class="meta"><div>Ritual: ${s.ritual.cadence || '—'}</div><div>Streak goal: ${s.ritual.streak_goal || '—'}</div></div>` : ''}
      <div style="margin-top:10px">
        <button data-action="open" data-scroll="${s.id}">Open</button>
        <button data-action="share" data-scroll="${s.id}">Share</button>
      </div>
    </article>`).join('');
};

const loadYaml = async () => {
  try {
    const res = await fetch('./data/scrolls.yml', { cache: 'no-store' });
    if (!res.ok) throw new Error('Failed to load scrolls.yml');
    const text = await res.text();
    const doc = jsyaml.load(text);
    if (!Array.isArray(doc)) throw new Error('YAML root must be a list');
    state.raw = doc;
    render();
    track('trainer_loaded', { count: doc.length });
  } catch (err) {
    cardsEl.innerHTML = `<div class="card"><strong>Could not load scrolls:</strong><br>${err.message}</div>`;
    track('trainer_error', { message: String(err) });
  }
};

// UI wiring
document.addEventListener('change', (e) => {
  const cb = e.target;
  if (cb && cb.matches('input[type="checkbox"][data-scroll]')) {
    const sid = cb.getAttribute('data-scroll');
    const idx = Number(cb.getAttribute('data-quest'));
    setQuestDone(sid, idx, cb.checked);
  }
});

document.addEventListener('click', (e) => {
  const b = e.target.closest('button[data-action]');
  if (!b) return;
  const action = b.getAttribute('data-action');
  const sid = b.getAttribute('data-scroll');
  track(`scroll_${action}`, { scrollId: sid });
  if (action === 'share') {
    const url = location.href;
    navigator.clipboard?.writeText(url);
    b.textContent = 'Copied link';
    setTimeout(() => (b.textContent = 'Share'), 1200);
  }
  if (action === 'open') {
    document.querySelector(`[data-id="${sid}"]`)?.scrollIntoView({ behavior: 'smooth' });
  }
});

// Filters
el('#statusFilter').addEventListener('input', (e) => { state.filterStatus = e.target.value; render(); });
el('#tagFilter').addEventListener('input', (e) => { state.filterTag = e.target.value; render(); });
el('#resetBtn').addEventListener('click', () => {
  state.filterStatus = '';
  state.filterTag = '';
  el('#statusFilter').value = '';
  el('#tagFilter').value = '';
  render();
});

loadYaml();
