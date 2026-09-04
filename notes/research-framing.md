# Research framing (working notes)

This file is **not** manuscript text. Use it to keep the paper aligned while drafting.

## Venue / topic

- Target: HMSS 2026 (2nd International Conference on Health Medical Systems and Services)
- Proposed topic area: Precision and Personalized Health
- Format: IEEE conference, A4 (`IEEEtran` with `conference,a4paper`)

## Working title

CWC Health: Co-Designing a Privacy-Preserving Mobile Health Navigation Platform for University Communities

**Note:** The funded project setting is **Community Wellness Centers (CWCs)** / peer recovery centers (CSPNJ), with a Rutgers interdisciplinary team. Keep the working title until asked to change it; manuscript prose should prefer CWC / peer-recovery framing over implying a general campus-student app.

## What this paper is about

A privacy-preserving, co-designed mobile **health-navigation** system that provides contextual / personalized access to health resources while minimizing collection and retention of sensitive information.

Central question:

> How much useful, contextually personalized health support can a mobile application provide while collecting and retaining as little sensitive user data as possible?

Secondary focus: co-design / usability (discoverability, trust, visual language, design iteration from community feedback).

## Preferred terminology

- mobile health navigation
- digital health
- health-resource access
- personalized health access *(use carefully)*
- context-aware health navigation
- location-aware health-resource discovery
- privacy by design / privacy-preserving
- data minimization
- on-device health information
- co-design / participatory design
- university health / university communities

## Avoid unless explicitly evidenced

- precision medicine / precision health
- clinical AI / intelligent diagnosis
- treatment recommendation / clinical decision support
- predictive healthcare
- improved patient outcomes / clinical efficacy

**“Personalized”** here means contextualized access based on user context (e.g. location) and locally held health information — **not** personalized medical treatment.

## Separate repositories

| Role | Location |
| --- | --- |
| This paper | This repo (`CWC Health`) |
| Flutter app (read-only truth for tech claims) | `~/Documents/Repos/rutgers-health-services-app` |
| Research corpus (do not copy into git) | `/Users/ks1686/rclone/School-Box/BHE RFP 2025-2026` |

**Agents:** Re-inspect the Flutter app before every technical edit. The study build changes; older handoff bullets (e.g. encrypted My Health, device GPS) may already be wrong. See `AGENTS.md` and `notes/claims-and-evidence.md`.
