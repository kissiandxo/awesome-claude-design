# Gateway Mitsubishi — July Sales Event Ad Campaign

Website advertisement package for the Gateway Mitsubishi dealer site, built around two
Higgsfield **Elements** so every ad shows *our* car and *our* store:

| Element | Type | Higgsfield ID |
|---|---|---|
| `@Outlander-exceed` | prop (white Outlander Exceed, black contrast roof) | `16ddce54-fcf5-46b5-8261-eec199dba827` |
| `@Gateway-mitsubishi` | environment (dealership exterior, golden hour) | `56075343-d70e-4a19-81b1-6f735eb8e1f5` |

## July offers used in the creative

Sourced from Mitsubishi Motors' national July 2026 programs — **verify against your
current dealer bulletin before publishing**, and swap in regional offers if this store
sells the Exceed trim outside the US market:

1. **0.0% APR for 72 months** on select new 2026 Outlander models — new retail delivery by **July 6, 2026**.
2. **Up to $4,500 factory rebate** on select Outlander PHEV / 2026 Outlander Trail Edition — through **July 6, 2026** (not combinable with special APR/lease).
3. **4.99% APR for 72 months** on any new 2026 Outlander PHEV — **July 1 – August 3, 2026**.

## Files

- `index.html` — drop-in, self-contained ad section for the dealer website
  (hero banner + two offer tiles + compliance fine print). Images load from `assets/`.
- `prompts.md` — the three optimized Higgsfield generation prompts (model,
  aspect ratio, element placeholders). Re-run any prompt to refresh a creative.
- `assets/` — destination for the generated ads:
  - `hero-july-sales-event.jpg` (16:9 website hero)
  - `tile-phev-rebate.jpg` (1:1 offer tile)
  - `tile-finance-offer.jpg` (4:5 offer tile)

## Regenerating the ads

Generate with Higgsfield `generate_image` using model `nano_banana_2` (best text
rendering for ad typography; ~1.5 credits per image at 1K). Embed the element IDs in
the prompt as `<<<element-id>>>` placeholders exactly as written in `prompts.md`.
