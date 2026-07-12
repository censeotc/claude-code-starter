# Website Style Guide — Local Home-Services Template

A reusable styling reference extracted from a real local-services website (home trades / HVAC-style business). All business-identifying content has been removed. Give this file to Claude Design as the brief for building a website template.

**Reference source:** homepage HTML only. Two details live in files that couldn't be retrieved and are marked **[VERIFY]** — everything else is confirmed from the markup.

---

## 1. Overall aesthetic

- **Style:** friendly, trustworthy, local-business feel — not corporate, not minimalist. Warm accent color over a deep navy base, lots of real photography (team photos, technicians at work, service imagery), badge/award logos used generously as social proof.
- **Era/framework:** classic Bootstrap 3 marketing-site layout — boxed 1170px container, full-width color-banded sections, 12-column responsive grid.
- **Tone:** conversion-focused. Phone number and booking CTA visible at all times; multiple "nominate / finance / contact" pathways above the fold.

## 2. Color palette

| Role | Value | Where it appears |
|---|---|---|
| Primary accent (brand orange/amber) | `#F29E00` | Brand color (declared in favicon mask-icon), buttons, link accents, "Read more" links |
| Primary dark (deep navy) | `#212A44` | Full-width feature band backgrounds; likely header/footer base |
| White | `#FFFFFF` | Header text/links, text over dark bands, hero captions |
| Light gray | (defined in stylesheet) **[VERIFY]** | "Gray content box" section background behind intro + reviews |
| Body text | dark gray/near-black **[VERIFY]** | Paragraph copy on white |

Usage pattern: white/light-gray content sections alternate with full-bleed dark navy and photo-background bands. Orange is reserved for CTAs and small accents — it is the action color, never a background for long text.

**[VERIFY]** Exact grays, hover states, and button hex values are defined in the site's `layout.css`, which was not retrievable. `#F29E00` and `#212A44` are confirmed from the markup.

## 3. Typography

- **Font delivery:** Adobe Fonts (Typekit kit). **[VERIFY]** The exact family names are inside the kit JS, which was not retrievable — visually inspect the live site to confirm. Safe assumption: a rounded/humanist sans-serif for headings and body.
- **Icons:** Font Awesome 4 (`fa fa-phone`, `fa fa-bars`, `fa fa-caret-right`, social glyphs).
- **Hierarchy observed:**
  - Page-header strip: single large tagline line directly under the hero
  - `h1` centered for major section titles (e.g. "Awards"), followed by an `<hr>`
  - `h2` for section headings ("Professional Affiliations", footer call-to-action)
  - `h3` for card/tile captions and sub-headings
  - `h4` italic centered for taglines under images
  - Emphasis style: bold + italic combined for key words inside body copy
- **Alignment:** section headings frequently centered; body copy left-aligned.

## 4. Layout structure (top to bottom)

1. **Header bar** (dark background, white text)
   - Logo left (~25% width), contact info right: "City, State • 24 Hour Service • phone number" as plain white text, phone numbers are `tel:` links
   - Horizontal dropdown navigation below/beside (up to 3 levels deep), collapses to a hamburger (`fa-bars`) toolbar on mobile
   - Persistent **"Book Now!"** button in the nav (opens a scheduling widget) — the primary CTA

2. **Hero carousel** (full-width)
   - Auto-rotating image slider (FlexSlider pattern), 4 lifestyle/service photos
   - Overlaid caption: large two-line brand tagline, width synced to viewport by JS
   - Overlaid promo ribbon (e.g. "NEW FINANCING OPTIONS!!!") in white, linking to a promo page
   - Row of 3 ghost/quick-link buttons over or under the hero: CONTACT / FINANCING / JOIN US (uppercase labels)

3. **Tagline strip** — one-sentence positioning statement ("your hometown professionals since …")

4. **Gray content box** — two columns (7/5 split):
   - Left: intro paragraph + full-width team photo
   - Right: embedded reviews widget (third-party) with an orange "Read more ›" link

5. **Three-card row** (equal thirds, `col-sm-4`)
   - Each card: background-image tile, caption-on-hover effect, `h3` title, and a brand-colored button (`btn-sitecolor`)

6. **Dark navy feature band** (`#212A44`, full row)
   - Left third: award/recognition photo; right two-thirds: embedded 16:9 YouTube video

7. **Affiliations & awards section** (white)
   - Centered `h2`, then rows of 3–4 partner/association logos (centered, scaled by % width)
   - Centered `h1` "Awards" + `hr`, then rows of award badge logos (~175px tall)

8. **Photo-background band** ("imagebgBox")
   - Full-bleed background image, white text
   - Left: `h2` + `h3` + paragraph (service-area pitch); right: coverage-map graphic + italic centered tagline

9. **Specialty grid** — 5 equal columns (custom `fivecol` class, container-fluid full width)
   - Each: photo tile with Codrops-style caption-hover effect (`cs-style-3`), `h3` service name revealed on hover

10. **Footer** (dark)
    - Big CTA block: "Call For Your Free Estimate Today" `h2` + phone number `h2` (tel: link), with a "since-year" badge floated right
    - Logo, inline horizontal footer nav (single-level list), address block
    - Social icon row (custom round PNG icons: Facebook, Google reviews, Instagram, Yelp, email)
    - Copyright line with small designer credit

## 5. Components

- **Buttons**
  - Primary: `btn btn-sitecolor` — Bootstrap button skinned in the brand orange, used on cards
  - Nav CTA: pill/solid "Book Now!" button with white text
  - Hero quick-links: large uppercase text links styled as flat buttons
- **Cards/tiles:** background-image div + hover-revealed caption + button; used in 3-across and 5-across grids
- **Sliders:** FlexSlider for both the hero and the reviews rotator
- **Modals:** Bootstrap modal available (`data-toggle="modal"`)
- **Embeds:** responsive 16:9 wrapper (`embed-responsive-16by9`) for video

## 6. Grid & responsive behavior

- Bootstrap 3: `col-xs / col-sm / col-md` breakpoints, offsets, push/pull for footer reordering
- Mobile: nav collapses to hamburger; header contact line hides the middle segment (`hidden-xs`); hero caption hides when the mobile menu opens; card rows stack to full width
- Section rhythm: ~15–20px vertical padding/margins between bands (inline styles use 15/20px)

## 7. Tech notes (for the template build)

- Original stack: Bootstrap 3 + jQuery, FlexSlider carousel, Font Awesome 4, third-party menu plugin, CMS-rendered pages — **rebuild with modern equivalents** (CSS grid/flexbox, a lightweight carousel or static hero, SVG icons) while keeping the same visual structure
- Third-party surfaces to plan for: online-booking widget button, reviews widget embed, chat widget, analytics/GTM
- Keep: `tel:` links everywhere the phone number appears; sticky/prominent booking CTA; alternating band structure

## 8. What to parameterize per client

- Accent color (here `#F29E00`) and dark base (here `#212A44`)
- Logo, hero photos, tagline, promo ribbon text
- Service names for the 5-tile grid and nav
- Affiliation/award logo sets
- Booking/reviews/chat widget embeds
