# cross-asset readings — run 2026-09-04
fetcher: cross-asset

### dxy
source:  ICE DXY (DX-Y.NYB) — direct fetch succeeded this run (unlike the prior two runs) against tradingeconomics.com/dxy:cur and investing.com/indices/usdollar-historical-data; cross-checked against web-search snapshots (vantagemarkets.com) for the same dates. investing.com's historical-data table (fetched directly) is used as the primary daily-close series below; tradingeconomics gives a live intraday level, not a daily close.
series:
  - as_of: 2026-08-31 · 99.43 (investing.com daily close)
  - as_of: 2026-09-01 · 99.68 (investing.com daily close)
  - as_of: 2026-09-02 · 99.60 (investing.com daily close)
  - as_of: 2026-09-03 · 98.91 (investing.com daily close)
  - as_of: 2026-09-04 · 98.99 (investing.com daily close, latest in the table) / 99.02-99.03 (tradingeconomics.com, live intraday read, "Dollar Index traded at 99.013 this Friday September 4th, increasing 0.028 or 0.03 percent since the previous trading session") — the two sources are within ~0.03-0.04 points of each other, not a meaningful conflict
conflict: this run's investing.com-direct series (99.43 → 99.68 → 99.60 → 98.91 → 98.99) is close to but not identical to the prior run's search-snapshot series for the overlapping dates (99.44 vs 99.43 on 08-31; three disputed 09-01 figures of 99.412/99.416/99.6608 vs this run's clean 99.68; 99.692 vs this run's 99.60 on 09-02) — direction is the same (a rise from the Aug-21 98.8 low into the 99.4-99.7 range through Sept 1-2) and this run's figures come from a single directly-fetched table rather than scattered search snapshots, so treat this run's series as the more reliable one, but note the drop back to ~98.9-99.0 by Sept 3-4 is new information not in the prior run.

### btc-nasdaq-corr
source:  K33 Research, cited via The Block (2026-08-26 article, "Altitude sickness can wait") and a Grayscale Research note (Pandl) covered independently by Cointelegraph (X/Twitter post), bloomingbit.io, Benzinga, and cryptobriefing.com. Direct fetch of theblock.co and the citing outlets was not attempted this run (prior runs found them egress-blocked); values below are search-snapshot quotations of these sources, consistent with the prior run.
window:  90-day rolling correlation of daily returns
series:
  - as_of: 2026-08-26 · 0.38 (38%), K33/The Block, described as a one-year low
  - as_of: ~2026-08-27 to 2026-09-01 (exact as_of date not resolved across outlets) · 0.33 (33%), Grayscale Research (Pandl) via Cointelegraph/bloomingbit.io/Benzinga/cryptobriefing.com, stated as "fallen from 60% to 33%"
conflict: same unresolved as_of-date ambiguity carried over from the prior run — multiple outlets report the same ~0.33 Grayscale figure but attach it to different dates (08-27 vs 09-01); the original Grayscale note itself was not directly reachable this run to pin down the exact date. No new reading beyond what was on file from the prior run was found.

### equity-valuation
source:  Shiller CAPE — direct fetch of multpl.com succeeded this run (unlike the prior run, where multpl.com was unreachable): https://www.multpl.com/shiller-pe (current) and https://www.multpl.com/shiller-pe/table/by-month (monthly table).
series:
  - as_of: 2026-06-01 (June 2026 monthly print) · 40.50
  - as_of: 2026-07-01 (July 2026 monthly print) · 40.73
  - as_of: 2026-09-03 (current/live reading, not yet a closed monthly print) · 42.38 (+0.45, +1.07% on the day per the site's current-value module)
conflict: the by-month table returned by this run's fetch jumps directly from Jul 1, 2026 (40.73) to Sep 3, 2026 (42.38) with no August 2026 monthly print shown — this is inconsistent with the prior run's on-file August 2026 value of 41.59 (GuruFocus) / 41.2 (thetrading.tools) / 41.18 (macroradar.io); it's unclear whether multpl's table skips a month, the August print has not yet been finalized/posted, or the August value is present elsewhere in the table that this fetch did not surface. Also, this run's July value (40.73, from multpl.com directly) differs from the prior run's on-file July value of 41.37 — multpl.com direct is the primary source per the fetch spec, so this run's 40.73 should be treated as the more authoritative July figure, superseding the prior 41.37/"crossed above 42" snippets. Flagging both discrepancies rather than silently overwriting.

### gold
source:  spot gold — Kitco (kitco.com/charts/gold) direct fetch succeeded this run for the current level (unlike the prior run, where all primary gold sources were unreachable). Daily series for Sept 1-3 taken from web-search snapshots citing Yahoo Finance, Forbes Advisor, and TradingEconomics (direct fetch of those pages not attempted this run); BTC-gold correlation from the same K33/Grayscale research cited in btc-nasdaq-corr above.
series:
  - as_of: 2026-09-01 · $4,432.20/oz (7:56am ET, Yahoo Finance) — described alongside Dec futures opening $4,498.70/oz (+0.4% from Monday's close, a futures figure, not spot)
  - as_of: 2026-09-02 · $4,336.30/oz, +$7.79 (+0.18%) on the day (described as "steadied near a four-week low, clawing back part of Tuesday's steep loss")
  - as_of: 2026-09-03 · $4,427.99/oz (TradingEconomics, +0.92% from previous day) / $4,432.10/oz at 1:56pm NY time, +$45.10 (+1.03%) (Kitco, per search snapshot) — broadly consistent with each other
  - as_of: 2026-09-04 · $4,467.40/oz (Kitco, direct fetch, 3:10pm NY time), -$4.80 (-0.11%) on the day
  - BTC-gold 90-day correlation, as_of: 2026-08-26 · 0.52 (K33/The Block, described as highest since October 2020)
  - BTC-gold 90-day correlation, as_of: ~2026-09-01 (same date ambiguity as btc-nasdaq-corr) · "climbed above 50%" (Grayscale/Cointelegraph); 30-day BTC-gold correlation separately described as reaching 0.8 as of 2026-09-01, described as an all-time high
conflict: the 2026-09-02 figure ($4,336.30, described as a "four-week low") sits noticeably below both the 09-01 ($4,432.20) and 09-03 ($4,427.99/$4,432.10) figures on either side of it — a ~$90-100 single-day round trip down and back up. This is a materially different shape than the prior run's flagged scatter (which had same-day multi-source disagreement); here the disagreement is across consecutive days from different named outlets, and could not be cross-verified against a single continuous source this run. Also carrying forward: the prior run's unresolved 08-31 three-way spread ($4,425-4,451) was not re-checked this run. Direction into Sept 4 (a recovery back to ~$4,430-4,467) is the new information this run.

### boj-carry-trade
source:  Bank of Japan policy statements (boj.or.jp/en/mopo/mpmdeci — July 31, 2026 statement PDF at boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260731a.pdf, listing confirmed via direct fetch of the BOJ decision-index page) + USD/JPY spot (exchangerate-api.com direct fetch, cross-checked against a search snapshot of Wise's rate-history page) + primary coverage of carry-trade positioning (Bloomberg "Carry Trade Exodus Fuels Yen Surge Ahead of BOJ Rate Decision," 2026-09-04, and Bloomberg "Bank of Japan Holds Interest Rate Steady at 1% as Expected," 2026-07-31, both via search snapshot — bloomberg.com itself returned 403 on direct fetch; also CNBC 2026-07-31 and 2026-09-03 articles, and japantimes.co.jp 2026-08-27, all via search snapshot). BOJ decision-index page itself does not state vote composition or rate levels in plain text (PDF content not parsed) — vote/rate details below are from the Bloomberg/CNBC search snapshots, not a direct read of the BOJ PDF.
series:
  - as_of: 2026-07-31 · status: BOJ held its policy rate steady at 1% (highest level since 1995), an outcome all 52 economists surveyed by Bloomberg had expected. Vote was 8-1; sole dissenter Hajime Takata proposed a hike to 1.25%. BOJ statement flagged core inflation likely to exceed the 2% target "from September" and signaled a possible September hike. The US and Japan reportedly staged a joint intervention to support the yen around this date (per the 2026-09-04 Bloomberg piece, which references "shortly after the U.S. and Japan staged a joint intervention... on July 31").
  - as_of: 2026-08-26/27 · status: BOJ Deputy Governor Ryozo Himino said the BOJ "should continue to raise" its policy rate, citing higher crude prices (Middle East conflict), rising semiconductor prices (AI demand), and yen weakness as upside inflation risks; he stopped short of committing to September timing, saying only that "in-depth deliberations" happen at each meeting. Separately, Governor Ueda and board member Takata made hawkish comments this week "raising the possibility of an outsized rate increase" at the Sept-18 meeting (per the 2026-09-04 Bloomberg piece).
  - as_of: 2026-09-02 · status: Himino said (per FXStreet headline) the BOJ "will watch the certainty of the outlook and risks" for a rate hike; a separate FXStreet piece headlined "Japanese yen slides after hawkish BOJ comments" for the same date.
  - as_of: 2026-09-04 · status: yen strengthened sharply (described as "Thursday" in the source, i.e. 2026-09-03) to a one-month high vs. the dollar, up more than 1% at one point touching 156.15/USD — its strongest level since Aug 3, shortly after the Jul-31 US-Japan joint intervention. USD/JPY spot as read directly (exchangerate-api.com, dated 2026-09-04): 156.02. A search snapshot of Wise's rate-history page separately described 155.8150 as "the lowest" USD/JPY rate during the recent period (unclear exact as_of date). Next BOJ policy decision: 2026-09-18 (confirmed independently across the Bloomberg, CNBC, and Vantage Markets sources above).
next_release: 2026-09-18 (BOJ Monetary Policy Meeting decision)
conflict: one web-search snippet (from an unrelated/stale-looking query result) described the BOJ as having "raised its benchmark rate by 25bps to 0.75%, the highest in three decades" — this directly contradicts the well-corroborated 1%/8-1-hold-on-July-31 figure from Bloomberg, CNBC, Focus Economics, and the BOJ's own PDF filename/index listing, and looks like a stale or mismatched search result (possibly referencing an earlier hike cycle). Discarded in favor of the corroborated 1% figure; flagging in case the Reporter sees the same conflicting snippet elsewhere. Also note: this stream's `impact` field in streams.md is "BTC price (fast path)" but the standard status-type/event-resolution stream naming pattern in this file uses `series` with a status per as_of, matching other status-type streams below (kept for consistency with the fetch spec's "current status + change log").

### credit-spreads
source:  ICE BofA US High Yield Index Option-Adjusted Spread, FRED series BAMLH0A0HYM2 — https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=2026-08-21 — direct fetch succeeded this run (unlike the prior two runs, where fred.stlouisfed.org was unreachable). Clean, single-source daily series, no cross-source conflict this run.
series:
  - as_of: 2026-08-21 · 270 bps (2.70%)
  - as_of: 2026-08-24 · 269 bps (2.69%)
  - as_of: 2026-08-25 · 270 bps (2.70%)
  - as_of: 2026-08-26 · 267 bps (2.67%)
  - as_of: 2026-08-27 · 263 bps (2.63%)
  - as_of: 2026-08-28 · 260 bps (2.60%)
  - as_of: 2026-08-31 · 263 bps (2.63%)
  - as_of: 2026-09-01 · 265 bps (2.65%)
  - as_of: 2026-09-02 · 266 bps (2.66%)
conflict: this run's directly-fetched FRED series resolves the prior run's gap (no reading had been found for 08-25 through 09-01) and directly contradicts the prior run's unverified "roughly 295-315 bps" search-synthesized figure — that figure appears to have been wrong or was describing a different series; this run's FRED-direct 260-270 bps range is the authoritative figure and should supersede it. No reading beyond 2026-09-02 was available in the CSV as of this fetch (FRED's typical one-to-two-day publication lag).
