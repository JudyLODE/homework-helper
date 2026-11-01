# tools/ 說明（給接手的 AI／開發者）

- `tests/pw*.py`：Playwright（Python）測試腳本，57 支。腳本都以
  `file:///mnt/user-data/outputs/study-helper.html` 開啟 App。在新環境請先建立連結：
  `mkdir -p /mnt/user-data/outputs && ln -sf "$PWD/index.html" /mnt/user-data/outputs/study-helper.html`
  執行：`python3 tools/tests/pw8.py`。截圖會寫到執行目錄下的 `shots/`、`shots2/`（需先 mkdir）。
  - `pw8.py` 回歸（輸出 `bad: []` 為通過）
  - `pw45.py` 數學闖關流程
  - `pw60.py` 各回出題與總分 =100
  - `pw61.py N` 每回全部填正確 → 滿分（N 為重複次數）
  - `pw70.py` 考卷出題 60 次
  - `pw71.py` 考卷 UI 流程並匯出 PDF（shots2/exam_q.pdf、exam_a.pdf）
  - 其餘 `pwNN.py` 為各階段的功能測試。
  - 固定會出現無害訊息「The compressed data was not valid…」。
- `strip_priv.py <in> <out>`：移除所有 `/*PRIV:Mn:BEGIN…END*/` 區塊（產生公開版；使用者沒說就不要用）。
- `priv_src/priv_m2–m5.js`：照片整理題型區塊的原始碼（已包含在 index.html）。
- `history/`：v59／v60 的建置腳本（build.py、patch_ex.py、g1–g3.js、ex1.js）。**僅供參考，不要重跑**，會覆蓋後來的修改。
