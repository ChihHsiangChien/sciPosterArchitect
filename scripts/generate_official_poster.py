import os
import html
import json
import poster_resources as res

# ==========================================
# 1. Configuration for Simplified Template
# ==========================================
CONFIG = {
    "UI_STYLE_ID": 8,        # Capsule Title
    "COLOR_PALETTE_ID": 5,   # Academic Red
    "OUTPUT_FILENAME": "official_scientific_poster.svg",
    "CONTENT_FILE": "content.json",
    "TEMPLATE_FILE": os.path.join("正式範本", "poster.svg")
}

# Standard Taiwan Science Fair Layout (mm) - Optimized for Unified ViewBox
LAYOUT = {
    "LEFT":   {"x": 0,    "y": 0,    "w": 650, "h": 1200, "margin": 40},
    "MIDDLE": {"x": 660,  "y": 0,    "w": 750, "h": 1200, "margin": 40},
    "RIGHT":  {"x": 1420, "y": 0,    "w": 650, "h": 1200, "margin": 40},
    "TOP":    {"x": 660,  "y": -210, "w": 750, "h": 200,  "margin": 20}
}

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scripts_dir = os.path.join(root_dir, "scripts")
    
    # 1. Load Data
    content_path = os.path.join(scripts_dir, CONFIG["CONTENT_FILE"])
    with open(content_path, "r", encoding="utf-8") as f:
        content = json.load(f)

    # 2. Load Colors (v4 System)
    pal = res.PALETTES[CONFIG["COLOR_PALETTE_ID"] - 1]
    p_c, s_c, board_bg, card_bg = pal["p"], pal["s"], pal["board_bg"], pal["card_bg"]
    t_h, t_b = pal["t_h"], pal["t_b"]

    # 3. Read Clean Template
    template_path = os.path.join(root_dir, CONFIG["TEMPLATE_FILE"])
    with open(template_path, "r", encoding="utf-8") as f:
        template_svg = f.read()

    # --- CONTENT INJECTION ---
    content_nodes = []
    
    # Global Defs
    content_nodes.append('<defs>')
    content_nodes.append(f'<linearGradient id="gradHead" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" style="stop-color:{p_c}"/><stop offset="100%" style="stop-color:{s_c}"/></linearGradient>')
    content_nodes.append('<filter id="shadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1"/></filter>')
    content_nodes.append('</defs>')

    sid = CONFIG["UI_STYLE_ID"]

    # --- TOP PANEL ---
    L_TOP = LAYOUT["TOP"]
    content_nodes.append(f'<g transform="translate({L_TOP["x"]}, {L_TOP["y"]})" id="panel_top">')
    content_nodes.append(f'<rect width="{L_TOP["w"]}" height="{L_TOP["h"]}" fill="{board_bg}" rx="5"/>')
    content_nodes.append(f'<rect width="{L_TOP["w"]}" height="18" fill="url(#gradHead)" rx="5"/>')
    # Exhibit & Serial (Enlarged)
    content_nodes.append(f'<text x="25" y="60" font-family="sans-serif" font-size="20" fill="{t_h}" font-weight="bold">{html.escape(content["exhibit"])}</text>')
    content_nodes.append(f'<text x="{L_TOP["w"]-25}" y="60" font-family="sans-serif" font-size="22" fill="{t_h}" text-anchor="end" font-weight="bold">{html.escape(content["serial"])}</text>')
    
    title_text = content["title"]
    # GIANT Title Mode
    if len(title_text) > 12:
        l1, l2 = title_text[:12], title_text[12:]
        content_nodes.append(f'<text x="{L_TOP["w"]/2}" y="115" font-family="serif" font-size="85" fill="{t_h}" font-weight="bold" text-anchor="middle">{html.escape(l1)}</text>')
        content_nodes.append(f'<text x="{L_TOP["w"]/2}" y="175" font-family="serif" font-size="75" fill="{t_h}" font-weight="bold" text-anchor="middle">{html.escape(l2)}</text>')
    else:
        content_nodes.append(f'<text x="{L_TOP["w"]/2}" y="145" font-family="serif" font-size="110" fill="{t_h}" font-weight="bold" text-anchor="middle">{html.escape(title_text)}</text>')
    content_nodes.append('</g>')

    # --- LEFT PANEL ---
    L_L = LAYOUT["LEFT"]; m = L_L["margin"]; cw = L_L["w"] - 2*m
    content_nodes.append(f'<g transform="translate({L_L["x"]}, {L_L["y"]})">')
    content_nodes.append(f'<rect width="{L_L["w"]}" height="{L_L["h"]}" fill="{board_bg}"/>')
    content_nodes.append(f'<g transform="translate({m}, {m})">')
    content_nodes.append(res.render_styled_section(0, 0, cw, 220, "摘要 (Abstract)", content["abstract"], sid, p_c, card_bg, t_h, t_b))
    content_nodes.append(res.render_styled_section(0, 260, cw, 400, "研究動機", content["motivation"], sid, p_c, card_bg, t_h, t_b))
    content_nodes.append(res.render_styled_section(0, 700, cw, 420, "研究目的與展望", content["purpose"], sid, p_c, card_bg, t_h, t_b))
    content_nodes.append('</g></g>')

    # --- MIDDLE PANEL ---
    L_M = LAYOUT["MIDDLE"]; m = L_M["margin"]; cw = L_M["w"] - 2*m
    content_nodes.append(f'<g transform="translate({L_M["x"]}, {L_M["y"]})">')
    content_nodes.append(f'<rect width="{L_M["w"]}" height="{L_M["h"]}" fill="{board_bg}"/>')
    content_nodes.append(f'<g transform="translate({m}, {m})">')
    content_nodes.append(res.render_styled_section(0, 0, cw, 600, "研究方法與系統流程", "這裡放置實驗設計圖示與模型細節。\n\n" + content["purpose"], sid, p_c, card_bg, t_h, t_b))
    content_nodes.append(res.render_styled_section(0, 650, cw, 480, "數據結果與量化分析", content["result"], sid, p_c, card_bg, t_h, t_b))
    content_nodes.append('</g></g>')

    # --- RIGHT PANEL ---
    L_R = LAYOUT["RIGHT"]; m = L_R["margin"]; cw = L_R["w"] - 2*m
    content_nodes.append(f'<g transform="translate({L_R["x"]}, {L_R["y"]})">')
    content_nodes.append(f'<rect width="{L_R["w"]}" height="{L_R["h"]}" fill="{board_bg}"/>')
    content_nodes.append(f'<g transform="translate({m}, {m})">')
    content_nodes.append(res.render_styled_section(0, 0, cw, 500, "綜合討論與分析", content["result"], sid, p_c, card_bg, t_h, t_b))
    content_nodes.append(res.render_styled_section(0, 540, cw, 340, "研究結論", "本研究成功優化了偵測效率並顯著降低運算能耗。", sid, p_c, card_bg, t_h, t_b))
    content_nodes.append(res.render_styled_section(0, 920, cw, 180, "參考文獻", content["refs"], sid, p_c, card_bg, t_h, t_b))
    content_nodes.append('</g></g>')

    # Final Injection
    merged_content = "".join(content_nodes)
    final_svg_str = template_svg.replace('id="layer_content">', f'id="layer_content">{merged_content}')

    output_path = os.path.join(root_dir, CONFIG["OUTPUT_FILENAME"])
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_svg_str)

    # PNG Export
    png_path = output_path.replace(".svg", ".png")
    try:
        import subprocess
        subprocess.run(["inkscape", "--export-filename=" + png_path, "--export-type=png", "--export-dpi=150", output_path], check=True, capture_output=True)
    except: pass
    
    print(f"✅ Clean Poster Generated: {CONFIG['OUTPUT_FILENAME']}")

if __name__ == "__main__": main()
