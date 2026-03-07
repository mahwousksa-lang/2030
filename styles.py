"""
styles.py - التصميم v20.0 — بطاقات محسنة + عرض المنافسين
"""

def get_styles():
    return get_main_css()

def get_main_css():
    return """<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
*{font-family:'Tajawal',sans-serif!important}
.main .block-container{max-width:1400px;padding:1rem 2rem}
.stat-card{background:#1A1A2E;border-radius:12px;padding:16px;text-align:center;border:1px solid #333344}
.stat-card:hover{box-shadow:0 4px 16px rgba(108,99,255,.15);border-color:#6C63FF}
.stat-card .num{font-size:2.2rem;font-weight:900;margin:4px 0}
.stat-card .lbl{font-size:.85rem;color:#8B8B8B}
.cmp-table{width:100%;border-collapse:separate;border-spacing:0;border-radius:8px;overflow:hidden;font-size:.88rem}
.cmp-table thead th{background:#16213e;color:#fff;padding:10px 8px;font-weight:700;text-align:center;border-bottom:2px solid #6C63FF;position:sticky;top:0;z-index:10}
.cmp-table tbody tr:nth-child(even){background:rgba(26,26,46,.4)}
.cmp-table tbody tr:hover{background:rgba(108,99,255,.1)!important}
.cmp-table td{padding:8px 6px;text-align:center;border-bottom:1px solid rgba(51,51,68,.4);vertical-align:middle}
.td-our{background:rgba(108,99,255,.06)!important;border-right:3px solid #6C63FF;text-align:right!important;font-weight:600;color:#B8B4FF;max-width:250px;word-wrap:break-word}
.td-comp{background:rgba(255,152,0,.06)!important;border-left:3px solid #ff9800;text-align:right!important;font-weight:600;color:#FFD180;max-width:250px;word-wrap:break-word}
.badge{display:inline-block;padding:2px 8px;border-radius:12px;font-size:.75rem;font-weight:700}
.b-high{background:rgba(255,23,68,.15);color:#FF1744;border:1px solid #FF1744}
.b-med{background:rgba(255,214,0,.15);color:#FFD600;border:1px solid #FFD600}
.b-low{background:rgba(0,200,83,.15);color:#00C853;border:1px solid #00C853}
.conf-bar{width:100%;height:6px;background:rgba(255,255,255,.08);border-radius:3px;overflow:hidden}
.conf-fill{height:100%;border-radius:3px}
/* ── بطاقة VS المحسنة مع المنافسين ── */
.vs-row{display:grid;grid-template-columns:1fr 36px 1fr;gap:10px;align-items:center;padding:12px;background:#1A1A2E;border-radius:8px 8px 0 0;margin:5px 0 0 0;border:1px solid #333344;border-bottom:none}
.vs-badge{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:.7rem}
.our-s{text-align:right;padding:8px;background:rgba(108,99,255,.04);border-radius:6px;border-right:3px solid #6C63FF}
.comp-s{text-align:left;padding:8px;background:rgba(255,152,0,.04);border-radius:6px;border-left:3px solid #ff9800}
.action-btn{display:inline-block;padding:4px 10px;border-radius:6px;font-size:.75rem;font-weight:700;cursor:pointer;margin:2px;border:1px solid}
.btn-approve{background:rgba(0,200,83,.1);color:#00C853;border-color:#00C853}
.btn-remove{background:rgba(255,23,68,.1);color:#FF1744;border-color:#FF1744}
.btn-delay{background:rgba(255,152,0,.1);color:#ff9800;border-color:#ff9800}
.btn-export{background:rgba(108,99,255,.1);color:#6C63FF;border-color:#6C63FF}
.ai-box{background:#1A1A2E;padding:12px;border-radius:8px;border:1px solid #333344;margin:6px 0}
.paste-area{background:#0E1117;border:2px dashed #333344;border-radius:8px;padding:12px;min-height:80px}
.multi-comp{background:rgba(0,123,255,.06);border:1px solid rgba(0,123,255,.2);border-radius:6px;padding:8px;margin:4px 0}
/* ── شريط المنافسين المصغر ── */
.comp-strip{background:#0e1628;border:1px solid #333344;border-top:none;border-radius:0 0 8px 8px;padding:8px 12px;margin:0 0 2px 0;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.comp-chip{display:inline-flex;align-items:center;gap:4px;padding:3px 8px;border-radius:14px;font-size:.72rem;font-weight:600;border:1px solid;white-space:nowrap}
.comp-chip.leader{background:rgba(255,152,0,.12);border-color:#ff9800;color:#ffb74d}
.comp-chip.normal{background:rgba(108,99,255,.08);border-color:#333366;color:#9e9eff}
.comp-chip .cp-name{max-width:100px;overflow:hidden;text-overflow:ellipsis}
.comp-chip .cp-price{font-weight:900}
/* ── بطاقة المنتج المفقود المحسنة ── */
.miss-card{border-radius:10px;padding:14px;margin:6px 0;background:linear-gradient(135deg,#0a1628,#0e1a30)}
.miss-card .miss-header{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.miss-card .miss-info{flex:1}
.miss-card .miss-name{font-weight:700;color:#4fc3f7;font-size:1rem}
.miss-card .miss-meta{font-size:.75rem;color:#888;margin-top:4px}
.miss-card .miss-prices{text-align:left;min-width:120px}
.miss-card .miss-comp-price{font-size:1.2rem;font-weight:900;color:#ff9800}
.miss-card .miss-suggested{font-size:.72rem;color:#4caf50}
/* ── شارات الثقة ── */
.trust-badge{display:inline-block;padding:2px 8px;border-radius:10px;font-size:.68rem;font-weight:700;margin-right:4px}
.trust-green{background:rgba(0,200,83,.15);color:#00C853;border:1px solid #00C85366}
.trust-yellow{background:rgba(255,214,0,.15);color:#FFD600;border:1px solid #FFD60066}
.trust-red{background:rgba(255,23,68,.15);color:#FF1744;border:1px solid #FF174466}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#0E1117,#1A1A2E);transition:all .3s ease}
#MainMenu,footer,header{visibility:hidden}
/* إصلاح أيقونات Streamlit */
[data-testid="stExpander"] summary svg,
[data-testid="stSelectbox"] svg[data-testid="stExpanderToggleIcon"],
details summary span[data-testid] svg {
    font-family: system-ui, -apple-system, sans-serif !important;
}
[data-testid="stExpander"] summary {
    direction: rtl;
    font-family: 'Tajawal', sans-serif !important;
}
.stSelectbox label, .stMultiSelect label {
    direction: rtl;
    font-family: 'Tajawal', sans-serif !important;
}
/* ── زر إخفاء/إظهار القائمة الجانبية ── */
#sidebar-toggle-btn {
    position: fixed;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    z-index: 99999;
    background: linear-gradient(180deg,#6C63FF,#4a42cc);
    color: #fff;
    border: none;
    border-radius: 0 10px 10px 0;
    width: 20px;
    height: 64px;
    cursor: pointer;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 3px 0 10px rgba(108,99,255,.5);
    transition: all .25s ease;
    padding: 0;
    line-height: 1;
}
#sidebar-toggle-btn:hover {
    width: 26px;
    background: linear-gradient(180deg,#7c74ff,#5a52dc);
    box-shadow: 4px 0 14px rgba(108,99,255,.7);
}
#sidebar-toggle-btn .arrow {
    font-size: 14px;
    font-style: normal;
    transition: transform .25s ease;
}
</style>"""


def get_sidebar_toggle_js():
    """JavaScript لزر إخفاء/إظهار القائمة الجانبية"""
    return """
<button id="sidebar-toggle-btn" onclick="toggleSidebar()" title="إخفاء/إظهار القائمة">
  <span class="arrow" id="toggle-arrow">◀</span>
</button>
<script>
(function() {
    var _hidden = false;

    function toggleSidebar() {
        var sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
        var btn     = window.parent.document.getElementById('sidebar-toggle-btn');
        var arrow   = window.parent.document.getElementById('toggle-arrow');
        if (!sidebar) return;

        _hidden = !_hidden;
        if (_hidden) {
            sidebar.style.display = 'none';
            btn.style.left = '0px';
            if (arrow) arrow.textContent = '▶';
        } else {
            sidebar.style.display = '';
            if (arrow) arrow.textContent = '◀';
        }
    }

    // تأكد أن الزر موجود في الـ parent document
    window.parent.toggleSidebar = toggleSidebar;

    // نقل الزر إلى parent document إذا كان في iframe
    window.addEventListener('load', function() {
        var existingBtn = window.parent.document.getElementById('sidebar-toggle-btn');
        if (!existingBtn) {
            var btn = document.getElementById('sidebar-toggle-btn');
            if (btn) {
                window.parent.document.body.appendChild(btn.cloneNode(true));
                // إعادة ربط الحدث
                var newBtn = window.parent.document.getElementById('sidebar-toggle-btn');
                if (newBtn) newBtn.onclick = function() { window.parent.toggleSidebar(); };
            }
        }
    });
})();
</script>
"""


def stat_card(icon, label, value, color="#6C63FF"):
    return f'<div class="stat-card" style="border-top:3px solid {color}"><div style="font-size:1.3rem">{icon}</div><div class="num" style="color:{color}">{value}</div><div class="lbl">{label}</div></div>'


def vs_card(our_name, our_price, comp_name, comp_price, diff, comp_source="", product_id=""):
    """بطاقة VS الأساسية — المنافس الرئيسي (الأقل سعراً)"""
    dc = "#FF1744" if diff > 0 else "#00C853" if diff < 0 else "#FFD600"
    src = f'<div style="font-size:.65rem;color:#666">{comp_source}</div>' if comp_source else ""
    pid = str(product_id) if product_id and str(product_id) not in ("", "nan", "None", "0") else ""
    pid_html = f'<div style="font-size:.65rem;color:#6C63FF99;margin-top:1px">#{pid}</div>' if pid else ""
    # السعر المقترح = أقل من أقل منافس بريال
    suggested = comp_price - 1 if comp_price > 0 else 0
    sugg_html = ""
    if suggested > 0 and diff > 10:
        sugg_html = f'<div style="font-size:.7rem;color:#4caf50;margin-top:2px">مقترح: {suggested:,.0f} ر.س</div>'
    return f'''<div class="vs-row">
<div class="our-s"><div style="font-size:.7rem;color:#8B8B8B">منتجنا</div><div style="font-weight:700;color:#B8B4FF;font-size:.9rem">{our_name}</div>{pid_html}<div style="font-size:1.1rem;font-weight:900;color:#6C63FF;margin-top:2px">{our_price:.0f} ر.س</div>{sugg_html}</div>
<div class="vs-badge">VS</div>
<div class="comp-s"><div style="font-size:.7rem;color:#8B8B8B">المنافس المتصدر</div><div style="font-weight:700;color:#FFD180;font-size:.9rem">{comp_name}</div><div style="font-size:1.1rem;font-weight:900;color:#ff9800;margin-top:2px">{comp_price:.0f} ر.س</div>{src}</div>
</div><div style="text-align:center;background:#1A1A2E;padding:4px;border-left:1px solid #333344;border-right:1px solid #333344;margin:0"><span style="color:{dc};font-weight:700;font-size:.9rem">الفرق: {diff:+.0f} ر.س</span></div>'''


def comp_strip(all_comps):
    """شريط المنافسين المصغر — يعرض كل المنافسين بأسعارهم مرتبين من الأقل"""
    if not all_comps or not isinstance(all_comps, list) or len(all_comps) == 0:
        return ""
    # ترتيب من الأقل سعراً
    sorted_comps = sorted(all_comps, key=lambda c: float(c.get("price", 0) or 0))
    chips = []
    for i, cm in enumerate(sorted_comps):
        c_name = str(cm.get("competitor", ""))[:15]
        c_price = float(cm.get("price", 0) or 0)
        c_pname = str(cm.get("name", ""))[:30]
        cls = "leader" if i == 0 else "normal"
        crown = "👑 " if i == 0 else ""
        chips.append(
            f'<span class="comp-chip {cls}" title="{c_pname}">'
            f'{crown}<span class="cp-name">{c_name}</span> '
            f'<span class="cp-price">{c_price:,.0f}</span>'
            f'</span>'
        )
    return f'<div class="comp-strip">{"".join(chips)}</div>'


def miss_card(name, price, brand, size, ptype, comp, suggested_price,
              note="", variant_html="", tester_badge="", border_color="#007bff44",
              confidence_level="green", confidence_score=0):
    """بطاقة المنتج المفقود المحسنة — أنيقة وواضحة"""
    # شارة الثقة
    trust_map = {
        "green":  ("trust-green",  "مؤكد"),
        "yellow": ("trust-yellow", "محتمل"),
        "red":    ("trust-red",    "مشكوك"),
    }
    t_cls, t_lbl = trust_map.get(confidence_level, ("trust-green", "مؤكد"))
    trust_html = f'<span class="trust-badge {t_cls}">{t_lbl}</span>' if confidence_level != "green" else ""

    note_html = f'<div style="font-size:.72rem;color:#ff9800;margin-top:4px">{note}</div>' if note and "⚠️" in note else ""

    return f"""
    <div class="miss-card" style="border:1px solid {border_color}">
      <div class="miss-header">
        <div class="miss-info">
          <div class="miss-name">
            {trust_html}{tester_badge}{name}
          </div>
          <div class="miss-meta">
            🏷️ {brand or "—"} &nbsp;|&nbsp; 📏 {size or "—"} &nbsp;|&nbsp;
            🧴 {ptype or "—"} &nbsp;|&nbsp; 🏪 {comp}
          </div>
          {variant_html}
          {note_html}
        </div>
        <div class="miss-prices">
          <div class="miss-comp-price">{price:,.0f} ر.س</div>
          <div class="miss-suggested">مقترح: {suggested_price:,.0f} ر.س</div>
        </div>
      </div>
    </div>"""
