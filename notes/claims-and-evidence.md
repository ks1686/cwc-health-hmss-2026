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
| My Health / Learn / More largely static sample / placeholder in study build | As-built | Companion app README; demo data / placeholders | Supported |
| Help Now: `HELP_NOW_LIVE` gates 988/911/Poison `tel:`/`sms:`; warmline/CWC stay sample | As-built | Companion app README; Help Now feature | Supported |
| Encrypted on-device My Health storage | Spec / intended | Feature spec; not in study-build code | Do not claim as shipped |
| Optional PIN locking My Health | Spec / intended | Spec + UI “does not lock… yet”; Settings placeholder | Do not claim as shipped |
| Working one-tap erase of personal PHI | Spec / intended | Erase is still a demo message (“nothing… not saved”) | Do not claim as shipped |
| Device GPS / coarse one-shot location for Nearby | Prior assumption | Contradicted by as-built Nominatim town path | Do not claim for current study build |
| Empirical co-design / usability evaluation findings | Study | Team study materials (not yet drafted into paper) | TODO |

## Candidate contributions (provisional)

1. Context-aware Nearby discovery that minimizes location retention (as-built: town geocode + OSM; no GPS tracking).
2. Privacy-oriented product without accounts or analytics; personal-health workspace as a design target progressing from demo data toward local-first storage.
3. Unified co-designed information architecture: Nearby, My Health, Learn, More, Help Now.
4. Empirical evaluation — assert only after sourced study evidence.
