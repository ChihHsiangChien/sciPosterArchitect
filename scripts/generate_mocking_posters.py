import os
import html
import poster_resources as res
import subprocess

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 預設公用文案
    content = {
        "exhibit": "中華民國第二百屆中小學科學展覽會 | 應用科學科",
        "serial": "編號：080215-M001 | 國立中學",
        "title": "智慧城市架構下之自動化廢棄物分類系統優化研究",
        "abstract": "請查看此摘要區塊之佈局壓力與自動分行效果表現，此處填入高密度科研文字，以便測試。此技術完全兼容於 Inkscape。",
        "motivation": "廢棄物管理為永續展之關鍵，現今技術處理形變金屬與素材。我們於端點實現微秒級決策。經 5 萬組樣本驗證，誤判率降至 2.4% 以下。",
        "purpose": "1. 構建低功耗分辨模型。 2. 研發動態感知爪。 3. 量化運行穩定性。目標達成 60 FPS 以上處理效率。",
        "result": "抓取成功率 94.8%，處理通量提升 45%，數據顯示座標誤差精確收斂於 ±0.02 範圍。顯著性檢定 (p < 0.001)。"
    }

    # --- 1. GENERATE COLOR SYSTEM CATALOG ---
    catalog_path = os.path.abspath(os.path.join(root_dir, "..", "color_system_catalog.svg"))
    # 增加寬度與高度以容納更多資訊 (20x105 + 100 = 2200)
    cat_svg = ['<svg width="850" height="2250" xmlns="http://www.w3.org/2000/svg">']
    cat_svg.append('<rect width="850" height="2250" fill="#f4f6f8"/>')
    cat_svg.append('<text x="425" y="45" font-family="sans-serif" font-size="24" text-anchor="middle" font-weight="bold" fill="#333">專業配色型錄 (含 HEX &amp; RGB)</text>')
    
    for i, p in enumerate(res.PALETTES):
        y = 100 + (i * 105)
        cat_svg.append(f'<g transform="translate(40, {y})"><rect width="770" height="90" fill="#fff" rx="12" stroke="#ddd" stroke-width="0.5"/>')
        
        # Primary (間距拉開到 120px)
        rgb_p = f"rgb{hex_to_rgb(p['p'])}"
        cat_svg.append(f'<rect x="15" y="15" width="40" height="40" fill="{p["p"]}" rx="5"/><text x="15" y="68" font-family="monospace" font-size="8" fill="#666" font-weight="bold">{p["p"]}</text><text x="15" y="80" font-family="monospace" font-size="7" fill="#888">{rgb_p}</text>')
        
        # Secondary
        rgb_s = f"rgb{hex_to_rgb(p['s'])}"
        cat_svg.append(f'<rect x="135" y="15" width="40" height="40" fill="{p["s"]}" rx="5"/><text x="135" y="68" font-family="monospace" font-size="8" fill="#666">{p["s"]}</text><text x="135" y="80" font-family="monospace" font-size="7" fill="#888">{rgb_s}</text>')
        
        # BG
        rgb_bg = f"rgb{hex_to_rgb(p['bg'])}"
        cat_svg.append(f'<rect x="255" y="15" width="40" height="40" fill="{p["bg"]}" rx="5" stroke="#eee"/><text x="255" y="68" font-family="monospace" font-size="8" fill="#666">{p["bg"]}</text><text x="255" y="80" font-family="monospace" font-size="7" fill="#888">{rgb_bg}</text>')
        
        # 文字描述往右移到 400
        cat_svg.append(f'<text x="400" y="32" font-family="sans-serif" font-size="14" fill="{p["p"]}" font-weight="bold">方案 {i+1:02d} | 標題文字樣式</text>')
        cat_svg.append(f'<text x="400" y="55" font-family="sans-serif" font-size="10" fill="#666">這是可讀性測試文字 (Scheme Preview Content)</text></g>')


    cat_svg.append('</svg>')
    with open(catalog_path, "w", encoding="utf-8") as f: f.write("\n".join(cat_svg))
    print(f"✅ 配色型錄已更新：color_system_catalog.svg")
    
    # 產出 PNG 預覽 (使用實體背景)
    cat_png_path = catalog_path.replace(".svg", ".png")
    try:
        subprocess.run(["inkscape", "--export-filename=" + cat_png_path, "--export-type=png", "--export-dpi=150", catalog_path], check=True, capture_output=True)
        print(f"📸 配色型錄 PNG 已產出 (附帶實體背景)：color_system_catalog.png")
    except: pass

    # --- 2. GENERATE UI COMPONENT CATALOG ---
    ui_cat_path = os.path.abspath(os.path.join(root_dir, "..", "ui_component_catalog.svg"))
    ui_svg = ['<svg width="1000" height="3400" xmlns="http://www.w3.org/2000/svg">']
    ui_svg.append('<rect width="1000" height="3400" fill="#f5f7f9"/>') # 加入實體背景色避免透明導致預覽困難
    ui_svg.append('<text x="500" y="55" font-family="sans-serif" font-size="32" text-anchor="middle" font-weight="bold">科展海報 UI 元件設計大賞 (全 20 套展示)</text>')
    for i in range(20):
        y = 150 + (i * 160)
        ui_svg.append(f'<g transform="translate(50, {y})">')
        ui_svg.append(f'<text x="0" y="65" font-size="18" font-weight="bold">STYLE {i+1:02d}</text>')
        ui_svg.append(res.render_styled_section(220, 0, 720, 140, f"預覽佈局風格 {i+1:02d}", content["abstract"], i+1, "#01579B", "#E1F5FE"))
        ui_svg.append('</g>')
        ui_svg.append(f'<line x1="50" y1="{y + 150}" x2="950" y2="{y + 150}" stroke="#ddd" stroke-width="1"/>')
    ui_svg.append('<defs><filter id="shadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1"/></filter><pattern id="dotGrid" width="10" height="10" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#ddd"/></pattern><linearGradient id="gradHead" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:#01579B"/><stop offset="100%" style="stop-color:#00B0FF"/></linearGradient></defs></svg>')
    with open(ui_cat_path, "w", encoding="utf-8") as f: f.write("\n".join(ui_svg))
    print(f"✅ UI 元件型錄已更新：ui_component_catalog.svg")

    # 產出 PNG 預覽 (使用實體背景)
    ui_png_path = ui_cat_path.replace(".svg", ".png")
    try:
        subprocess.run(["inkscape", "--export-filename=" + ui_png_path, "--export-type=png", "--export-dpi=150", ui_cat_path], check=True, capture_output=True)
        print(f"📸 UI 元件型錄 PNG 已產出 (附帶實體背景)：ui_component_catalog.png")
    except: pass

    # --- 3. GENERATE MASTER LAYOUT SHOWCASE (FULL POSTERS) ---
    showcase_dir = os.path.abspath(os.path.join(root_dir, "..", "master_layout_showcase"))
    if not os.path.exists(showcase_dir): os.makedirs(showcase_dir)
    p_c, bg_c = "#01579B", "#E1F5FE" # Use unified comparison blue
    for i in range(20):
        svg = [f'<svg width="595" height="842" viewBox="0 0 595 842" xmlns="http://www.w3.org/2000/svg">']
        svg.append('<rect width="595" height="842" fill="#fafafa"/>')
        svg.append(f'<rect width="595" height="110" fill="{p_c}"/>')
        svg.append(f'<text x="35" y="45" font-family="sans-serif" font-size="10" fill="#fff" opacity="0.8">{html.escape(content["exhibit"])} | STYLE-{i+1:02d}</text>')
        svg.append(f'<text x="35" y="80" font-family="serif" font-size="24" fill="#fff" font-weight="bold">{html.escape(content["title"])}</text>')
        svg.append(res.render_styled_section(35, 140, 175, 130, "摘要", content["abstract"], i+1, p_c, bg_c))
        svg.append(res.render_styled_section(35, 290, 175, 310, "研究動機", content["motivation"], i+1, p_c, bg_c))
        svg.append(res.render_styled_section(230, 140, 335, 250, "研究流程與方法", content["purpose"], i+1, p_c, bg_c))
        svg.append(res.render_styled_section(230, 420, 335, 380, "結果分析報告", content["result"], i+1, p_c, bg_c))
        svg.append('<defs><filter id="shadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1"/></filter><pattern id="dotGrid" width="10" height="10" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#ddd"/></pattern><linearGradient id="gradHead" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:#01579B"/><stop offset="100%" style="stop-color:#00B0FF"/></linearGradient></defs></svg>')
        svg_file = os.path.join(showcase_dir, f"full_poster_style_{i+1:02d}.svg")
        with open(svg_file, "w", encoding="utf-8") as f: f.write("\n".join(svg))
        
        # 產出 PNG 預覽
        png_file = svg_file.replace(".svg", ".png")
        try:
            subprocess.run(["inkscape", "--export-filename=" + png_file, "--export-type=png", "--export-dpi=150", svg_file], check=True, capture_output=True)
            print(f"Generated Style Poster: {i+1:02d} (SVG + PNG)")
        except:
            print(f"Generated Style Poster: {i+1:02d} (SVG only)")
            
    print(f"✅ 全套 20 種佈局海報已產出於：master_layout_showcase/ (含 PNG 預覽)")

if __name__ == "__main__": main()
