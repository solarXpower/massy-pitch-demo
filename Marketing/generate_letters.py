from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

# ── Colour palette ──────────────────────────────────────────
NAVY  = RGBColor(0x0B, 0x1F, 0x3A)
BLUE  = RGBColor(0x1A, 0x4A, 0x8A)
GOLD  = RGBColor(0xC9, 0xA8, 0x4C)
GREY  = RGBColor(0x6B, 0x72, 0x80)
BLACK = RGBColor(0x2C, 0x3E, 0x50)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREEN = RGBColor(0x16, 0xA3, 0x4A)

# ── Helpers ─────────────────────────────────────────────────
def set_cell_bg(cell, hex_color):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement('w:shd')
    shd.set(qn('w:val'),   'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'),  hex_color)
    tcPr.append(shd)

def add_run(para, text, bold=False, italic=False,
            size=10, color=BLACK, font='Calibri'):
    run = para.add_run(text)
    run.bold   = bold
    run.italic = italic
    run.font.name  = font
    run.font.size  = Pt(size)
    run.font.color.rgb = color
    return run

def add_para(doc, text='', align=WD_ALIGN_PARAGRAPH.LEFT,
             space_before=0, space_after=6):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    if text:
        p.add_run(text)
    return p

def add_heading(doc, text, color=NAVY, size=13, space_before=14, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    # Gold bottom border
    pPr  = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bot  = OxmlElement('w:bottom')
    bot.set(qn('w:val'),   'single')
    bot.set(qn('w:sz'),    '4')
    bot.set(qn('w:space'), '1')
    bot.set(qn('w:color'), 'C9A84C')
    pBdr.append(bot)
    pPr.append(pBdr)
    run = p.add_run(text.upper())
    run.bold = True
    run.font.name  = 'Calibri'
    run.font.size  = Pt(size)
    run.font.color.rgb = color
    return p

def add_bullet(doc, text, bold_prefix=''):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after  = Pt(3)
    p.paragraph_format.space_before = Pt(0)
    if bold_prefix:
        r = p.add_run(bold_prefix)
        r.bold = True
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.font.color.rgb = BLACK
    r2 = p.add_run(text)
    r2.font.name = 'Calibri'
    r2.font.size = Pt(10)
    r2.font.color.rgb = BLACK
    return p

# ── Main letter builder ──────────────────────────────────────
def build_letter(company_name, company_address, greeting,
                 pitch_url, pitch_label, store_ref,
                 closing_sentence, output_path):

    doc = Document()

    # Page margins
    for sec in doc.sections:
        sec.top_margin    = Cm(1.8)
        sec.bottom_margin = Cm(1.8)
        sec.left_margin   = Cm(2.2)
        sec.right_margin  = Cm(2.2)

    # ── LETTERHEAD ──────────────────────────────────────────
    hdr_tbl = doc.add_table(rows=1, cols=2)
    hdr_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_tbl.style = 'Table Grid'

    # Left cell — brand
    lc = hdr_tbl.cell(0, 0)
    set_cell_bg(lc, '0B1F3A')
    lc.width = Inches(4)
    lc_p = lc.paragraphs[0]
    lc_p.paragraph_format.space_before = Pt(8)
    lc_p.paragraph_format.space_after  = Pt(2)
    r1 = lc_p.add_run('INTER')
    r1.bold = True; r1.font.name = 'Calibri'; r1.font.size = Pt(22)
    r1.font.color.rgb = WHITE
    r2 = lc_p.add_run('XDB')
    r2.bold = True; r2.font.name = 'Calibri'; r2.font.size = Pt(22)
    r2.font.color.rgb = GOLD
    tag_p = lc.add_paragraph()
    tag_p.paragraph_format.space_before = Pt(0)
    tag_p.paragraph_format.space_after  = Pt(8)
    rt = tag_p.add_run('Digital Retail & Auction Platform — Barbados')
    rt.font.name = 'Calibri'; rt.font.size = Pt(8)
    rt.font.color.rgb = RGBColor(0xAA, 0xBB, 0xCC)

    # Right cell — contact
    rc = hdr_tbl.cell(0, 1)
    set_cell_bg(rc, '0B1F3A')
    rc.width = Inches(2.8)
    rc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    for line in ['contact@INTERXDB.com', 'Tel: 1(246) 241-3771', 'www.interxdb.com']:
        rp = rc.add_paragraph(line)
        rp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rp.paragraph_format.space_before = Pt(2)
        rp.paragraph_format.space_after  = Pt(2)
        rn = rp.runs[0]
        rn.font.name = 'Calibri'; rn.font.size = Pt(8.5)
        rn.font.color.rgb = RGBColor(0xAA, 0xBB, 0xCC)

    # Remove table borders
    for row in hdr_tbl.rows:
        for cell in row.cells:
            tc   = cell._tc
            tcPr = tc.get_or_add_tcPr()
            tcBdr = OxmlElement('w:tcBdr')
            for side in ('top','left','bottom','right','insideH','insideV'):
                el = OxmlElement(f'w:{side}')
                el.set(qn('w:val'),   'none')
                el.set(qn('w:sz'),    '0')
                el.set(qn('w:space'), '0')
                el.set(qn('w:color'), 'auto')
                tcBdr.append(el)
            tcPr.append(tcBdr)

    # Gold rule
    rule_p = doc.add_paragraph()
    rule_p.paragraph_format.space_before = Pt(0)
    rule_p.paragraph_format.space_after  = Pt(0)
    pPr  = rule_p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bot  = OxmlElement('w:bottom')
    bot.set(qn('w:val'),   'single')
    bot.set(qn('w:sz'),    '12')
    bot.set(qn('w:space'), '0')
    bot.set(qn('w:color'), 'C9A84C')
    pBdr.append(bot)
    pPr.append(pBdr)

    # ── DATE ────────────────────────────────────────────────
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after  = Pt(8)
    add_run(p, 'May 2026', color=GREY, size=10)

    # ── RECIPIENT ───────────────────────────────────────────
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(3)
    add_run(p, 'The Management Team', bold=True, color=NAVY)
    doc.add_paragraph(company_name).paragraph_format.space_after = Pt(2)
    doc.add_paragraph('Barbados').paragraph_format.space_after = Pt(14)

    # ── SUBJECT BOX ────────────────────────────────────────
    sub_tbl = doc.add_table(rows=1, cols=1)
    sub_tbl.style = 'Table Grid'
    sc = sub_tbl.cell(0, 0)
    set_cell_bg(sc, 'F7F9FC')
    sp1 = sc.paragraphs[0]
    sp1.paragraph_format.space_before = Pt(4)
    sp1.paragraph_format.space_after  = Pt(2)
    add_run(sp1, 'PARTNERSHIP INVITATION', color=GREY, size=8.5, bold=True)
    sp2 = sc.add_paragraph()
    sp2.paragraph_format.space_before = Pt(0)
    sp2.paragraph_format.space_after  = Pt(6)
    add_run(sp2, "Introducing INTERXDB — Barbados' First Exclusive Retail Auction & Deals App",
            bold=True, color=NAVY, size=13, font='Calibri')

    # Gold left border on subject table
    tc   = sc._tc
    tcPr = tc.get_or_add_tcPr()
    tcBdr = OxmlElement('w:tcBdr')
    left  = OxmlElement('w:left')
    left.set(qn('w:val'),   'single')
    left.set(qn('w:sz'),    '18')
    left.set(qn('w:space'), '4')
    left.set(qn('w:color'), 'C9A84C')
    tcBdr.append(left)
    for side in ('top','right','bottom'):
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'),   'none')
        el.set(qn('w:sz'),    '0')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), 'auto')
        tcBdr.append(el)
    tcPr.append(tcBdr)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ── BODY ────────────────────────────────────────────────
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    add_run(p, f'Dear {greeting},', bold=True, size=11, color=NAVY)

    def body_para(text, bold_parts=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_run(p, text, size=10.5, color=BLACK)

    body_para(
        f"On behalf of INTERXDB, we are pleased to extend this exclusive invitation to {company_name} "
        "to become one of the founding retail partners on the island's first dedicated "
        "business-to-consumer auction and deals platform."
    )

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_run(p, "INTERXDB owns and operates the complete digital infrastructure — the platform, "
               "the mobile application, all hosting, and all technical services. "
               "You simply list products — we handle the rest.", size=10.5, color=BLACK)

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_run(p, "The platform is designed with one purpose: ", size=10.5, color=BLACK)
    add_run(p, f"to keep {store_ref} as the buzz word in every Barbadian household, "
               "24 hours a day, 7 days a week", bold=True, size=10.5, color=NAVY)
    add_run(p, " — whether your doors are open or not. Customers compete for your products "
               "through live auctions, driving excitement, urgency, and loyalty to your brand.",
               size=10.5, color=BLACK)

    # ── HOW IT WORKS ────────────────────────────────────────
    add_heading(doc, 'How the Platform Works')

    how_items = [
        ('01  App-Only Marketplace',
         'All auctions, Deals of the Week, and Deals of the Month are conducted exclusively '
         'through the INTERXDB mobile app. No auctions appear on the public website.'),
        ('02  Registered Businesses Only',
         'Only verified, registered retail businesses may list products. No individual or '
         'private sellers are permitted — ensuring a professional marketplace.'),
        ('03  25-Item Weekly Limit',
         'Each store is allocated up to 25 items per week. This controlled supply creates '
         'scarcity, drives urgency, and maximises competitive bidding among your customers.'),
        ('04  Free Customer Registration',
         'End-users register on the app at no cost. Stores promote the app in-store and '
         'across their social media and marketing channels to drive downloads.'),
    ]

    how_tbl = doc.add_table(rows=2, cols=2)
    how_tbl.style = 'Table Grid'
    how_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    idx = 0
    for row in how_tbl.rows:
        for cell in row.cells:
            if idx >= len(how_items): break
            set_cell_bg(cell, 'F7F9FC')
            title, body = how_items[idx]
            tp = cell.paragraphs[0]
            tp.paragraph_format.space_before = Pt(6)
            tp.paragraph_format.space_after  = Pt(4)
            add_run(tp, title, bold=True, color=NAVY, size=10)
            bp = cell.add_paragraph(body)
            bp.paragraph_format.space_before = Pt(0)
            bp.paragraph_format.space_after  = Pt(6)
            for r in bp.runs:
                r.font.name = 'Calibri'; r.font.size = Pt(9.5)
                r.font.color.rgb = GREY
            idx += 1

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ── FREE OFFER ───────────────────────────────────────────
    add_heading(doc, 'Introductory Offer — No Monthly Cost for 60 Days')

    fo_tbl = doc.add_table(rows=1, cols=2)
    fo_tbl.style = 'Table Grid'
    fo_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Badge cell
    bc = fo_tbl.cell(0, 0)
    set_cell_bg(bc, 'C9A84C')
    bc.width = Inches(1.2)
    bc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    bp1 = bc.paragraphs[0]
    bp1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    bp1.paragraph_format.space_before = Pt(8)
    bp1.paragraph_format.space_after  = Pt(2)
    add_run(bp1, '60', bold=True, color=NAVY, size=28)
    bp2 = bc.add_paragraph('DAYS FREE')
    bp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    bp2.paragraph_format.space_before = Pt(0)
    bp2.paragraph_format.space_after  = Pt(8)
    add_run(bp2, '', bold=True, color=NAVY, size=10)
    for r in bp2.runs:
        r.font.name = 'Calibri'; r.font.size = Pt(10)
        r.bold = True; r.font.color.rgb = NAVY
    # fix text
    bc.paragraphs[1].runs[0].text = 'DAYS FREE'

    # Text cell
    tc2 = fo_tbl.cell(0, 1)
    set_cell_bg(tc2, '0B1F3A')
    tp1 = tc2.paragraphs[0]
    tp1.paragraph_format.space_before = Pt(8)
    tp1.paragraph_format.space_after  = Pt(4)
    add_run(tp1, 'Zero Cost for Your First 60 Days', bold=True, color=WHITE, size=12)
    tp2 = tc2.add_paragraph()
    tp2.paragraph_format.space_before = Pt(0)
    tp2.paragraph_format.space_after  = Pt(8)
    add_run(tp2, 'Full use of the platform at zero monthly cost for the first 60 days. A ',
            color=RGBColor(0xCC, 0xCC, 0xCC), size=10)
    add_run(tp2, '$500.00 deposit', bold=True, color=GOLD, size=10)
    add_run(tp2, f' is required to secure primary advertisement placement within the app. '
                 f'This guarantees {store_ref} is featured prominently to all registered users from day one.',
            color=RGBColor(0xCC, 0xCC, 0xCC), size=10)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ── PRICING TABLE ────────────────────────────────────────
    add_heading(doc, 'Platform Pricing — After 60-Day Introductory Period (BBD)')

    pt = doc.add_table(rows=5, cols=3)
    pt.style = 'Table Grid'
    pt.alignment = WD_TABLE_ALIGNMENT.CENTER

    headers = ['Service', 'Description', 'Rate']
    for i, h in enumerate(headers):
        cell = pt.cell(0, i)
        set_cell_bg(cell, '0B1F3A')
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(5)
        p.paragraph_format.space_after  = Pt(5)
        add_run(p, h, bold=True, color=WHITE, size=10)

    rows_data = [
        ('Base Listing Package',   'Up to 25 items listed per week on the app',                      '$450.00 / month'),
        ('Additional Items',       'Per additional 10 items above the 25-item base',                  '$150.00 / month'),
        ('Deal of the Week',       'Featured deal highlighted to all app users for 7 days',            '$150.00 / week'),
        ('Deal of the Month',      'Premium featured deal — top placement for the full month',         '$200.00 / month'),
    ]
    for ri, (s, d, r) in enumerate(rows_data):
        bg = 'F7F9FC' if ri % 2 == 0 else 'FFFFFF'
        for ci, txt in enumerate([s, d, r]):
            cell = pt.cell(ri + 1, ci)
            set_cell_bg(cell, bg)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after  = Pt(4)
            bold = (ci == 0 or ci == 2)
            col  = NAVY if (ci == 0 or ci == 2) else BLACK
            add_run(p, txt, bold=bold, color=col, size=10)

    note = doc.add_paragraph('All pricing in Barbados Dollars (BBD). Rates are fixed for the first 12 months for founding partners.')
    note.paragraph_format.space_before = Pt(4)
    note.paragraph_format.space_after  = Pt(10)
    for r in note.runs:
        r.italic = True; r.font.size = Pt(9); r.font.color.rgb = GREY

    # ── PITCH DEMO LINK ──────────────────────────────────────
    add_heading(doc, 'See the Vision — Your Interactive Demo')

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_run(p, f"We have prepared a personalised before-and-after demonstration of the INTERXDB platform "
               f"experience for {company_name}. Click the link below to view your interactive pitch:",
               size=10.5, color=BLACK)

    demo_tbl = doc.add_table(rows=1, cols=1)
    demo_tbl.style = 'Table Grid'
    dc = demo_tbl.cell(0, 0)
    set_cell_bg(dc, 'F7F9FC')
    dp = dc.paragraphs[0]
    dp.paragraph_format.space_before = Pt(8)
    dp.paragraph_format.space_after  = Pt(8)
    add_run(dp, f'{pitch_label}  →  ', bold=True, color=NAVY, size=11)
    add_run(dp, pitch_url, bold=False, color=BLUE, size=11)

    # left gold border
    tc3  = dc._tc
    tcPr = tc3.get_or_add_tcPr()
    tcBdr2 = OxmlElement('w:tcBdr')
    left2  = OxmlElement('w:left')
    left2.set(qn('w:val'),   'single')
    left2.set(qn('w:sz'),    '18')
    left2.set(qn('w:space'), '4')
    left2.set(qn('w:color'), 'C9A84C')
    tcBdr2.append(left2)
    for side in ('top','right','bottom'):
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'),   'none')
        el.set(qn('w:sz'),    '0')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), 'auto')
        tcBdr2.append(el)
    tcPr.append(tcBdr2)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ── OBLIGATIONS ──────────────────────────────────────────
    add_heading(doc, 'Partner Obligations & Platform Conduct')

    ob_tbl = doc.add_table(rows=1, cols=1)
    ob_tbl.style = 'Table Grid'
    oc = ob_tbl.cell(0, 0)
    set_cell_bg(oc, 'FFF8F8')
    oh = oc.paragraphs[0]
    oh.paragraph_format.space_before = Pt(6)
    oh.paragraph_format.space_after  = Pt(4)
    add_run(oh, 'Store Partner Responsibilities', bold=True,
            color=RGBColor(0x8B, 0x1A, 0x1A), size=10.5)

    obligations = [
        "Actively promote the INTERXDB app in-store and across all social media and marketing channels.",
        "Ensure all listed products are accurately described, available, and fulfilled upon auction completion.",
        "Honour all winning auction bids — failure to fulfil confirmed orders may result in suspension from the platform.",
        "Maintain professional standards of communication with winning customers via the platform.",
    ]
    for ob in obligations:
        op = oc.add_paragraph(ob, style='List Bullet')
        op.paragraph_format.space_before = Pt(2)
        op.paragraph_format.space_after  = Pt(2)
        for r in op.runs:
            r.font.name = 'Calibri'; r.font.size = Pt(10)
            r.font.color.rgb = BLACK

    pb = oc.add_paragraph()
    pb.paragraph_format.space_before = Pt(6)
    pb.paragraph_format.space_after  = Pt(6)
    add_run(pb, 'User Conduct: ', bold=True, color=RGBColor(0x8B, 0x1A, 0x1A), size=10)
    add_run(pb, 'Registered customers who fail to honour confirmed auction wins will be banned from the platform. '
                'Disputes are subject to review, with reasonable evidence from both parties considered before any action is taken.',
                size=10, color=BLACK)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ── CLOSING PARAGRAPHS ───────────────────────────────────
    cp = doc.add_paragraph()
    cp.paragraph_format.space_after = Pt(8)
    cp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_run(cp, closing_sentence, size=10.5, color=BLACK)

    cp2 = doc.add_paragraph()
    cp2.paragraph_format.space_after = Pt(16)
    add_run(cp2, 'We welcome the opportunity to schedule a presentation at your convenience.',
            size=10.5, color=BLACK)

    # ── SIGNATURE ────────────────────────────────────────────
    sp0 = doc.add_paragraph()
    sp0.paragraph_format.space_before = Pt(4)
    sp0.paragraph_format.space_after  = Pt(6)
    # Top border
    pPr2  = sp0._p.get_or_add_pPr()
    pBdr2 = OxmlElement('w:pBdr')
    top2  = OxmlElement('w:top')
    top2.set(qn('w:val'),   'single')
    top2.set(qn('w:sz'),    '4')
    top2.set(qn('w:space'), '1')
    top2.set(qn('w:color'), 'D8E2EF')
    pBdr2.append(top2)
    pPr2.append(pBdr2)
    add_run(sp0, 'Yours sincerely,', size=10.5, color=BLACK)

    sn = doc.add_paragraph()
    sn.paragraph_format.space_before = Pt(12)
    sn.paragraph_format.space_after  = Pt(2)
    add_run(sn, 'INTER', bold=True, color=NAVY, size=16)
    add_run(sn, 'XDB',   bold=True, color=GOLD, size=16)

    st = doc.add_paragraph()
    st.paragraph_format.space_after = Pt(10)
    add_run(st, 'DIGITAL RETAIL & AUCTION PLATFORM', color=GREY, size=9)

    sc_p = doc.add_paragraph()
    sc_p.paragraph_format.space_after = Pt(4)
    add_run(sc_p, 'contact@INTERXDB.com', color=BLUE, size=10)
    add_run(sc_p, '   |   Tel 1(246) 241-3771   |   www.interxdb.com', color=GREY, size=10)

    # ── FOOTER ──────────────────────────────────────────────
    ft_p = doc.add_paragraph()
    ft_p.paragraph_format.space_before = Pt(16)
    ft_p.paragraph_format.space_after  = Pt(4)
    ft_pPr  = ft_p._p.get_or_add_pPr()
    ft_pBdr = OxmlElement('w:pBdr')
    ft_top  = OxmlElement('w:top')
    ft_top.set(qn('w:val'),   'single')
    ft_top.set(qn('w:sz'),    '6')
    ft_top.set(qn('w:space'), '1')
    ft_top.set(qn('w:color'), 'C9A84C')
    ft_pBdr.append(ft_top)
    ft_pPr.append(ft_pBdr)
    ft_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(ft_p, 'INTER', bold=True, color=NAVY, size=10)
    add_run(ft_p, 'XDB',   bold=True, color=GOLD, size=10)
    add_run(ft_p, '  —  Auction & Get Buzz                    Confidential — For Addressee Only',
            color=GREY, size=9)

    doc.save(output_path)
    print(f'Saved: {output_path}')


# ── Generate all three letters ───────────────────────────────
BASE = r'C:\AI Software\websites'

build_letter(
    company_name    = 'Massy Stores Barbados',
    company_address = 'Barbados',
    greeting        = 'Massy Stores Management Team',
    pitch_url       = 'https://interxdb.com/WebSites/massy-pitch/',
    pitch_label     = 'Massy Stores Barbados — Live Demo',
    store_ref       = 'Massy Stores',
    closing_sentence= ("We believe this partnership represents a significant and low-risk opportunity to extend "
                       "Massy Stores' digital reach, engage a new generation of digital-first customers, and "
                       "strengthen your position as Barbados' leading retail brand."),
    output_path     = fr'{BASE}\Massy\marketing-letter.docx',
)

build_letter(
    company_name    = "Carter & Co Ltd",
    company_address = 'Barbados',
    greeting        = "Carter & Co Management Team",
    pitch_url       = 'https://interxdb.com/WebSites/carters-pitch/',
    pitch_label     = "Carter & Co Ltd — Live Demo",
    store_ref       = "Carter's",
    closing_sentence= ("We believe this partnership represents a significant and low-risk opportunity for "
                       "Carter & Co to extend its digital reach, engage a new generation of customers, and "
                       "build on its strong reputation as a trusted Barbados hardware institution."),
    output_path     = fr'{BASE}\Carters\marketing-letter.docx',
)

build_letter(
    company_name    = 'ACE H&B Hardware & Lumber Inc.',
    company_address = 'Barbados',
    greeting        = 'H&B Hardware Management Team',
    pitch_url       = 'https://interxdb.com/WebSites/hbhardware-pitch/',
    pitch_label     = 'ACE H&B Hardware & Lumber Inc. — Live Demo',
    store_ref       = 'H&B Hardware',
    closing_sentence= ("We believe this partnership represents a significant and low-risk opportunity for "
                       "H&B Hardware to extend its digital reach, engage a new generation of customers, and "
                       'reinforce its well-earned reputation as "the helpful place" across Barbados.'),
    output_path     = fr'{BASE}\HBHARDWARE\marketing-letter.docx',
)

print('All 3 Word documents generated successfully.')
