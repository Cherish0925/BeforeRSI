/* Functional checks of the offline page's real JavaScript, not browser layout tests. */
const fs=require('fs'),vm=require('vm'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'..');const html=fs.readFileSync(path.join(root,'research/atlas/index.html'),'utf8');
const scripts=[...html.matchAll(/<script(?:[^>]*)>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
const nodes={};const node=id=>nodes[id]??=( {innerHTML:'',textContent:'',open:false,handlers:{},addEventListener(k,f){this.handlers[k]=f},setAttribute(){},showModal(){this.open=true},close(){this.open=false}} );
node('atlas-data').textContent=scripts[0];const events={};
const document={getElementById:node,querySelector:node,querySelectorAll:()=>[],addEventListener:(k,f)=>events[k]=f};
const ctx=vm.createContext({document,window:{scrollTo(){}}});vm.runInContext(scripts[1],ctx);
const run=s=>vm.runInContext(s,ctx);const count=(s,c)=>(s.match(new RegExp('class="'+c+'"','g'))||[]).length;
assert.equal(count(nodes.main.innerHTML,'route'),3);
assert(nodes.main.innerHTML.includes('不是全球最终筛选数'));
assert(nodes.main.innerHTML.includes('产学联合'));
for(const [route,n] of [['harness',12],['model',5],['hybrid',2]]){run(`tab='${route}';render()`);assert.equal(count(nodes.main.innerHTML,'work'),n);}
run("tab='space';spaceRoute='all';render()");assert.equal(count(nodes.main.innerHTML,'space'),18);
run("tab='catalog';route='';placement='all';query='';render()");assert.equal(count(nodes.results.innerHTML,'work'),127);
for(const [p,n] of [['main',19],['small',6],['scale_unverified',4],['adjacent',6],['crosscut',3],['pending',67],['historical',16],['background',6]]){run(`placement='${p}';query='';drawResults()`);assert.equal(count(nodes.results.innerHTML,'work'),n);}
run("route='model';placement='main';drawResults()");assert.equal(count(nodes.results.innerHTML,'work'),5);
assert(nodes.results.innerHTML.includes('Kimi K2'));assert(nodes.results.innerHTML.includes('DeepSeekMath-V2'));
run("route='';placement='all';query='SEAL';drawResults()");assert(nodes.results.innerHTML.includes('data-work="seal"'));
const a=JSON.parse(scripts[0]);for(const w of a.works){run(`openWork(${JSON.stringify(w.id)})`);assert(nodes['detail-title'].innerHTML.includes(w.number.toString().padStart(3,'0')));assert(nodes['detail-body'].innerHTML.includes('https://'));}
run("openWork('on-policy-harness-coevolution')");assert(nodes['detail-body'].innerHTML.includes('30B / 3B'));assert(nodes['detail-body'].innerHTML.includes('26B / 4B'));assert(nodes['detail-body'].innerHTML.includes('低于门槛'));assert(nodes['detail-body'].innerHTML.includes('LoRA SFT'));
run("openWork('self-taught-evaluators')");assert(nodes['detail-body'].innerHTML.includes('同一原始种子'));
run("openWork('evotrainer')");assert(nodes['detail-body'].innerHTML.includes('未核准'));
run("openWork('deepseek-math-v2')");assert(nodes['detail-body'].innerHTML.includes('架构下界'));assert(nodes['detail-body'].innerHTML.includes('规模通过'));
events.click({target:{closest:()=>({dataset:{tab:'model'}})}});assert.equal(count(nodes.main.innerHTML,'work'),5);
events.click({target:{closest:()=>({dataset:{spaceRoute:'hybrid'}})}});assert.equal(count(nodes.main.innerHTML,'space'),6);
events.click({target:{closest:()=>({dataset:{catalogRoute:'hybrid'}})}});assert(nodes.result.textContent.includes('显示'));
assert(!/<script[^>]+src=|<link[^>]+href=/.test(html));assert(!/\bfetch\(/.test(scripts[1]));
console.log('PASS: 12/5/2 cases, institutional table, size/reference filters, 127 dialogs, navigation, offline assets. Browser layout not tested.');
