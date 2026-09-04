# CWC Health — HMSS 2026 paper

IEEE conference paper repository for a possible **HMSS 2026** submission on CWC Health.

This is **not** the application repository. The Flutter app lives separately at:

```text
../rutgers-health-services-app
```

Treat that app repo as **read-only** technical truth when verifying system claims. Do not modify it from this project unless explicitly asked.

## Working title

CWC Health: Co-Designing a Privacy-Preserving Mobile Health Navigation Platform for University Communities

## Build (local)

Requires [MacTeX](https://tug.org/mactex/) (this machine: Homebrew cask `mactex-no-gui`). Put TeX binaries on `PATH`:

```bash
export PATH="/Library/TeX/texbin:$PATH"
latexmk -pdf main.tex
```

Clean build artifacts:

```bash
latexmk -C
```

Uses `IEEEtran` with `\documentclass[conference,a4paper]{IEEEtran}` and BibTeX (`references.bib`, `IEEEtran` style).

## Layout

| Path | Role |
| --- | --- |
| `main.tex` | Manuscript skeleton |
| `references.bib` | Bibliography |
| `figures/` | Figures for `\includegraphics` |
| `notes/` | Research framing / claims map (not manuscript prose) |

## External research corpus

Team research materials (Box sync) are **outside** this git repo — do not commit them here:

```text
/Users/ks1686/rclone/School-Box/BHE RFP 2025-2026
```

See `notes/` for pointers into Focus Groups, IRB, Articles, etc.
