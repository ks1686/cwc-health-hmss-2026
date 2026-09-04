# CWC Health, HMSS 2026 paper

LaTeX source for a possible HMSS 2026 (IEEE) submission on CWC Health.

This is the paper repo, not the app. The Flutter app lives at:

```text
../rutgers-health-services-app
```

Treat the app repo as read-only when checking technical claims. Do not edit it from here unless asked.

## Working title

CWC Health: Co-Designing a Privacy-Preserving Mobile Health Navigation Platform for University Communities

## Build

Needs MacTeX (on this machine: Homebrew cask `mactex-no-gui`). Put TeX on `PATH`, then:

```bash
export PATH="/Library/TeX/texbin:$PATH"
latexmk -pdf main.tex
```

Clean up:

```bash
latexmk -C
```

`IEEEtran`, `conference,a4paper`, BibTeX with `references.bib`.

## Layout

| Path | Role |
| --- | --- |
| `main.tex` | Manuscript |
| `references.bib` | Bibliography |
| `figures/` | Figures for `\includegraphics` |
| `notes/` | Framing, claims-to-evidence map, related-work and study pointers (not manuscript text) |

## Research materials

Team research (Box sync) is outside this repo. Do not commit it here:

```text
/Users/ks1686/rclone/School-Box/BHE RFP 2025-2026
```

`notes/` has pointers into Focus Groups, IRB, Articles, etc.
