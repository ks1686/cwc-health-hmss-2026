# Claims and evidence

Map paper claims to supporting evidence before asserting them in `main.tex`.

**Re-verify rule:** The companion Flutter app changes often. Before editing technical prose, re-inspect that app’s current `README`, engineering docs, and relevant source. Update this table’s Status / Source columns when reality drifts. Do not treat a prior row as durable truth.

Do not invent participant counts, quotations, statistical results, IRB status, or clinical outcomes.

**Framing:** The manuscript describes the researched **future product** / Figma planned service grounded in Stage~1. Engineering demo notes are secondary evidence that the same shell can be exercised. Snapshot date for rows below: **2026-09-05** (companion audit @ `5464776`; re-check before the next System Design edit).

| Claim | Kind | Evidence | Status |
| --- | --- | --- | --- |
| Flutter navigation product shell; four tabs + Help Now | Product / demo | Figma Final Design v1.1; companion app shell | Supported |
| No accounts / no stored credentials / no third-party analytics SDKs | Product / demo | Companion app README; runtime deps limited to http, url_launcher, shared_preferences (plus privacy libs as shipped) | Supported |
| Nearby is town-first; OSM Overpass behind `LIVE_NEARBY` | Product / demo | Product story + companion Nearby feature | Supported |
| Optional one-shot Use my location (coarse); no background tracking; no GPS history retention | Product | Product privacy story; companion can use coarse GPS + embedded maps when `LIVE_NEARBY=true` | Supported as product rule |
| On-device Nearby cache: last-success list + town/point only (no identity) | Product / demo | Nearby prefs cache; companion app README | Supported |
| Live Nearby never falls back to demo listings on failure | Product / demo | Companion Nearby repository behavior | Supported |
| Live cards parse OSM opening_hours; NJ bbox guard; Overpass mirror failover | Product / demo | Companion hours control / Overpass source | Supported |
| Google Places is optional soft-fail side path (not required middle step) | Product / demo | Companion Nearby design | Supported |
| My Health: on-device PIN, encrypted store, erase | Product (demo implements) | Companion audit @ `5464776`: PIN / encrypt / erase shipped | Supported as product capability |
| Help Now: urgent dialers (988/911/Poison) + local entries | Product | Figma + companion Help Now; demo may gate live `tel:`/`sms:` for meeting safety | Supported as product surface |
| Map browsing of requested Nearby results OK; not continuous surveillance | Product | Privacy narrative in manuscript | Supported as product rule |
| Empirical Stage-1 co-design / needs-assessment findings | Study | Pre-survey summary + FG theme tables | Supported (Stage 1 only) |
| Stage-3 usability evaluation of Flutter product | Study | Not completed / not drafted | TODO |

## Candidate contributions (provisional)

1. Context-aware Nearby discovery that minimizes location retention (town-first + optional one-shot location; no background GPS history).
2. Privacy-oriented product without accounts or analytics; on-device My Health with PIN, encrypted store, and erase.
3. Unified co-designed information architecture: Nearby, My Health, Learn, More, Help Now.
4. Empirical evaluation: assert only after sourced study evidence.

## Method / Results claims (2026-09-04)

| Claim | Kind | Evidence | Status |
| --- | --- | --- | --- |
| IRB Exempt 3b, Pro2025002116, approved 2025-11-19 | Ethics | Rutgers HRPP eIRB notice of approval | Supported |
| Five Stage-1 focus groups (2 virtual PSS, 3 in-person member) | Method | Focus group schedule; progress accomplishments list | Supported |
| Compensated FG attendance n=7 PSS (virtual), n=38 members (in person) | Method | Gift-card clearing sheet aggregates ($50); no names in manuscript | Supported |
| Pre-survey member demographics n=41; smartphone items ~n=27; PSS ~n=9-10 | Results | Group comparison / pre-survey summary (July) | Supported |
| Member/PSS qualitative themes (privacy, plain language, resource navigation, digital hesitancy, peer support) | Results | Member and PSS summary tables; July comparison narrative | Supported |
| Themes → four-tab planned product + Help Now + town-first Nearby | Design bridge | Figma + Stage-1 themes; companion demo implements shell (re-checked 2026-09-05) | Supported as design response |
| Stage-3 usability metrics (task completion, Help Now discoverability) | Study | Not in Stage-1 corpus | Do not claim yet |
