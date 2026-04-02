# SciPoster Architect (科學海報架構設計)

這是一個專為科學展覽、學術研討會設計的高效率海報自動化生成系統。透過 **SciPoster Architect** 引擎，實現了 **「研究文字」** 與 **「佈局美學」** 的融合與技術分離。

## 核心優勢

- **原子化設計 (Atomic Design)**：內建 20 種高品質章節區塊 UI，涵蓋磨砂玻璃、瑞士簡約、未來感等多元品味。
- **20x20 靈活組合**：20 種佈局架構 × 20 套專業學術配色，可輕易合成出 400 種不同的視覺組合。
- **Inkscape 深度兼容**：產出的成品在 Inkscape 中可 100% 編輯文字與形狀，專為最後的手工微調而生。

---

## 📂 檔案架構說明

### 系統核心件
- `scripts/poster_resources.py`: **佈局UI與配色庫**。集中存放所有 20 種配色、20 種 UI 設計與文字演算邏輯。
- `scripts/content.json`: **科研資料中心**。使用者在此集中維護海報的所有文案。
- `scripts/generate_final_poster.py`: **正式海報引擎**。根據設定產出最終成品海報。
- `scripts/generate_mocking_posters.py`: **展示工具**。用於產出所有的視覺參考型錄。

### 三大視覺參考庫 (Reference Gallery)
1.  **`master_layout_showcase/`**: **【全海報佈局大賞】**
    *   展示每一種 UI 元件套用到「一整張完整海報」時呈現出的視覺壓力與風格表現。
2.  **`ui_component_catalog.svg`**: **【UI 元件設計型錄】**
    *   深度展示 20 種不同章節區塊（如：實心標籤、點狀格紙、圓角陰影）的細節。
3.  **`color_system_catalog.svg`**: **【配色方案型錄】**
    *   展示 20 套經測試的高對比學術配色，並附帶精確的 RGB 色碼。

---

## 正式海報製作流程 (4 Step Workflow)

### Step 1：撰寫科研文案
在 [scripts/content.json](scripts/content.json) 中填寫您的研究數據、摘要、動機與結論。

### Step 2：挑選風格母版
查看 [master_layout_showcase/](master_layout_showcase/) 查看完整預覽，選定一個 **UI 風格編號** (1-20)。
查看 [color_system_catalog.svg](color_system_catalog.svg) 選定一個 **配色編號** (1-20)。

### Step 3：引擎配置
開啟 [scripts/generate_final_poster.py](scripts/generate_final_poster.py)，在 `CONFIG` 中輸入編號：
```python
CONFIG = {
    "UI_STYLE_ID": 14,       # 輸入選定的佈局編號
    "COLOR_PALETTE_ID": 3,   # 輸入選定的配色編號
    "OUTPUT_FILENAME": "final_poster_architect.svg"
}
```

### Step 4：一鍵產出與終極微調
執行 Python 腳本生成海報，產出後建議以 **Inkscape** 開啟進行圖表置入與排版微修。

---
> [!IMPORTANT]
> 執行 `scripts/generate_mocking_posters.py` 將會自動重建上述所有的型錄與預覽目錄。
