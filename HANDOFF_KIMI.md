# 交接文件：作業輔導小幫手（給 KIMI）
更新：2026-11-01　目前版本：v60（App 內頁尾顯示「版本 v60（11/1）」）

## 1. 專案是什麼
- 單一檔案 vanilla-JS HTML App（無建置工具、無框架），給國小三年級孩子課後練習、家長輔導用。介面一律繁體中文、台灣用語。
- 檔案：`index.html`（GitHub repo `JudyLODE/homework-helper`，Pages：https://judylode.github.io/homework-helper/）。孩子的資料只存在瀏覽器（localStorage），不上傳。
- 注意：GitHub repo 目前是 v59；v60（考卷出題）尚未推送，需使用者同意後才推。

## 2. 使用者的硬性規則（不可違反）
1. 不要擅自 push；使用者說「上傳」才 push。先在 Claude 試用確認，再上 GitHub。
2. 完整版必須保留 `/*PRIV:Mn:BEGIN … END*/` 區塊（M1–M5，由照片整理出的題型資料）。不要自行刪除。
3. 不出現教科書品牌字（翰林／康軒／南一／Here We Go）、不寫「三上」、綜合評量不寫「期中考」字樣。
4. 國語答案依教育部《重編國語辭典修訂本》；國語不做計算／筆畫／口語跟讀題。
5. 只有英語有聲音。上傳頁只保留三種教材選項。每個科目一次訓練一個。
6. 練習畫面不顯示分數，只顯示 ✅／❌ 與星星。
7. 照片只取「題型、作答格式、題數」；數字與文字每次重新產生。照片上的手寫字跡、紅筆批改一律忽略。
8. 數學：答案由程式計算、圖由程式繪製；不做直式計算板；每一回總分 100。
9. 數學闖關：每組答對 ≥80% 得 1 格；需要格數 1/2/3/5（預設 3）；最多 6 組；通過前「下一大題」鎖住。考卷課程（pp.ex）不鎖。
10. 回覆使用者用中文、簡潔。

## 3. 程式結構速覽（在 index.html 內搜尋這些名稱）
- 狀態 `S`；`render()` 的 view 對照表（home、sec、cards、info、dream、quiz、add、parent、dict、order、calc、match、paper、full、settings、exam、examprint）。
- 點擊事件統一委派在 `app.addEventListener('click')`，用 `data-a`；`p_` 開頭給習作引擎（ppClick），`ex_` 開頭給考卷（exClick）。
- 習作引擎：`PT`、`normPaper`、`ppUnits`、`ppMax`、`ppEval`、`ppItem`、`ppSecs`、`ppStart`、`ppRegenSec`、`MREGEN`、`paperV`。課程資料 `pp:{title,z:[{t,secs}],rg:1,...}`；每題配分 `sec.pt × units`，每回合計 100。
- 數學題型註冊：`MATH[k]={name,norm,units,gen,can,ev,render}`；文字題模板 `MXG[tpl]` 與 `mkMx(tpl,pa)`。語法：（ ）填空、〔甲｜乙｜丙〕圈選、⟦位⟧位值表、⟦畫⟧畫錢幣；`a` 為答案（"x|y" 表示可接受多種）。
- 應用題：`WPT` 情境池、`wpGen`、`segSvg`（線段圖）；數線 `nlSvg`；SVG 一律經 `svgOk` 過濾。
- 考卷出題：`EXST`（期中 44 單位／8 大題、期末 58／10）、`exMath`、`exAI`（非數學，走 aiCall）、`exPoints`（整數配分）、`exSave`、`exam()`、`examprint()`、`exSheet`；列印 CSS 在 `.sheet…` 與 `@media print`。
- 備份／還原：`bkOut`／`bkIn`，JSON `{app:'homework-helper',v:1,lessons,prog}`。iPad 貼文字還原曾失敗，請用檔案還原；若要改善，可做容錯解析。
- 私有區塊：`makePrivM1`–`M5` 由安裝 IIFE 掛到課程的 `L.pp`。

## 4. 修改流程
1. 改 `index.html`；每次發佈把頁尾版本號 +1。
2. 小修：直接編輯。大修：寫 Python patch 腳本做字串替換並檢查匹配次數（避免誤改）。
3. 用 Playwright（Chromium）跑測試，至少：開首頁無錯誤；數學各回「全部填正確 → 滿分」；各回總分 =100；考卷出題 60 次不出錯；電子作答全對滿分；列印用 `emulate_media('print')` 輸出 PDF 看版面（A4、黑白、解答頁不該有 ✅／❌）。
4. 在 Claude 試用（artifact 連結：https://claude.ai/artifact/49nMVoC21d8dqp5XMeGLkr，同一網址覆蓋更新）。
5. 使用者同意後才 push 到 GitHub。Commit 訊息結尾要加：
   Co-Authored-By: <你的名稱> <noreply@…>（原本是 Claude 的署名；換成 KIMI 時請寫上實際作者，不要冒用 Claude）

## 5. 已知限制／待辦
- 非數學科的 AI 出題（`exAI`）尚未用真實金鑰測過。
- 數學「上傳照片自動整理題型」流程尚未做；目前 21 回習作題型是人工從照片整理好的。
- 還沒題型的數學課程（如「列表與規律」）不能出考卷。
- window.print() 在 Claude 內嵌檢視可能被擋，需在 GitHub Pages 網址上列印。
- 測試中固定會出現無害訊息「The compressed data was not valid…」。

## 6. 權限與安全
- 不要把任何金鑰、token 寫進 index.html 或 commit。使用者的 AI 金鑰只存在使用者瀏覽器。
- KIMI 要能 push，需要使用者在 GitHub 把 KIMI 使用的帳號加為 repo collaborator，或給 KIMI 一組只限此 repo 的 token（由使用者自己操作，不要貼在對話裡）。

## 7. 其他文件
專案「Homework」內：計分與闖關機制、數學習作題型與作答設計、科目x教材處理方式紀錄、考卷出題設計。
