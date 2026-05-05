# Massy Stores Barbados — Client Pitch Demo Design Spec
**Date:** 2026-05-05  
**Purpose:** Before/After sales demo to pitch a full website overhaul to Massy Stores Barbados (massystoresbb.com). This is a non-functional visual demo only — no backend, no real data.

---

## Goal

Convince Massy Stores to invest in a full website + mobile app rebuild by showing them:
1. How dated their current site looks
2. How dramatically modern it could become
3. The competitive edge of having an eBay-style live auction platform

---

## Deliverable

A single self-contained HTML file (with embedded CSS and JS) that runs in any browser with no server required. Saved to `C:\AI Software\websites\Massy\demo\index.html`.

---

## Tech Stack

| Concern | Technology |
|---|---|
| Structure | HTML5 |
| Styling | CSS3 (custom properties, flexbox, grid, keyframe animations) |
| 3D products | Three.js (CDN) |
| Scroll/entrance animations | GSAP + ScrollTrigger (CDN) |
| Audio | Web Audio API (no external files) |
| Fonts | Google Fonts — Montserrat (headings), Inter (body) |
| No build step | Everything inline or CDN — opens directly in browser |

---

## Section 1 — Before/After Drag Slider (Opening Screen)

**Layout:** Full-screen split. Left half = Before (current site recreation). Right half = After (redesign).

**Before (left panel):**
- Faithful recreation of massystoresbb.com as seen in the screenshot
- White background, orange top nav, Massy logo, COVID hygiene banner
- Static, flat, dated — the deliberate contrast

**After (right panel):**
- Dark cinematic hero (`#0D0D0D` background) glowing with orange/gold
- 3D product sphere orbiting (Three.js), bold headline, pulsing CTAs
- Smartphone mockup visible with auction animation running

**Divider:**
- Draggable vertical handle in the centre — user drags left/right
- Handle styled as a glowing orange pill with `◀ ▶` arrows
- Label above: `"DRAG TO SEE THE DIFFERENCE"`

**CTA below slider:**
- Button: `"See the Full Vision →"` — collapses Before, expands After to full-screen with cinematic fade transition

---

## Section 2 — After: Cinematic Hero

**Background:** `#0D0D0D` with animated floating particle field (tiny dots in orange/gold/white, drifting slowly)

**3D Product Orbit (Three.js):**
- 7 product icons orbit a central glowing Massy "M" logo in 3D space
- Products: flat-screen TV, sofa, grocery bag, smartphone, blender, camera, gift box
- Slow continuous rotation on Y-axis, each product at a different orbital radius
- Hover on any product — it pulses and enlarges slightly

**Headline (GSAP fade-in, staggered):**
- Line 1: `"The Future of Shopping"` — large, white, Montserrat 700
- Line 2: `"in Barbados."` — same size, Massy orange
- Sub-headline: `"Shop. Bid. Win. — All in one place."` — smaller, grey

**CTAs:**
- `Shop Now` — orange filled button, slight scale on hover
- `Join Live Auction` — outlined button with orange glow pulse animation

**Navigation:**
- Sleek dark top bar: Logo | Shop | Deals | Auction | App | Locations | Contact
- Transparent on load, solid dark on scroll

---

## Section 3 — Auction Wow Factor (Embedded in Hero, Right Side)

This is the centrepiece — occupies at least 25% of the full demo's visual real estate. Positioned on the right side of the hero alongside the headline.

**Smartphone Mockup Frame:**
- CSS-drawn phone frame (rounded rectangle, thin bezel, camera dot)
- Screen inside plays the auction story as a looping auto-animation

**Auction Story Animation Sequence (auto-plays, loops):**

| Step | Duration | What Happens |
|---|---|---|
| 1. Product Listing | 2s | Product image (TV), title, starting bid `$299.00` fades in |
| 2. Login Flash | 1s | Login screen overlay — username/password tap animation |
| 3. Bidders Join | 2s | Counter animates: `12 bidders... 38... 75 BIDDERS LIVE` in red, spinning fast |
| 4. Bid War | 3s | Current bid climbs rapidly: `$310 → $340 → $389 → $412` — fast number roll |
| 5. Outbid Alert | 2s | Red popup slides in: `"You've been outbid! Bid Again to WIN! 🔥"` — pulsing BID NOW button |
| 6. Final Countdown | 3s | `00:00:03 → 00:00:02 → 00:00:01 → 00:00:00` each second punched with audio |
| 7. YOU WON! | 2s | Confetti explosion (canvas), gold text: `"🏆 Congratulations — YOU WON!"` |
| 8. Reset | 1s | Smooth fade back to Step 1 |

**Total loop:** ~16 seconds

---

## Section 4 — Heartbeat Audio (Web Audio API)

No external files. All sound generated via `AudioContext` oscillators and gain nodes.

| Auction Phase | Sound | BPM |
|---|---|---|
| Page load / product listing | Slow deep heartbeat | ~60 BPM |
| Bidders joining | Beat quickens | ~80 BPM |
| Bid war / numbers climbing | Rapid thumping | ~120 BPM |
| Outbid popup | Sharp tension sting + fast beat | ~140 BPM |
| Final countdown 3...2...1 | Peak intensity, each second punched | Max |
| YOU WON! | Triumphant ascending tone + cheer swell | — |
| Loop reset | Fade back to calm | ~60 BPM |

**Mute button:** Fixed bottom-right corner, `🔊 / 🔇` toggle. On by default (autoplay requires user interaction — audio starts on first click/drag).

---

## Section 5 — Deals Strip

Positioned below the hero on scroll.

**Deal of the Week + Deal of the Month:**
- Two dark cards side by side with orange glowing borders
- Each card: product image placeholder, product name, struck-through original price, deal price in large gold text
- Live countdown timer: `Days : Hours : Minutes : Seconds` — ticking in real time using `setInterval`
- `Grab This Deal` button — pulses on hover
- Cards slide in from left/right on scroll (GSAP ScrollTrigger)

**Email Opt-In Banner:**
- Full-width Massy orange strip
- Text: `"Be first. Get exclusive deals, new arrivals & auction alerts."`
- Email input + `Notify Me` button (visual only — no actual submission)
- Micro-copy: `"No spam. Unsubscribe anytime."`

---

## Section 6 — Mobile App Preview

Two phone mockups side by side showing:
- **Phone 1:** App home dashboard — "What's New", "Top Deals", "Live Auctions" tabs with sample cards
- **Phone 2:** Live auction screen — countdown, current bid, bid button, bidder count

Brief copy beside them:
> *"The Massy App puts the store in your pocket. Shop, track deals, and join live auctions from anywhere — instant notifications keep you always in the game."*

App store badge placeholders (App Store / Google Play — visual only).

---

## Section 7 — Closing CTA

Full-width dark section:
- Heading: `"Ready to transform your business?"`
- Sub: `"Let's build the future of Massy Stores together."`
- Button: `"Start the Conversation"` — large, orange, with glow
- Contact details below (placeholder)

---

## Visual Design Tokens

| Token | Value |
|---|---|
| Primary orange | `#F47B20` |
| Gold accent | `#FFD700` |
| Dark background | `#0D0D0D` |
| Card background | `#1A1A1A` |
| White text | `#FFFFFF` |
| Muted text | `#A0A0A0` |
| Danger/outbid red | `#FF3B30` |
| Success/won green | `#34C759` |
| Heading font | Montserrat 700/800 |
| Body font | Inter 400/500 |

---

## File Output

```
C:\AI Software\websites\Massy\demo\
└── index.html   ← single self-contained file
```

All JS, CSS, and CDN links embedded. Opens by double-clicking. No server needed.

---

## Out of Scope (Phase 2 & 3)

- Real backend / database
- Functional auction engine
- Real email capture
- Mobile app build
- CMS / product management

---

## Full Stack Technology — Phase 2 & 3 (Post Client Sign-Off)

> This section outlines the complete technology stack that will power the real Massy platform once the client approves the demo. Included here for technical transparency and stakeholder confidence.

### Frontend (Web)
| Layer | Technology |
|---|---|
| Framework | **Next.js 14** (React, App Router, SSR/SSG) |
| Styling | **Tailwind CSS** + custom design tokens |
| 3D / Animation | **Three.js**, **GSAP**, **Framer Motion** |
| Real-time UI | **Socket.IO client** (live auction bid updates) |
| State management | **Zustand** |
| Auth UI | **NextAuth.js** |

### Mobile App (iOS & Android)
| Layer | Technology |
|---|---|
| Framework | **React Native** (Expo managed workflow) |
| Navigation | **Expo Router** |
| Push Notifications | **Expo Notifications** + **Firebase Cloud Messaging (FCM)** |
| Real-time bidding | **Socket.IO client** |
| Local storage | **AsyncStorage** / **MMKV** |

### Backend (API & Services)
| Layer | Technology |
|---|---|
| Runtime | **Node.js** with **Express** or **Fastify** |
| Real-time auction engine | **Socket.IO server** — live bid broadcasting, room per auction |
| REST API | **RESTful endpoints** for products, users, deals, orders |
| Authentication | **JWT** + **Refresh Tokens**, OAuth2 (Google/Facebook login) |
| Email notifications | **Nodemailer** + **SendGrid** (opt-in deal alerts, outbid alerts) |
| Job scheduling | **Bull** + **Redis** (deal timers, auction expirations, email queues) |

### Database & Storage
| Layer | Technology |
|---|---|
| Primary database | **PostgreSQL** (products, users, bids, orders, auctions) |
| ORM | **Prisma** |
| Cache / sessions | **Redis** |
| Media storage | **AWS S3** or **Cloudflare R2** (product images, uploads) |
| Search | **Meilisearch** (fast product & auction search) |

### Infrastructure & DevOps
| Layer | Technology |
|---|---|
| Hosting (web) | **Vercel** (Next.js) or **AWS EC2** |
| Hosting (API) | **Railway** or **AWS ECS** |
| CI/CD | **GitHub Actions** |
| SSL / CDN | **Cloudflare** |
| Monitoring | **Sentry** (errors) + **Uptime Kuma** (availability) |
| Containerisation | **Docker** + **Docker Compose** |

### CRM & AI Integration
| Layer | Technology |
|---|---|
| CRM | **Customer profiles, purchase history, bid history, segmentation** |
| Targeted email engine | Dynamic deal emails based on user browse/bid behaviour |
| **Local AI Server** *(optional)* | Private, on-premise AI server — automated product descriptions, personalised deal recommendations, customer support chatbot, and CRM behavioural segmentation. No data leaves the client's server. |

> **Note on Local AI:** The local AI server option gives Massy full data sovereignty — customer behaviour, purchase patterns, and auction data never leave their infrastructure while still powering intelligent personalisation and automation. This is a significant competitive differentiator over retailers relying on third-party SaaS AI.

---

---

*Designed by **INTERXDB***  
*Concept, Architecture & Development — Full Stack Web, Mobile & AI Integration*
