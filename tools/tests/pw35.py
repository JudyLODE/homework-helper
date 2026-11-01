from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("""window.__n=0;window.claude={use:async(n)=>({limits:async()=>({images:{maxCount:5}}),json:async(pr,o)=>{
 if(pr.includes('請依這些內容設計'))return {lessons:[{title:'測驗題',secs:[{k:'mc',g:'x',t:'測驗',pt:1,items:[{q:'題?',o:['甲','乙'],a:0}]}]}]};
 const n=++window.__n;window.__cnt=(window.__cnt||[]);window.__cnt.push(o.images.length);
 if(n===1)return {lessons:[{title:'第四課 小丑魚和海葵',secs:[{k:'txt',t:'課文',items:[{p:'課文段落'}]},{k:'tbl',t:'生字',head:['字'],items:[{c:['丑']}]}]}]};
 if(n===2)return {lessons:[{title:'詞語',secs:[{k:'vocab',t:'詞語',items:['共生：互相幫助','保護：照顧']},{k:'mc',t:'課文重點',items:[{q:'缺答案'}]}]}]};
 return {lessons:[{title:'語文天地',secs:[{k:'poem',t:'語文天地',items:[{line:'小丑魚'},{line:'海葵'}]}]}]}}})};""")
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    pg.click('[data-a="flt"][data-f="cn"]')
    pg.locator('[data-a=tup][data-t="第四課 小丑魚和海葵"]').click()
    pg.set_input_files('#ph',['/tmp/b0.jpg','/tmp/b1.jpg','/tmp/b2.jpg','/tmp/b3.jpg','/tmp/b4.jpg']);pg.wait_for_timeout(500);pg.click('[data-a=ai]');pg.wait_for_timeout(9000)
    print(pg.evaluate("[S.v,window.__cnt,SEC.filter(s=>s.custom).map(s=>[s.t,s.pp.o.map(x=>x.t+':'+x.k)])]"))
    print(pg.inner_text('#app')[:500]);print(errs)
