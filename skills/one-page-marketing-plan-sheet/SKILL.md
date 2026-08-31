---
name: one-page-marketing-plan-sheet
description: Draft a first-pass of Allan Dib's 1-Page Marketing Plan from what's known about the business, refine it square by square with the user (the Before / During / After customer journey, three squares each), and build a formatted Google Sheet laid out as that 3x3 grid. Use when the user wants a marketing plan, a "1-page marketing plan", or to turn the book's framework into a living spreadsheet they can keep and revisit.
---

# One-Page Marketing Plan → Google Sheet

Turn Allan Dib's *The 1-Page Marketing Plan* into a real, editable Google Sheet:
a 3x3 grid of the nine squares, filled with the user's own answers, that they
keep as a living document.

The grid — three phases of the customer journey, three squares each:

| Phase | Square 1 | Square 2 | Square 3 |
|-------|----------|----------|----------|
| **Before** (prospect) | Target market | Message | Media |
| **During** (lead) | Capture leads | Nurture leads | Sales conversion |
| **After** (customer) | World-class experience | Lifetime value | Referrals |

## Instructions

Start from a draft, not a blank page — but get the foundation right first. A plan
built on the wrong assumption is worse than none.

1. **Set the assumptions with the user — don't guess these.** State your best read
   from context, then ask them to confirm or correct:
   - **The item** — what exactly is being marketed? One or two sentences.
   - **The sale** — what counts as a "conversion" here? Name it explicitly: a
     purchase, a subscription, a signup, a booked call, a contribution? What does
     the business actually want people to *do* or *buy*? If there's a longer-term
     **business model** (e.g. "free now, sell to companies later"), write it down —
     it reshapes squares 4–9. Don't move on until the user agrees what "the sale"
     is; everything downstream depends on it.
2. **Draft all nine squares from that context** — a concrete proposed answer in
   every square — and show it as a starting draft the user will edit.
3. **Refine square by square with the user.** For each square, give a one-line
   plain-language explanation first (assume they are *not* a marketer), then your
   proposed answer, then let them correct. Push back on vagueness.
   - **1. Target market** — *who, exactly, this is for.* Niche down: the specific
     person, their situation, the pain. ("everyone" is not an answer.)
   - **2. Message** — *what you say to that market.* The offer, the promise, what
     makes you different, the hook that makes them care.
   - **3. Media** — *where you'll reach them* — the specific channels/platforms the
     target actually uses (not where it's easy for you to post).
   - **4. Capture leads** — *how you get a way to contact interested people.* A
     "lead" is someone who showed interest and gave you a way to reach them (a
     follow, a signup, a star, an email). Name the mechanism and where they land.
   - **5. Nurture leads** — *how you build trust over time before asking for the
     sale.* The ongoing content/contact, and its cadence.
   - **6. Sales conversion** — *how an interested lead becomes the "sale" you
     defined in step 1.* The offer, the pricing/ask, and what reduces their risk.
   - **7. World-class experience** — *how you deliver so well they become fans.*
     Onboarding, the "wow" moments, what you'll systematize.
   - **8. Lifetime value** — *how you grow what each customer is worth over time.*
     Upsells, retention, higher tiers, reactivation.
   - **9. Referrals** — *how you deliberately get customers to bring others.* The
     ask, the incentive, and making it easy to refer.

4. **Build the Google Sheet.** Create a new spreadsheet titled
   `1-Page Marketing Plan — <business or product>`, using whatever Google Sheets
   capability you have, in this order of preference:
   - a Google Sheets / Docs MCP tool if one is available (e.g. a `createSpreadsheet`
     tool), or
   - the Google Sheets API via a client library such as `gspread` (Python), or
   - the `google-apps-script`/Sheets REST API you're configured for.

   Lay it out to mirror the grid: a title row, a header row
   `Phase | Square 1 | Square 2 | Square 3`, then three phase rows
   (Before / During / After). In each cell put the **square's name in bold**
   followed by the user's answer. Format it: bold the header row and phase
   column, tint each phase a different soft color, enable text wrapping, widen
   the columns, and freeze the header row. Add the guiding question as a light
   cell note where a square was skipped.

5. **Fallback when you have no Google Sheets access:** produce the exact same 3x3
   as a CSV (or a Markdown table) and give the user the import steps —
   *Google Sheets → File → Import → Upload → Replace current sheet* — so they get
   the same artifact in under a minute. Never claim you created a Sheet you did
   not create.

6. **Hand it over.** Return the Sheet's share URL (or the CSV). Remind the user
   this is a living document — revisit it quarterly, and change one square at a
   time rather than rewriting the plan.

## Examples

- **Input:** "Help me make a 1-page marketing plan for my Flutter time-tracking
  app."
  **Expected:** The agent first reads the repo/README (or asks 2–3 framing
  questions), drafts all nine squares as a starting point, and presents them.
  After the user refines each square, it creates a Google Sheet titled
  "1-Page Marketing Plan — <app>" with a 3x3 grid (Before / During / After)
  whose cells hold the final answers under each square's name, formatted and
  shared, and returns the link.

- **Input:** "I don't have Google Sheets connected."
  **Expected:** The agent runs the same interview and returns a CSV of the 3x3
  grid plus the three-step import instructions — not a fabricated Sheet link.
