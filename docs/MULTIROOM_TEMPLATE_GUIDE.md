# Multi-Room Agent Confirmation Template Guide

## Template: `agent_confirmation_multiroom.html`

## Design Changes for Multi-Room Support

### 1. Stay Overview (Yellow Box)
Moved check-in/check-out dates to **single yellow box** at top of accommodation section.
- Avoids repeating dates for each room
- Shows total nights once
- Cleaner, more compact

### 2. Compact Room Sections
Each room gets a condensed card:
- Room name + total rate in header
- 3-column layout (not 4): Adults | Children | Rate/Night
- Removed duplicate "Nights" column (shown once in overview)
- Smaller padding (12px vs 15px)
- Smaller fonts (16px title vs 18px)

### 3. Dynamic Room Sections
```html
<!-- Room 1 - Always present -->
<div class="room-section">...</div>

<!-- Room 2 - Use {{ROOM_2_SECTION}} variable -->
{{ROOM_2_SECTION}}

<!-- Room 3 - Use {{ROOM_3_SECTION}} variable -->
{{ROOM_3_SECTION}}
```

If booking has 1 room: Set `ROOM_2_SECTION = ""` and `ROOM_3_SECTION = ""`
If booking has 2 rooms: Populate `ROOM_2_SECTION`, set `ROOM_3_SECTION = ""`
If booking has 3 rooms: Populate both

### 4. Dynamic Pricing Rows
Use `{{PRICING_ROWS}}` variable to inject room-specific pricing:

```python
# Single room example
PRICING_ROWS = """
<div class="price-row">
    <span class="price-label">Sunbird Suite (2 nights)</span>
    <span class="price-value">USD 296.10</span>
</div>
<div class="price-row">
    <span class="price-label">Children's Accommodation</span>
    <span class="price-value">Included</span>
</div>
<div class="price-row">
    <span class="price-label">Breakfast, WiFi, Taxes & Service</span>
    <span class="price-value">Included</span>
</div>
"""

# Multi-room example
PRICING_ROWS = """
<div class="price-row">
    <span class="price-label">Sunbird Suite (2 nights)</span>
    <span class="price-value">USD 296.10</span>
</div>
<div class="price-row">
    <span class="price-label">Oriole Room (2 nights)</span>
    <span class="price-value">USD 220.00</span>
</div>
<div class="price-row">
    <span class="price-label">Children's Accommodation</span>
    <span class="price-value">Included</span>
</div>
<div class="price-row">
    <span class="price-label">Breakfast, WiFi, Taxes & Service</span>
    <span class="price-value">Included</span>
</div>
"""
```

## All Variables

### Shared Variables
- `{{CONFIRMATION_NUMBER}}`
- `{{GUEST_NAME}}`
- `{{GUEST_EMAIL}}`
- `{{GUEST_PHONE}}`
- `{{NATIONALITY}}`
- `{{AGENT_NAME}}`
- `{{AGENT_CONTACT}}`
- `{{AGENT_EMAIL}}`
- `{{TOUR_REFERENCE}}`
- `{{VOUCHER_NUMBER}}`

### Stay Overview
- `{{CHECK_IN_DATE}}` - e.g., "Wednesday, 1 January 2026"
- `{{CHECK_OUT_DATE}}`
- `{{NIGHTS}}` - Number only (e.g., "2")

### Room 1 (Always Required)
- `{{ROOM_1_NAME}}` - e.g., "The Sunbird Suite"
- `{{ROOM_1_RATE}}` - Total for this room (e.g., "296.10")
- `{{ROOM_1_ADULTS}}` - Number (e.g., "2")
- `{{ROOM_1_CHILDREN}}` - Number (e.g., "2")
- `{{ROOM_1_PER_NIGHT}}` - Per night rate (e.g., "148.05")

### Room 2 (Optional)
- `{{ROOM_2_SECTION}}` - Full HTML block or empty string
- If populated, needs: ROOM_2_NAME, ROOM_2_RATE, ROOM_2_ADULTS, ROOM_2_CHILDREN, ROOM_2_PER_NIGHT

### Room 3 (Optional)
- `{{ROOM_3_SECTION}}` - Full HTML block or empty string
- If populated, needs: ROOM_3_NAME, ROOM_3_RATE, ROOM_3_ADULTS, ROOM_3_CHILDREN, ROOM_3_PER_NIGHT

### Pricing
- `{{PRICING_ROWS}}` - Full HTML with all price-row divs
- `{{TOTAL_RATE}}` - Grand total (e.g., "296.10")

### Notes
- `{{INCLUSIONS_NOTE}}` - Green box
- `{{GUEST_RESPONSIBILITY}}` - Yellow box

### Billing (All Flexible)
- `{{BILLING_TITLE}}`
- `{{BILLING_LABEL_1}}` through `{{BILLING_LABEL_4}}`
- `{{BILLING_VALUE_1}}` through `{{BILLING_VALUE_4}}`
- `{{INVOICE_NOTE}}`

## Room 2/3 Section Template

```python
ROOM_2_SECTION = """
<div class="room-section">
    <div class="room-header">
        <h2 class="room-title">{ROOM_2_NAME}</h2>
        <span class="room-rate">USD {ROOM_2_RATE}</span>
    </div>
    <div class="room-details">
        <div class="detail-box">
            <div class="detail-label">Adults</div>
            <div class="detail-value">{ROOM_2_ADULTS}</div>
        </div>
        <div class="detail-box">
            <div class="detail-label">Children</div>
            <div class="detail-value">{ROOM_2_CHILDREN}</div>
        </div>
        <div class="detail-box">
            <div class="detail-label">Rate/Night</div>
            <div class="detail-value">${ROOM_2_PER_NIGHT}</div>
        </div>
    </div>
</div>
"""
```

## A4 Fit Testing

### Max Capacity
- 1 room: Comfortable fit
- 2 rooms: Tight but fits at 95% print scale
- 3 rooms: Maximum - test carefully, may need font reduction

### If 3 Rooms Don't Fit
Reduce in this order:
1. Room section padding: 12px → 10px
2. Room title font: 16px → 15px
3. Pricing section padding: 15px → 12px
4. Info-grid margin-bottom: 20px → 15px

## Example: Parents + Kids in Separate Rooms

```python
ROOM_1_NAME = "The Sunbird Suite"
ROOM_1_RATE = "296.10"
ROOM_1_ADULTS = "2"
ROOM_1_CHILDREN = "0"
ROOM_1_PER_NIGHT = "148.05"

ROOM_2_SECTION = """
<div class="room-section">
    <div class="room-header">
        <h2 class="room-title">The Bunk Room</h2>
        <span class="room-rate">USD 0.00</span>
    </div>
    <div class="room-details">
        <div class="detail-box">
            <div class="detail-label">Adults</div>
            <div class="detail-value">0</div>
        </div>
        <div class="detail-box">
            <div class="detail-label">Children</div>
            <div class="detail-value">2</div>
        </div>
        <div class="detail-box">
            <div class="detail-label">Rate/Night</div>
            <div class="detail-value">Included</div>
        </div>
    </div>
</div>
"""

ROOM_3_SECTION = ""

PRICING_ROWS = """
<div class="price-row">
    <span class="price-label">Sunbird Suite (2 nights)</span>
    <span class="price-value">USD 296.10</span>
</div>
<div class="price-row">
    <span class="price-label">Bunk Room (2 nights)</span>
    <span class="price-value">Complimentary</span>
</div>
<div class="price-row">
    <span class="price-label">Breakfast, WiFi, Taxes & Service</span>
    <span class="price-value">Included</span>
</div>
"""
```
