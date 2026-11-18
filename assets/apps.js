/* Progressive filters: default HTML remains browsable without JavaScript. */
(() => {
  const root = document.querySelector('.mode-apps');
  if (!root) return;
  const search = root.querySelector('#app-search');
  const buttons = [...root.querySelectorAll('[data-filter]')];
  const cards = [...root.querySelectorAll('[data-app-category]')];
  const empty = root.querySelector('#apps-empty');
  if (!search || !buttons.length || !cards.length) return;
  let category = 'all';
  const update = () => {
    const term = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    for (const card of cards) {
      const matches = (category === 'all' || card.dataset.appCategory === category) && (!term || card.textContent.toLocaleLowerCase().includes(term));
      card.hidden = !matches;
      if (matches) visible++;
    }
    empty.hidden = visible !== 0;
  };
  buttons.forEach(button => button.addEventListener('click', () => {
    category = button.dataset.filter;
    buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    update();
  }));
  search.addEventListener('input', update);
})();
