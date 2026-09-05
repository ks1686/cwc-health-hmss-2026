# Claims and evidence

Map paper claims to supporting evidence before asserting them in `main.tex`.

**Re-verify rule:** The companion Flutter app changes often. Before editing technical prose, re-inspect that app’s current `README`, engineering docs, and relevant source. Update this table’s Status / Source columns when reality drifts. Do not treat a prior row as durable truth.

Do not invent participant counts, quotations, statistical results, IRB status, or clinical outcomes.

Snapshot date for rows below: **2026-09-03** (re-check before the next System Design edit).

| Claim | Kind | Evidence | Status |
| --- | --- | --- | --- |
| Flutter navigation prototype; four tabs + Help Now | As-built | Companion app README; app shell | Supported |
| No accounts / no stored credentials / no third-party analytics SDKs | As-built | Companion app README; runtime deps limited to http, url_launcher, shared_preferences | Supported |
| Nearby live listings via OSM Overpass behind `LIVE_NEARBY` (default off) | As-built | Companion app README; Nearby feature + engineering notes | Supported |
| Live Nearby geocodes a fixed town (New Brunswick) via Nominatim; no GPS path in v1 | As-built | Companion app README; Nearby live design | Supported |
| On-device Nearby cache: last-success list + town point only (no identity) | As-built | Nearby prefs cache; companion app README | Supported |
| Live Nearby never falls back to demo listings on failure | As-built | Companion app README; Nearby repository behavior | Supported |
| Live cards parse OSM opening_hours into Open now / Closed (expand weekdays) | As-built | Companion app hours control; engineering handoff | Supported |
| Overpass mirror failover for shared-IP rate limits | As-built | Companion app OSM source; engineering handoff | Supported |
| NJ bounding-box guard on live points | As-built | Companion app Overpass source | Supported |
| My Health / Learn / More largely static sample / placeholder in study build | As-built | Companion app README; demo data / placeholders | Supported |
| Help Now: `HELP_NOW_LIVE` gates 988/911/Poison `tel:`/`sms:`; warmline/CWC stay sample | As-built | Companion app README; Help Now feature | Supported |
| Encrypted on-device My Health storage | Spec / intended | Feature spec; not in study-build code | Do not claim as shipped |
| Optional PIN locking My Health | Spec / intended | Spec + UI “does not lock… yet”; Settings placeholder | Do not claim as shipped |
| Working one-tap erase of personal PHI | Spec / intended | Erase is still a demo message (“nothing… not saved”) | Do not claim as shipped |
| Device GPS / coarse one-shot location for Nearby | Prior assumption | Contradicted by as-built Nominatim town path | Do not claim for current study build |
| Empirical Stage-1 co-design / needs-assessment findings | Study | Pre-survey summary + FG theme tables (drafted into Results 2026-09-04) | Supported (Stage 1 only) |
| Stage-3 usability evaluation of Flutter build | Study | Not completed / not drafted | TODO |

## Candidate contributions (provisional)

1. Context-aware Nearby discovery that minimizes location retention (as-built: town geocode + OSM; no GPS tracking).
2. Privacy-oriented product without accounts or analytics; personal-health workspace as a design target progressing from demo data toward local-first storage.
3. Unified co-designed information architecture: Nearby, My Health, Learn, More, Help Now.
4. Empirical evaluation — assert only after sourced study evidence.


## Method / Results claims (2026-09-04)

| Claim | Kind | Evidence | Status |
| --- | --- | --- | --- |
| IRB Exempt 3b, Pro2025002116, approved 2025-11-19 | Ethics | Rutgers HRPP eIRB notice of approval | Supported |
| Five Stage-1 focus groups (2 virtual PSS, 3 in-person member) | Method | Focus group schedule; progress accomplishments list | Supported |
| Compensated FG attendance n=7 PSS (virtual), n=38 members (in person) | Method | Gift-card clearing sheet aggregates ($50); no names in manuscript | Supported |
| Pre-survey member demographics n=41; smartphone items ~n=27; PSS ~n=9–10 | Results | Group comparison / pre-survey summary (July) | Supported |
| Member/PSS qualitative themes (privacy, plain language, resource navigation, digital hesitancy, peer support) | Results | Member and PSS summary tables; July comparison narrative | Supported |
| Themes → four-tab study build + gated Help Now + town geocode Nearby | Design bridge | Progress accomplishments + companion app README (re-checked 2026-09-04) | Supported as design response |
| Stage-3 usability metrics (task completion, Help Now discoverability) | Study | Not in Stage-1 corpus | Do not claim yet |
