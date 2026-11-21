#!/usr/bin/env python3
"""Render a 1024x1024 dark news infographic for 21 November 2026."""
from PIL import Image, ImageDraw, ImageFont

BG = (13, 17, 23)
TEXT = (230, 237, 243)
MUTED = (139, 148, 158)
ACCENTS = [(255, 88, 96), (63, 185, 80), (88, 166, 255), (210, 153, 34), (188, 140, 255), (255, 166, 87), (79, 209, 197)]

STORIES = [
    ("ICJ: Myanmar guilty of Rohingya genocide",
     "UN court's first-ever country genocide ruling orders probes and safe returns.", "WORLD"),
    ("Russian missiles strike Poland",
     "Rutte guarantees NATO will defend 'every inch' after airspace violations.", "EUROPE"),
    ("Trump defers Iran strike decision",
     "Cites 'dirty bomb' threat; Iran readies tankers to break blockade.", "MIDEAST"),
    ("Russian-linked cargo ship burns off Finland",
     "Drone-hit vessel drifts into Finnish waters; crew evacuated.", "BALTIC"),
    ("Youth strike sweeps 25+ countries",
     "Students protest across Europe for climate, schools, against conscription.", "SOCIETY"),
    ("Basra power station fire kills four",
     "At least 35 injured in blaze at Iraq's Hartha plant; toll may rise.", "MENA"),
    ("Markets: S&P 500 enters correction",
     "Nvidia plunges 14% on SEC probe; worst weekly losing run since 2008.", "BUSINESS"),
]

F = "/usr/share/fonts/truetype/dejavu/"
def font(size, bold=False):
    return ImageFont.truetype(F + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"), size)

W = H = 1024
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
M = 64  # margin

# Headline area
d.text((M, 56), "WORLD NEWS", font=font(58, True), fill=TEXT)
d.text((M, 130), "Saturday 21 November 2026", font=font(26), fill=MUTED)
d.line([(M, 186), (W - M, 186)], fill=(48, 54, 61), width=2)

card_top = 216
card_h = 96
gap = 14
for i, (head, summ, tag) in enumerate(STORIES):
    y = card_top + i * (card_h + gap)
    acc = ACCENTS[i]
    d.rounded_rectangle([M, y, W - M, y + card_h], radius=12, fill=(22, 27, 34))
    d.rounded_rectangle([M, y, M + 6, y + card_h], radius=3, fill=acc)
    tagtxt = f"{tag}  ·  21 NOV 2026"
    hf = font(24, True)
    htxt = head
    maxw = (W - M) - (M + 28) - d.textlength(tagtxt, font=font(13)) - 48
    while d.textlength(htxt, font=hf) > maxw and len(htxt) > 4:
        htxt = htxt[:-2].rstrip() + "…"
    d.text((M + 28, y + 14), htxt, font=hf, fill=TEXT)
    tagtxt = f"{tag}  ·  21 NOV 2026"
    d.text((W - M - 28 - d.textlength(tagtxt, font=font(13)), y + 16), tagtxt, font=font(13), fill=acc)
    d.text((M + 28, y + 52), summ, font=font(17), fill=MUTED)

foot = "Sources: Reuters · Anadolu · Euronews · Xinhua · The Independent"
d.text((M, H - 44), foot, font=font(14), fill=MUTED)

img.save("21.png", optimize=True)
print("saved 21.png")
