// Reuse across modules to standardize analytics
window.dataLayer = window.dataLayer || [];
export const track = (event, params = {}) => {
window.dataLayer.push({ event, ts: Date.now(), ...params });
};
