import os
import html
import json
import poster_resources as res

# ==========================================
# 1. 配置與輸入區
# ==========================================
CONFIG = {
    "UI_STYLE_ID": 17,        # 挑選 UI 元件風格 (1-20)
    "COLOR_PALETTE_ID": 3,   # 挑選配色方案 (1-20)
    "OUTPUT_FILENAME": "final_poster_modular.svg",
    "CONTENT_FILE": "content.json" # 在此外部檔案維護文案
}

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 讀取外部文案內容
    content_path = os.path.join(root_dir, CONFIG["CONTENT_FILE"])
    if os.path.exists(content_path):
        with open(content_path, "r", encoding="utf-8") as f:
            content = json.load(f)
            print(f"✅ 已讀取外部文案檔案：{CONFIG['CONTENT_FILE']}")
    else:
        print(f"❌ 找不到文案檔案 {CONFIG['CONTENT_FILE']}，請確認路徑。")
        return

    # 讀取全域配色
    pal = res.PALETTES[CONFIG["COLOR_PALETTE_ID"] - 1]
    p_c, board_bg, card_bg = pal["p"], pal["board_bg"], pal["card_bg"]
    t_h, t_b = pal["t_h"], pal["t_b"]
    
    # 生成 SVG 畫布
    svg = ['<svg width="595" height="842" viewBox="0 0 595 842" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="595" height="842" fill="{board_bg}"/>') # 套用配套底板色
    
    # --- 頁首製作 ---
    svg.append(f'<rect width="595" height="110" fill="{p_c}"/>')
    svg.append(f'<text x="35" y="45" font-family="sans-serif" font-size="10" fill="#fff" opacity="0.8">{html.escape(content["exhibit"])}</text>')
    svg.append(f'<text x="35" y="80" font-family="serif" font-size="24" fill="#fff" font-weight="bold">{html.escape(content["title"])}</text>')
    
    # --- 模組化佈局調用 ---
    sid = CONFIG["UI_STYLE_ID"]
    svg.append(res.render_styled_section(35, 140, 175, 130, "摘要", content["abstract"], sid, p_c, card_bg, t_h, t_b))
    svg.append(res.render_styled_section(35, 290, 175, 310, "研究動機", content["motivation"], sid, p_c, card_bg, t_h, t_b))
    svg.append(res.render_styled_section(230, 140, 335, 250, "研究流程與方法", content["purpose"], sid, p_c, card_bg, t_h, t_b))
    svg.append(res.render_styled_section(230, 420, 335, 380, "結果分析報告", content["result"], sid, p_c, card_bg, t_h, t_b))
    
    # --- 腳註與引用 ---
    footer_y = 810
    svg.append(f'<line x1="35" y1="{footer_y}" x2="560" y2="{footer_y}" stroke="{p_c}" stroke-width="0.5" opacity="0.3"/>')
    svg.append(f'<text x="35" y="{footer_y + 15}" font-family="sans-serif" font-size="8" fill="#666">{html.escape(content["refs"])}</text>')
    
    # --- 資源與濾鏡定義 ---
    svg.append('<defs>')
    svg.append('<filter id="shadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1"/></filter>')
    svg.append('<pattern id="dotGrid" width="10" height="10" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#ddd"/></pattern>')
    svg.append(f'<linearGradient id="gradHead" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:{p_c}"/><stop offset="100%" style="stop-color:#00B0FF"/></linearGradient>')
    svg.append('</defs></svg>')
    
    output_path = os.path.abspath(os.path.join(root_dir, "..", CONFIG["OUTPUT_FILENAME"]))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    
    # --- PNG 產出 (Proactive Improvement) ---
    png_path = output_path.replace(".svg", ".png")
    try:
        import subprocess
        subprocess.run(["inkscape", "--export-filename=" + png_path, "--export-type=png", "--export-dpi=300", output_path], check=True, capture_output=True)
        print(f"📸 已產出 PNG 預覽 (300 DPI)：{os.path.basename(png_path)}")
    except:
        pass
    
    print(f"==========================================")
    print(f"🚀 已生成模組化海報：{CONFIG['OUTPUT_FILENAME']}")
    print(f"🎨 配色：方案 {CONFIG['COLOR_PALETTE_ID']} | 🏗️ 結構：風格 {CONFIG['UI_STYLE_ID']}")
    print(f"==========================================")

if __name__ == "__main__": main()
