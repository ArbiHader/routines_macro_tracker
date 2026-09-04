# cross-asset readings — run 2026-09-03
fetcher: cross-asset

### dxy
source:  ICE DXY (DX-Y.NYB) — no free unauthenticated endpoint exists, so multiple search-indexed / lightly-rendered pages were used and cross-checked: investing.com historical-data table (direct fetch, gave a dated daily series), tradingeconomics.com/dxy:cur (direct fetch, current level), and finance.yahoo.com/quote/DX-Y.NYB (direct fetch, current level). All three converged for today; labeled secondary per spec since none is the ICE terminal itself.
series:
  - as_of: 2026-08-26 · 99.17 (investing.com historical table)
  - as_of: 2026-08-27 · 99.16 (investing.com historical table)
  - as_of: 2026-08-28 · 99.70 (investing.com historical table)
  - as_of: 2026-08-31 · 99.43 (investing.com historical table)
  - as_of: 2026-09-01 · 99.68 (investing.com historical table)
  - as_of: 2026-09-02 · 99.60 (investing.com historical table)
  - as_of: 2026-09-03 · 98.89 (investing.com, intraday) / 98.92 (Yahoo Finance, 2:37:15pm EDT, -0.68% day) / 98.914 (tradingeconomics.com, -0.68% to -0.71% day) — three sources agree within 0.03 points
conflict: resolved from prior run — the prior run's unresolved 2026-08-31 (99.44 vs 99.70) and 2026-09-01 (99.412/99.416 vs 99.6608) three-way splits are superseded by this run's single self-consistent investing.com daily series (99.43 for 08-31, 99.68 for 09-01), which lines up with the higher of the two prior competing figures in each case. One outlier from an earlier WebSearch snippet this run claimed 99.5093 for 09-03 (a stale-looking figure inconsistent with the three converging direct-fetch reads of ~98.9); discarded in favor of the three-way agreement. Net move this run: DXY fell from ~99.60-99.68 (Sep 1-2) to ~98.9 (Sep 3), a same-day ~0.7% drop.

### btc-nasdaq-corr
source:  K33 Research figures cited via The Block (2026-08-26, "Altitude sickness can wait" — direct URL 404'd this run, figures taken from search-snapshot citations) and Grayscale Research (Michael/Zach Pandl) figures cited via Cointelegraph/X, bloomingbit.io, coinedition.com, Benzinga, cryptobriefing.com (all dated ~2026-09-01/09-02, search-snapshot citations — direct fetch of theblock.co's 2026-09-03 follow-up succeeded but that article did not restate the exact Nasdaq-correlation number). A separate, differently-sourced figure (Bloomberg's Eric Balchunas, not K33/Grayscale) is also on record and flagged as such.
window:  90-day rolling correlation of daily returns
series:
  - as_of: 2026-08-26 · 0.38 (38%), K33/The Block, described as a one-year low
  - as_of: ~2026-09-01/09-02 · fallen "from 60% to 33%" (i.e. ~0.33), Grayscale Research per Cointelegraph and multiple secondary outlets, framed as a continuation of the same August decline reported by K33
  - as_of: 2026-08-26 to 2026-09-03 (period, not a single date) · Bloomberg's Eric Balchunas separately states BTC's correlation "to stocks" has "always been about .40" over the past six months, per The Block's 2026-09-03 article — a different source/methodology than K33/Grayscale's 90-day figure, not swapped in for it
  - as_of: 2026-09-03 · Glassnode (via The Block, direct fetch) states BTC's 30-day correlation with the S&P 500 (not Nasdaq, not 90-day) "fell toward zero during the August rally" — noted as a related but methodologically distinct reading, not used to update the 90-day Nasdaq series above
conflict: none new this run beyond what was already flagged prior — the 0.38 (08-26) and ~0.33 (~09-01/02) readings both describe the same ongoing K33/Grayscale-tracked decline at different report dates, consistent in direction; could not obtain a single dated print for 2026-09-03 itself specifically for the 90-day BTC-Nasdaq figure (only the differently-scoped Balchunas .40 and Glassnode 30-day-SPX-near-zero figures were available for that date).

### equity-valuation
source:  Shiller CAPE, multpl.com (direct fetch succeeded this run — https://www.multpl.com/shiller-pe and https://www.multpl.com/shiller-pe/table/by-month), the primary source named in the spec.
series:
  - as_of: 2026-09-02 (current daily reading, 4:00pm EDT) · 41.93 (+0.19, +0.45% on the day)
  - as_of: 2026-07-01 (July 2026 monthly print) · 40.73
  - as_of: 2026-06-01 (June 2026 monthly print, extra context) · 40.50
conflict: resolved from prior run — multpl.com was unreachable last run, forcing reliance on disagreeing secondary aggregators (41.18-41.59 range for August, plus a conflicting "crossed above 42" claim for July). This run's direct primary-source read gives a clean, single-sourced series: July 2026 = 40.73 (not 41.37 or >42 as previously reported by secondary sources), June 2026 = 40.50, current (Sept 2 daily) = 41.93. Long-term mean 17.40, median 16.11, per the same page.

### gold
source:  spot gold — Kitco (kitco.com/charts/gold, direct fetch succeeded this run, gave a timestamped current reading) plus web-search snapshots citing CNBC/Yahoo Finance/mygoldcalc/USAGOLD for the daily series (primary sources' historical pages were not directly fetchable). BTC-gold correlation from K33/Grayscale research, cited via the same outlets as btc-nasdaq-corr above, plus The Block's 2026-09-03 direct-fetched follow-up (Bitwise-attributed figure, no exact number given).
series:
  - as_of: 2026-08-30 · $4,453.89/oz (mygoldcalc, daily close)
  - as_of: 2026-08-31 · $4,431.10/oz (Bloomberg, "settled 1% lower," attributed to hawkish Warsh remarks + renewed Iran tensions) — also reported as ~$4,446/oz by other outlets for the same date, a ~$15 spread
  - as_of: 2026-09-01 · scattered intraday reads: $4,350.25/oz (CNBC, 9:00am ET), $4,331/oz (9:10am ET, source unclear), $4,374.54/oz (down $71.13/-1.60% on the day, per one snapshot) — roughly $45 spread across same-day reads, no single close resolved
  - as_of: 2026-09-02 · $4,336.30/oz (CNBC, +$7.79/+0.18% on the day)
  - as_of: 2026-09-03 · $4,480.90/oz (Kitco, direct fetch, 2:46pm NY time, +$93.90/+2.14% on the day); a same-day Yahoo Finance headline attributes the rise to "hopes that Iran war reescalation will be short-lived" following a described "very heavy attack" on Iran
  - BTC-gold 90-day correlation, as_of: 2026-08-26 · 0.52 (K33/The Block, described as highest since October 2020)
  - BTC-gold 90-day correlation, as_of: ~2026-09-01/09-02 · ~0.50 ("topped 50%"), described as an all-time high, per Grayscale/K33 via multiple outlets; 30-day BTC-gold correlation separately described as 0.8 as of 2026-09-01, also an all-time high
  - BTC-gold correlation, as_of: 2026-09-03 · The Block (direct fetch) describes it as having reached "its highest level since 2020" / a "nearly six-year high" as of "the end of August," citing Bitwise data — no exact coefficient given, direction consistent with the K33/Grayscale 0.50-0.52 figures above but a separate data provider
conflict: spot gold remains scattered across sources this run, same pattern as prior runs — largest spread is 2026-09-01 (~$45 across three same-day reads: $4,331-$4,374.54) and 2026-08-31 (~$15 spread: $4,431.10-$4,446). The Sep 2 ($4,336.30) to Sep 3 ($4,480.90) jump of ~$144 (+3.3%) is large but directionally corroborated by a same-day news narrative (Iran re-escalation) rather than resting on a single unexplained print. Kitco's Sep-3 reading is a direct, timestamped primary-adjacent fetch (unlike the other dates, which are search-snapshot secondary reads) — treat it as the more reliable point in this series.

### boj-carry-trade
source:  Bank of Japan policy statements (boj.or.jp/en/mopo/mpmdeci — July 31, 2026 statement PDF at boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260731a.pdf, listing confirmed via direct fetch of the BOJ decision-index page) + USD/JPY spot (exchangerate-api.com direct fetch, cross-checked against a search snapshot of Wise's rate-history page) + primary coverage of carry-trade positioning (Bloomberg "Carry Trade Exodus Fuels Yen Surge Ahead of BOJ Rate Decision," 2026-09-04, and Bloomberg "Bank of Japan Holds Interest Rate Steady at 1% as Expected," 2026-07-31, both via search snapshot — bloomberg.com itself returned 403 on direct fetch; also CNBC 2026-07-31 and 2026-09-03 articles, and japantimes.co.jp 2026-08-27, all via search snapshot). Note: this section was gathered by a concurrent same-day pipeline run (the stream was added to the catalog after this file's own Fetcher pass started) and is carried in here verbatim for continuity — not independently re-verified by this run.
series:
  - as_of: 2026-07-31 · status: BOJ held its policy rate steady at 1% (highest level since 1995), an outcome all 52 economists surveyed by Bloomberg had expected. Vote was 8-1; sole dissenter Hajime Takata proposed a hike to 1.25%. BOJ statement flagged core inflation likely to exceed the 2% target "from September" and signaled a possible September hike. The US and Japan reportedly staged a joint intervention to support the yen around this date.
  - as_of: 2026-08-26/27 · status: BOJ Deputy Governor Ryozo Himino said the BOJ "should continue to raise" its policy rate, citing higher crude prices (Middle East conflict), rising semiconductor prices (AI demand), and yen weakness as upside inflation risks; he stopped short of committing to September timing. Separately, Governor Ueda and board member Takata made hawkish comments this week "raising the possibility of an outsized rate increase" at the Sept-18 meeting.
  - as_of: 2026-09-02 · status: Himino said the BOJ "will watch the certainty of the outlook and risks" for a rate hike; a separate headline "Japanese yen slides after hawkish BOJ comments" for the same date.
  - as_of: 2026-09-04 · status: yen strengthened sharply to a one-month high vs. the dollar, up more than 1% at one point touching 156.15/USD — its strongest level since Aug 3, shortly after the Jul-31 US-Japan joint intervention. USD/JPY spot as read directly: 156.02.
next_release: 2026-09-18 (BOJ Monetary Policy Meeting decision)

### credit-spreads
source:  ICE BofA US High Yield Index Option-Adjusted Spread, FRED series BAMLH0A0HYM2 — fred.stlouisfed.org/graph/fredgraph.csv direct fetch succeeded this run (the exact URL named in the spec), returning the full official daily series with no gaps.
series:
  - as_of: 2026-08-27 · 263 bps (2.63%)
  - as_of: 2026-08-28 · 260 bps (2.60%)
  - as_of: 2026-08-31 · 263 bps (2.63%)
  - as_of: 2026-09-01 · 265 bps (2.65%)
  - as_of: 2026-09-02 · 266 bps (2.66%)
  - (additional context, same fetch) as_of: 2026-08-20 · 275 bps; 2026-08-21 · 270 bps; 2026-08-24 · 269 bps; 2026-08-25 · 270 bps; 2026-08-26 · 267 bps
conflict: resolved from prior run — the prior run's data gap (2026-08-25 through 2026-09-01 unreported) and the unattributed "roughly 295-315 bps" search-synthesized outlier are both superseded by this run's direct FRED CSV fetch, which returned a complete, gap-free official series through 2026-09-02 with no value above 275 bps in the whole window. The 295-315 bps figure from last run is now clearly wrong / not from this series and should be dropped.
