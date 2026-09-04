# Claims and evidence

Map paper claims to supporting evidence before asserting them in `main.tex`.

**Re-verify rule:** The app at `../rutgers-health-services-app` changes frequently. Before editing technical prose, re-open that repo’s `README.md`, `AGENTS.md`, `docs/engineering/`, and relevant `lib/` files. Update this table’s Status / Source columns when reality drifts. Do not treat a prior row as durable truth.

Do not invent participant counts, quotations, statistical results, IRB status, or clinical outcomes.

Snapshot date for rows below: **2026-09-03** (re-check before next System Design edit).

| Claim | Kind | Evidence | Status |
| --- | --- | --- | --- |
| Flutter navigation prototype; four tabs + Help Now | As-built | App `README.md`; `lib/shell/app_shell.dart` | Supported |
| No accounts / no stored credentials / no third-party analytics SDKs | As-built | App `README.md`; `pubspec.yaml` (http, url_launcher, shared_preferences only) | Supported |
| Nearby live listings via OSM Overpass behind `LIVE_NEARBY` (default off) | As-built | App `README.md`; `lib/features/nearby/`; `docs/engineering/nearby-live-data.md` | Supported |
| Live Nearby geocodes fixed town (New Brunswick) via Nominatim — **no GPS path in v1** | As-built | App `README.md`; nearby live design/docs | Supported |
| On-device Nearby cache: last-success list + town point only (no identity) | As-built | `lib/features/nearby/data/prefs_nearby_cache.dart`; README | Supported |
| Live Nearby never falls back to demo listings on failure | As-built | App `README.md`; nearby repository docs | Supported |
| My Health / Learn / More largely static sample / placeholder in study build | As-built | App `README.md`; `lib/data/demo_*.dart`; More placeholders | Supported |
| Help Now: `HELP_NOW_LIVE` gates 988/911/Poison `tel:`/`sms:`; warmline/CWC stay sample | As-built | App `README.md`; `lib/features/help_now/` | Supported |
| Encrypted on-device My Health storage | Spec / intended | Feature spec in `CWC_Health_App/`; **not in study-build code** | Do not claim as shipped |
| Optional PIN locking My Health | Spec / intended | Spec + UI “does not lock… yet”; Settings placeholder | Do not claim as shipped |
| Working one-tap erase of personal PHI | Spec / intended | More erase is demo snackbar (“nothing… not saved”) | Do not claim as shipped |
| Device GPS / coarse one-shot location for Nearby | Prior handoff assumption | Contradicted by as-built Nominatim town path | Do not claim for current study build |
| Empirical co-design / usability evaluation findings | Study | Box Focus Groups / IRB — not yet drafted into paper | TODO |

## Candidate contributions (provisional)

1. Context-aware Nearby discovery architecture minimizing location retention (as-built: town geocode + OSM; no GPS tracking).
2. Privacy-oriented product posture without accounts/analytics; personal-health workspace as a **design target** progressing from demo data toward local-first storage.
3. Unified co-designed IA: Nearby, My Health, Learn, More, Help Now.
4. Empirical evaluation — assert only after sourced study evidence.
