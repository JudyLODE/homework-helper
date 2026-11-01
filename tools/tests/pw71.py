from playwright.sync_api import sync_playwright
import re
src=open('pw61.py',encoding='utf8').read()
FILL=re.search(r'FILL="""(.*?)"""',open('pw50.py',encoding='utf8').read().replace(' if(sec.k===\'mx\'',' if(sec.k===\'wp\'){A[k+\'.e\']=it.nums[0]+(it.op===\'-\'?\'-\':it.op)+it.nums[1];A[k+\'.n\']=String(it.a);A[k+\'.u\']=it.u;if(it.chk){A[k+\'.v\']=it.op===\'+\'?(it.a+\'-\'+it.nums[1]):(it.a+\'+\'+it.nums[1])}}\n if(sec.k===\'ruler\'){if(it.o===\'mm\')A[k+\'.0\']=String(it.mm);else{A[k+\'.0\']=String(Math.floor(it.mm/10));A[k+\'.1\']=String(it.mm%10)}}\n if(sec.k===\'nl\'){it.blank.forEach((b,j)=>A[k+\'.\'+j]=String(it.v[b]))}\n if(sec.k===\'mx\'',1),re.S).group(1)
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    pg.click('[data-a="exam"]')
    pg.click('[data-a="ex_sub"][data-v="math"]')
    for i,t in enumerate(['10000 以內的加減','毫米與數線','乘法']):
        idx=pg.evaluate("(t)=>SEC.findIndex(s=>s.t===t)",t)
        pg.click('[data-a="ex_t"][data-v="%d"]'%idx)
    pg.click('[data-a="ex_go"]');pg.wait_for_timeout(300)
    print(pg.inner_text('#app')[-700:-200])
    pg.screenshot(path='shots2/e1.png',full_page=True)
    # print views
    pg.click('[data-a="ex_pq"]');pg.wait_for_timeout(300);pg.screenshot(path='shots2/e2.png',full_page=True)
    pg.click('.back');pg.wait_for_timeout(200)
    pg.click('[data-a="ex_pa"]');pg.wait_for_timeout(300);pg.screenshot(path='shots2/e3.png',full_page=True)
    pg.emulate_media(media='print');pg.pdf(path='shots2/exam_a.pdf',format='A4',print_background=True);pg.emulate_media(media='screen')
    pg.click('.back');pg.wait_for_timeout(200)
    pg.click('[data-a="ex_pq"]');pg.wait_for_timeout(300)
    pg.emulate_media(media='print');pg.pdf(path='shots2/exam_q.pdf',format='A4',print_background=True);pg.emulate_media(media='screen')
    pg.click('.back');pg.wait_for_timeout(200)
    # electronic: fill all correct
    pg.click('[data-a="ex_do"]');pg.wait_for_timeout(300)
    n=pg.evaluate("ppSecs().length")
    for si in range(n):
        pg.evaluate(FILL,si)
        pg.evaluate("()=>{S.pp.ck[S.pp.ver+S.pp.i]=1;render()}")
        sc=pg.evaluate("((si)=>ppSecScore(ppSecs()[si],si))",si)
        if abs(sc['got']-sc['max'])>1e-6:print('NOT FULL',si,sc)
        pg.evaluate("()=>{S.pp.i++}")
    print('secs',n,'lock?',pg.evaluate("ppSecs().map((s,i)=>secLock(s,i))"))
    print('errs',[e for e in errs if 'compressed' not in e])
