/* All asset paths are relative so the site also works under /repository-name/. */
'use strict';
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-nav');
function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  navigation.classList.remove('is-open');
}
menuButton.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('is-open', open);
});
navigation.addEventListener('click', (event) => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', (event) => { if (event.key === 'Escape') closeMenu(); });
window.matchMedia('(min-width: 801px)').addEventListener('change', closeMenu);

const dialog = document.querySelector('#video-dialog');
const player = document.querySelector('#tutorial-player');
const videoError = document.querySelector('#video-error');
let videoTrigger;
document.querySelectorAll('[data-video]').forEach((button) => {
  button.addEventListener('click', () => {
    const number = button.dataset.video;
    const labels = {1:'一', 2:'二', 3:'三'};
    videoTrigger = button;
    document.querySelector('#video-title').textContent = `EViews 操作教程 · ${labels[number]}`;
    player.src = `assets/videos/eviews-${number}.mp4`;
    player.poster = `assets/poster-${number}.jpg`;
    document.querySelector('#video-direct').href = player.src;
    videoError.hidden = true;
    dialog.showModal();
    document.body.classList.add('modal-open');
    // Deliberately no autoplay or play(): playback requires the native play control.
  });
});
document.querySelector('#close-video').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', (event) => {
  const rect = dialog.getBoundingClientRect();
  if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
});
dialog.addEventListener('close', () => {
  player.pause();
  player.removeAttribute('src');
  player.load();
  document.body.classList.remove('modal-open');
  videoTrigger?.focus();
});
player.addEventListener('error', () => { if (player.hasAttribute('src')) videoError.hidden = false; });
document.querySelector('#copy-email').addEventListener('click', async () => {
  const status = document.querySelector('#copy-status');
  try {
    await navigator.clipboard.writeText('1932370757@qq.com');
    status.textContent = '邮箱已复制';
  } catch {
    status.textContent = '暂时无法自动复制，请选中左侧邮箱手动复制。';
  }
});
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      navigation.querySelectorAll('a').forEach((link) => {
        if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    });
  }, {rootMargin:'-15% 0px -60% 0px'});
  document.querySelectorAll('main section[id]').forEach((section) => observer.observe(section));
}
