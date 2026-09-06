# Research framing (working notes)

Working notes for authors. Not manuscript text. Keep the paper aligned while drafting.

## Venue / topic

- Target: [HMSS 2026](https://www.hmss-conference.org/) (2nd International Conference on Health Medical Systems and Services)
- Proposed topic area: Precision and Personalized Health
- Format: IEEE conference, A4 (`IEEEtran` with `conference,a4paper`)

## Working title

CWC Health: Co-Designing a Privacy-Preserving Mobile Health Navigation Platform for Community Wellness Centers

The funded project setting is Community Wellness Centers (CWCs) / peer recovery centers, with a Rutgers interdisciplinary team. Title now names Community Wellness Centers. Manuscript prose should prefer CWC / peer-recovery framing over implying a general campus-student app.

## What this paper is about

A privacy-preserving, co-designed mobile health-navigation **product** (Figma planned service) that provides contextual access to health resources while minimizing collection and retention of sensitive information. Stage~1 grounds the product. An engineering demo implements the same shell; demo details are secondary to the product story.

Central question:

> How much useful, contextually personalized health support can a mobile application provide while collecting and retaining as little sensitive user data as possible?

Secondary focus: co-design and usability (discoverability, trust, visual language, design iteration from community feedback).

## Preferred terminology

- mobile health navigation
- digital health
- health-resource access
- personalized health access (use carefully)
- context-aware health navigation
- location-aware health-resource discovery
- privacy by design / privacy-preserving
- data minimization
- on-device health information
- co-design / participatory design
- community wellness / Community Wellness Centers

## Avoid unless explicitly evidenced

- precision medicine / precision health
- clinical AI / intelligent diagnosis
- treatment recommendation / clinical decision support
- predictive healthcare
- improved patient outcomes / clinical efficacy

“Personalized” here means contextualized access based on user context (for example a town-first search, optional one-shot Use my location) and locally held health information (PIN, on-device store, erase). It does not mean personalized medical treatment. No background GPS tracking. No GPS history retention.

## Related repositories

| Role | Notes |
| --- | --- |
| This paper | LaTeX sources in this repository |
| Companion Flutter app | Separate repository. Use it to verify that the engineering demo can implement the product shell. Lead manuscript claims with the product / Figma design answering Stage~1, not demo-only hedges |
| Study and literature corpus | Held by the research team outside this git tree. Do not commit IRB files, focus-group transcripts, or other sensitive study materials here |

When editing System Design or other technical claims, re-check the companion app and update `notes/claims-and-evidence.md`.
