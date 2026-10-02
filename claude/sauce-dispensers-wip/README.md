# Sauce-dispenser research — work in progress (paused 2 Oct 2026, 10:50 UTC)

Research on the Shopify "Sauce Dispensers" collection was started and stopped on request after about 12 minutes.
Nothing from this folder is in the workbook yet.

- offers_AT.csv (25 rows: ALLPAX Österreich, GastroHero Österreich), offers_DE.csv (3 rows: Gastro-Spirit), offers_CZ.csv (13 rows: Gastrofans) — raw agent output, not yet curated. Slovakia and Romania: nothing yet.
- BRIEF2.md — the research brief (34 variants to research, 8 skipped, matching and price rules, CSV schema).
- spec_sauce.json — benchmark specifications for the 34 variants (used by build2.py).
- build2.py — appends a product family to the workbook: `python3 build2.py "<base.xlsx>" combined.csv spec_sauce.json out.xlsx [changelog_extra.csv]`; base = "YES Market Research 2026-10-03.xlsx".
- combine2.py — curates/trims the agent CSVs into combined.csv (+ raw_all.csv, changelog_extra.csv). Note: CZ product strings carry a "(SKU)" suffix that must be stripped first.
- verify.py — independent recomputation of the new rows after LibreOffice recalculation (expects 0 mismatches).
- render.js — headless-browser page renderer used for JavaScript-priced shops (needs Playwright's Chromium).

To resume: relaunch the per-market research for the remaining shops, append new rows to the CSVs, then run combine2.py → build2.py → recalc → verify.py.
