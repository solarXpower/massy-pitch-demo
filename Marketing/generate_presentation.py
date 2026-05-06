"""
BiziBid — Retail Partner Presentation Generator
Generates: marketing-presentation.pptx + marketing-presentation-print.html (for PDF)
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy, os

# ── Colours ──────────────────────────────────────────────────────────────────
GOLD   = RGBColor(0xC9, 0xA8, 0x4C)
BLACK  = RGBColor(0x0A, 0x0A, 0x0A)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT  = RGBColor(0xF8, 0xF8, 0xF8)
MGREY  = RGBColor(0x4B, 0x55, 0x63)
LGREY  = RGBColor(0x9C, 0xA3, 0xAF)
RED    = RGBColor(0xDC, 0x26, 0x26)
NAVY   = RGBColor(0x0B, 0x1F, 0x3A)
DKGOLD = RGBColor(0x92, 0x70, 0x20)

SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H

blank_layout = prs.slide_layouts[6]  # completely blank

# ── Helpers ──────────────────────────────────────────────────────────────────

def add_rect(slide, l, t, w, h, fill=None, line=None, line_w=None):
    shape = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    shape.line.fill.background()
    if fill:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill
    else:
        shape.fill.background()
    if line:
        shape.line.color.rgb = line
        if line_w:
            shape.line.width = line_w
    else:
        shape.line.fill.background()
    return shape

def add_text(slide, text, l, t, w, h,
             size=18, bold=False, color=BLACK, align=PP_ALIGN.LEFT,
             italic=False, wrap=True):
    txBox = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txBox

def add_para(tf, text, size=14, bold=False, color=BLACK,
             align=PP_ALIGN.LEFT, italic=False, space_before=6):
    p = tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(space_before)
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return p

def slide_bg(slide, color=WHITE):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def gold_bar(slide, t=0.92, h=0.07):
    """Horizontal gold accent bar."""
    add_rect(slide, 0, t, 13.33, h, fill=GOLD)

def page_num(slide, n, total):
    add_text(slide, f"{n} / {total}", 12.3, 7.1, 1.0, 0.35,
             size=9, color=LGREY, align=PP_ALIGN.RIGHT)

def logo_text(slide, l=0.4, t=0.18):
    txBox = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(2.5), Inches(0.55))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    r1 = p.add_run(); r1.text = "Bizi"; r1.font.size = Pt(22); r1.font.bold = True; r1.font.color.rgb = BLACK
    r2 = p.add_run(); r2.text = "Bid"; r2.font.size = Pt(22); r2.font.bold = True; r2.font.color.rgb = GOLD

def section_label(slide, text, l=0.5, t=1.05, color=GOLD):
    add_text(slide, text.upper(), l, t, 8, 0.32,
             size=9, bold=True, color=color)

def heading(slide, text, l=0.5, t=1.45, w=12.3, size=30, color=BLACK):
    add_text(slide, text, l, t, w, 0.85, size=size, bold=True, color=color)

def sub(slide, text, l=0.5, t=2.1, w=12.3, size=15, color=MGREY):
    add_text(slide, text, l, t, w, 0.45, size=size, color=color)

def bullet_box(slide, items, l, t, w, h,
               icon_color=GOLD, text_color=BLACK,
               text_size=13, header=None, header_color=BLACK):
    box = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    first = True
    if header:
        p = tf.paragraphs[0]
        r = p.add_run(); r.text = header
        r.font.size = Pt(13); r.font.bold = True; r.font.color.rgb = header_color
        first = False
    for item in items:
        if first:
            p = tf.paragraphs[0]; first = False
        else:
            p = tf.add_paragraph()
            p.space_before = Pt(5)
        r = p.add_run()
        r.text = item
        r.font.size = Pt(text_size)
        r.font.color.rgb = text_color
    return box

def feature_card(slide, icon, title, body, l, t, w=3.9, h=1.7,
                 bg=LIGHT, icon_color=GOLD, title_color=BLACK, body_color=MGREY):
    """A small card with icon + title + body text."""
    add_rect(slide, l, t, w, h, fill=bg)
    # gold left accent strip
    add_rect(slide, l, t, 0.05, h, fill=icon_color)
    # icon
    add_text(slide, icon, l+0.12, t+0.12, 0.5, 0.45, size=20, color=icon_color)
    # title
    add_text(slide, title, l+0.65, t+0.12, w-0.8, 0.38,
             size=12, bold=True, color=title_color)
    # body
    add_text(slide, body, l+0.12, t+0.58, w-0.25, h-0.7,
             size=10, color=body_color)

def stat_card(slide, number, label, l, t, w=2.2, h=1.1):
    add_rect(slide, l, t, w, h, fill=LIGHT)
    add_rect(slide, l, t, w, 0.04, fill=GOLD)
    add_text(slide, number, l, t+0.1, w, 0.5,
             size=26, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    add_text(slide, label, l, t+0.6, w, 0.45,
             size=10, color=MGREY, align=PP_ALIGN.CENTER)

# ── TOTAL SLIDES ─────────────────────────────────────────────────────────────
TOTAL = 14

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 1 — COVER
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)

# Full-width navy top band
add_rect(s, 0, 0, 13.33, 5.2, fill=NAVY)

# Gold bottom bar
add_rect(s, 0, 5.2, 13.33, 0.08, fill=GOLD)

# BiziBid large wordmark
txBox = s.shapes.add_textbox(Inches(1.0), Inches(1.1), Inches(11), Inches(1.8))
tf = txBox.text_frame
p = tf.paragraphs[0]
p.alignment = PP_ALIGN.CENTER
r1 = p.add_run(); r1.text = "Bizi"; r1.font.size = Pt(80); r1.font.bold = True; r1.font.color.rgb = WHITE
r2 = p.add_run(); r2.text = "Bid";  r2.font.size = Pt(80); r2.font.bold = True; r2.font.color.rgb = GOLD

add_text(s, "Barbados' First Retail Auction & Deals Platform",
         1.0, 3.05, 11.3, 0.6, size=20, color=RGBColor(0xC0,0xC8,0xD8),
         align=PP_ALIGN.CENTER)

add_text(s, "Partnership Opportunity  ·  Confidential",
         1.0, 3.75, 11.3, 0.5, size=13, color=RGBColor(0x5A,0x66,0x78),
         align=PP_ALIGN.CENTER, italic=True)

add_text(s, "Presented by INTERXDB  ·  Digital Retail & Auction Platform  ·  Barbados",
         1.0, 5.5, 11.3, 0.45, size=11, color=MGREY, align=PP_ALIGN.CENTER)

add_text(s, "bizibid.com  ·  contact@interxdb.com  ·  Tel 1(246) 241-3771",
         1.0, 6.0, 11.3, 0.4, size=11, color=LGREY, align=PP_ALIGN.CENTER)

page_num(s, 1, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 2 — WHAT IS BIZIBID?
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Platform Overview")
heading(s, "What is BiziBid?")
sub(s, "A mobile-first auction and deals platform built exclusively for Barbados' retail market.")

# Three pillars
pillars = [
    ("📱", "The BiziBid App",
     "A free mobile app (iOS & Android) where registered customers browse live auctions and exclusive deals — 24 hours a day, 7 days a week."),
    ("🏪", "Your Back-Office Portal",
     "A private web portal at BiziBid.com where your team uploads products, manages deals, reviews auction results, and tracks performance."),
    ("🏆", "Operated by INTERXDB",
     "INTERXDB owns and operates the entire platform — the app, the hosting, the technology. You simply list products. We handle everything else."),
]
for i, (icon, title, body) in enumerate(pillars):
    feature_card(s, icon, title, body, l=0.5 + i*4.3, t=2.7, w=4.1, h=2.6)

page_num(s, 2, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 3 — THE OPPORTUNITY
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "The Opportunity")
heading(s, "Your Store — 24/7 in Every Customer's Pocket")
sub(s, "BiziBid keeps your brand top-of-mind every single day — whether your doors are open or not.")

points = [
    "★  Customers open the app daily to check new auctions and deals from your store",
    "★  Your store logo is displayed prominently on the app's home screen",
    "★  Exclusive auction prices (below shelf) create urgency and loyal repeat engagement",
    "★  Deals of the Week and Month drive customers physically through your doors",
    "★  Every deal or auction item shared on WhatsApp or Instagram puts your brand in front of new potential customers — at no cost to you",
    "★  Founding retail partners secure premium placement before competitors",
]
box = s.shapes.add_textbox(Inches(0.8), Inches(2.6), Inches(11.7), Inches(4.2))
tf = box.text_frame
tf.word_wrap = True
for i, pt in enumerate(points):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.space_before = Pt(8)
    r = p.add_run()
    r.text = pt
    r.font.size = Pt(14)
    r.font.color.rgb = BLACK

page_num(s, 3, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 4 — THE APP EXPERIENCE (Customer View)
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Customer Experience")
heading(s, "How Customers Experience BiziBid")
sub(s, "A beautifully simple home screen keeps customers focused on your store — and coming back every day.")

cards = [
    ("⌨️", "The Store Keypad",
     "Your store logo appears on the app's home screen — just like a speed-dial button. Customers tap it to see your live auctions and deals instantly."),
    ("🔔", "Live Notifications",
     "Colour-coded badge alerts on your store logo tell customers how many bids are active, who is watching, and when they have been outbid. They respond immediately."),
    ("📌", "Pin Your Store",
     "Customers can pin your store as their favourite, giving your logo a prominent permanent position on their personal home screen."),
    ("⚡", "One-Tap Bidding",
     "Customers bid with a single tap without ever leaving the home screen. A sliding panel shows all their active bids across all stores simultaneously."),
]
for i, (icon, title, body) in enumerate(cards):
    c, r = i % 2, i // 2
    feature_card(s, icon, title, body, l=0.5 + c*6.5, t=2.7 + r*2.0, w=6.1, h=1.8)

page_num(s, 4, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 5 — LIVE AUCTIONS
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Feature — Auctions")
heading(s, "Live Auctions — Excitement That Sells")
sub(s, "Customers compete in real-time for your products. The excitement keeps them engaged and coming back.")

# Left column
bullet_box(s, [
    "▶  You upload products with a starting bid price (set below shelf price)",
    "▶  Up to 25 items per week rotate through the platform automatically",
    "▶  5 new items are released each day at varied morning hours — keeping customers checking in daily",
    "▶  Auctions run for 3, 7, or 14 days depending on the item",
    "▶  Real-time bidding — customers see bids update live on their screen",
    "▶  Unsold items re-enter the rotation for the following week automatically",
], l=0.5, t=2.55, w=6.0, h=4.2, text_color=BLACK, text_size=13)

# Right — how winning works
add_rect(s, 7.0, 2.55, 5.8, 4.2, fill=NAVY)
add_rect(s, 7.0, 2.55, 5.8, 0.06, fill=GOLD)
add_text(s, "When a Customer Wins", 7.2, 2.65, 5.4, 0.45,
         size=13, bold=True, color=GOLD)
win_steps = [
    "1  Auction closes — winner is confirmed",
    "2  A unique collection code is generated",
    "3  Winner receives code on their phone",
    "4  Winner visits your store and shows code to cashier",
    "5  Cashier confirms the code — item is collected",
    "6  Record of the sale is stored in your portal",
]
box = s.shapes.add_textbox(Inches(7.2), Inches(3.2), Inches(5.3), Inches(3.3))
tf = box.text_frame; tf.word_wrap = True
for i, step in enumerate(win_steps):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.space_before = Pt(7)
    r = p.add_run(); r.text = step
    r.font.size = Pt(12); r.font.color.rgb = WHITE

add_text(s, "No online payment needed — all purchases are cash in-store.",
         7.2, 6.35, 5.3, 0.38, size=10, italic=True,
         color=RGBColor(0x9C,0xA3,0xAF))

page_num(s, 5, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 6 — DEALS OF THE WEEK / MONTH
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Feature — Deals")
heading(s, "Deals of the Week & Month — Drive Foot Traffic")
sub(s, "Fixed-price deals showcase your best offers and bring customers through your doors.")

left_items = [
    "▶  You set a fixed price — no bidding, no auction pressure",
    "▶  Customers see your deal prominently in the app all week or all month",
    "▶  Customers can Like the deal — like count is visible to all users (social proof)",
    "▶  Customers share deals directly to WhatsApp, Instagram, and other platforms",
    "▶  Shared links show the deal to people who do not yet have the app — driving new downloads",
    "▶  Walk-in customers ask for the deal by name — increased foot traffic guaranteed",
    "▶  Deals of the Month offer extended 30-day visibility at premium placement",
]
bullet_box(s, left_items, l=0.5, t=2.55, w=7.5, h=4.2, text_color=BLACK, text_size=13)

# Right info box
add_rect(s, 8.3, 2.55, 4.5, 1.9, fill=LIGHT)
add_rect(s, 8.3, 2.55, 0.06, 1.9, fill=GOLD)
add_text(s, "Deal of the Week", 8.5, 2.65, 4.1, 0.38, size=12, bold=True, color=BLACK)
add_text(s, "7-day fixed-price feature\nPremium placement in app\nLike + Share enabled\nDrives walk-in purchase",
         8.5, 3.1, 4.0, 1.2, size=11, color=MGREY)

add_rect(s, 8.3, 4.6, 4.5, 1.9, fill=NAVY)
add_rect(s, 8.3, 4.6, 0.06, 1.9, fill=GOLD)
add_text(s, "Deal of the Month", 8.5, 4.7, 4.1, 0.38, size=12, bold=True, color=GOLD)
add_text(s, "Full 30-day visibility\nTop placement position\nMaximum brand exposure\nIdeal for key product lines",
         8.5, 5.15, 4.0, 1.2, size=11, color=RGBColor(0xC0,0xC8,0xD8))

page_num(s, 6, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 7 — BACK-OFFICE PORTAL
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Your Back-Office — BiziBid.com")
heading(s, "Your Private Management Portal")
sub(s, "Log in at BiziBid.com to manage your entire BiziBid presence — available 24/7 from any browser.")

portal_features = [
    ("📦", "Bulk Product Upload",
     "Upload multiple products at once with images, descriptions, and your chosen starting bid price. No technical knowledge required."),
    ("🏷️", "Deals Management",
     "Create and schedule Deals of the Week and Deals of the Month. Set your own price and valid dates. Activate with one click."),
    ("🏆", "Auction Results",
     "View all completed auctions — winning bid amount, customer name, collection code. Full record of every sale."),
    ("🔑", "Collection Codes",
     "See the unique code for each auction winner so your cashier can verify the customer quickly and confidently."),
    ("📄", "Invoice Download",
     "View and download your monthly platform invoices as PDF. Full record of your subscription and activity charges."),
    ("📊", "Store Statistics",
     "Live dashboard showing user engagement, bid activity, deal shares, and more. Know exactly how customers interact with your store."),
]
for i, (icon, title, body) in enumerate(portal_features):
    c, r = i % 3, i // 3
    feature_card(s, icon, title, body, l=0.4 + c*4.3, t=2.6 + r*1.9, w=4.0, h=1.75)

page_num(s, 7, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 8 — STORE STATISTICS
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Back-Office — Statistics Dashboard")
heading(s, "Know Your Customers — Live Store Statistics")
sub(s, "Your back-office portal shows you exactly how registered BiziBid users interact with your store in real time.")

# Stat cards row 1
stats1 = [
    ("1,240", "Registered users\nfollowing your store"),
    ("86", "Active bids on\nyour items today"),
    ("312", "Users watching\nyour products"),
    ("94%", "Auction completion\nrate this month"),
]
for i, (num, lbl) in enumerate(stats1):
    stat_card(s, num, lbl, l=0.5 + i*3.1, t=2.55, w=2.9, h=1.2)

# Stat cards row 2
stats2 = [
    ("48", "Deals shared on\nWhatsApp & Instagram"),
    ("$8,400", "Total auction value\ngenerated this month"),
    ("22", "New app users from\nyour shared links"),
    ("4.8★", "Average customer\nengagement score"),
]
for i, (num, lbl) in enumerate(stats2):
    stat_card(s, num, lbl, l=0.5 + i*3.1, t=3.9, w=2.9, h=1.2)

# Bottom text
add_rect(s, 0.5, 5.25, 12.3, 1.4, fill=LIGHT)
add_rect(s, 0.5, 5.25, 0.06, 1.4, fill=GOLD)
add_text(s,
    "All statistics are updated in real time and available directly in your back-office portal at BiziBid.com. "
    "Track which products generate the most interest, which deals are most shared, and how your store's following "
    "grows week over week. No data is shared with other retail partners.",
    0.65, 5.32, 12.0, 1.25, size=12, color=MGREY)

page_num(s, 8, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 9 — VIRAL SHARE & FREE MARKETING
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Feature — Viral Growth")
heading(s, "Every Share is Free Marketing for Your Store")
sub(s, "When customers share your auctions and deals, your store name reaches people who have never heard of BiziBid.")

# Flow boxes
flow = [
    ("Your customer\nsees a great deal\nor live auction", "01"),
    ("They share it\nto WhatsApp or\nInstagram", "02"),
    ("Their contact sees\nyour store name,\nprice & product", "03"),
    ("They visit\nBiziBid.com and\ndownload the app", "04"),
    ("New registered\nbidder — on your\nauctions", "05"),
]
for i, (text, num) in enumerate(flow):
    x = 0.35 + i * 2.56
    add_rect(s, x, 2.5, 2.3, 2.3, fill=NAVY if i % 2 == 0 else LIGHT)
    add_text(s, num, x+0.1, 2.58, 0.5, 0.45,
             size=11, bold=True, color=GOLD)
    add_text(s, text, x+0.1, 2.95, 2.1, 1.7,
             size=12, color=WHITE if i % 2 == 0 else BLACK)
    if i < 4:
        add_text(s, "→", x+2.32, 3.35, 0.22, 0.5, size=18, color=GOLD)

add_rect(s, 0.5, 5.05, 12.3, 1.65, fill=LIGHT)
add_rect(s, 0.5, 5.05, 0.06, 1.65, fill=GOLD)

share_points = [
    "When a customer shares a live auction, the shared link shows the current bid price and countdown timer — creating instant FOMO for their contacts.",
    "When a customer shares a Deal of the Week, the link shows your store name, product image, and fixed price — driving walk-in intent.",
    "All shared links direct visitors to BiziBid.com where they can download the app. New downloads = new bidders on your products.",
]
box = s.shapes.add_textbox(Inches(0.7), Inches(5.12), Inches(12.0), Inches(1.5))
tf = box.text_frame; tf.word_wrap = True
for i, pt in enumerate(share_points):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.space_before = Pt(4)
    r = p.add_run(); r.text = "▸  " + pt
    r.font.size = Pt(11); r.font.color.rgb = MGREY

page_num(s, 9, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 10 — KEYPAD PLACEMENT & ADS
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Placement & Visibility")
heading(s, "Secure Your Position on the BiziBid Keypad")
sub(s, "Your store logo placement on the app home screen is a paid position. First come, first placed.")

tiers = [
    (GOLD, "Tier 1 — Pinned Position",
     "Top of every user's home screen. Your logo is displayed largest, with full notification badge visibility. One store only — the most premium placement available."),
    (NAVY, "Tier 2 — Primary Keypad",
     "First 6–9 visible positions in the main keypad grid. Seen immediately when the app opens. No scrolling required. Highest traffic positions after Tier 1."),
    (MGREY, "Tier 3 — Slide-Out Panel",
     "Your store appears in the extended keypad panel (swipe to reveal). Still accessible and notified — ideal for entry-level platform participation."),
    (RGBColor(0x44,0x44,0x44), "Banner Advertisements",
     "A rotating advertisement strip displayed across all screens at the top of the app. Separate from keypad placement — available to any registered partner."),
]
for i, (color, title, body) in enumerate(tiers):
    x = 0.5 + (i % 2) * 6.35
    y = 2.55 + (i // 2) * 2.15
    add_rect(s, x, y, 6.1, 1.95, fill=color)
    add_text(s, title, x+0.18, y+0.14, 5.7, 0.45,
             size=13, bold=True,
             color=BLACK if color == GOLD else WHITE)
    add_text(s, body, x+0.18, y+0.62, 5.7, 1.2,
             size=11,
             color=NAVY if color == GOLD else RGBColor(0xD0,0xD8,0xE8) if color == NAVY else WHITE)

page_num(s, 10, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 11 — USER FEATURES SUMMARY
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Customer App Features")
heading(s, "What BiziBid Offers Your Customers")
sub(s, "A rich, engaging experience that keeps registered users checking the app every day.")

user_features = [
    ("📱", "Free to Download & Register",
     "The BiziBid app is free for all consumers. Registration requires name, email, and mobile number — quick and simple."),
    ("⚡", "Real-Time Live Bidding",
     "Bids update live on screen. Customers see every new bid the moment it is placed — no refreshing required."),
    ("🔴", "Instant Outbid Alerts",
     "Push notifications fire the moment a customer is outbid. They are brought back to the app to counter-bid immediately."),
    ("📌", "Pin Favourite Stores",
     "Customers pin their favourite store for prominent home screen placement and enhanced notification visibility."),
    ("🗂️", "Active Bids Panel",
     "A slide-out panel shows all active bids across all stores simultaneously. Customers manage multiple auctions without navigating away."),
    ("↗️", "Share Deals & Auctions",
     "One tap to share any deal or auction to WhatsApp, Instagram, or any app on their phone. Every share promotes your store."),
    ("🏷️", "Like & Save Deals",
     "Customers like deals they are interested in. High like counts signal popular products and drive walk-in intent."),
    ("🔑", "Unique Collection Code",
     "Every auction winner receives a unique code on their phone to present at your cashier — secure, simple, fraud-proof."),
]
for i, (icon, title, body) in enumerate(user_features):
    c, r = i % 4, i // 4
    feature_card(s, icon, title, body, l=0.38 + c*3.24, t=2.55 + r*1.9, w=3.05, h=1.78)

page_num(s, 11, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 12 — PRICING
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Partnership Pricing")
heading(s, "Simple, Transparent Pricing (BBD)")
sub(s, "All rates are fixed for the first 12 months for founding partners. No hidden fees.")

# Intro offer box — navy
add_rect(s, 0.5, 2.4, 12.3, 1.4, fill=NAVY)
add_rect(s, 0.5, 2.4, 0.06, 1.4, fill=GOLD)
add_text(s, "60 DAYS FREE", 0.7, 2.48, 2.5, 0.5,
         size=22, bold=True, color=GOLD)
add_text(s,
    "No monthly cost for the first 60 days. A $500.00 BBD deposit secures your primary advertisement "
    "placement within the app — guaranteeing your store is featured prominently to all registered "
    "users from day one.",
    3.3, 2.5, 9.3, 1.2, size=12, color=WHITE)

# Pricing table
headers = ["Service", "Description", "Rate (BBD)"]
rows = [
    ("Base Listing Package", "Up to 25 items listed per week on the app", "$450.00 / month"),
    ("Additional Items",     "Per additional 10 items above the 25-item base", "$150.00 / month"),
    ("Deal of the Week",     "Featured deal highlighted to all users for 7 days", "$150.00 / week"),
    ("Deal of the Month",    "Premium featured deal — top placement for full month", "$200.00 / month"),
]

th = 0.38; row_h = 0.52
table_t = 3.95
col_w = [3.8, 6.2, 2.1]
col_x = [0.5, 4.3, 10.5]

# Header row
for j, (hdr, cx, cw) in enumerate(zip(headers, col_x, col_w)):
    add_rect(s, cx, table_t, cw, th, fill=NAVY)
    add_text(s, hdr, cx+0.1, table_t+0.05, cw-0.15, th-0.08,
             size=11, bold=True, color=WHITE)

for i, row in enumerate(rows):
    bg = LIGHT if i % 2 == 0 else WHITE
    for j, (cell, cx, cw) in enumerate(zip(row, col_x, col_w)):
        add_rect(s, cx, table_t + th + i*row_h, cw, row_h, fill=bg)
        is_price = (j == 2)
        add_text(s, cell,
                 cx+0.1, table_t + th + i*row_h + 0.07,
                 cw-0.15, row_h-0.1,
                 size=11, bold=is_price,
                 color=NAVY if is_price else BLACK)

add_text(s,
    "All pricing in Barbados Dollars (BBD). Rates fixed for the first 12 months for founding partners. "
    "Keypad placement and banner ad pricing available on request.",
    0.5, 7.0, 12.3, 0.38, size=10, italic=True, color=LGREY)

page_num(s, 12, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 13 — WHY BIZIBID
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)
gold_bar(s)
logo_text(s)
section_label(s, "Why BiziBid?")
heading(s, "Built for Barbados Retail. Starting Today.")

reasons = [
    ("🏝️", "Barbados First",
     "BiziBid is built specifically for the Barbados market — the culture, the community, the retail landscape. Not a foreign platform adapted for the island."),
    ("📲", "Zero Technical Effort",
     "You upload products and set prices. INTERXDB operates the entire platform — the app, the hosting, the technology, the maintenance. Nothing more is required from you."),
    ("📈", "Keep Your Store Relevant",
     "Digital shopping is growing. BiziBid gives your store a daily digital presence that keeps you competitive with online alternatives — without the cost of building your own platform."),
    ("🔒", "Exclusive & Professional",
     "Only verified, registered businesses may list products on BiziBid. No individual sellers. No flea-market feel. A premium marketplace that reflects well on your brand."),
    ("👨‍👩‍👧", "Your Target Market",
     "BiziBid targets medium-to-high income earners and family units — the customers who already shop at your store. Reach them digitally where they are."),
    ("🌱", "Founding Partner Advantage",
     "Founding partners lock in rates for 12 months and secure preferred keypad placement before the platform opens to all retailers. Act now — positions are limited."),
]
for i, (icon, title, body) in enumerate(reasons):
    c, r = i % 3, i // 3
    feature_card(s, icon, title, body, l=0.4 + c*4.3, t=2.55 + r*2.0, w=4.05, h=1.82)

page_num(s, 13, TOTAL)

# ════════════════════════════════════════════════════════════════════════════
# SLIDE 14 — CALL TO ACTION
# ════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank_layout)
slide_bg(s, WHITE)

add_rect(s, 0, 0, 13.33, 5.5, fill=NAVY)
add_rect(s, 0, 5.5, 13.33, 0.08, fill=GOLD)

add_text(s, "Ready to Join BiziBid?",
         0.8, 0.7, 11.7, 0.9, size=36, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
add_text(s, "Secure your founding partner status today — positions are limited.",
         0.8, 1.65, 11.7, 0.55, size=16, color=LGREY, align=PP_ALIGN.CENTER)

# Three action cards
actions = [
    ("📞", "Schedule a Presentation",
     "We will come to you. A personalised walkthrough of the platform tailored to your store — at your convenience."),
    ("🌐", "View Your Interactive Demo",
     "A personalised before-and-after demonstration of how BiziBid would represent your store has been prepared for you."),
    ("✉️", "Contact Us Directly",
     "Our team is ready to answer any questions and walk you through the partnership terms at your pace."),
]
for i, (icon, title, body) in enumerate(actions):
    x = 0.8 + i * 3.95
    add_rect(s, x, 2.55, 3.65, 2.65, fill=RGBColor(0x12,0x2A,0x4A))
    add_rect(s, x, 2.55, 3.65, 0.05, fill=GOLD)
    add_text(s, icon, x+0.18, 2.65, 0.55, 0.5, size=22, color=GOLD)
    add_text(s, title, x+0.18, 3.22, 3.3, 0.5, size=12, bold=True, color=WHITE)
    add_text(s, body,  x+0.18, 3.72, 3.3, 1.3, size=10, color=LGREY)

# Contact block
logo_row = s.shapes.add_textbox(Inches(0.8), Inches(5.75), Inches(11.7), Inches(0.55))
tf = logo_row.text_frame
p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
r1 = p.add_run(); r1.text = "Bizi"; r1.font.size = Pt(18); r1.font.bold = True; r1.font.color.rgb = BLACK
r2 = p.add_run(); r2.text = "Bid"; r2.font.size = Pt(18); r2.font.bold = True; r2.font.color.rgb = GOLD
r3 = p.add_run(); r3.text = "  ·  Operated by INTERXDB"
r3.font.size = Pt(12); r3.font.color.rgb = MGREY

add_text(s,
    "contact@interxdb.com   ·   Tel 1(246) 241-3771   ·   BiziBid.com",
    0.8, 6.42, 11.7, 0.4, size=12, color=MGREY, align=PP_ALIGN.CENTER)
add_text(s,
    "Confidential — For Addressee Only",
    0.8, 6.9, 11.7, 0.35, size=10, italic=True, color=LGREY, align=PP_ALIGN.CENTER)

page_num(s, 14, TOTAL)

# ── SAVE ─────────────────────────────────────────────────────────────────────
out_dir = r"C:\AI Software\websites\Marketing"
pptx_path = os.path.join(out_dir, "BiziBid-Partner-Presentation.pptx")
prs.save(pptx_path)
print(f"Saved PowerPoint: {pptx_path}")


# ════════════════════════════════════════════════════════════════════════════
# HTML PRINT VERSION (open in browser → Print → Save as PDF)
# ════════════════════════════════════════════════════════════════════════════

slides_html = [
    # (slide_num, title, content_html)
    (1, "Cover", """
<div class="cover-slide">
  <div class="cover-band">
    <div class="cover-logo">Bizi<span>Bid</span></div>
    <div class="cover-tagline">Barbados' First Retail Auction &amp; Deals Platform</div>
    <div class="cover-sub">Partnership Opportunity &nbsp;·&nbsp; Confidential</div>
  </div>
  <div class="cover-footer">
    Presented by INTERXDB &nbsp;·&nbsp; Digital Retail &amp; Auction Platform &nbsp;·&nbsp; Barbados<br>
    bizibid.com &nbsp;·&nbsp; contact@interxdb.com &nbsp;·&nbsp; Tel 1(246) 241-3771
  </div>
</div>"""),

    (2, "What is BiziBid?", """
<div class="slide-label">Platform Overview</div>
<div class="slide-h1">What is BiziBid?</div>
<div class="slide-sub">A mobile-first auction and deals platform built exclusively for Barbados' retail market.</div>
<div class="card-row">
  <div class="card"><div class="card-icon">📱</div><div class="card-title">The BiziBid App</div><p>A free mobile app (iOS &amp; Android) where registered customers browse live auctions and exclusive deals — 24 hours a day, 7 days a week.</p></div>
  <div class="card"><div class="card-icon">🏪</div><div class="card-title">Your Back-Office Portal</div><p>A private web portal at BiziBid.com where your team uploads products, manages deals, reviews auction results, and tracks performance.</p></div>
  <div class="card"><div class="card-icon">🏆</div><div class="card-title">Operated by INTERXDB</div><p>INTERXDB owns and operates the entire platform — the app, the hosting, the technology. You simply list products. We handle everything else.</p></div>
</div>"""),

    (3, "The Opportunity", """
<div class="slide-label">The Opportunity</div>
<div class="slide-h1">Your Store — 24/7 in Every Customer's Pocket</div>
<div class="slide-sub">BiziBid keeps your brand top-of-mind every single day — whether your doors are open or not.</div>
<ul class="big-bullets">
  <li>Customers open the app daily to check new auctions and deals from your store</li>
  <li>Your store logo is displayed prominently on the app's home screen</li>
  <li>Exclusive auction prices (below shelf) create urgency and loyal repeat engagement</li>
  <li>Deals of the Week and Month drive customers physically through your doors</li>
  <li>Every deal or auction shared on WhatsApp or Instagram puts your brand in front of new potential customers — at no cost to you</li>
  <li>Founding retail partners secure premium placement before competitors</li>
</ul>"""),

    (4, "Customer Experience", """
<div class="slide-label">Customer Experience</div>
<div class="slide-h1">How Customers Experience BiziBid</div>
<div class="slide-sub">A beautifully simple home screen keeps customers focused on your store — and coming back every day.</div>
<div class="card-row">
  <div class="card"><div class="card-icon">⌨️</div><div class="card-title">The Store Keypad</div><p>Your store logo appears on the app's home screen — just like a speed-dial button. Customers tap it to see your live auctions and deals instantly.</p></div>
  <div class="card"><div class="card-icon">🔔</div><div class="card-title">Live Notifications</div><p>Colour-coded badge alerts on your store logo tell customers how many bids are active, who is watching, and when they have been outbid.</p></div>
  <div class="card"><div class="card-icon">📌</div><div class="card-title">Pin Your Store</div><p>Customers can pin your store as their favourite, giving your logo a prominent permanent position on their personal home screen.</p></div>
  <div class="card"><div class="card-icon">⚡</div><div class="card-title">One-Tap Bidding</div><p>Customers bid with a single tap without leaving the home screen. A sliding panel shows all active bids across all stores simultaneously.</p></div>
</div>"""),

    (5, "Live Auctions", """
<div class="slide-label">Feature — Auctions</div>
<div class="slide-h1">Live Auctions — Excitement That Sells</div>
<div class="slide-sub">Customers compete in real-time for your products. The excitement keeps them engaged and coming back.</div>
<div class="two-col">
  <ul class="big-bullets">
    <li>You upload products with a starting bid price (set below shelf price)</li>
    <li>Up to 25 items per week rotate through the platform automatically</li>
    <li>5 new items are released each day at varied morning hours — keeping customers checking in daily</li>
    <li>Auctions run for 3, 7, or 14 days depending on the item</li>
    <li>Real-time bidding — customers see bids update live on their screen</li>
    <li>Unsold items re-enter the rotation for the following week automatically</li>
  </ul>
  <div class="dark-box">
    <div class="dark-box-title">When a Customer Wins</div>
    <ol class="win-steps">
      <li>Auction closes — winner is confirmed</li>
      <li>A unique collection code is generated</li>
      <li>Winner receives code on their phone</li>
      <li>Winner visits your store and shows code to cashier</li>
      <li>Cashier confirms the code — item is collected</li>
      <li>Record of the sale is stored in your portal</li>
    </ol>
    <div class="dark-note">No online payment needed — all purchases are cash in-store.</div>
  </div>
</div>"""),

    (6, "Deals of the Week & Month", """
<div class="slide-label">Feature — Deals</div>
<div class="slide-h1">Deals of the Week &amp; Month — Drive Foot Traffic</div>
<div class="slide-sub">Fixed-price deals showcase your best offers and bring customers through your doors.</div>
<div class="two-col">
  <ul class="big-bullets">
    <li>You set a fixed price — no bidding, no auction pressure</li>
    <li>Customers see your deal prominently in the app all week or all month</li>
    <li>Customers can Like the deal — like count is visible to all users (social proof)</li>
    <li>Customers share deals directly to WhatsApp, Instagram, and other platforms</li>
    <li>Shared links show the deal to people who do not yet have the app — driving new downloads</li>
    <li>Walk-in customers ask for the deal by name — increased foot traffic guaranteed</li>
    <li>Deals of the Month offer extended 30-day visibility at premium placement</li>
  </ul>
  <div style="display:flex;flex-direction:column;gap:12px;">
    <div class="info-box light-box"><div class="ib-title">Deal of the Week</div><p>7-day fixed-price feature<br>Premium placement in app<br>Like + Share enabled<br>Drives walk-in purchase</p></div>
    <div class="info-box dark-box-sm"><div class="ib-title gold">Deal of the Month</div><p>Full 30-day visibility<br>Top placement position<br>Maximum brand exposure<br>Ideal for key product lines</p></div>
  </div>
</div>"""),

    (7, "Your Back-Office Portal", """
<div class="slide-label">Your Back-Office — BiziBid.com</div>
<div class="slide-h1">Your Private Management Portal</div>
<div class="slide-sub">Log in at BiziBid.com to manage your entire BiziBid presence — available 24/7 from any browser.</div>
<div class="card-row three">
  <div class="card"><div class="card-icon">📦</div><div class="card-title">Bulk Product Upload</div><p>Upload multiple products at once with images, descriptions, and your chosen starting bid price. No technical knowledge required.</p></div>
  <div class="card"><div class="card-icon">🏷️</div><div class="card-title">Deals Management</div><p>Create and schedule Deals of the Week and Deals of the Month. Set your own price and valid dates. Activate with one click.</p></div>
  <div class="card"><div class="card-icon">🏆</div><div class="card-title">Auction Results</div><p>View all completed auctions — winning bid amount, customer name, collection code. Full record of every sale.</p></div>
  <div class="card"><div class="card-icon">🔑</div><div class="card-title">Collection Codes</div><p>See the unique code for each auction winner so your cashier can verify the customer quickly and confidently.</p></div>
  <div class="card"><div class="card-icon">📄</div><div class="card-title">Invoice Download</div><p>View and download your monthly platform invoices as PDF. Full record of your subscription and activity charges.</p></div>
  <div class="card"><div class="card-icon">📊</div><div class="card-title">Store Statistics</div><p>Live dashboard showing user engagement, bid activity, deal shares, and more. Know exactly how customers interact with your store.</p></div>
</div>"""),

    (8, "Store Statistics", """
<div class="slide-label">Back-Office — Statistics Dashboard</div>
<div class="slide-h1">Know Your Customers — Live Store Statistics</div>
<div class="slide-sub">Your back-office portal shows you exactly how registered BiziBid users interact with your store in real time.</div>
<div class="stat-row">
  <div class="stat-card"><div class="stat-num">1,240</div><div class="stat-lbl">Registered users following your store</div></div>
  <div class="stat-card"><div class="stat-num">86</div><div class="stat-lbl">Active bids on your items today</div></div>
  <div class="stat-card"><div class="stat-num">312</div><div class="stat-lbl">Users watching your products</div></div>
  <div class="stat-card"><div class="stat-num">94%</div><div class="stat-lbl">Auction completion rate this month</div></div>
</div>
<div class="stat-row" style="margin-top:10px;">
  <div class="stat-card"><div class="stat-num">48</div><div class="stat-lbl">Deals shared on WhatsApp &amp; Instagram</div></div>
  <div class="stat-card"><div class="stat-num">$8,400</div><div class="stat-lbl">Total auction value generated this month</div></div>
  <div class="stat-card"><div class="stat-num">22</div><div class="stat-lbl">New app users from your shared links</div></div>
  <div class="stat-card"><div class="stat-num">4.8★</div><div class="stat-lbl">Average customer engagement score</div></div>
</div>
<div class="footnote-box">All statistics are updated in real time in your back-office portal. No data is shared with other retail partners.</div>"""),

    (9, "Viral Growth", """
<div class="slide-label">Feature — Viral Growth</div>
<div class="slide-h1">Every Share is Free Marketing for Your Store</div>
<div class="slide-sub">When customers share your auctions and deals, your store name reaches people who have never heard of BiziBid.</div>
<div class="flow-row">
  <div class="flow-box dark"><span class="flow-num">01</span>Your customer sees a great deal or live auction</div>
  <div class="flow-arrow">→</div>
  <div class="flow-box light"><span class="flow-num gold">02</span>They share it to WhatsApp or Instagram</div>
  <div class="flow-arrow">→</div>
  <div class="flow-box dark"><span class="flow-num">03</span>Their contact sees your store name, price &amp; product</div>
  <div class="flow-arrow">→</div>
  <div class="flow-box light"><span class="flow-num gold">04</span>They visit BiziBid.com and download the app</div>
  <div class="flow-arrow">→</div>
  <div class="flow-box dark"><span class="flow-num">05</span>New registered bidder — on your auctions</div>
</div>
<div class="footnote-box" style="margin-top:14px;">
  <b>Auction shares</b> show the live bid price and countdown — creating instant urgency for the viewer.<br>
  <b>Deal shares</b> show your store name, product image, and fixed price — driving walk-in intent.<br>
  All shared links direct visitors to BiziBid.com to download the app. New downloads = new bidders on your products.
</div>"""),

    (10, "Keypad Placement", """
<div class="slide-label">Placement &amp; Visibility</div>
<div class="slide-h1">Secure Your Position on the BiziBid Keypad</div>
<div class="slide-sub">Your store logo placement on the app home screen is a paid position. First come, first placed.</div>
<div class="tier-row">
  <div class="tier gold-tier"><div class="tier-label">Tier 1 — Pinned Position</div><p>Top of every user's home screen. Your logo is displayed largest, with full notification badge visibility. One store only — the most premium placement available.</p></div>
  <div class="tier navy-tier"><div class="tier-label">Tier 2 — Primary Keypad</div><p>First 6–9 visible positions in the main keypad grid. Seen immediately when the app opens. No scrolling required. Highest traffic positions after Tier 1.</p></div>
  <div class="tier grey-tier"><div class="tier-label">Tier 3 — Slide-Out Panel</div><p>Your store appears in the extended keypad panel. Still fully accessible and notified — ideal for entry-level platform participation.</p></div>
  <div class="tier dark-tier"><div class="tier-label">Banner Advertisements</div><p>A rotating advertisement strip displayed across all screens. Separate from keypad placement — available to any registered partner.</p></div>
</div>"""),

    (11, "Customer App Features", """
<div class="slide-label">Customer App Features</div>
<div class="slide-h1">What BiziBid Offers Your Customers</div>
<div class="slide-sub">A rich, engaging experience that keeps registered users checking the app every day.</div>
<div class="card-row four">
  <div class="card sm"><div class="card-icon">📱</div><div class="card-title">Free to Download</div><p>The app is free. Quick registration — name, email, mobile number.</p></div>
  <div class="card sm"><div class="card-icon">⚡</div><div class="card-title">Real-Time Bidding</div><p>Bids update live. No refreshing required. Instant engagement.</p></div>
  <div class="card sm"><div class="card-icon">🔴</div><div class="card-title">Outbid Alerts</div><p>Push notifications fire the moment a customer is outbid. They return to bid immediately.</p></div>
  <div class="card sm"><div class="card-icon">📌</div><div class="card-title">Pin Favourite Stores</div><p>Customers pin their favourite store for prominent home screen placement.</p></div>
  <div class="card sm"><div class="card-icon">🗂️</div><div class="card-title">Active Bids Panel</div><p>Slide-out panel shows all active bids across all stores — no navigation required.</p></div>
  <div class="card sm"><div class="card-icon">↗️</div><div class="card-title">Share Deals &amp; Auctions</div><p>One tap to share to WhatsApp, Instagram, or any app on their phone.</p></div>
  <div class="card sm"><div class="card-icon">🏷️</div><div class="card-title">Like &amp; Save Deals</div><p>Customers like deals. High like counts signal popular products and drive walk-in intent.</p></div>
  <div class="card sm"><div class="card-icon">🔑</div><div class="card-title">Collection Code</div><p>Every winner receives a unique code to present at your cashier — secure and fraud-proof.</p></div>
</div>"""),

    (12, "Pricing", """
<div class="slide-label">Partnership Pricing</div>
<div class="slide-h1">Simple, Transparent Pricing (BBD)</div>
<div class="slide-sub">All rates are fixed for the first 12 months for founding partners. No hidden fees.</div>
<div class="offer-box"><span class="offer-days">60 DAYS FREE</span> No monthly cost for the first 60 days. A <b>$500.00 BBD</b> deposit secures your primary advertisement placement — guaranteeing your store is featured prominently to all registered users from day one.</div>
<table class="price-table">
  <thead><tr><th>Service</th><th>Description</th><th>Rate (BBD)</th></tr></thead>
  <tbody>
    <tr><td><b>Base Listing Package</b></td><td>Up to 25 items listed per week on the app</td><td class="price">$450.00 / month</td></tr>
    <tr class="alt"><td><b>Additional Items</b></td><td>Per additional 10 items above the 25-item base</td><td class="price">$150.00 / month</td></tr>
    <tr><td><b>Deal of the Week</b></td><td>Featured deal highlighted to all users for 7 days</td><td class="price">$150.00 / week</td></tr>
    <tr class="alt"><td><b>Deal of the Month</b></td><td>Premium featured deal — top placement for full month</td><td class="price">$200.00 / month</td></tr>
  </tbody>
</table>
<div class="table-note">All pricing in Barbados Dollars (BBD). Rates fixed for the first 12 months for founding partners. Keypad placement and banner ad pricing available on request.</div>"""),

    (13, "Why BiziBid?", """
<div class="slide-label">Why BiziBid?</div>
<div class="slide-h1">Built for Barbados Retail. Starting Today.</div>
<div class="card-row three">
  <div class="card"><div class="card-icon">🏝️</div><div class="card-title">Barbados First</div><p>Built specifically for the Barbados market — the culture, the community, the retail landscape. Not a foreign platform adapted for the island.</p></div>
  <div class="card"><div class="card-icon">📲</div><div class="card-title">Zero Technical Effort</div><p>You upload products and set prices. INTERXDB operates the entire platform. Nothing more is required from you.</p></div>
  <div class="card"><div class="card-icon">📈</div><div class="card-title">Keep Your Store Relevant</div><p>BiziBid gives your store a daily digital presence that keeps you competitive — without the cost of building your own platform.</p></div>
  <div class="card"><div class="card-icon">🔒</div><div class="card-title">Exclusive &amp; Professional</div><p>Only verified, registered businesses may list products. No individual sellers. A premium marketplace that reflects well on your brand.</p></div>
  <div class="card"><div class="card-icon">👨‍👩‍👧</div><div class="card-title">Your Target Market</div><p>BiziBid targets medium-to-high income earners and family units — the customers who already shop at your store.</p></div>
  <div class="card"><div class="card-icon">🌱</div><div class="card-title">Founding Partner Advantage</div><p>Founding partners lock in rates for 12 months and secure preferred keypad placement before the platform opens to all retailers.</p></div>
</div>"""),

    (14, "Get Started", """
<div class="cover-slide cta-slide">
  <div class="cover-band">
    <div class="cover-logo" style="font-size:42px;">Bizi<span>Bid</span></div>
    <div class="cover-tagline" style="font-size:26px;margin-top:12px;">Ready to Join BiziBid?</div>
    <div class="cover-sub">Secure your founding partner status today — positions are limited.</div>
    <div class="cta-cards">
      <div class="cta-card"><div class="cta-icon">📞</div><div class="cta-title">Schedule a Presentation</div><p>A personalised walkthrough at your convenience.</p></div>
      <div class="cta-card"><div class="cta-icon">🌐</div><div class="cta-title">View Your Interactive Demo</div><p>A personalised before-and-after demonstration prepared for your store.</p></div>
      <div class="cta-card"><div class="cta-icon">✉️</div><div class="cta-title">Contact Us Directly</div><p>Our team is ready to answer any questions and walk you through the terms.</p></div>
    </div>
  </div>
  <div class="cover-footer">
    BiziBid &nbsp;·&nbsp; Operated by INTERXDB &nbsp;·&nbsp; contact@interxdb.com &nbsp;·&nbsp; Tel 1(246) 241-3771 &nbsp;·&nbsp; BiziBid.com<br>
    <span style="font-size:10px;color:#6B7280;">Confidential — For Addressee Only</span>
  </div>
</div>"""),
]

css = """
@page { size: 13.33in 7.5in; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Arial, sans-serif; background: #ccc; }
.slide { width: 13.33in; height: 7.5in; background: #fff; position: relative; page-break-after: always; overflow: hidden; display: flex; flex-direction: column; padding: 0.45in 0.5in 0.4in; }
.slide:last-child { page-break-after: avoid; }
.gold-bar { position: absolute; bottom: 0; left: 0; right: 0; height: 0.09in; background: #C9A84C; }
.logo-top { position: absolute; top: 0.2in; left: 0.4in; font-size: 22pt; font-weight: 900; }
.logo-top .bizi { color: #0A0A0A; }
.logo-top .bid  { color: #C9A84C; }
.page-num { position: absolute; bottom: 0.2in; right: 0.4in; font-size: 9pt; color: #9CA3AF; }

.slide-label { font-size: 9pt; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; color: #C9A84C; margin-top: 0.55in; margin-bottom: 0.06in; }
.slide-h1 { font-size: 28pt; font-weight: 900; color: #0A0A0A; margin-bottom: 0.08in; line-height: 1.15; }
.slide-sub { font-size: 13pt; color: #4B5563; margin-bottom: 0.22in; }

.card-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.14in; margin-top: 0.1in; }
.card-row.four { grid-template-columns: repeat(4, 1fr); }
.card { background: #F8F8F8; padding: 0.16in; border-left: 0.05in solid #C9A84C; }
.card.sm { padding: 0.12in; }
.card-icon { font-size: 18pt; margin-bottom: 0.06in; }
.card-title { font-size: 11pt; font-weight: 700; color: #0A0A0A; margin-bottom: 0.06in; }
.card p { font-size: 10pt; color: #4B5563; line-height: 1.45; }
.card.sm p { font-size: 9pt; }

.big-bullets { list-style: none; padding-left: 0; }
.big-bullets li { font-size: 13pt; color: #0A0A0A; padding: 0.06in 0; padding-left: 0.2in; position: relative; border-bottom: 1px solid #F3F4F6; }
.big-bullets li::before { content: "▸"; color: #C9A84C; position: absolute; left: 0; }

.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 0.22in; }
.dark-box { background: #0B1F3A; padding: 0.18in; color: #fff; }
.dark-box-title { font-size: 12pt; font-weight: 700; color: #C9A84C; margin-bottom: 0.1in; }
.win-steps { padding-left: 0.18in; }
.win-steps li { font-size: 11pt; color: #fff; padding: 0.04in 0; }
.dark-note { font-size: 9pt; color: #9CA3AF; margin-top: 0.1in; font-style: italic; }
.info-box { padding: 0.14in; border-left: 0.05in solid #C9A84C; }
.light-box { background: #F8F8F8; }
.dark-box-sm { background: #0B1F3A; }
.ib-title { font-size: 11pt; font-weight: 700; color: #0A0A0A; margin-bottom: 0.06in; }
.ib-title.gold { color: #C9A84C; }
.info-box p { font-size: 10pt; color: #4B5563; line-height: 1.6; }
.dark-box-sm p { color: #C0C8D8; }

.stat-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.12in; }
.stat-card { background: #F8F8F8; padding: 0.12in; text-align: center; border-top: 0.04in solid #C9A84C; }
.stat-num { font-size: 26pt; font-weight: 900; color: #C9A84C; }
.stat-lbl { font-size: 9pt; color: #4B5563; margin-top: 0.04in; line-height: 1.3; }
.footnote-box { background: #F8F8F8; border-left: 0.05in solid #C9A84C; padding: 0.12in; font-size: 10pt; color: #4B5563; line-height: 1.5; margin-top: 0.14in; }

.flow-row { display: flex; align-items: stretch; gap: 0; margin: 0.1in 0; }
.flow-box { flex: 1; padding: 0.14in; font-size: 11pt; position: relative; line-height: 1.4; }
.flow-box.dark  { background: #0B1F3A; color: #fff; }
.flow-box.light { background: #F8F8F8; color: #0A0A0A; }
.flow-num { display: block; font-size: 9pt; font-weight: 700; color: #9CA3AF; margin-bottom: 0.06in; }
.flow-num.gold { color: #C9A84C; }
.flow-arrow { display: flex; align-items: center; font-size: 18pt; color: #C9A84C; padding: 0 0.06in; background: #F8F8F8; }

.tier-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.14in; margin-top: 0.1in; }
.tier { padding: 0.18in; color: #fff; }
.tier.gold-tier  { background: #C9A84C; color: #0A0A0A; }
.tier.navy-tier  { background: #0B1F3A; }
.tier.grey-tier  { background: #4B5563; }
.tier.dark-tier  { background: #1F2937; }
.tier-label { font-size: 11pt; font-weight: 700; margin-bottom: 0.1in; }
.gold-tier .tier-label { color: #0A0A0A; }
.tier p { font-size: 10pt; line-height: 1.45; opacity: 0.9; }
.gold-tier p { color: #2A1800; opacity: 0.85; }

.offer-box { background: #0B1F3A; color: #fff; padding: 0.16in; border-left: 0.06in solid #C9A84C; font-size: 12pt; line-height: 1.5; margin-bottom: 0.18in; }
.offer-days { font-size: 18pt; font-weight: 900; color: #C9A84C; margin-right: 0.12in; }
.price-table { width: 100%; border-collapse: collapse; font-size: 11pt; }
.price-table thead tr { background: #0B1F3A; }
.price-table thead th { padding: 0.1in; text-align: left; color: #fff; font-weight: 700; font-size: 10pt; }
.price-table tbody td { padding: 0.09in 0.1in; color: #0A0A0A; border-bottom: 1px solid #E5E7EB; }
.price-table tbody tr.alt td { background: #F8F8F8; }
.price-table tbody td.price { font-weight: 700; color: #0B1F3A; }
.table-note { font-size: 9pt; color: #9CA3AF; margin-top: 0.1in; font-style: italic; }

.cover-slide { width: 100%; height: 100%; display: flex; flex-direction: column; padding: 0; }
.cover-band { background: #0B1F3A; flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 0.5in; }
.cover-logo { font-size: 72pt; font-weight: 900; letter-spacing: -2px; line-height: 1; }
.cover-logo .bizi, .cover-logo span.bizi { color: #fff; }
.cover-logo span { color: #C9A84C; }
.cover-tagline { font-size: 18pt; color: #C0C8D8; margin-top: 0.15in; text-align: center; }
.cover-sub { font-size: 12pt; color: #5A6678; margin-top: 0.1in; font-style: italic; text-align: center; }
.cover-footer { background: #fff; padding: 0.18in 0.4in; font-size: 11pt; color: #4B5563; text-align: center; }
.cta-cards { display: flex; gap: 0.2in; margin-top: 0.3in; }
.cta-card { background: #122A4A; padding: 0.2in; flex: 1; border-top: 0.05in solid #C9A84C; }
.cta-icon { font-size: 18pt; margin-bottom: 0.08in; }
.cta-title { font-size: 12pt; font-weight: 700; color: #fff; margin-bottom: 0.06in; }
.cta-card p { font-size: 10pt; color: #9CA3AF; }
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>BiziBid — Retail Partner Presentation</title>
<style>{css}</style>
</head>
<body>
"""

for num, title, content in slides_html:
    html += f"""<div class="slide">
  <div class="logo-top"><span class="bizi">Bizi</span><span class="bid">Bid</span></div>
  {content}
  <div class="gold-bar"></div>
  <div class="page-num">{num} / {TOTAL}</div>
</div>\n"""

html += "</body></html>"

pdf_html_path = os.path.join(out_dir, "BiziBid-Partner-Presentation-PRINT.html")
with open(pdf_html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Saved print HTML: {pdf_html_path}")
print("To generate PDF: Open the HTML file in Chrome > File > Print > Save as PDF > set paper size to 13.33x7.5in (or Tabloid Landscape)")
print("\nAll done.")
