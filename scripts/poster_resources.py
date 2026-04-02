import html

# --- 1. 20 PROFESSIONAL PALETTES (GENOME v4) ---
# p: Primary (Headers, Accents)
# s: Secondary (Gradients, Sub-headers)
# board_bg: Main Poster Substrate (Large boards)
# card_bg: UI Component Background (Inner cards)
# t_h: Title/Header Text Color (High contrast)
# t_b: Body/Content Text Color (Readability optimized)

PALETTES = [
    {"p": "#0D47A1", "s": "#1E88E5", "board_bg": "#F8FAFC", "card_bg": "#FFFFFF", "t_h": "#012169", "t_b": "#334155"}, # 01: Executive Blue
    {"p": "#1B5E20", "s": "#388E3C", "board_bg": "#F1F8E9", "card_bg": "#FFFFFF", "t_h": "#0D2E11", "t_b": "#2D3748"}, # 02: Forest Research
    {"p": "#B71C1C", "s": "#D32F2F", "board_bg": "#FFF5F5", "card_bg": "#FFFFFF", "t_h": "#440000", "t_b": "#4A5568"}, # 03: Academic Red
    {"p": "#E65100", "s": "#F57C00", "board_bg": "#FFF8E1", "card_bg": "#FFFFFF", "t_h": "#3E2723", "t_b": "#4A3728"}, # 04: Energy Orange
    {"p": "#4A148C", "s": "#7B1FA2", "board_bg": "#FAFAFF", "card_bg": "#FFFFFF", "t_h": "#21004A", "t_b": "#2D3748"}, # 05: Deep Purple
    {"p": "#006064", "s": "#00838F", "board_bg": "#F0FDFA", "card_bg": "#FFFFFF", "t_h": "#00241F", "t_b": "#1A365D"}, # 06: Teal Med
    {"p": "#880E4F", "s": "#AD1457", "board_bg": "#FFF1F2", "card_bg": "#FFFFFF", "t_h": "#4A0021", "t_b": "#4C1D95"}, # 07: Magenta Tech
    {"p": "#33691E", "s": "#558B2F", "board_bg": "#F9FBE7", "card_bg": "#FFFFFF", "t_h": "#1B3000", "t_b": "#365314"}, # 08: Bio Olive
    {"p": "#01579B", "s": "#0288D1", "board_bg": "#F0F9FF", "card_bg": "#FFFFFF", "t_h": "#00214A", "t_b": "#1E3A8A"}, # 09: Ocean Deep
    {"p": "#BF360C", "s": "#D84315", "board_bg": "#FFF7ED", "card_bg": "#FFFFFF", "t_h": "#441200", "t_b": "#431407"}, # 10: Earth Terra
    {"p": "#374151", "s": "#4B5563", "board_bg": "#F3F4F6", "card_bg": "#FFFFFF", "t_h": "#111827", "t_b": "#374151"}, # 11: Slate Modern
    {"p": "#1E1B4B", "s": "#312E81", "board_bg": "#EEF2FF", "card_bg": "#FFFFFF", "t_h": "#1E1B4B", "t_b": "#312E81"}, # 12: Indigo Night
    {"p": "#064E3B", "s": "#065F46", "board_bg": "#ECFDF5", "card_bg": "#FFFFFF", "t_h": "#064E3B", "t_b": "#065F46"}, # 13: Emerald
    {"p": "#451A03", "s": "#78350F", "board_bg": "#FFFBEB", "card_bg": "#FFFFFF", "t_h": "#451A03", "t_b": "#78350F"}, # 14: Amber Gold
    {"p": "#333333", "s": "#666666", "board_bg": "#FFFFFF", "card_bg": "#F9FAFB", "t_h": "#000000", "t_b": "#4B5563"}, # 15: Clean White
    {"p": "#1E293B", "s": "#334155", "board_bg": "#F1F5F9", "card_bg": "#FFFFFF", "t_h": "#020617", "t_b": "#1E293B"}, # 16: Iron Grey
    {"p": "#0F172A", "s": "#1E293B", "board_bg": "#FFFFFF", "card_bg": "#F8FAFC", "t_h": "#0F172A", "t_b": "#334155"}, # 17: Paper Ink
    {"p": "#7C2D12", "s": "#9A3412", "board_bg": "#FFF7ED", "card_bg": "#FFFFFF", "t_h": "#7C2D12", "t_b": "#9A3412"}, # 18: Burnt Orange
    {"p": "#4C1D95", "s": "#5B21B6", "board_bg": "#F5F3FF", "card_bg": "#FFFFFF", "t_h": "#4C1D95", "t_b": "#5B21B6"}, # 19: Violet Soft
    {"p": "#000000", "s": "#222222", "board_bg": "#E5E7EB", "card_bg": "#FFFFFF", "t_h": "#000000", "t_b": "#1F2937"}, # 20: Industrial
]

# --- 2. SAFE MULTI-LINE TEXT ---
def render_safe_text(x, y, width, font_size, line_height, text, color="#333", align="left"):
    lines_raw = text.split('\n')
    chars_per_line = int(width / (font_size * 1.1))
    wrapped_lines = []
    for line in lines_raw:
        if not line.strip():
            wrapped_lines.append("")
            continue
        for i in range(0, len(line), chars_per_line):
            wrapped_lines.append(line[i:i + chars_per_line])
    anchor = "start" if align=="left" else "middle"
    res = f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{font_size}" fill="{color}" text-anchor="{anchor}">'
    for i, line_content in enumerate(wrapped_lines[:80]):
        safe_line = html.escape(line_content)
        dy = font_size * line_height if i > 0 else 0
        res += f'<tspan x="{x}" dy="{dy}">{safe_line}</tspan>'
    res += '</text>'
    return res

# --- 3. UI RENDERERS (v5 with High-Visibility Large Type) ---
def render_styled_section(x, y, w, h, title, content, style_id, p_c, card_bg, t_h, t_b):
    res = f'<g transform="translate({x}, {y})">'
    sid = (style_id - 1) % 20
    s_title = html.escape(title)

    # Styles implementation with ENLARGED type
    if sid == 0: # Solid
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" stroke="{p_c}" stroke-width="1"/><rect width="{w}" height="40" fill="{p_c}"/><text x="20" y="28" font-size="24" fill="#fff" font-weight="bold">{s_title}</text>'
    elif sid == 1: # Shadow Rounded
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" rx="15" stroke="#eee" filter="url(#shadow)"/><text x="20" y="40" font-size="24" fill="{t_h}" font-weight="bold">● {s_title}</text>'
    elif sid == 2: # Left Border Accent
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}"/><path d="M 0,0 V {h}" stroke="{p_c}" stroke-width="12"/><text x="25" y="32" font-size="26" fill="{t_h}" font-weight="bold">{s_title}</text>'
    elif sid == 3: # Minimalist Underline
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" opacity="0.3"/><text x="0" y="35" font-size="32" fill="{t_h}" font-weight="900" style="text-transform:uppercase">{s_title}</text><path d="M 0,45 H {w}" stroke="{p_c}" stroke-width="4"/>'
    elif sid == 4: # Double Border
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" stroke="{p_c}" stroke-width="2"/><rect x="6" y="6" width="{w-12}" height="{h-12}" fill="none" stroke="{p_c}" stroke-width="0.8" opacity="0.4"/><text x="20" y="42" font-size="22" fill="{t_h}" font-weight="bold">{s_title}</text>'
    elif sid == 5: # Capsule Title
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" rx="8" stroke="#ddd"/><rect x="20" y="-18" width="180" height="36" rx="18" fill="{p_c}"/><text x="110" y="8" font-size="18" fill="{fff}" text-anchor="middle" font-weight="bold">{s_title}</text>'
    elif sid == 6: # Dots Grid
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" stroke="{p_c}" stroke-dasharray="2,6"/><text x="20" y="45" font-size="26" fill="{t_h}" font-weight="bold"># {s_title}</text>'
    elif sid == 7: # Gradient Top
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" rx="10" stroke="#ccc"/><rect width="{w}" height="50" fill="url(#gradHead)" rx="10"/><text x="20" y="35" font-size="24" fill="#fff" font-weight="bold">{s_title}</text>'
    elif sid == 8: # Modern Glass
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" fill-opacity="0.8" rx="25" stroke="#fff" stroke-opacity="0.5"/><text x="30" y="45" font-size="28" fill="{t_h}" font-weight="800">{s_title}</text>'
    elif sid == 9: # Journal Serif
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" stroke="#333" stroke-width="3"/><line x1="20" y1="55" x2="{w-20}" y2="55" stroke="#333" stroke-width="1.5"/><text x="20" y="40" font-family="serif" font-size="28" fill="{t_h}" font-weight="bold">{s_title}</text>'
    elif sid == 10: # Bracket Style
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}"/><path d="M 30,0 H 0 V {h} H 30" fill="none" stroke="{p_c}" stroke-width="5"/><path d="M {w-30},0 H {w} V {h} H {w-30}" fill="none" stroke="{p_c}" stroke-width="5"/><text x="{w/2}" y="40" font-size="26" fill="{t_h}" text-anchor="middle" font-weight="bold">{s_title}</text>'
    elif sid == 11: # Tag Style
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" rx="5" stroke="#eee"/><path d="M 0,0 H 60 L 75,22.5 L 60,45 H 0 Z" fill="{p_c}"/><text x="30" y="30" font-size="16" fill="#fff" text-anchor="middle" font-weight="bold">{s_title[:4]}</text>'
    elif sid == 12: # Geometric Corner
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" stroke="{p_c}" stroke-width="2"/><polygon points="0,0 60,0 0,60" fill="{p_c}"/><text x="70" y="45" font-size="26" fill="{t_h}" font-weight="bold">{s_title}</text>'
    elif sid == 13: # Clean Float
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" filter="url(#shadow)" rx="10"/><text x="0" y="-15" font-size="28" fill="{t_h}" font-weight="bold">{s_title}</text>'
    elif sid == 14: # Outline Bold
        res += f'<rect x="4" y="4" width="{w}" height="{h}" fill="none" stroke="{p_c}" opacity="0.4"/><rect width="{w}" height="{h}" fill="{card_bg}" stroke="{p_c}" stroke-width="3"/><text x="20" y="45" font-size="32" fill="{t_h}" font-weight="900">{s_title}</text>'
    elif sid == 15: # Circle Bullet
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}"/><circle cx="25" cy="30" r="15" fill="{p_c}"/><text x="55" y="40" font-size="26" fill="{t_h}" font-weight="bold">{s_title}</text>'
    elif sid == 16: # Top Notch
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" stroke="#ddd"/><path d="M 0,0 H {w/2}" stroke="{p_c}" stroke-width="15"/><text x="20" y="55" font-size="28" fill="{t_h}" font-weight="bold">{s_title}</text>'
    elif sid == 17: # Slanted Header
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" stroke="#eee"/><path d="M 0,0 H {w} V 60 L 0,30 Z" fill="{p_c}"/><text x="20" y="40" font-size="20" fill="#fff" font-weight="bold">{s_title}</text>'
    elif sid == 18: # Cyber Line
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}"/><path d="M 0,45 H {w}" stroke="{p_c}" stroke-width="1"/><path d="M 0,52 H {w/2}" stroke="{p_c}" stroke-width="5"/><text x="0" y="32" font-size="32" fill="{t_h}" font-weight="bold" font-style="italic">{s_title}</text>'
    elif sid == 19: # Leaf Style
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" rx="40 0 40 0" stroke="{p_c}" stroke-width="2"/><text x="{w/2}" y="45" font-size="26" fill="{t_h}" text-anchor="middle" font-weight="bold">◈ {s_title} ◈</text>'
    else: # Default
        res += f'<rect width="{w}" height="{h}" fill="{card_bg}" stroke="#ccc"/><text x="10" y="30" font-size="20" fill="{t_h}" font-weight="bold">{s_title}</text>'
    
    # ENLARGED Body Text: Default font_size = 15
    if content:
        res += render_safe_text(20, 70 if sid!=3 else 80, w-40, 15, 1.4, content, color=t_b)
    
    res += '</g>'
    return res
