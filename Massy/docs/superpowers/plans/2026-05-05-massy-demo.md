# Massy Stores Before/After Demo — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single self-contained `index.html` before/after demo that a client can open in any browser to experience the Massy Stores redesign pitch — draggable split-screen comparison, 3D animated hero, live auction sequence, heartbeat audio, and deals sections.

**Architecture:** One HTML file with all CSS in a `<style>` block and all JavaScript in a `<script>` block at the end of `<body>`. CDN links for Three.js, GSAP, and Google Fonts are the only external dependencies. No server, no build step — double-click to open.

**Tech Stack:** HTML5, CSS3, Three.js r128 (CDN), GSAP 3.12.2 + ScrollTrigger (CDN), Web Audio API, Google Fonts (Montserrat + Inter)

---

## File Map

```
C:\AI Software\websites\Massy\demo\
└── index.html   ← entire demo lives here
```

All tasks modify `index.html`. The file is built incrementally — each task adds HTML, CSS, or JS to the appropriate section.

---

## Task 1: Scaffold — HTML shell, CDNs, CSS tokens, global reset

**Files:**
- Create: `C:\AI Software\websites\Massy\demo\index.html`

- [ ] **Step 1: Create index.html with full scaffold**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Massy Stores — The Future of Shopping in Barbados</title>

  <!--
  ============================================================
  MASSY STORES BARBADOS — CLIENT PITCH DEMO
  Designed by INTERXDB
  Concept, Architecture & Development — Full Stack Web, Mobile & AI Integration

  PHASE 2 & 3 FULL STACK (post client sign-off):
  Frontend:  Next.js 14 (React, App Router) · Tailwind CSS · Three.js · GSAP · Framer Motion
  Mobile:    React Native (Expo) · Expo Router · Firebase Cloud Messaging · Socket.IO client
  Backend:   Node.js · Express/Fastify · Socket.IO server (live auction engine) · JWT Auth
             SendGrid (email) · Bull + Redis (job queues)
  Database:  PostgreSQL · Prisma ORM · Redis (cache) · AWS S3/Cloudflare R2 (media)
             Meilisearch (product search)
  DevOps:    Docker · GitHub Actions · Cloudflare CDN · Vercel/AWS · Sentry · Uptime Kuma
  CRM/AI:    Customer profiles · bid/purchase history · targeted email engine
             Local AI Server [optional]: private on-premise AI for product descriptions,
             personalised recommendations, support chatbot, CRM segmentation —
             zero customer data leaves client infrastructure.
  ============================================================
  -->

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>

  <style>
    /* ── Design Tokens ── */
    :root {
      --orange:  #F47B20;
      --gold:    #FFD700;
      --dark:    #0D0D0D;
      --card-bg: #1A1A1A;
      --white:   #FFFFFF;
      --muted:   #A0A0A0;
      --red:     #FF3B30;
      --green:   #34C759;
      --font-head: 'Montserrat', sans-serif;
      --font-body: 'Inter', sans-serif;
    }

    /* ── Global Reset ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body { font-family: var(--font-body); background: var(--dark); color: var(--white); overflow-x: hidden; }
    button { cursor: pointer; border: none; outline: none; font-family: var(--font-body); }
    a { text-decoration: none; color: inherit; }
  </style>
</head>
<body>

  <!-- JS goes here at end of body -->
  <script>
    // placeholder — JS added per task
  </script>
</body>
</html>
```

- [ ] **Step 2: Open in browser and verify**

Open `C:\AI Software\websites\Massy\demo\index.html` in Chrome.
Expected: blank dark page, no console errors, fonts load (check Network tab).

- [ ] **Step 3: Commit**

```bash
git -C "C:\AI Software\websites" init
git -C "C:\AI Software\websites" add .
git -C "C:\AI Software\websites" commit -m "feat: scaffold massy demo — html shell, CDNs, design tokens"
```

---

## Task 2: Before Panel — Current Site Recreation

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html` (add HTML + CSS)

- [ ] **Step 1: Add Before panel HTML inside `<body>` before the `<script>` tag**

```html
<!-- ══════════════════════════════════════
     SPLIT SCREEN WRAPPER
══════════════════════════════════════ -->
<div class="split-wrapper" id="splitWrapper">

  <!-- ── BEFORE PANEL (current site recreation) ── -->
  <div class="before-panel" id="beforePanel">
    <!-- Social bar -->
    <div class="bb-social">
      <span>f</span><span>&#9679;</span>
    </div>
    <!-- Header -->
    <header class="bb-header">
      <div class="bb-logo">
        <div class="bb-logo-icon">M</div>
        <div class="bb-logo-text"><span class="bb-massy">MASSY</span><br><span class="bb-stores">STORES</span></div>
      </div>
      <nav class="bb-nav">
        <a href="#">ABOUT</a><a href="#">SAVINGS</a><a href="#">SHOP NOW</a>
        <a href="#">FOOD &amp; DRINK</a><a href="#">VILLAGE DELI</a>
        <a href="#">LOCATIONS</a><a href="#">CONTACT US</a>
      </nav>
    </header>
    <!-- Colour bar -->
    <div class="bb-colorbar">
      <div style="background:#1B3A6B;flex:2"></div>
      <div style="background:#F4C430;flex:1"></div>
      <div style="background:#F47B20;flex:2"></div>
      <div style="background:#00AEEF;flex:3"></div>
    </div>
    <!-- COVID banner -->
    <div class="bb-covid-banner">
      <div class="bb-covid-left">
        <div class="bb-covid-logo">M</div>
        <div class="bb-covid-msg">
          <strong>Follow Proper Hygiene Practices</strong><br>
          to Reduce the Risk of Infection
        </div>
      </div>
      <div class="bb-covid-right">
        <div class="bb-who-label">Guidelines from the:</div>
        <div class="bb-who-logo">WHO</div>
        <div class="bb-who-name">World Health<br>Organization</div>
      </div>
    </div>
    <!-- Hygiene icons -->
    <div class="bb-icons">
      <span>🚿</span><span>🤲</span><span>🤧</span><span>🚫</span>
      <span>💻</span><span>😷</span><span>🧴</span>
    </div>
    <!-- Welcome text -->
    <div class="bb-welcome">
      <h2>WELCOME TO MASSY STORES</h2>
      <p>In July 2014 Massy Stores was launched in Barbados. In the 2 years hence, Massy Stores has seen many changes, including the opening of our Skymall location in 2015. Massy Stores (Barbados) Ltd now offers 5 supermarkets, the Warrens SuperCentre, 2 Home locations, 8 Pharmacies and 2 Express locations.</p>
    </div>
    <!-- Bottom cards -->
    <div class="bb-cards">
      <div class="bb-card">
        <div class="bb-card-img">🏪</div>
        <div class="bb-card-body">
          <h4>ABOUT MASSY STORES</h4>
          <p>In July 2014 Massy Stores was launched in Barbados.</p>
          <a href="#" class="bb-read">READ MORE</a>
        </div>
      </div>
      <div class="bb-card">
        <div class="bb-card-img">💳</div>
        <div class="bb-card-body">
          <h4>SERVICES</h4>
          <p>Making it easier for you to access the services you use the most.</p>
          <a href="#" class="bb-read">READ MORE</a>
        </div>
      </div>
      <div class="bb-card">
        <div class="bb-card-img">📍</div>
        <div class="bb-card-body">
          <h4>MASSY LOCATIONS</h4>
          <p>Find a store near you.</p>
          <a href="#" class="bb-read">READ MORE</a>
        </div>
      </div>
    </div>
    <!-- Before label -->
    <div class="panel-label before-label">BEFORE</div>
  </div>

  <!-- DIVIDER and AFTER panel added in later tasks -->
</div>

<!-- Drag instruction label -->
<div class="drag-label" id="dragLabel">◀&nbsp;&nbsp;DRAG TO SEE THE DIFFERENCE&nbsp;&nbsp;▶</div>

<!-- See Full Vision button -->
<button class="see-vision-btn" id="seeVisionBtn">See the Full Vision →</button>
```

- [ ] **Step 2: Add Before panel CSS inside `<style>`**

```css
/* ── Split wrapper ── */
.split-wrapper {
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  overflow: hidden;
}

/* ── Before panel ── */
.before-panel {
  width: 50%;
  height: 100%;
  background: #fff;
  overflow-y: auto;
  position: relative;
  flex-shrink: 0;
  transition: width 0.8s cubic-bezier(0.77,0,0.175,1);
}

/* Social bar */
.bb-social {
  background: #fff;
  border-bottom: 1px solid #eee;
  padding: 4px 12px;
  display: flex;
  gap: 8px;
  font-size: 12px;
  justify-content: flex-end;
}

/* Header */
.bb-header {
  background: #fff;
  padding: 10px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #eee;
}
.bb-logo { display: flex; align-items: center; gap: 6px; }
.bb-logo-icon {
  background: var(--orange);
  color: #fff;
  font-weight: 900;
  font-size: 20px;
  width: 36px; height: 36px;
  display: flex; align-items: center; justify-content: center;
  border-radius: 4px;
}
.bb-massy { font-weight: 800; font-size: 14px; color: var(--orange); }
.bb-stores { font-size: 10px; color: #333; letter-spacing: 2px; }
.bb-nav { display: flex; gap: 8px; flex-wrap: wrap; }
.bb-nav a { font-size: 9px; color: #333; font-weight: 600; letter-spacing: 0.5px; white-space: nowrap; }

/* Colour bar */
.bb-colorbar { display: flex; height: 6px; }

/* COVID banner */
.bb-covid-banner {
  background: var(--orange);
  padding: 12px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}
.bb-covid-left { display: flex; align-items: center; gap: 10px; }
.bb-covid-logo {
  background: rgba(255,255,255,0.2);
  color: #fff;
  font-weight: 900;
  font-size: 16px;
  width: 30px; height: 30px;
  display: flex; align-items: center; justify-content: center;
  border-radius: 3px;
}
.bb-covid-msg { color: #fff; font-size: 11px; line-height: 1.5; }
.bb-covid-right { text-align: center; color: #fff; font-size: 9px; }
.bb-who-logo { font-size: 20px; font-weight: 900; }

/* Hygiene icons */
.bb-icons {
  padding: 20px;
  display: flex;
  justify-content: space-around;
  font-size: 24px;
  border-bottom: 1px solid #eee;
}

/* Welcome text */
.bb-welcome { padding: 20px 16px; text-align: center; border-bottom: 1px solid #eee; }
.bb-welcome h2 { font-size: 14px; color: #1B3A6B; margin-bottom: 10px; font-family: var(--font-head); }
.bb-welcome p { font-size: 10px; color: #666; line-height: 1.6; }

/* Bottom cards */
.bb-cards { display: flex; gap: 8px; padding: 12px; }
.bb-card { flex: 1; border: 1px solid #eee; overflow: hidden; border-radius: 2px; }
.bb-card-img { font-size: 36px; padding: 12px; background: #f9f9f9; text-align: center; }
.bb-card-body { padding: 8px; }
.bb-card-body h4 { font-size: 9px; font-weight: 700; margin-bottom: 4px; color: #333; }
.bb-card-body p { font-size: 8px; color: #666; line-height: 1.4; }
.bb-read { font-size: 9px; color: var(--orange); font-weight: 700; display: block; margin-top: 6px; }

/* Panel labels */
.panel-label {
  position: absolute; bottom: 16px; left: 50%;
  transform: translateX(-50%);
  font-family: var(--font-head);
  font-size: 11px; font-weight: 800;
  letter-spacing: 4px;
  padding: 6px 16px;
  border-radius: 20px;
}
.before-label { background: #ddd; color: #333; }

/* Drag label */
.drag-label {
  position: fixed; top: 12px; left: 50%;
  transform: translateX(-50%);
  background: rgba(0,0,0,0.7);
  color: #fff;
  font-family: var(--font-head);
  font-size: 11px; font-weight: 700;
  letter-spacing: 2px;
  padding: 8px 20px;
  border-radius: 20px;
  z-index: 100;
  pointer-events: none;
  border: 1px solid var(--orange);
}

/* See Full Vision button */
.see-vision-btn {
  position: fixed; bottom: 32px; left: 50%;
  transform: translateX(-50%);
  background: var(--orange);
  color: #fff;
  font-family: var(--font-head);
  font-size: 14px; font-weight: 700;
  padding: 14px 36px;
  border-radius: 40px;
  z-index: 100;
  box-shadow: 0 0 30px rgba(244,123,32,0.5);
  letter-spacing: 1px;
  transition: transform 0.2s, box-shadow 0.2s;
}
.see-vision-btn:hover {
  transform: translateX(-50%) scale(1.05);
  box-shadow: 0 0 50px rgba(244,123,32,0.8);
}
```

- [ ] **Step 3: Verify in browser**

Open `index.html`. Expected: left half shows recreated Massy site — white background, orange nav, COVID banner, hygiene icons, welcome text, three cards. Right half is blank dark.

---

## Task 3: After Panel Shell + Dark Navigation

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html`

- [ ] **Step 1: Add After panel HTML inside `.split-wrapper`, after `.before-panel`**

```html
  <!-- ── DIVIDER ── -->
  <div class="divider" id="divider">
    <div class="divider-handle">◀ ▶</div>
  </div>

  <!-- ── AFTER PANEL ── -->
  <div class="after-panel" id="afterPanel">

    <!-- Navigation -->
    <nav class="after-nav" id="afterNav">
      <div class="nav-logo">
        <span class="nav-logo-m">M</span>
        <div><span class="nav-massy">MASSY</span><br><span class="nav-stores">STORES</span></div>
      </div>
      <ul class="nav-links">
        <li><a href="#">Shop</a></li>
        <li><a href="#">Deals</a></li>
        <li><a href="#auction-section">Auction</a></li>
        <li><a href="#app-section">App</a></li>
        <li><a href="#">Locations</a></li>
        <li><a href="#closing-section">Contact</a></li>
      </ul>
    </nav>

    <!-- Hero section — content added in Task 5 & 7 -->
    <section class="hero-section" id="heroSection">
      <!-- Particle canvas -->
      <canvas id="particleCanvas"></canvas>
      <!-- Three.js mount -->
      <div id="threeMount"></div>
      <!-- Hero text + CTAs -->
      <div class="hero-content" id="heroContent">
        <!-- added Task 5 -->
      </div>
      <!-- Auction phone -->
      <div class="phone-wrap" id="phoneWrap">
        <!-- added Task 8 -->
      </div>
    </section>

    <!-- Deals section — Task 12 -->
    <section class="deals-section" id="dealsSection"></section>

    <!-- Email opt-in — Task 13 -->
    <section class="optin-section" id="optinSection"></section>

    <!-- App preview — Task 14 -->
    <section class="app-section" id="appSection"></section>

    <!-- Closing CTA — Task 15 -->
    <section class="closing-section" id="closingSection"></section>

    <!-- Footer -->
    <footer class="site-footer">
      <p>Designed by <strong>INTERXDB</strong> — Full Stack Web, Mobile &amp; AI Integration</p>
    </footer>

    <!-- After label -->
    <div class="panel-label after-label">AFTER</div>
  </div>
```

- [ ] **Step 2: Add After panel + nav CSS inside `<style>`**

```css
/* ── After panel ── */
.after-panel {
  width: 50%;
  height: 100%;
  background: var(--dark);
  overflow-y: auto;
  position: relative;
  flex-shrink: 0;
  transition: width 0.8s cubic-bezier(0.77,0,0.175,1);
}
.after-label { background: var(--orange); color: #fff; }

/* ── Divider ── */
.divider {
  width: 4px;
  height: 100%;
  background: var(--orange);
  position: relative;
  z-index: 50;
  cursor: col-resize;
  flex-shrink: 0;
  box-shadow: 0 0 20px rgba(244,123,32,0.8);
}
.divider-handle {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: var(--orange);
  color: #fff;
  padding: 10px 8px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  white-space: nowrap;
  box-shadow: 0 0 20px rgba(244,123,32,0.9);
  user-select: none;
}

/* ── After Nav ── */
.after-nav {
  position: sticky;
  top: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 32px;
  background: transparent;
  transition: background 0.3s;
}
.after-nav.scrolled { background: rgba(13,13,13,0.95); backdrop-filter: blur(10px); }
.nav-logo { display: flex; align-items: center; gap: 8px; }
.nav-logo-m {
  background: var(--orange);
  color: #fff;
  font-weight: 900;
  font-size: 18px;
  width: 36px; height: 36px;
  display: flex; align-items: center; justify-content: center;
  border-radius: 6px;
}
.nav-massy { font-family: var(--font-head); font-weight: 800; font-size: 13px; color: var(--orange); }
.nav-stores { font-size: 8px; letter-spacing: 3px; color: var(--muted); }
.nav-links { list-style: none; display: flex; gap: 24px; }
.nav-links a {
  font-size: 12px;
  font-weight: 600;
  color: var(--muted);
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: color 0.2s;
}
.nav-links a:hover { color: var(--orange); }

/* ── Hero section ── */
.hero-section {
  min-height: calc(100vh - 64px);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 80px 40px 60px;
  overflow: hidden;
  gap: 20px;
}
#particleCanvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
#threeMount {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

/* ── Footer ── */
.site-footer {
  text-align: center;
  padding: 24px;
  color: var(--muted);
  font-size: 11px;
  border-top: 1px solid #222;
}
.site-footer strong { color: var(--orange); }
```

- [ ] **Step 3: Verify in browser**

Refresh `index.html`. Expected: dark right panel with sticky dark nav (logo + links), hero section space visible. Divider is an orange vertical line with handle at centre.

---

## Task 4: Drag Slider Mechanism + "See Full Vision" Transition

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html` (JS section)

- [ ] **Step 1: Replace the JS placeholder with drag slider + full-vision code**

```javascript
// ── Drag Slider ──
const splitWrapper  = document.getElementById('splitWrapper');
const beforePanel   = document.getElementById('beforePanel');
const afterPanel    = document.getElementById('afterPanel');
const divider       = document.getElementById('divider');
const seeVisionBtn  = document.getElementById('seeVisionBtn');
const afterNav      = document.getElementById('afterNav');

let isDragging = false;
let fullVisionMode = false;

divider.addEventListener('mousedown', startDrag);
divider.addEventListener('touchstart', startDrag, { passive: true });

function startDrag(e) {
  isDragging = true;
  // init audio on first interaction
  if (!audioCtx) initAudio();
  document.body.style.cursor = 'col-resize';
  document.body.style.userSelect = 'none';
}

document.addEventListener('mouseup', () => { isDragging = false; document.body.style.cursor = ''; document.body.style.userSelect = ''; });
document.addEventListener('touchend', () => { isDragging = false; });

document.addEventListener('mousemove', onDrag);
document.addEventListener('touchmove', (e) => onDrag(e.touches[0]), { passive: true });

function onDrag(e) {
  if (!isDragging || fullVisionMode) return;
  const rect = splitWrapper.getBoundingClientRect();
  let pct = ((e.clientX - rect.left) / rect.width) * 100;
  pct = Math.min(Math.max(pct, 5), 95);
  beforePanel.style.width = pct + '%';
  afterPanel.style.width  = (100 - pct) + '%';
}

// ── See Full Vision transition ──
seeVisionBtn.addEventListener('click', () => {
  if (!audioCtx) initAudio();
  fullVisionMode = true;
  beforePanel.style.width = '0%';
  divider.style.display    = 'none';
  afterPanel.style.width   = '100%';
  document.getElementById('dragLabel').style.opacity  = '0';
  seeVisionBtn.style.opacity = '0';
  seeVisionBtn.style.pointerEvents = 'none';
  // Trigger GSAP hero entrance after panel expands
  setTimeout(triggerHeroEntrance, 900);
});

// ── Nav scroll effect ──
afterPanel.addEventListener('scroll', () => {
  if (afterPanel.scrollTop > 50) afterNav.classList.add('scrolled');
  else afterNav.classList.remove('scrolled');
});

// Placeholder — functions defined in later tasks
function initAudio() {}
function triggerHeroEntrance() {}
```

- [ ] **Step 2: Verify in browser**

Drag the divider left and right — Before/After panels resize smoothly. Click "See the Full Vision →" — Before panel collapses, After expands to full width. No console errors.

---

## Task 5: Hero Content — Headline + CTAs (GSAP)

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html`

- [ ] **Step 1: Add hero content HTML inside `.hero-content` div**

```html
<div class="hero-content" id="heroContent">
  <div class="hero-eyebrow">The Future is Here</div>
  <h1 class="hero-h1">
    <span class="h1-line1">The Future of</span>
    <span class="h1-line2">Shopping.</span>
  </h1>
  <p class="hero-sub">Shop. Bid. Win. — All in one place.</p>
  <div class="hero-ctas">
    <button class="btn-primary">Shop Now</button>
    <button class="btn-outline">Join Live Auction</button>
  </div>
  <div class="hero-stats">
    <div class="stat"><span class="stat-n">75+</span><span class="stat-l">Live Bidders</span></div>
    <div class="stat-sep"></div>
    <div class="stat"><span class="stat-n">200+</span><span class="stat-l">Weekly Deals</span></div>
    <div class="stat-sep"></div>
    <div class="stat"><span class="stat-n">18</span><span class="stat-l">Store Locations</span></div>
  </div>
</div>
```

- [ ] **Step 2: Add hero content CSS inside `<style>`**

```css
.hero-content {
  position: relative;
  z-index: 10;
  flex: 1;
  max-width: 50%;
}
.hero-eyebrow {
  font-family: var(--font-head);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 4px;
  text-transform: uppercase;
  color: var(--orange);
  margin-bottom: 16px;
  opacity: 0;
}
.hero-h1 {
  font-family: var(--font-head);
  font-weight: 900;
  line-height: 1.05;
  margin-bottom: 20px;
}
.h1-line1 {
  display: block;
  font-size: clamp(28px, 3.5vw, 52px);
  color: var(--white);
  opacity: 0;
  transform: translateY(30px);
}
.h1-line2 {
  display: block;
  font-size: clamp(32px, 4vw, 60px);
  color: var(--orange);
  opacity: 0;
  transform: translateY(30px);
}
.hero-sub {
  font-size: clamp(13px, 1.2vw, 16px);
  color: var(--muted);
  margin-bottom: 32px;
  opacity: 0;
}
.hero-ctas { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 40px; opacity: 0; }

.btn-primary {
  background: var(--orange);
  color: #fff;
  font-family: var(--font-head);
  font-weight: 700;
  font-size: 13px;
  padding: 14px 28px;
  border-radius: 40px;
  letter-spacing: 1px;
  transition: transform 0.2s, box-shadow 0.2s;
}
.btn-primary:hover { transform: scale(1.06); box-shadow: 0 0 24px rgba(244,123,32,0.6); }

.btn-outline {
  background: transparent;
  color: var(--orange);
  font-family: var(--font-head);
  font-weight: 700;
  font-size: 13px;
  padding: 13px 28px;
  border-radius: 40px;
  border: 2px solid var(--orange);
  letter-spacing: 1px;
  animation: outlinePulse 2s infinite;
}
@keyframes outlinePulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(244,123,32,0.4); }
  50%       { box-shadow: 0 0 0 10px rgba(244,123,32,0); }
}

/* Stats */
.hero-stats { display: flex; align-items: center; gap: 20px; opacity: 0; }
.stat { text-align: center; }
.stat-n { display: block; font-family: var(--font-head); font-weight: 800; font-size: 22px; color: var(--gold); }
.stat-l { display: block; font-size: 9px; color: var(--muted); letter-spacing: 1px; text-transform: uppercase; }
.stat-sep { width: 1px; height: 36px; background: #333; }
```

- [ ] **Step 3: Update `triggerHeroEntrance()` function in JS**

Replace the placeholder `function triggerHeroEntrance() {}` with:

```javascript
function triggerHeroEntrance() {
  gsap.registerPlugin(ScrollTrigger);
  const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
  tl.to('.hero-eyebrow', { opacity: 1, duration: 0.5 })
    .to('.h1-line1', { opacity: 1, y: 0, duration: 0.6 }, '-=0.2')
    .to('.h1-line2', { opacity: 1, y: 0, duration: 0.6 }, '-=0.3')
    .to('.hero-sub',  { opacity: 1, duration: 0.5 }, '-=0.2')
    .to('.hero-ctas', { opacity: 1, duration: 0.5 }, '-=0.2')
    .to('.hero-stats',{ opacity: 1, duration: 0.5 }, '-=0.2');
  // also start particle canvas
  startParticles();
  // start Three.js
  initThreeJS();
  // start auction loop
  startAuctionLoop();
}
```

- [ ] **Step 4: Verify**

Click "See the Full Vision →". After the panel expands, the hero text should animate in staggered. Stats row appears last. No console errors.

---

## Task 6: Particle Background (Canvas)

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html` (JS)

- [ ] **Step 1: Add `startParticles()` function in the JS section**

```javascript
// ── Particle Background ──
function startParticles() {
  const canvas = document.getElementById('particleCanvas');
  const ctx    = canvas.getContext('2d');
  const hero   = document.getElementById('heroSection');

  function resize() {
    canvas.width  = hero.offsetWidth;
    canvas.height = hero.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  const COLORS = ['rgba(244,123,32,0.6)', 'rgba(255,215,0,0.4)', 'rgba(255,255,255,0.2)'];
  const dots = Array.from({ length: 80 }, () => ({
    x:  Math.random() * canvas.width,
    y:  Math.random() * canvas.height,
    r:  Math.random() * 2 + 0.5,
    vx: (Math.random() - 0.5) * 0.4,
    vy: (Math.random() - 0.5) * 0.4,
    color: COLORS[Math.floor(Math.random() * COLORS.length)],
  }));

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    dots.forEach(d => {
      d.x += d.vx;
      d.y += d.vy;
      if (d.x < 0) d.x = canvas.width;
      if (d.x > canvas.width)  d.x = 0;
      if (d.y < 0) d.y = canvas.height;
      if (d.y > canvas.height) d.y = 0;
      ctx.beginPath();
      ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
      ctx.fillStyle = d.color;
      ctx.fill();
    });
    requestAnimationFrame(draw);
  }
  draw();
}
```

- [ ] **Step 2: Verify**

After clicking "See the Full Vision →", tiny orange/gold/white particles should drift slowly across the hero background. No console errors.

---

## Task 7: Three.js 3D Product Orbit

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html` (JS)

- [ ] **Step 1: Add `initThreeJS()` in the JS section**

```javascript
// ── Three.js 3D Product Orbit ──
function initThreeJS() {
  const mount = document.getElementById('threeMount');
  const hero  = document.getElementById('heroSection');

  const W = hero.offsetWidth;
  const H = hero.offsetHeight;

  // Scene
  const scene    = new THREE.Scene();
  const camera   = new THREE.PerspectiveCamera(60, W / H, 0.1, 1000);
  camera.position.set(0, 0, 5);

  const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
  renderer.setSize(W, H);
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.domElement.style.position = 'absolute';
  renderer.domElement.style.inset    = '0';
  renderer.domElement.style.pointerEvents = 'none';
  mount.appendChild(renderer.domElement);

  // Central glowing M sphere
  const coreGeo  = new THREE.SphereGeometry(0.18, 32, 32);
  const coreMat  = new THREE.MeshStandardMaterial({ color: 0xF47B20, emissive: 0xF47B20, emissiveIntensity: 1 });
  const core     = new THREE.Mesh(coreGeo, coreMat);
  scene.add(core);

  // Ambient + point lights
  scene.add(new THREE.AmbientLight(0xffffff, 0.3));
  const pLight = new THREE.PointLight(0xF47B20, 2, 10);
  pLight.position.set(0, 0, 3);
  scene.add(pLight);

  // Product emoji sprites
  const PRODUCTS = ['📺', '🛋️', '🛒', '📱', '🍹', '📷', '🎁'];
  const RADII    = [1.2, 1.5, 1.0, 1.8, 1.3, 1.6, 1.1];
  const SPEEDS   = [0.004, 0.003, 0.005, 0.0035, 0.0045, 0.003, 0.0055];
  const sprites  = [];

  PRODUCTS.forEach((emoji, i) => {
    const cvs = document.createElement('canvas');
    cvs.width = cvs.height = 128;
    const c = cvs.getContext('2d');
    c.font = '80px serif';
    c.textAlign = 'center';
    c.textBaseline = 'middle';
    c.fillText(emoji, 64, 64);

    const tex = new THREE.CanvasTexture(cvs);
    const mat = new THREE.SpriteMaterial({ map: tex, transparent: true });
    const spr = new THREE.Sprite(mat);
    spr.scale.set(0.55, 0.55, 0.55);
    // offset per-product on Y axis for 3D depth
    spr.userData = { radius: RADII[i], speed: SPEEDS[i], angle: (i / PRODUCTS.length) * Math.PI * 2, yOff: (Math.random() - 0.5) * 0.6 };
    scene.add(spr);
    sprites.push(spr);
  });

  // Animate
  let groupAngle = 0;
  function animate() {
    requestAnimationFrame(animate);
    groupAngle += 0.003;
    sprites.forEach(spr => {
      spr.userData.angle += spr.userData.speed;
      const a = spr.userData.angle + groupAngle * 0.2;
      spr.position.set(
        Math.cos(a) * spr.userData.radius,
        spr.userData.yOff + Math.sin(groupAngle + spr.userData.radius) * 0.2,
        Math.sin(a) * spr.userData.radius * 0.4
      );
      // scale pulse
      const s = 0.55 + Math.sin(a * 2) * 0.05;
      spr.scale.set(s, s, s);
    });
    core.rotation.y += 0.01;
    renderer.render(scene, camera);
  }
  animate();

  // Resize handler
  window.addEventListener('resize', () => {
    const nW = hero.offsetWidth;
    const nH = hero.offsetHeight;
    camera.aspect = nW / nH;
    camera.updateProjectionMatrix();
    renderer.setSize(nW, nH);
  });
}
```

- [ ] **Step 2: Verify**

After clicking "See the Full Vision →", 7 product emoji sprites should orbit the glowing orange core in 3D. Orbit is continuous and smooth. No console errors.

---

## Task 8: Auction Smartphone Mockup — HTML & CSS

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html`

- [ ] **Step 1: Add phone mockup HTML inside `.phone-wrap` div**

```html
<div class="phone-wrap" id="phoneWrap">
  <div class="phone-frame">
    <div class="phone-notch"></div>
    <div class="phone-screen" id="phoneScreen">

      <!-- State 1: Product Listing -->
      <div class="auction-state" id="state-listing">
        <div class="auction-header">🔴 LIVE AUCTION</div>
        <div class="auction-product-img">📺</div>
        <div class="auction-product-name">Samsung 65" QLED 4K TV</div>
        <div class="auction-starting">Starting Bid</div>
        <div class="auction-price" id="startingBid">$299.00</div>
        <div class="auction-timer-row">⏱ Ends in: <span class="auction-time">00:08:42</span></div>
      </div>

      <!-- State 2: Login -->
      <div class="auction-state hidden" id="state-login">
        <div class="auction-header">🔐 LOGIN TO BID</div>
        <div class="login-field"><span>📧</span> onsolarnow@massy.com</div>
        <div class="login-field"><span>🔑</span> ••••••••</div>
        <button class="login-btn">Login &amp; Bid</button>
      </div>

      <!-- State 3: Bidders Joining -->
      <div class="auction-state hidden" id="state-bidders">
        <div class="auction-header">🔴 LIVE AUCTION</div>
        <div class="bidder-count-label">BIDDERS LIVE</div>
        <div class="bidder-count" id="bidderCount">12</div>
        <div class="bidder-sub">and climbing...</div>
        <div class="bidder-bar"></div>
        <div class="bidder-names">👤 James · 👤 Keisha · 👤 Marco · 👤 Tara...</div>
      </div>

      <!-- State 4: Bid War -->
      <div class="auction-state hidden" id="state-bidwar">
        <div class="auction-header">⚡ BID WAR!</div>
        <div class="auction-product-name" style="font-size:11px">Samsung 65" QLED 4K TV</div>
        <div class="bidwar-label">Current Bid</div>
        <div class="bidwar-price" id="bidWarPrice">$310</div>
        <div class="bidwar-bids">75 bids · 23 bidders</div>
        <button class="bidnow-btn">BID NOW</button>
      </div>

      <!-- State 5: Outbid Alert -->
      <div class="auction-state hidden" id="state-outbid">
        <div class="outbid-popup">
          <div class="outbid-icon">😱</div>
          <div class="outbid-title">You've Been Outbid!</div>
          <div class="outbid-msg">Someone just topped your bid.<br>Don't let them win!</div>
          <button class="bidagain-btn">🔥 BID AGAIN TO WIN!</button>
        </div>
      </div>

      <!-- State 6: Final Countdown -->
      <div class="auction-state hidden" id="state-countdown">
        <div class="auction-header" style="color:var(--red)">⏰ FINAL SECONDS!</div>
        <div class="countdown-price">$412.00</div>
        <div class="countdown-display" id="countdownDisplay">00:00:03</div>
        <div class="countdown-bidders">75 bidders watching...</div>
      </div>

      <!-- State 7: You Won! -->
      <div class="auction-state hidden" id="state-won">
        <div class="won-content">
          <div class="won-trophy">🏆</div>
          <div class="won-title">YOU WON!</div>
          <div class="won-item">Samsung 65" QLED 4K TV</div>
          <div class="won-price">Final Bid: <span>$412.00</span></div>
          <div class="won-congrats">Congratulations!</div>
        </div>
        <canvas id="confettiCanvas" style="position:absolute;inset:0;pointer-events:none"></canvas>
      </div>

    </div>
  </div>
  <div class="phone-label">MASSY AUCTION APP</div>
  <!-- Mute button lives next to phone -->
  <button class="mute-btn" id="muteBtn">🔊</button>
</div>
```

- [ ] **Step 2: Add phone CSS inside `<style>`**

```css
/* ── Phone wrap ── */
.phone-wrap {
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

/* ── Phone frame ── */
.phone-frame {
  width: 200px;
  height: 400px;
  background: #111;
  border-radius: 36px;
  border: 3px solid #333;
  box-shadow: 0 0 60px rgba(244,123,32,0.3), inset 0 0 10px rgba(0,0,0,0.8);
  position: relative;
  overflow: hidden;
}
.phone-notch {
  width: 60px; height: 12px;
  background: #111;
  border-radius: 0 0 10px 10px;
  margin: 0 auto;
  position: relative; z-index: 5;
}
.phone-screen {
  position: absolute;
  inset: 0;
  border-radius: 34px;
  overflow: hidden;
  background: #0a0a0a;
}

/* ── Auction states ── */
.auction-state {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px 14px 14px;
  gap: 6px;
  text-align: center;
  animation: fadeIn 0.4s ease;
}
.auction-state.hidden { display: none; }
@keyframes fadeIn { from { opacity:0; transform: scale(0.96); } to { opacity:1; transform: scale(1); } }

.auction-header {
  font-family: var(--font-head);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 2px;
  color: var(--orange);
  margin-bottom: 4px;
}
.auction-product-img { font-size: 48px; }
.auction-product-name { font-size: 10px; font-weight: 700; color: var(--white); line-height: 1.3; }
.auction-starting { font-size: 9px; color: var(--muted); }
.auction-price { font-family: var(--font-head); font-size: 26px; font-weight: 800; color: var(--gold); }
.auction-timer-row { font-size: 9px; color: var(--muted); }
.auction-time { color: var(--orange); font-weight: 700; }

/* Login state */
.login-field {
  background: #1a1a1a; border: 1px solid #333; border-radius: 8px;
  padding: 8px 10px; font-size: 9px; color: var(--muted); width: 100%; text-align: left;
}
.login-btn {
  background: var(--orange); color: #fff; border-radius: 20px;
  padding: 8px 20px; font-weight: 700; font-size: 10px; width: 100%; margin-top: 4px;
}

/* Bidders state */
.bidder-count-label { font-size: 9px; letter-spacing: 3px; color: var(--muted); text-transform: uppercase; }
.bidder-count { font-family: var(--font-head); font-size: 52px; font-weight: 900; color: var(--red); line-height: 1; }
.bidder-sub { font-size: 10px; color: var(--muted); }
.bidder-bar { width: 100%; height: 4px; background: #222; border-radius: 2px; overflow: hidden; }
.bidder-bar::after { content:''; display: block; height: 100%; width: 80%; background: linear-gradient(90deg, var(--orange), var(--red)); animation: barGrow 2s ease-in-out; }
@keyframes barGrow { from { width: 20%; } to { width: 80%; } }
.bidder-names { font-size: 8px; color: var(--muted); line-height: 1.4; }

/* Bid war state */
.bidwar-label { font-size: 9px; letter-spacing: 2px; color: var(--muted); text-transform: uppercase; }
.bidwar-price { font-family: var(--font-head); font-size: 38px; font-weight: 900; color: var(--gold); animation: priceFlash 0.3s ease infinite alternate; }
@keyframes priceFlash { from { color: var(--gold); } to { color: var(--orange); } }
.bidwar-bids { font-size: 9px; color: var(--muted); }
.bidnow-btn {
  background: linear-gradient(135deg, var(--orange), #ff5500);
  color: #fff; border-radius: 20px;
  padding: 8px 24px; font-weight: 800; font-size: 11px;
  animation: outlinePulse 1s infinite;
}

/* Outbid state */
.outbid-popup { background: #1a1a1a; border: 2px solid var(--red); border-radius: 16px; padding: 16px; width: 100%; }
.outbid-icon { font-size: 32px; }
.outbid-title { font-family: var(--font-head); font-size: 14px; font-weight: 800; color: var(--red); }
.outbid-msg { font-size: 9px; color: var(--muted); line-height: 1.5; }
.bidagain-btn {
  background: var(--red); color: #fff; border-radius: 20px;
  padding: 8px 16px; font-weight: 800; font-size: 10px;
  width: 100%; margin-top: 8px;
  animation: outlinePulse 0.8s infinite;
}

/* Countdown state */
.countdown-price { font-family: var(--font-head); font-size: 22px; font-weight: 800; color: var(--gold); }
.countdown-display { font-family: var(--font-head); font-size: 36px; font-weight: 900; color: var(--red); letter-spacing: 4px; }
.countdown-bidders { font-size: 9px; color: var(--muted); }

/* Won state */
.won-content { display: flex; flex-direction: column; align-items: center; gap: 6px; }
.won-trophy { font-size: 48px; animation: trophyBounce 0.5s ease infinite alternate; }
@keyframes trophyBounce { from { transform: scale(1); } to { transform: scale(1.15); } }
.won-title { font-family: var(--font-head); font-size: 26px; font-weight: 900; color: var(--gold); }
.won-item { font-size: 9px; color: var(--muted); }
.won-price { font-size: 11px; color: var(--white); }
.won-price span { color: var(--green); font-weight: 700; }
.won-congrats { font-family: var(--font-head); font-size: 12px; font-weight: 800; color: var(--green); }

/* Phone label */
.phone-label { font-family: var(--font-head); font-size: 9px; font-weight: 800; letter-spacing: 3px; color: var(--muted); text-transform: uppercase; }

/* Mute button */
.mute-btn {
  background: rgba(255,255,255,0.08);
  border: 1px solid #333;
  color: var(--white);
  border-radius: 20px;
  padding: 6px 14px;
  font-size: 13px;
  transition: background 0.2s;
}
.mute-btn:hover { background: rgba(244,123,32,0.2); }
```

- [ ] **Step 3: Verify**

Reload. After "See the Full Vision →", the phone mockup appears on the right of the hero — a dark phone frame with "State 1: Product Listing" visible inside. No other states visible.

---

## Task 9: Auction Animation State Machine (JS)

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html` (JS)

- [ ] **Step 1: Add auction state machine + confetti in the JS section**

```javascript
// ── Auction State Machine ──
const AUCTION_STATES = [
  { id: 'listing',   duration: 2200 },
  { id: 'login',     duration: 1500 },
  { id: 'bidders',   duration: 2200 },
  { id: 'bidwar',    duration: 3000 },
  { id: 'outbid',    duration: 2000 },
  { id: 'countdown', duration: 3200 },
  { id: 'won',       duration: 2500 },
  { id: 'reset',     duration: 800  },
];

// BPM per state — matches heartbeat audio phases
const STATE_BPM = { listing: 60, login: 65, bidders: 80, bidwar: 120, outbid: 140, countdown: 160, won: 80, reset: 60 };

let auctionTimer = null;

function showState(id) {
  document.querySelectorAll('.auction-state').forEach(el => el.classList.add('hidden'));
  const el = document.getElementById('state-' + id);
  if (el) { el.classList.remove('hidden'); }
  if (typeof setHeartbeatBPM === 'function') setHeartbeatBPM(STATE_BPM[id] || 60);
}

function startAuctionLoop() {
  let idx = 0;
  showState(AUCTION_STATES[0].id);
  animateBidders();

  function next() {
    idx = (idx + 1) % AUCTION_STATES.length;
    const state = AUCTION_STATES[idx];
    showState(state.id);
    if (state.id === 'bidders') animateBidders();
    if (state.id === 'bidwar')  animateBidWar();
    if (state.id === 'countdown') animateCountdown();
    if (state.id === 'won')     launchConfetti();
    auctionTimer = setTimeout(next, state.duration);
  }
  auctionTimer = setTimeout(next, AUCTION_STATES[0].duration);
}

// Bidder count animation: 12 → 75
function animateBidders() {
  const el = document.getElementById('bidderCount');
  if (!el) return;
  let count = 12;
  const target = 75;
  const step = () => {
    count = Math.min(count + Math.ceil(Math.random() * 6), target);
    el.textContent = count;
    if (count < target) setTimeout(step, 80);
  };
  step();
}

// Bid price animation: $310 → $412
function animateBidWar() {
  const el = document.getElementById('bidWarPrice');
  if (!el) return;
  const prices = [310, 322, 335, 341, 358, 367, 380, 389, 398, 404, 412];
  let i = 0;
  const step = () => {
    if (i < prices.length) {
      el.textContent = '$' + prices[i];
      i++;
      setTimeout(step, 260);
    }
  };
  step();
}

// Countdown: 00:00:03 → 00:00:00
function animateCountdown() {
  const el = document.getElementById('countdownDisplay');
  if (!el) return;
  const ticks = ['00:00:03', '00:00:02', '00:00:01', '00:00:00'];
  let i = 0;
  const step = () => {
    if (i < ticks.length) {
      el.textContent = ticks[i];
      i++;
      if (i < ticks.length) setTimeout(step, 900);
    }
  };
  step();
}

// ── Confetti ──
function launchConfetti() {
  const canvas = document.getElementById('confettiCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  canvas.width  = canvas.offsetWidth  || 200;
  canvas.height = canvas.offsetHeight || 400;
  const COLORS = ['#F47B20','#FFD700','#FFFFFF','#34C759','#FF3B30'];
  const bits = Array.from({ length: 120 }, () => ({
    x:  Math.random() * canvas.width,
    y: -10,
    vx: (Math.random() - 0.5) * 4,
    vy: Math.random() * 3 + 1.5,
    w:  Math.random() * 8 + 3,
    h:  Math.random() * 4 + 2,
    rot: Math.random() * Math.PI * 2,
    rs: (Math.random() - 0.5) * 0.15,
    color: COLORS[Math.floor(Math.random() * COLORS.length)],
  }));
  let frame = 0;
  const draw = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    bits.forEach(b => {
      b.x += b.vx; b.y += b.vy; b.vy += 0.08; b.rot += b.rs;
      ctx.save();
      ctx.translate(b.x, b.y);
      ctx.rotate(b.rot);
      ctx.fillStyle = b.color;
      ctx.fillRect(-b.w/2, -b.h/2, b.w, b.h);
      ctx.restore();
    });
    frame++;
    if (frame < 100) requestAnimationFrame(draw);
    else ctx.clearRect(0, 0, canvas.width, canvas.height);
  };
  draw();
}
```

- [ ] **Step 2: Verify**

Click "See Full Vision →". The phone screen should cycle through all 8 states automatically: listing → login → bidders (counter spins 12→75) → bid war (price climbs $310→$412) → outbid alert → countdown (3→0) → YOU WON + confetti → loop resets.

---

## Task 10: Web Audio API — Heartbeat System

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html` (JS)

- [ ] **Step 1: Replace `function initAudio() {}` placeholder with full audio engine**

```javascript
// ── Web Audio API Heartbeat ──
let audioCtx      = null;
let heartTimer    = null;
let isMuted       = false;
let currentBPM    = 60;

function initAudio() {
  if (audioCtx) return;
  audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  startHeartbeat(60);
  document.getElementById('muteBtn').addEventListener('click', toggleMute);
}

function playBeat(time, freq, gain, dur) {
  const osc = audioCtx.createOscillator();
  const g   = audioCtx.createGain();
  osc.connect(g);
  g.connect(audioCtx.destination);
  osc.type = 'sine';
  osc.frequency.value = freq;
  g.gain.setValueAtTime(0, time);
  g.gain.linearRampToValueAtTime(gain, time + 0.015);
  g.gain.exponentialRampToValueAtTime(0.0001, time + dur);
  osc.start(time);
  osc.stop(time + dur);
}

function doHeartbeat() {
  if (!audioCtx || isMuted) return;
  const t = audioCtx.currentTime;
  playBeat(t,        62, 0.35, 0.14);  // lub
  playBeat(t + 0.18, 55, 0.25, 0.12); // dub
}

function startHeartbeat(bpm) {
  currentBPM = bpm;
  if (heartTimer) clearInterval(heartTimer);
  const ms = (60 / bpm) * 1000;
  doHeartbeat();
  heartTimer = setInterval(doHeartbeat, ms);
}

function setHeartbeatBPM(bpm) {
  if (bpm !== currentBPM) startHeartbeat(bpm);
}

function playTriumph() {
  if (!audioCtx || isMuted) return;
  const notes = [523, 659, 784, 1047]; // C5 E5 G5 C6
  notes.forEach((f, i) => {
    const t = audioCtx.currentTime + i * 0.12;
    playBeat(t, f, 0.3, 0.25);
  });
}

function toggleMute() {
  isMuted = !isMuted;
  document.getElementById('muteBtn').textContent = isMuted ? '🔇' : '🔊';
  if (!isMuted) doHeartbeat();
}
```

- [ ] **Step 2: Hook triumph sound into the won state — update `showState()`**

Find `if (typeof setHeartbeatBPM === 'function') setHeartbeatBPM(STATE_BPM[id] || 60);` and add after it:

```javascript
  if (id === 'won') setTimeout(playTriumph, 300);
```

- [ ] **Step 3: Verify**

Click "See Full Vision →", then drag the divider (or click the button — first interaction initialises audio). You should hear a slow heartbeat that speeds up as the auction heats up, peaks at the countdown, and plays a 4-note rising triumph when "YOU WON!" appears. The 🔇 button mutes/unmutes.

---

## Task 11: Deals Section + Countdown Timers

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html`

- [ ] **Step 1: Add deals HTML inside `#dealsSection`**

```html
<section class="deals-section" id="dealsSection">
  <div class="section-header">
    <div class="section-eyebrow">Don't Miss Out</div>
    <h2 class="section-title">Hot Deals</h2>
  </div>
  <div class="deals-grid">
    <!-- Deal of the Week -->
    <div class="deal-card" id="dealWeek">
      <div class="deal-badge">🔥 DEAL OF THE WEEK</div>
      <div class="deal-img">🧊</div>
      <div class="deal-name">Samsung Side-by-Side Fridge</div>
      <div class="deal-prices">
        <span class="deal-was">$2,499</span>
        <span class="deal-now">$1,799</span>
      </div>
      <div class="deal-save">Save $700</div>
      <div class="deal-timer" id="timerWeek">Loading...</div>
      <button class="deal-btn">Grab This Deal</button>
    </div>
    <!-- Deal of the Month -->
    <div class="deal-card" id="dealMonth">
      <div class="deal-badge" style="background:var(--gold);color:#000">⭐ DEAL OF THE MONTH</div>
      <div class="deal-img">🛋️</div>
      <div class="deal-name">3-Piece Living Room Set</div>
      <div class="deal-prices">
        <span class="deal-was">$5,200</span>
        <span class="deal-now">$3,499</span>
      </div>
      <div class="deal-save">Save $1,701</div>
      <div class="deal-timer" id="timerMonth">Loading...</div>
      <button class="deal-btn">Grab This Deal</button>
    </div>
  </div>

  <!-- Email opt-in -->
  <div class="optin-strip">
    <div class="optin-text">
      <strong>Be first.</strong> Get exclusive deals, new arrivals &amp; auction alerts.
    </div>
    <div class="optin-form">
      <input class="optin-input" type="email" placeholder="your@email.com">
      <button class="optin-btn">Notify Me</button>
    </div>
    <div class="optin-micro">No spam. Unsubscribe anytime.</div>
  </div>
</section>
```

- [ ] **Step 2: Add deals + opt-in CSS**

```css
/* ── Deals Section ── */
.deals-section { padding: 80px 40px; background: var(--dark); }

.section-header { text-align: center; margin-bottom: 48px; }
.section-eyebrow {
  font-family: var(--font-head); font-size: 11px; font-weight: 700;
  letter-spacing: 4px; color: var(--orange); text-transform: uppercase; margin-bottom: 10px;
}
.section-title {
  font-family: var(--font-head); font-size: clamp(28px, 3vw, 42px);
  font-weight: 800; color: var(--white);
}

.deals-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 60px; }

.deal-card {
  background: var(--card-bg);
  border: 1px solid #2a2a2a;
  border-radius: 16px;
  padding: 28px 24px;
  display: flex; flex-direction: column; align-items: center; gap: 10px;
  text-align: center;
  transition: border-color 0.3s, box-shadow 0.3s;
  box-shadow: 0 0 0 0 rgba(244,123,32,0);
}
.deal-card:hover {
  border-color: var(--orange);
  box-shadow: 0 0 30px rgba(244,123,32,0.2);
}
.deal-badge {
  background: var(--orange); color: #fff;
  font-family: var(--font-head); font-size: 9px; font-weight: 800;
  padding: 4px 14px; border-radius: 20px; letter-spacing: 1px;
}
.deal-img { font-size: 56px; }
.deal-name { font-weight: 600; font-size: 14px; color: var(--white); }
.deal-prices { display: flex; align-items: baseline; gap: 12px; }
.deal-was { font-size: 14px; color: var(--muted); text-decoration: line-through; }
.deal-now { font-family: var(--font-head); font-size: 32px; font-weight: 800; color: var(--gold); }
.deal-save { font-size: 11px; color: var(--green); font-weight: 600; }
.deal-timer {
  font-family: var(--font-head); font-size: 13px; font-weight: 700;
  color: var(--orange); background: #111; padding: 6px 16px; border-radius: 20px;
  letter-spacing: 2px;
}
.deal-btn {
  background: var(--orange); color: #fff;
  font-family: var(--font-head); font-weight: 700; font-size: 12px;
  padding: 10px 24px; border-radius: 30px; width: 100%;
  transition: transform 0.2s, box-shadow 0.2s;
}
.deal-btn:hover { transform: scale(1.04); box-shadow: 0 0 20px rgba(244,123,32,0.5); }

/* ── Opt-in strip ── */
.optin-strip {
  background: var(--orange);
  border-radius: 16px;
  padding: 32px 40px;
  display: flex; flex-direction: column; align-items: center; gap: 14px;
  text-align: center;
}
.optin-text { font-size: 16px; color: #fff; }
.optin-form { display: flex; gap: 10px; }
.optin-input {
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.4);
  border-radius: 30px; padding: 10px 20px;
  color: #fff; font-size: 13px; width: 220px;
}
.optin-input::placeholder { color: rgba(255,255,255,0.7); }
.optin-btn {
  background: #fff; color: var(--orange);
  font-family: var(--font-head); font-weight: 800; font-size: 12px;
  padding: 10px 20px; border-radius: 30px;
}
.optin-micro { font-size: 10px; color: rgba(255,255,255,0.7); }
```

- [ ] **Step 3: Add countdown timer JS**

```javascript
// ── Deal Countdown Timers ──
function startDealTimers() {
  // Week deal: ends in 3 days from now
  const weekEnd  = new Date(Date.now() + 3 * 24 * 60 * 60 * 1000);
  // Month deal: ends in 18 days from now
  const monthEnd = new Date(Date.now() + 18 * 24 * 60 * 60 * 1000);

  function fmt(ms) {
    if (ms <= 0) return '00d 00h 00m 00s';
    const d = Math.floor(ms / 86400000);
    const h = Math.floor((ms % 86400000) / 3600000);
    const m = Math.floor((ms % 3600000) / 60000);
    const s = Math.floor((ms % 60000) / 1000);
    return `${String(d).padStart(2,'0')}d ${String(h).padStart(2,'0')}h ${String(m).padStart(2,'0')}m ${String(s).padStart(2,'0')}s`;
  }

  setInterval(() => {
    document.getElementById('timerWeek').textContent  = fmt(weekEnd  - Date.now());
    document.getElementById('timerMonth').textContent = fmt(monthEnd - Date.now());
  }, 1000);
}
```

- [ ] **Step 4: Call `startDealTimers()` inside `triggerHeroEntrance()`**

Add to the bottom of `triggerHeroEntrance()`:

```javascript
  startDealTimers();
```

- [ ] **Step 5: Add GSAP scroll entrance for deal cards inside `triggerHeroEntrance()`**

```javascript
  gsap.from('#dealWeek',  { scrollTrigger: { trigger: '#dealWeek',  scroller: '#afterPanel', start: 'top 85%' }, x: -60, opacity: 0, duration: 0.8, ease: 'power3.out' });
  gsap.from('#dealMonth', { scrollTrigger: { trigger: '#dealMonth', scroller: '#afterPanel', start: 'top 85%' }, x:  60, opacity: 0, duration: 0.8, ease: 'power3.out' });
```

- [ ] **Step 6: Verify**

After clicking "See Full Vision →", scroll down (inside the right panel). Two deal cards should slide in from left/right. Countdown timers tick live. Email opt-in strip is orange and full-width.

---

## Task 12: Mobile App Preview Section

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html`

- [ ] **Step 1: Add app preview HTML inside `#appSection`**

```html
<section class="app-section" id="appSection">
  <div class="app-inner">
    <div class="app-copy">
      <div class="section-eyebrow">Available Soon</div>
      <h2 class="section-title" style="text-align:left">The Massy App.</h2>
      <p class="app-desc">The store in your pocket. Shop, track deals, and join live auctions from anywhere — instant push notifications keep you always in the game.</p>
      <div class="app-features">
        <div class="app-feat">📦 <span>What's New</span></div>
        <div class="app-feat">🔥 <span>Live Deals Feed</span></div>
        <div class="app-feat">⚡ <span>Auction Bid Wars</span></div>
        <div class="app-feat">🔔 <span>Instant Notifications</span></div>
      </div>
      <div class="store-badges">
        <div class="badge">🍎 App Store</div>
        <div class="badge">▶ Google Play</div>
      </div>
    </div>
    <div class="app-phones">
      <!-- Phone 1: Dashboard -->
      <div class="app-phone-frame">
        <div class="app-phone-notch"></div>
        <div class="app-phone-screen">
          <div class="app-screen-header">Good morning, James 👋</div>
          <div class="app-tabs">
            <span class="app-tab active">What's New</span>
            <span class="app-tab">Deals</span>
            <span class="app-tab">Auctions</span>
          </div>
          <div class="app-card-mini">📺 New arrivals in Electronics →</div>
          <div class="app-card-mini orange">🔥 Deal ends in 02:14:33</div>
          <div class="app-card-mini">🛋️ Furniture sale — up to 40% off</div>
          <div class="app-notif">🔔 Auction starting in 5 minutes!</div>
        </div>
      </div>
      <!-- Phone 2: Live Auction -->
      <div class="app-phone-frame" style="margin-top:40px">
        <div class="app-phone-notch"></div>
        <div class="app-phone-screen dark">
          <div class="app-live-badge">🔴 LIVE</div>
          <div class="app-live-product">📺</div>
          <div class="app-live-name">Samsung 65" QLED TV</div>
          <div class="app-live-bid">$412.00</div>
          <div class="app-live-time">00:01:23</div>
          <div class="app-live-bidders">75 active bidders</div>
          <button class="app-bid-btn">BID NOW</button>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Add app section CSS**

```css
/* ── App Section ── */
.app-section { padding: 80px 40px; background: #0a0a0a; }
.app-inner { display: flex; align-items: center; gap: 60px; }
.app-copy { flex: 1; }
.app-desc { color: var(--muted); font-size: 14px; line-height: 1.7; margin: 20px 0 28px; max-width: 400px; }
.app-features { display: flex; flex-direction: column; gap: 10px; margin-bottom: 28px; }
.app-feat { display: flex; align-items: center; gap: 10px; font-size: 13px; color: var(--white); }
.app-feat span { color: var(--muted); }
.store-badges { display: flex; gap: 12px; }
.badge {
  background: #1a1a1a; border: 1px solid #333;
  color: var(--white); font-size: 12px; font-weight: 600;
  padding: 10px 20px; border-radius: 10px;
}

/* App phone mockups */
.app-phones { display: flex; gap: 20px; align-items: flex-start; flex-shrink: 0; }
.app-phone-frame {
  width: 160px; height: 320px;
  background: #111; border: 2px solid #2a2a2a;
  border-radius: 28px; overflow: hidden; position: relative;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}
.app-phone-notch {
  width: 50px; height: 10px;
  background: #111; border-radius: 0 0 8px 8px;
  margin: 0 auto; position: relative; z-index: 5;
}
.app-phone-screen {
  padding: 10px 10px 14px;
  display: flex; flex-direction: column; gap: 6px;
  background: #f8f9fa;
}
.app-phone-screen.dark { background: #0d0d0d; }
.app-screen-header { font-size: 9px; font-weight: 700; color: #333; }
.app-tabs { display: flex; gap: 6px; }
.app-tab { font-size: 7px; padding: 3px 7px; border-radius: 10px; color: #666; background: #eee; font-weight: 600; }
.app-tab.active { background: var(--orange); color: #fff; }
.app-card-mini { background: #fff; border-radius: 6px; padding: 6px 8px; font-size: 8px; color: #333; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
.app-card-mini.orange { background: #fff3ec; color: var(--orange); font-weight: 600; }
.app-notif { background: #1a1a1a; color: #fff; border-radius: 6px; padding: 6px 8px; font-size: 8px; }

/* Live auction phone */
.app-live-badge { font-size: 8px; font-weight: 800; color: var(--red); letter-spacing: 2px; }
.app-live-product { font-size: 36px; text-align: center; }
.app-live-name { font-size: 9px; color: var(--muted); text-align: center; }
.app-live-bid { font-family: var(--font-head); font-size: 28px; font-weight: 900; color: var(--gold); text-align: center; }
.app-live-time { font-family: var(--font-head); font-size: 18px; font-weight: 800; color: var(--red); text-align: center; letter-spacing: 2px; }
.app-live-bidders { font-size: 9px; color: var(--muted); text-align: center; }
.app-bid-btn {
  background: var(--orange); color: #fff;
  font-weight: 800; font-size: 11px;
  padding: 8px; border-radius: 20px; width: 100%; margin-top: 4px;
}
```

- [ ] **Step 3: Verify**

Scroll down past the deals section. App preview appears: copy on left, two phone mockups on right — one showing the dashboard, one showing the live auction screen. No console errors.

---

## Task 13: Closing CTA Section

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html`

- [ ] **Step 1: Add closing HTML inside `#closingSection`**

```html
<section class="closing-section" id="closingSection">
  <div class="closing-inner">
    <div class="closing-eyebrow">Your Competitive Edge Awaits</div>
    <h2 class="closing-title">Ready to transform<br>your business?</h2>
    <p class="closing-sub">Let's build the future of Massy Stores together. Full stack web, mobile app, live auctions — delivered by INTERXDB.</p>
    <button class="closing-btn">Start the Conversation</button>
    <div class="closing-contact">
      <span>✉ hello@interxdb.com</span>
      <span>📞 +1 (246) 000-0000</span>
    </div>
    <div class="closing-stack">
      <div class="stack-item">Next.js</div>
      <div class="stack-item">React Native</div>
      <div class="stack-item">Node.js</div>
      <div class="stack-item">PostgreSQL</div>
      <div class="stack-item">Socket.IO</div>
      <div class="stack-item">AI Ready</div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Add closing CSS**

```css
/* ── Closing CTA ── */
.closing-section {
  padding: 100px 40px;
  background: linear-gradient(180deg, #0a0a0a 0%, #0D0D0D 100%);
  text-align: center;
  border-top: 1px solid #1a1a1a;
}
.closing-inner { max-width: 640px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 20px; }
.closing-eyebrow { font-family: var(--font-head); font-size: 11px; font-weight: 700; letter-spacing: 4px; color: var(--orange); text-transform: uppercase; }
.closing-title { font-family: var(--font-head); font-size: clamp(28px, 3.5vw, 48px); font-weight: 900; color: var(--white); line-height: 1.1; }
.closing-sub { font-size: 14px; color: var(--muted); line-height: 1.7; max-width: 500px; }
.closing-btn {
  background: var(--orange); color: #fff;
  font-family: var(--font-head); font-weight: 800; font-size: 15px;
  padding: 16px 48px; border-radius: 40px; letter-spacing: 1px;
  box-shadow: 0 0 40px rgba(244,123,32,0.5);
  transition: transform 0.2s, box-shadow 0.2s;
}
.closing-btn:hover { transform: scale(1.05); box-shadow: 0 0 60px rgba(244,123,32,0.8); }
.closing-contact { display: flex; gap: 32px; font-size: 13px; color: var(--muted); }
.closing-stack { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin-top: 12px; }
.stack-item {
  background: #1a1a1a; border: 1px solid #2a2a2a;
  color: var(--muted); font-size: 10px; font-weight: 600;
  padding: 5px 14px; border-radius: 20px; letter-spacing: 1px;
}
```

- [ ] **Step 3: Verify full scroll**

Scroll all the way down the After panel. Sequence should be: Hero → Deals + opt-in → App preview → Closing CTA → Footer (Designed by INTERXDB). All sections visible and styled correctly.

---

## Task 14: Final Polish — Responsive + Scroll Triggers + Startup State

**Files:**
- Modify: `C:\AI Software\websites\Massy\demo\index.html`

- [ ] **Step 1: Add responsive CSS at the bottom of `<style>`**

```css
/* ── Responsive ── */
@media (max-width: 900px) {
  .hero-section { flex-direction: column; padding: 60px 20px 40px; align-items: center; }
  .hero-content { max-width: 100%; }
  .phone-wrap { margin-top: 20px; }
  .deals-grid { grid-template-columns: 1fr; }
  .app-inner { flex-direction: column; }
  .app-phones { justify-content: center; }
  .before-panel, .after-panel { width: 50% !important; }
  .nav-links { gap: 12px; }
}
@media (max-width: 600px) {
  .split-wrapper { flex-direction: column; height: auto; }
  .before-panel, .after-panel { width: 100% !important; height: 50vh; }
  .divider { width: 100%; height: 4px; cursor: row-resize; }
  .hero-section { padding: 40px 16px; }
}
```

- [ ] **Step 2: Auto-start auction loop + particles when page loads (not just on "See Vision" click)**

The auction phone is visible in the split screen right panel from the start, so it should animate immediately. Add this at the bottom of the JS `<script>` block:

```javascript
// Auto-start visible elements on page load
window.addEventListener('DOMContentLoaded', () => {
  startParticles();
  initThreeJS();
  startAuctionLoop();
  startDealTimers();
});
```

- [ ] **Step 3: Add scroll trigger for app section entrance**

Add inside `triggerHeroEntrance()`:

```javascript
  gsap.from('.app-phone-frame', {
    scrollTrigger: { trigger: '#appSection', scroller: '#afterPanel', start: 'top 80%' },
    y: 60, opacity: 0, duration: 0.8, stagger: 0.2, ease: 'power3.out'
  });
  gsap.from('.closing-inner', {
    scrollTrigger: { trigger: '#closingSection', scroller: '#afterPanel', start: 'top 80%' },
    y: 40, opacity: 0, duration: 0.8, ease: 'power3.out'
  });
```

- [ ] **Step 4: Final browser test — full walkthrough**

Open `index.html` in Chrome:
1. Page loads — left panel shows current Massy site, right panel shows dark redesign with phone animation playing and particles running
2. Drag the divider — panels resize smoothly
3. Click "See the Full Vision →" — Before collapses, After expands, GSAP text animates in, audio heartbeat starts
4. Scroll down in the right panel — deal cards slide in, countdown timers tick, opt-in strip visible
5. Continue scrolling — app preview section animates in, closing CTA visible with tech stack badges and INTERXDB credit
6. Mute button toggles audio
7. Auction phone loops through all 8 states with heartbeat matching the tension
8. No console errors

- [ ] **Step 5: Commit final demo**

```bash
git -C "C:\AI Software\websites" add demo/index.html
git -C "C:\AI Software\websites" commit -m "feat: complete massy before/after pitch demo — drag slider, 3D orbit, auction sequence, heartbeat audio, deals, app preview"
```

---

## Self-Review Checklist

- [x] **Spec coverage:** All 7 spec sections covered — Before/After slider ✓, Cinematic hero ✓, Auction sequence (all 8 steps) ✓, Heartbeat audio (all phases + mute) ✓, Deals + timers + opt-in ✓, Mobile app preview ✓, Closing CTA ✓
- [x] **Tech stack comments:** Embedded in `<!-- ... -->` HTML comment block in `<head>` with all Phase 2/3 technologies and Local AI note
- [x] **INTERXDB credit:** In footer + closing section
- [x] **Placeholders:** None — all timers, prices, product names, and colors are concrete values
- [x] **Type consistency:** `showState()`, `startAuctionLoop()`, `initAudio()`, `triggerHeroEntrance()` referenced consistently across tasks
- [x] **Audio init:** Correctly deferred to first user interaction (mousedown on divider or button click)
- [x] **Single file:** All output goes to `demo/index.html` — no external files needed
