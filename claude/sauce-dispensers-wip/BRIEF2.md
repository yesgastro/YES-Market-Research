# YES Gastro sauce-dispenser research brief (2 Oct 2026)

YES Gastro (Budapest, B2B HoReCa supplier) benchmarks competitor NET prices per piece in Austria (AT), Germany (DE), Czechia (CZ),
Slovakia (SK) and Romania (RO). This round: squeeze bottles, shakers and pump dispensers. Date checked for every row: 2026-10-02.
Be economical: use category/listing pages that show many bottles at once, open product pages only to confirm material, tip type, volume, VAT basis.

## Variants TO RESEARCH (34). Use EXACTLY these strings in the CSV "product" column.
Squeeze bottles, standard neck, PE body, clear (YES: "Material: PE", -40/+99 C):
  Squeeze bottle 250 ml, PE, rotatable tip (GPSM-250) · Squeeze bottle 500 ml, PE, rotatable tip (GPSM-500) · Squeeze bottle 750 ml, PE, rotatable tip (GPSM-750) · Squeeze bottle 1,000 ml, PE, rotatable tip (GPSM-1000)
     = squeeze bottle whose nozzle/tip can be rotated or swivelled ("drehbare Spitze", "otočná tryska", "vârf rotativ"); a plain standard single-tip bottle of the same volume is CLOSE.
  Squeeze bottle 250 ml, PE, covered tip (GPSC-250) · Squeeze bottle 500 ml, PE, covered tip (GPSC-500) · Squeeze bottle 750 ml, PE, covered tip (GPSC-750) · Squeeze bottle 1,000 ml, PE, covered tip (GPSC-1000)
     = standard squeeze bottle with a cap/closure over the tip ("mit Verschlusskappe", "s uzávěrem/krytkou", "cu capac"); non-leak cap.
Wide-mouth (wide filling opening) squeeze bottles, PP/PE:
  Squeeze bottle 750 ml, triple tip (GBT-750) · Squeeze bottle 1,000 ml, triple tip (GBT-1000)   = three nozzles ("3-fach", "3 trysky", "3 orificii")
  Squeeze bottle 500 ml, PP/PE, wide covered tip (GBC-500) · Squeeze bottle 1,000 ml, PP/PE, wide covered tip (GBC-1000)  = wide-mouth bottle with covered nozzle
  Squeeze bottle 500 ml, PP/PE, silicone tip (GBS-500) · Squeeze bottle 750 ml, PP/PE, silicone tip (GBS-750) · Squeeze bottle 1,000 ml, PP/PE, silicone tip (GBS-1000) = silicone nozzle / silicone valve tip ("Silikonspitze", "silikonová tryska/ventil", "vârf silicon")
Bottom-fill (dual-opening) squeeze bottles — opening at the bottom for refilling (FIFO-type; competitor "FIFO bottle" 473/591/710/946 ml are CLOSE on volume, APPROX if far):
  Squeeze bottle 500 ml, triple tip, bottom-fill lid (GBT2-500) · Squeeze bottle 750 ml, triple tip, bottom-fill lid (GBT2-750) · Squeeze bottle 1,000 ml, triple tip, bottom-fill lid (GBT2-1000)
  Squeeze bottle 500 ml, covered tip, bottom-fill lid (GBC2-500) · Squeeze bottle 750 ml, covered tip, bottom-fill lid (GBC2-750) · Squeeze bottle 1,000 ml, covered tip, bottom-fill lid (GBC2-1000)
  Squeeze bottle 500 ml, silicone tip, bottom-fill lid (GBS2-500) · Squeeze bottle 750 ml, silicone tip, bottom-fill lid (GBS2-750) · Squeeze bottle 1,000 ml, silicone tip, bottom-fill lid (GBS2-1000)
Oil bottles: Oil squeeze bottle 500 ml, PP (GY-500) · Oil squeeze bottle 1,000 ml, PP (GY-1000) = squeeze/dispensing bottle sold for oil ("Ölflasche/Öl-Dosierflasche Kunststoff", "láhev na olej", "sticlă ulei"); plastic squeeze type, not glass/steel.
Shakers, PP/PE, wide mouth, plastic: Seasoning shaker 500 ml, PP/PE (GS-500) · Seasoning shaker 750 ml, PP/PE (GS-750) · Seasoning shaker 1,000 ml, PP/PE (GS-1000) = "Gewürzstreuer/Streudose Kunststoff", "kořenka/dávkovač koření plast", "solniță/presărător condimente plastic"
  Salt and pepper shaker 500 ml, PP/PE (GSP-500) · Salt and pepper shaker 750 ml, PP/PE (GSP-750) · Salt and pepper shaker 1,000 ml, PP/PE (GSP-1000) = large plastic salt/pepper shaker ("Salzstreuer Kunststoff"); perforated lid.
Pump dispensers: Sauce dispenser pump 20 ml, PP (GDP-01) = spare/replacement pump for sauce dispensers, ~20-30 ml per push ("Ersatzpumpe für Saucenspender", "náhradní pumpa", "pompă de rezervă")
  Double sauce dispenser 2 + 2 L, PP/ABS (GDP-02) = two-container pump dispenser, 2 x ~2 L, plastic (PP containers, ABS housing); stainless double dispensers = APPROX.

## SKIPPED (already in the workbook — never record): PP single-tip squeeze bottles 250/500/750/1,000 ml (any colour), 500 ml triple tip, 750 ml wide covered tip,
2 L ketchup/mustard/mayo pump dispenser with or without stand (single container). Also out of scope: glass, stainless steel, bowls.

## Matching rules ("match")
- EXACT: volume within ±10 %, tip/type as described, plastic (PP or PE or PP/PE) stated or clearly a plastic squeeze bottle. Colour free.
- CLOSE: volume 10-25 % off, OR tip type slightly different but same family (e.g. plain single tip for "rotatable tip"; FIFO 473 ml for 500 ml bottom-fill), OR material not stated.
- APPROX: volume >25 % off or a different family (standard bottle for a bottom-fill type, stainless double dispenser). At most ONE APPROX per shop per variant, only when nothing better exists.

## Price rules
- "price_shown" as on the page; "vat_basis" = "incl." or "excl."; VAT: AT 0.2, DE 0.19, CZ 0.21, SK 0.23, RO 0.21.
- pack_size = count when the price is for a pack/set (price_basis "per pack"), else 1 and "per piece". Single-piece price preferred; tiers in the note.
- Current (promo) price recorded, regular price in the note. Out of stock may be recorded with the stock text.

## Tools
1. WebFetch or curl first. 2. If 403/503 or JS-rendered prices (GGM Gastro, Gastromania, Intergastro, Nisbets): `node /tmp/claude-0/-home-user-YES-Market-Research/caa99c21-76ce-5edd-a73a-8ffba06512e2/scratchpad/render.js "<url>" 20000` (visible text). fetch_method = "browser".
3. Cloudflare challenge / captcha / 403 even in the browser = blocked: skip, note it, do not work around. Known blocked: LUSINI (lusini.com), Esmeyer, hendi.ro, gastroprofesional.ro, METRO, GastroMarket.sk.
4. No search-engine snippets as price evidence. Live shop pages only.
5. Put helper files ONLY under /tmp/claude-0/-home-user-YES-Market-Research/caa99c21-76ce-5edd-a73a-8ffba06512e2/scratchpad/<your market>/ — never in /home/user/YES-Market-Research and never overwrite other agents' files.

## Output CSV columns (UTF-8, header, comma separated, quote fields with commas):
market,shop,url,product_name,brand,capacity_ml,material,tip_type,colour,pack_size,price_shown,currency,vat_basis,vat_rate,price_basis,match,matching_note,stock,yes_sku,product,date_checked,fetch_method
- market: Austria | Germany | Czech | Slovakia | Romania  - capacity_ml numeric  - material: PE | PP | PP/PE | LDPE | "other: ..." | "not stated"
- tip_type: single | rotatable | covered | triple | silicone | wide covered | bottom-fill ... (free text, short)  - currency EUR | CZK | RON
- matching_note: one sentence on why EXACT/CLOSE/APPROX, plus code, regular price, tiers, VAT wording.
Also a short notes markdown: shops checked, blocked (URL + what it showed), shops with no range, oddities. Write the CSV incrementally.
Quality over quantity; do not invent prices.
