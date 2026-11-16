(() => {
  const disclosure = document.querySelector('.toc-disclosure');
  if (!disclosure) return;
  const mobile = window.matchMedia('(max-width: 760px)');
  const setLayout = () => { disclosure.open = !mobile.matches; };
  setLayout();
  mobile.addEventListener('change', setLayout);
  const links = [...document.querySelectorAll('.toc-list a[href^="#"]')];
  const headings = links.map(link => document.getElementById(link.hash.slice(1))).filter(Boolean);
  let scheduled = false;
  function update() {
    scheduled = false;
    let current = headings[0];
    for (const heading of headings) {
      if (heading.getBoundingClientRect().top <= 140) current = heading;
    }
    for (const link of links) {
      const active = current && link.hash === '#' + current.id;
      if (active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    }
    document.querySelectorAll('.toc-group').forEach(group => {
      group.classList.toggle('contains-current', Boolean(group.querySelector('[aria-current="location"]')));
    });
  }
  function revealHash() {
    const link = links.find(link => link.hash === window.location.hash);
    const group = link && link.closest('.toc-group details');
    if (group) group.open = true;
  }
  window.addEventListener('hashchange', () => { revealHash(); update(); });
  window.addEventListener('scroll', () => {
    if (!scheduled) { scheduled = true; requestAnimationFrame(update); }
  }, { passive: true });
  window.addEventListener('resize', update);
  document.querySelectorAll('.toc a').forEach(link => link.addEventListener('click', () => {
    if (mobile.matches) disclosure.open = false;
  }));
  revealHash();
  update();
})();
