const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const d=process.argv[2];const b=await chromium.launch();
const p=await b.newPage({viewport:{width:794,height:1123},deviceScaleFactor:2480/794});
const files=fs.readdirSync(d).filter(f=>/^p\d+\.html$/.test(f)).sort();const links={};
for(const f of files){await p.goto('file://'+d+'/'+f,{waitUntil:'networkidle'});await p.waitForTimeout(700);
 await p.screenshot({path:d+'/'+f.replace('.html','.png')});
 const r=await p.evaluate(()=>[...document.querySelectorAll('a[data-slug]')].map(a=>{const r=a.getBoundingClientRect();return {slug:a.dataset.slug,x:r.x,y:r.y,w:r.width,h:r.height};}));
 if(r.length) links[f.replace('.html','')]=r;}
fs.writeFileSync(d+'/links.json',JSON.stringify(links));await b.close();})();
