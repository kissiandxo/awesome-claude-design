# Logo

An **L + T merged** monogram drawn in the **Teletech / "TT"** style: a shared
vertical stem with the **T**'s crossbar near the top and the **L**'s foot at the
bottom-right. Every free stroke ends in a flared, **forked (split) terminal**
with a small dot in the crook — the same terminal authored once and reused at
each stroke end so the style is identical across the mark. Monochrome: near-white
`#F5F5F2` on near-black `#0A0A0A`, rounded app-icon corners, 1024×1024.

## Files

| File | Use |
|------|-----|
| `logo.svg` | Scalable vector master (edit this) |
| `logo-1024.png` | Full-size icon |
| `logo-512.png` | Medium icon |
| `logo-180.png` | Small / app icon |
| `build_logo.py` | Generator for the SVG + PNG set |

PNGs are transparent outside the rounded tile, so the rounded corners show on
any background.

## Regenerate

```bash
pip install cairosvg          # one-time
python3 logo/build_logo.py    # run from the repo root
```

Tune via the constants in `build_logo.py`:

- **Terminal style** — `cap()` (flare width `hh`, prong length, notch depth).
- **Letterform layout** — `SX`, `TOP`, `BOT`, `CY` (crossbar height), `FY` (foot
  height), `CAP_L` / `CAP_R` / `FOOT_R` (arm + foot reach), stroke weight `W`.
- **Sparkles** — set `SHOW_SPARKLES = True` to re-add subtle 4-pointed stars.
