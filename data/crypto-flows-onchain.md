# crypto-flows-onchain readings — run 2026-09-02
fetcher: crypto-flows-onchain

### btc-price
source: CoinDesk (coindesk.com/price/bitcoin), Fortune daily BTC price series, CoinGecko (coingecko.com/en/coins/bitcoin) — cross-checked; direct fetch to coindesk.com/coingecko.com blocked by network egress proxy at run time, so values are as captured via search-indexed snapshots of those sources, not a direct live pull
series:
  - as_of: 2026-09-01 · $77,648.17 (9:43am EDT, CoinDesk); separately CoinGecko showed $77,157.03 (-2.30% 24h) same day
  - as_of: 2026-08-31 · $78,414.14 (8:30am ET, Fortune/CoinDesk-sourced)
  - as_of: 2026-08-30 · ~$78,231.51 (+0.75% 24h)
  - as_of: 2026-08-29 · $77,838 (-3.01% on the day, post-Jackson Hole/Warsh selloff; intraday low near $77,000 per other outlets)
  - as_of: 2026-08-28 · opened $80,261.86 (highest opening since 2026-05-15, 3-month high), intraday high ~$81,455, fell back to close ~$79,560
  - as_of: 2026-08-27 · closed within the $80,000–$82,000 band (4:00pm UTC reference window)
  - as_of: 2026-08-26 · closed near $78,500 (below $79,000)
conflict: no single as_of-2026-09-02 (today's) print located via search as of this run — most recent confirmed reading is 2026-09-01 ($77,648.17 CoinDesk / $77,157.03 CoinGecko, a ~$490 spread between sources same-day); no intraday high/low for 2026-09-02 found — record as not yet available rather than guessed

### spot-etf-flows
source: Farside Investors (farside.co.uk/btc/) figures as reported via search-indexed coverage (direct fetch to farside.co.uk blocked by network egress proxy); TFTC Bitcoin ETF Flow Tracker (tftc.io/bitcoin-etf-flows) for the August daily table
series:
  - as_of: 2026-08-31 (session reported 2026-09-01) · +$216.7M net inflow (IBIT +$205.9M, FBTC +$6.9M, BITB +$4.3M, MSTB/Grayscale BTC-Mini +$3.6M/+$9.4M, HODL -$13.4M) — return to inflows after one prior session of outflows
  - as_of: 2026-08-19 · +$517.2M (largest single session referenced in the August table)
  - as_of: 2026-08-18 · +$189.3M net (FBTC alone supplied $111.9M of a reported $137.3M day elsewhere in coverage — the two figures for this date are not fully reconciled from available sources)
  - as_of: 2026-08-17 · +$297.6M
  - as_of: month-to-date through 2026-08-19 · August 2026 cumulative net inflow ~$1.5B across 13 trading days (9 inflow days vs 4 outflow days)
  - as_of: year-to-date, 2026 · cumulative ~$4.84B net outflows for the year as of the most recent rollup found (54% of 2026 sessions have been net-outflow days; longest outflow streak 2026-05-15 to 2026-06-03, 13 sessions, -$4.37B)
conflict: could not obtain a complete unbroken 10-daily-observation table (2026-08-20 through 2026-08-28, and 2026-09-01 per-fund breakdown for days other than 08-31, are missing from what search surfaced) — direct fetch to farside.co.uk was blocked; recorded only the specific dated data points found rather than filling gaps

### stablecoin-supply
source: DefiLlama Stablecoins dashboard (defillama.com/stablecoins, direct fetch blocked by egress proxy — figures via search-indexed secondary coverage), StableCoin.com and Forbes trackers cross-checked
window: weekly, per fetch spec (8 readings) — only the dated snapshots below were locatable via search; true weekly cadence not confirmed
series:
  - as_of: 2026-09-01 · $289.8B (StableCoin.com, 15:47 UTC) / $290.70B (Forbes, same-day) — the two trackers differ by ~$0.9B
  - as_of: 2026-08-13 · $308.0B (DefiLlama, +14.3% YoY, -4.5% vs May peak)
  - as_of: 2026-07-27 · reported as "shrank for the first time in four years" (Forbes) — no exact figure attached in source
  - as_of: 2026-07-12 · ~$310B (-$10B since the 2026-05-17 peak, incl. -$7.7B in June alone)
  - as_of: 2026-05-17 · $322.4B (all-time peak, DefiLlama)
conflict: on-file note (added 2026-09-01) described the contraction as "~$14.6B from the $322B peak"; current-run figures show a larger contraction — $289.8-290.7B as of 2026-09-01 is ~$32-33B (≈10%) below the $322.4B May peak, roughly double the previously logged decline. The decline has continued/accelerated since the note was written, it is not a same-day discrepancy. Could not source a clean weekly-cadence 8-point series — only the dated snapshots above were found; USDT holds ~63.3% share, USDT+USDC ~88.6% combined (2026-09-01 composition)

### corporate-treasuries
source: bitcointreasuries.net + corporate filings via search-indexed coverage (Yahoo Finance, CryptoBriefing, Barchart); direct fetch to bitcointreasuries.net not attempted (other bitcointreasuries pages returned via search only)
series:
  - as_of: 2026-08-31 (purchase window 2026-08-24 to 2026-08-30) · Strategy (MicroStrategy) purchased 4,603 BTC for $369.7M at avg. price $80,318/BTC — ends a 10-week buying pause (last prior purchase 2026-06-15 to 2026-06-21: 520 BTC for $34.9M). Reported total holdings after purchase: 845,050 BTC. Funded via sale of 4,531,421 Class A shares ($602.8M net proceeds); $151.8M of proceeds used to buy back 1,557,177 STRC preferred shares, $50.7M to STRC dividends, $30M to cash reserves. At BTC ~$78,083, unrealized profit on the position cited as $2.25B (avg. acquisition price $75,412)
  - as_of: 2026 (undated, current status) · Twenty One Capital holds 43,514 BTC — second-largest corporate holder
  - as_of: 2026 (undated, current status) · institutional buying (ETFs + corporate treasuries incl. Strategy) reported running at 2.8x new mining supply in early 2026
conflict: one older-dated search snippet ("microstrategy buys 430 more bitcoins... total holdings top 629k btc") is inconsistent with the 845,050 BTC current figure — that snippet is from an earlier point in 2026 and is stale, not a same-day conflict; not used as the current reading

### sovereign-adoption
source: bitcointreasuries.net/governments pages + coverage (Finance Yahoo, IBTimes, GL Insight, CCN) via search-indexed results
series:
  - as_of: 2026 (current status) · El Salvador holds ~7,663 BTC via its Bitcoin Office, which continues posting daily purchase-themed social posts, but the public sector has not executed a net new BTC purchase since 2025-02 (per the $1.4B IMF program terms); described as "the only country directly buying Bitcoin among 13 BTC-holding nations" in one source, which appears to conflict with the "no purchases since Feb 2025" characterization in another — both traced to search-indexed coverage, not reconciled
  - as_of: 2026 (current status, trailing ~18 months) · Bhutan has sold roughly $1B of its BTC holdings over the past ~18 months (net seller, not buyer, despite still being described elsewhere as the world's 3rd-largest sovereign holder at 12,062 BTC as of 2025-06)
  - as_of: 2025-10 (background, not current-period news) · France lawmakers proposed a national BTC Strategic Reserve bill
checked_absence: no new sovereign accumulation announcement (a state newly adopting or actively buying) found as of 2026-09-02; the two active sovereign programs found (El Salvador, Bhutan) are both currently non-accumulating or net-selling

### mvrv
source: Glassnode MVRV (studio.glassnode.com/charts/market.Mvrv) figures via search-indexed secondary coverage (AhaSignals, CryptoPotato); direct fetch to studio.glassnode.com not attempted (blocked-domain pattern seen elsewhere)
series:
  - as_of: 2026-08-28 · ~1.5 (BTC near $79,000) — "modest by historical standards," has not confirmed a clean accumulation-zone bottom
  - as_of: 2026-08-08 · 1.24 (raw MVRV ratio)
  - as_of: 2026-08-08 · MVRV Z-Score separately reported at 0.42 (a related but distinct metric, noted for context not substitution)

### puell-multiple
source: Glassnode Puell Multiple, via secondary aggregator (MacroMicro, en.macromicro.me/series/8112) — search-indexed, direct fetch not attempted
series:
  - as_of: 2026-08-26 · 0.9451 (miner revenue below its 365-day average)
conflict: fetch spec calls for current + prior; only one dated observation was locatable via search — no prior-period Puell value found as of this run

### exchange-netflows
source: CryptoQuant Exchange Netflow/Reserve charts (cryptoquant.com/asset/btc/chart/exchange-flows) via secondary coverage (Coin-Turk); direct fetch not attempted for cryptoquant.com
series:
  - as_of: 2026-08 (trend through month) · Binance BTC reserves rose to ~687,000 BTC, the highest mark for 2026, having bottomed near 617,000 BTC in late April 2026 before reversing and accelerating higher through August — described as increasing available BTC supply on exchanges, coinciding with price resistance near $80,000
conflict: fetch spec calls for last 7 daily netflow readings (a flow metric); only an exchange-reserve trend (a stock/level metric, not a daily netflow figure) was locatable via search — no daily netflow series found as of this run, recorded the closest available on-chain reading instead of guessing at daily figures

### funding-rates
source: Coinglass aggregated BTC perpetual funding (coinglass.com/FundingRate/BTC); direct fetch blocked by network egress proxy, and no dated September 2026 figure was located via search
series:
  - as_of: 2026-02-28 (background only, not current) · funding rates fell to -6%, a 3-month low at that time — cited only for definitional context, not as a current reading
checked_absence: no current (late-August/September 2026) funding-rate figure located via search or direct fetch as of this run — Coinglass access is blocked at the network level; recording as no current value found rather than substituting the stale February figure

### futures-oi-liquidations
source: Coinglass aggregated OI + liquidations (coinglass.com/currencies/BTC/futures, coinglass.com/liquidations/BTC) via search-indexed coverage; direct fetch blocked by network egress proxy
series:
  - as_of: 2026-08-30 · aggregate BTC futures open interest $54.82B (695,020 BTC) across venues — Binance 142,500 BTC ($11.24B, 20.5% share), CME 116,040 BTC ($9.15B), MEXC $5.01B, Bybit $4.58B, Gate $4.57B, OKX $2.79B, Bitget $2.16B, KuCoin $1.62B
  - as_of: 2026-08-29 · ~$487.68M in liquidations across the crypto market over 24h (97,691 traders affected), long positions >$360M of that total, following the Warsh Jackson Hole speech
  - as_of: 2026-08-25 · BTC open interest (coin terms) at a 5-month low of ~587,600 BTC even as price was still climbing; margin OI at a record low near 52,000 BTC
  - as_of: 2026-09-01/02 · a separate, unattributed-date figure found: OI $47.75B with $46.28M in 24h liquidations, alongside another figure of OI $54.30B — the two OI figures in this snippet are inconsistent with each other and not clearly dated; recorded for completeness but flagged as unreliable
conflict: the 2026-09-01/02 OI figures are internally inconsistent ($47.75B vs $54.30B in the same source snippet) and could not be resolved to a single value — use the dated 2026-08-30 figure ($54.82B) as the more reliable current reading

### options-vol-skew
source: Deribit DVOL + 25-delta skew (insights.deribit.com, studio.glassnode.com/charts/derivatives series) via search-indexed coverage (CoinDesk, TradingView); direct fetch not attempted for deribit.com/glassnode.com
series:
  - as_of: 2026-08-29 (Friday, Jackson Hole/$6.4B options-expiry day) · DVOL surged from ~35% to a peak of ~65% intraday — the sharpest DVOL move since early 2023
  - as_of: 2026-09-01/02 (most recent found) · DVOL "cooled down to 43%" per the same source thread (exact date of this reading not separately confirmed)
  - as_of: 2026-08 (week preceding the above) · during BTC's move from ~$62,000 to ~$80,000, the volatility term structure shifted from backwardation to contango and call-put skew flipped from negative to positive (more call demand than put demand) — described qualitatively, no numeric skew value found
conflict: fetch spec asks for numeric current + prior; only descriptive/relative DVOL levels (35% → 65% → 43%) were locatable, and the skew reading is qualitative only (direction, not a numeric 25-delta value) — recorded as found rather than inventing a number

### fear-greed
source: alternative.me Crypto Fear & Greed Index (alternative.me/crypto/fear-and-greed-index) — direct fetch blocked by network egress proxy; values below via search-indexed secondary trackers (BitDegree, CFGI.io, FearGreedMeter, Milkroad) that cite or mirror alternative.me
series:
  - as_of: 2026-09-01 · 44 ("Fear") — per one search-indexed reading attributed to alternative.me
  - as_of: undated (same source thread) · a separate reading of 62 ("Greed," described as a 16-point jump from a prior 46) was also found, but that snippet's price context (BTC "near $69,803") does not match the ~$77-78K level confirmed for late Aug/Sept 1 2026 — this reading is very likely from a different, earlier date mislabeled in the source and is NOT used as the current value
  - as_of: undated · CFGI.io (a different, non-alternative.me index) separately shows 44 ("Neutral" per its own scale) same period; FearGreedMeter.com (also non-alternative.me) shows 69 ("Greed") — cited only to show cross-tracker spread, not substituted for the alternative.me reading
conflict: direct access to alternative.me was blocked at the network level, so the primary source itself could not be verified directly this run; the 44 ("Fear") reading as of 2026-09-01 is the best-supported figure (consistent with the post-Jackson-Hole selloff context of 2026-08-29 onward), but it is a secondary-source characterization of alternative.me, not a direct pull — flagged per the "verify at primary source" rule since primary access failed
checked_absence: no alternative.me reading specifically for 2026-09-02 located; last confirmed dated reading is 2026-09-01

### technical-trend
source: bitbo.io 50/200-day MA chart (charts.bitbo.io/50-200-day-ma) + CoinDesk golden-cross coverage — direct fetch to bitbo.io blocked by network egress proxy; figures via search-indexed secondary reporting
series:
  - as_of: 2026-08 (most recent found) · 50-day SMA ≈ $65,785–66,000; 200-day SMA ≈ $69,005–69,144 — BTC price (~$77-78K late Aug/early Sept) trades above both averages; 200-day SMA reported rising since 2026-08-28
  - as_of: 2026-08-20 · golden cross not yet confirmed but the 50-day/200-day gap continues to narrow (50-day was rising toward the 200-day from below)
  - as_of: background (2025-10) · BTC had been trading below its 200-day SMA since Oct 2025 (price then ~$110,000), i.e. the "death cross" state this golden-cross setup would reverse
conflict: minor inconsistency in exact SMA levels across sources ($65,785.40/$69,144.45 in one figure vs "$65,000"/"$69,000" rounded in another, and one snippet citing 50-day at "$63,976") — figures cluster tightly enough ($65-66K / $69K) to treat as the same reading from slightly different capture times, not a real conflict

### altcoin-dominance
source: Bitcoin dominance (BTC.D) + Altcoin Season Index (blockchaincenter/CMC-style index), via search-indexed coverage (BeInCrypto, Bitget, Phemex, bitcoinfoundation.org)
series:
  - as_of: 2026-08 (most recent found) · BTC dominance ~60.15-60.66%, having broken out above 60% and ending an eight-month accumulation phase, targeting the 66% cycle high from June 2025; Altcoin Season Index reads ~35 (below the 40-below range cited elsewhere), well under the 75 threshold that defines altseason
  - as_of: earlier August 2026 reading (undated within month) · BTC dominance cited elsewhere as "58%" and "mid-to-high 50s," Altcoin Season Index "below 40" — the dominance figures across sources range 58-60.66%, not fully reconciled to a single day
conflict: multiple BTC-dominance figures (58%, 59.9%, 60.15%, 60.66%, 65%) and Altcoin Season Index figures (35, "below 40") appear across sources without consistent dating — recorded the range rather than picking one number as ground truth; the qualitative read (Bitcoin Season, altseason unlikely before end of 2026) is consistent across all of them

### social-retail-sentiment
source: Santiment (app.santiment.net social-volume/sentiment data) via search-indexed coverage (CoinMarketCap Academy, Bitbo); direct fetch not attempted
series:
  - as_of: 2026-08 (week noted as "This Week in Crypto, W2 Aug '26") · BTC's positive-to-negative social comment ratio stayed below 1.0 every day since a referenced "Cold Card hack," producing the most negative sentiment week since Santiment's social data began
  - as_of: 2026-01 (background, not current) · social sentiment had begun 2026 strong/"very positive" (20% rise in positive mentions since Jan 1), which had preceded a period Santiment flagged as a caution signal for sustained upside
checked_absence: no sentiment reading specifically dated to late Aug/Sept 2026 (post the "most negative week" note) located as of this run

### four-year-cycle-belief
source: analyst/positioning commentary — Benjamin Cowen (CoinMarketCap Academy, BeInCrypto), Jesse Olson chart commentary (Yahoo Finance), Alphractal and CryptoQuant model commentary, via search-indexed coverage
series:
  - as_of: 2026-08 (most recent found) · Benjamin Cowen's base case remains an October 2026 cycle low, consistent with prior midterm-year bottoms (2014, 2018, 2022); he states the 4-year cycle is "not dead," noting BTC topped within roughly a week of the historically expected peak date
  - as_of: 2026-08 · Jesse Olson's cross-cycle chart (scaled to the 2024 halving) places the current cycle at ~day 775 post-halving, with every prior cycle bottoming near day ~900 — implying roughly 125 days (~4 months) until the historical bottom window opens; his chart's projected low band sits in the $40,000s
  - as_of: 2026-08 · Alphractal targets late September/early October 2026 for a bottom; CryptoQuant's models show a high-probability bottom window spanning September-November 2026
  - as_of: 2026-08 · a separate historical-trend citation suggests BTC could fall to a $50,000-$55,000 range before the next major bull leg, per unspecified "historical trends" framing
