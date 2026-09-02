# cross-asset readings — run 2026-09-02
fetcher: cross-asset

### dxy
source:  ICE DXY — primary market-data terminals (Bloomberg .DXY, ICE, CNBC, investing.com, tradingeconomics, statista, yahoo finance) were unreachable via direct fetch this run (network egress proxy blocked all of them, same as prior run); values below are from web-search snapshots citing those same sources' published numbers, not a direct terminal read.
series:
  - as_of: 2026-08-21 · 98.8 (described as a three-month low, per search-snapshot context citing tradingeconomics/investing.com)
  - as_of: 2026-08-27 · 99.05
  - as_of: 2026-08-28 · 99.65 (+0.5% on the day, day of Warsh Jackson Hole remarks)
  - as_of: 2026-08-31 · 99.44 (per prior fetcher run; unresolved vs. an alternate 99.70 figure — see conflict below)
  - as_of: 2026-09-01 · three figures found for the same date: 99.412 (described as "softened 0.29% to 99.412"), 99.416, and 99.6608 (described as "rose ... up 0.23% from the previous session") — could not resolve to one official close
  - as_of: 2026-09-02 · 99.692 (+0.15% in past 24h, per one snapshot) / opening 99.68, intraday range 99.64-99.71 (per a second snapshot) — broadly consistent with each other, inconsistent with the lower 99.412/99.416 figure given for 09-01
conflict: 2026-08-31 close still unresolved (99.44 vs. 99.70, carried over from prior run — primary terminals remain unreachable). New this run: 2026-09-01 also has three disagreeing figures (99.412 / 99.416 / 99.6608, a ~0.25 point spread) across search snapshots citing the same underlying sources (investing.com/tradingeconomics-style aggregators); could not verify the single official close because none of ICE/Bloomberg/investing.com/tradingeconomics/CNBC/statista/yahoo finance were directly reachable this run. Direction (index firming from the Aug-21 98.8 low toward ~99.4-99.7 by Sept 1-2) is consistent across all snapshots even though the exact daily print is not.

### btc-nasdaq-corr
source:  K33 Research, cited via multiple outlets this run — The Block (2026-08-26 article, "Altitude sickness can wait"), and a newer Grayscale research note (Pandl) covered by Yahoo Finance, bloomingbit.io, thecryptobasic.com, hokanews.com, finance.biggo.com, and FXStreet, all dated around 2026-08-27 to 2026-09-01. Direct fetch of theblock.co, finance.yahoo.com, bloomingbit.io, thecryptobasic.com, hokanews.com, and finance.biggo.com was blocked by network egress this run; values taken from web-search snapshots/quotations of these articles.
window:  90-day rolling correlation of daily returns
series:
  - as_of: 2026-08-26 · 0.38 (K33/The Block, described as a one-year low)
  - as_of: 2026-08-27 · "above 60% down to approximately 33%" (Grayscale research note by Pandl, per search snapshot — stated as a range/direction rather than a single print date; described elsewhere as reported "from early September 2026")
  - as_of: 2026-09-01 · 0.33 (33%), reported alongside a 90-day BTC-gold correlation described as "topped 50%" / "all-time high" as of this date, per multiple outlets (bloomingbit.io, thecryptobasic.com, hokanews.com, finance.biggo.com) each citing K33/Grayscale
conflict: three different point-in-time 90-day readings now on file for a short span (0.38 on 08-26, "approx 33%" attributed to an 08-27 Grayscale note, and 0.33 again as-of 09-01) — these may all describe the same ongoing decline reported at different times by different outlets rather than genuinely distinct daily prints; could not access the original K33/Grayscale note directly (theblock.co and all citing outlets were egress-blocked) to confirm exact as-of dates. Recording all three as found rather than collapsing them.

### equity-valuation
source:  Shiller CAPE — primary source multpl.com was unreachable again this run (network egress blocked); secondary aggregators used instead (GuruFocus, thetrading.tools, macroradar.io), each describing itself as tracking multpl.com's series. GuruFocus and macroradar.io pages themselves were also unreachable via direct fetch this run; figures are from search-result snippets of those pages.
series:
  - as_of: 2026-07 (July 2026 print) · 41.37 (per prior run); also described by one search snippet as "crossed above 42 for the first time since July 2000" for the July print — inconsistent with the 41.37 figure
  - as_of: 2026-08 (August 2026 print) · 41.59 (GuruFocus) — also reported as 41.2 (thetrading.tools) and 41.18 (macroradar.io) for the same print
conflict: no new dated print located beyond the August 2026 value already on file from the prior run; primary source (multpl.com) still unreachable, so this reading again rests on secondary aggregators only, which disagree with each other on the exact August 2026 value (range 41.18-41.59) and on whether the July print crossed 42 or was 41.37. Direction (elevated, near dot-com-era highs, ~98.9th percentile since 1881) is consistent across all sources even though the exact value is not.

### gold
source:  spot gold — primary sources (Kitco, World Gold Council, JM Bullion, APMEX) were unreachable via direct fetch this run (network egress blocked); values are web-search snapshots citing Kitco/JM Bullion/TradingEconomics/Yahoo Finance/Fortune. BTC-gold correlation from K33/Grayscale research, cited via the same outlets as btc-nasdaq-corr above.
series:
  - as_of: 2026-08-30 · $4,453.89/oz (per prior run)
  - as_of: 2026-08-31 · three figures for the same date: $4,446.83/oz (2:55pm EDT, one source), $4,425.10/oz (Kitco, 10:11am NY time), $4,450.95/oz (TradingEconomics); additionally, a Yahoo Finance headline for this date reads "Gold sinks following U.S. strikes on Iran," with Dec futures reported opening at $4,483.20/oz, down 1.0% from Friday's close (a futures figure, not spot — flagged, not used as the spot reading)
  - as_of: 2026-09-01 · four figures found for the same date: $4,438.55/oz and $4,456.86/oz (two sources, per prior run), $4,302.95/oz (JM Bullion, "as of 11:41pm EDT"), $4,365.40/oz (Kitco snapshot), and $4,358.74/oz (described as "down 1.86% from the previous day"); accompanying text from one source: "gold fell below $4,450 an ounce on Monday, extending a sharp drop in the previous session as hawkish remarks from Federal Reserve Chair Kevin Warsh revived expectations for an imminent interest rate hike"
  - as_of: 2026-09-02 · $4,374.54/oz, described as down $71.13 (-1.60%) on the day; accompanying text: "physical gold slid to a two-week low as surging Treasury yields and rising bets on a September Federal Reserve rate hike dragged the metal down from last week's three-month high"
  - BTC-gold 90-day correlation, as_of: 2026-08-26 · 0.52 (K33/The Block, described as highest since October 2020)
  - BTC-gold 90-day correlation, as_of: 2026-09-01 · described as "topped 50%" / "all-time high" (K33/Grayscale, per multiple outlets — see btc-nasdaq-corr conflict note); 30-day BTC-gold correlation separately described as reaching 0.8 as of this date
conflict: spot gold readings are badly scattered across sources for both 2026-08-31 (three figures, ~$26 spread, carried over from prior run) and 2026-09-01 (four figures this run, spread of over $150 — $4,302.95 to $4,456.86); direction is consistent (a multi-day decline from a "three-month high" the prior week down to a "two-week low" by 09-02, attributed variously to the Iran strikes (08-31) and to hawkish Fed / rate-hike repricing (09-01, 09-02)), but no single official close could be verified because Kitco/World Gold Council/JM Bullion/APMEX were all unreachable for direct verification this run. The 2026-08-28 $4,656 futures-vs-spot flag from the prior run is dropped as stale (superseded by this run's later, lower prints).

### credit-spreads
source:  ICE BofA US High Yield Index Option-Adjusted Spread, FRED series BAMLH0A0HYM2 — fred.stlouisfed.org was unreachable via direct fetch this run (network egress blocked), as were tradingeconomics.com, macrotrends.net, convextrade.com, ferrantecapitaladvisers.com, ycharts.com, and iga.capital. Values are web-search snapshots from secondary trackers/commentary that cite the same FRED series (Convex, TradingEconomics, and general fixed-income commentary).
series:
  - as_of: 2026-07-27 · 281 bps (2.81%) — described as "priced close to perfection," "richest decile of its history against a long-run median near 450 bps"
  - as_of: 2026-08-20 · 275 bps (2.75%) (per prior run)
  - as_of: 2026-08-24 · 269 bps (2.69%) (per prior run)
  - August 2026 monthly average (as reported by TradingEconomics) · 273 bps (2.73%)
  - as_of: 2026-09-02 (context only, no single dated print) · one search-snapshot claim described the "current reading" as "roughly 295 to 315 bps" (source unclear — a synthesized web-search answer, not a named single source); this conflicts with the 269-281 bps range from the other sources above and could not be verified against any primary source this run
conflict: no daily reading found for 2026-08-25 through 2026-09-01 — same gap flagged in the prior run persists; FRED HY OAS is typically reported with a short publication lag and fred.stlouisfed.org could not be reached directly this run to check for more recent daily prints. Additionally, one search-synthesized figure this run ("roughly 295-315 bps," unattributed to a specific named source) is meaningfully wider than the 269-281 bps range from named sources (Convex/TradingEconomics) covering late July-August; flagging this discrepancy for the Reporter rather than picking one. General fixed-income commentary found this run (Nuveen-style weekly notes, undated more precisely than "early September") describes high yield spreads as having "tightened" recently even as IG spreads separately tightened to 78 bps — directionally at odds with the wider 295-315 bps figure.
