/* Offline reader contracts and optional real-browser interaction checks. */
const fs=require('fs'),vm=require('vm'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'..'),file=path.join(root,'research/atlas/index.html');
const html=fs.readFileSync(file,'utf8'),scripts=[...html.matchAll(/<script(?:[^>]*)>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
const data=JSON.parse(scripts[0]),corpus=data.corpus_review,nodes={};
const node=id=>nodes[id]??={innerHTML:'',textContent:'',value:'',open:false,scrollTop:0,scrollLeft:0,handlers:{},classList:{toggle(){}},addEventListener(k,f){this.handlers[k]=f},showModal(){this.open=true},close(){this.open=false}};
node('literature-data').textContent=scripts[0];const events={};
const ctx=vm.createContext({URLSearchParams,document:{getElementById:node,querySelectorAll:()=>[],addEventListener:(k,f)=>(events[k]??=[]).push(f)},window:{location:{hash:''},scrollTo(){}}});
vm.runInContext(scripts[1],ctx);const run=s=>vm.runInContext(s,ctx);
const focused=(w,all=false)=> (all?['core','support','mechanism_supplement']:['core']).includes(w.corpus_selection?.decision);
assert.equal((nodes.main.innerHTML.match(/class="field-card"/g)||[]).length,3);
assert.equal((nodes.main.innerHTML.match(/class="field-network"/g)||[]).length,3);
for(const r of data.field.routes){
 run(`state.researchFocus='core';state.small=false;setPage('${r.id}')`);
 assert.equal(run('state.mapMode'),'domain');assert(nodes.main.innerHTML.includes('领域知识图谱'));
 for(const n of r.nodes){run(`openDomainTopic('${n.id}')`);assert(nodes.main.innerHTML.includes(n.question));}
 for(const e of r.edges){run(`openDomainEdge('${e.id}')`);assert(nodes.main.innerHTML.includes(e.source_urls[0]));assert(nodes.main.innerHTML.includes(e.explanation));}
 run(`setPage('${r.id}');state.mapMode='papers';render()`);
 const ws=data.works.filter(w=>w.route===r.id);
 assert.equal(run('selectedWorks().length'),ws.filter(w=>focused(w)&&w.placement!=='small').length);
 run("state.researchFocus='all';state.small=true;drawGraph()");
 assert.equal(run('selectedWorks().length'),ws.filter(w=>focused(w,true)).length);
 assert(run("selectedWorks().every(w=>!['insufficient','outside','redundant'].includes(corpusSelection(w)))"));
}
run("state.researchFocus='core';state.small=false;setPage('search')");
assert.equal(run('corpusSearchResults().length'),corpus.counts.total);
assert.equal((nodes.results.innerHTML.match(/class="result-card"/g)||[]).length,20);
run("state.searchPage=2;drawResults()");assert.equal(run('state.searchPage'),2);assert(nodes['search-pages'].innerHTML.includes('第 2 /'));
run("state.query='EURISKO';drawResults()");assert.equal(run('corpusSearchResults()[0].work_id'),'eurisko');
run("state.query='2411.02337';drawResults()");assert.equal(run('corpusSearchResults()[0].work_id'),'webrl');
run("state.query='';state.searchPage=1");
for(const [decision,count] of Object.entries(corpus.counts.selection)){
 run(`state.searchDecision=${JSON.stringify(decision)}`);assert.equal(run('corpusSearchResults().length'),count);
}
run("state.searchDecision='all'");
for(const w of data.works){run(`openPaper(${JSON.stringify(w.id)})`);assert(nodes['paper-content'].innerHTML.includes('id="paper-title"'));assert(nodes['paper-content'].innerHTML.includes(run('esc('+JSON.stringify(w.primary_url)+')')),w.id);}
for(const e of corpus.entries){
 run(`openCorpusEntry(${JSON.stringify(e.entry_id)})`);assert(nodes['paper-content'].innerHTML.includes('id="paper-title"'));
 if(e.review){assert(nodes['paper-content'].innerHTML.includes(run('esc('+JSON.stringify(e.review.reading.sources[0].url)+')')));assert(nodes['paper-content'].innerHTML.includes('可执行的机制'));}
 else assert(nodes['paper-content'].innerHTML.includes('尚未完成原文阅读'));
}
for(const rel of corpus.relations){
 assert(run(`corpusRelationsFor(${JSON.stringify(rel.source)}).some(r=>r.other===${JSON.stringify(rel.target)})`));
 assert(run(`corpusRelationsFor(${JSON.stringify(rel.target)}).some(r=>r.other===${JSON.stringify(rel.source)})`));
}
run("setPage('coverage')");assert(nodes.main.innerHTML.includes('全部记录与逐项理由'));assert.equal(run('corpusMatches().length'),corpus.counts.total);
for(const [decision,count] of Object.entries(corpus.counts.selection)){run(`state.corpusDecision=${JSON.stringify(decision)}`);assert.equal(run('corpusMatches().length'),count);}
run("state.corpusDecision='all';state.corpusQuery='2411.02337'");assert.equal(run('corpusMatches().length'),1);
run("state.corpusQuery='';openPaper('webrl')");assert(nodes['paper-content'].innerHTML.includes('70B'));
run("openPaper('eurisko')");assert(!nodes['paper-content'].innerHTML.includes('既有操作记录'));
for(const e of data.relations){run(`selectEdge('${e.id}')`);assert(nodes.inspector.innerHTML.includes(run('esc('+JSON.stringify(e.sources[0].url)+')')),e.id+' '+e.sources[0].url);}
run("locate('skillrl')");assert.equal(run('state.small'),true);assert.equal(run('state.selected'),'skillrl');assert(run("selectedWorks().some(w=>w.id==='skillrl')"));
assert(!/<script[^>]+src=|<link[^>]+href=/.test(html));assert(!/\bfetch\(/.test(scripts[1]));
run("setPage('companies')");
for(const c of data.industry.companies){run(`openCompany(${JSON.stringify(c.id)})`);assert(nodes['paper-content'].innerHTML.includes(c.name));for(const x of c.work_links)assert(nodes['paper-content'].innerHTML.includes(x.work_id));}
for(const [query,id] of [['元环','metacircle'],['超衍','apex'],['姐夫哥','discovery-loop'],['Nous','nous']]){run(`state.query=${JSON.stringify(query)}`);assert(run(`COMPANIES.filter(c=>companyMatches(c,state.query)).some(c=>c.id===${JSON.stringify(id)})`));}
run("state.query='超衍';state.searchRoute='all';state.searchStatus='all';state.searchOrg='all'");assert(run("corpusSearchResults().some(e=>e.work_id==='apex-tune')"));
run("state.researchFocus='core';setPage('actors')");
for(const type of ['academic','tech','ai','independent','unresolved'])for(const route of ['harness','model','hybrid']){
 run(`state.actorKind='${type}';state.actorRoute='${route}';state.actorId='all';state.actorQuery='';state.actorSmall=false;state.actorCoop='all'`);
 const expected=data.works.filter(w=>focused(w)&&w.route===route&&w.placement!=='small'&&w.actor_types.includes(type));
 assert.equal(run('selectedActorWorks().length'),expected.length);
}
run("state.actorKind='all';state.actorRoute='all';state.actorQuery='谷歌'");assert(run("selectedActors().some(a=>a.id==='google')"));
run("openActor('google')");assert(nodes['paper-content'].innerHTML.includes('Google DeepMind'));
assert(!data.works.find(w=>w.id==='asi-bench').actor_ids.includes('profile-apex'));
console.log(`PASS: three field maps; ${corpus.counts.total} searchable records; ${data.works.length} catalog cards; source-backed two-way relations; core/expanded, institution, company and scope filters; offline payload.`);
if(process.env.CHROMIUM_PATH)(async()=>{
 const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
 const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('file://'+file);assert.equal(await page.locator('.field-card svg').count(),3);
 const outputs=process.env.ATLAS_SCREENSHOTS;
 const shot=async(name,fullPage=false)=>{if(outputs){fs.mkdirSync(outputs,{recursive:true});await page.screenshot({path:path.join(outputs,name+'.png'),fullPage});}};
 await shot('first-screen');
 for(const r of data.field.routes){
  await page.locator(`nav [data-nav="${r.id}"]`).click();assert.equal(await page.locator('svg .concept-node').count(),r.nodes.length);
  await page.locator('[data-domain-expand]').click();assert.equal(await page.locator('.field-subtopic').count(),r.nodes.reduce((a,n)=>a+n.subtopics.length,0));
  await shot(r.id+'-field');await page.locator('[data-domain-expand]').click();
  await page.locator(`svg [data-topic="${r.nodes[0].id}"]`).click();assert((await page.locator('.domain-inspector').innerText()).includes(r.nodes[0].question));
  await page.locator('[data-map-mode="papers"]').click();assert.equal(await page.locator('.graph-svg .work').count(),data.works.filter(w=>w.route===r.id&&focused(w)&&w.placement!=='small').length);
 }
 await page.locator('nav [data-nav="harness"]').click();await page.locator('svg [data-topic="h-improver"]').click();
 await page.locator('#domain-work-list [data-paper="dgm"]').first().click();assert.equal(await page.locator('.axis').count(),6);await shot('research-card');await page.keyboard.press('Escape');
 await page.locator('#global-search').fill('2411.02337');await page.locator('#search-form button').click();assert.equal(await page.locator('.result-card').count(),1);
 await page.locator('.result-card h3 a').click();assert((await page.locator('#paper-content').innerText()).includes('70B'));await page.locator('[data-close]').click();
 await page.locator('[data-clear-search]').click();assert.equal(await page.locator('.result-card').count(),20);
 await page.locator('[data-search-page="2"]').click();assert((await page.locator('#search-pages').innerText()).includes('第 2 /'));await shot('all-record-search');
 await page.locator('nav [data-nav="coverage"]').click();await page.locator('#corpus-query').fill('EURISKO');assert(await page.locator('.corpus-row').count()>=1);
 await page.locator('.corpus-row [data-corpus-entry="catalog-eurisko"]').first().click();assert((await page.locator('#paper-content').innerText()).includes('原文与阅读位置'));await page.keyboard.press('Escape');
 await page.locator('#corpus-query').fill('');await shot('reading-ledger',true);
 await page.setViewportSize({width:390,height:844});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await shot('mobile-ledger');
 await page.locator('nav [data-nav="overview"]').click();assert.equal(await page.locator('.field-card svg').count(),3);assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await shot('mobile-overview');
 await page.locator('nav [data-nav="model"]').click();await page.locator('svg [data-topic="m-bootstrapping"]').focus();await page.keyboard.press('Enter');assert((await page.locator('.domain-inspector').innerText()).includes('模型的哪些输出'));
 await page.locator('#domain-work-list [data-paper="rest-em"]').first().click();assert(await page.evaluate(()=>document.querySelector('#paper-dialog').scrollWidth<=document.querySelector('#paper-dialog').clientWidth+1));await shot('mobile-card');
 assert.deepEqual(errors,[]);await browser.close();console.log('PASS: real browser desktop/mobile navigation, search, pagination, source dialogs and keyboard; no overflow or script errors.');
})().catch(e=>{console.error(e);process.exitCode=1});
