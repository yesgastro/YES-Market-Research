import csv, glob, re, sys
from collections import Counter, defaultdict
FX = {'EUR': 1.0, 'CZK': 366.11/14.99, 'RON': 366.11/69.37}
CAP = {'Austria': 7, 'Germany': 7, 'Czech': 5, 'Slovakia': 5, 'Romania': 5}
files = sys.argv[1:] or sorted(glob.glob('out2/offers_*.csv'))
rows = []
for f in files:
    for r in csv.DictReader(open(f, encoding='utf-8')):
        r['_f'] = f; r['curation'] = ''; r['selected'] = ''; rows.append(r)
actions = []
def downgrade(r, reason):
    if r['match'] == 'EXACT':
        r['match'] = 'CLOSE'; r['curation'] = 'downgraded EXACT->CLOSE: ' + reason
        r['matching_note'] = 'CLOSE (curated): ' + reason + ' | ' + r['matching_note']; actions.append(('downgrade', r, reason))
def drop(r, reason): r['curation'] = 'dropped: ' + reason; actions.append(('drop', r, reason))
def vol(p):
    m = re.search(r'([\d,]+) ml', p); return int(m.group(1).replace(',', '')) if m else None
for r in rows:
    nl = r['matching_note'].lower()
    try: cap = float(r['capacity_ml'] or 0)
    except ValueError: cap = 0
    v = vol(r['product'])
    if v and cap and r['match'] == 'EXACT':
        dev = abs(cap - v) / v
        if dev > 0.25: drop(r, f'volume {cap:g} ml is more than 25% off {v} ml but recorded EXACT')
        elif dev > 0.10: downgrade(r, f'volume {cap:g} ml is {dev:.0%} off {v} ml')
    if r['match'] == 'EXACT' and r['material'].strip().lower() in ('not stated', '', 'plast', 'kunststoff', 'plastic'): downgrade(r, 'plastic type not stated on the page')
    if r['match'] == 'EXACT' and ('flag' in nl or 'uncertain' in nl or 'unclear' in nl): downgrade(r, 'researcher flagged an uncertainty (see note)')
    if 'pack quantity not shown' in nl or 'no pack quantity' in nl: drop(r, 'pack quantity not shown on the page, per-piece price uncertain')
    r['spec_txt'] = f"{cap:g} ml" if cap else r['product']
    r['spec_txt'] += f", {r['material']}" if r['material'] else ''
    r['spec_txt'] += f", {r['tip_type']} tip" if r['tip_type'] else ''
    r['spec_txt'] += f", {r['colour']}" if r['colour'] else ''
rows = [r for r in rows if not r['curation'].startswith('dropped')]
for r in rows:
    p = float(r['price_shown']); q = float(r['vat_rate']); ps = int(float(r['pack_size'] or 1))
    net = round((p/(1+q) if r['vat_basis'] == 'incl.' else p)/(ps if r['price_basis'] == 'per pack' else 1), 2)
    r['_net_eur'] = round(net/FX[r['currency']], 6)
MR = {'EXACT': 0, 'CLOSE': 1, 'APPROX': 2}
coverage = Counter((r['market'], r['shop']) for r in rows)
groups = defaultdict(list)
for r in rows: groups[(r['product'], r['market'])].append(r)
selected = []; trimmed = []
for (p, m), g in groups.items():
    cap = CAP[m]; byshop = defaultdict(list)
    for r in g: byshop[r['shop']].append(r)
    for s in byshop: byshop[s].sort(key=lambda r: (MR[r['match']], r['_net_eur']))
    shops = sorted(byshop, key=lambda s: (-coverage[(m, s)], s))
    picked = [byshop[s][0] for s in shops][:cap]
    if len(picked) < cap:
        rest = [r for s in shops for r in byshop[s][1:]]; rest.sort(key=lambda r: (MR[r['match']], -coverage[(m, r['shop'])], r['_net_eur']))
        picked += rest[:cap - len(picked)]
    ids = set(id(r) for r in picked)
    for r in g:
        if id(r) in ids: r['selected'] = 'yes'; selected.append(r)
        else: r['selected'] = 'no (over the target count)'; trimmed.append(r)
cols = [c for c in rows[0].keys() if not c.startswith('_')]
with open('out2/combined.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore'); w.writeheader(); [w.writerow(r) for r in selected]
with open('out2/raw_all.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols + ['_net_eur'], extrasaction='ignore'); w.writeheader(); [w.writerow(r) for r in rows]
with open('out2/changelog_extra.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f); w.writerow(['sheet', 'row', 'market', 'competitor', 'product', 'field', 'old', 'new', 'evidence', 'reason'])
    for kind, r, reason in actions:
        if kind == 'downgrade': w.writerow(['Offers', 'appended', r['market'], r['shop'], r['product'], 'Match', 'EXACT (as researched)', 'CLOSE', r['url'], reason])
        else: w.writerow(['Offers', 'not added', r['market'], r['shop'], r['product'], 'Row', f"offer found ({r['price_shown']} {r['currency']})", 'not recorded', r['url'], reason])
    w.writerow(['Offers', 'not added', 'AT / DE / CZ / SK / RO', 'various', 'sauce-dispenser variants', 'Rows beyond the target count', f'{len(trimmed)} further offers found', 'kept in claude/sauce-offers-raw-2026-10-02.csv (repository)', '—',
                'Research target: up to 7 offers per variant in AT/DE, 3-5 in CZ/SK/RO. One best offer per shop (EXACT preferred, then cheapest) kept first, shops ordered by market coverage; further rows filled up to the target.'])
print('files', files, 'rows', len(rows) + sum(1 for a in actions if a[0] == 'drop'), 'selected', len(selected), 'trimmed', len(trimmed), 'downgrades', sum(1 for a in actions if a[0] == 'downgrade'), 'drops', sum(1 for a in actions if a[0] == 'drop'))
print('per market', dict(Counter(r['market'] for r in selected))); print('match', dict(Counter(r['match'] for r in selected)))
cells = Counter((r['product'], r['market']) for r in selected); print('cells', len(cells), 'under 3:', sorted((k, v) for k, v in cells.items() if v < 3))
