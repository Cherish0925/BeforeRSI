// Browser behavior checks for the generated, offline landscape.
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
  await page.context().setOffline(true);
  const networkRequests = [];
  page.on("request", (request) => {
    if (/^https?:/.test(request.url())) networkRequests.push(request.url());
  });
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  const file = "file://" + path.join(root, "RSI_Field_landscape.html");
  const landscape = JSON.parse(
    fs.readFileSync(path.join(root, "data/landscape.json")),
  );
  async function labelsFit(selector) {
    await page.evaluate(() => document.fonts.ready);
    const clipped = await page.locator(selector).evaluateAll((cards) =>
      cards.flatMap((card) => {
        const rect = card.querySelector("rect").getBBox();
        return [...card.querySelectorAll("text")]
          .filter((text) => {
            const box = text.getBBox();
            return (
              box.x < rect.x ||
              box.x + box.width > rect.x + rect.width + 1 ||
              box.y < rect.y ||
              box.y + box.height > rect.y + rect.height + 1
            );
          })
          .map((text) => text.textContent);
      }),
    );
    assert.deepEqual(clipped, [], `Labels overflow: ${selector}`);
  }
  for (const lang of ["en", "zh"]) {
    await page.goto(file + "?lang=" + lang);
    await page.evaluate(() => document.fonts.ready);
    assert.equal(await page.locator(".field-card").count(), 3);
    assert.equal(await page.locator(".concept-node").count(), 29);
    assert.equal(await page.locator(".concept-link").count(), 60);
    await labelsFit(".concept-node");
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
    assert.equal(await page.locator(".field-card").count(), 3);
    await page.screenshot({ path: path.join(out, `overview-${lang}.png`) });
    for (const route of ["harness", "model", "hybrid"]) {
      await page.goto(file + "?lang=" + lang + "#route=" + route);
      assert.equal(
        await page.locator(".map-node").count(),
        route === "hybrid" ? 9 : 10,
      );
      await page.locator(".map-node").nth(2).click();
      assert.ok((await page.locator("#node-detail .mini-list a").count()) > 0);
      await page.locator(".concept-link").first().press("Enter");
      assert.ok(
        (await page.locator("#node-detail .source-list a").count()) > 0,
      );
      await page.locator("[data-expand-map]").click();
      const r = landscape.field.routes.find((r) => r.id === route);
      assert.equal(
        await page.locator(".field-subtopic").count(),
        r.nodes.reduce((n, x) => n + x.subtopics.length, 0),
      );
      await labelsFit(".concept-node");
      await page.locator("[data-expand-map]").click();
      await page
        .locator(`.mode-bar a[href="#route=${route}&mode=papers"]`)
        .click();
      assert.equal(
        await page.locator(".paper-node").count(),
        { harness: 52, model: 15, hybrid: 13 }[route],
      );
      await labelsFit(".paper-node, .paper-group");
      const width = await page.locator(".paper-network").getAttribute("width");
      await page.locator('[data-zoom="in"]').click();
      assert.ok(
        Number(await page.locator(".paper-network").getAttribute("width")) >
          Number(width),
      );
      await page.locator("[data-method-wires]").click();
      assert.equal(await page.locator(".method-wire").count(), 0);
      await page.locator("[data-reset-paper]").click();
      await page.locator(".paper-node").first().click();
      await page.locator(".domain-inspector [data-open-work]").first().click();
      assert.equal(
        await page.locator("#paper-dialog").evaluate((d) => d.open),
        true,
      );
      assert.ok(
        (await page.locator("#paper-content .article > section").count()) >= 6,
      );
      await page.locator("[data-dialog-language]").click();
      assert.equal(
        await page.locator("html").getAttribute("lang"),
        lang === "en" ? "zh" : "en",
      );
      assert.equal(
        await page.locator("#paper-dialog").evaluate((d) => d.open),
        true,
      );
      await page.locator("[data-dialog-language]").click();
      await page.keyboard.press("Escape");
      assert.equal(
        await page.locator("#paper-dialog").evaluate((d) => d.open),
        false,
      );
      await page.locator(".paper-edge-link").first().press("Enter");
      assert.equal(
        await page.locator(".domain-inspector .relation-card").count(),
        1,
      );
      await page.locator("#map-small").check();
      assert.equal(
        await page.locator(".paper-node").count(),
        r.id === "harness" ? 52 : r.id === "model" ? 36 : 22,
      );
      await page.locator("#paper-group").selectOption({ index: 1 });
      assert.ok((await page.locator(".paper-node").count()) > 0);
      await page.locator("[data-reset-paper]").click();
    }
    await page.screenshot({ path: path.join(out, `route-${lang}.png`) });
    await page.goto(file + "?lang=" + lang + "#participants");
    assert.equal(await page.locator(".actor-matrix tbody tr").count(), 4);
    assert.equal(await page.locator(".participant-table tbody tr").count(), 18);
    await page.locator('[data-participant-page="2"]').click();
    assert.equal(
      await page
        .locator("#participant-results .result-pager span")
        .textContent(),
      "2 / 9",
    );
    await page.locator("#participant-query").fill("Google");
    assert.ok((await page.locator(".participant-table tbody tr").count()) > 0);
    await page.locator('.actor-matrix a[href*="kind=all&route=model"]').click();
    assert.match(
      await page.locator("#participant-results > .quiet").textContent(),
      /^36 /,
    );
    await page.goto(file + "?lang=" + lang + "#guide");
    assert.equal(await page.locator(".guide-case-tabs a").count(), 6);
    await page.locator(".guide-case-tabs a").nth(3).click();
    assert.equal(await page.locator(".case-details dt").count(), 8);
    await page.goto(file + "?lang=" + lang + "#discovery");
    assert.match(
      await page.locator("#lead-results > .quiet").textContent(),
      /^567 /,
    );
    await page.locator('[data-lead-filter="scope_candidate"]').click();
    assert.match(
      await page.locator("#lead-results > .quiet").textContent(),
      /^240 /,
    );
    await page.locator('[data-lead-page="2"]').click();
    assert.equal(
      await page.locator("#lead-results .result-pager span").textContent(),
      "2 / 20",
    );
    await page.locator("#lead-filter").selectOption("all");
    await page.locator("#lead-query").fill("Darwin");
    assert.ok((await page.locator(".lead-entry").count()) > 0);
    await page.locator(".lead-entry > summary").first().click();
    assert.ok(
      (await page.locator(".lead-entry[open] > p").first().textContent())
        .length > 0,
    );
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
      "route=model&mode=papers",
      "participants",
      "guide",
      "discovery",
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
  assert.deepEqual(
    networkRequests,
    [],
    "Local reading must not require network requests",
  );
  console.log(
    "Browser checks passed: both languages, 3 mechanism maps and research graphs, expanded subquestions, filters, dialogs, 141 works, 69 relations, 27 companies, 157 participants, 567 discovery entries, glossary, search, links, PDF bytes, labels, and mobile overflow.",
  );
  await browser.close();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
