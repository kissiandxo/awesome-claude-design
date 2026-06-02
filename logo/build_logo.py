#!/usr/bin/env python3
"""Generate the LT monogram logo (SVG) and render the PNG icon set.

The mark is an "L and T merged" letterform — a shared vertical stem with the
T's crossbar near the top and the L's foot at the bottom-right — drawn in the
Teletech / "TT" style: every free stroke ends in a flared, forked (split)
terminal with a small dot in the crook. White-on-black, rounded app-icon
corners. Each terminal is one authored cap, reused/rotated to every stroke end
so the style is identical across the mark.

Run:  python3 logo/build_logo.py
"""
import cairosvg

# ---- canvas / palette -------------------------------------------------------
SIZE = 1024
CORNER = 224          # rounded-corner radius (~22%, matches the app icon)
BG = "#0A0A0A"        # near-black tile
FG = "#F5F5F2"        # near-white symbol
SHOW_SPARKLES = False  # Teletech style has none; flip to re-add subtle ones

W = 42                # stroke half-width (84px slim strokes; flare is at the tips)
OVER = 8              # shaft overlap into each cap (seamless join)

# ---- Teletech-style forked terminal cap (local coords, points "up" = -y) ----
def cap(w):
    """Flared, forked split terminal. Base-centered at (0,0); extends up (-y).

    Short, contained prongs with a shallow central notch — the clean heraldic
    terminal, not long spikes. Pair with a dot at (0, -68) for the crook detail.
    """
    hh = w + 26          # flared half-width (outer corner)
    tip = w + 18         # prong-tip half-width
    return (
        f"M {-w} 0 "
        f"C {-w} -20 {-hh} -32 {-hh} -58 "                 # flare -> outer corner
        f"C {-hh} -74 {-(tip+2)} -76 {-tip} -86 "          # -> left prong tip
        f"C {-(hh-26)} -68 -50 -46 -24 -58 "               # inner edge -> notch top
        f"Q -16 -46 0 -50 "                                # dip to center
        f"Q 16 -46 24 -58 "                                # (mirror) ->
        f"C 50 -46 {hh-26} -68 {tip} -86 "
        f"C {tip+2} -76 {hh} -74 {hh} -58 "
        f"C {hh} -32 {w} -20 {w} 0 Z"
    )


def sparkle(px, py, r, k=0.16):
    c = r * k
    return (
        f"M {px} {py-r} Q {px+c} {py-c} {px+r} {py} Q {px+c} {py+c} {px} {py+r} "
        f"Q {px-c} {py+c} {px-r} {py} Q {px-c} {py-c} {px} {py-r} Z"
    )


# ---- LT layout (stem / crossbar / foot) -------------------------------------
SX = 512              # stem center x (symbol is centered on canvas)
TOP = 346             # up-cap base y (stem top); tip reaches ~242
BOT = 770             # bottom edge (L corner)
CY = 452              # crossbar center y
FY = 696              # foot center y
CAP_L = SX - 114      # crossbar left cap base x  (398)
CAP_R = SX + 114      # crossbar right cap base x (626)
FOOT_R = SX + 114     # foot right cap base x     (626)


def term(cx, cy, angle):
    """One terminal: a rotated cap plus its dot, placed at (cx, cy)."""
    return (
        f'<g transform="translate({cx} {cy}) rotate({angle})">'
        f'<path d="{cap(W)}"/><circle cx="0" cy="-68" r="11"/></g>'
    )


def build_svg():
    shafts = (
        f'<rect x="{SX-W}" y="{TOP-OVER}" width="{2*W}" height="{BOT-(TOP-OVER)}"/>'  # stem
        f'<rect x="{CAP_L-OVER}" y="{CY-W}" width="{(CAP_R+OVER)-(CAP_L-OVER)}" height="{2*W}"/>'  # crossbar
        f'<rect x="{SX-W}" y="{FY-W}" width="{(FOOT_R+OVER)-(SX-W)}" height="{2*W}"/>'  # foot
    )
    terminals = (
        term(SX, TOP, 0)        # stem top  (up)
        + term(CAP_L, CY, -90)  # crossbar left
        + term(CAP_R, CY, 90)   # crossbar right
        + term(FOOT_R, FY, 90)  # foot right
    )
    extra = (sparkle(322, 318, 28) + sparkle(706, 320, 18)) if SHOW_SPARKLES else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}" height="{SIZE}" '
        f'viewBox="0 0 {SIZE} {SIZE}">'
        f'<rect width="{SIZE}" height="{SIZE}" rx="{CORNER}" ry="{CORNER}" fill="{BG}"/>'
        f'<g fill="{FG}">{shafts}{terminals}<path d="{extra}"/></g>'
        f"</svg>"
    )


def main():
    svg = build_svg()
    with open("logo/logo.svg", "w") as f:
        f.write(svg)
    for size in (1024, 512, 180):
        cairosvg.svg2png(
            bytestring=svg.encode(), write_to=f"logo/logo-{size}.png",
            output_width=size, output_height=size,
        )
    print("wrote logo/logo.svg and PNGs at 1024, 512, 180")


if __name__ == "__main__":
    main()
