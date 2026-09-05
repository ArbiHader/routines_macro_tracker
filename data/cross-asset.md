# cross-asset readings — run 2026-09-05
fetcher: cross-asset

### dxy
source:  ICE DXY (DX-Y.NYB) — no free unauthenticated endpoint exists, so multiple search-indexed / lightly-rendered pages were used and cross-checked: tradingeconomics.com/dxy:cur (direct fetch), investing.com/indices/usdollar-historical-data (direct fetch, daily table), and a WebSearch snippet citing a Sept-5 level. Labeled secondary per spec since none is the ICE terminal itself.
series:
  - as_of: 2026-08-31 · 99.43 (investing.com historical table)
  - as_of: 2026-09-01 · 99.68 (investing.com historical table)
  - as_of: 2026-09-02 · 99.60 (investing.com historical table)
  - as_of: 2026-09-03 · 98.91 (investing.com historical table, -0.69% day)
  - as_of: 2026-09-04 · 99.18 (investing.com historical table, +0.27% day) / 99.176 (tradingeconomics.com, "this Friday September 4th," +0.268/+0.27%) — two sources agree within 0.01
conflict: a WebSearch snippet (unnamed page) claims "the dollar index (DXY) climbed 0.25% to 99.157 on September 5, 2026," attributing the move to an August jobs report (162,000 vs. 55,000 forecast) and rising Fed-hike odds. 2026-09-05 is a Saturday — FX/index markets are closed for new trading over the weekend, so a same-day "climbed to X" figure for Sept 5 is not consistent with a live market session; likely a stale/mis-dated snippet or an article written using Friday's (Sept 4) data under a Sept-5 dateline. Not used as the current reading; Sept 4's 99.18/99.176 (converging across two direct-fetched sources) stands as the latest confirmed close. Also note: the same snippet's claim that the jobs surprise raises "odds the Fed will raise interest rates this month" is inconsistent with the macro-monetary category's on-file fed-funds-path direction (a cut-oriented path) — flagging the discrepancy for the Reporter/Curator to reconcile with the macro-monetary Fetcher's read, not resolving it here.

### btc-nasdaq-corr
source:  Grayscale Research figures cited via Cointelegraph (direct-fetched summary of theblock.co/bloomingbit.io citation, published 2026-09-02 3:19pm) — bloomingbit.io/feed/news/119627 direct fetch succeeded and gave an exact publication date. K33 Research's 30-day-correlation figure cited via a WebSearch snippet (source article undated in the snippet, content otherwise matches known K33 September coverage). theblock.co/latest checked directly this run for a fresher dated print — none found beyond what's already on file.
window:  90-day rolling correlation of daily returns (Grayscale figure); a separately-scoped 30-day figure is also on record and kept distinct
series:
  - as_of: 2026-08-26 · 0.38 (38%), K33/The Block, described as a one-year low (carried from prior run, unchanged — no fresher K33 90-day print found this run)
  - as_of: 2026-09-02 · 0.33 (33%), Grayscale via Cointelegraph, down from 0.60 — exact publication timestamp (3:19pm) confirmed via direct fetch of bloomingbit.io this run
  - as_of: undated (~early Sept 2026, per WebSearch snippet, not independently re-dated this run) · K33's 30-day BTC-Nasdaq correlation "pushed above 0.7," described as a level previously seen only in major macro-driven periods (Apr/Oct 2022, Mar 2025) — a different window (30-day, not 90-day) from the Grayscale figure above, kept separate, not swapped in
conflict: none new this run. The 30-day K33 (>0.7) vs. 90-day Grayscale (0.33, falling) figures describe different windows and are not directly comparable — both are recorded as-is; reconciling what a rising 30-day correlation alongside a falling 90-day correlation implies is a Reporter-level read, not a Fetcher one. Could not obtain a fresher single dated print of the specific 90-day BTC-Nasdaq figure beyond 2026-09-02 (Grayscale) this run; a prior attempt to reach theblock.co/latest for a newer article found none.

### equity-valuation
source:  Shiller CAPE, multpl.com (direct fetch succeeded this run — https://www.multpl.com/shiller-pe and https://www.multpl.com/shiller-pe/table/by-month), the primary source named in the spec.
series:
  - as_of: 2026-09-04 (current daily reading, 4:00pm EDT) · 41.41 (-0.16, -0.39% on the day)
  - as_of: 2026-09-01 (September 2026 monthly print) · 40.90
  - as_of: 2026-08-01 (August 2026 monthly print) · 41.13
  - as_of: 2026-07-01 (July 2026 monthly print, extra context) · 40.02
conflict: none this run against the prior reading — prior run's current reading was 41.93 (as_of 2026-09-02); this run's 41.41 (as_of 2026-09-04) is a lower, later, and separately-fetched value from the same primary page, consistent with normal day-to-day index movement, not a source conflict. Note: this run's July-2026 monthly print (40.02) differs from the prior run's July print (40.73) and the prior run's June print (40.50) is not restated by this run's table fetch (August's print, 41.13, appears in its place) — the by-month table's reported values for a given month may be adjusted/updated between runs since CAPE uses trailing data; flagging the July figure's drift (40.73 → 40.02) for the Reporter rather than silently overwriting. Long-term mean/median from this run: 17.42 / 16.13 (prior run: 17.40 / 16.11 — trivial rounding drift, not a real conflict).

### gold
source:  spot gold — Kitco (kitco.com/charts/gold, direct fetch succeeded this run) plus a WebSearch snippet citing Yahoo Finance for Sept 4's close. BTC-gold correlation from the same Grayscale-via-Cointelegraph / bloomingbit.io citation used for btc-nasdaq-corr above (dated 2026-09-02).
series:
  - as_of: 2026-09-02 · $4,336.30/oz (carried from prior run's CNBC-sourced figure; not independently re-fetched this run)
  - as_of: 2026-09-03 · $4,480.90/oz (carried from prior run's Kitco direct fetch, +$93.90/+2.14% day, attributed to Iran re-escalation headlines)
  - as_of: 2026-09-04 · $4,420.00/oz (WebSearch snippet citing Yahoo Finance, down $57.10/-1.28% on the day, attributed to a stronger-than-expected August jobs report lifting yields/the dollar) — a separate same-day snippet cites gold futures (December contract) opening at $4,522/oz, a different instrument (futures vs. spot), not swapped in
  - as_of: 2026-09-05 (10:09am NY time, Kitco direct fetch) · $4,429.10/oz, -$43.10/-0.96% on the day — note: 2026-09-05 is a Saturday; spot gold/FX trade closes Friday ~5pm ET and reopens Sunday ~5pm ET, so a "current day" change figure fetched Saturday morning likely reflects a stale/cached page still showing Friday's session or a rollover artifact rather than live Saturday trading. A separate WebSearch snippet states gold markets are closed 2026-09-05/06 with the next trading day 2026-09-07 — flagging this Kitco read as unreliable for a genuinely new Sept-5 level; treat 2026-09-04's ~$4,420-4,429 range as the latest confirmed session close.
  - BTC-gold 90-day correlation, as_of: 2026-08-26 · 0.52 (K33/The Block, described as highest since October 2020) — carried from prior run
  - BTC-gold 90-day correlation, as_of: 2026-09-02 · ~0.50 ("rose to about 50%"), Grayscale via Cointelegraph (bloomingbit.io direct fetch, same citation as btc-nasdaq-corr's 2026-09-02 entry, exact publication timestamp 3:19pm confirmed this run)
conflict: gold's Sept-3 to Sept-4 move (~$4,480.90 → ~$4,420-4,429, a ~1.3-2% pullback) reverses part of the Sept-2→Sept-3 Iran-driven spike already on file; both directions are now attributed to distinct same-day news narratives (Iran re-escalation on the way up, a strong jobs report lifting yields/dollar on the way down) rather than being unexplained. The Sept-5 Kitco read is flagged above as likely stale (weekend) rather than a genuine new print — do not treat $4,429.10 as a fresher number than Sept-4's close.

### boj-carry-trade
source:  Bank of Japan July 31 policy statement (carried from prior run, unchanged this run) + USD/JPY spot (exchangerate-api.com direct fetch this run, cross-checked against a WebSearch-cited mitrade.com analysis piece dated with a Sept-4 14:50 timestamp in its URL) + primary-adjacent coverage of carry-trade positioning and rate-hike odds (mitrade.com direct fetch succeeded; cnbc.com's named Sept-3 article on yen/intervention 403'd on direct fetch this run, so that specific CNBC piece's content is NOT independently re-confirmed this run beyond what search snippets already carried).
series:
  - as_of: 2026-07-31 · status: BOJ held its policy rate steady at 1% (highest since 1995); vote 8-1, sole dissenter Takata proposed a hike to 1.25%; statement flagged core inflation likely to exceed 2% "from September" (carried from prior run, unchanged).
  - as_of: 2026-08-26/27 · status: Himino said the BOJ "should continue to raise" its rate; Ueda and Takata comments raised the possibility of an outsized September hike (carried from prior run, unchanged).
  - as_of: 2026-09-03/04 (mitrade.com, direct fetch) · status: yen rallied from the 160 area to a one-month high of 155.28 (per mitrade's own figure) before settling near 156.3 in early Sept-4/5 Asia trading; markets pricing "close to an 80% chance of a 25-basis-point hike to 1.25% at the September 17-18 meeting, and those bets have intensified since"; drivers cited: Tokyo August core CPI above consensus at 1.8%, and PM Takaichi's public backing for an early BOJ move (a new named driver not on file from prior runs).
  - as_of: 2026-09-05 (exchangerate-api.com direct fetch) · USD/JPY spot: 156.16
  - as_of: undated, WebSearch snippet (not independently source-dated this run) · a cited Polymarket contract shows 97.5% probability of a BOJ hike at the Sept-18 meeting; a separately cited overnight-index-swap read implies ~96.5bps of cumulative BOJ tightening over the next 12 months with September priced at 84% — these two probability figures (97.5% vs. 84%) differ from each other and from mitrade's ~80%; all three are recorded, not reconciled, since they may reflect different instruments/methodologies (event contract vs. OIS-implied vs. analyst estimate).
next_release: 2026-09-18 (BOJ Monetary Policy Meeting decision)
conflict: hike-probability figures now range 80-97.5% across three differently-sourced reads (mitrade ~80%, OIS-implied 84%, Polymarket 97.5%) — up from the prior run's framing of "leaning toward a quarter-point hike" without a specific probability number; recording the spread rather than picking one. USD/JPY also shows a spread across sources for the same window: prior run's direct exchangerate-api.com read was 156.02 (as_of 2026-09-04); this run's same-endpoint read is 156.16 (as_of 2026-09-05), while mitrade's narrative cites an intraday one-month-high touch of 155.28 on Sept-3 and a "near 156.3" level in early Sept-4/5 Asia hours — all in a tight ~155.3-156.2 band, treated as normal intraday/day-to-day movement, not a source conflict.

### credit-spreads
source:  ICE BofA US High Yield Index Option-Adjusted Spread, FRED series BAMLH0A0HYM2 — fred.stlouisfed.org/graph/fredgraph.csv direct fetch succeeded this run (the exact URL named in the spec), returning the full official daily series with no gaps through the latest available observation.
series:
  - as_of: 2026-08-28 · 260 bps (2.60%)
  - as_of: 2026-08-31 · 263 bps (2.63%)
  - as_of: 2026-09-01 · 265 bps (2.65%)
  - as_of: 2026-09-02 · 266 bps (2.66%)
  - as_of: 2026-09-03 · 265 bps (2.65%)
conflict: none — this run's direct FRED CSV fetch extends the prior run's series by one more day (2026-09-03, 265 bps) with no discontinuity; FRED had not yet posted a 2026-09-04 observation as of this run's fetch (consistent with the series' typical one-business-day reporting lag, and 2026-09-05 being a non-trading Saturday). A WebSearch cross-check independently returned the same 2.65% figure for 2026-09-03, and separately surfaced a third-party aggregator (govspending.org) also showing 2.65% with no date conflict.
