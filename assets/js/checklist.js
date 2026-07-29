(function() {
  const STORAGE_KEY = 'tseo-checklist-progress';
  let totalItems = 0;
  let checkedItems = 0;

  function loadProgress() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      return saved ? JSON.parse(saved) : {};
    } catch { return {}; }
  }

  function saveProgress(progress) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
    } catch {}
  }

  function updateUI() {
    const fill = document.querySelector('.progress-bar-fill');
    const text = document.querySelector('.progress-text');
    if (!fill || !text) return;

    const items = document.querySelectorAll('.checklist-item');
    totalItems = items.length;
    checkedItems = document.querySelectorAll('.checklist-item.checked').length;

    const pct = totalItems ? Math.round((checkedItems / totalItems) * 100) : 0;
    fill.style.width = pct + '%';
    text.innerHTML = checkedItems + ' of ' + totalItems + ' completed <span>(' + pct + '%)</span>';
  }

  function toggleItem(item, progress) {
    const id = item.dataset.id;
    if (!id) return;

    if (item.classList.contains('checked')) {
      item.classList.remove('checked');
      delete progress[id];
    } else {
      item.classList.add('checked');
      progress[id] = true;
    }

    saveProgress(progress);
    updateUI();
  }

  function init() {
    const items = document.querySelectorAll('.checklist-item');
    if (!items.length) return;

    const progress = loadProgress();

    items.forEach(function(item, index) {
      if (!item.dataset.id) {
        item.dataset.id = 'item-' + index;
      }

      const id = item.dataset.id;

      if (progress[id]) {
        item.classList.add('checked');
      }

      item.addEventListener('click', function(e) {
        if (e.target.closest('.expand-btn') || e.target.closest('.checklist-code')) return;
        toggleItem(item, progress);
      });

      const checkbox = item.querySelector('.checkbox-custom');
      if (checkbox) {
        checkbox.addEventListener('click', function(e) {
          e.stopPropagation();
          toggleItem(item, progress);
        });
      }

      const expandBtn = item.querySelector('.expand-btn');
      if (expandBtn) {
        expandBtn.addEventListener('click', function(e) {
          e.stopPropagation();
          item.classList.toggle('expanded');
          expandBtn.textContent = item.classList.contains('expanded') ? 'Hide code' : 'Show code';
        });
      }
    });

    updateUI();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
