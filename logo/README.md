# Logo

Redesigned cross logo — a four-way **symmetric heraldic cross** with bold arms
that flare into short **forked (split) tips**, each with a small dot in the
crook, plus two **subtle 4-pointed sparkles**. Restyled after the reference
("TT") while keeping the original mark's identity, rounded app-icon corners, and
1024×1024 dimensions. Monochrome: near-white `#F5F5F2` on near-black `#0A0A0A`.

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

Tune the look by editing the geometry constants near the top of
`build_logo.py` (arm width `sh`, flare `hh`, tip length `ty`, notch, sparkle
size/position), then re-run.
