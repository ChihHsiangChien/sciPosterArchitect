import html

# --- 1. 20 PROFESSIONAL PALETTES (GENOME) ---
PALETTES = [
    {"p": "#0D47A1", "s": "#1E88E5", "bg": "#E3F2FD", "t": "#012169"}, # 01
    {"p": "#1B5E20", "s": "#388E3C", "bg": "#E8F5E9", "t": "#0D2E11"},
    {"p": "#B71C1C", "s": "#D32F2F", "bg": "#FFEBEE", "t": "#440000"},
    {"p": "#E65100", "s": "#F57C00", "bg": "#FFF3E0", "t": "#3E2723"},
    {"p": "#4A148C", "s": "#7B1FA2", "bg": "#F3E5F5", "t": "#21004A"},
    {"p": "#006064", "s": "#00838F", "bg": "#E0F7FA", "t": "#00241f"},
    {"p": "#880E4F", "s": "#AD1457", "bg": "#FCE4EC", "t": "#4A0021"},
    {"p": "#33691E", "s": "#558B2F", "bg": "#F1F8E9", "t": "#1B3000"},
    {"p": "#01579B", "s": "#0288D1", "bg": "#E1F5FE", "t": "#00214a"},
    {"p": "#BF360C", "s": "#D84315", "bg": "#FBE9E7", "t": "#441200"},
    {"p": "#263238", "s": "#455A64", "bg": "#ECEFF1", "t": "#101010"},
    {"p": "#1A237E", "s": "#303F9F", "bg": "#C5CAE9", "t": "#000033"},
    {"p": "#004D40", "s": "#00695C", "bg": "#B2DFDB", "t": "#00241f"},
    {"p": "#3E2723", "s": "#5D4037", "bg": "#EFEBE9", "t": "#210000"},
    {"p": "#F57F17", "s": "#FBC02D", "bg": "#FFF9C4", "t": "#332200"},
    {"p": "#212121", "s": "#424242", "bg": "#eeeeee", "t": "#000000"},
    {"p": "#0D47A1", "s": "#2962FF", "bg": "#BBDEFB", "t": "#012169"},
    {"p": "#2E7D32", "s": "#00C853", "bg": "#DCEDC8", "t": "#0D2E11"},
    {"p": "#C62828", "s": "#FF1744", "bg": "#FFCCBC", "t": "#440000"},
    {"p": "#311B92", "s": "#651FFF", "bg": "#D1C4E9", "t": "#1A237E"}
]

# --- 2. SAFE MULTI-LINE TEXT (Inkscape Ready) ---
def render_safe_text(x, y, width, font_size, line_height, text, color="#333", align="left"):
    # Clear escaping & manual wrap
    chars_per_line = int(width / (font_size * 1.05))
    raw_lines = [text[i:i + chars_per_line] for i in range(0, len(text), chars_per_line)]
    anchor = "start" if align=="left" else "middle"
    res = f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{font_size}" fill="{color}" text-anchor="{anchor}">'
    for i, raw_line in enumerate(raw_lines[:30]):
        safe_line = html.escape(raw_line)
        dy = font_size * line_height if i > 0 else 0
        res += f'<tspan x="{x}" dy="{dy}">{safe_line}</tspan>'
    res += '</text>'
    return res

# --- 3. ALL 20 UNIQUE UI RENDERERS ---
def render_styled_section(x, y, w, h, title, content, style_id, p_c, bg_c):
    res = f'<g transform="translate({x}, {y})">'
    sid = (style_id - 1) % 20
    s_title = html.escape(title)

    if sid == 0: # Solid
        res += f'<rect width="{w}" height="{h}" fill="#fff" stroke="{p_c}" stroke-width="0.8"/><rect width="{w}" height="24" fill="{p_c}"/><text x="10" y="16" font-size="12" fill="#fff" font-weight="bold">{s_title}</text>'
    elif sid == 1: # Shadow Rounded
        res += f'<rect width="{w}" height="{h}" fill="#fff" rx="15" stroke="#eee" filter="url(#shadow)"/><text x="12" y="24" font-size="12" fill="{p_c}" font-weight="bold">● {s_title}</text>'
    elif sid == 2: # Thin Line
        res += f'<line x1="0" y1="22" x2="{w}" y2="22" stroke="{p_c}" stroke-width="3"/><text x="0" y="16" font-size="14" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 3: # Side Accent
        res += f'<rect width="8" height="{h}" fill="{p_c}"/><text x="18" y="20" font-size="13" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 4: # Shaded Inset
        res += f'<rect width="{w}" height="{h}" fill="#fff" rx="10" stroke="#ddd"/><rect width="{w}" height="32" fill="{bg_c}" rx="10"/><rect y="20" width="{w}" height="12" fill="{bg_c}"/><text x="12" y="22" font-size="12" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 5: # Dashed Blueprint
        res += f'<rect width="{w}" height="{h}" fill="none" stroke="{p_c}" stroke-dasharray="4,2"/><rect width="100" height="22" fill="{p_c}"/><text x="10" y="16" font-size="11" fill="#fff">{s_title}</text>'
    elif sid == 6: # Offset Floating
        res += f'<rect width="{w}" height="{h}" fill="#fff" stroke="#ddd" rx="5"/><rect x="15" y="-12" width="120" height="24" fill="{p_c}" rx="5"/><text x="25" y="4" font-size="11" fill="#fff" font-weight="bold">{s_title}</text>'
    elif sid == 7: # Flow Node
        res += f'<line x1="-12" y1="12" x2="-12" y2="{h}" stroke="{p_c}" stroke-width="2" stroke-dasharray="2,2"/><circle cx="-12" cy="12" r="6" fill="{p_c}"/><text x="10" y="18" font-size="14" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 8: # Banded Header
        res += f'<rect width="{w}" height="6" fill="{p_c}"/><rect y="6" width="{w}" height="{h-6}" fill="{bg_c}" opacity="0.3"/><text x="0" y="25" font-size="14" fill="{p_c}" font-weight="bold">{s_title.upper()}</text>'
    elif sid == 9: # Brackets
        res += f'<path d="M20,0 L0,0 L0,20" fill="none" stroke="{p_c}" stroke-width="3"/><path d="M{w-20},{h} L{w},{h} L{w},{h-20}" fill="none" stroke="{p_c}" stroke-width="3"/><text x="12" y="24" font-size="14" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 10: # Journal Serif
        res += f'<line x1="0" y1="0" x2="{w}" y2="0" stroke="#000" stroke-width="2"/><text x="0" y="22" font-family="serif" font-size="16" fill="#000" font-weight="bold">{s_title}</text>'
    elif sid == 11: # Number Badge
        res += f'<circle cx="20" cy="20" r="22" fill="{bg_c}" stroke="{p_c}"/><text x="20" y="28" text-anchor="middle" font-size="22" fill="{p_c}" font-weight="bold">★</text><text x="55" y="26" font-size="14" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 12: # Geometric Badge
        res += f'<rect width="{w}" height="{h}" fill="#fff" stroke="#ddd"/><path d="M0,0 L40,0 L0,40 Z" fill="{p_c}"/><text x="45" y="20" font-size="12" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 13: # Glassmorphism
        res += f'<rect width="{w}" height="{h}" fill="#fff" fill-opacity="0.8" stroke="#fff" stroke-width="1" rx="12" filter="url(#shadow)"/><text x="15" y="24" font-size="13" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 14: # Organic Soft
        res += f'<rect width="{w}" height="{h}" fill="#fff" stroke="{p_c}" stroke-width="0.5" rx="30 5 30 5"/><text x="30" y="24" font-size="13" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 15: # Swiss Heavy
        res += f'<rect width="{w}" height="{h}" fill="#fff" stroke="#000" stroke-width="4"/><rect width="{w}" height="32" fill="#000"/><text x="10" y="22" font-size="14" fill="#fff" font-weight="bold">{s_title.upper()}</text>'
    elif sid == 16: # Dotted Background
        res += f'<rect width="{w}" height="{h}" fill="url(#dotGrid)" stroke="#ddd"/><rect x="10" y="8" width="100" height="22" fill="#fff" stroke="{p_c}"/><text x="18" y="24" font-size="11" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 17: # Clean Title-only
        res += f'<rect width="{w}" height="{h}" fill="none" stroke="#eee"/><text x="0" y="15" font-size="13" fill="{p_c}" font-weight="bold" text-decoration="underline">{s_title}</text>'
    elif sid == 18: # Double Inset Border
        res += f'<rect width="{w}" height="{h}" fill="none" stroke="{p_c}" stroke-width="4" opacity="0.1"/><rect x="6" y="6" width="{w-12}" height="{h-12}" fill="#fff" stroke="{p_c}" stroke-width="1"/><text x="16" y="28" font-size="13" fill="{p_c}" font-weight="bold">{s_title}</text>'
    elif sid == 19: # Linear Gradient Head
        res += f'<rect width="{w}" height="{h}" fill="#fff" stroke="#ddd" rx="4"/><rect width="{w}" height="35" fill="url(#gradHead)" rx="4"/><text x="12" y="24" font-size="13" fill="#fff" font-weight="bold">{s_title}</text>'
    else: # Fallback Box
        res += f'<rect width="{w}" height="{h}" fill="#fff" stroke="#ddd"/><text x="10" y="20" font-size="12" fill="{p_c}" font-weight="bold">{s_title}</text>'

    res += render_safe_text(12, 50 if sid!=2 else 40, w-24, 10.5, 1.6, content)
    res += '</g>'
    return res
