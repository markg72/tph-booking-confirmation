# Changelog

All notable changes to The Planters House Booking Confirmation System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Web interface for drag-and-drop PDF transformation
- Batch processing with booking type filtering
- Email integration for agent bookings
- Multi-language support for international guests
- Power Automate integration for automated workflow

## [4.0.0] - 2024-11-15

### Added

- **Multi-room booking support** (1-3 rooms per confirmation)
- **Agent booking support** for travel agencies and tour operators
  - Agent information section with tour reference and voucher number
  - Billing status section (blue theme) instead of payment status
  - Flexible billing labels for agent invoicing
- **Automatic booking type detection**
  - Detects "direct" vs "agent" bookings from PDF content
  - Looks for agent name, tour operator, voucher number indicators
- **Automatic room count detection**
  - Extracts multiple rooms with individual rates
  - Creates rooms array with details for each room
- **Dynamic template selection**
  - 4 scenarios: direct/agent × single/multi-room
  - Claude API chooses appropriate layout automatically
- Template library organization:
  - `templates/guest/single_room.html` - Direct booking, 1 room
  - `templates/guest/multiroom.html` - Direct booking, 2-3 rooms
  - `templates/agent/single_room.html` - Agent booking, 1 room
  - `templates/agent/multiroom.html` - Agent booking, 2-3 rooms
- Multi-room template guide in `docs/MULTIROOM_TEMPLATE_GUIDE.md`

### Changed

- **Updated to Claude Sonnet 4.5** (`claude-sonnet-4-5-20250929`) - Latest model version
- **Enhanced Claude API extraction prompt** to detect booking type and multiple rooms
- **Enhanced Claude API generation prompt** with booking-type-specific instructions
- Improved output display to show detected booking type, room count, and agent name
- Reorganized file structure with dedicated `templates/` directory
- Updated logo paths to `../../planters-logo.png` from templates subdirectories
- Updated pricing information to reflect 2025 rates

### Fixed

- Multi-room confirmations now fit on single A4 page with compact layout
- Agent bookings properly show billing section instead of payment status

## [3.0.0] - 2024-11-15

### Added

- **Claude API integration** for intelligent PDF transformation
- Vision-based PDF reading (no brittle regex patterns)
- Automatic data extraction with context understanding
- Dynamic HTML generation following design constraints
- Self-healing capability when Cloudbeds changes PDF format
- Environment variable management with `.env` file
- `.env.example` template for API configuration
- `.gitignore` to protect API keys from version control

### Changed

- **BREAKING**: Replaced regex-based extraction with Claude Vision API
- Moved old extraction scripts to `.old/` folder:
  - `extract_and_generate.py.old`
  - `transform_cloudbeds_to_branded.py.old`
  - `web_interface.py.old`
  - `batch_transform.py.old`
- Updated `requirements.txt` to focus on Claude API dependencies
- Reduced dependencies from 50+ packages to 4 core packages
- Documentation rewritten to emphasize Claude API benefits

### Cost

- ~$0.01-0.03 per PDF transformation
- ~$10-30/month for 30 bookings
- No maintenance costs (no regex patterns to update)

## [2.2.0] - 2024-11-14

### Added

- PDF extraction workflow documentation
- Sample Python script for PDF data extraction
- OCR capability for scanned PDFs
- Confidence scoring for extraction accuracy
- Email attachment processing framework
- Folder watching for automatic processing

### Changed

- Prioritized PDF extraction over API integration (API unavailable)
- Updated requirements to include PDF processing libraries
- Reorganized workflow to use Cloudbeds PDFs as primary data source

## [2.1.0] - 2024-11-14

### Added

- Comprehensive documentation structure (README, CHANGELOG, TODO)
- `.reference/` directory with Before/After PDF examples
- `.sample code/` directory for template organization
- Quick troubleshooting guide in CLAUDE.md

### Changed

- Reorganized file structure with dedicated directories
- Updated logo path references for subdirectory usage

## [2.0.0] - 2024-11-01

### Changed

- **BREAKING**: Redesigned from three-column to two-column layout
  - Three-column middle section was too cramped for email addresses
  - Two columns provide better balance and readability
- Reduced all dimensions for A4 fitting:
  - Logo: 120px → 80px → 70px → final 65px
  - Container width: 800px → 760px
  - Line height: 1.6 → 1.4 → final 1.3
  - Font sizes: Scaled down ~5% across all elements
- Implemented 95% scale requirement for Adobe Acrobat
- Added 15px margin-top between yellow date box and detail cards

### Added

- Payment status color coding system:
  - Yellow (#fff3cd): Unpaid
  - Light Blue (#d1ecf1): Partially paid
  - Green (planned): Fully paid
- Visual checkmarks for paid deposits
- Side-by-side pricing and payment sections
- Chrome-specific print optimization

### Fixed

- A4 page overflow issues
- Payment status box alignment
- Print margin problems

### Removed

- "One-night exception approved" message (to avoid highlighting policy breach)

## [1.5.0] - 2024-10-26

### Added

- Deposit payment confirmation template (Meagan Gunn example)
- Balance due calculations
- Payment deadline highlighting

### Changed

- Updated payment status box styling for partial payments
- Enhanced visual hierarchy for payment information

## [1.0.0] - 2024-10-15

### Added

- Initial HTML template design
- Google Fonts integration (Playfair Display, Source Sans Pro)
- Peacock logo branding
- Guest information grid
- Booking details section
- Accommodation cards with dates
- Pricing breakdown
- Cancellation policy footer
- Manual confirmation generation process

### Features

- Professional boutique hotel appearance
- Brand-consistent design
- Clear information hierarchy
- Print-ready format
- Responsive column layout

## [0.1.0] - 2024-10-01

### Added

- Project inception
- Initial requirements gathering
- Analysis of Cloudbeds default confirmations

### Identified Issues

- Poor formatting in default system
- Mobile readability problems
- Lack of brand consistency
- A4 printing issues
- Unclear visual hierarchy

---

## Version Guidelines

- **Major version (X.0.0)**: Breaking changes to template structure or automation
- **Minor version (0.X.0)**: New features or significant improvements
- **Patch version (0.0.X)**: Bug fixes and minor adjustments

## Migration Notes

### From 1.x to 2.0
- Update all templates to use two-column layout
- Adjust logo references to 65px size
- Apply 95% scale in print settings
- Update container width to 760px maximum