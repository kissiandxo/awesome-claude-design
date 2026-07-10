# Gateway Mitsubishi — July Sales Event Ad Campaign

Website advertisement package for the Gateway Mitsubishi dealer site, built around two
Higgsfield **Elements** so every ad shows *our* car and *our* store:

| Element | Type | Higgsfield ID |
|---|---|---|
| `@Outlander-exceed` | prop (white Outlander Exceed, black contrast roof) | `16ddce54-fcf5-46b5-8261-eec199dba827` |
| `@Gateway-mitsubishi` | environment (dealership exterior, golden hour) | `56075343-d70e-4a19-81b1-6f735eb8e1f5` |

## July offers used in the creative

Sourced from Mitsubishi Motors' national July 2026 program (July 1 – August 3 window) —
**verify against your current dealer bulletin before publishing**, and swap in regional
offers if this store sells the Exceed trim outside the US market:

1. **Up to $4,500 factory rebate** on select 2025 Outlander PHEV trims (SE / SEL / SEL Premium / SEL Black Edition / Platinum Edition) — not combinable with special APR/lease.
2. **4.99% APR for 72 months** on any new 2026 Outlander PHEV — **July 1 – August 3, 2026**.
3. **2.99% APR for 60 months** on a new 2026 Outlander (excl. Trail Edition & Ralliart) — **July 1 – August 3, 2026**.
4. Lease example: 2026 Outlander ES 1.5T 2WD, **$389/mo × 39 months**, $4,388 due at signing.

The earlier headline offers (0% APR/72 mo, rebate window ending July 6) expired
on July 6, 2026 and were removed from the page.

## Files

- `index.html` — the full **July Sales Event landing page**: self-contained single file
  (all imagery embedded as data URIs), cinematic dark theme, live countdown to the
  August 3 offer deadline, offer cards, Outlander Exceed showcase, and compliance
  fine print. Drop it onto the dealer site as-is.
- `prompts.md` — three optimized Higgsfield generation prompts (model, aspect ratio,
  element placeholders) for future AI ad composites. Note: offer copy inside the
  prompts reflects the pre-July-6 program — refresh the text before re-running.
- `assets/` — the campaign imagery, cut from the two Higgsfield Elements:
  `gateway-hero.jpg` (dealership at dusk), `car-hero.jpg` (rear three-quarter),
  `car-front.jpg`, `car-side.jpg`, and the `det-*.jpg` close-up tiles.

## Regenerating the ads

Generate with Higgsfield `generate_image` using model `nano_banana_2` (best text
rendering for ad typography; ~1.5 credits per image at 1K). Embed the element IDs in
the prompt as `<<<element-id>>>` placeholders exactly as written in `prompts.md`.
