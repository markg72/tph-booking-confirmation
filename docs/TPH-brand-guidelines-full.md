# The Planters House - Brand Guidelines (Full)

**Version 1.0 | November 2025**

---

## Table of Contents

1. [Brand Overview](#brand-overview)
2. [Colour Palette](#colour-palette)
3. [Typography](#typography)
4. [Design Elements](#design-elements)
5. [Logo Usage](#logo-usage)
6. [Email & Document Templates](#email--document-templates)
7. [Photography Style](#photography-style)
8. [Tone of Voice](#tone-of-voice)
9. [Brand Applications](#brand-applications)
10. [Accessibility Standards](#accessibility-standards)
11. [Technical Specifications](#technical-specifications)

---

## Brand Overview

The Planters House is a boutique tea estate hotel in Sri Lanka's Uva Province, offering an authentic heritage experience in the heart of tea country. Our brand identity reflects the natural beauty, colonial heritage, and artisanal quality of Ceylon tea estates.

**Brand Values:**
- Authenticity over artifice
- Heritage with modern comfort
- Personal service at scale
- Environmental stewardship
- Tea country expertise

---

## Colour Palette

### Primary Colours

#### Deep Tea Green `#264b3a`
**Primary brand colour**

- **RGB:** 38, 75, 58
- **CMYK:** 75, 38, 62, 44
- **Usage:** Headers, titles, borders, primary CTAs, navigation
- **Meaning:** Tea heritage, nature, tradition, stability
- **Contrast:** 12.4:1 on white (excellent accessibility)

**When to use:**
- All primary headers and navigation elements
- Border accents on information boxes
- Primary call-to-action buttons (with white text)
- Email/document headers

**When not to use:**
- Body text (too dark, use soft grey instead)
- Backgrounds for large areas (overwhelming)

---

#### Warm Cream `#f6f1e9`
**Secondary brand colour**

- **RGB:** 246, 241, 233
- **CMYK:** 3, 3, 7, 0
- **Usage:** Backgrounds, accent boxes, subtle highlights
- **Meaning:** Tea colour, warmth, hospitality, breathing space
- **Works with:** All palette colours

**When to use:**
- Section backgrounds for visual breaks
- Payment/pricing information boxes
- Alternating content sections on web pages
- Email background accents

**When not to use:**
- Primary text backgrounds (white is clearer)
- With dusty rose (insufficient contrast)

---

#### Muted Gold `#b89b5e`
**Accent colour**

- **RGB:** 184, 155, 94
- **CMYK:** 24, 30, 61, 11
- **Usage:** Highlights, links, subtle CTAs, decorative elements
- **Meaning:** Quality, heritage, Ceylon tea, luxury
- **Important:** Use sparingly for maximum impact

**When to use:**
- Hover states on links
- Border accents (optional)
- Decorative elements
- Large text highlights (18pt+)

**When not to use:**
- Normal-sized body text (fails WCAG AA contrast)
- Primary backgrounds
- Critical information (insufficient contrast)

---

### Supporting Colours

#### Soft Grey `#6b6b6b`
**Primary text colour**

- **RGB:** 107, 107, 107
- **CMYK:** 53, 44, 44, 17
- **Usage:** Body text, captions, secondary information
- **Contrast:** 5.7:1 on white (WCAG AA compliant)

**Why not black?**
Soft grey is easier to read for extended periods and feels more sophisticated than pure black `#000000`.

---

#### Sage `#9caf88`
**Information highlight colour**

- **RGB:** 156, 175, 136
- **CMYK:** 34, 13, 41, 3
- **Usage:** Information boxes, callouts, highlights
- **Meaning:** Tea gardens, natural environment, growth
- **Pairs with:** Deep tea green borders, white text

**Best practices:**
- Always use white `#ffffff` text on sage backgrounds
- Combine with `#264b3a` border-left for information boxes
- Excellent for policies, important notices, travel tips

---

### Seasonal/Accent Colours

#### Dusty Rose `#c4989f`
**Seasonal promotional colour**

- **RGB:** 196, 152, 159
- **CMYK:** 23, 36, 20, 4
- **Usage:** Seasonal promotions, feminine touches, special occasions
- **Meaning:** Tea flowers, sunrise over estates, romance

**Use sparingly for:**
- Valentine's/romantic packages
- Women's retreat promotions
- Floral design accents

**Never combine with:**
- Sage (insufficient contrast)
- As primary backgrounds

---

## Typography

### Primary Typeface: Playfair Display

**Character:** Elegant, traditional, refined serif
**Evokes:** Colonial heritage, boutique luxury, timeless quality
**Available weights:** Regular (400), Bold (700)

#### Hierarchy

**H1 - Page Titles**
```
Font: Playfair Display Bold
Size: 36-48px
Colour: #264b3a (deep tea green)
Line height: 1.2
Use: Page headers, hero titles
```

**H2 - Section Headings**
```
Font: Playfair Display Bold
Size: 28-32px
Colour: #264b3a (deep tea green)
Line height: 1.3
Use: Section breaks, major headings
```

**H3 - Subsection Headings**
```
Font: Playfair Display Regular
Size: 20-24px
Colour: #264b3a (deep tea green)
Line height: 1.4
Use: Subsections, card titles
```

**Feature Text**
```
Font: Playfair Display Regular (Italic optional)
Size: 18-20px
Colour: #264b3a or #6b6b6b
Use: Pull quotes, testimonials, highlighted content
```

---

### Secondary Typeface: System Sans-Serif Stack

**Recommended stack:**
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

**Why system fonts?**
- Fast loading (no web font downloads)
- Excellent readability
- Native to each operating system
- Accessible and familiar

#### Usage

**Body Text**
```
Font: System Sans-Serif Regular
Size: 16px
Colour: #6b6b6b (soft grey)
Line height: 1.6
Letter spacing: Normal
```

**Captions**
```
Font: System Sans-Serif Regular
Size: 13-14px
Colour: #6b6b6b
Line height: 1.5
```

**Labels & UI Elements**
```
Font: System Sans-Serif Medium
Size: 12px
Colour: #6b6b6b
Transform: Uppercase
Letter spacing: 0.5px
```

---

## Design Elements

### Information Boxes

**Purpose:** Highlight policies, important notices, travel information

**Styling:**
```css
background: #9caf88; /* sage */
border-left: 3px solid #264b3a; /* deep tea green */
color: #ffffff; /* white text */
padding: 12px 16px;
border-radius: 4px;
margin-bottom: 12px;
```

**Example use cases:**
- Booking and cancellation policies
- Check-in/check-out information
- Travel tips and directions
- Important safety notices
- Dietary information

**Best practices:**
- Keep text concise (2-4 sentences max per box)
- Use paragraph format, not bullet points inside boxes
- Stack multiple boxes vertically with consistent spacing
- White text provides strong contrast on sage background

---

### Accent Boxes

**Purpose:** Display pricing, dates, payment information, inclusions

**Styling:**
```css
background: #f6f1e9; /* warm cream */
border: 1px solid #b89b5e; /* muted gold - optional */
color: #333333; /* dark grey text */
padding: 16px 20px;
border-radius: 4px;
margin-bottom: 16px;
```

**Example use cases:**
- Payment summaries
- Date ranges and booking windows
- Inclusion lists (breakfast, WiFi, etc.)
- Pricing breakdowns
- Confirmation details

**Best practices:**
- Optional muted gold border adds elegance
- Dark grey `#333333` text (not soft grey) for maximum contrast
- Slightly more padding than information boxes (feels spacious)

---

### Date Display Grid

**Three-column layout for booking confirmations:**

```
┌─────────────────┬─────────────────┬──────────────┐
│    Check-in     │   Check-out     │    Nights    │
│  [DD/MM/YYYY]   │  [DD/MM/YYYY]   │     [X]      │
└─────────────────┴─────────────────┴──────────────┘
```

**Styling:**
```css
/* Header row */
background: #9caf88; /* sage */
color: #264b3a; /* deep tea green */
font-weight: bold;
padding: 8px;
border-bottom: 2px solid #264b3a;

/* Data row */
background: #ffffff;
color: #333333;
padding: 12px;
border: 1px solid #e0e0e0;
```

**Why three columns?**
- More scannable than inline text
- Clear visual hierarchy
- Professional presentation
- Easy to parse at a glance

---

### Buttons & CTAs

**Primary Button (High emphasis)**
```css
background: #264b3a; /* deep tea green */
color: #ffffff;
padding: 12px 24px;
border-radius: 4px;
font-weight: 500;
border: none;

/* Hover state */
background: #1a3327; /* darker tea green */
```

**Secondary Button (Medium emphasis)**
```css
background: transparent;
color: #264b3a;
padding: 12px 24px;
border: 2px solid #264b3a;
border-radius: 4px;
font-weight: 500;

/* Hover state */
background: #f6f1e9; /* warm cream */
```

**Text Link (Low emphasis)**
```css
color: #b89b5e; /* muted gold */
text-decoration: none;
border-bottom: 1px solid transparent;

/* Hover state */
border-bottom: 1px solid #b89b5e;
```

---

## Logo Usage

### Clear Space

Maintain clear space around the logo equal to the height of the peacock crest (the topmost element).

**Visual guide:**
```
    [crest height]
    ↕
    ┌─────────────────┐
    │   [PEACOCK]     │
    │   [CREST]       │
    │                 │
    │ THE PLANTERS    │
    │     HOUSE       │
    └─────────────────┘
←→                    ←→
[crest    Logo      [crest
height]             height]
    ↕
[crest height]
```

---

### Minimum Sizes

**Digital applications:**
- Minimum width: 120px
- Recommended: 150-200px for web headers
- Maximum: 300px (avoid oversized logos)

**Print applications:**
- Minimum width: 30mm
- Business cards: 40-50mm
- Letterhead: 60-80mm

---

### Approved Backgrounds

**White `#ffffff`**
- Use: Full-colour logo
- Most common application
- Best for print materials

**Warm Cream `#f6f1e9`**
- Use: Full-colour logo
- Softer than white
- Good for premium applications

**Deep Tea Green `#264b3a`**
- Use: White or cream logo version
- Strong brand presence
- Use for dark-theme applications

---

### Forbidden Uses

✗ Never place logo on busy photographic backgrounds without overlay
✗ Never use logo on dusty rose background (poor contrast)
✗ Never use logo on sage background (poor contrast)
✗ Never stretch, distort, or alter logo proportions
✗ Never rotate logo at angles
✗ Never add drop shadows or effects
✗ Never change logo colours
✗ Never recreate or modify logo artwork

---

## Email & Document Templates

### Email Structure

**Header section:**
```
┌─────────────────────────────────────┐
│  [Logo - centered or left-aligned]  │
│                                     │
└─────────────────────────────────────┘
```
- Background: White `#ffffff` or tea green `#264b3a`
- If white: Add 2px bottom border in `#264b3a`
- Padding: 20-30px

**Body section:**
```
Maximum width: 600-650px
Background: #ffffff
Padding: 20-30px
Font: System Sans-Serif, 16px, #6b6b6b
Line height: 1.6
```

**Accent sections:**
- Use warm cream `#f6f1e9` or sage `#9caf88` boxes
- Alternate with white for visual rhythm
- Maintain consistent padding

**Footer section:**
```
Line 1: [Policy reminder or call-to-action]
Line 2: Contact information

Style:
- Font size: 13px
- Colour: #666666
- Line spacing: 4-8px
- Background: White or very light grey
- Top border: 1px solid #e0e0e0
```

---

### Standard Footer Format

**Two-line structure (preferred):**
```
Please review our cancellation policy and payment terms above.
The Planters House | +94 (0)77 683 6955 | reservations@theplantershouse.com | www.theplantershouse.com
```

**Alternative formats:**

*Booking confirmations:*
```
We look forward to welcoming you to The Planters House.
The Planters House | +94 (0)77 683 6955 | reservations@theplantershouse.com | www.theplantershouse.com
```

*Enquiry responses:*
```
Please contact us if you need any further information.
The Planters House | +94 (0)77 683 6955 | reservations@theplantershouse.com | www.theplantershouse.com
```

**Avoid:**
- Three or more lines of text before contact info
- Flowery language or excessive warmth
- Repeated information from email body
- Social media links (keep footer clean)

---

### Document Templates (Letterhead, Invoices)

**Header:**
```
┌─────────────────────────────────────┐
│ [Logo - left]    [Date/Ref - right] │
└─────────────────────────────────────┘
```

**Body:**
- Margins: 25-30mm all sides
- Font: System Sans-Serif, 11-12pt
- Headings: Playfair Display, tea green `#264b3a`
- Line spacing: 1.4-1.5

**Footer:**
```
┌─────────────────────────────────────┐
│ The Planters House                   │
│ Monarakanda Estate, Koslanda        │
│ Uva Province, 90190, Sri Lanka      │
│ +94 (0)77 683 6955                  │
│ reservations@theplantershouse.com   │
└─────────────────────────────────────┘
```
- Font size: 9-10pt
- Colour: `#6b6b6b`
- Optional: 1px top border in `#264b3a`

---

## Photography Style

### Colour Grading Principles

**Warm tones:**
- Enhance golden hour lighting
- Complement cream and gold palette
- Avoid cool blue tones
- Natural warmth without oversaturation

**Green tones:**
- Natural, realistic greens
- Harmonize with tea green and sage
- Avoid artificial-looking enhancement
- Show authentic tea estate environment

**Overall feel:**
- Natural, uncontrived
- Honest representation
- Soft contrast (not harsh shadows)
- Slightly desaturated for elegance

---

### Subject Matter

**Primary focus:**

✓ Tea estate landscapes and garden vistas
✓ Colonial architecture and heritage details
✓ Authentic guest experiences (not staged)
✓ Local culture and tea-making craftsmanship
✓ Natural light and golden hour photography
✓ Interior spaces showing comfort and character
✓ Food and dining experiences
✓ Wildlife and nature (endemic species)

**Avoid:**

✗ Overly staged or artificial compositions
✗ Heavy filters or Instagram-style processing
✗ Generic hotel stock photography
✗ Unrealistic HDR or over-processed images
✗ Images that don't reflect actual guest experience
✗ Cluttered or unflattering angles

---

### Photography Specifications

**Web use:**
- Format: .JPG
- Resolution: 72dpi
- Colour space: sRGB
- File size: Under 200KB (optimized)
- Dimensions: Minimum 1920px width for hero images

**Print use:**
- Format: .TIFF or high-res .JPG
- Resolution: 300dpi
- Colour space: CMYK
- Uncompressed or minimal compression

---

## Tone of Voice

### Core Characteristics

**Professional yet warm**
- We are experts in tea country hospitality
- We care about each guest's experience
- We maintain professional boundaries
- We're approachable, not stuffy

**Knowledgeable but not pretentious**
- We share expertise without showing off
- We educate without talking down
- We use plain language
- We explain when needed

**Personal without being overfamiliar**
- We use first names in greetings
- We remember guest preferences
- We maintain appropriate distance
- We're friendly, not friends

**Clear and concise**
- We respect people's time
- We communicate essential information efficiently
- We avoid unnecessary words
- We structure information logically

---

### Language Guidelines

**British English:**
- Honour, colour, favour (not honor, color, favor)
- Organise, realise (not organize, realize)
- Centre, metre (not center, meter)
- Travelled, cancelled (double 'l')

**Punctuation preferences:**
- Use regular hyphens (-) not em dashes (—)
- Minimal exclamation marks (only for genuine excitement)
- Oxford comma when needed for clarity
- Standard apostrophe use (British style)

**Voice:**
- Active voice preferred: "We confirm your booking" not "Your booking has been confirmed"
- Second person for direct communication: "Your arrival" not "The guest's arrival"
- First person plural for The Planters House: "We look forward" not "The hotel looks forward"

---

### Email Greetings & Sign-offs

**Greetings:**
- Preferred: "Hi [First Name],"
- Formal alternative: "Dear [First Name],"
- Never: "Hello [First Name]!" (no exclamation mark)
- Never: "Dear Mr/Mrs [Surname]" (too formal)

**Sign-offs:**

*Standard:*
```
Best wishes,
Mark
```

*Professional (invoice/formal):*
```
Many thanks,
Mark
```

*Quick confirmations:*
```
Thanks,
Mark
```

*Never:*
- "Kind regards" (too corporate)
- "Warmest wishes" (too effusive)
- "Yours sincerely/faithfully" (too formal)
- Any sign-off with exclamation marks

---

### Writing Examples

**Good example (booking confirmation):**
```
Hi Sarah,

Thank you for your booking at The Planters House from 15th to 18th March 2026.

We've reserved The Garden Suite for you. Your rate of $325 per night includes breakfast, WiFi, and all taxes.

The balance of $975 is due by 13th February 2026. You can pay via bank transfer or credit card - details are in the attached invoice.

Please let us know your estimated arrival time and any dietary requirements.

Best wishes,
Mark
```

**Why it works:**
- Uses first name
- Clear structure (confirmation → details → payment → action needed)
- Specific dates and amounts
- Polite but not effusive
- Direct call-to-action

---

**Bad example:**
```
Dear Guest,

We are absolutely delighted to confirm your wonderful booking with us!! We can't wait to welcome you to our beautiful tea estate - it's going to be amazing!

As per our terms and conditions, payment must be received in accordance with our cancellation policy which you can find on our website.

We trust this meets with your approval.

Yours sincerely,
The Planters House Team
```

**Why it fails:**
- No personalization
- Excessive enthusiasm (multiple exclamation marks)
- Vague about payment details
- Corporate jargon ("as per", "meets with your approval")
- No specific information
- Impersonal sign-off

---

### Service Recovery Language

**Good approach:**
```
Hi James,

I can see where the confusion has come from - our booking system didn't update your room preference correctly.

I've moved you to The Sunbird Suite for your entire stay at no additional charge. This suite has the bunk room you requested for your children.

As a mini sorry for the mix-up, there'll be no charge for the children.

Best wishes,
Mark
```

**Principles:**
- Immediate acknowledgment
- Transparent explanation (no blame)
- Clear solution
- Small gesture ("mini sorry" not "we're terribly sorry")
- No excessive apology

---

## Brand Applications

### Website

**Navigation:**
- Background: `#264b3a` (deep tea green)
- Text: `#ffffff` (white)
- Hover: Slightly lighter tea green
- Active state: Muted gold `#b89b5e` underline

**Hero sections:**
- Full-width imagery
- Warm cream `#f6f1e9` overlay (20-30% opacity)
- Playfair Display headlines in white or tea green
- CTAs in muted gold or tea green

**Content sections:**
- Alternate white `#ffffff` and warm cream `#f6f1e9` backgrounds
- Maintain visual rhythm
- Use sage boxes for highlighted information

**Call-to-action buttons:**
- Primary: Muted gold `#b89b5e` background, white text
- Hover: Darker gold
- Secondary: Tea green border, transparent background

**Footer:**
- Background: `#264b3a` (deep tea green)
- Text: `#ffffff` or cream
- Links: Muted gold `#b89b5e`
- Structure: Multi-column layout with logo, contact, links

---

### Booking Confirmations

**Layout structure:**
- Maximum width: 650px
- Scale: 95% for A4 printing compatibility
- Background: White with cream/sage accents

**Date grid (three columns):**
```
Check-in | Check-out | Nights
```
- Header background: Sage `#9caf88`
- Border: Tea green `#264b3a`

**Payment/pricing boxes:**
- Background: Warm cream `#f6f1e9`
- Border: Optional muted gold `#b89b5e`

**Policy information:**
- Sage boxes `#9caf88` with white text
- Tea green `#264b3a` left border

**Headers:**
- Playfair Display
- Tea green `#264b3a`

---

### Marketing Materials

**Brochures/Flyers:**
- Dominant colour: Deep tea green `#264b3a`
- Breathing space: Warm cream `#f6f1e9`
- Accents: Muted gold `#b89b5e`
- Photography: High-quality estate images
- Typography: Playfair Display headlines, sans-serif body

**Social media graphics:**
- Template backgrounds: White, warm cream, or tea green
- Consistent logo placement
- Playfair Display for quotes/headlines
- Natural, warm-toned photography

**Print advertisements:**
- Hero image with cream overlay
- Minimal text (headline + CTA)
- Logo in bottom corner
- Contact information in small type

---

## Accessibility Standards

### WCAG Compliance Level

**Target:** WCAG AA compliance minimum
**Goal:** AAA compliance where feasible

---

### Contrast Ratios

All text must meet minimum contrast requirements:

**Normal text (under 18pt):**
- Minimum ratio: 4.5:1
- Recommended: 7:1 or higher

**Large text (18pt+ or 14pt+ bold):**
- Minimum ratio: 3:1
- Recommended: 4.5:1 or higher

---

### Approved Colour Combinations

**Excellent (AAA compliant):**

✓ `#264b3a` on `#ffffff` - **12.4:1** (deep tea green on white)
- Use for: All headers, important text, navigation

✓ `#333333` on `#f6f1e9` - **10.1:1** (dark grey on warm cream)
- Use for: Body text on cream backgrounds

✓ `#ffffff` on `#264b3a` - **12.4:1** (white on deep tea green)
- Use for: Reversed text, dark headers

**Good (AA compliant):**

✓ `#6b6b6b` on `#ffffff` - **5.7:1** (soft grey on white)
- Use for: Body text, captions

✓ `#264b3a` on `#f6f1e9` - **10.8:1** (tea green on cream)
- Use for: Headers on cream backgrounds

**Acceptable (AA large text only):**

⚠ `#ffffff` on `#9caf88` - **2.3:1** (white on sage)
- Use for: Large text (18pt+) only in information boxes
- Never for body text

⚠ `#b89b5e` on `#ffffff` - **3.2:1** (muted gold on white)
- Use for: Large decorative text, buttons (18pt+)
- Never for normal-sized text

**Forbidden combinations:**

✗ `#264b3a` on `#9caf88` - **2.8:1** (insufficient)
✗ `#b89b5e` on `#f6f1e9` - **2.9:1** (insufficient)
✗ `#c4989f` on `#ffffff` - **2.7:1** (insufficient)
✗ `#c4989f` on `#9caf88` - **1.2:1** (very poor)

---

### Text Sizing

**Minimum sizes:**
- Body text: 16px (desktop), 14px (mobile minimum)
- Captions: 13px minimum
- Labels: 12px minimum (uppercase with letter spacing)

**Never:**
- Use text smaller than 12px
- Rely on colour alone to convey information
- Use light text on light backgrounds

---

### Interactive Elements

**Focus states:**
All interactive elements must have clear focus indicators:
```css
outline: 2px solid #264b3a;
outline-offset: 2px;
```

**Touch targets:**
Minimum size: 44×44px for mobile interfaces

**Links:**
- Underline or other non-colour indicator required
- Colour alone is insufficient for accessibility

---

## Technical Specifications

### File Formats

**Logos:**
- **Vector:** .AI (Adobe Illustrator), .EPS, .SVG
- **Raster:** .PNG with transparent background
- **Print:** .EPS or .PDF (vector)
- **Web:** .SVG (preferred) or .PNG

**Photography:**
- **Web:** .JPG, 72dpi, sRGB colour space, optimized
- **Print:** .TIFF or high-res .JPG, 300dpi, CMYK colour space
- **Maximum web file size:** 200KB (compressed/optimized)

**Documents:**
- **Editable:** .DOCX, .XLSX, .INDD (InDesign)
- **Distribution:** .PDF (print-ready or web-optimized)

---

### Colour Values Reference

| Colour Name | Hex | RGB | CMYK | Pantone |
|-------------|-----|-----|------|---------|
| Deep Tea Green | `#264b3a` | 38, 75, 58 | 75, 38, 62, 44 | 5535 C (approx) |
| Warm Cream | `#f6f1e9` | 246, 241, 233 | 3, 3, 7, 0 | - |
| Muted Gold | `#b89b5e` | 184, 155, 94 | 24, 30, 61, 11 | 4515 C (approx) |
| Soft Grey | `#6b6b6b` | 107, 107, 107 | 53, 44, 44, 17 | Cool Gray 9 C |
| Sage | `#9caf88` | 156, 175, 136 | 34, 13, 41, 3 | 7493 C (approx) |
| Dusty Rose | `#c4989f` | 196, 152, 159 | 23, 36, 20, 4 | 5025 C (approx) |

**Note:** Pantone matches are approximate. Always use Hex/RGB for digital, CMYK for print.

---

### Web Font Loading

**Playfair Display:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
```

**CSS implementation:**
```css
h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', serif;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
```

---

### Print Specifications

**Business cards:**
- Size: 85mm × 55mm (standard UK)
- Bleed: 3mm all sides
- Resolution: 300dpi minimum
- Colour: CMYK
- Finish: Matt or silk (not gloss)

**Letterhead:**
- Size: A4 (210mm × 297mm)
- Bleed: 3mm all sides
- Resolution: 300dpi
- Colour: CMYK
- Paper: 100-120gsm premium uncoated

**Brochures:**
- Resolution: 300dpi
- Bleed: 3mm all sides
- Colour: CMYK
- Paper: 150-170gsm silk or matt

---

## Brand Governance

### Who Can Use These Guidelines

**Internal team:**
- Full access to all brand assets
- Authorized to create marketing materials
- Must follow guidelines for all communications

**External partners:**
- Limited access (logo, colours, basic guidelines)
- Must submit designs for approval
- Cannot alter brand assets

**Travel agents:**
- Logo usage for website listings (approved formats only)
- Rates cards with standard formatting
- Cannot create custom marketing materials

---

### Approval Process

**Requires approval:**
- New marketing materials
- Website design changes
- Print materials for distribution
- Partnership/co-branding materials
- Merchandise or promotional items

**Does not require approval:**
- Standard email templates (already approved)
- Internal documents using guidelines
- Social media posts following brand standards
- Minor text updates to existing materials

**Approval contact:**
Mark Griffiths - markgriffiths@peacockestate.com

---

### Brand Updates

**Version history:**
- v1.0 (November 2025) - Initial comprehensive guidelines
- Tea estate colour palette established
- Email template standards defined
- Accessibility compliance integrated

**Review schedule:**
- Annual review: November
- Updates as needed for new applications
- Maintain version control for all changes

---

### Questions & Support

For brand guideline questions, template requests, or asset access:

**Email:** markgriffiths@peacockestate.com
**Phone (UK):** +44 7836 388977
**Phone (Sri Lanka):** +94 775 238528 (WhatsApp)

---

*The Planters House Brand Guidelines v1.0 | November 2025*
*Monarakanda Estate, Koslanda, Uva Province, Sri Lanka*
