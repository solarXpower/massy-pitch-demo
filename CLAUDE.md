# INTERXDB — BiziBid Platform & Retail Pitch Demo Workspace

## Platform Name
**BiziBid** — Barbados' first retail auction and deals mobile platform, operated by INTERXDB.
- Domain secured: **BiziBid.com**
- Mobile app: **BiziBid** (iOS + Android)
- Back-office portal: **BiziBid.com** (store owners)
- Platform code: `C:\AI Software\AuctionPlatform\` → GitHub: `solarXpower/bizibid-platform`

---

## Service Overview

INTERXDB is a Barbados-based digital platform company that offers retail stores a fully managed mobile auction and deals service under the **BiziBid** brand. INTERXDB owns and operates all technology — the platform, mobile app, hosting, and infrastructure. Retail stores do not manage any technology; they list products and INTERXDB handles the rest.

The service is designed to keep retail stores as the buzz word in every customer's household, 24 hours a day, 7 days a week — whether store doors are open or not.

---

## Platform Rules & Model

- **App-only bidding:** All auctions, Deal of the Week, and Deal of the Month activity runs exclusively through the BiziBid mobile app. The public website is not used for bidding.
- **Registered businesses only:** Only verified retail businesses may list products. No individual or private sellers permitted.
- **Free customer registration:** End-users (customers) register and use the app at no cost.
- **25-item weekly limit per store:** Controlled supply creates scarcity, urgency, and competitive bidding. 5 items released daily at random times (05:30–15:00 AST).
- **Store promotion obligation:** Participating stores must promote the BiziBid app in-store and via their own social media and marketing channels.
- **User conduct:** Customers who fail to honour confirmed auction wins receive warnings. Three warnings = automatic ban.

---

## Pricing Model (BBD)

| Period | Cost |
|--------|------|
| First 60 days (introductory) | FREE |
| $500.00 deposit | Required — secures primary ad placement in app |
| Base package after 60 days (25 items/week) | $450.00 / month |
| Additional items (per 10 above base) | $150.00 / month |
| Deal of the Week feature | $150.00 / week |
| Deal of the Month feature | $200.00 / month |

---

## Client Companies & Pitch Demos

### 1. Massy Stores Barbados
- **Industry:** Supermarket / General Retail
- **Website:** [www.massystoresbarbados.com](https://www.massystoresbarbados.com)
- **Pitch Demo:** https://interxdb.com/WebSites/massy-pitch/
- **Demo Folder:** `Massy/demo/index.html`
- **Brand Colors:** Blue (#003087), Red, White
- **Marketing Materials:** `Massy/marketing-letter.html`, `Massy/email-template.html`

### 2. Carter & Co Ltd
- **Industry:** Hardware / Lumber / Homeware
- **Website:** [www.cartersonline.bb](https://www.cartersonline.bb)
- **Pitch Demo:** https://interxdb.com/WebSites/carters-pitch/
- **Demo Folder:** `Carters/demo/index.html`
- **Brand Colors:** Dark Green (#124A1F), Red (#ee2a24), Gold (#f5c842)
- **Marketing Materials:** `Carters/marketing-letter.html`, `Carters/email-template.html`

### 3. ACE H&B Hardware & Lumber Inc.
- **Industry:** Hardware / Lumber / Home Goods (ACE Affiliate)
- **Website:** [www.myhandb.bb](https://www.myhandb.bb)
- **Pitch Demo:** https://interxdb.com/WebSites/hbhardware-pitch/
- **Demo Folder:** `HBHARDWARE/DEMO/index.html`
- **Brand Colors:** Red (#CC2222), Green (#2E7D32), White
- **Tagline:** "The helpful place"
- **Marketing Materials:** `HBHARDWARE/marketing-letter.html`, `HBHARDWARE/email-template.html`

---

## Completed Work

### Pitch Demo Pages
- [x] Massy Stores — full before/after drag-slider demo, CSS 3D product orbit, live auction phone animation, deals section, app preview, Bid & Win banner, crowd cheer audio
- [x] Carter & Co — full before/after demo, Carter's brand colors, BBQ grill deal card (local image `BBqgrillPNG.png`), Girl Cheering image right of phone
- [x] H&B Hardware — full before/after demo, H&B red/green brand, ACE affiliation, manPNG hero image, Girl Cheering image right of phone

### Marketing Materials
- [x] Shared marketing letter (`Marketing/marketing-letter.html`) — all 3 client pitch links
- [x] Shared email template (`Marketing/email-template.html`) — all 3 client pitch links
- [x] Massy-specific letter and email — Massy pitch link only
- [x] Carter's-specific letter and email — Carter's pitch link only
- [x] H&B Hardware-specific letter and email — H&B pitch link only
- [x] Each company's documents are saved in their own folder — competitors cannot see each other's pitch links
- [x] Word `.docx` marketing letters generated via `Marketing/generate_letters.py` (python-docx)

### BiziBid Partner Presentation
- [x] Platform design spec — `docs/specs/2026-05-05-bizibid-platform-design.md` (17 sections, full architecture)
- [x] Partner PowerPoint — `Marketing/BiziBid-Partner-Presentation.pptx` (14 slides, marketing-only, no tech details)
- [x] Print/PDF version — `Marketing/BiziBid-Partner-Presentation-PRINT.html` (open in Chrome → Print → Save as PDF)
- [x] Generator script — `Marketing/generate_presentation.py` (python-pptx)

### Infrastructure
- [x] `robots.txt` — Disallows `/WebSites/` from search engine indexing to keep pitch demos private
- [x] Bluehost/cPanel deployment — Massy demo uploaded to `interxdb.com/WebSites/massy-pitch/`
- [x] GitHub repository — all files committed and pushed to `solarXpower/massy-pitch-demo`

---

## Folder Structure

```
websites/
├── Massy/
│   ├── demo/              Massy pitch demo (index.html + assets)
│   ├── marketing-letter.html
│   ├── email-template.html
│   └── NOTES.md
├── Carters/
│   ├── demo/              Carter's pitch demo (index.html + assets)
│   ├── marketing-letter.html
│   └── email-template.html
├── HBHARDWARE/
│   ├── DEMO/              H&B Hardware pitch demo (index.html + assets)
│   ├── marketing-letter.html
│   └── email-template.html
├── Marketing/
│   ├── marketing-letter.html          (combined — all 3 pitch links)
│   ├── email-template.html            (combined — all 3 pitch links)
│   ├── generate_letters.py            (generates .docx letters via python-docx)
│   ├── generate_presentation.py       (generates PPTX + HTML via python-pptx)
│   ├── BiziBid-Partner-Presentation.pptx
│   └── BiziBid-Partner-Presentation-PRINT.html
├── docs/
│   └── specs/
│       └── 2026-05-05-bizibid-platform-design.md
├── robots.txt
└── CLAUDE.md              (this file)
```

---

## Demo Page Architecture

Each demo is a single self-contained `index.html` file featuring:
- **Drag-to-compare split screen** — Before (current site recreation) vs After (INTERXDB redesign)
- **"See the Future" button** — expands after panel to full screen with GSAP entrance animation
- **CSS 3D product orbit** — 7 product images rotating around a central phone
- **Live auction state machine** — 8-state cycle simulating a real bidding session (listing → login → bidders → bid war → outbid → countdown → win → reset)
- **Deals section** — Deal of the Week and Deal of the Month with live countdown timers
- **App preview** — Two phone mockups showing the home feed and live auction screen
- **Bid & Win banner** — with Web Audio API crowd cheer sound on scroll
- **Closing CTA** — INTERXDB contact details and tech stack

All external assets (fonts, GSAP) load from CDN. Local images must be uploaded alongside `index.html` to the server.

---

## Deployment Notes

- Pitch demos are hosted at `interxdb.com/WebSites/[client-name]-pitch/`
- Upload `index.html` plus any local image files to the same folder on Bluehost via cPanel
- The `robots.txt` at the root of `websites/` must be placed at the root of `interxdb.com` to block indexing
- Each demo is confidential — do not share one client's link with another client
