---
nombre: Prompt Para Magic Patterns
tipo: prompt
anadido: 2026-08-10
---

# Prompt Para Magic Patterns

> Detecta nicho y avatar desde el sales copy y genera la landing page con paleta y UI acordes.

---

Act as a World-Class UI/UX Designer and Frontend Developer specialized in High-Converting Landing Pages.

# 1. DESIGN INTELLIGENCE (AUTO-DETECT)
I am providing you with the full Sales Copy for a product below.
**Your task is to analyze the text to determine the specific Niche and User Avatar.**
Based on that analysis, you must **automatically select**:
- **Color Palette:** Choose colors that evoke the right emotion for this niche (e.g., Trust, Excitement, Calm, Luxury, or Urgency).
- **Typography:** Choose a font pairing (Header/Body) that fits the industry standards for this specific product.
- **Imagery Style:** Use placeholders that match the context of the copy.

# 2. TECHNICAL SPECS & SHOPIFY LOGIC
- **Tech Stack:** React + Tailwind CSS.
- **Mobile-First:** The design must be fully responsive and optimized for scrolling on phones.
- **Dynamic Currency Logic:** Implement a `PriceDisplay` component. This component should simulate **Shopify Markets** behavior: it must use a basic JS script to detect the user's browser locale (`navigator.language`) and display the appropriate currency symbol (e.g., $, €, £) next to the price.
- **Cart Integration:** ALL Call-to-Action (CTA) buttons must link to: `[CART_LINK]`

# 3. PAGE ARCHITECTURE (Long-Form Structure)
Create the layout following this specific "Direct Response" sequence:

## A. STICKY ALERT BAR
- Top of the page. High contrast. Urgent message from the copy.

## B. HERO SECTION (The Hook)
- Layout: 2-Columns on Desktop, Stacked on Mobile.
- Content: Main Headline, Subheadline, and a compelling Hero Image/Video Placeholder.
- Trust: "Verified Purchase" badges or Star Ratings visible immediately.

## C. THE "SALES LETTER" CONTAINER
- A centered content area (max-width: 800px) designed for readability.
- This section contains the main body of the story/pitch.
- **Styling:** Use distinct styling for "Pain Points" (e.g., red bullets) and "Solutions" (e.g., green checks).

## D. THE "WHAT YOU GET" STACK
- Visual breakdown of the product components.
- Layout: Alternating image/text or a Grid of features.

## E. THE BONUS SECTION (Crucial Value Stack)
- A distinct section with a higher perceived value design (e.g., gold borders or distinct background).
- **Vertical Stack:** List the bonuses vertically.
- Elements: Bonus Image thumbnail + Title + Description + "Value: $XX (FREE)".
- **Total Value Box:** A summary box at the bottom showing the total value crossed out vs. the free offer.

## F. DYNAMIC PRICING OFFER
- The main conversion section.
- Display the **Dynamic Currency** price (based on the logic defined in step 2).
- Visuals: Product Mockup + Huge Discount Badge.
- Primary CTA Button: Large, full-width on mobile. Links to `[CART_LINK]`.
- Trust Elements: Secure Checkout icons / Payment Logos below the button.

## G. SOCIAL PROOF & FOOTER
- Masonry Grid for Testimonials (Text + Star Rating + User Photo).
- Simple Footer with Copyright and Links.

# 4. CONTENT SOURCE (The Source of Truth)
Populate the structure above using EXACTLY the text provided below. Do not use Lorem Ipsum; use the real copy.

[PASTE YOUR FULL SALES COPY HERE]

GENERATE THE HIGH-CONVERTING DESIGN NOW.
