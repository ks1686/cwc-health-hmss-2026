#!/usr/bin/env python3
"""Generate manuscript figures for HMSS 2026 CWC Health paper.
Outputs PDF (vector) files into this directory. No participant identifiers.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.titlesize": 11,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08,
})

SCARLET = "#CC0033"
INK = "#21262B"
SUB = "#5F6A72"
LINE = "#E4E1DB"
SURFACE = "#FCFBF9"
TINT = "#FAE7EC"
CARD = "#FFFFFF"


def rounded(ax, xy, w, h, text, fc=CARD, ec=LINE, tc=INK, fs=8, lw=1.2, weight="normal"):
    box = FancyBboxPatch(
        xy, w, h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        linewidth=lw, edgecolor=ec, facecolor=fc, zorder=2,
    )
    ax.add_patch(box)
    ax.text(
        xy[0] + w / 2, xy[1] + h / 2, text,
        ha="center", va="center", color=tc, fontsize=fs,
        fontweight=weight, wrap=True, zorder=3,
    )


def arrow(ax, p1, p2, color=SUB):
    ax.annotate(
        "", xy=p2, xytext=p1,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=1.2),
        zorder=1,
    )


def fig_architecture():
    fig, ax = plt.subplots(figsize=(7.0, 3.6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7.2)
    ax.axis("off")
    ax.set_title("CWC Health product architecture (planned service)", pad=8)

    # Shell
    rounded(ax, (0.4, 5.4), 13.2, 1.4,
            "Flutter product shell  \u00b7  no accounts  \u00b7  no analytics SDKs\n"
            "On-device first; engineering demo implements the same shell",
            fc=TINT, ec=SCARLET, fs=8.5, weight="bold")

    # Tabs
    tabs = [
        ("Nearby\n(town-first)", 0.6),
        ("My Health\nPIN / store / erase", 3.5),
        ("Learn\nsource-labeled", 6.4),
        ("More\nsettings + erase", 9.3),
    ]
    for label, x in tabs:
        rounded(ax, (x, 3.2), 2.6, 1.6, label, fc=CARD, ec=LINE, fs=8.5)

    rounded(ax, (12.0, 3.2), 1.6, 1.6, "Help Now\n(header)",
            fc=SCARLET, ec=SCARLET, tc="white", fs=8, weight="bold")

    # Data / privacy layer
    rounded(ax, (0.6, 0.4), 5.8, 2.2,
            "Nearby: town-first discovery\n"
            "Optional one-shot Use my location\n"
            "OSM Overpass (+ optional Google soft-fail)\n"
            "No background tracking; no GPS history",
            fc=SURFACE, ec=SCARLET, fs=7.5)
    rounded(ax, (6.8, 0.4), 6.6, 2.2,
            "My Health: on-device PIN, encrypted store, erase\n"
            "Help Now: 988 / 911 / Poison Control + local entries\n"
            "Map browsing allowed; not continuous surveillance\n"
            "No accounts; no third-party analytics",
            fc=SURFACE, ec=LINE, fs=7.5)

    arrow(ax, (1.9, 3.2), (2.5, 2.6))
    arrow(ax, (4.8, 3.2), (8.5, 2.6))

    fig.savefig(OUT / "architecture.pdf")
    fig.savefig(OUT / "architecture.png")
    plt.close(fig)


def fig_nearby_pipeline():
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 5.6)
    ax.axis("off")
    ax.set_title("Nearby data path (town-first; optional location)", pad=6)

    # Main town-first path (Google is a side path, not a required middle box)
    steps = [
        (0.3, "Town name\n(primary)", SURFACE, LINE),
        (3.3, "Nominatim\ngeocode", CARD, LINE),
        (6.3, "OSM Overpass\n(+ mirror failover)", CARD, SCARLET),
        (9.5, "NJ bbox + hours\nparse + cache", SURFACE, LINE),
        (12.7, "UI + disclaimer\nCall / Text / Dir.", SCARLET, SCARLET),
    ]
    for x, label, fc, ec in steps:
        tc = "white" if fc == SCARLET else INK
        w = 2.6 if x < 12.7 else 2.8
        rounded(ax, (x, 2.0), w, 1.9, label, fc=fc, ec=ec, tc=tc, fs=7.0,
                weight="bold" if fc == SCARLET else "normal")

    for i in range(len(steps) - 1):
        x1 = steps[i][0] + (2.6 if steps[i][0] < 12.7 else 2.8)
        x2 = steps[i + 1][0]
        arrow(ax, (x1, 2.95), (x2, 2.95), color=SUB)

    # Optional Google soft-fail as a side path (not in the required chain)
    rounded(ax, (6.0, 0.55), 3.2, 1.15,
            "Google Places\n(optional soft-fail)",
            fc=TINT, ec=SCARLET, fs=6.5)
    # Side arrow from Nominatim area down to Google, then up toward OSM
    ax.annotate(
        "", xy=(7.6, 1.7), xytext=(5.0, 2.0),
        arrowprops=dict(arrowstyle="-|>", color=SUB, lw=1.0,
                        connectionstyle="arc3,rad=-0.25"),
        zorder=1,
    )
    ax.annotate(
        "", xy=(8.0, 2.0), xytext=(8.4, 1.7),
        arrowprops=dict(arrowstyle="-|>", color=SUB, lw=1.0,
                        connectionstyle="arc3,rad=-0.2"),
        zorder=1,
    )

    ax.text(8.0, 5.15,
            "Optional: one-shot Use my location (coarse). No background tracking; no GPS history retained.",
            ha="center", va="center", color=SUB, fontsize=7.0)
    ax.text(8.0, 0.15,
            "Failure: plain error + retry. Never swaps in demo pharmacy names.",
            ha="center", va="center", color=SUB, fontsize=7.5)

    fig.savefig(OUT / "nearby_pipeline.pdf")
    fig.savefig(OUT / "nearby_pipeline.png")
    plt.close(fig)


def fig_presurvey():
    # Aggregate member smartphone items (n=27 unless noted). Public manuscript numbers only.
    labels = [
        "Smartphone\naccess (n=41)",
        "Android\n(of phones)",
        "Use phone\nmany\u00d7/day",
        "Health apps\nrarely/never",
        "Would find\nhealth app helpful",
        "Want help\nusing an app",
    ]
    values = [63, 78, 81, 63, 89, 67]
    colors = [SCARLET if v >= 70 else TINT for v in values]

    fig, ax = plt.subplots(figsize=(7.0, 3.2))
    y = np.arange(len(labels))
    bars = ax.barh(y, values, color=colors, edgecolor=LINE, height=0.7)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlim(0, 100)
    ax.set_xlabel("% of respondents (item-level n)", fontsize=8)
    ax.set_title("Member pre-survey highlights (Stage 1)", pad=6)
    ax.invert_yaxis()
    for bar, v in zip(bars, values):
        ax.text(v + 1.2, bar.get_y() + bar.get_height() / 2, f"{v}%",
                va="center", ha="left", fontsize=8, color=INK)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.axvline(50, color=LINE, lw=0.8, ls="--")
    fig.savefig(OUT / "presurvey_highlights.pdf")
    fig.savefig(OUT / "presurvey_highlights.png")
    plt.close(fig)


def fig_theme_map():
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Stage-1 themes \u2192 planned product features", pad=6)

    left = [
        (6.4, "Trusted local resources\n+ action-oriented next steps"),
        (5.0, "Distrust of data-heavy apps\n+ login / password friction"),
        (3.6, "Plain language +\nsource-labeled education"),
        (2.2, "Appointments / meds\nself-management needs"),
        (0.8, "Peer onboarding +\ncrisis access without delay"),
    ]
    right = [
        (6.4, "Nearby: town-first + OSM\n+ optional Use my location"),
        (5.0, "No accounts / no analytics\nNo background GPS history"),
        (3.6, "Learn tab\n(named sources)"),
        (2.2, "My Health: on-device PIN,\nencrypted store, erase"),
        (0.8, "Help Now header\n(urgent dialers + local entries)"),
    ]
    for y, label in left:
        rounded(ax, (0.3, y), 4.8, 1.15, label, fc=TINT, ec=LINE, fs=7.2)
    for y, label in right:
        rounded(ax, (6.9, y), 4.8, 1.15, label, fc=CARD, ec=SCARLET, fs=7.2)
    for y, _ in left:
        arrow(ax, (5.15, y + 0.55), (6.85, y + 0.55))

    ax.text(2.7, 7.55, "Stage 1 evidence", ha="center", color=SUB, fontsize=8, fontweight="bold")
    ax.text(9.3, 7.55, "Product response", ha="center", color=SUB, fontsize=8, fontweight="bold")

    fig.savefig(OUT / "theme_to_features.pdf")
    fig.savefig(OUT / "theme_to_features.png")
    plt.close(fig)


def fig_ui_schematic():
    """Phone-frame schematic of the four-tab shell (not a product screenshot)."""
    fig, axes = plt.subplots(1, 4, figsize=(7.4, 3.6))
    titles = ["Nearby", "My Health", "Learn", "More"]
    bodies = [
        ["Disclaimer / town chip", "Category filters", "Place card", "Call \u00b7 Text \u00b7 Directions"],
        ["PIN lock (on-device)", "Appointments", "Medications", "Wallet card"],
        ["Physical Health", "Mental Health", "Nutrition \u00b7 Exercise", "Source-labeled articles"],
        ["How to use", "Ask a Peer", "Settings", "Erase personal data"],
    ]
    for ax, title, rows in zip(axes, titles, bodies):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 18)
        ax.axis("off")
        # phone outline
        phone = FancyBboxPatch((1, 0.5), 8, 17, boxstyle="round,pad=0.05,rounding_size=0.4",
                               linewidth=1.5, edgecolor=INK, facecolor=SURFACE)
        ax.add_patch(phone)
        # header
        ax.add_patch(FancyBboxPatch((1.3, 15.2), 7.4, 1.6, boxstyle="round,pad=0.02,rounding_size=0.1",
                                    linewidth=0, facecolor=CARD))
        ax.text(3.2, 16.0, title, fontsize=8, fontweight="bold", color=INK, va="center")
        ax.add_patch(FancyBboxPatch((6.3, 15.45), 2.2, 1.1, boxstyle="round,pad=0.02,rounding_size=0.4",
                                    linewidth=0, facecolor=SCARLET))
        ax.text(7.4, 16.0, "Help Now", fontsize=5.5, color="white", ha="center", va="center")
        # body rows
        y = 13.8
        for row in rows:
            ax.add_patch(FancyBboxPatch((1.5, y - 0.9), 7.0, 1.5, boxstyle="round,pad=0.02,rounding_size=0.1",
                                        linewidth=0.8, edgecolor=LINE, facecolor=CARD))
            ax.text(5.0, y - 0.15, row, fontsize=6.5, ha="center", va="center", color=INK)
            y -= 2.2
        # tab bar
        ax.add_patch(plt.Rectangle((1.3, 0.9), 7.4, 1.4, facecolor=CARD, edgecolor=LINE, lw=0.8))
        for i, t in enumerate(["N", "H", "L", "M"]):
            color = SCARLET if titles[i] == title else SUB
            ax.text(2.2 + i * 1.8, 1.6, t, fontsize=7, ha="center", color=color, fontweight="bold")
        ax.set_title(title, fontsize=8, pad=2)

    fig.suptitle("Product information architecture (schematic)", fontsize=10, y=1.02)
    fig.savefig(OUT / "ui_shell.pdf")
    fig.savefig(OUT / "ui_shell.png")
    plt.close(fig)


if __name__ == "__main__":
    fig_architecture()
    fig_nearby_pipeline()
    fig_presurvey()
    fig_theme_map()
    fig_ui_schematic()
    print("Wrote figures to", OUT)
