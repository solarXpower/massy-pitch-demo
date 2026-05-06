"""BiziBid HTML Marketing Letter + Email Template Generator
Generates marketing-letter.html and email-template.html for all 7 clients.
Run:  python generate_html_letters.py
"""
import os

BASE = r'C:\AI Software\WebSites'

CSS = """
    :root { --navy:#0B1F3A; --blue:#1A4A8A; --gold:#C9A84C; --light:#F7F9FC; --border:#D8E2EF; --text:#2C3E50; --muted:#6B7280; }
    * { box-sizing:border-box; margin:0; padding:0; }
    body { font-family:'Roboto',sans-serif; background:#E8EDF3; color:var(--text); }
    .page { max-width:820px; margin:40px auto; background:#fff; box-shadow:0 4px 32px rgba(0,0,0,0.12); }

    .letterhead { background:var(--navy); padding:36px 48px 28px; display:flex; align-items:center; justify-content:space-between; }
    .lh-brand   { display:flex; flex-direction:column; gap:4px; }
    .lh-name    { font-family:'Montserrat',sans-serif; font-size:32px; font-weight:900; color:#fff; letter-spacing:-1px; }
    .lh-name span { color:var(--gold); }
    .lh-sub     { font-size:11px; color:rgba(255,255,255,0.65); }
    .lh-sub strong { color:var(--gold); }
    .lh-tag     { font-size:10px; color:rgba(255,255,255,0.4); letter-spacing:2px; text-transform:uppercase; }
    .lh-contact { text-align:right; }
    .lh-contact p { font-size:11px; color:rgba(255,255,255,0.6); line-height:1.9; }
    .lh-contact a { color:var(--gold); text-decoration:none; }
    .gold-bar   { height:5px; background:linear-gradient(to right,var(--gold),#e8c870,var(--gold)); }

    .letter-body { padding:48px 56px 56px; }
    .date-line  { font-size:13px; color:var(--muted); margin-bottom:28px; }
    .recipient  { margin-bottom:28px; }
    .recipient p { font-size:14px; line-height:1.8; }
    .recipient strong { color:var(--navy); }

    .subject-line { background:var(--light); border-left:4px solid var(--gold); padding:14px 20px; margin-bottom:32px; border-radius:0 6px 6px 0; }
    .subject-line p { font-size:13px; color:var(--muted); font-weight:500; text-transform:uppercase; letter-spacing:1px; }
    .subject-line h2 { font-family:'Montserrat',sans-serif; font-size:18px; font-weight:800; color:var(--navy); margin-top:4px; }

    .body-text { font-size:14px; line-height:1.9; color:var(--text); margin-bottom:22px; }

    .section-block { margin:32px 0; }
    .section-block h3 { font-family:'Montserrat',sans-serif; font-size:13px; font-weight:800; text-transform:uppercase; letter-spacing:2px; color:var(--blue); margin-bottom:14px; padding-bottom:8px; border-bottom:1px solid var(--border); }

    .how-grid { display:grid; grid-template-columns:1fr 1fr; gap:16px; }
    .how-card { background:var(--light); border-radius:8px; padding:18px; border:1px solid var(--border); }
    .how-card-num   { font-family:'Montserrat',sans-serif; font-size:28px; font-weight:900; color:var(--gold); line-height:1; margin-bottom:8px; }
    .how-card-title { font-weight:700; font-size:13px; color:var(--navy); margin-bottom:6px; }
    .how-card-body  { font-size:12px; color:var(--muted); line-height:1.7; }

    .pricing-table { width:100%; border-collapse:collapse; font-size:13px; }
    .pricing-table thead tr { background:var(--navy); color:#fff; }
    .pricing-table thead th { padding:12px 16px; text-align:left; font-weight:700; letter-spacing:0.5px; font-size:12px; }
    .pricing-table tbody tr { border-bottom:1px solid var(--border); }
    .pricing-table tbody tr:nth-child(even) { background:var(--light); }
    .pricing-table tbody td { padding:12px 16px; color:var(--text); }
    .pricing-table tbody td:last-child { font-weight:700; color:var(--navy); }
    .pricing-table tfoot tr { background:#F0F4F0; }
    .pricing-table tfoot td { padding:12px 16px; font-size:12px; color:var(--muted); font-style:italic; }

    .free-offer { background:linear-gradient(135deg,#0B1F3A 0%,#1A4A8A 100%); border-radius:10px; padding:28px 32px; margin:28px 0; display:flex; align-items:center; gap:24px; }
    .free-offer-badge { background:var(--gold); color:var(--navy); font-family:'Montserrat',sans-serif; font-weight:900; font-size:13px; padding:10px 18px; border-radius:6px; text-align:center; white-space:nowrap; letter-spacing:0.5px; flex-shrink:0; }
    .free-offer-badge span { display:block; font-size:28px; font-weight:900; line-height:1.1; }
    .free-offer-text h4 { font-family:'Montserrat',sans-serif; font-size:16px; font-weight:800; color:#fff; margin-bottom:6px; }
    .free-offer-text p  { font-size:12px; color:rgba(255,255,255,0.75); line-height:1.7; }

    .product-list { padding-left:20px; margin:8px 0; }
    .product-list li { font-size:13px; color:var(--text); line-height:1.9; }

    .pitch-links { display:flex; flex-direction:column; gap:12px; margin-top:16px; }
    .pitch-link-card { display:flex; align-items:center; justify-content:space-between; border:1px solid var(--border); border-radius:8px; padding:14px 18px; background:var(--light); text-decoration:none; }
    .plc-left { display:flex; align-items:center; gap:14px; }
    .plc-dot  { width:36px; height:36px; border-radius:8px; background:var(--navy); display:flex; align-items:center; justify-content:center; font-size:18px; flex-shrink:0; }
    .plc-name  { font-weight:700; font-size:13px; color:var(--navy); }
    .plc-url   { font-size:11px; color:var(--muted); margin-top:2px; }
    .plc-arrow { font-size:18px; color:var(--gold); }

    .obligations { border:1px solid #E8D5D5; background:#FFF8F8; border-radius:8px; padding:20px 22px; }
    .obligations h4 { font-weight:700; font-size:13px; color:#8B1A1A; margin-bottom:10px; }
    .obligations ul { padding-left:18px; }
    .obligations li { font-size:13px; color:var(--text); line-height:1.9; }

    .asset-grid { display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:8px; }
    .asset-card { background:var(--light); border-radius:8px; padding:18px; border:1px solid var(--border); }
    .asset-card h4 { font-weight:700; font-size:13px; color:var(--navy); margin-bottom:8px; }
    .asset-card p  { font-size:12px; color:var(--muted); line-height:1.7; }

    .signature { margin-top:40px; padding-top:28px; border-top:1px solid var(--border); }
    .signature p { font-size:14px; line-height:1.9; margin-bottom:6px; }
    .sig-name    { font-family:'Montserrat',sans-serif; font-size:20px; font-weight:900; color:var(--navy); margin-top:16px; }
    .sig-name span { color:var(--gold); }
    .sig-sub     { font-size:12px; color:var(--muted); margin-top:4px; }
    .sig-sub strong { color:var(--gold); }
    .sig-tag     { font-size:11px; color:var(--muted); margin-top:2px; }
    .sig-contact { margin-top:12px; font-size:13px; color:var(--muted); line-height:1.9; }
    .sig-contact a { color:var(--blue); text-decoration:none; }

    .letter-footer { background:var(--navy); padding:18px 48px; display:flex; align-items:center; justify-content:space-between; }
    .lf-left  { font-family:'Montserrat',sans-serif; font-size:13px; font-weight:800; }
    .lf-bizi  { color:var(--gold); }
    .lf-bid   { color:#fff; }
    .lf-by    { color:rgba(255,255,255,0.55); font-weight:400; font-size:12px; }
    .lf-right { font-size:11px; color:rgba(255,255,255,0.45); }
    @media print { body{background:#fff;} .page{box-shadow:none;margin:0;} }
"""

def letterhead_html(contact_email_subject=""):
    return f"""  <div class="letterhead">
    <div class="lh-brand">
      <div class="lh-name">INTER<span>XDB</span></div>
      <div class="lh-sub">Presenting <strong>BiziBid</strong> — bizibid.com</div>
      <div class="lh-tag">Barbados&#39; First Retail Auction &amp; Deals App</div>
    </div>
    <div class="lh-contact">
      <p><a href="mailto:contact@bizibid.com">contact@bizibid.com</a><br>
         Tel: 1(246) 241-3771<br>
         www.bizibid.com<br>
         www.interxdb.com</p>
    </div>
  </div>
  <div class="gold-bar"></div>"""


def footer_html():
    return """  <div class="letter-footer">
    <div class="lf-left"><span class="lf-bizi">Bizi</span><span class="lf-bid">Bid</span> <span class="lf-by">by INTERXDB — Auction &amp; Get Buzz</span></div>
    <div class="lf-right">Confidential — For Addressee Only</div>
  </div>"""


def signature_html():
    return """    <div class="signature">
      <p>Yours sincerely,</p>
      <div class="sig-name">INTER<span>XDB</span></div>
      <div class="sig-sub">Presenting the <strong>BiziBid</strong> Platform</div>
      <div class="sig-tag">Barbados&#39; First Retail Auction &amp; Deals App</div>
      <div class="sig-contact">
        ✉ <a href="mailto:contact@bizibid.com">contact@bizibid.com</a> &nbsp;|&nbsp;
        📞 Tel 1(246) 241-3771 &nbsp;|&nbsp;
        🌐 <a href="https://www.bizibid.com">www.bizibid.com</a>
      </div>
    </div>"""


def how_it_works_merchant():
    items = [
        ("01", "App-Only Marketplace",
         "All auctions, Deals of the Week, and Deals of the Month run exclusively through "
         "the BiziBid mobile app (iOS &amp; Android). Download free at bizibid.com."),
        ("02", "Registered Businesses Only",
         "Only verified retail businesses may list products. No private sellers — "
         "a professional marketplace that protects your brand."),
        ("03", "25-Item Weekly Limit",
         "Up to 25 items per store per week. Controlled supply creates scarcity, "
         "drives urgency, and maximises competitive bidding."),
        ("04", "Free Customer Registration",
         "Customers register on BiziBid at no cost. Stores promote the app in-store "
         "and via social media to grow the bidder audience."),
    ]
    cards = "\n".join(
        f'        <div class="how-card">'
        f'<div class="how-card-num">{n}</div>'
        f'<div class="how-card-title">{t}</div>'
        f'<div class="how-card-body">{b}</div></div>'
        for n, t, b in items
    )
    return f"""    <div class="section-block">
      <h3>How the BiziBid Platform Works</h3>
      <div class="how-grid">
{cards}
      </div>
    </div>"""


def how_it_works_bank():
    items = [
        ("01", "Asset Submission",
         "Your team submits asset details (photos, description, reserve price) via the "
         "BiziBid.com portal. INTERXDB reviews and publishes within 24 hours."),
        ("02", "Instant Bidder Reach",
         "The asset immediately reaches all registered BiziBid users in Barbados. "
         "Push notifications alert users watching similar assets."),
        ("03", "Transparent Live Bidding",
         "All bids are live and visible. No closed-door negotiations. Maximum fair "
         "market value is achieved through open competition."),
        ("04", "Fast Disposal",
         "Assets move faster than traditional auctions — reducing holding costs, "
         "administration burden, and legal exposure on stale inventory."),
    ]
    cards = "\n".join(
        f'        <div class="how-card">'
        f'<div class="how-card-num">{n}</div>'
        f'<div class="how-card-title">{t}</div>'
        f'<div class="how-card-body">{b}</div></div>'
        for n, t, b in items
    )
    return f"""    <div class="section-block">
      <h3>How BiziBid Works for Financial Institutions</h3>
      <div class="how-grid">
{cards}
      </div>
    </div>"""


def free_offer_html(store_ref):
    return f"""    <div class="free-offer">
      <div class="free-offer-badge"><span>60</span>DAYS FREE</div>
      <div class="free-offer-text">
        <h4>Zero Cost for Your First 60 Days</h4>
        <p>Full access to the BiziBid platform at no monthly cost for 60 days. A
           <strong style="color:var(--gold);">$500.00 deposit</strong> secures primary
           ad placement within the BiziBid app for {store_ref} from day one.
           Refundable subject to terms.</p>
      </div>
    </div>"""


def pricing_table_merchant():
    return """    <div class="section-block">
      <h3>Platform Pricing — After 60-Day Introductory Period (BBD)</h3>
      <table class="pricing-table">
        <thead><tr><th>Service</th><th>Description</th><th>Rate (BBD)</th></tr></thead>
        <tbody>
          <tr><td><strong>Base Listing Package</strong></td><td>Up to 25 items listed per week on the BiziBid app</td><td>$450.00 / month</td></tr>
          <tr><td><strong>Additional Items</strong></td><td>Per additional 10 items above the 25-item base</td><td>$150.00 / month</td></tr>
          <tr><td><strong>Deal of the Week</strong></td><td>Featured deal highlighted to all BiziBid users for 7 days</td><td>$150.00 / week</td></tr>
          <tr><td><strong>Deal of the Month</strong></td><td>Premium featured deal — top placement for the full month</td><td>$200.00 / month</td></tr>
        </tbody>
        <tfoot><tr><td colspan="3">All pricing in Barbados Dollars (BBD). Rates fixed for first 12 months for founding partners.</td></tr></tfoot>
      </table>
    </div>"""


def pricing_table_bank():
    return """    <div class="section-block">
      <h3>Platform Pricing — After 60-Day Introductory Period (BBD)</h3>
      <table class="pricing-table">
        <thead><tr><th>Service</th><th>Best For</th><th>Rate (BBD)</th></tr></thead>
        <tbody>
          <tr><td><strong>Base Listing Package</strong></td><td>Up to 25 asset listings per week (vehicles)</td><td>$450.00 / month</td></tr>
          <tr><td><strong>Additional Listings</strong></td><td>Per additional 10 assets above the 25-item base</td><td>$150.00 / month</td></tr>
          <tr><td><strong>Deal of the Week</strong></td><td>Featured vehicle — maximum 7-day exposure</td><td>$150.00 / week</td></tr>
          <tr><td><strong>Deal of the Month</strong></td><td>Foreclosed property — full month top placement</td><td>$200.00 / month</td></tr>
        </tbody>
        <tfoot><tr><td colspan="3">All pricing in BBD. Volume pricing available for institutions listing 10+ assets monthly.</td></tr></tfoot>
      </table>
    </div>"""


def obligations_html():
    return """    <div class="section-block">
      <h3>Partner Obligations &amp; Platform Conduct</h3>
      <div class="obligations">
        <h4>BiziBid Store Partner Responsibilities</h4>
        <ul>
          <li>Actively promote the BiziBid app in-store (signage, POS) and across all social media and marketing channels.</li>
          <li>Ensure all listed products are accurately described, available, and fulfilled upon auction completion.</li>
          <li>Honour all winning BiziBid auction bids — failure to fulfil may result in suspension from the platform.</li>
          <li>Maintain professional communication with winning customers through the BiziBid platform.</li>
        </ul>
      </div>
      <p class="body-text" style="margin-top:16px;"><strong>User Conduct:</strong> Customers who fail to honour confirmed BiziBid auction wins will be banned. Disputes are reviewed with evidence from both parties before action is taken.</p>
    </div>"""


def pitch_section_html(pitch_url, pitch_label, company_name):
    if pitch_url:
        return f"""    <div class="section-block">
      <h3>See the Vision — Your Interactive Demo</h3>
      <p class="body-text" style="margin-bottom:16px;">We have prepared a personalised interactive demonstration of the BiziBid platform for {company_name}. Click below to view:</p>
      <div class="pitch-links">
        <a class="pitch-link-card" href="{pitch_url}" target="_blank">
          <div class="plc-left">
            <div class="plc-dot">▶</div>
            <div>
              <div class="plc-name">{pitch_label}</div>
              <div class="plc-url">{pitch_url.replace("https://","")}</div>
            </div>
          </div>
          <div class="plc-arrow">→</div>
        </a>
      </div>
    </div>"""
    else:
        return """    <div class="section-block">
      <h3>Live Platform Demo</h3>
      <p class="body-text">Visit <strong>www.bizibid.com</strong> for the full interactive platform walkthrough and live app demo. We are happy to arrange an in-person demonstration at your premises.</p>
    </div>"""


# ── MERCHANT LETTER ──────────────────────────────────────────────────────────
def build_html_letter(
        company_name, greeting, pitch_url, pitch_label,
        store_ref, industry_intro, product_examples,
        body_para2, closing_sentence, output_path):

    products_html = ""
    if product_examples:
        items = "\n".join(f"          <li>{ex}</li>" for ex in product_examples)
        products_html = f"""    <div class="section-block">
      <h3>Products Well-Suited for BiziBid Auctions</h3>
      <ul class="product-list">
{items}
      </ul>
    </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BiziBid — Partnership Letter — {company_name}</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">
  <style>{CSS}</style>
</head>
<body>
<div class="page">

{letterhead_html()}

  <div class="letter-body">
    <p class="date-line">May 2026</p>

    <div class="recipient">
      <p><strong>The Management Team</strong><br>{company_name}<br>Barbados</p>
    </div>

    <div class="subject-line">
      <p>Partnership Invitation</p>
      <h2>Introducing BiziBid — Barbados&#39; First Retail Auction &amp; Deals App</h2>
    </div>

    <p class="body-text">Dear {greeting},</p>

    <p class="body-text">On behalf of INTERXDB, we are pleased to extend this exclusive invitation to {company_name} to become one of the founding retail partners on BiziBid — the island&#39;s first dedicated business-to-consumer mobile auction and deals platform.</p>

    <p class="body-text">{industry_intro} The BiziBid app is now available at www.bizibid.com and on iOS and Android. INTERXDB owns and operates the complete technology — the platform, the BiziBid mobile app, all hosting, and all technical services. You simply list products — we handle the rest.</p>

    <p class="body-text">The BiziBid platform is designed with one purpose: <strong>to keep {store_ref} as the buzz word in every Barbadian household, 24 hours a day, 7 days a week</strong> — whether your doors are open or not.</p>

{products_html}

{how_it_works_merchant()}

    <div class="section-block">
      <h3>Introductory Offer — No Monthly Cost for 60 Days</h3>
{free_offer_html(store_ref)}
    </div>

{pricing_table_merchant()}

{pitch_section_html(pitch_url, pitch_label, company_name)}

{obligations_html()}

    <p class="body-text">{closing_sentence}</p>
    <p class="body-text">We welcome the opportunity to schedule a BiziBid presentation at your convenience. Contact us at <a href="mailto:contact@bizibid.com">contact@bizibid.com</a> or visit www.bizibid.com.</p>

{signature_html()}
  </div>

{footer_html()}
</div>
</body>
</html>"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Saved letter: {output_path}')


# ── BANK LETTER ──────────────────────────────────────────────────────────────
def build_html_bank_letter(
        company_name, greeting, bank_ref,
        closing_sentence, output_path):

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BiziBid — Partnership Letter — {company_name}</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">
  <style>{CSS}</style>
</head>
<body>
<div class="page">

{letterhead_html()}

  <div class="letter-body">
    <p class="date-line">May 2026</p>

    <div class="recipient">
      <p><strong>Asset Management &amp; Recovery Division</strong><br>{company_name}<br>Barbados</p>
    </div>

    <div class="subject-line">
      <p>Partnership Invitation — Asset Disposal</p>
      <h2>BiziBid — Fast, Transparent Asset Disposal for Financial Institutions</h2>
    </div>

    <p class="body-text">Dear {greeting},</p>

    <p class="body-text">On behalf of INTERXDB, we are pleased to present BiziBid — Barbados&#39; first mobile auction and deals platform — as a highly effective channel for {company_name} to dispose of repossessed vehicles and foreclosed properties quickly, transparently, and at fair market value.</p>

    <p class="body-text">Traditional asset disposal methods — physical auctions, sealed bids, and private negotiations — are slow, costly, and reach a limited audience. BiziBid solves this by putting your assets in front of thousands of registered, verified Barbados-based bidders the moment they are listed. Visit www.bizibid.com to see the platform in action.</p>

    <p class="body-text">Every repossessed vehicle or foreclosed property listed on BiziBid immediately reaches the full BiziBid registered user base. Bidding is live, competitive, and fully transparent — maximising the recovery value for {bank_ref} on every single asset.</p>

    <div class="section-block">
      <h3>Asset Types Suitable for BiziBid</h3>
      <div class="asset-grid">
        <div class="asset-card">
          <h4>Repossessed Vehicles</h4>
          <p>Cars, SUVs, trucks, motorcycles, and commercial vehicles recovered from defaulted loans. Each unit listed separately with photos, year, make, model, mileage, and reserve price. Bidding opens immediately.</p>
        </div>
        <div class="asset-card">
          <h4>Foreclosed Properties</h4>
          <p>Residential and commercial properties in foreclosure. Listed as Deal of the Month for maximum 30-day exposure. Full legal descriptions, photos, and title details provided by your team and displayed to all registered BiziBid users.</p>
        </div>
      </div>
    </div>

{how_it_works_bank()}

    <div class="section-block">
      <h3>Introductory Offer — No Monthly Cost for 60 Days</h3>
{free_offer_html(bank_ref)}
    </div>

{pricing_table_bank()}

    <div class="section-block">
      <h3>Live Platform Demo</h3>
      <p class="body-text">Visit <strong>www.bizibid.com</strong> for the full interactive platform walkthrough and live app demo. We are happy to arrange an in-person demonstration at your offices.</p>
    </div>

    <p class="body-text">{closing_sentence}</p>
    <p class="body-text">We welcome the opportunity to schedule a BiziBid presentation at your offices. Contact us at <a href="mailto:contact@bizibid.com">contact@bizibid.com</a> or visit www.bizibid.com.</p>

{signature_html()}
  </div>

{footer_html()}
</div>
</body>
</html>"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Saved letter: {output_path}')


# ── EMAIL TEMPLATE BUILDER ────────────────────────────────────────────────────
def build_html_email(
        company_name, greeting_hint, pitch_url,
        store_ref, benefits_extra, is_bank,
        output_path):

    eyebrow = f"Exclusive Invitation — {company_name}"
    if is_bank:
        headline = "Fast, Transparent Asset<br>Disposal via BiziBid"
        sub_text = (f"INTERXDB invites {company_name} to list repossessed vehicles and foreclosed "
                    "properties on BiziBid — Barbados&#39; first mobile auction platform — at no cost for 60 days.")
        benefit_items = [
            ("🏦", "Asset-Only Listings", f"Repossessed vehicles and foreclosed properties listed exclusively for {company_name} and other financial institutions."),
            ("📣", "Instant Island-Wide Reach", f"Every asset immediately reaches thousands of registered BiziBid bidders across Barbados."),
            ("🔍", "Transparent Live Bidding", "All bids are live and visible — no closed-door negotiations. Maximum fair market recovery on every asset."),
            ("⚡", "Fast Disposal", "Assets move faster than physical auctions, reducing holding costs and legal exposure."),
            ("🌐", "No Overhead", "INTERXDB manages all technology. You submit assets — we handle the rest."),
        ]
        intro_para = (f"We would like to introduce <strong>BiziBid</strong> — Barbados&#39; first mobile auction platform, "
                      f"operated by INTERXDB — as the most effective channel for <strong>{company_name}</strong> to dispose of "
                      "repossessed vehicles and foreclosed properties at fair market value.")
        pitch_section = ""
        if pitch_url:
            pitch_section = f"""      <div class="pitch-section">
        <h3>Live Platform Demo</h3>
        <p>See the BiziBid platform in action:</p>
        <a class="pitch-btn" href="{pitch_url}" target="_blank">
          <div class="pb-left">
            <div class="pb-dot">▶</div>
            <div><div class="pb-name">{company_name} — BiziBid Demo</div><div class="pb-url">{pitch_url.replace("https://","")}</div></div>
          </div>
          <div class="pb-arrow">→</div>
        </a>
      </div>"""
        else:
            pitch_section = """      <div class="pitch-section">
        <h3>Live Platform Demo</h3>
        <p>Visit <strong>www.bizibid.com</strong> for the full interactive platform walkthrough and live demo.</p>
      </div>"""
        cta_subject = f"BiziBid+Asset+Disposal+Partnership+-+{company_name.replace(' ','+')}";
    else:
        headline = "Your Store. On Every Phone.<br>24 Hours a Day."
        sub_text = (f"INTERXDB invites {company_name} to join BiziBid — Barbados&#39; first dedicated "
                    "mobile auction and deals platform — at no cost for 60 days.")
        benefit_items = [
            ("📱", "BiziBid App-Only Auctions &amp; Deals", f"All activity happens exclusively on the BiziBid mobile app. Customers download, register free, and bid on {store_ref} products."),
            ("🏪", "Registered Businesses Only", "A professional marketplace. No private sellers. Only verified retail stores."),
            ("🔥", "25 Items Per Week — Controlled Scarcity", "Limited weekly supply creates urgency and drives competitive bidding."),
            ("📣", "Your Store Becomes the Buzz", f"Customers talk about {store_ref} BiziBid auctions at home, at work, everywhere."),
            ("🌐", "No Store Hours Needed", "Auctions run around the clock — whether your doors are open or not."),
        ]
        intro_para = (f"We would like to introduce <strong>BiziBid</strong> — Barbados&#39; first dedicated mobile auction and deals platform, "
                      f"operated by INTERXDB — that keeps <strong>{store_ref}</strong> in front of Barbadian customers <strong>24/7</strong>. "
                      "We own and operate all technology. You simply list your products.")
        if pitch_url:
            pitch_section = f"""      <div class="pitch-section">
        <h3>See Your Store&#39;s Demo</h3>
        <p>We built a personalised interactive demo for {company_name}. Click below to see the vision:</p>
        <a class="pitch-btn" href="{pitch_url}" target="_blank">
          <div class="pb-left">
            <div class="pb-dot">▶</div>
            <div><div class="pb-name">{company_name} — Live BiziBid Demo</div><div class="pb-url">{pitch_url.replace("https://","")}</div></div>
          </div>
          <div class="pb-arrow">→</div>
        </a>
      </div>"""
        else:
            pitch_section = f"""      <div class="pitch-section">
        <h3>Live Platform Demo</h3>
        <p>Visit <strong>www.bizibid.com</strong> for the full interactive platform walkthrough and live BiziBid app demo.</p>
      </div>"""
        cta_subject = f"BiziBid+Partnership+-+{company_name.replace(' ','+')}";

    benefits_html = "\n".join(
        f'        <div class="benefit-item"><div class="bi-icon">{icon}</div>'
        f'<div class="bi-text"><strong>{title}</strong> — {body}</div></div>'
        for icon, title, body in benefit_items
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BiziBid — Email Template — {company_name}</title>
  <style>
    * {{ box-sizing:border-box; margin:0; padding:0; }}
    body {{ font-family:'Segoe UI',Roboto,Arial,sans-serif; background:#E8EDF3; color:#2C3E50; }}
    .email-wrapper {{ max-width:640px; margin:32px auto; }}

    .email-header {{ background:#0B1F3A; padding:28px 40px; border-radius:10px 10px 0 0; display:flex; align-items:center; justify-content:space-between; }}
    .eh-brand {{ font-family:Georgia,serif; font-size:26px; font-weight:700; color:#fff; }}
    .eh-brand span {{ color:#C9A84C; }}
    .eh-sub   {{ font-size:11px; color:rgba(255,255,255,0.6); margin-top:3px; }}
    .eh-sub strong {{ color:#C9A84C; }}
    .eh-tag   {{ font-size:10px; color:rgba(255,255,255,0.4); letter-spacing:2px; text-transform:uppercase; margin-top:2px; }}
    .gold-line {{ height:4px; background:linear-gradient(to right,#C9A84C,#e8c870,#C9A84C); }}

    .email-hero {{ background:linear-gradient(135deg,#0B1F3A 0%,#1A4A8A 100%); padding:40px 40px 36px; text-align:center; }}
    .eh-eyebrow  {{ font-size:11px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#C9A84C; margin-bottom:12px; }}
    .eh-headline {{ font-size:26px; font-weight:800; color:#fff; line-height:1.25; margin-bottom:14px; }}
    .eh-sub2     {{ font-size:14px; color:rgba(255,255,255,0.7); line-height:1.7; max-width:480px; margin:0 auto 24px; }}
    .eh-badge    {{ display:inline-block; background:#C9A84C; color:#0B1F3A; font-size:13px; font-weight:800; padding:10px 28px; border-radius:30px; }}

    .email-body {{ background:#fff; padding:40px 40px 32px; }}
    .greeting  {{ font-size:15px; font-weight:600; color:#0B1F3A; margin-bottom:18px; }}
    .body-p    {{ font-size:14px; line-height:1.85; color:#4A5568; margin-bottom:18px; }}
    .body-p strong {{ color:#0B1F3A; }}

    .benefits {{ background:#F7F9FC; border-radius:10px; padding:24px 28px; margin:28px 0; }}
    .benefits h3 {{ font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:2px; color:#1A4A8A; margin-bottom:16px; }}
    .benefit-item {{ display:flex; align-items:flex-start; gap:12px; margin-bottom:13px; }}
    .benefit-item:last-child {{ margin-bottom:0; }}
    .bi-icon {{ font-size:16px; flex-shrink:0; margin-top:1px; }}
    .bi-text  {{ font-size:13px; color:#4A5568; line-height:1.6; }}
    .bi-text strong {{ color:#0B1F3A; }}

    .free-strip {{ background:#0B1F3A; border-radius:10px; padding:22px 28px; margin:24px 0; display:flex; align-items:center; gap:20px; }}
    .fs-badge {{ background:#C9A84C; color:#0B1F3A; font-size:11px; font-weight:800; text-align:center; padding:10px 14px; border-radius:8px; flex-shrink:0; white-space:nowrap; }}
    .fs-badge span {{ display:block; font-size:26px; font-weight:900; line-height:1; }}
    .fs-text h4 {{ font-size:14px; font-weight:700; color:#fff; margin-bottom:5px; }}
    .fs-text p  {{ font-size:12px; color:rgba(255,255,255,0.65); line-height:1.65; }}
    .fs-text strong {{ color:#C9A84C; }}

    .pricing-summary h3 {{ font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:2px; color:#1A4A8A; margin-bottom:14px; }}
    .price-row {{ display:flex; justify-content:space-between; align-items:center; padding:11px 14px; border-radius:6px; margin-bottom:6px; background:#F7F9FC; border:1px solid #E2E8F0; }}
    .price-row:nth-child(odd) {{ background:#fff; }}
    .price-label  {{ font-size:13px; color:#4A5568; }}
    .price-amount {{ font-size:14px; font-weight:800; color:#0B1F3A; }}
    .price-free   {{ font-size:13px; font-weight:800; color:#16A34A; }}

    .pitch-section {{ margin:28px 0; }}
    .pitch-section h3 {{ font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:2px; color:#1A4A8A; margin-bottom:6px; }}
    .pitch-section p  {{ font-size:13px; color:#4A5568; margin-bottom:14px; line-height:1.6; }}
    .pitch-btn {{ display:flex; align-items:center; justify-content:space-between; text-decoration:none; border:1px solid #D8E2EF; border-radius:8px; padding:13px 18px; background:#F7F9FC; }}
    .pb-left  {{ display:flex; align-items:center; gap:12px; }}
    .pb-dot   {{ width:32px; height:32px; border-radius:6px; background:#0B1F3A; display:flex; align-items:center; justify-content:center; font-size:15px; flex-shrink:0; color:#C9A84C; }}
    .pb-name  {{ font-size:13px; font-weight:700; color:#0B1F3A; }}
    .pb-url   {{ font-size:11px; color:#9CA3AF; }}
    .pb-arrow {{ color:#C9A84C; font-size:16px; font-weight:700; }}

    .cta-block {{ text-align:center; margin:32px 0 16px; }}
    .cta-btn   {{ display:inline-block; text-decoration:none; background:#0B1F3A; color:#fff; font-size:14px; font-weight:700; padding:15px 48px; border-radius:40px; }}
    .cta-sub   {{ font-size:12px; color:#9CA3AF; margin-top:10px; text-align:center; }}

    .email-footer {{ background:#0B1F3A; padding:24px 40px; border-radius:0 0 10px 10px; text-align:center; }}
    .ef-brand {{ font-size:16px; font-weight:700; margin-bottom:4px; }}
    .ef-bizi  {{ color:#C9A84C; }}
    .ef-bid   {{ color:#fff; }}
    .ef-by    {{ color:rgba(255,255,255,0.5); font-weight:400; font-size:13px; }}
    .ef-links {{ font-size:11px; color:rgba(255,255,255,0.5); margin-top:6px; }}
    .ef-links a {{ color:#C9A84C; text-decoration:none; }}
    .ef-unsub {{ font-size:10px; color:rgba(255,255,255,0.3); margin-top:10px; }}

    .preview-note {{ background:#FEF3C7; border:1px solid #F59E0B; border-radius:6px; padding:12px 18px; max-width:640px; margin:0 auto 16px; font-size:12px; color:#92400E; }}
  </style>
</head>
<body>
  <div class="preview-note"><strong>TEMPLATE GUIDE:</strong> Replace <em>[Contact Name]</em> before sending. Remove this yellow bar before use.</div>
  <div class="email-wrapper">

    <div class="email-header">
      <div>
        <div class="eh-brand">INTER<span>XDB</span></div>
        <div class="eh-sub">Presenting <strong>BiziBid</strong> — bizibid.com</div>
        <div class="eh-tag">Barbados&#39; First Auction &amp; Deals App</div>
      </div>
      <div style="font-size:11px;color:rgba(255,255,255,0.4);text-align:right;">Barbados<br>www.bizibid.com</div>
    </div>
    <div class="gold-line"></div>

    <div class="email-hero">
      <div class="eh-eyebrow">{eyebrow}</div>
      <div class="eh-headline">{headline}</div>
      <div class="eh-sub2">{sub_text}</div>
      <div class="eh-badge">Auction &amp; Get Buzz</div>
    </div>

    <div class="email-body">
      <p class="greeting">Dear [Contact Name] / {greeting_hint},</p>
      <p class="body-p">{intro_para}</p>

      <div class="benefits">
        <h3>Why Partner with BiziBid</h3>
{benefits_html}
      </div>

      <div class="free-strip">
        <div class="fs-badge"><span>60</span>DAYS<br>FREE</div>
        <div class="fs-text">
          <h4>Zero Cost for Your First 60 Days</h4>
          <p>Full BiziBid platform access with no monthly fee. A <strong>$500.00 deposit</strong> secures {store_ref}&#39;s primary ad placement within the app from launch.</p>
        </div>
      </div>

      <div class="pricing-summary">
        <h3>After 60 Days — Simple Pricing (BBD)</h3>
        <div class="price-row"><span class="price-label">First 60 Days</span><span class="price-free">FREE + $500 deposit</span></div>
        <div class="price-row"><span class="price-label">Base Package — 25 items/week</span><span class="price-amount">$450 / month</span></div>
        <div class="price-row"><span class="price-label">Additional Items — per 10 items above 25</span><span class="price-amount">$150 / month</span></div>
        <div class="price-row"><span class="price-label">Deal of the Week Feature</span><span class="price-amount">$150 / week</span></div>
        <div class="price-row"><span class="price-label">Deal of the Month Feature</span><span class="price-amount">$200 / month</span></div>
      </div>

{pitch_section}

      <div class="cta-block">
        <a class="cta-btn" href="mailto:contact@bizibid.com?subject={cta_subject}">Request a Presentation</a>
        <p class="cta-sub">contact@bizibid.com &nbsp;|&nbsp; Tel 1(246) 241-3771</p>
      </div>
    </div>

    <div class="email-footer">
      <div class="ef-brand"><span class="ef-bizi">Bizi</span><span class="ef-bid">Bid</span> <span class="ef-by">by INTERXDB</span></div>
      <div class="ef-links">
        <a href="mailto:contact@bizibid.com">contact@bizibid.com</a> ·
        Tel 1(246) 241-3771 ·
        <a href="https://www.bizibid.com">www.bizibid.com</a>
      </div>
      <div class="ef-unsub">Confidential — prepared exclusively for {company_name}.</div>
    </div>
  </div>
</body>
</html>"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Saved email:  {output_path}')


# ══════════════════════════════════════════════════════════════════════════════
# GENERATE ALL FILES
# ══════════════════════════════════════════════════════════════════════════════
print('Generating BiziBid HTML marketing letters and email templates...\n')

clients = [
    # (folder, company_name, greeting, pitch_url, pitch_label, store_ref, industry_intro, products, closing)
    (
        'Marketing',
        '[Business Name]',
        'Management Team',
        None, None,
        'your store',
        ('Your retail business has built a loyal customer base in Barbados. '
         'BiziBid gives you a direct mobile channel to keep your customers '
         'engaged, excited, and bidding — 24 hours a day, 7 days a week.'),
        [
            'Electronics — smartphones, laptops, tablets, TVs, smartwatches',
            'Appliances — stoves, microwaves, refrigerators, washing machines',
            'Hardware &amp; Tools — drills, power tools, tool sets, lumber',
            'Furniture &amp; Home — beds, sofas, lamps, mirrors, décor',
            'Food &amp; Beverage — gift baskets, premium beverages, seasonal items',
            'Fashion &amp; Lifestyle — clothing bundles, accessories, gift vouchers',
        ],
        ("We believe BiziBid represents a significant, low-risk opportunity to extend your store's digital reach, "
         "engage a new generation of customers, and position your brand as a leader in Barbados' evolving retail landscape."),
    ),
    (
        'Massy',
        'Massy Stores Barbados',
        'Massy Stores Management Team',
        'https://interxdb.com/WebSites/massy-pitch/',
        'Massy Stores Barbados — Live BiziBid Demo',
        'Massy Stores',
        ("As Barbados' leading supermarket and general retail brand, Massy Stores has unmatched reach across "
         "the island. BiziBid amplifies that reach by placing your products in front of active, engaged bidders every single day."),
        [
            'Electronics &amp; Tech — smartphones, smartwatches, tablets',
            'Home &amp; Living — beds, furniture, mirrors, décor, lamps',
            'Cycling &amp; Outdoors — bicycles, fitness equipment',
            'Food &amp; Beverage — premium gift baskets, rum selections, seasonal bundles',
            'Seasonal &amp; Holiday — Christmas hampers, Easter specials, back-to-school bundles',
        ],
        ("We believe this partnership represents a significant opportunity to extend Massy Stores' digital reach, "
         "engage a new generation of digital-first customers, and strengthen your position as Barbados' leading retail brand on BiziBid."),
    ),
    (
        'Carters',
        'Carter &amp; Co Ltd',
        'Carter &amp; Co Management Team',
        'https://interxdb.com/WebSites/carters-pitch/',
        'Carter &amp; Co Ltd — Live BiziBid Demo',
        "Carter's",
        ("Carter &amp; Co is one of Barbados' most trusted hardware and homeware destinations. "
         "BiziBid connects Carter's with thousands of active bidders looking for tools, lumber, homeware, "
         "and outdoor products at competitive prices."),
        [
            'Power Tools — drills, impact drivers, circular saws, tool sets',
            'Hand Tools — hammers, wrenches, toolboxes, hardware accessories',
            'Outdoor &amp; BBQ — grills, outdoor furniture, garden equipment',
            'Home Improvement — paint, fixtures, fittings, electrical supplies',
            'Premium Beverages — wine selections, spirits (where applicable)',
            'Décor &amp; Gifts — crystal ware, vases, decorative items',
        ],
        ("We believe BiziBid represents a significant opportunity for Carter &amp; Co to extend its digital reach, "
         "engage a new generation of customers, and build on its strong reputation as a trusted Barbados hardware institution."),
    ),
    (
        'HBHARDWARE',
        'ACE H&amp;B Hardware &amp; Lumber Inc.',
        'H&amp;B Hardware Management Team',
        'https://interxdb.com/WebSites/hbhardware-pitch/',
        'ACE H&amp;B Hardware &amp; Lumber Inc. — Live BiziBid Demo',
        'H&amp;B Hardware',
        ('ACE H&amp;B Hardware &amp; Lumber Inc. — "The Helpful Place" — is a trusted name for hardware, tools, '
         'and lumber across Barbados. BiziBid puts H&amp;B\'s products in front of active bidders including '
         'contractors, homeowners, and DIY enthusiasts.'),
        [
            'Power Tools — DeWalt, Makita, and ACE-brand drills, drivers, and sets',
            'Tool Kits &amp; Cases — professional toolcases, multi-tool combos',
            'Hand Tools &amp; Hardware — all categories of professional hardware',
            'Lumber &amp; Building Materials — selected premium items',
            'Home Improvement Supplies — fixtures, fittings, specialty items',
        ],
        ('We believe BiziBid represents a significant opportunity for H&amp;B Hardware to extend its digital reach, '
         'engage a new generation of customers, and reinforce its well-earned reputation as "the helpful place" across Barbados.'),
    ),
    (
        'Courts',
        'Courts Barbados Ltd',
        'Courts Barbados Management Team',
        None, None,
        'Courts Barbados',
        ("Courts Barbados is the island's leading electronics, appliance, and furniture retailer. "
         "BiziBid is the perfect channel for Courts to move high-demand products through exciting live auctions "
         "— generating buzz and urgency around your brand every week."),
        [
            'Smart TVs — 50&quot;, 55&quot;, 65&quot; QLED, OLED, and LED screens',
            'Large Appliances — stoves, refrigerators, washing machines, dishwashers',
            'Small Appliances — microwaves, air fryers, coffee machines',
            'Smartphones &amp; Tablets — Samsung, Apple, and other premium brands',
            'Furniture — bedroom sets, living room suites, dining sets',
            'Laptops &amp; Computing — notebooks, desktops, accessories',
        ],
        ("We believe BiziBid represents a significant opportunity for Courts Barbados to engage a new generation "
         "of digital-first customers, drive weekly excitement around your brand, and move high-demand inventory "
         "through live competitive auctions."),
    ),
    (
        'PromoTech',
        'PromoTech',
        'PromoTech Management Team',
        None, None,
        'PromoTech',
        ("PromoTech is a specialist technology retailer trusted by Barbados consumers for the latest in laptops, "
         "smartphones, and accessories. BiziBid creates weekly excitement around PromoTech's product range "
         "— driving sales through live competitive bidding on the island's premier mobile auction platform."),
        [
            'Laptops — premium ultrabooks, gaming laptops, business notebooks',
            'Smartphones — latest Android and Apple handsets, including bundles',
            'Smartwatches — Apple Watch, Samsung Galaxy Watch, fitness trackers',
            'Tablets &amp; Accessories — iPads, Android tablets, laptop bags, covers',
            'Memory &amp; Storage — SSDs, USB drives, memory cards, external drives',
            'Printers &amp; Peripherals — laser/inkjet printers, scanners, accessories',
        ],
        ("We believe BiziBid represents a significant opportunity for PromoTech to engage Barbados' growing "
         "tech-savvy consumer base, drive weekly demand for your product range, and build PromoTech's brand "
         "as the go-to tech destination on Barbados' premier mobile auction platform."),
    ),
]

# Generate merchant letters + emails
for (folder, company, greeting, pitch_url, pitch_label,
     store_ref, industry_intro, products, closing) in clients:

    letter_path = fr'{BASE}\{folder}\marketing-letter.html'
    email_path  = fr'{BASE}\{folder}\email-template.html'

    build_html_letter(
        company_name=company, greeting=greeting,
        pitch_url=pitch_url, pitch_label=pitch_label,
        store_ref=store_ref, industry_intro=industry_intro,
        product_examples=products, body_para2='',
        closing_sentence=closing,
        output_path=letter_path,
    )
    build_html_email(
        company_name=company, greeting_hint=greeting,
        pitch_url=pitch_url, store_ref=store_ref,
        benefits_extra=None, is_bank=False,
        output_path=email_path,
    )

# First Citizens Bank
build_html_bank_letter(
    company_name='First Citizens Bank Barbados',
    greeting='First Citizens Bank Asset Management Team',
    bank_ref='First Citizens Bank',
    closing_sentence=(
        "We believe BiziBid represents a fast, transparent, and cost-effective solution for "
        "First Citizens Bank to recover maximum value on repossessed vehicles and foreclosed "
        "properties — reaching more qualified buyers, more quickly, than any traditional disposal "
        "method available in Barbados today."
    ),
    output_path=fr'{BASE}\FirstCitizens\marketing-letter.html',
)
build_html_email(
    company_name='First Citizens Bank Barbados',
    greeting_hint='First Citizens Bank Asset Management Team',
    pitch_url=None,
    store_ref='First Citizens Bank',
    benefits_extra=None, is_bank=True,
    output_path=fr'{BASE}\FirstCitizens\email-template.html',
)

print(f'\nAll 14 HTML files generated successfully.')
