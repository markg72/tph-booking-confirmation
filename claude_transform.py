#!/usr/bin/env python3
"""
Claude API-Powered Booking Confirmation Transformer
Converts Cloudbeds PDFs to branded The Planters House confirmations
"""

import os
import sys
import argparse
import base64
from pathlib import Path
from datetime import datetime, timedelta
from dotenv import load_dotenv
from anthropic import Anthropic
from pdf2image import convert_from_path
from io import BytesIO
import json

# Load environment variables
load_dotenv()

class CloudbedsTransformer:
    """Transform Cloudbeds PDFs using Claude API vision and generation"""

    def __init__(self, api_key=None, debug=False):
        """Initialize transformer with Claude API"""
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment or .env file")

        self.client = Anthropic(api_key=self.api_key)
        self.debug = debug
        self.output_dir = Path('output')
        self.output_dir.mkdir(exist_ok=True)

    def pdf_to_images(self, pdf_path):
        """Convert PDF to images for Claude vision"""
        if self.debug:
            print(f"Converting PDF to images: {pdf_path}")

        images = convert_from_path(pdf_path, dpi=200)
        return images

    def image_to_base64(self, image):
        """Convert PIL image to base64 string"""
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')

    def extract_booking_data(self, pdf_path):
        """Extract booking data from PDF using Claude vision"""
        if self.debug:
            print("Extracting booking data with Claude vision...")

        # Convert PDF to images
        images = self.pdf_to_images(pdf_path)

        # Prepare image content for Claude
        image_content = []
        for idx, img in enumerate(images):
            image_content.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": self.image_to_base64(img)
                }
            })

        # Create extraction prompt
        extraction_prompt = """You are analyzing a Cloudbeds booking confirmation PDF.
Extract ALL booking information and return it as a JSON object with these exact fields:

{
  "booking_type": "direct|agent",
  "guest_name": "Full guest name",
  "email": "Guest email address",
  "phone": "Guest phone number with country code",
  "mobile": "Guest mobile number (if different from phone, otherwise same as phone)",
  "primary_contact": "Primary contact person name (if specified, otherwise same as guest_name)",
  "nationality": "Guest nationality (if available, otherwise 'Not specified')",
  "res_id": "Reservation ID number",
  "check_in": "Check-in date in DD/MM/YYYY format",
  "check_out": "Check-out date in DD/MM/YYYY format",
  "nights": "Number of nights (as number)",
  "rooms": [
    {
      "room_name": "Room/suite name",
      "adults": "Number of adults (as number)",
      "children": "Number of children (as number)",
      "rate_per_night": "Per night rate (number only)",
      "total_rate": "Total for this room (number only)"
    }
  ],
  "total_amount": "Grand total for all rooms (number only, no currency)",
  "deposit_amount": "Deposit required (number only)",
  "amount_paid": "Amount already paid (number only)",
  "balance_due": "Balance remaining (number only)",
  "reserved_date": "Date booking was made (if available)",
  "booking_via": "Booking source - look for 'Travel Agent' field (e.g., 'Direct', 'Booking.com', 'Expedia')",
  "heard_about": "Marketing source - look for 'How did you hear about us?' field (e.g., 'TBC', 'Google', 'Referral')",
  "agent_info": {
    "agent_name": "Agent/company name (if agent booking)",
    "agent_contact": "Agent contact person (if applicable)",
    "agent_email": "Agent email (if applicable)",
    "tour_reference": "Tour reference number (if applicable)",
    "voucher_number": "Voucher number (if applicable)"
  }
}

IMPORTANT DETECTION RULES:
1. BOOKING TYPE:
   - Set to "agent" if you find: agent name, tour operator, travel agency, voucher number, or tour reference
   - Set to "direct" otherwise

2. MULTI-ROOM DETECTION:
   - If multiple rooms listed with separate rates, create separate entries in rooms array
   - Each room gets its own object with name, adults, children, and rates
   - Grand total_amount is sum of all room totals

3. AGENT INFO:
   - Only populate agent_info if booking_type is "agent"
   - Leave fields as null or empty if not applicable

4. DATA INFERENCE:
   - Return ONLY valid JSON, no markdown formatting
   - Calculate nights from dates if not shown
   - If deposit not specified, use 50% of total
   - All monetary values should be numbers without currency symbols
   - Infer booking_via from email domain or explicit mentions"""

        # Send to Claude API
        message = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2048,
            messages=[{
                "role": "user",
                "content": image_content + [{
                    "type": "text",
                    "text": extraction_prompt
                }]
            }]
        )

        # Parse response
        response_text = message.content[0].text

        if self.debug:
            print(f"Claude response:\n{response_text}")

        # Extract JSON from response
        try:
            # Remove markdown code blocks if present
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()

            booking_data = json.loads(response_text)
            return booking_data
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON response: {e}")
            print(f"Response was: {response_text}")
            raise

    def generate_html(self, booking_data):
        """Generate branded HTML using Claude with design constraints"""
        if self.debug:
            print("Generating branded HTML with Claude...")

        # Determine booking type and room count
        booking_type = booking_data.get('booking_type', 'direct')
        rooms = booking_data.get('rooms', [])
        room_count = len(rooms)

        # Load template reference (if exists) or use embedded design rules
        design_rules = """
CRITICAL DESIGN CONSTRAINTS (must follow exactly):

1. BRANDING (MUST USE EXACT DETAILS):
   - Hotel Name: "The Planters House"
   - Logo: planters-logo.png (65px width)
   - Address: Monarakanda Estate, Koslanda, Sri Lanka
   - Phone: +94 77 683 6955
   - Email: reservations@theplantershouse.com
   - Website: www.theplantershouse.com
   - DO NOT include VAT numbers or UK details

2. A4 PAGE FITTING:
   - Container max-width: 760px
   - Logo width: 65px
   - Scale: 95% for perfect A4 fit
   - Line-height: 1.3
   - For 2-3 rooms: reduce padding to maintain A4 fit

3. LAYOUT STRUCTURE:
   - Two-column grid for guest/booking info (NOT three columns)
   - Side-by-side pricing and payment sections
   - For multi-room: single yellow box with check-in/check-out dates (don't repeat per room)
   - For multi-room: compact room cards with 3 columns (Adults | Children | Rate/Night)

4. COLOUR PALETTE (Tea Estate Theme):
   - Primary headers and borders: #264b3a (deep tea green)
   - Accent backgrounds for payment boxes: #f6f1e9 (warm cream)
   - Inclusion/information boxes background: #9caf88 (sage)
   - Gold highlights and accents: #b89b5e (muted gold)
   - Information box text: #ffffff (white for contrast on sage)
   - Body text: #6b6b6b (soft grey) on white backgrounds
   - Body text: #333333 (dark grey) ONLY on cream #f6f1e9 backgrounds for higher contrast
   - White backgrounds: #ffffff

   Payment Status Colors:
   - Unpaid (balance = total): #f6f1e9 background, #b89b5e border
   - Partial payment (0 < balance < total): #f6f1e9 background, #b89b5e border
   - Fully paid (balance = 0): #9caf88 background, #264b3a border

5. TYPOGRAPHY (Brand Compliance):
   - Headers: Playfair Display (serif, elegant) - Google Fonts
   - Body: System sans-serif stack (NO web fonts for body)
   - Body font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif
   - Import ONLY Playfair Display from Google Fonts
   - DO NOT import Source Sans Pro or any other body text fonts
   - Reason: Fast loading, excellent readability, native to OS

6. BOOKING TYPE-SPECIFIC LAYOUTS:

   A. DIRECT BOOKINGS (booking_type = "direct"):
      - Guest info (left) | Booking Information (right)
      - Guest info MUST include: Name, Email, Phone, Mobile (if different), Nationality
      - Booking Information MUST include: Reserved On (reserved_date), Booking Via (booking_via), Reference (heard_about), Contact (+94 77 683 6955), Email (reservations@theplantershouse.com)
      - Standard payment status section
      - Check-in/check-out times in footer

   B. AGENT BOOKINGS (booking_type = "agent"):
      - Guest info (left) | Agent info (right)
      - Guest info MUST include: Name, Email, Phone, Nationality
      - Agent info includes: agent name, contact, email, tour reference, voucher number
      - Billing status section instead of payment status
      - Use sage box styling for agent section

7. MULTI-ROOM HANDLING (if rooms array has 2-3 items):
   - Show dates ONCE in three-column date grid (see DATE DISPLAY section)
   - Each room gets compact card: Room name + total | Adults | Children | Rate/Night
   - Pricing section lists all rooms separately
   - Reduce spacing/padding to fit on A4

8. STYLES:
   - All CSS inline (no external stylesheets)
   - No JavaScript
   - Professional letter spacing for uppercase text
   - Minimal padding/margins for A4 fit

9. FOOTER (exactly two lines):
   Line 1: "Please review our cancellation policy and payment terms above."
   Line 2: "The Planters House | +94 (0)77 683 6955 | reservations@theplantershouse.com | www.theplantershouse.com"

10. INFORMATION BOXES:
   Important policies and information should use sage-colored boxes:
   - Background: #9caf88 (sage)
   - Border-left: 3px solid #264b3a (deep tea green)
   - Text color: #ffffff (white for contrast)
   - Padding: 12px 16px
   - Border-radius: 4px
   - Margin-bottom: 12px
   - No bullet points - use paragraph format within divs
   - Each policy item is a separate box

11. DATE DISPLAY (Three-Column Grid - REQUIRED):
   Use a three-column table/grid layout for check-in/check-out dates:

   Structure: Check-in | Check-out | Nights

   CSS Grid Implementation:
   - Container: display: grid; grid-template-columns: 1fr 1fr 1fr;
   - Border: 1px solid #e0e0e0

   Header Row Styling:
   - Background: #9caf88 (sage)
   - Text color: #264b3a (deep tea green)
   - Font-weight: bold
   - Padding: 10px
   - Border-bottom: 2px solid #264b3a
   - Text-align: center

   Data Row Styling:
   - Background: #ffffff (white)
   - Text color: #333333 (dark grey)
   - Padding: 12px
   - Text-align: center
   - Border-right: 1px solid #e0e0e0 (between columns)

   Date Format: DD/MM/YYYY (e.g., 25/11/2025)

   FORBIDDEN:
   - Yellow background boxes (#fff8e1, #fff9e6, #fff3cd)
   - Four-item horizontal layouts with arrows
   - Single-line date ranges with pipe separators
   - Any layout other than three-column grid
"""

        # Add specific instructions based on booking scenario
        scenario_instructions = ""
        if booking_type == "agent":
            scenario_instructions = f"""
AGENT BOOKING INSTRUCTIONS:
- This is an AGENT booking for a tour operator or travel agency
- Include agent information section with: {booking_data.get('agent_info', {})}
- Use sage box styling for agent section: #9caf88 background, #264b3a border-left, #ffffff text
- Agent section should include: Agent Company, Contact Person, Tour Reference, Agent Email
- Position agent section after guest details, before room details
- Use billing status section instead of payment status (same sage styling)
"""

        if room_count > 1:
            scenario_instructions += f"""
MULTI-ROOM BOOKING INSTRUCTIONS:
- This booking has {room_count} rooms
- Show check-in/check-out dates ONCE in three-column date grid (NOT yellow box)
- Create separate compact cards for each room
- List all {room_count} rooms in pricing breakdown
- Ensure everything fits on single A4 page (reduce padding if needed)
"""

        generation_prompt = f"""Generate a complete, self-contained HTML file for a hotel booking confirmation using this data:

{json.dumps(booking_data, indent=2)}

{design_rules}

{scenario_instructions}

REQUIREMENTS:
1. Return ONLY the complete HTML (<!DOCTYPE html> to </html>)
2. No markdown code blocks or explanations
3. All CSS must be inline
4. Font imports: Import ONLY Playfair Display from Google Fonts
   Example: <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
   DO NOT import Source Sans Pro or any other body text fonts
5. Logo path: "planters-logo.png" (NOT ../../planters-logo.png)
6. Hotel branding MUST be: "The Planters House" (NOT Planters Country Hotel)
7. Contact details MUST be: +94 77 683 6955, reservations@theplantershouse.com, www.theplantershouse.com
8. Must fit on single A4 page when printed at 95% scale
9. Apply correct payment/billing status color based on balance_due
10. Format dates nicely (e.g., "Monday, 25 November 2025")
11. Calculate balance due date as 14 days before check-in
12. For agent bookings: use sage billing section, include agent fields
13. For multi-room bookings: use compact layout, show dates once in three-column grid
14. Include all design constraints above
15. Footer contact line format: "reservations@theplantershouse.com | +94 77 683 6955 | www.theplantershouse.com"
16. Body text MUST use system sans-serif stack (not web fonts)
17. Date display MUST use three-column grid with sage header (not yellow boxes or horizontal layout)
18. Body text color: #6b6b6b on white backgrounds, #333333 on cream #f6f1e9 backgrounds only

Generate the complete HTML now:"""

        # Send to Claude API
        message = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=8192,
            messages=[{
                "role": "user",
                "content": generation_prompt
            }]
        )

        html_content = message.content[0].text

        # Clean up if Claude wrapped in markdown
        if "```html" in html_content:
            html_content = html_content.split("```html")[1].split("```")[0].strip()
        elif "```" in html_content:
            html_content = html_content.split("```")[1].split("```")[0].strip()

        return html_content

    def save_outputs(self, booking_data, html_content):
        """Save HTML and optionally convert to PDF"""
        res_id = booking_data.get('res_id', 'unknown')

        # Save HTML
        html_path = self.output_dir / f"{res_id}_confirmation.html"
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        if self.debug:
            print(f"Saved HTML to: {html_path}")

        return html_path

    def transform(self, pdf_path):
        """Main transformation workflow"""
        print(f"Transforming: {pdf_path}")

        # Step 1: Extract data
        booking_data = self.extract_booking_data(pdf_path)

        # Show detection results
        booking_type = booking_data.get('booking_type', 'direct')
        rooms = booking_data.get('rooms', [])
        room_count = len(rooms)
        guest_name = booking_data.get('guest_name', 'Unknown')

        print(f"✓ Extracted data for: {guest_name}")
        print(f"  - Booking type: {booking_type.upper()}")
        print(f"  - Rooms: {room_count}")

        if booking_type == "agent":
            agent_name = booking_data.get('agent_info', {}).get('agent_name', 'N/A')
            print(f"  - Agent: {agent_name}")

        if room_count > 1:
            for idx, room in enumerate(rooms, 1):
                print(f"    Room {idx}: {room.get('room_name', 'Unknown')}")

        # Step 2: Generate HTML
        html_content = self.generate_html(booking_data)
        template_type = f"{booking_type}/{room_count}-room"
        print(f"✓ Generated branded HTML ({template_type})")

        # Step 3: Save outputs
        html_path = self.save_outputs(booking_data, html_content)
        print(f"✓ Saved to: {html_path}")

        print("\n🎉 Transformation complete!")
        print(f"   Open {html_path} in Chrome and print to PDF (Ctrl+P)")
        print(f"   Settings: A4, Minimum margins, 95% scale in Adobe")

        return html_path


def main():
    """Command-line interface"""
    parser = argparse.ArgumentParser(
        description="Transform Cloudbeds PDFs to branded confirmations using Claude AI"
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Path to Cloudbeds PDF file'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug output'
    )

    args = parser.parse_args()

    # Validate input file
    pdf_path = Path(args.input)
    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}")
        sys.exit(1)

    if not pdf_path.suffix.lower() == '.pdf':
        print(f"Error: File must be a PDF: {pdf_path}")
        sys.exit(1)

    # Transform
    try:
        transformer = CloudbedsTransformer(debug=args.debug)
        transformer.transform(pdf_path)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
