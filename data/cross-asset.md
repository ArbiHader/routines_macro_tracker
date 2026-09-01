# cross-asset readings — run 2026-09-01
fetcher: cross-asset

### dxy
source:  ICE DXY — primary market-data terminals (Bloomberg .DXY, ICE, CNBC, marketwatch, investing.com, tradingeconomics, yahoo finance, macrotrends) were unreachable via direct fetch this run (network egress proxy blocked all of them); values below are from web-search snapshots of those same sources' published numbers, not a direct terminal read.
series:
  - as_of: 2026-08-25 · 98.96
  - as_of: 2026-08-27 · 99.05
  - as_of: 2026-08-28 · 99.65 (+0.5% on the day, day of Warsh Jackson Hole remarks)
  - as_of: 2026-08-31 · 99.44
  - as_of: 2026-09-01 · 99.56 (latest intraday reading found, -0.12% in past 24h; day range 99.47-99.72)
conflict: for 2026-08-31, one source (search snapshot citing Bloomberg .DXY) gave 99.70 instead of 99.44 for the same date — could not resolve which is the official close because fred/bloomberg/investing.com/marketwatch/tradingeconomics/macrotrends/yahoo were all unreachable for direct verification this run. Recorded 99.44 as the more frequently cited figure; flagging both for the Reporter.

### btc-nasdaq-corr
source:  K33 Research, via The Block ("'Altitude sickness can wait': Bitcoin's historic short squeeze...", theblock.co, 2026-08-26) — direct fetch of theblock.co was blocked by network egress; value taken from web-search snapshot/quotation of the article.
window:  90-day rolling correlation of daily returns
series:
  - as_of: 2026-08-26 · 0.38 (described by K33/The Block as a one-year low)
conflict: stream asks for last 4 weekly readings of this 90-day window; only one dated 90-day reading was locatable this run (2026-08-26). A separate K33 reading of 0.43 (2026-07-28) exists but is a 30-day correlation, not the specified 90-day window — not substituted in. No further weekly 90-day prints found as of 2026-09-01; series is incomplete.

### equity-valuation
source:  Shiller CAPE — primary source multpl.com was unreachable (network egress blocked); secondary aggregators used instead (GuruFocus economic indicators page, thetrading.tools), both of which describe themselves as tracking multpl.com's series.
series:
  - as_of: 2026-07 (July 2026 print) · 41.37
  - as_of: 2026-08 (August 2026 print) · 41.59 (GuruFocus) — also reported as 41.2 (thetrading.tools) and 41.18 (a further secondary mention) for the same print
conflict: primary source (multpl.com) unreachable this run, so this reading rests on secondary aggregators only, which disagree with each other on the exact August 2026 value (range 41.18-41.59). Direction (up from July) is consistent across all of them.

### gold
source:  spot gold — primary sources (Kitco, World Gold Council, JM Bullion, APMEX) were unreachable via direct fetch (network egress blocked); values are web-search snapshots citing Kitco/TradingEconomics/Fortune/mygoldcalc. BTC-gold correlation from K33 Research via The Block (same article as btc-nasdaq-corr, 2026-08-26).
series:
  - as_of: 2026-08-27 · $4,589/oz (7:15am ET reading, cited via Fortune)
  - as_of: 2026-08-28 · $4,656 — this figure was described as a December futures opening price, not spot; flagged, not treated as the spot reading for that date (no separate spot figure for 08-28 was found)
  - as_of: 2026-08-30 · $4,453.89/oz
  - as_of: 2026-08-31 · $4,446.83/oz (2:55pm EDT, one source) / $4,425.10/oz (Kitco, 10:11am NY time) / $4,450.95/oz (TradingEconomics) — three figures for the same date, see conflict note
  - as_of: 2026-09-01 · $4,438.55/oz and $4,456.86/oz (two sources); accompanying text: "gold fell below $4,450 an ounce on Monday, extending a sharp drop in the previous session as hawkish remarks from Federal Reserve Chair Kevin Warsh revived expectations for an imminent interest rate hike"
  - BTC-gold 90-day correlation, as_of: 2026-08-26 · 0.52 (K33/The Block, described as highest since October 2020)
conflict: 2026-08-31 spot gold reported at three different values across sources ($4,425.10-$4,450.95, a ~$26 spread) — could not verify the single official close because Kitco/World Gold Council were unreachable this run. The 2026-08-28 $4,656 figure looks like a futures (not spot) quote and is inconsistent with the surrounding spot readings (~$4,450-4,590); flagged rather than used.

### credit-spreads
source:  ICE BofA US High Yield Index Option-Adjusted Spread, FRED series BAMLH0A0HYM2 — fred.stlouisfed.org was unreachable via direct fetch (network egress blocked); values are web-search snapshots from secondary trackers that cite the same FRED series (Convex, DollarLiquidity.com, govspending.org, TradingEconomics).
series:
  - as_of: 2026-08-20 · 275 bps (2.75%)
  - as_of: 2026-08-24 · 269 bps (2.69%)
  - August 2026 monthly average (as reported by TradingEconomics) · 273 bps (2.73%)
conflict: no daily reading found for 2026-08-25 through 2026-09-01 — FRED HY OAS is typically reported with a short publication lag, and the primary source (fred.stlouisfed.org) could not be reached directly this run to check for more recent daily prints. Series depth requested was "last 5 daily"; only two distinct daily points (08-20, 08-24) plus one monthly average were located. Flagging the gap for the Reporter rather than guessing intervening values.
