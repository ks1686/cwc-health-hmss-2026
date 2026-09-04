# CWC Health (HMSS 2026)

LaTeX source for an IEEE conference paper on **CWC Health**, a privacy-preserving mobile health navigation prototype co-designed with Community Wellness Center members, peer support specialists, and a Rutgers team in behavioral health and engineering.

**Working title:** *CWC Health: Co-Designing a Privacy-Preserving Mobile Health Navigation Platform for University Communities*

The study build described in the manuscript is a Flutter app with four tabs (Nearby, My Health, Learn, More) and a persistent Help Now control. It emphasizes data minimization: no user accounts, no third-party analytics, and no device GPS tracking for nearby care discovery. This repository is the paper only, not the application source.

Venue target: [HMSS 2026](https://www.hmss-conference.org/) (IEEE A4 conference manuscript template). The draft is in progress; method and results will be filled from study materials as they are finalized.

## Build

Requires a TeX distribution with `latexmk`, `pdflatex`, and BibTeX (for example [TeX Live](https://www.tug.org/texlive/) or MacTeX).

```bash
latexmk -pdf main.tex
```

Or, if [`just`](https://github.com/casey/just) is installed:

```bash
just build    # compile
just check    # same compile CI runs
just clean    # remove aux files
```

Entry point: `main.tex`. Bibliography: `references.bib` (IEEE style).

## Continuous integration

Every push to `main` and every pull request compiles `main.tex` with `latexmk`. The workflow fails if the PDF is not produced. Successful builds upload `main.pdf` as a workflow artifact (14-day retention).

## Repository layout

| Path | Contents |
| --- | --- |
| `main.tex` | Manuscript |
| `references.bib` | Bibliography |
| `figures/` | Figures for inclusion |
| `notes/` | Author working notes (not part of the compiled paper) |
