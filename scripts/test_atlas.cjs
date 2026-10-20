// Browser behavior checks for the generated, offline atlas.
// Requires Playwright. Set CHROMIUM_PATH to use an existing Chromium binary.
const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");
(async () => {
  const root = path.resolve(__dirname, "..");
  const out = path.join(root, ".cache/browser");
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({
    headless: true,
    ...(process.env.CHROMIUM_PATH
      ? { executablePath: process.env.CHROMIUM_PATH }
      : {}),
    args: ["--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"],
  });
  const page = await browser.newPage({
    viewport: { width: 1440, height: 1080 },
  });
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  const file = "file://" + path.join(root, "docs/index.html");
  for (const lang of ["en", "zh"]) {
    await page.goto(file + "?lang=" + lang);
    await page.evaluate(() => document.fonts.ready);
    assert.equal(await page.locator(".route-card").count(), 3);
    await page.keyboard.press("Tab");
    assert.equal(
      await page.locator(".skip").evaluate((e) => e === document.activeElement),
      true,
    );
    await page.keyboard.press("Enter");
    assert.equal(
      await page.locator("#main").evaluate((e) => e === document.activeElement),
      true,
    );
    assert.equal(await page.locator(".route-card").count(), 3);
    await page.screenshot({ path: path.join(out, `overview-${lang}.png`) });
    for (const route of ["harness", "model", "hybrid"]) {
      await page.goto(file + "?lang=" + lang + "#route=" + route);
      assert.equal(
        await page.locator(".map-node").count(),
        route === "hybrid" ? 9 : 10,
      );
      await page.locator(".map-node").nth(2).click();
      assert.ok((await page.locator("#node-detail .mini-list a").count()) > 0);
    }
    await page.screenshot({ path: path.join(out, `route-${lang}.png`) });
    await page.goto(file + "?lang=" + lang + "#works");
    assert.equal(await page.locator(".work-card").count(), 141);
    await page.locator("#work-search").fill("Promptbreeder");
    assert.ok((await page.locator(".work-card").count()) > 0);
    await page.locator("#clear-filters").click();
    await page.locator("#route-filter").selectOption("model");
    assert.equal(await page.locator(".work-card").count(), 36);
    await page.goto(file + "?lang=" + lang + "#works&route=hybrid");
    assert.equal(await page.locator(".work-card").count(), 22);
    await page.goto(file + "?lang=" + lang + "#work=dgm");
    assert.equal(await page.locator(".article > section").count(), 7);
    await page.locator("#language").click();
    assert.equal(await page.locator(".article > section").count(), 7);
    assert.ok(page.url().endsWith("#work=dgm"));
    await page.goto(file + "?lang=" + lang + "#paper=dgm");
    assert.equal(await page.locator(".article > section").count(), 7);
    await page.goto(file + "?lang=" + lang + "#company=metacircle");
    assert.equal(await page.locator(".work-card").count(), 3);
    await page.goto(file + "?lang=" + lang + "#relations");
    assert.equal(await page.locator(".relation-card").count(), 69);
    await page.locator("#relation-kind").selectOption("extends");
    assert.ok((await page.locator(".relation-card").count()) > 0);
    await page.goto(file + "?lang=" + lang + "#people");
    assert.equal(
      await page.locator("#company-results .actor-card").count(),
      27,
    );
    assert.equal(await page.locator("#actor-results .actor-card").count(), 157);
    await page.locator("#actor-search").fill("Google");
    assert.ok((await page.locator("#actor-results .actor-card").count()) > 0);
    await page.goto(file + "?lang=" + lang + "#learn=A");
    assert.equal(await page.locator(".guide-content tbody tr").count(), 148);
    await page.locator("#guide-search").fill("GRPO");
    assert.ok((await page.locator(".guide-search-results a").count()) >= 3);
    await page.goto(file + "?lang=" + lang + "#learn=11");
    assert.equal(await page.locator(".ml-equation svg").count(), 3);
    await page.screenshot({ path: path.join(out, `manual-${lang}.png`) });
    await page.locator('[data-learn-ref="22"]').first().click();
    await page.waitForSelector("#ml-source-22");
    const downloading = page.waitForEvent("download");
    await page.locator("[data-pdf]").click();
    const download = await downloading;
    const target = path.join(out, `download-${lang}.pdf`);
    await download.saveAs(target);
    assert.ok(
      fs
        .readFileSync(target)
        .equals(
          fs.readFileSync(
            path.join(
              root,
              "docs/Model_LLM_Learning_Manual" +
                (lang === "en" ? ".en" : "") +
                ".pdf",
            ),
          ),
        ),
    );
    await page.setViewportSize({ width: 390, height: 844 });
    for (const hash of [
      "overview",
      "route=harness",
      "work=dgm",
      "learn=25",
      "people",
      "scope",
    ]) {
      await page.goto(file + "?lang=" + lang + "#" + hash);
      const size = await page.evaluate(() => ({
        width: innerWidth,
        body: document.body.scrollWidth,
      }));
      assert.ok(
        size.body <= size.width + 1,
        `${lang}/${hash}: horizontal page overflow ${JSON.stringify(size)}`,
      );
    }
    await page.screenshot({ path: path.join(out, `mobile-${lang}.png`) });
    await page.setViewportSize({ width: 1440, height: 1080 });
  }
  assert.deepEqual(errors, []);
  console.log(
    "Browser checks passed: both languages, 3 maps, 141 works, 69 relations, 27 companies, 157 participants, glossary, search, links, PDF bytes, and mobile overflow.",
  );
  await browser.close();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
