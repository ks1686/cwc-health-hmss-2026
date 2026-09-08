# Claims and evidence

Map paper claims to supporting evidence before asserting them in `main.tex`.

**Re-verify rule:** The companion Flutter app changes often. Before editing technical prose, re-inspect that app’s current `README`, engineering docs, and relevant source. Update this table’s Status / Source columns when reality drifts. Do not treat a prior row as durable truth.

Do not invent participant counts, quotations, statistical results, IRB status, or clinical outcomes.

**Framing:** The manuscript leads with the needs assessment and then presents the planned Flutter product that responds to those findings. Engineering evidence is secondary. Snapshot date for rows below: **2026-09-07** (companion `origin/main` audit @ `5464776`; re-check remote `main` before the next System Design edit).

| Claim | Kind | Evidence | Status |
| --- | --- | --- | --- |
| Flutter navigation product shell; four tabs + Help Now | Product / demo | Figma Final Design v1.1; companion app shell | Supported |
| No accounts / no stored credentials / no third-party analytics SDKs | Product / demo | Companion app README; runtime deps limited to http, url_launcher, shared_preferences (plus privacy libs as shipped) | Supported |
| Final Nearby design is town-first; OSM Overpass supplies live listings | Product target | Feature specification and product story | Supported as target behavior |
| Optional one-shot Use my location (coarse); no background tracking; coordinates remain in memory and are not retained | Product / demo | Product privacy requirements; companion live-location README and source | Supported |
| On-device Nearby cache: last-success town listings and geocoded town point only; no one-shot device origin or identity | Product / demo | Product privacy requirements; companion repository behavior at `5464776` | Supported |
| Current prototype live mode requests one-shot coarse location on load and falls back to the New Brunswick town path | Demo divergence | Companion README and Nearby source at `5464776` | Supported; do not describe as final entry flow |
| Live Nearby never falls back to demo listings on failure | Product / demo | Companion Nearby repository behavior | Supported |
| Live cards parse OSM opening_hours; NJ bbox guard; Overpass mirror failover | Product / demo | Companion hours control / Overpass source | Supported |
| Google Places is optional soft-fail side path (not required middle step) | Product / demo | Companion Nearby design | Supported |
| Final My Health design: optional PIN, encrypted on-device store, erase | Product target / demo | Product requirements; companion audit @ `5464776` confirms prototype implementation | Supported; no Stage-3 usability claim |
| Help Now: urgent dialers (988/911/Poison) + local entries | Product | Figma + companion Help Now; demo may gate live `tel:`/`sms:` for meeting safety | Supported as product surface |
| Map browsing of requested Nearby results OK; not continuous surveillance | Product | Privacy narrative in manuscript | Supported as product rule |
| Empirical co-design / needs-assessment findings | Study | Pre-survey summary + FG theme tables | Supported |
| Usability evaluation of Flutter product | Study | Not completed | Future work only |

## Candidate contributions (provisional)

1. Context-aware Nearby discovery that minimizes location retention (town-first + optional one-shot location; no background GPS history).
2. Privacy-oriented product without accounts or analytics; on-device My Health with optional PIN, encrypted store, and erase.
3. Unified co-designed information architecture: Nearby, My Health, Learn, More, Help Now.
4. Empirical evaluation: assert only after sourced study evidence.

## Method / Results claims (updated 2026-09-07)

| Claim | Kind | Evidence | Status |
| --- | --- | --- | --- |
| IRB Exempt 3b, Pro2025002116, approved 2025-11-19 | Ethics | Rutgers HRPP eIRB notice of approval | Supported |
| Eight focus groups (2 virtual PSS, 6 in-person member groups across 3 site days) | Method | Distinct Box recording/transcript records; progress summary uses site-session shorthand | Supported |
| Member-group sites: Glassboro, Jersey City, Plainfield | Method | Focus-group recording folders and site schedule | Supported |
| Compensated FG attendance n=7 PSS (virtual), n=38 members (in person) | Method | Gift-card clearing sheet aggregates ($50); no names in manuscript | Supported |
| Pre-survey member demographics n=41; smartphone items ~n=27; PSS ~n=9-10 | Results | Group comparison / pre-survey summary (July) | Supported |
| Member/PSS qualitative themes (privacy, plain language, resource navigation, digital hesitancy, peer support) | Results | Member and PSS summary tables; July comparison narrative | Supported |
| Themes → four-tab Flutter target + Help Now + town-first Nearby | Design bridge | Theme summaries, 2026-08-11 design summary, target requirements, and companion evidence | Supported as design response |
| Target users are adults who may experience poverty with mental health, substance-use, or co-occurring physical health challenges | Product / study | Final proposal research narrative | Supported |
| Four tabs are Nearby, My Health, Learn, and More; Help Now is persistent | Product | 2026-08-11 design summary and companion shell | Supported; do not merge Learn and More into one tab |
| Future testing will assess resource finding, personal-information tasks, Help Now, readability, trust, platform behavior, and peer training needs | Future study | Approved proposal and usability materials | Supported as planned work; do not claim results |
| Exact future usability sample differs across planning sources (proposal n=84; later meeting plan mentions 12 remote participants) | Future study | Proposal and 2026-09-07 meeting transcript | Unresolved; omit n until protocol is confirmed |
| Usability metrics (task completion, Help Now discoverability) | Study | Not in completed needs-assessment corpus | Do not claim yet |
