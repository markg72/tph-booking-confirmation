# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Claude API-powered transformation system that intelligently converts Cloudbeds booking confirmations into branded, professional confirmations for The Planters House boutique tea estate hotel. Using Claude's vision and generation capabilities, the system extracts data from any Cloudbeds PDF format and generates perfect HTML confirmations - no brittle regex patterns, fully adaptive to format changes.

## Claude API-Powered Processing

The system uses Claude API to:

1. **Read & Understand** Cloudbeds PDFs using vision capabilities (handles any format)
2. **Extract** all booking data intelligently (guest info, dates, amounts, context)
3. **Generate** perfect branded HTML following design constraints
4. **Apply** correct payment status colors based on balance
5. **Convert** to PDF while maintaining all design requirements
6. **Self-heal** when Cloudbeds changes their PDF format

## Why Claude API?

### Advantages Over Traditional Extraction

- **No Brittle Regex**: Claude understands context, not just patterns
- **Format Agnostic**: Works with any Cloudbeds PDF layout changes
- **Intelligent Inference**: Fills in missing data using context
- **Error Recovery**: Handles edge cases gracefully
- **Future-Proof**: Adapts to changes automatically

### Model & Pricing

**Model Used**: Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)

**Pricing** (as of 2025):
- **Input**: $3.00 per million tokens
- **Output**: $15.00 per million tokens

**Cost Per Transformation**:
- Average PDF: 1,000-2,000 input tokens (image) + 500-1,000 output tokens (HTML)
- **Per PDF**: ~$0.01-0.03
- **30 bookings/month**: ~$10-30
- **100 bookings/month**: ~$30-90
- **No maintenance costs**: No regex patterns to update

## Booking Scenarios Supported

The system intelligently handles **4 booking scenarios**:

### 1. Direct Booking, Single Room

- Standard guest booking
- Guest info + property details layout
- Payment status section (yellow/blue/green)
- Most common scenario

### 2. Direct Booking, Multiple Rooms (1-3 rooms)

- Family or group bookings with multiple rooms
- Single yellow overview box with check-in/check-out dates
- Compact room cards (3-column: Adults | Children | Rate/Night)
- Pricing breakdown lists all rooms separately
- Optimized spacing to fit on single A4 page

### 3. Agent Booking, Single Room

- Travel agency or tour operator booking
- Guest info (left) + Agent info (right) layout
- Agent fields: agent name, contact, email, tour reference, voucher number
- Billing status section (blue theme) instead of payment status
- Flexible billing labels for agent invoicing

### 4. Agent Booking, Multiple Rooms (1-3 rooms)

- Combines agent + multi-room features
- Compact multi-room layout with agent billing
- Tour reference and voucher prominently displayed
- All rooms listed in pricing section

### Automatic Detection

Claude API automatically detects:

- **Booking type**: Looks for agent name, tour reference, voucher → "agent" or "direct"
- **Room count**: Counts distinct rooms with separate rates → generates array
- **Agent details**: Extracts all agent-specific fields if present

## Key Design Constraints

### A4 Page Fitting (Critical)
- All confirmations must fit on a single A4 page when printed
- Design uses **95% scale** in Adobe Acrobat to achieve proper fit
- Container width: 760px (reduced from 800px)
- Logo size: 65px (optimized from 120px original)
- Line height: 1.3 (reduced from 1.6)
- Font sizes scaled down by ~5% across all elements

### Visual Hierarchy
- **Two-column layout** for guest/booking information (not three - middle column becomes too cramped)
- **15px margin-top** between yellow date box and detail cards for visual breathing room
- Side-by-side pricing and payment sections

## Template Structure

Each HTML file is self-contained with inline CSS and includes:

1. **Header**: Peacock logo (65px), hotel name, confirmation number
2. **Guest Info Grid** (left column): Name, email, phone, nationality
3. **Booking Info Grid** (right column): Reserved on, booking via, reference, contact details
4. **Accommodation Section**: Room name, yellow date box, detail cards (Adults/Children/Nights/Total Rate)
5. **Pricing/Payment** (side-by-side): Itemized charges left, payment status right
6. **Footer**: Cancellation policy, check-in/out times

## Color Coding System

Payment status boxes use specific colors:
- **Yellow (#fff3cd)**: Unpaid
- **Light Blue (#d1ecf1)**: Partially paid
- **Green (planned)**: Fully paid

## Workflow Methods

### Primary: Claude API Transformation (3-5 seconds)

1. **Command line**: `python claude_transform.py --input "cloudbeds.pdf"`
2. **Web interface**: `python web_interface.py` → Drag & drop PDF
3. **Power Automate**: Monitors folder → Calls Claude API → Saves result
4. **Batch processing**: Place PDFs in `inbox/` → run `python batch_transform.py`

The Claude API:

- Reads the PDF using vision capabilities
- Extracts all booking data intelligently
- Generates complete branded HTML
- Handles any PDF format variations automatically
- No regex patterns to break or maintain

### Backup: Manual Template Editing (if API unavailable)

1. Copy template from `.sample code/` (e.g., `meagan_confirmation_95_PERCENT.html`)
2. Update guest details, dates, and pricing manually
3. Adjust payment status class (`.payment-status` or `.payment-status.partial-paid`)
4. Ensure logo path is `../planters-logo.png` from subdirectories

### Browser Compatibility
- Optimized for Chrome (recommended for PDF generation)
- Print testing should always use Chrome's print dialog

### Testing Print Output
```bash
# Open HTML in Chrome and use Print Preview (Ctrl+P)
# Settings: A4, Minimum margins, Background graphics enabled
# Must show at 95% scale in Adobe Acrobat
```

### Font Requirements
Templates use Google Fonts:
- **Playfair Display**: Headers and titles (serif, elegant)
- **Source Sans Pro**: Body text (sans-serif, readable)

## Common Modifications

### Booking Scenarios
- **Standard multi-night**: Use `.sample code/andrew_morris_updated_design.html` as base
- **Single night exception**: Based on `.sample code/meagan_confirmation_deposit_paid.html` (note: exception message removed to avoid highlighting policy breach)
- **Family with children**: Use `.sample code/joachim_confirmation_two_column.html` showing child charges

### Spacing Adjustments
If confirmation doesn't fit on one page:
- Reduce font sizes proportionally (maintain hierarchy)
- Decrease padding/margins systematically
- Verify 95% scale still works in print preview

## Common Issues

### Quick Troubleshooting
- **Text overflow**: Reduce guest name/email font size before adjusting layout
- **Payment box misalignment**: Check grid gap hasn't been changed from 25px (info-grid) or side-by-side spacing
- **Logo missing**: Verify path to planters-logo.png (use `../planters-logo.png` from `.sample code/` directory)
- **Content doesn't fit A4**: Ensure container width is 760px and all scale reductions are applied
- **Print cuts off content**: Check Chrome print settings for minimum margins and A4 paper size

## File Organization

```
/
├── claude_transform.py                        # Main Claude API transformation script
├── web_interface.py                          # Web UI for drag & drop
├── batch_transform.py                        # Batch processing script
├── .env                                      # API keys (not in git)
├── .env.example                              # Template for API configuration
├── templates/                                # HTML template library
│   ├── guest/
│   │   ├── single_room.html                  # Direct booking, 1 room
│   │   └── multiroom.html                    # Direct booking, 2-3 rooms
│   └── agent/
│       ├── single_room.html                  # Agent booking, 1 room
│       └── multiroom.html                    # Agent booking, 2-3 rooms
├── docs/
│   ├── booking_confirmation_documentation.md  # Design decisions and evolution
│   └── MULTIROOM_TEMPLATE_GUIDE.md           # Multi-room template guide
├── .sample code/
│   └── meagan_confirmation_95_PERCENT.html   # Reference template
├── .reference/
│   ├── Before/                               # Original Cloudbeds confirmations (PDF)
│   └── After/                                # Custom HTML confirmations (PDF)
├── .old/                                     # Deprecated files (old extraction methods)
├── inbox/                                    # Drop PDFs here for processing
├── output/                                   # Generated confirmations appear here
└── planters-logo.png                         # Peacock logo (65px display)
```

## Environment Setup

### API Configuration

1. Create `.env` file from template:

   ```bash
   cp .env.example .env
   ```

2. Add your Claude API key:

   ```env
   ANTHROPIC_API_KEY=your_api_key_here
   ```

3. Get API key from: <https://console.anthropic.com/>

### Dependencies

```bash
pip install anthropic pdf2image pillow python-dotenv
```

## Important Notes

- **API Key Security**: Never commit `.env` to git (already in .gitignore)
- Logo path in HTML must be adjusted based on template location (use `../planters-logo.png` from subdirectories)
- All CSS is inline (no external stylesheets)
- No JavaScript required
- Templates optimized for PDF generation via browser print
- Letter spacing crucial for premium appearance (especially uppercase text)
- Reference PDFs available in `.reference/Before/` (original) and `.reference/After/` (custom)
- Claude API intelligently handles all extraction and generation - no manual pattern updates needed

## Template Version

Current version: 4.0 (Multi-room and agent booking support)
Last updated: November 2024

### Version History

- **v4.0** (Nov 2024): Added multi-room and agent booking support with automatic detection
- **v3.0** (Nov 2024): Claude API-powered intelligent extraction and generation
- **v2.0** (Nov 2024): Two-column design, 95% scale optimized
- **v1.0** (Earlier): Initial manual template