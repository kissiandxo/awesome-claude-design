#!/usr/bin/env python3
"""Generate the redesigned cross logo (SVG) and render the PNG icon set.

The mark is a four-way symmetric cross with bold arms whose ends flare into a
wide head that is split by a short central notch (forked/heraldic tips, styled
after the reference), plus two subtle 4-pointed sparkles. White-on-black,
rounded app-icon corners. One arm is authored and mirrored/rotated so the
result is perfectly symmetric.

Run:  python3 logo/build_logo.py
"""
import cairosvg

# ---- canvas / palette -------------------------------------------------------
SIZE = 1024
CX = CY = SIZE / 2
CORNER = 224          # rounded-corner radius (~22%, matches the app icon)
BG = "#0A0A0A"        # near-black tile
FG = "#F5F5F2"        # near-white symbol

m = lambda x: 2 * CX - x   # mirror across the vertical center

# ---- cross arm geometry (up arm; mirrored L/R, rotated 4x) ------------------
sh  = 86             # shaft half-width  -> 172px arms (clear negative space)
iy  = CY + 96        # inner end (past center, for the 4-arm overlap)
fy  = CY - 178       # flare begins near the end (long straight shaft)
hh  = 112            # head half-width (modest flare)
hy  = CY - 236       # outer corner y of the flared head
ty  = CY - 264       # prong-tip y (short, contained tips)
pin = 8              # how far the rounded tip leans in from the outer corner
iw  = 24             # inner notch half-width (top opening of the split)
ny  = CY - 236       # inner notch y
nby = CY - 228       # notch bottom (shallow center dip)


def arm_path():
    """Path 'd' for one upward arm: long shaft, modest flare, short forked tip."""
    return (
        f"M {CX-sh} {iy} "
        f"L {CX-sh} {fy} "
        # flare: shaft -> outer corner of head
        f"C {CX-sh} {fy-20} {CX-hh} {hy+26} {CX-hh} {hy} "
        # outer edge -> rounded left prong tip (leans slightly in)
        f"C {CX-hh} {hy-16} {CX-hh+pin-2} {ty+10} {CX-hh+pin} {ty} "
        # inner edge -> down to notch
        f"C {CX-hh+26} {ty+18} {CX-iw-26} {ny-12} {CX-iw} {ny} "
        # notch dip across center
        f"Q {CX-iw+8} {nby-4} {CX} {nby} "
        # ---- mirror to the right half ----
        f"Q {m(CX-iw+8)} {nby-4} {m(CX-iw)} {ny} "
        f"C {m(CX-iw-26)} {ny-12} {m(CX-hh+26)} {ty+18} {m(CX-hh+pin)} {ty} "
        f"C {m(CX-hh+pin-2)} {ty+10} {m(CX-hh)} {hy-16} {m(CX-hh)} {hy} "
        f"C {m(CX-hh)} {hy+26} {m(CX-sh)} {fy-20} {m(CX-sh)} {fy} "
        f"L {m(CX-sh)} {iy} Z"
    )


def sparkle(px, py_, r, k=0.16):
    """4-pointed concave 'twinkle' star centered at (px, py_)."""
    c = r * k
    return (
        f"M {px} {py_-r} "
        f"Q {px+c} {py_-c} {px+r} {py_} "
        f"Q {px+c} {py_+c} {px} {py_+r} "
        f"Q {px-c} {py_+c} {px-r} {py_} "
        f"Q {px-c} {py_-c} {px} {py_-r} Z"
    )


def build_svg():
    arm = arm_path()
    pellet = f'<circle cx="{CX}" cy="{nby-18}" r="11"/>'   # dot in the fork crook
    # one arm + its pellet, rotated to the four directions
    arms = "".join(
        f'<g transform="rotate({a} {CX} {CY})"><path d="{arm}"/>{pellet}</g>'
        for a in (0, 90, 180, 270)
    )
    sparkles = sparkle(320, 322, 30) + " " + sparkle(704, 700, 20)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}" height="{SIZE}" '
        f'viewBox="0 0 {SIZE} {SIZE}">'
        f'<rect x="0" y="0" width="{SIZE}" height="{SIZE}" rx="{CORNER}" ry="{CORNER}" fill="{BG}"/>'
        f'<g fill="{FG}">{arms}<path d="{sparkles}"/></g>'
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
