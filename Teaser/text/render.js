// Rendert die Text-Ebenen des Leonard-Teasers als transparente PNGs in voller Bildgröße (Skill social-teaser-video).
// Aufruf auf dem VPS: node text/render.js
const { chromium } = require('/opt/karakeep/node_modules/playwright-core');
const path = require('path');

const FORMATS = { '16x9': { w: 1920, h: 1080, y: 800 } };

const CSS = `
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800&family=Bangers&family=Manrope:wght@600&display=block');
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { background: transparent; }
body { width: var(--w); height: var(--h); position: relative; color: #f4f1ea; }
.block { position: absolute; left: 120px; right: 120px; text-align: center; }
.tag { font-family: Cinzel, serif; font-weight: 800; letter-spacing: 0.12em; white-space: nowrap; text-transform: uppercase;
  text-shadow: 0 4px 30px rgba(0,0,0,0.9), 0 1px 3px rgba(0,0,0,0.95); }
.gold { color: #f2c14e; }
.title { font-family: Bangers, cursive; letter-spacing: 0.04em; color: #f2c14e; line-height: 0.95;
  -webkit-text-stroke: 4px #0b1a10; text-shadow: 0 8px 0 #0b1a10, 0 12px 40px rgba(0,0,0,0.8); }
.sub { font-family: Cinzel, serif; font-weight: 800; letter-spacing: 0.5em; text-transform: uppercase;
  text-shadow: 0 0 18px rgba(0,0,0,1), 0 3px 24px rgba(0,0,0,1), 0 0 4px rgba(0,0,0,1); }
.rule { width: 160px; height: 3px; background: #f2c14e; margin: 22px auto; }
`;

function blocks(f) {
  return {
    tA: `<div class="block" style="top:${f.y}px"><div class="tag" style="font-size:60px">In einer Welt voller Gefahren …</div></div>`,
    tB: `<div class="block" style="top:${f.y}px"><div class="tag" style="font-size:60px">… braucht es <span class="gold">Helden</span>.</div></div>`,
    tC: `<div class="block" style="top:${f.y}px"><div class="tag" style="font-size:60px">Diesmal ist es <span class="gold">Familiensache</span>.</div></div>`,
    ti: `<div class="block" style="top:300px"><div class="title" style="font-size:230px">LEONARD</div>
           <div class="rule"></div><div class="sub" style="font-size:66px">der Superheld</div></div>`,
    en: `<div class="block" style="top:420px"><div class="title" style="font-size:170px">BALD.</div>
           <div class="sub" style="font-size:36px;margin-top:26px;letter-spacing:0.4em">Nur im Familienkino</div></div>`
  };
}

(async () => {
  const browser = await chromium.launch({ executablePath: '/usr/bin/chromium', args: ['--no-sandbox'] });
  for (const [name, f] of Object.entries(FORMATS)) {
    const page = await browser.newPage({ viewport: { width: f.w, height: f.h } });
    for (const [id, html] of Object.entries(blocks(f))) {
      await page.setContent(`<html><head><style>${CSS}</style></head>
        <body style="--w:${f.w}px;--h:${f.h}px">${html}</body></html>`, { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      await page.screenshot({ path: path.join(__dirname, `${name}_${id}.png`), omitBackground: true });
    }
    await page.close();
  }
  await browser.close();
})();
