# SciPoster Architect (科學海報架構設計)

這是一個專為科學展覽、學術研討會設計的高效率海報自動化生成系統。透過 **SciPoster Architect** 引擎，實現了 **「研究文字」** 與 **「佈局美學」** 的融合與技術分離。

## 核心優勢

- **原子化設計 (Atomic Design)**：內建 20 種高品質章節區塊 UI，涵蓋磨砂玻璃、瑞士簡約、未來感等多元品味。
- **20x20 靈活組合**：20 種佈局架構 × 20 套專業學術配色，可輕易合成出 400 種不同的視覺組合。
- **Inkscape 深度兼容**：產出的成品在 Inkscape 中可 100% 編輯文字與形狀，專為最後的手工微調而生。

- **線上圖形化介面**：全新部署於 GitHub Pages 的響應式即時編輯器，實現所見即所得的操作體驗。

---

## 🚀 立即體驗線上版 Web Builder

本專案現已全面升級，支援免本地安裝、直接透過瀏覽器開啟的圖形化工具！  
👉 **[進入 SciPoster Architect Web Builder 線上介面](https://chihhsiangchien.github.io/sciPosterArchitect/)**

透過線上版，您可以：
1. **即時組合預覽**：直接點擊切換 **20 種色彩系統** × **8 種區塊底板** × **10 種標題裝飾**，獲得高達 1,600 種排列組合。
2. **即時填鴨預覽**：左側輸入摘要、動機與研究內容，右側立刻以縮放畫布即時渲染排版結果。
3. **一鍵導出 SVG**：對排版與配色滿意後，點擊「下載」，立刻產出帶有精確渲染參數且 100% 格式友善的 SVG，無縫串接 Inkscape！

> **請注意**：產出的 SVG 若要更換自訂背景元素或是更換成其他圖片，請打開您的 Inkscape 等進階編輯器接手終極的排版與圖表植入。

---

## 📂 檔案架構說明

### 系統核心件
- `scripts/poster_resources.py`: **佈局UI與配色庫**。集中存放所有 20 種配色、20 種 UI 設計與文字演算邏輯。
- `scripts/content.json`: **科研資料中心**。使用者在此集中維護海報的所有文案。
- `scripts/generate_final_poster.py`: **正式海報引擎**。根據設定產出最終成品海報。
### Python 開發與本地批次生成模式 (Advanced Usage)

如果您是進階開發者，或需要本機大批量產生海報版型池，您也可以直接呼叫我們的 Python 核心引擎：

1. `scripts/poster_resources.py`: 核心設計系統資源庫。
2. `scripts/content.json`: 從此處外部輸入海報文案資料庫。
3. `scripts/generate_final_poster.py`: 手機設定 config，一鍵生成單一高畫質海報。
4. `scripts/generate_mocking_posters.py`: 海量生成指令碼，執行後將自動產出所有的色彩方案與佈局型錄。

> [!TIP]
> 第一階段排版建議全部使用 **[Web Builder](https://chihhsiangchien.github.io/sciPosterArchitect/)**，匯出 `SVG` 再丟進 Inkscape 做後端精密排版。只有在需要開發新元件時才需要動用到 Python 腳本。
