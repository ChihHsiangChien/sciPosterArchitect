import os
import html
import poster_resources as res
import subprocess

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scripts_dir = os.path.join(root_dir, "scripts")
    
    content = {
        "exhibit": "中華民國第二百屆中小學科學展覽會 | 應用科學科",
        "serial": "作品編號：080215-M001",
        "title": "智慧城市架構下之自動化廢棄物分類系統優化研究",
        "abstract": "本研究致力於開發高效率之自動化廢棄物分類技術，整合神經網路模型，實現低延遲預測系統。",
        "motivation": "廢棄物管理為永續展之關鍵，現今技術處理形變金屬。我們實現微秒級決策，誤判率降至 2.4% 以下。",
        "purpose": "1. 構建低功耗分辨模型。 2. 研發動態感知爪。 3. 量化運行穩定性。",
        "result": "抓取成功率 94.8%，處理通量提升 45%，數據顯示座標誤差精確收斂於 ±0.02 範圍。"
    }

    # --- 1. COLOR CATALOG (v4 - Text Pairing) ---
    catalog_path = os.path.join(root_dir, "color_system_catalog.svg")
    cat_svg = ['<svg width="850" height="2350" xmlns="http://www.w3.org/2000/svg">']
    cat_svg.append('<rect width="850" height="2350" fill="#f8fafc"/>')
    cat_svg.append('<text x="425" y="45" font-family="sans-serif" font-size="28" text-anchor="middle" font-weight="bold" fill="#0f172a">專業設計配色型錄 </text>')
    cat_svg.append('<text x="425" y="70" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#64748b">Hierarchy: Board | Card | Title Text | Body Text</text>')
    
    for i, p in enumerate(res.PALETTES):
        y = 120 + (i * 110)
        cat_svg.append(f'<g transform="translate(40, {y})">')
        cat_svg.append(f'<rect width="770" height="100" fill="{p["board_bg"]}" rx="12" stroke="#e2e8f0" stroke-width="0.5"/>')
        cat_svg.append(f'<rect x="280" y="15" width="260" height="70" fill="{p["card_bg"]}" rx="8" stroke="{p["p"]}" stroke-width="0.5" filter="url(#shadow)"/>')
        
        # Chips
        chips = [("P", p["p"], 20), ("S", p["s"], 90), ("TH", p["t_h"], 160), ("TB", p["t_b"], 220)]
        for label, color, x_offset in chips:
            cat_svg.append(f'<circle cx="{x_offset+25}" cy="35" r="18" fill="{color}" stroke="#fff" stroke-width="2"/>')
            cat_svg.append(f'<text x="{x_offset+25}" y="70" font-family="monospace" font-size="8" text-anchor="middle" fill="#64748b">{color}</text>')
            
        # Sample display inside card
        cat_svg.append(f'<text x="300" y="40" font-family="sans-serif" font-size="14" fill="{p["t_h"]}" font-weight="bold">方案 {i+1:02d}標題樣式</text>')
        cat_svg.append(f'<text x="300" y="62" font-family="sans-serif" font-size="10" fill="{p["t_b"]}">這是對比測試內文 (Matched Body Text)</text>')
        
        # Details on right
        cat_svg.append(f'<text x="560" y="42" font-family="sans-serif" font-size="12" fill="{p["t_h"]}" font-weight="bold">配對組合 {i+1:02d}</text>')
        cat_svg.append(f'<text x="560" y="62" font-family="monospace" font-size="8" fill="#94a3b8">B:{p["board_bg"]} | C:{p["card_bg"]}</text>')
        cat_svg.append('</g>')

    cat_svg.append('<defs><filter id="shadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1"/></filter></defs></svg>')
    with open(catalog_path, "w", encoding="utf-8") as f: f.write("\n".join(cat_svg))
    print(f"✅ color_system_catalog.svg updated (v4).")

    # --- 2. UI COMPONENT CATALOG (v2 - Matching BGs) ---
    ui_cat_path = os.path.join(root_dir, "ui_component_catalog.svg")
    ui_svg = ['<svg width="1000" height="3400" xmlns="http://www.w3.org/2000/svg">']
    ui_svg.append('<rect width="1000" height="3400" fill="#f1f5f9"/>')
    ui_svg.append('<text x="500" y="55" font-family="sans-serif" font-size="32" text-anchor="middle" font-weight="bold" fill="#0f172a">科展海報 UI 元件設計大賞 (全層次配套展示)</text>')
    
    for i in range(20):
        y = 150 + (i * 160)
        p = res.PALETTES[i]
        ui_svg.append(f'<g transform="translate(50, {y})">')
        ui_svg.append(f'<rect width="900" height="145" fill="{p["board_bg"]}" rx="10" stroke="#e2e8f0"/>')
        ui_svg.append(f'<text x="20" y="45" font-size="18" fill="{p["p"]}" font-weight="bold">STYLE {i+1:02d}</text>')
        ui_svg.append(f'<text x="20" y="70" font-size="9" fill="{p["t_b"]}" opacity="0.6">Hierarchy Check:</text>')
        ui_svg.append(f'<text x="20" y="85" font-size="9" fill="{p["t_b"]}">{p["board_bg"]} (B) | {p["card_bg"]} (C)</text>')
        # Use full coordination
        ui_svg.append(res.render_styled_section(220, 5, 660, 130, f"佈局風格樣式 {i+1:02d}", content["abstract"], i+1, p["p"], p["card_bg"], p["t_h"], p["t_b"]))
        ui_svg.append('</g>')
    
    ui_svg.append('<defs><filter id="shadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1"/></filter><linearGradient id="gradHead" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:#01579B"/><stop offset="100%" style="stop-color:#00B0FF"/></linearGradient></defs></svg>')
    with open(ui_cat_path, "w", encoding="utf-8") as f: f.write("\n".join(ui_svg))
    print(f"✅ ui_component_catalog.svg updated (v2).")

    # Export
    for svg_file in [catalog_path, ui_cat_path]:
        try:
            subprocess.run(["inkscape", "--export-filename=" + svg_file.replace(".svg", ".png"), "--export-type=png", "--export-dpi=150", svg_file], check=True, capture_output=True)
        except: pass

if __name__ == "__main__": main()
