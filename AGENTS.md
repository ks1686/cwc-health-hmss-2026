# CWC Health — HMSS 2026 paper

This repository is the **HMSS 2026 IEEE conference paper** (LaTeX) for CWC Health. It is **not** the Flutter application repo.

## App repo is live — re-verify before claiming

The sibling Flutter app at `~/Documents/Repos/rutgers-health-services-app` changes often. **Do not trust prior chat summaries, this paper’s older drafts, or `notes/claims-and-evidence.md` alone.**

Before asserting or revising any technical claim in `main.tex` (System Design, privacy, Nearby, My Health, Help Now, storage, location, flags):

1. Re-inspect the app repo as it exists **now** (prefer `README.md`, `AGENTS.md`, `docs/engineering/`, and `lib/`).
2. Distinguish **as-built study prototype** behavior from **aspirational MVP** in `CWC_Health_App/` specs.
3. Update `notes/claims-and-evidence.md` with the new evidence paths (and date) when claims change.
4. Soften or remove manuscript text that no longer matches the code.

Treat the app repo as **read-only** unless the human explicitly asks to modify it.

## Learned User Preferences

- If a file or directory cannot be found, stop and ask rather than deep-searching or inventing paths.
- Treat `rutgers-health-services-app` as read-only technical truth unless explicitly asked to modify it.
- Do not invent participant counts, study results, IRB status, quotes, or clinical outcomes; unsupported claims stay TODOs or notes.
- Prefer outline/TODO section bodies over fabricated manuscript prose until evidence exists.
- Do not copy Box research materials, Downloads example papers, or the app repo into this git tree (pointers in `notes/` only).
- Prefer as-built language for the current study build; label intended MVP features as design targets until implemented.

## Learned Workspace Facts

- Paper root: `/Users/ks1686/Documents/Repos/CWC Health` — IEEE `\documentclass[conference,a4paper]{IEEEtran}`; build with `PATH="/Library/TeX/texbin:$PATH" latexmk -pdf main.tex`.
- Working title: `CWC Health: Co-Designing a Privacy-Preserving Mobile Health Navigation Platform for University Communities`.
- Sibling app repo (read-only for claims): `~/Documents/Repos/rutgers-health-services-app`.
- External research corpus (not tracked here): `/Users/ks1686/rclone/School-Box/BHE RFP 2025-2026` (Focus Groups, IRB, Articles, App Design, Team Notes, etc.).
- Venue-format example PDFs live under `~/Downloads` for reference only.
- MacTeX is brew cask `mactex-no-gui`; binaries under `/Library/TeX/texbin` (may need PATH refresh after install).
- Framing is privacy-preserving co-designed mobile health navigation / data minimization — not precision medicine, clinical AI, diagnosis, or treatment recommendation unless later evidence supports it.
- As of 2026-09-03 study-build snapshot: live Nearby is town→Nominatim→OSM behind `LIVE_NEARBY` (no GPS); My Health/Learn/More remain largely static demo; Help Now dialers gated by `HELP_NOW_LIVE`; encrypted My Health / PIN / working erase are spec targets, not yet implemented — **re-check app before relying on this bullet**.
