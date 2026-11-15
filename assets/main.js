'use strict';
document.documentElement.classList.add('js');

const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.site-nav');
const closeMenu = () => {
  if (!menuButton || !navigation) return;
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.setAttribute('aria-label', 'Open navigation');
  navigation.classList.remove('is-open');
};
if (menuButton && navigation) {
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    navigation.classList.toggle('is-open', open);
  });
  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) closeMenu();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      menuButton.focus();
    }
  });
  document.addEventListener('click', (event) => {
    if (!event.target.closest('.site-header')) closeMenu();
  });
  window.matchMedia('(min-width: 601px)').addEventListener('change', closeMenu);
}

const filterButtons = [...document.querySelectorAll('[data-filter]')];
const projects = [...document.querySelectorAll('[data-project-group]')];
const filterStatus = document.querySelector('#filter-status');
filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    filterButtons.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
    projects.forEach((item) => { item.hidden = filter !== 'all' && item.dataset.projectGroup !== filter; });
    const featuredVisible = projects.some((item) => item.classList.contains('project-card') && !item.hidden);
    const moreVisible = projects.some((item) => item.classList.contains('project-row') && !item.hidden);
    document.querySelector('.project-grid').hidden = !featuredVisible;
    document.querySelector('.more-work').hidden = !moreVisible;
    const visible = projects.filter((item) => !item.hidden).length;
    if (filterStatus) filterStatus.textContent = filter === 'all' ? `Showing all ${visible} projects` : `Showing ${visible} ${visible === 1 ? 'project' : 'projects'}`;
  });
});

const copyButton = document.querySelector('.copy-email');
const copyStatus = document.querySelector('.copy-status');
let copyTimer;
if (copyButton) {
  copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText('sangambaral9@gmail.com');
      copyStatus.textContent = 'Email copied';
    } catch {
      copyStatus.textContent = 'sangambaral9@gmail.com';
    }
    clearTimeout(copyTimer);
    copyTimer = setTimeout(() => { copyStatus.textContent = ''; }, 5000);
  });
}

const timeElement = document.querySelector('[data-local-time]');
if (timeElement) {
  const updateTime = () => {
    try {
      timeElement.textContent = new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Kathmandu', hour: '2-digit', minute: '2-digit', hour12: false }).format(new Date()) + ' NPT';
    } catch { timeElement.textContent = 'UTC +05:45'; }
  };
  updateTime();
  setInterval(updateTime, 60000);
}

const quietButton = document.querySelector('.cinema-button');
if (quietButton) {
  quietButton.addEventListener('click', () => {
    const quiet = quietButton.getAttribute('aria-pressed') !== 'true';
    quietButton.setAttribute('aria-pressed', String(quiet));
    quietButton.closest('.cinema-frame').classList.toggle('is-quiet', quiet);
    quietButton.replaceChildren(document.createTextNode(quiet ? 'Leave quiet view ' : 'Enter quiet view '));
    const icon = document.createElement('span');
    icon.setAttribute('aria-hidden', 'true');
    icon.textContent = quiet ? '↙' : '⤢';
    quietButton.append(icon);
  });
}

const shareButton = document.querySelector('.share-page');
const shareStatus = document.querySelector('.share-status');
if (shareButton && shareStatus) {
  shareButton.addEventListener('click', async () => {
    const pageUrl = document.querySelector('link[rel="canonical"]').href;
    try {
      await navigator.clipboard.writeText(pageUrl);
      shareStatus.textContent = 'Page link copied. Thanks for sharing.';
    } catch {
      shareStatus.textContent = pageUrl;
    }
  });
}
