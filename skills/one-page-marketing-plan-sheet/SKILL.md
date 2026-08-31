---
name: one-page-marketing-plan-sheet
description: Interview the user through Allan Dib's 1-Page Marketing Plan (the Before / During / After customer journey, three squares each) and build a formatted Google Sheet laid out as that 3x3 grid, filled with their answers. Use when the user wants a marketing plan, a "1-page marketing plan", or to turn the book's framework into a living spreadsheet they can keep and revisit.
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

1. **Explain the grid** in two sentences, then interview the user square by
   square, in order. Ask focused questions; keep each answer to a few bullets.
   Don't move on until a square has a concrete answer (or an explicit "skip").
   - **1. Target market** — Who exactly is this for? Niche down. Demographics,
     situation, the specific pain. ("everyone" is not an answer.)
   - **2. Message** — What do you say to that market? The offer, the promise,
     what makes you different, the emotional hook.
   - **3. Media** — Where will you reach them? The specific channels the target
     market actually uses (not where it's easy for you to post).
   - **4. Capture leads** — How do you collect contact details? Lead magnet,
     landing page, the CRM/list where they land.
   - **5. Nurture leads** — How do you build trust over time before the sale?
     Email sequence, content, cadence.
   - **6. Sales conversion** — How does a nurtured lead become a paying
     customer? The offer, pricing, the mechanism that reduces risk.
   - **7. World-class experience** — How do you deliver so well they become
     fans? Onboarding, the "wow" moments, what you'll systematize.
   - **8. Lifetime value** — How do you increase what each customer is worth?
     Upsells, ascension, retention, raising prices, reactivation.
   - **9. Referrals** — How do you deliberately stimulate word of mouth? The
     ask, the incentive, making it easy to refer.

2. **Build the Google Sheet.** Create a new spreadsheet titled
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

3. **Fallback when you have no Google Sheets access:** produce the exact same 3x3
   as a CSV (or a Markdown table) and give the user the import steps —
   *Google Sheets → File → Import → Upload → Replace current sheet* — so they get
   the same artifact in under a minute. Never claim you created a Sheet you did
   not create.

4. **Hand it over.** Return the Sheet's share URL (or the CSV). Remind the user
   this is a living document — revisit it quarterly, and change one square at a
   time rather than rewriting the plan.

## Examples

- **Input:** "Help me make a 1-page marketing plan for my Flutter time-tracking
  app."
  **Expected:** The agent asks the nine sets of questions in order, then creates
  a Google Sheet titled "1-Page Marketing Plan — <app>" with a 3x3 grid
  (Before / During / After) whose cells hold the user's answers under each
  square's name, formatted and shared, and returns the link.

- **Input:** "I don't have Google Sheets connected."
  **Expected:** The agent runs the same interview and returns a CSV of the 3x3
  grid plus the three-step import instructions — not a fabricated Sheet link.
