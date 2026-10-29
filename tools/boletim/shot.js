// node shot.js <slug>  -> out/<slug>.png (1080x1920) e out/<slug>.jpg via python
const {chromium}=require('playwright');const path=require('path');
const slug=process.argv[2];const dir=__dirname;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.join(dir,slug+'.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
await p.screenshot({path:path.join(dir,'out',slug+'.png')});await b.close();})();
