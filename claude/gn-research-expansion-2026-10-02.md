# GN container and lid research expansion — status note (2 Oct 2026)

Deliverable: `YES Market Research 2026-10-03.xlsx` (repository root). Base: "YES Market Research 2026-10-02.xlsx" (uploaded). Structure kept: Offers, Benchmarks, Review, Compare, Pricing, Change log (+ Sources note).
The Gastroplast supplier price list was **not** attached, so cost EUR and markup over cost are empty for the new rows (amber cells in Pricing column D are ready to be filled).

## 1. Shopify catalogue (read-only pull, 2 Oct 2026)

91 products with GNP-/GNPP-/GNPL-/GNPPL-/GNPS-/GNPPS- SKUs (full list with size, depth, material, lid type and colour: `claude/gn-shopify-catalogue-2026-10-02.csv`):

- 23 clear PC containers GNP-\<size\>\<depth\> and 23 black PC containers GNP-…/B (sizes 1/1, 1/2, 1/3, 1/4, 1/6 at 65/100/150/200 mm; 1/9 at 65/100/150 mm)
- 23 PP containers GNPP-… (same grid)
- 6 PC lids GNPL-11…19 and 6 PP lids GNPPL-11…19; all are plain flat tight-fit lids (no handle cut-out, no notch, no seal) per the product descriptions
- 10 drain shelves (GNPS-/GNPPS-): GN-sized but neither container nor lid → out of scope, listed for completeness
- No other GN-sized container or lid exists in the store (dome covers, serving trays and the thermobox are different product types).

Black and clear PC of the same size and depth are one benchmark (the workbook's existing rule: "colour unrestricted"); the matched YES SKU per offer carries "/B" for black competitor items.

## 2. To research vs already in file

**Already in file — skipped, rows untouched (13 variants):**
PC containers 1/1 65 mm, 1/1 100 mm, 1/2 150 mm, 1/3 100 mm, 1/6 100 mm · PP containers 1/1 65 mm, 1/2 150 mm, 1/3 100 mm, 1/6 100 mm, 1/9 100 mm · lids GN 1/1 PC, GN 1/1 PP, GN 1/3 PP.

**To research (45 variants, all done):**
- PC containers (18): 1/1 150, 1/1 200 · 1/2 65, 100, 200 · 1/3 65, 150, 200 · 1/4 65, 100, 150, 200 · 1/6 65, 150, 200 · 1/9 65, 100, 150
- PP containers (18): 1/1 100, 150, 200 · 1/2 65, 100, 200 · 1/3 65, 150, 200 · 1/4 65, 100, 150, 200 · 1/6 65, 150, 200 · 1/9 65, 150
- PC lids (5): 1/2, 1/3, 1/4, 1/6, 1/9 · PP lids (4): 1/2, 1/4, 1/6, 1/9

## 3. Method

- Live shop pages on 2 Oct 2026, read with the fetch tool or curl; where a shop renders prices with JavaScript (GGM Gastro, Intergastro, Nisbets, Gastromania) the page was loaded once in a plain headless browser. Shops that answered with a bot challenge or 403 were skipped and not worked around.
- Strict matching on GN size, depth and material (PC ≠ PP; stainless steel out of scope). EXACT = size, depth, material all stated; CLOSE = plastic type not stated, container bundled with lid, sealing/raised/allergen-colour lid of the right material; APPROX = other depth or material. Lids with handle cut-outs count as EXACT (workbook precedent).
- Net price per piece: gross prices divided by local VAT (AT 20 %, DE 19 %, CZ 21 %, SK 23 %, RO 21 %), pack prices divided by the pack count; EUR at the Erste mid-rates of 30 Sep 2026 already in the Sources sheet, rounded to 6 decimals (the workbook's own formulas do this; Python cross-check below).
- Research target applied: up to 7 offers per variant in AT/DE, 5 in CZ/SK/RO. The agents found 1,922 offers; 1,240 were recorded (one best offer per shop first — EXACT preferred, then cheapest — shops ordered by their coverage of the market, then further brand/colour rows up to the target). Every offer found, including the 681 beyond the target, is in `claude/gn-offers-raw-2026-10-02.csv` (column "selected").
- Curation applied before writing (logged in Change log): 28 offers downgraded EXACT → CLOSE (Intergastro PP lids whose page says only "Kunststoff"; shopbuero WAS GN 96 rows with depth inferred from the article number; GGM CZ items whose title says polypropylene while category and description say polycarbonate; TOMGAST M2-12100 with a 65/100 mm conflict; one Gastrofans item with a copied description); 1 offer dropped (GGM CZ GPCL16 lid, pack quantity not shown).

## 4. Results

| Market | Offers recorded | Shops used |
|---|---|---|
| Austria | 292 | shopbuero.com, Gastrodax, Intergastro (AT shop), GastroHero Österreich, ALLPAX Österreich, Gastro Star, Gastroladen.at, GGM Gastro (AT), Gastro Zimml, Jungheinrich PROFISHOP |
| Germany | 293 | Intergastro, Gastro-Spirit, GastroHero, Gastrodax [substitute], ALLPAX, Nisbets, Gastroladen.de [substitute], GGM Gastro |
| Czechia | 219 | Gastromania, Gastrofans, Gastrošance, TOMGAST, Gastrozone, Promos Gastro, Gastro Novotný, GGM Gastro (CZ) |
| Slovakia | 217 | Profikuchyna.sk (new), Gastromania.sk, Gastrozone.sk, GastroREX.sk (new), Gastroalka.sk (new), Masiarskenaradie.sk (new), GGM Gastro (SK storefront, new) |
| Romania | 219 | mmgastro, Gastrozone, Direca, FiMax, Lancom, GGM Gastro (RO storefront, new), Pro-cucina, Horecamag |
| **Total** | **1,240** | 1,174 EXACT · 63 CLOSE · 3 APPROX |

Coverage: 223 of 225 variant × market cells have offers.
- **No usable offer:** GN 1/9 PC container 150 mm in Austria and Germany (no shop in either market lists a 1/9 polycarbonate deeper than 100 mm).
- **Fewer than 3 offers (extra −5 % applied by the Pricing logic):** GN 1/9 PC container 150 mm in CZ, SK and RO (2 each).
- Every other cell has 5 (CZ/SK/RO) or 7 (AT/DE) offers.

**Blocked / unusable shops (skipped, not worked around):** LUSINI Österreich and LUSINI Deutschland (Cloudflare challenge, 403); Esmeyer Shop (403); hendi.ro (connection failure / 502) and gastroprofesional.ro (Cloudflare block); in Slovakia hendi.sk, tomgast.sk, gastroshop.sk, gastroprodukt.sk, gastro-obchod.sk, gastrotrend.sk, horecaworld.sk (certificate / 502 errors), METRO.sk and GastroMarket.sk (known bot challenge). expondo Österreich, Magora and Stylehoreca are reachable but carry no plastic GN range; Patiser.ro shows placeholder prices and was not used.

**Shops named as "blocked" in the brief that were in fact readable today and were used:** Gastrozone (CZ/SK/RO storefronts answered the fetch tool directly), Gastromania (CZ/SK; the CZ site answers 503 to the simple fetch tool but serves the page to a browser) and Intergastro AT (JavaScript-rendered prices). Their rows are marked "page read with a headless browser" in the Offers notes where applicable; filter on the Competitor column to remove them if they should stay excluded.

**Thin-margin flags (markup < +50 % at the entry price):** none can be computed — the price list was not attached, so cost is empty for all 45 new rows. Entry prices do not depend on cost while the minimum-markup input (Pricing C10) is 0.

## 5. Entry prices (EUR net per piece, Pricing sheet, EXACT + CLOSE filter, median statistic)

n = offers counted; entry = market-entry price from the existing logic (cheapest −5 %; outlier → median −25 %; never above median −25 %; extra −5 % with < 3 offers; rounded down to 0.05 / 0.10 / 1).

| Product | AT n / entry | DE n / entry | CZ n / entry | SK n / entry | RO n / entry |
|---|---|---|---|---|---|
| GN 1/1 PC container, 150 mm | 7 / 12.20 | 7 / 13.20 | 5 / 11.20 | 5 / 11.40 | 5 / 11.90 |
| GN 1/1 PC container, 200 mm | 7 / 19.40 | 7 / 16.80 | 5 / 13.20 | 5 / 13.40 | 5 / 15 |
| GN 1/2 PC container, 65 mm | 7 / 5.30 | 7 / 4.60 | 5 / 4.05 | 5 / 4.60 | 5 / 4.60 |
| GN 1/2 PC container, 100 mm | 7 / 5.60 | 7 / 5.30 | 5 / 4.50 | 5 / 5.05 | 5 / 5.20 |
| GN 1/2 PC container, 200 mm | 7 / 8.75 | 7 / 8.35 | 5 / 7.50 | 5 / 7.10 | 5 / 8 |
| GN 1/3 PC container, 65 mm | 7 / 4.20 | 7 / 3.65 | 5 / 3.10 | 5 / 3.50 | 5 / 3.55 |
| GN 1/3 PC container, 150 mm | 7 / 5.20 | 7 / 5.15 | 5 / 6.50 | 5 / 4.20 | 5 / 5.45 |
| GN 1/3 PC container, 200 mm | 7 / 7.45 | 7 / 5.45 | 5 / 7.10 | 5 / 6.80 | 5 / 6.45 |
| GN 1/4 PC container, 65 mm | 7 / 4.20 | 7 / 3.30 | 5 / 2.70 | 5 / 2.35 | 5 / 2.90 |
| GN 1/4 PC container, 100 mm | 7 / 3.55 | 7 / 3.40 | 5 / 2.95 | 5 / 3.05 | 5 / 3.20 |
| GN 1/4 PC container, 150 mm | 7 / 4.70 | 7 / 4.10 | 5 / 3.70 | 5 / 3.55 | 5 / 3.45 |
| GN 1/4 PC container, 200 mm | 7 / 7.40 | 7 / 6.80 | 3 / 4.50 | 4 / 5.80 | 4 / 4.85 |
| GN 1/6 PC container, 65 mm | 7 / 2.50 | 7 / 2.35 | 5 / 1.80 | 5 / 1.80 | 5 / 1.50 |
| GN 1/6 PC container, 150 mm | 7 / 3.60 | 7 / 3.25 | 5 / 3.10 | 5 / 2.60 | 5 / 2.95 |
| GN 1/6 PC container, 200 mm | 7 / 5.50 | 7 / 5.30 | 5 / 2.60 | 5 / 4.50 | 5 / 4.15 |
| GN 1/9 PC container, 65 mm | 7 / 2.70 | 7 / 1.65 | 5 / 1.60 | 5 / 1.70 | 5 / 1.40 |
| GN 1/9 PC container, 100 mm | 7 / 3 | 7 / 1.95 | 5 / 3.10 | 5 / 1.60 | 5 / 1.50 |
| GN 1/9 PC container, 150 mm | 0 / — | 0 / — | 2 / 4.40 | 2 / 4 | 2 / 2.40 |
| GN 1/1 PP container, 100 mm | 7 / 10.80 | 7 / 8.30 | 5 / 8 | 5 / 9 | 5 / 6.90 |
| GN 1/1 PP container, 150 mm | 7 / 10.90 | 7 / 7.95 | 5 / 10.80 | 5 / 8.45 | 5 / 9.15 |
| GN 1/1 PP container, 200 mm | 7 / 13.10 | 7 / 11 | 5 / 11.90 | 5 / 10 | 5 / 10.50 |
| GN 1/2 PP container, 65 mm | 4 / 3.20 | 7 / 2.75 | 5 / 3.05 | 4 / 2.95 | 5 / 3.45 |
| GN 1/2 PP container, 100 mm | 7 / 5.30 | 7 / 3.75 | 5 / 3.90 | 5 / 4.50 | 5 / 5.10 |
| GN 1/2 PP container, 200 mm | 7 / 5.70 | 7 / 5.35 | 5 / 7.65 | 5 / 5.50 | 5 / 5.65 |
| GN 1/3 PP container, 65 mm | 6 / 3.85 | 7 / 2.75 | 5 / 2.70 | 5 / 3.30 | 5 / 3.05 |
| GN 1/3 PP container, 150 mm | 7 / 4.35 | 7 / 4.30 | 5 / 3.90 | 5 / 4.75 | 5 / 4.10 |
| GN 1/3 PP container, 200 mm | 6 / 5 | 4 / 5.15 | 5 / 6.45 | 5 / 4.65 | 5 / 4.95 |
| GN 1/4 PP container, 65 mm | 4 / 4.20 | 6 / 2.70 | 5 / 2.65 | 5 / 2.70 | 5 / 2.60 |
| GN 1/4 PP container, 100 mm | 7 / 2.65 | 7 / 2.75 | 5 / 3.35 | 5 / 3 | 5 / 2.90 |
| GN 1/4 PP container, 150 mm | 7 / 3.90 | 7 / 3.40 | 5 / 3.95 | 5 / 4.10 | 5 / 2.90 |
| GN 1/4 PP container, 200 mm | 7 / 4.50 | 6 / 4.40 | 5 / 4.80 | 5 / 5.35 | 4 / 4.45 |
| GN 1/6 PP container, 65 mm | 6 / 2.50 | 7 / 1.70 | 5 / 2.70 | 5 / 2.15 | 5 / 2 |
| GN 1/6 PP container, 150 mm | 7 / 2.65 | 7 / 2.25 | 5 / 3.85 | 5 / 2.55 | 5 / 2.85 |
| GN 1/6 PP container, 200 mm | 5 / 3.55 | 4 / 3.90 | 5 / 3.75 | 5 / 4.85 | 4 / 3.75 |
| GN 1/9 PP container, 65 mm | 6 / 3.20 | 6 / 2.35 | 5 / 2.20 | 4 / 2 | 5 / 1.75 |
| GN 1/9 PP container, 150 mm | 4 / 3.85 | 3 / 3.70 | 4 / 4.65 | 4 / 2.90 | 5 / 3.30 |
| GN 1/2 PC lid | 7 / 3.80 | 7 / 3.50 | 5 / 5.40 | 5 / 4.50 | 5 / 3.45 |
| GN 1/3 PC lid | 7 / 3.05 | 7 / 2.95 | 5 / 3.80 | 5 / 3.05 | 5 / 1.95 |
| GN 1/4 PC lid | 7 / 2.35 | 7 / 2.30 | 5 / 1.85 | 5 / 2.45 | 5 / 2.10 |
| GN 1/6 PC lid | 7 / 1.85 | 7 / 1.65 | 5 / 1.40 | 5 / 1.60 | 5 / 1.20 |
| GN 1/9 PC lid | 7 / 1.55 | 7 / 1.30 | 5 / 1.20 | 5 / 1.40 | 5 / 1.10 |
| GN 1/2 PP lid | 7 / 3.15 | 7 / 2 | 4 / 3.60 | 5 / 2.25 | 5 / 2.20 |
| GN 1/4 PP lid | 7 / 1.50 | 7 / 1.50 | 4 / 2 | 5 / 1.45 | 5 / 1.35 |
| GN 1/6 PP lid | 7 / 1.50 | 7 / 1.50 | 5 / 1.60 | 5 / 1.10 | 5 / 0.95 |
| GN 1/9 PP lid | 6 / 1.55 | 5 / 1.30 | 4 / 1.20 | 4 / 1 | 5 / 1.70 |

Basis breakdown across the 225 cells: 111 "median (cheapest is an outlier)", 88 "undercut cheapest", 24 "median", 2 no offers. The high share of outlier cases reflects GGM pack prices, Nisbets clearance prices and Gastrozone/Araven 3–5-week items sitting far below the median; the logic leaves those alone as designed.

## 6. Workbook changes (all logged in Change log rows 51–140)

- Offers: 1,240 rows appended (rows 870–2109) with the standard formulas (net/pc, EUR, filter flag, rank). Source file "Claude research 02.10.2026 (live shop pages)", checked by Claude, date 2026-10-02.
- Benchmarks: 45 rows (42–86). Review: 270 rows (217–486, product × 6 markets). Compare: 45 product rows (47–91); the research-dates block moved to rows 93–103. Pricing: 45 rows (50–94) with the market-entry formulas copied from row 49; notes moved to rows 96–103.
- Formula ranges widened from Offers rows 7–1000 to 7–3000 and Review rows 7–216 to 7–600 (4,066 formulas; conditional formats and the four Excel tables extended). Values of existing rows unchanged.
- Recalculated with LibreOffice: 26,377 formulas, **0 errors, 0 formula strings left as text**.
- Independent Python cross-check of every new Offers row (net per piece, EUR), every new Review row (min/median/max local and EUR), every new Compare cell and every new Pricing cell (count, cheapest, median, max, basis, entry price): **0 mismatches**.

## 7. Caveats

- Several Austrian-facing storefronts quote German VAT (GGM de-at, GastroHero AT, Gastrodax, shopbuero); net prices were read directly so per-piece nets are right, the source VAT rate is kept as shown.
- GGM storefronts sell 6/12-packs with most 12-packs "available from 19 Oct 2026"; prices are per-piece conversions of the pack price.
- Gastro Novotný (CZ) is "na dotaz" for most items; Gastrozone Araven items are 3–5-week orders with prepayment; ALLPAX black PC partly pre-order (KW 49/2026, KW 05/2027). Availability is in the "In stock?" column.
- Intergastro AT/DE depth variants and shopbuero WAS series were read from the shops' own product data (variant endpoints / product JSON), noted per row.

Files: `YES Market Research 2026-10-03.xlsx`, `claude/gn-offers-raw-2026-10-02.csv` (all 1,921 offers found, with the selection flag), `claude/gn-entry-prices-2026-10-02.csv`, `claude/gn-shopify-catalogue-2026-10-02.csv`.
