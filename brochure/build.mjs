import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';
import path from 'path';
import fs from 'fs';

const { chromium } = pkg;
const __dirname = path.dirname(fileURLToPath(import.meta.url));

const browser = await chromium.launch();
const context = await browser.newContext();
const page = await context.newPage();

const htmlPath = path.join(__dirname, 'brochure.html');
await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(2500);

const rawPdf = path.join(__dirname, '.raw.pdf');
const outPdf = path.join(__dirname, 'Vida_Dubai_Mall_T1_3BR_Brochure.pdf');

await page.pdf({
  path: rawPdf,
  width: '297mm',
  height: '210mm',
  printBackground: true,
  margin: { top: 0, right: 0, bottom: 0, left: 0 },
  preferCSSPageSize: true,
});

await browser.close();

execSync(
  `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/printer ` +
  `-dNOPAUSE -dQUIET -dBATCH -dDetectDuplicateImages -dCompressFonts=true ` +
  `-dDownsampleColorImages=true -dColorImageResolution=300 ` +
  `-dDownsampleGrayImages=true -dGrayImageResolution=300 ` +
  `-sOutputFile="${outPdf}" "${rawPdf}"`,
  { stdio: 'inherit' }
);
fs.unlinkSync(rawPdf);

const sizeKB = Math.round(fs.statSync(outPdf).size / 1024);
console.log(`PDF generated: ${sizeKB} KB`);
