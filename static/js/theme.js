const toggle = document.getElementById('theme-toggle');
function applyTheme(theme) {
  if (theme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
    toggle.textContent = 'روشن';
  } else {
    document.documentElement.removeAttribute('data-theme');
    localStorage.setItem('theme', 'light');
    toggle.textContent = 'تاریک';
  }
}
const saved = localStorage.getItem('theme') || 'light';
applyTheme(saved);
toggle.addEventListener('click', () => {
  const cur = localStorage.getItem('theme') || 'light';
  applyTheme(cur === 'light' ? 'dark' : 'light');
});
