import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';
import path from 'path';
import fs from 'fs';

const { chromium } = pkg;
const __dirname = path.dirname(fileURLToPath(import.meta.url));

const variants = [
  {
    html: 'brochure.html',
    pdf: 'Vida_Dubai_Mall_T1_3BR_Brochure_Landscape.pdf',
    width: '297mm',
    height: '210mm',
  },
  {
    html: 'brochure-portrait.html',
    pdf: 'Vida_Dubai_Mall_T1_3BR_Brochure_Portrait.pdf',
    width: '210mm',
    height: '297mm',
  },
];

const browser = await chromium.launch();
const context = await browser.newContext();

for (const v of variants) {
  const page = await context.newPage();
  const htmlPath = path.join(__dirname, v.html);
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(2000);

  const rawPdf = path.join(__dirname, `.raw-${v.html}.pdf`);
  const outPdf = path.join(__dirname, v.pdf);

  await page.pdf({
    path: rawPdf,
    width: v.width,
    height: v.height,
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
    preferCSSPageSize: true,
  });

  await page.close();

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
  console.log(`${v.pdf}: ${sizeKB} KB`);
}

await browser.close();
console.log('Done.');
