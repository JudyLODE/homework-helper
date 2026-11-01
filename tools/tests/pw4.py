import json
from playwright.sync_api import sync_playwright
calls=[];errs=[]
lesson={"lessons":[{"sub":"cn","t":"第五課 飛舞的絲帶","w":[["絲帶","ㄙ ㄉㄞˋ｜細長的布條","🎀"]],"d":[["題",'',"是","因",["否","不"],"","o1"]]}]}
body=json.dumps(lesson,ensure_ascii=False)
half=len(body)//2
def sse(*parts):
    return "".join('data: '+json.dumps({"candidates":[{"content":{"parts":[{"text":p}]}}]},ensure_ascii=False)+"\n\n" for p in parts)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':390,'height':844})
    pg.on('pageerror',lambda e:errs.append(str(e)))
    def models(route):route.fulfill(status=200,content_type='application/json',body=json.dumps({"models":[{"name":"models/gemini-3.6-flash","supportedGenerationMethods":["generateContent"]},{"name":"models/gemini-2.5-flash","supportedGenerationMethods":["generateContent"]}]}))
    def gen(route):
        n=len(calls);calls.append(route.request.url.split('/models/')[1][:30])
        if n==0:route.abort('failed')   # first call: network failure -> should fall to next model
        else:route.fulfill(status=200,content_type='text/event-stream',body=sse(body[:half],body[half:]))
    pg.route(__import__('re').compile(r'v1beta/models\?pageSize'),models);pg.route(__import__('re').compile(r'streamGenerateContent'),gen)
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(300)
    pg.evaluate("AI.url='AIzaX';S.v='add';S.asub='cn';render()")
    pg.set_input_files('#ph',[f'/home/claude/shots/p{i}.jpg' for i in range(7)])
    pg.wait_for_timeout(300)
    pg.click('[data-a=ai]');pg.wait_for_timeout(2500)
    print('calls',calls)
    print(pg.evaluate("JSON.stringify({v:S.v,t:SEC[S.s].t,w:SEC[S.s].w.length,d:SEC[S.s].d.length,os:(document.getElementById('os')||{}).textContent})"))
    b.close()
print(errs)
