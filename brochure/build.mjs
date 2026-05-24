import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
import { fileURLToPath } from 'url';
import path from 'path';

const { chromium } = pkg;
const __dirname = path.dirname(fileURLToPath(import.meta.url));

const browser = await chromium.launch();
const context = await browser.newContext();
const page = await context.newPage();

const htmlPath = path.join(__dirname, 'brochure.html');
await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(2500);

await page.pdf({
  path: path.join(__dirname, 'Vida_Dubai_Mall_T1_3BR_Brochure.pdf'),
  width: '297mm',
  height: '210mm',
  printBackground: true,
  margin: { top: 0, right: 0, bottom: 0, left: 0 },
  preferCSSPageSize: true,
});

await browser.close();
console.log('PDF generated.');
