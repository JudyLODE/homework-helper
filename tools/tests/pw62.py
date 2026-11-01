from playwright.sync_api import sync_playwright
import sys
Q=[('10000 以內的加減',2,1),('10000 以內的加減',2,3),('10000 以內的加減',4,3),('毫米與數線',0,1),('毫米與數線',0,4),('毫米與數線',1,0),('毫米與數線',1,1),('毫米與數線',3,3),('乘法',2,0),('乘法',2,2),('乘法',4,1),('第 1～4 單元綜合評量',0,2),('第 1～4 單元綜合評量',1,1)]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    for n,(T,zi,si) in enumerate(Q):
        pg.evaluate("(a)=>{const [T,zi,si]=a;const i=SEC.findIndex(x=>x.t===T);S.s=i;S.v='sec';render();ppStart('z'+zi);S.pp.i=si;render()}",[T,zi,si])
        pg.wait_for_timeout(200)
        pg.screenshot(path='shots2/s%02d.png'%n,full_page=True)
print('done')
