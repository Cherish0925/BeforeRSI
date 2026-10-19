/* Offline functional checks. Set CHROMIUM_PATH to add real-browser interaction checks. */
const fs=require('fs'),vm=require('vm'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'..'),file=path.join(root,'research/atlas/index.html');
const html=fs.readFileSync(file,'utf8'),scripts=[...html.matchAll(/<script(?:[^>]*)>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
const data=JSON.parse(scripts[0]),nodes={};
const node=id=>nodes[id]??={innerHTML:'',textContent:'',value:'',open:false,scrollTop:0,scrollLeft:0,handlers:{},classList:{toggle(){}},addEventListener(k,f){this.handlers[k]=f},showModal(){this.open=true},close(){this.open=false}};
node('literature-data').textContent=scripts[0];const events={};
const ctx=vm.createContext({URLSearchParams,document:{getElementById:node,querySelectorAll:()=>[],addEventListener:(k,f)=>events[k]=f},window:{location:{hash:''},scrollTo(){}}});
vm.runInContext(scripts[1],ctx);const run=s=>vm.runInContext(s,ctx);
assert.equal((nodes.main.innerHTML.match(/class="route-card"/g)||[]).length,3);
for(const r of data.routes){
 run(`setPage('${r.id}')`);assert.equal(run('selectedWorks().length'),r.counts.catalog-r.counts.small);
 run('state.small=true;drawGraph()');assert.equal(run('selectedWorks().length'),r.counts.catalog);
 run("state.status='methods';drawGraph()");assert.equal(run('selectedWorks().length'),r.counts.methods);
 run("state.small=false;state.status='all'");
}
run("setPage('search')");assert.equal(run('searchWorks().length'),127);
run("state.query='伯克利'");assert(run('searchWorks().length')>2);
run("state.query='EURISKO'");assert.equal(run('searchWorks()[0].id'),'eurisko');
for(const w of data.works){run(`openPaper(${JSON.stringify(w.id)})`);assert(nodes['paper-content'].innerHTML.includes('id="paper-title"'));assert(nodes['paper-content'].innerHTML.includes(w.primary_url));}
run("openPaper('eurisko')");assert(nodes['paper-content'].innerHTML.includes('带槽位'));assert(!nodes['paper-content'].innerHTML.includes('既有操作记录'));
for(const e of data.relations){run(`selectEdge('${e.id}')`);assert(nodes.inspector.innerHTML.includes(e.sources[0].url));}
run("locate('skillrl')");assert.equal(run('state.small'),true);assert.equal(run('state.selected'),'skillrl');
assert(!/<script[^>]+src=|<link[^>]+href=/.test(html));assert(!/\bfetch\(/.test(scripts[1]));
console.log('PASS: three routes, scope/size filters, all 127 cards, 43 relationships, search aliases and offline payload.');
if(process.env.CHROMIUM_PATH)(async()=>{
 const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
 const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('file://'+file);
 assert.equal(await page.locator('.route-card').count(),3);
 for(const r of data.routes){await page.locator(`nav [data-nav="${r.id}"]`).click();assert.equal(await page.locator('.graph-svg .work').count(),r.counts.catalog-r.counts.small);if(r.counts.small){await page.locator('#small-filter').check();assert.equal(await page.locator('.graph-svg .work').count(),r.counts.catalog);await page.locator('#small-filter').uncheck();}}
 await page.locator('nav [data-nav="harness"]').click();
 await page.locator('.graph-svg [data-node="gepa"]').click();assert((await page.locator('#inspector').innerText()).includes('GEPA'));
 await page.locator('#inspector [data-paper="gepa"]').click();assert(await page.locator('#paper-dialog').isVisible());await page.keyboard.press('Escape');assert(!(await page.locator('#paper-dialog').isVisible()));
 await page.locator('#global-search').fill('EURISKO');await page.locator('#search-form button').click();assert.equal(await page.locator('.result-card').count(),1);
 await page.locator('.result-card h3 a').click();assert.equal(await page.locator('.axis').count(),6);await page.locator('[data-close]').click();
 await page.locator('[data-clear-search]').click();assert.equal(await page.locator('.result-card').count(),127);
 await page.locator('#search-route').selectOption('hybrid');assert.equal(await page.locator('.result-card').count(),25);
 await page.locator('nav [data-nav="overview"]').click();await page.locator('[data-edge="rel-001"]').click();assert((await page.locator('#inspector').innerText()).includes('DGM-H'));
 const outputs=process.env.ATLAS_SCREENSHOTS;
 if(outputs){fs.mkdirSync(outputs,{recursive:true});await page.locator('nav [data-nav="overview"]').click();await page.screenshot({path:path.join(outputs,'landscape-overview.png'),fullPage:true});
  for(const route of ['harness','model','hybrid']){await page.locator(`nav [data-nav="${route}"]`).click();
   const svg=await page.locator('.graph-svg').evaluate(s=>{const copy=s.cloneNode(true);copy.setAttribute('width',copy.viewBox.baseVal.width);copy.setAttribute('height',copy.viewBox.baseVal.height);const st=document.createElementNS('http://www.w3.org/2000/svg','style');st.textContent=[...document.styleSheets].flatMap(x=>[...x.cssRules]).filter(x=>x.cssText.startsWith('.graph-svg')||x.cssText.startsWith('.edge-hit')||x.cssText.startsWith('.topic')).map(x=>x.cssText).join('\n');copy.prepend(st);return new XMLSerializer().serializeToString(copy)});
   fs.writeFileSync(path.join(outputs,route+'-graph.svg'),svg);
  }
 }
 await page.setViewportSize({width:390,height:844});await page.locator('nav [data-nav="harness"]').click();assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
 await page.locator('.graph-svg [data-node="gepa"]').click();await page.locator('#inspector [data-paper="gepa"]').click();assert(await page.evaluate(()=>document.querySelector('#paper-dialog').scrollWidth<=document.querySelector('#paper-dialog').clientWidth+1));
 if(outputs)await page.screenshot({path:path.join(outputs,'mobile-card.png')});
 assert.deepEqual(errors,[]);await browser.close();console.log('PASS: Chromium desktop/mobile navigation, graph-node and relation clicks, dialogs, filters, search, no page overflow or JavaScript errors.');
})().catch(e=>{console.error(e);process.exitCode=1});
