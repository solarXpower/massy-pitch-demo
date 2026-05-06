# BiziBid Platform — Design Specification

**Date:** 2026-05-05  
**Status:** Approved for implementation planning  
**Operated by:** INTERXDB (Digital Retail & Auction Platform, Barbados)

---

## 1. What BiziBid Is

BiziBid is a business-to-consumer retail auction and deals platform targeting **medium-to-high income earners and family units in Barbados**.

| Product | Purpose | Who uses it |
|---|---|---|
| **BiziBid App** (iOS & Android) | Live auctions, deals, bidding | Consumers (registered bidders) |
| **BiziBid.com** | Back-office product upload portal | Verified retail store owners only |
| **Admin Panel** (web) | Platform management, billing, approvals | INTERXDB internal team |

**Critical rule:** No public auctions or bidding occur on the website. All consumer interaction is in the mobile app exclusively. BiziBid.com is a store owner back-office.

---

## 2. Domain & Brand

- **Domain:** BiziBid.com (secured)
- **App name:** BiziBid
- **Infrastructure operator:** INTERXDB

### 2.1 Design System

**Palette — Gold / Black / White**

| Colour | Hex | Use |
|---|---|---|
| Gold | `#C9A84C` | Logo, buttons, CTAs, idle button glow, labels |
| White | `#FFFFFF` | App background (default), prices, item names, primary text |
| Black | `#000000` | App background (dark mode), text on light mode |
| Light grey | `#FAFAFA` | Card surfaces in light mode |
| Near-black | `#0A0A0A` | Card surfaces in dark mode |
| Red | `#DC2626` | Outbid alerts, urgent countdown timers — urgency only |

**No rotating colour themes.** The app stays Gold/Black/White at all times. Colour is reserved for semantic meaning.

**Theme modes:**
- **Light mode** (default) — white `#FFFFFF` background, black `#111111` text, gold accents. Active for all users out of the box.
- **Dark mode** (user toggle) — black `#000000` background, white `#FFFFFF` text, gold accents. User switches via Profile → Settings → Dark Mode toggle.
- User preference stored in their profile record (`theme_preference: 'light' | 'dark'`).
- The Gold/Black/White palette, all notification badge colours, button glow system, and CTA button style are **identical in both modes**. Only the background and text colours invert.

**Typography rules:**

| Element | Light mode | Dark mode |
|---|---|---|
| Prices / bid amounts | Black `#111` bold | White `#FFF` bold |
| Item names | Black `#111` | White `#FFF` |
| Store names / secondary | Grey `#9CA3AF` | Grey `#4B5563` |
| Urgent timers | Red `#DC2626` bold | Red `#DC2626` bold |
| Gold labels | Gold `#C9A84C` | Gold `#C9A84C` |
| CTA buttons | Gold background, black text | Gold background, black text |

**Product images:**
- PNG format with transparent backgrounds
- Light mode: transparent PNG on white card surface — products appear natural, no visible background
- Dark mode: transparent PNG on white-transparent surface — products appear to float
- Server-side conversion: PNG → WebP (Sharp.js), transparency preserved
- Three sizes generated: thumbnail (120×120), card (400×400), detail (800×800)
- Max delivered file size: 150KB per image
- Delivered via Cloudflare CDN (Caribbean edge)

---

## 3. Notification & Glow System

The keypad store buttons use an ambient glow system. The glow colour communicates notification state **without requiring the user to read text** — like traffic signals.

### 3.1 Badge Colours (notification dots on logos)

| Badge | Colour | Meaning |
|---|---|---|
| 🔵 Blue circle | `#1D4ED8` | Number of active bids placed on items from this store |
| 🟠 Orange circle | `#EA580C` | Number of other users watching items you are bidding on |
| 🔴 Red circle (flashing) | `#DC2626` | You have been outbid on one or more items at this store |

### 3.2 Button Rim Glow States

The outer rim of each store logo button glows to match its highest-priority notification:

| State | Glow colour | Animation |
|---|---|---|
| No notifications | Gold `#C9A84C` | Slow breathing pulse (2.5s ease-in-out) |
| Bids active (blue badge present) | Blue `#3B82F6` | Steady glow |
| Watching (orange badge present) | Orange `#F97316` | Steady glow |
| Outbid (red badge present) | Red `#EF4444` | Fast flash (0.8s — urgent) |

Priority order when multiple badges present: **Red > Orange > Blue**. The glow colour reflects the highest priority state.

---

## 4. Business Rules

### 4.1 Item Release Engine

The platform's core scheduling logic:

1. Retail store bulk-uploads products to BiziBid.com portal (no limit on uploads)
2. Each product has a store-set starting bid price
3. **Weekly selector** (runs every Monday 00:00 AST): picks up to **25 items** at random from that store's pending pool
4. **Daily releaser** (runs every day at 05:15 AST): schedules 5 items for release at random times between **05:30–15:00 AST**
5. Items accumulate across days: Day 1 releases 5, Day 2 adds 5 more, etc. — up to 25 live simultaneously
6. **Unsold items** return to the pending pool and are mixed with new uploads for the following week's selection
7. **Sold items** are removed from the pool and archived as records (with winner key) in the store owner portal
8. Items are cleared from user devices on the weekly reset (push notification triggers local cache clear)

### 4.2 Auction Rules

- Auction starting bid must be **lower than the shelf/retail price** — the value proposition is always cheaper online
- Products must not be used as pure loss leaders (no below-cost pricing)
- Auction durations: **3 days / 7 days / 14 days / custom** (set by admin, store owner cannot override)
- Real-time bidding via Socket.IO rooms (one room per auction)
- Only registered, verified app users may bid

### 4.3 Deals of the Week / Month

- **Fixed price only** — no bidding permitted on deals
- Purchase method: walk in to store and pay
- Purpose: drive physical foot traffic, keep non-bidding users engaged
- Users can **Like** a deal (like count stored, visible to all)
- Users can **Share** a deal (see Section 6)
- Clearly labelled "Walk-in Only" — BID NOW button is hidden/disabled
- Store sets the fixed BBD price and valid dates
- Weekly deals valid 7 days, monthly deals valid the calendar month

### 4.4 Pricing — After 60-Day Introductory Period (BBD)

| Service | Description | Rate |
|---|---|---|
| Base Listing Package | Up to 25 items listed per week | $450.00 / month |
| Additional Items | Per additional 10 items above the 25-item base | $150.00 / month |
| Deal of the Week | Featured deal for 7 days | $150.00 / week |
| Deal of the Month | Premium featured deal for the full month | $200.00 / month |
| Pinned Store Placement | Top-of-screen keypad position (Tier 1) | Premium — admin-configured |
| Primary Keypad Position | First 6–9 visible grid positions (Tier 2) | Mid-tier — admin-configured |
| Slide-out Position | Overflow/secondary panel positions (Tier 3) | Standard — admin-configured |
| Banner Ads | Rotating ad strip across all user screens | Per-week — admin-configured |

Introductory offer: 60 days free + $500 BBD deposit for primary ad placement.  
Rates fixed for first 12 months for founding partners.

### 4.5 Payment for Auction Winners

**Cash in-store only.** No online payment gateway. The win key serves as the authentication mechanism at the point of collection.

---

## 5. App — Keypad Home Screen

The main screen is the user's permanent home base. Navigation happens via **overlays and slide panels** — the keypad remains visible and accessible at all times.

### 5.1 Screen Layout (top to bottom)

1. **BiziBid wordmark bar** — "Bizi" (white) + "Bid" (gold), Barbados label
2. **Sliding ad banner** — paid store promotions, gold on black
3. **Pinned Store zone** — user's pinned store shown large with all 3 badge types at full size
4. **Keypad grid** — 3-column grid of store logos with glow rims and notification badges
5. **Just Released strip** — latest item released today, price in white, timer in red
6. **Tab bar** — Home | ⚡ My Bids (gold pill button with red outbid count badge) | Profile

### 5.2 Keypad Placement Tiers

| Tier | Location | Cost |
|---|---|---|
| Pinned (Tier 1) | Top zone, large display — one store only | Highest fee |
| Primary (Tier 2) | First 6–9 visible grid cells | Mid fee |
| Slide-out (Tier 3) | Additional stores, swipe-right overflow pages | Lower fee |

The user can **pin any one store** themselves (personal preference, free). This is separate from the paid Tier 1 placement — paid placement gets the Tier 1 zone; user-pinned store gets visual prominence in the standard grid.

### 5.3 Store Logo Tap Behaviour

Tapping a store logo opens that store's auctions and deals in the **top 25% of the screen** as an overlay panel — the keypad remains visible and interactive below. No full-screen navigation.

### 5.4 Active Bids Slide Panel

Tapping the **"⚡ My Bids"** tab button slides a panel in from the right edge, overlaying the keypad (keypad dims to ~30% opacity, remains visible).

Panel contents:
- **Header:** "My Active Bids" + count summary (e.g. "3 active · 1 outbid")
- **Pinned bid** (if any) shown at top — red border + flashing OUTBID badge if outbid, green if leading
- **Divider:** "Also Watching"
- **Remaining active bids** sorted by urgency (soonest ending first)
- Each card shows: item image, item name, store name, current bid (white), time remaining (red if <2h), LEADING (green) / OUTBID (red) status badge, user's own last bid amount
- **OUTBID cards** show a pre-filled "BID $[next valid amount]" gold button — one tap to counter-bid without leaving the panel
- **LEADING cards** show a "Watching" muted button

Tapping outside the panel or tapping the ✕ closes it — user returns to full keypad instantly.

**Push notification deep-link behaviour:** All outbid/ending-soon push notifications deep-link to the main screen with the slide panel **auto-opened** at the relevant bid card. User lands ready to act.

---

## 6. Share System

Both **auction items** and **deals** are shareable. Each generates a unique public URL on BiziBid.com.

### 6.1 URL Format

| Type | URL pattern |
|---|---|
| Auction | `bizibid.com/auctions/[slug]` |
| Deal | `bizibid.com/deals/[slug]` |

### 6.2 Share Mechanic

- React Native `Share` API opens the device's **native share sheet**
- User sees all installed apps (WhatsApp, Instagram, iMessage, Facebook, Copy Link, etc.)
- No custom social integrations needed — the native sheet handles everything

### 6.3 Public Landing Page

The shared URL opens a **publicly accessible page** on BiziBid.com (no login required) showing:
- Product image (from Cloudflare R2/CDN)
- Item name and store name
- **Auction page:** current bid (white, large), countdown timer, "LIVE AUCTION" indicator, app download buttons
- **Deal page:** fixed price, valid dates, walk-in notice, app download buttons
- Open Graph meta tags auto-generate the preview card when pasted into WhatsApp/Instagram/Facebook

### 6.4 Open Graph Tags (server-generated per item)

```
og:title     → "[Item name] — [price] BBD | BiziBid"
og:image     → Cloudflare R2 URL of product image (card size, 400×400)
og:description → "[Store name] · [Auction: X hours left / Deal: Walk in to buy]"
og:url       → bizibid.com/auctions/[slug] or bizibid.com/deals/[slug]
```

### 6.5 Viral Growth Loop

Auction shares drive FOMO: contacts see the live bid + countdown, download BiziBid to join the auction. Deal shares drive curiosity: contacts see a good price, download BiziBid to find more deals. Every share is a free advertisement for both BiziBid and the retail store.

### 6.6 Like System

- `deal_likes` and `auction_likes` tables: `item_id` + `user_id` + `liked_at`
- One like per user per item (deduplicated)
- Like count visible in-app and on the public share page
- Social proof signal for the store

---

## 7. User Registration

Required fields for consumer registration:
- First name
- Last name
- Date of birth
- Username
- Email address
- Mobile number
- Selfie (in-app camera capture)
- Terms & Conditions acceptance (checkbox, must be checked to proceed)

**Selfie storage:** Stored in a private Cloudflare R2 bucket (not publicly accessible). Shared with the retail store owner upon auction win to assist cashier identification alongside the win key.

---

## 8. Win Key System

When an auction closes:
1. Server generates an **8-character alphanumeric code** (e.g. `HBD-X4K9`)
2. Code stored encrypted in the database
3. **Push notification** sent to winner: "You won! Show your collection code at the cashier." (Code displayed in-app after authenticated fetch — not transmitted in the push notification text)
4. Store owner sees winner name + code in their BiziBid.com portal
5. Winner shows phone to cashier → cashier matches code → item released
6. Prevents impersonation — the code is the only proof of identity needed

---

## 9. Warning & Ban System

| Event | Action |
|---|---|
| Winner fails to collect confirmed auction | 1 warning issued by admin |
| Warning #2 | Final warning email sent |
| Warning #3 | Account auto-banned — "Account suspended" on login |
| Admin unban | Available via admin panel |

---

## 10. Technology Stack

### 10.1 Backend API

| Component | Technology | Reason |
|---|---|---|
| Runtime | Node.js + TypeScript | Typed, reliable, large ecosystem |
| HTTP Framework | Fastify | 2× faster throughput than Express — critical for high-frequency bid events |
| Real-time | Socket.IO | Auction rooms, real-time bid broadcast, outbid events, countdown sync |
| ORM | Prisma | Type-safe DB queries, migration management |
| Database | PostgreSQL | Relational data, ACID transactions (no bid lost), audit trail |
| Cache | Redis | Auction state cache (sub-ms reads), Socket.IO adapter, rate limiting, session store |
| Job queue | BullMQ | All scheduled jobs (item release, auction close, invoice, theme rotation) |
| Image processing | Sharp.js | PNG → WebP, resize to 3 sizes, preserve transparency |
| PDF generation | pdfkit | Monthly invoices |
| Email | SendGrid | Transactional email, invoice delivery |
| Push notifications | Firebase Cloud Messaging (FCM) | iOS + Android, outbid alerts, win confirmations, new items |
| File storage | Cloudflare R2 | Images, invoice PDFs — S3-compatible, Caribbean CDN edge |
| Containerisation | Docker Compose | Local dev + production, consistent environment |

### 10.2 Consumer Mobile App

| Component | Technology |
|---|---|
| Framework | React Native + Expo |
| Platforms | iOS & Android (single codebase) |
| Animations | Reanimated 3 (keypad glow, panel slide, bid flash) |
| Image loading | react-native-fast-image (aggressive caching) |
| Local storage | MMKV (fast key-value, stores current week's auction cache) |
| Real-time | Socket.IO client (persistent connection, exponential backoff on reconnect) |
| Push | Expo + FCM token registration |
| Share | React Native `Share` API (native OS share sheet) |

### 10.3 Store Owner Web Portal & Admin Panel

| Component | Technology |
|---|---|
| Framework | React + Vite |
| Styling | Tailwind CSS |
| Data fetching | React Query |
| Auth | JWT (role: `store_owner` or `super_admin`) |
| Deployment | Cloudflare Pages (free tier) |

---

## 11. Database Schema (Core Tables)

```
users              id, first_name, last_name, date_of_birth, username, email, mobile,
                   selfie_r2_key, role, warning_count, is_banned, fcm_token,
                   theme_preference ('light' | 'dark', default 'light'), created_at

businesses         id, user_id, business_name, contact_email, approved, created_at

keypad_placements  id, business_id, tier (1/2/3), position_index, valid_from, valid_to, active

products           id, business_id, name, description, images_r2[], starting_bid,
                   status (draft/pending_pool/scheduled/live/sold/archived)

auctions           id, product_id, duration_type, start_time, end_time,
                   current_bid, leading_bidder_id, status, win_key_hash

bids               id, auction_id, user_id, amount, placed_at

auction_likes      id, auction_id, user_id, liked_at
deal_likes         id, deal_id, user_id, liked_at

deals              id, business_id, name, description, image_r2_key, fixed_price,
                   type (week/month), valid_from, valid_to, like_count

warnings           id, user_id, auction_id, reason, issued_at

rental_invoices    id, business_id, period_start, period_end, line_items[],
                   total_amount, status (pending/sent/paid), pdf_r2_key, sent_at

app_themes         id, name, is_active, activated_at
                   (reserved for future — primary palette is fixed Gold/Black/White)
```

---

## 12. BullMQ Scheduled Jobs

| Job | Schedule (AST) | Action |
|---|---|---|
| `weekly-item-selector` | Mon 00:00 | Picks 25 random items from each store's pending pool, creates auction schedule |
| `daily-item-releaser` | Every day 05:15 | Schedules 5 sub-jobs at random times between 05:30–15:00 for that store |
| `auction-ender` | At each auction's `end_time` | Closes auction, generates win key, notifies winner + store owner |
| `weekly-content-refresh` | Sun 23:30 | Push notification to all devices: "New items dropping tomorrow" — triggers local cache clear |
| `monthly-invoice-gen` | 1st of month 06:00 | Calculates fees, generates PDF, uploads to R2, emails via SendGrid |
| `notification-count-sync` | Every 30 seconds | Aggregates bid/watch/outbid counts per store → writes to Redis → app reads via Socket.IO |

---

## 13. Hosting — Recommended (Railway.app)

Launch configuration (~$20 BBD/month):

| Service | Provider | Cost |
|---|---|---|
| Backend API | Railway.app service | ~$5–10/month |
| PostgreSQL | Railway managed DB | ~$5/month |
| Redis | Railway managed Redis | ~$3/month |
| Store portal + Admin panel | Cloudflare Pages | Free |
| Images + PDFs | Cloudflare R2 | ~$0 egress + $0.015/GB storage |
| Push notifications | Firebase FCM | Free |
| Email (≤100/day) | SendGrid | Free tier |

**Migration path:** Railway → DigitalOcean ($30/month, more control) when traction is proven. AWS/Azure when scaling to broader Caribbean.

---

## 14. Performance Strategy

| Concern | Solution |
|---|---|
| Bid latency | All live auction state in Redis, not DB — sub-millisecond reads per bid |
| Image load speed | WebP delivery via Cloudflare CDN Caribbean edge, react-native-fast-image caching |
| App startup | Current week's auctions cached in MMKV — loads instantly before API responds |
| Bid spam | Redis-based per-user rate limiting on bid endpoint |
| Socket scale | Redis adapter for Socket.IO — supports horizontal API scaling |
| Off-screen images | FlatList lazy rendering — only load images scrolled into view |

---

## 15. Security

| Concern | Measure |
|---|---|
| Win key exposure | Never sent in push notification text — only returned via authenticated API fetch in-app |
| Win key storage | Stored as bcrypt hash in DB, plaintext only returned to authenticated winner + store owner |
| Image uploads | Server-side MIME type validation, max input size enforced, Sharp.js reprocesses file |
| User data | Date of birth, selfie, mobile number — stored securely, accessible only to authenticated user and admin |
| Selfie storage | Private R2 bucket — not accessible via public URL, requires signed URL |
| Bid validation | Server-side only: bid must exceed current highest, auction must be active, user must not be banned |
| Rate limiting | Redis per-user per-auction bid rate limit prevents spam bidding |

---

## 16. Build Phases

| Phase | Deliverable | Duration |
|---|---|---|
| 1 | Backend API — Fastify, PostgreSQL, Prisma schema, Redis, Auth (JWT + roles), Socket.IO, BullMQ item release engine, Docker Compose | 4–6 weeks |
| 2 | Store Owner Web Portal — React + Vite, bulk upload, product management, auction results, win key view, invoice download | 2–3 weeks |
| 3 | Admin Panel — store approvals, user management, keypad placement management, billing dashboard, analytics | 2–3 weeks |
| 4 | BiziBid Mobile App — keypad home screen, glow system, active bids slide panel, live auction bidding, win key display, selfie capture, share system, FCM push | 6–8 weeks |
| 5 | Billing System — BullMQ monthly cron, fee tier calculation, pdfkit invoice generation, SendGrid delivery | 1–2 weeks |

**Total estimate:** 15–22 weeks  
**Recommended build order:** Phases 1–3 tested end-to-end before Phase 4 begins. Phase 5 runs in parallel with late Phase 4.

---

## 17. Verification Checkpoints

| Phase | How to verify |
|---|---|
| Phase 1 | Postman collection hits all routes. JWT roles enforced (store owner cannot call admin routes). Socket.IO bid broadcast confirmed on two clients. BullMQ item release fires at scheduled time on test clock. |
| Phase 2 | Store owner logs in, bulk-uploads 30 items, sees them enter pending_pool. Confirms only 25 selected weekly. Views auction history and downloads a test invoice PDF. |
| Phase 3 | Admin approves a new business account. Assigns keypad placement. Issues a warning to a test user. Views billing dashboard. |
| Phase 4 | Two devices registered as bidders. One bids on an item — second device sees bid update in real-time via Socket.IO. Outbid notification fires on first device. Win key displayed after auction closes. Share link opens correct public page on BiziBid.com. Slide panel opens and pre-fills counter-bid amount. |
| Phase 5 | Test invoice generated and emailed. PDF correctly shows line items, totals, store name, period. R2 upload confirmed. |
