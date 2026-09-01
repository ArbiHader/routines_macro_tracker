# crypto-flows-onchain readings — run 2026-09-01
fetcher: crypto-flows-onchain

note: Direct WebFetch access to most named primary sources (coinbase.com, coingecko.com,
farside.co.uk, defillama.com, alternative.me, coinglass.com, bitcointreasuries.net,
theblock.co, tradingeconomics.com, finance.yahoo.com, fortune.com, coindesk.com) was
blocked by the network egress proxy this run ("EGRESS_BLOCKED" on every direct fetch
attempt). All readings below were obtained via web search of/about those same primary
sources (search-engine-surfaced snippets naming the primary source and its figure), not
by reading the primary page directly. Flagged per-stream where this materially limited
depth (fewer daily points than the spec's depth calls for).

### btc-price
source:  web-search aggregation of CoinDesk (BTC Price Index), Fortune "Current price of
         Bitcoin" daily series, CoinGecko, CoinMarketCap, Kraken — direct fetch of
         coinbase.com and coingecko.com blocked by egress proxy; CoinDesk (a reputable
         aggregate index) used as the primary reference price
series:
  - as_of: 2026-08-26 · $78,745.95 (Fortune)
  - as_of: 2026-08-27 · $79,707.18 (Fortune, 7:15am ET; +$961.23 vs prior day)
  - as_of: 2026-08-28 · $79,132.61 (Fortune, 6:30am ET); intraday high ~$81,455 reported same day (3-month high)
  - as_of: 2026-08-29 · fell below $78,000 intraday (no single exact print found; described as "sharp reversal" off the ~$81,455 high)
  - as_of: 2026-08-30 · ~$78,231.51 (Fortune, Sunday)
  - as_of: 2026-08-31 · $78,414.14 (Fortune, 8:30am ET)
  - as_of: 2026-09-01 · $78,769.60 (search-aggregated live read); CoinDesk article same day: "steady above $78,000," 24h range ~$77,200–$79,200; other same-day aggregator reads: CoinGecko $78,838.74, CoinMarketCap $78,089.74, Kraken $79,225.00, CoinDesk BPI alt-read $78,173.52
conflict: cross-aggregator spread on 2026-09-01 spans $78,089.74–$79,225.00 (normal exchange/index dispersion, all mutually consistent with "~$78K–79K, steady"). One Binance-labeled search snippet returned $99,887.18, which is inconsistent with every other source and with CoinDesk's own article text ("Bitcoin steady above $78,000") — treated as unreliable/stale search artifact and discarded, not used as the reading.

### spot-etf-flows
source:  web-search aggregation citing Farside Investors / SoSoValue / CoinGlass ETF trackers and news coverage (Cointelegraph, HedgeCo, CryptoTimes, BingX) — direct fetch of farside.co.uk, sosovalue.com, coinglass.com blocked by egress proxy
series:
  - as_of: 2026-08-25 · +$336.07M net inflow (BingX, citing +4,284 BTC); a second source's same-day figure cited elsewhere as part of a "7-day streak" narrative (exact per-source number not independently reconciled)
  - as_of: 2026-08-26 · daily figure not found in available search results
  - as_of: 2026-08-27 · daily figure not found in available search results
  - as_of: 2026-08-28 · −$201.9M net outflow (HedgeCo/CryptoTimes), ending a nine-trading-day inflow streak
  - as_of: week of 2026-08-24–28 · +$924M net inflow for the week (KuCoin, citing SoSoValue); IBIT led with +$938M inflows for the week, total IBIT cumulative net inflows $633.6B; a differently-scoped source put the same week's total at +$853.54M ("strongest weekly inflows since mid-April 2026") — two different weekly totals found, not reconciled
  - as_of: August 2026 (month) · +$3.03B net inflows for the month (Cointelegraph), described as strongest month since October 2025; cuts 2026 YTD net outflows to −$2.26B
  - as_of: 2026-08-31 (cumulative) · total net assets $99.05B; cumulative (since-launch) net inflows $54.36B
checked_absence: no September 2026 daily print found as of this run (US markets were at/near month-end; next trading-day print not yet published)
conflict: depth spec calls for "last 10 daily" — only 2 individual daily prints (8/25, 8/28) were recoverable via search; the remainder of the window is covered only by weekly/monthly rollups, and two different sources give two different totals for the same week (8/24-28: $924M vs $853.54M). Flagged for the Reporter; not resolved to a single number here.

### stablecoin-supply
source:  web-search aggregation citing DefiLlama Stablecoins dashboard — direct fetch of defillama.com blocked by egress proxy
window:  weekly (spec asks for last 8 weekly readings)
series:
  - as_of: 2026-05-17 · $322.4B (all-time peak, per DefiLlama-sourced reporting)
  - as_of: 2026-08-13 · $308.0B (up 14.3% YoY from $269.4B in Aug 2025; 4.5% below the May-2026 peak)
checked_absence: no reading more recent than 2026-08-13, and no intervening weekly prints between 5/17 and 8/13, were found in available search results as of 2026-09-01
conflict: this is only 2 of the requested 8 weekly readings — direct DefiLlama access being blocked prevented pulling the full weekly series; flagged as an incomplete depth for the Reporter.

### corporate-treasuries
source:  web-search aggregation citing bitcointreasuries.net, company SEC filings/press releases, CoinDesk, Yahoo Finance — direct fetch of bitcointreasuries.net blocked by egress proxy
series:
  - as_of: 2026-06-21 · Strategy (MSTR) peak holdings 847,363 BTC
  - as_of: early July 2026 · Strategy sold 3,588 BTC (~$216M raised, to fund dividends on Digital Credit securities) — described as Strategy's largest BTC sale since its 2022 tax-loss transaction
  - as_of: week of 2026-08-03–08-09 · Strategy sold 1,690 BTC for $108.6M aggregate proceeds (avg. sale price $64,262/BTC — this per-BTC figure is inconsistent with the ~$78-79K spot price prevailing that week, source discrepancy not resolved)
  - as_of: week of 2026-08-10–08-16 · Strategy sold 3,458,866 MSTR shares for $333.7M net proceeds (equity raise, not a BTC sale)
  - as_of: 2026-08-10 · H100 Group closed the largest M&A transaction in European public-Bitcoin-equity history, tripling its treasury to 3,506.4 BTC via zero-cash all-share deal
  - as_of: 2026-07-31 · Trump Media & Technology Group (DJT) held ~14,139 BTC (per SEC 10-Q, including pledged coins)
  - as_of: 2026-08-31 · Strategy total holdings 845,050 BTC (one source) / BTC value $66.6B, cost basis $63.73B (another source, same date)
  - as_of: current · Twenty One Capital: 43,514 BTC (2nd-largest corporate holder)
conflict: Strategy's 8/3-8/9 sale price ($64,262/BTC average) is well below the ~$78-79K spot level recorded for BTC that same week in the btc-price series above — flagged, not resolved (could be a reporting/date error in the source, or reflect an average cost basis rather than a sale-week market price).

### sovereign-adoption
source:  web-search aggregation of Bitcoin Policy Institute, Bitget News, Cointelegraph coverage — no single primary registry found reachable directly
series:
  - as_of: current (2026) · 27 countries hold direct/indirect BTC exposure; 13 more pursuing legislative measures (Bitcoin Policy Institute-sourced figure)
  - as_of: current · US: 328,372 BTC (largest sovereign holder, via criminal-asset confiscation) — consistent with the strategic-bitcoin-reserve stream's on-file figure
  - as_of: current · UK: 61,245 BTC
  - as_of: current · UAE: 30,382 BTC (sovereign wealth + mining-linked)
  - as_of: current · El Salvador: 7,514 BTC (only country with BTC as legal tender; government reserves via open-market purchases)
  - as_of: current · Czech National Bank: purchased $1M of BTC + other crypto as part of an experimental portfolio (date of purchase not specified in source)
checked_absence: no new sovereign-adoption announcement found dated within the last ~2 weeks (mid-to-late August 2026) as of this run
conflict: one search result cited "23 governments hold Bitcoin" (Bitget) vs. another citing "27 countries" (Bitcoin Policy Institute) for what reads as the same underlying claim — different counts, not reconciled; flagged for the Reporter.

### mvrv
source:  web-search aggregation citing Glassnode MVRV — direct fetch of studio.glassnode.com blocked by egress proxy
series:
  - as_of: 2026-08-08 · MVRV 1.24 (market value ~24% above realized value); realized price ~$52,330; short-term-holder MVRV 0.96 (below cost basis); long-term-holder MVRV 1.32 (above cost basis)
  - as_of: dated imprecisely, "June 2026" per source (KuCoin) · MVRV ~1.1, described as "nearing past market bottoms"
checked_absence: no MVRV reading dated later than 2026-08-08 found in available search results as of 2026-09-01

### puell-multiple
source:  web-search aggregation citing Glassnode/MacroMicro Puell Multiple — direct fetch blocked by egress proxy
series:
  - as_of: 2026-08-26 · Puell Multiple 0.9451 (BTC price cited alongside as $78,051, consistent with the btc-price series above)
  - as_of: 2026-07-28 · Puell Multiple 0.65
checked_absence: no reading later than 2026-08-26 found as of this run

### exchange-netflows
source:  web-search aggregation citing CryptoQuant exchange-reserve/netflow data — direct fetch of cryptoquant.com blocked by egress proxy
series:
  - as_of: late April 2026 · exchange reserves (aggregate) fell to a 2026 low of ~617,000 BTC
  - as_of: through August 2026 · reserves reversed and rose; Binance reserves specifically rose to ~687,000 BTC, its highest 2026 mark
checked_absence: no day-by-day netflow figures (spec asks for last 7 daily) were recoverable via search; only the reserve-level trend above was found — flagged as an incomplete depth for the Reporter.

### funding-rates
source:  web-search aggregation citing CoinGlass / MacroMicro / CryptoQuant aggregated perp funding — direct fetch of coinglass.com blocked by egress proxy
series:
  - as_of: 3rd week of August 2026 (period description) · funding positive in 88 of the prior 90 eight-hour windows; annualized rate running ~8-15%
  - as_of: 2026-08-20 · that crowded short positioning (note: source text says "short positioning" despite describing positive/long-leaning funding immediately prior — as-stated, not reconciled) unwound in a short squeeze: $1.74B in short liquidations over 24h
  - as_of: 2026-08-28 · funding rate −0.0048% (MacroMicro), i.e. slightly negative
checked_absence: no daily print later than 2026-08-28, and no full 7-day daily series, found as of this run — flagged as incomplete depth for the Reporter.
conflict: the "positive 88/90 windows, 8-15% annualized" read (mid-to-late August) sits awkwardly next to the −0.0048% read dated 2026-08-28 — could reflect the post-squeeze reset on 8/20, not resolved further here.

### futures-oi-liquidations
source:  web-search aggregation citing CoinGlass aggregated OI + liquidations — direct fetch of coinglass.com blocked by egress proxy
series:
  - as_of: mid-August 2026 · a liquidation event: crypto-wide futures OI dropped $3B, triggering $308M in liquidations; BTC futures specifically accounted for ~$24B of total OI at that time
  - as_of: 2026-08-20 · $1.74B in short liquidations over 24h (see funding-rates stream, same event)
  - as_of: 2026-09-01 · total BTC futures open interest $54,823,090,541 (CoinGlass, per search snippet)
checked_absence: no itemized daily OI series (spec: current OI + recent liquidation events, satisfied) beyond the points above
conflict: the mid-August BTC-specific OI figure (~$24B) and the 2026-09-01 BTC OI figure ($54.8B) imply more than a doubling of BTC futures OI in roughly two weeks — plausible given price recovery/relevering but large enough to flag as a discrepancy worth the Reporter's attention rather than face-value trend.

### options-vol-skew
source:  web-search aggregation citing Deribit DVOL + 25-delta skew (via Laevitas/Glassnode/CryptoGamma coverage) — direct fetch of deribit.com/insights and studio.glassnode.com blocked by egress proxy
series:
  - as_of: 2026-07-07 · 25-delta skew: 25Δ put −3.00% vs 25Δ call +3.00% (net skew flagged "Neutral — put skew within normal range")
checked_absence: no DVOL level or skew reading dated in August or September 2026 was found in available search results as of 2026-09-01 — this is a stale (55-day-old) reading; flagged as a real gap, not a current value.

### fear-greed
source:  web-search aggregation citing alternative.me Crypto Fear & Greed Index and several secondary trackers (feargreedmeter.com, CoinMarketCap, Bitget) — direct fetch of alternative.me blocked by egress proxy
series:
  - as_of: 2026-08-31 · 50 (Neutral) — closest dated alternative.me-attributed figure found
  - as_of: dated only "today" in one snippet (ambiguous, possibly 2026-08-31 or 2026-09-01) · 62 (Greed), "down 7 points" (feargreedmeter.com)
  - as_of: undated snippet, same query batch · 51 (Neutral, CoinMarketCap-attributed) and 73 (Greed, unspecified attribution)
checked_absence: no single unambiguous 2026-09-01-dated alternative.me print was recoverable
conflict: four different values (50, 51, 62, 73) surfaced across trackers/snippets for essentially the same date window, spanning Neutral to Greed classifications — this is a materially wide spread for a single index; flagged for the Reporter rather than picked-and-averaged here. The spec's named source (alternative.me) points to 50 (Neutral) as of 2026-08-31 as the best-attributed figure.

### technical-trend
source:  web-search aggregation citing TipRanks technical analysis page (50/200-day SMA) — direct fetch of tipranks.com blocked by egress proxy
series:
  - as_of: current (2026-09, per source) · 50-day SMA $65,785.40; 200-day SMA $69,144.45; spot price cited alongside $78,927.72 (consistent with the btc-price series above); 50-day SMA is below the 200-day SMA (a "death cross" configuration by the standard definition), while spot trades above both; 200-day SMA has been sloping up since 2025-01-30
checked_absence: no prior comparison print (spec: current + prior) was found to state the SMA levels as of a distinctly earlier date

### altcoin-dominance
source:  web-search aggregation citing BeInCrypto (Bitcoin dominance) and an Altcoin Season Index tracker — direct fetch of the underlying dashboards blocked by egress proxy
series:
  - as_of: current (last full week, per source) · BTC dominance closed the week at 60.15-60.66% (two figures cited across sources), described as breaking above 60% after an eight-month accumulation phase, targeting the 66% cycle high from June 2025
  - as_of: current · Altcoin Season Index: 37 (Bitcoin Season territory; altseason threshold is 75)
conflict: BTC dominance cited as both 60.15% and 60.66% for what appears to be the same "last week close" — not reconciled, flagged.

### social-retail-sentiment
source:  web-search aggregation citing LunarCrush — direct fetch of lunarcrush.com blocked by egress proxy
series:
  - as_of: current (trailing 24h, per source) · 159.9M engagements, 106.3K posts, 73% positive social sentiment (LunarCrush)
  - as_of: early 2026 (dated snippet, not September) · top mindshare drivers were Geopolitics (30%, Venezuela-US developments), Michael Saylor/accumulation talk (25%), BTC price outlook (20%) — this breakdown is from an earlier-2026 dated post, not current; included for reference only, not as a current reading
checked_absence: no September-2026-dated qualitative sentiment breakdown found; only the trailing-24h aggregate stat above is current as of this run

### four-year-cycle-belief
source:  web-search aggregation of analyst commentary (Benjamin Cowen/Into the Cryptoverse, CryptoQuant models, Joao Wedson, Peter Brandt coverage via CoinMarketCap, BeInCrypto, Altcoin Buzz, EconoTimes)
series:
  - as_of: current commentary (dated through late Aug 2026) · Benjamin Cowen's base case: cycle low in October 2026, consistent with 2014/2018/2022 midterm-year bottoming pattern; states BTC topped within one week of the historically expected peak
  - as_of: current · Joao Wedson: targets next bottom late September–early October 2026
  - as_of: current · CryptoQuant model: likely bottom window June–December 2026, with September–November flagged as especially probable
  - as_of: current · cycle-length comparison cited: current cycle topped on day 1,162 from prior low, vs. day 1,059 and day 1,168 for the two prior cycles (within historical range)
  - as_of: current · price-target range if the pattern holds: $50,000-55,000 (historical-analogy-based); one outlier scenario (NYDIG) cited $38,000-39,000 by October if the drawdown matches 2014/2018/2022 depth
checked_absence: no dissenting ("cycle is dead"/no-bottom-expected) commentary was surfaced in this run's search results — noted as an absence, not confirmation that no such commentary exists
