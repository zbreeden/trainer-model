// Reuse across modules to standardize analytics
window.dataLayer = window.dataLayer || [];
export const track = (event, params = {}) => {
window.dataLayer.push({ event, ts: Date.now(), ...params });
};

const MOD = document.querySelector('meta[name="ft-module"]')?.content;
export const track = (event, params = {}) => {
  const base = { event, ts: Date.now(), ...(MOD ? { module: MOD } : {}) };
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({ ...base, ...params });
};

track('trainer_loaded', { count: 2 });                          // on YAML load
track('scroll_open',    { scrollId: 'cbap-cert' });             // on Open
track('quest_toggled',  { scrollId: 'gtm-ga4-sprint', idx: 1, done: true });
track('scroll_share',   { scrollId: 'ibm-data-science-cert' }); // on Share
track('nav_back',       { to: 'sandbox' });                     // back link
