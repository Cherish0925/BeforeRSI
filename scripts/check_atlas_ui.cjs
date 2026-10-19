/* Offline reader checks; CHROMIUM_PATH adds real desktop/mobile interaction checks. */
const fs=require('fs'),vm=require('vm'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'..'),file=path.join(root,'research/atlas/index.html');
const html=fs.readFileSync(file,'utf8'),scripts=[...html.matchAll(/<script(?:[^>]*)>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
const data=JSON.parse(scripts[0]),nodes={};
const node=id=>nodes[id]??={innerHTML:'',textContent:'',value:'',open:false,scrollTop:0,scrollLeft:0,handlers:{},classList:{toggle(){}},addEventListener(k,f){this.handlers[k]=f},showModal(){this.open=true},close(){this.open=false}};
node('literature-data').textContent=scripts[0];const events={};
const ctx=vm.createContext({URLSearchParams,document:{getElementById:node,querySelectorAll:()=>[],addEventListener:(k,f)=>events[k]=f},window:{location:{hash:''},scrollTo(){}}});
vm.runInContext(scripts[1],ctx);const run=s=>vm.runInContext(s,ctx);
assert.equal((nodes.main.innerHTML.match(/class="field-card"/g)||[]).length,3);
assert.equal((nodes.main.innerHTML.match(/class="field-network"/g)||[]).length,3);
for(const r of data.field.routes){
 run(`setPage('${r.id}')`);assert.equal(run('state.mapMode'),'domain');assert(nodes.main.innerHTML.includes('领域知识图谱'));
 for(const n of r.nodes){run(`openDomainTopic('${n.id}')`);assert.equal(run('state.route'),r.id);assert(nodes.main.innerHTML.includes(n.question));}
 for(const e of r.edges){run(`openDomainEdge('${e.id}')`);assert(nodes.main.innerHTML.includes(e.source_urls[0]));assert(nodes.main.innerHTML.includes(e.explanation));}
 run(`setPage('${r.id}');state.mapMode='papers';render()`);const stats=data.routes.find(x=>x.id===r.id).counts;
 assert.equal(run('selectedWorks().length'),stats.catalog-stats.small);
 run('state.small=true;drawGraph()');assert.equal(run('selectedWorks().length'),stats.catalog);
 run("state.status='methods';drawGraph()");assert.equal(run('selectedWorks().length'),stats.methods);
 run("state.small=false;state.status='all'");
}
run("setPage('search')");assert.equal(run('searchWorks().length'),data.works.length);
run("state.query='伯克利'");assert(run('searchWorks().length')>2);
run("state.query='EURISKO'");assert.equal(run('searchWorks()[0].id'),'eurisko');
for(const w of data.works){run(`openPaper(${JSON.stringify(w.id)})`);assert(nodes['paper-content'].innerHTML.includes('id="paper-title"'));assert(nodes['paper-content'].innerHTML.includes(w.primary_url));}
run("openPaper('eurisko')");assert(nodes['paper-content'].innerHTML.includes('带槽位'));assert(!nodes['paper-content'].innerHTML.includes('既有操作记录'));
for(const e of data.relations){run(`selectEdge('${e.id}')`);assert(nodes.inspector.innerHTML.includes(e.sources[0].url));}
run("locate('skillrl')");assert.equal(run('state.small'),true);assert.equal(run('state.selected'),'skillrl');
assert(!/<script[^>]+src=|<link[^>]+href=/.test(html));assert(!/\bfetch\(/.test(scripts[1]));
// Company records are searchable through both company aliases and associated works.
run("setPage('companies')");assert.equal(run('selectedCompanies().length'),data.industry.counts.research+data.industry.counts.direction);
for(const c of data.industry.companies){run(`openCompany(${JSON.stringify(c.id)})`);assert(nodes['paper-content'].innerHTML.includes(c.name));for(const x of c.work_links)assert(nodes['paper-content'].innerHTML.includes(x.work_id));}
for(const [query,id] of [['元环','metacircle'],['超衍','apex'],['姐夫哥','discovery-loop'],['Nous','nous']]){run(`state.query=${JSON.stringify(query)}`);assert(run(`COMPANIES.filter(c=>companyMatches(c,state.query)).some(c=>c.id===${JSON.stringify(id)})`));}
run("state.query='超衍';state.searchRoute='all';state.searchStatus='all';state.searchOrg='all'");assert.equal(run('searchWorks().length'),3);
run("openDomainTopic('h-search')");assert(nodes.main.innerHTML.includes('data-company="metacircle"'));assert(nodes.main.innerHTML.includes('data-company="discovery-loop"'));
run("openDomainTopic('m-pretraining-ai4ai')");assert(nodes.main.innerHTML.includes('跨路线参考 · Harness'));
run("openPaper('apex-tune')");assert(nodes['paper-content'].innerHTML.includes('data-company="apex"'));
console.log(`PASS: three field maps, 29 topics, 60 conceptual relations, ${data.works.length} cards, ${data.relations.length} paper relations, filters/search/offline payload.`);
if(process.env.CHROMIUM_PATH)(async()=>{
 const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
 const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('file://'+file);
 assert.equal(await page.locator('.field-card svg').count(),3);
 for(const s of await page.locator('.field-card svg').all()){const b=await s.boundingBox();assert(b&&b.width>250&&b.height>350&&b.y+b.height<=1000);}
 const outputs=process.env.ATLAS_SCREENSHOTS;
 if(outputs){fs.mkdirSync(outputs,{recursive:true});await page.screenshot({path:path.join(outputs,'landscape-overview.png'),fullPage:true});await page.screenshot({path:path.join(outputs,'first-screen.png')});}
 for(const r of data.field.routes){
  await page.locator(`nav [data-nav="${r.id}"]`).click();assert.equal(await page.locator('svg .concept-node').count(),r.nodes.length);

  await page.locator('[data-domain-expand]').click();assert.equal(await page.locator('.field-subtopic').count(),r.nodes.reduce((a,n)=>a+n.subtopics.length,0));
  if(outputs){const svg=await page.locator('.domain-canvas svg').evaluate(s=>{const copy=s.cloneNode(true);copy.setAttribute('width',copy.viewBox.baseVal.width);copy.setAttribute('height',copy.viewBox.baseVal.height);const st=document.createElementNS('http://www.w3.org/2000/svg','style');st.textContent=[...document.styleSheets].flatMap(x=>[...x.cssRules]).filter(x=>/^\.(field-network|concept-|topic-|domain-)/.test(x.cssText)).map(x=>x.cssText).join('\n');copy.prepend(st);return new XMLSerializer().serializeToString(copy)});fs.writeFileSync(path.join(outputs,r.id+'-field-graph.svg'),svg);}
if(outputs&&r.id==='model')await page.screenshot({path:path.join(outputs,'model-subtopics.png')});await page.locator('[data-domain-expand]').click();
  const n=r.nodes[0];await page.locator(`svg [data-topic="${n.id}"]`).click();assert((await page.locator('.domain-inspector').innerText()).includes(n.question));
  await page.locator('.topic-relation button').first().click();assert((await page.locator('.domain-inspector').innerText()).includes('机制之间的关系'));
  await page.locator('[data-map-mode="papers"]').click();const stats=data.routes.find(x=>x.id===r.id).counts;assert.equal(await page.locator('.graph-svg .work').count(),stats.catalog-stats.small);
  if(stats.small){await page.locator('#small-filter').check();assert.equal(await page.locator('.graph-svg .work').count(),stats.catalog);await page.locator('#small-filter').uncheck();}
 }
 await page.locator('nav [data-nav="harness"]').click();await page.locator('svg [data-topic="h-improver"]').click();
 if(outputs)await page.screenshot({path:path.join(outputs,'harness-topic.png')});
 await page.locator('#domain-work-list [data-paper="dgm"]').first().click();assert.equal(await page.locator('.axis').count(),6);assert(await page.locator('.paper-domain-tags [data-topic]').count()>0);
 if(outputs)await page.screenshot({path:path.join(outputs,'research-card.png')});
 await page.locator('#paper-content [data-topic="h-improver"]').click();assert(!(await page.locator('#paper-dialog').isVisible()));assert((await page.locator('.domain-inspector').innerText()).includes('改进程序的自修改'));
 await page.locator('[data-map-mode="papers"]').click();await page.locator('.graph-svg [data-node="gepa"]').click();assert((await page.locator('#inspector').innerText()).includes('GEPA'));
 await page.locator('#inspector [data-paper="gepa"]').click();await page.keyboard.press('Escape');assert(!(await page.locator('#paper-dialog').isVisible()));
 await page.locator('#global-search').fill('EURISKO');await page.locator('#search-form button').click();assert.equal(await page.locator('.result-card').count(),1);
 await page.locator('.result-card h3 a').click();assert.equal(await page.locator('.axis').count(),6);await page.locator('[data-close]').click();
 await page.locator('[data-clear-search]').click();assert.equal(await page.locator('.result-card').count(),data.works.length);
 await page.locator('#search-route').selectOption('hybrid');assert.equal(await page.locator('.result-card').count(),data.routes.find(x=>x.id==='hybrid').counts.catalog);
 await page.locator('nav [data-nav="companies"]').click();assert.equal(await page.locator('.company-card').count(),data.industry.counts.research+data.industry.counts.direction);
 if(outputs)await page.screenshot({path:path.join(outputs,'industry-overview.png'),fullPage:true});
 await page.locator('#company-query').fill('超衍');assert.equal(await page.locator('.company-card').count(),1);
 await page.locator('.company-card h3 button').click();assert.equal(await page.locator('.company-output-list article').count(),3);
 if(outputs)await page.screenshot({path:path.join(outputs,'apex-company-card.png')});
 await page.locator('.company-output-list h4 [data-paper="apex-tune"]').click();assert.equal(await page.locator('.axis').count(),6);await page.locator('.paper-companies [data-company="apex"]').click();assert((await page.locator('#paper-content').innerText()).includes('具体工作与公开证据'));await page.locator('[data-close]').click();
 await page.locator('#global-search').fill('姐夫哥');await page.locator('#search-form button').click();assert.equal(await page.locator('#search-company-results .company-card').count(),1);await page.locator('#search-company-results h3 button').click();assert((await page.locator('#paper-content').innerText()).includes('尚未披露'));await page.locator('[data-close]').click();
 await page.setViewportSize({width:390,height:844});await page.locator('nav [data-nav="overview"]').click();assert.equal(await page.locator('.field-card svg').count(),3);assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
 if(outputs)await page.screenshot({path:path.join(outputs,'mobile-overview.png')});
 await page.locator('nav [data-nav="model"]').click();assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
 await page.locator('svg [data-topic="m-bootstrapping"]').focus();await page.keyboard.press('Enter');assert((await page.locator('.domain-inspector').innerText()).includes('模型的哪些输出'));
 await page.locator('#domain-work-list [data-paper="rest-em"]').first().click();assert(await page.evaluate(()=>document.querySelector('#paper-dialog').scrollWidth<=document.querySelector('#paper-dialog').clientWidth+1));
 if(outputs)await page.screenshot({path:path.join(outputs,'mobile-card.png')});
 await page.keyboard.press('Escape');await page.locator('nav [data-nav="companies"]').click();await page.locator('[data-company-clear]').click();await page.locator('#company-query').fill('元环');await page.locator('.company-card h3 button').click();assert(await page.evaluate(()=>document.querySelector('#paper-dialog').scrollWidth<=document.querySelector('#paper-dialog').clientWidth+1));
 if(outputs)await page.screenshot({path:path.join(outputs,'mobile-company.png')});
 assert.deepEqual(errors,[]);await browser.close();console.log('PASS: Chromium first-screen maps, topic/edge navigation, paper/field return, desktop/mobile search, dialogs, filters, keyboard, no page overflow or JavaScript errors.');
})().catch(e=>{console.error(e);process.exitCode=1});
