# CWC Health, HMSS 2026 paper

This repository is the HMSS 2026 IEEE conference paper (LaTeX) for CWC Health. It is not the Flutter application repository.

## Re-verify technical claims against the companion app

The companion Flutter app changes often. Do not trust prior chat summaries, older paper drafts, or `notes/claims-and-evidence.md` alone.

Before asserting or revising any technical claim in `main.tex` (System Design, privacy, Nearby, My Health, Help Now, storage, location, flags):

1. Re-inspect the companion app as it exists now (README, engineering docs, and relevant source).
2. Lead with the researched future product / Figma planned service grounded in Stage-1. Treat engineering demo notes as secondary.
3. Distinguish product capabilities from meeting-only demo flags when both exist.
4. Update `notes/claims-and-evidence.md` with the new evidence and date when claims change.
5. Soften or remove manuscript text that no longer matches the product story or companion evidence.

Do not modify the companion app from this paper repository unless the authors explicitly ask.

## Writing style (manuscript, notes, commits)

- Plain and direct. Short sentences. Lead with the point.
- Numbers over adjectives: cite the N, the version, the count, the flag name.
- No filler connectors ("Taken together", "At the same time", "likewise"), no marketing words (robust, seamless, comprehensive, leverage), no em-dash chains. Use commas, parentheses, or a new sentence.
- If something is unfinished or not implemented, say so in the text. Do not paper over it.

## Authoring constraints

- Do not invent participant counts, study results, IRB status, quotes, or clinical outcomes. Unsupported claims stay TODOs or notes.
- Prefer outline / TODO section bodies over fabricated manuscript prose until evidence exists.
- Do not commit study corpus materials (IRB packets, focus-group transcripts, identifiable notes) or the companion app into this git tree. Keep pointers and claim maps in `notes/` only.
- Prefer product-led language for the planned service answering Stage-1. Use engineering demo detail to support, not to undercut, product capabilities that the companion app already implements (for example PIN / encrypt / erase).

## Project facts (public)

- Build: `just check` or `latexmk -pdf main.tex` (`IEEEtran`, `conference,a4paper`).
- Working title: CWC Health: Co-Designing a Privacy-Preserving Mobile Health Navigation Platform for Community Wellness Centers.
- Framing: privacy-preserving co-designed mobile health navigation / data minimization. Not precision medicine, clinical AI, diagnosis, or treatment recommendation unless later evidence supports it.
- Product snapshot (2026-09-06, companion audit @ `5464776`): the final design is town-first Nearby with optional one-shot Use my location and no coordinate retention. The current prototype's live mode instead requests coarse location on load and falls back to a fixed New Brunswick list. PIN / encrypted My Health / erase are implemented in the prototype. There are no accounts or analytics. Re-check the companion app before relying on this bullet.

## Learned User Preferences

- Collaborative paper repo: keep AGENTS.md skill-agnostic (plain style guidance only; no skill names or skill-enforcement).
- Public GitHub: notes may be shared, but never commit local rclone/Box absolute paths, gift-card URLs, participant names, Zoom passwords, or other sensitive study materials.

## Learned Workspace Facts

- Public remote: `github.com/ks1686/cwc-health-hmss-2026`.
- Manuscript Method / Results / Discussion / Limitations / Conclusion target Stage-1 needs assessment only; do not invent Stage-3 usability results.
- External technical cites beyond the Box corpus are expected (privacy, location minimization, OSM, 988-style engineering literature).
- Compensated Stage-1 FG aggregates used in manuscript: n=7 PSS virtual, n=38 members in person; IRB Pro2025002116 Exempt 3b approved 2025-11-19.
- Tip scrub of local machine paths in committed notes was enough; do not force-push a history rewrite for that scrub.
