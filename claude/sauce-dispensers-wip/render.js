// Usage: node render.js <url> [maxChars]  -> prints page title, final URL, status and visible text
const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const url = process.argv[2]; const max = parseInt(process.argv[3] || '60000');
  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox','--ignore-certificate-errors'], proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined });
  const ctx = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    locale: 'de-AT', viewport: { width: 1366, height: 900 }, ignoreHTTPSErrors: true });
  const page = await ctx.newPage();
  let status = 'n/a';
  try {
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    status = resp ? resp.status() : 'n/a';
    await page.waitForTimeout(3500);
    // try to accept cookie banners
    for (const sel of ['button#onetrust-accept-btn-handler','button[data-testid="uc-accept-all-button"]','#uc-btn-accept-banner','button:has-text("Alle akzeptieren")','button:has-text("Akzeptieren")','button:has-text("Accept all")','button:has-text("Souhlasím")','button:has-text("Přijmout")','button:has-text("Accept")','button:has-text("Súhlasím")','button:has-text("Accept toate")']) {
      try { const b = page.locator(sel).first(); if (await b.isVisible({timeout: 300})) { await b.click({timeout:1000}); await page.waitForTimeout(800); break; } } catch(e) {}
    }
    const txt = await page.evaluate(() => document.body ? document.body.innerText : '');
    console.log('TITLE: ' + await page.title()); console.log('URL: ' + page.url()); console.log('STATUS: ' + status);
    console.log('--- TEXT ---'); console.log(txt.replace(/\n{3,}/g, '\n\n').slice(0, max));
  } catch (e) { console.log('ERROR: ' + e.message + ' STATUS: ' + status); }
  await browser.close();
})();
