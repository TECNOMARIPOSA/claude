const {chromium}=require('playwright');
(async()=>{const d=process.argv[2];const b=await chromium.launch();
const p=await b.newPage({viewport:{width:794,height:1123},deviceScaleFactor:2480/794});
for(let i=1;i<=3;i++){await p.goto('file://'+d+'/p'+i+'.html',{waitUntil:'networkidle'});await p.waitForTimeout(800);
await p.screenshot({path:d+'/page'+i+'.png'});}
await b.close();})();
