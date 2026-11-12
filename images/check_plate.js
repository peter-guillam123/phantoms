// Checks that the words on the home page's dark plate can be read over
// every ghost picture, on a phone and a desktop.
//
// It opens the built home page, steps through the ten lines, and for each
// one looks at the picture directly behind every piece of text. It takes
// the brightest patch there and works out the contrast with the text.
// Small text must reach 4.5:1 and the big title and line 3:1.
//
// Run it after adding or changing a picture in images/ghosts/:
//
//     python3 images/make_faint.py
//     python3 build.py
//     node images/check_plate.js
//
// It needs Playwright, which is not part of the site build.

const { chromium } = require("playwright");
const path = require("path");

const page_url = "file://" + path.resolve(__dirname, "..", "_site", "index.html");
const TEXTS = [
  [".hero .eyebrow", 4.5],
  [".hero h1", 3],
  [".hero .turn-lead", 4.5],
  [".hero .turn-phrase", 3],
  [".hero .turn-by", 4.5],
  [".hero .turn-toggle", 4.5],
];

function luminance([r, g, b]) {
  const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
}

(async () => {
  const browser = await chromium.launch();
  let failures = 0;
  for (const [label, width, height] of [["phone", 390, 844], ["desktop", 1280, 900]]) {
    const ctx = await browser.newContext({ viewport: { width, height }, reducedMotion: "reduce", deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    const reader = await ctx.newPage();
    await page.goto(page_url);
    const count = await page.locator(".turn-source li").count();
    for (let i = 0; i < count; i++) {
      if (i > 0) await page.click("[data-turn-toggle]");
      const who = await page.textContent("[data-turn-by]");
      const has = await page.evaluate((n) => !!document.querySelectorAll(".turn-source li")[n].getAttribute("data-ghost"), i);
      if (!has) continue;
      await page.waitForFunction(() => {
        const img = document.querySelector("[data-turn-plate] img.is-shown");
        return img && img.complete && img.naturalWidth > 0;
      });
      // Where each piece of text is, and what colour it is.
      const boxes = await page.evaluate((texts) => texts.map(([sel, need]) => {
        const el = document.querySelector(sel);
        // The words themselves, not the full-width box they sit in.
        const range = document.createRange();
        range.selectNodeContents(el);
        const r = range.getBoundingClientRect();
        const c = getComputedStyle(el).color.match(/[\d.]+/g).slice(0, 3).map(Number);
        return { sel, need, x: r.x, y: r.y, w: r.width, h: r.height, color: c };
      }), TEXTS);
      // The plate with the words hidden.
      await page.addStyleTag({ content: ".hero > :not(.hero-plate) { visibility: hidden !important; }" }).then((tag) => tag.evaluate((el) => el.setAttribute("data-check", "")));
      const shot = await page.screenshot({ type: "png" });
      await page.evaluate(() => document.querySelectorAll("style[data-check]").forEach((el) => el.remove()));
      // The brightest 6px patch behind each box.
      const brightest = await reader.evaluate(async ({ data, boxes }) => {
        const img = new Image();
        img.src = "data:image/png;base64," + data;
        await img.decode();
        const canvas = document.createElement("canvas");
        canvas.width = img.width; canvas.height = img.height;
        const g = canvas.getContext("2d");
        g.drawImage(img, 0, 0);
        return boxes.map((b) => {
          const x0 = Math.max(0, Math.floor(b.x)), y0 = Math.max(0, Math.floor(b.y));
          const w = Math.min(canvas.width - x0, Math.ceil(b.w)), h = Math.min(canvas.height - y0, Math.ceil(b.h));
          if (w < 6 || h < 6) return [0, 0, 0];
          const px = g.getImageData(x0, y0, w, h).data;
          let best = [0, 0, 0], bestSum = -1;
          for (let y = 0; y + 6 <= h; y += 3) for (let x = 0; x + 6 <= w; x += 3) {
            let s = [0, 0, 0];
            for (let dy = 0; dy < 6; dy++) for (let dx = 0; dx < 6; dx++) {
              const k = ((y + dy) * w + (x + dx)) * 4;
              s[0] += px[k]; s[1] += px[k + 1]; s[2] += px[k + 2];
            }
            const sum = s[0] + s[1] + s[2];
            if (sum > bestSum) { bestSum = sum; best = s.map((v) => v / 36); }
          }
          return best;
        });
      }, { data: shot.toString("base64"), boxes });
      const parts = boxes.map((b, k) => {
        const lt = luminance(b.color), lb = luminance(brightest[k]);
        const ratio = (Math.max(lt, lb) + 0.05) / (Math.min(lt, lb) + 0.05);
        const ok = ratio >= b.need;
        if (!ok) failures++;
        return `${b.sel.replace(".hero ", "")} ${ratio.toFixed(1)}${ok ? "" : " FAILS (needs " + b.need + ")"}`;
      });
      console.log(`${label}: ${who}\n    ${parts.join(", ")}`);
    }
    await ctx.close();
  }
  await browser.close();
  console.log(failures ? `\n${failures} piece(s) of text too faint.` : "\nAll text passes.");
  process.exit(failures ? 1 : 0);
})();
