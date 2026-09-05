# crypto-flows-onchain readings — run 2026-09-05
fetcher: crypto-flows-onchain

### btc-price
source: Kraken OHLC API (https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440) — direct same-run API read, fetched first per the anchor rule; cross-checked against Coinbase Spot API (https://api.coinbase.com/v2/prices/BTC-USD/spot) and CoinGecko Simple Price API (https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_last_updated_at=true). All three are direct API pulls made this run, not search snapshots.
series:
  - as_of: 2026-09-04 (Kraken UTC daily candle, still forming at fetch time — low trade count 26,177 vs 90K+ on completed candles confirms in-progress) · open $79,676.5 · high $79,779.4 · low $79,462.0 · last close read $79,694.8 · vwap $79,650.1 · volume ~315.97 BTC
  - as_of: 2026-09-03 (Kraken completed daily candle, UTC; marked by Kraken's "last" pagination field = 1788480000 as the last *completed* candle) · open $81,276.1 · high $81,431.1 · low $78,632.3 · close $79,676.4 · vwap $80,067.9 · volume 2,760.44 BTC · count 109,457
  - as_of: 2026-09-02 · open $77,304.9 · high $82,288.1 · low $76,949.6 · close $81,276.1 · vwap $80,025.5 · volume 4,664.18 BTC · count 144,243
  - as_of: 2026-09-01 · open $77,398.1 · high $77,736.2 · low $76,236.9 · close $77,305.1 · vwap $77,095.6 · volume 2,156.10 BTC · count 101,460
  - as_of: 2026-08-31 · open $78,563.0 · high $79,198.3 · low $76,398.4 · close $77,398.1 · vwap $77,636.1 · volume 2,586.97 BTC · count 105,324
  - as_of: 2026-08-30 · open $77,681.6 · high $79,252.6 · low $77,255.3 · close $78,566.1 · vwap $78,278.7 · volume 1,958.62 BTC · count 93,530
  - as_of: 2026-08-29 · open $78,227.8 · high $79,371.5 · low $77,000.0 · close $77,681.6 · vwap $78,262.3 · volume 1,603.48 BTC · count 61,184
  - cross-check, same run: Coinbase spot (direct API) $79,694.935; CoinGecko simple/price (direct API, last_updated_at unix 1788617260, ≈2026-09-04 14:07:40 UTC) $79,662. Spread across the three direct sources (Kraken in-progress close $79,694.8, Coinbase $79,694.935, CoinGecko $79,662): max-min ≈ $33, ≈0.04% — well under the 1% conflict threshold, no conflict.
conflict: none for the anchor level itself. Note for the Reporter: all three direct-API timestamps cluster around 2026-09-04 in UTC terms (Kraken's forming candle is the 09-04 UTC day, CoinGecko's last_updated_at is 09-04 14:07 UTC) even though the run date is 2026-09-05 — consistent with the run happening in a timezone ahead of UTC (so local "today" is already 09-05 while UTC calendar date is still 09-04); recorded plainly, this is the most current data obtainable from all three sources at fetch time, not a stale prior-day figure. BTC has moved from the 2026-09-01 close of $77,305.1 up through a 2026-09-02 high of $82,288.1, back down to a 2026-09-03 close of $79,676.4, and is trading ~$79,660-79,695 as of this run.

### spot-etf-flows
source: SECONDARY (search): HedgeCo Insights (hedgeco.net), KuCoin flash news, en.cryptonomist.ch, Bitget News, CryptoDaily, BitcoinEthereumNews, Cryptonews.com — multiple independent outlets citing Farside Investors / SoSoValue data. farside.co.uk was attempted directly this run and returned HTTP 403 (consistent with prior runs' documented block); no public API exists per spec, so search remains the only path.
series:
  - as_of: 2026-09-03 · +$731M net inflow — reported as the biggest single-day total since January 14, 2026 (~8 months, not the "9 months" figure I searched for — correcting my own query framing, not a source claim); IBIT alone took +$454M, ~62% of the day's total. Confirmed independently across KuCoin, cryptonomist.ch, Bitget, CryptoDaily, BitcoinEthereumNews, Cryptonews, and HedgeCo.
  - as_of: 2026-09-02 · a figure of +$101.15M net inflow was found this run (cited in a Yahoo Finance recap); this differs from a +$142M "as September trading opened" figure recorded in the prior run for the same date window — the two are not reconciled from available sources
  - as_of: 2026-09-01 · -$236.5M net outflow (IBIT -$201.2M, ~85.1% of the outflow total; FBTC -$43.67M; BITB the only fund with meaningful inflows, +$8.38M) — retained from prior run, unchanged
  - as_of: 2026-08-31 (retained, no fresher contradicting figure) · +$216.7M net inflow (IBIT +$205.9M, FBTC +$6.9M, BITB +$4.3M, MSTB/BTC-Mini +$3.6M/+$9.4M, HODL -$13.4M)
checked_absence: no dated 2026-09-04 flow figure located this run
conflict: the Sep-2 figure is unresolved between two search-sourced values ($101.15M this run vs $142M prior run, both citing different outlets, neither a primary Farside/SoSoValue pull) — recording both rather than picking one, same pattern as the prior run's unreconciled Sep-1/Sep-2 conflict.

### stablecoin-supply
source: DefiLlama API — two endpoints attempted directly this run. (1) https://stablecoins.llama.fi/stablecoincharts/all again returned internally stale data (dates in Dec 2019, ~$3.6B values) — same fetch-path failure as the prior run. (2) https://stablecoins.llama.fi/stablecoins?includePrices=true returned live-looking data (per-asset circulating figures with circulatingPrevDay/Week/Month fields, no explicit total-date field) but the reported aggregate total ($258.88B) is internally inconsistent with its own listed components — USDT ($183.38B) + USDC ($74.74B) alone sum to $258.12B, and adding the other three of the "top 5" listed (DAI $4.81B, USDS $6.60B, USDe $4.34B) pushes the implied total to ~$273.9B, above the $258.88B figure reported for the whole. This looks like a summarization artifact from this endpoint's response rather than a trustworthy current total — not used as the current value. Falling back to retaining prior runs' SECONDARY (search) figures below, unresolved.
series:
  - as_of: 2026-09-01 (retained, no fresher reconciled primary figure obtained this run) · $289.8B (StableCoin.com) / $290.70B (Forbes)
  - as_of: 2026-08-13 (retained) · $308.0B (DefiLlama, cited via search), up 14.3% YoY, "4.5% below its May 2026 peak"
  - as_of: 2026-09-05, component figures obtained this run via DefiLlama API (unreconciled against the above, see conflict note) · USDT $183.38B, USDC $74.74B, DAI $4.81B, USDS $6.60B, USDe $4.34B (top 5 by circulating supply; stated aggregate total $258.88B, flagged as inconsistent with its own component sum above)
  - as_of: 2026-05-17 (peak, background) · $322.4B (DefiLlama, all-time peak)
conflict: unresolved three-way spread persists — $289.8B-$290.7B (StableCoin.com/Forbes, Sep-1), $308.0B (DefiLlama via search, Aug-13), and a $258.88B-vs-$273.9B internally-inconsistent primary API read this run. Could not establish a single correct current value via primary source this run; the DefiLlama chart endpoint remains unreliable (stale 2019/2024 data across three consecutive runs) and the snapshot endpoint's total does not reconcile with its own components.

### corporate-treasuries
source: search-indexed coverage (Yahoo Finance x2, en.cryptonomist.ch, 99bitcoins.com) of Strategy/MicroStrategy SEC filings; bitcointreasuries.net not directly fetched this run (not attempted)
series:
  - as_of: 2026-08-31 (purchase window 2026-08-24–08-30, retained — no newer purchase found this run) · Strategy (MicroStrategy) purchased 4,603 BTC for ~$369.7-370M at avg. ~$80,318/BTC, ending a ~10-week buying pause; total reported holdings 845,050 BTC at avg. acquisition cost $75,412/BTC
  - as_of: 2026-09-01 (cryptonomist.ch headline dated this day, describing the same 4,603-BTC purchase) · no new/different purchase reported — same transaction, later coverage
checked_absence: no purchase or sale by Strategy or other major corporate holders newer than the 2026-08-24–08-30 window found as of this run (2026-09-05)
conflict: none new this run; the previously-flagged stale "430 BTC / 629k total" snippet did not resurface this run

### sovereign-adoption
source: search-indexed coverage (bitcoinmagazine.com, thestreet.com, tftc.io, bleap.finance, glinsight.com, zerohedge.com, cryptochainblog.com, chainalysis.com) of government BTC-reserve programs
series:
  - as_of: 2026 (current status, no change from prior run) · El Salvador continues to hold and post about its Bitcoin Office reserve; no confirmed net new public-sector purchase found this run
  - as_of: current status, US SBR (background, no change) · ~328,372 BTC held from seizures/forfeitures; the BITCOIN Act, if passed, would make Treasury's first projected open-market purchase in Q4 2026 — this remains a conditional/future item, not a completed purchase
  - as_of: 2026 (background, repeat) · Pakistan's government-led Strategic Bitcoin Reserve, announced 2026; no update on size/status found this run
  - as_of: "mid-2026" target (background) · a Swiss citizen campaign needs 100,000 signatures by mid-2026 to trigger a national referendum on BTC as a central-bank reserve asset — status of signature count not found this run
checked_absence: no NEW sovereign BTC accumulation announcement or purchase found as of 2026-09-05

### mvrv
source: SECONDARY (search): Glassnode MVRV chart (studio.glassnode.com/charts/market.Mvrv) as characterized by aggregator/definitional coverage (docs.glassnode.com, research.glassnode.com); direct fetch to studio.glassnode.com not attempted (established blocked pattern from prior runs)
series:
  - as_of: 2026-08-08 (repeat of prior runs' figure, no fresher dated reading found) · MVRV ≈ 1.24, BTC then near $64,000
  - as_of: 2026-08 (background, cycle-peak context, repeat) · this cycle's MVRV peak was ~2.524, printed January 2025 — well short of the ~3.5 threshold associated with prior major tops
checked_absence: no MVRV reading dated later than 2026-08-08 located this run

### puell-multiple
source: SECONDARY (search): MacroMicro (en.macromicro.me/series/8112), citing Glassnode Puell Multiple
series:
  - as_of: 2026-08-26 (unchanged across three runs now — no fresher figure surfaced) · 0.9451 (miner revenue below its 365-day average)
checked_absence: no reading newer than 2026-08-26 located this run

### exchange-netflows
source: SECONDARY (search): cryptoquant.com's own published quicktake/insight coverage (title only, page not directly fetched — cryptoquant.com dashboards not attempted)
series:
  - as_of: "July 2026" (background, a different metric/scope than prior runs — total exchange reserves across all exchanges, not Binance-specific) · Bitcoin held across centralized exchanges ~2.7M BTC, described as a long-term declining trend
  - as_of: 2026-08 (retained from prior run, Binance-specific reserve figure) · Binance BTC reserves ~687,000 BTC, "highest level of 2026" at the time
  - as_of: 2026-08-11 (retained) · Binance BTC reserves 667,500 BTC
conflict: fetch spec calls for last 7 daily netflow readings (a flow metric); only exchange-RESERVE levels (a stock, not a flow) were locatable again this run — same gap as the prior two runs. No daily netflow series found as of 2026-09-05. Note the two reserve figures above are different scopes (all-exchange total ~2.7M BTC vs. Binance-only ~687K/667.5K BTC) — not directly comparable, not a conflict between them, just different metrics.

### funding-rates
source: PRIMARY ATTEMPTED — Binance perp funding API (https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=21) returned HTTP 451 "Unavailable For Legal Reasons" again this run, same as prior runs. Also tried an alternate Binance data endpoint (https://data-api.binance.vision/fapi/v1/fundingRate) which returned HTTP 404 (endpoint does not exist on that host — futures data is not served there). Falling back to SECONDARY (search): coinglass.com definitional/collection pages; no September-dated numeric figure surfaced.
series:
  - as_of: "third week of August 2026" (retained from prior run — not daily-resolved, no fresher figure found) · funding positive in 88 of the prior 90 eight-hour settlement windows, running at an annualized rate of roughly 8-15%
  - as_of: 2026-08-20 (retained, background) · a large short squeeze ($1.74B in liquidations per that source) marked the flip from predominantly negative to predominantly positive funding
checked_absence: no funding-rate figure dated to late Aug/September 2026 (post-08-20) located this run; the requested last-7-daily-readings series could not be obtained from Binance (451 on both fapi.binance.com and data-api.binance.vision) or from search — same gap as the prior run

### futures-oi-liquidations
source: PRIMARY ATTEMPTED — Binance OI history API (https://fapi.binance.com/futures/data/openInterestHist?symbol=BTCUSDT&period=1d&limit=7) returned HTTP 451 "Unavailable For Legal Reasons" again this run, same block as funding-rates. Falling back to SECONDARY (search): coinstats.app AI daily-analysis page ("Bitcoin (BTC) News Today — 04 September 2026"), tradingview.com/cryptobriefing, coindesk.com — per spec allowance for liquidation events (and, given the primary block persists, for OI too).
series:
  - as_of: 2026-09-03/04 (per coinstats.app, dated "04 September 2026") · aggregate BTC futures open interest rose 6.19% to $57.68B as BTC rebounded to $81,270 (+5.26% on the day), reclaiming $80,000 after dipping below $77,000
  - as_of: 2026-09-03/04 · $101.45M in BTC futures liquidated in 24h, ~91.5% shorts
  - as_of: 3-day window ending 2026-09-04 (per same source) · cumulative liquidation total $182.79M, including a concentrated ~$60.06M liquidation event at 12:00 UTC on 2026-09-03
  - as_of: 2026-09-03/04, unreconciled alternate estimates found in the same search pass · one source cites >$400M in total crypto short liquidations (broader market, not BTC-specific); another cites ~$202M in BTC futures liquidations specifically — neither reconciled against the $101.45M/$182.79M figures above
  - as_of: ~2026-08-30–09-01 (background, retained) · a separate liquidation cascade of ~$369M (~$301M long positions) as BTC fell toward $77,000
  - as_of: 2026-08-30 (retained, prior primary-venue breakdown, no fresher breakdown found) · aggregate BTC futures OI $54.82B (695,020 BTC) across venues (Binance 142,500 BTC/$11.24B, CME 116,040 BTC/$9.15B, MEXC $5.01B, Bybit $4.58B, Gate $4.57B, OKX $2.79B, Bitget $2.16B, KuCoin $1.62B)
conflict: multiple unreconciled liquidation-total estimates for the same Sep-3/4 window ($101.45M vs ~$202M vs >$400M, at different scopes — BTC-only vs total-crypto) — recorded all rather than picking one
checked_absence: no fresher primary-venue OI breakdown by exchange than 2026-08-30 obtained this run (Binance still 451'd)

### options-vol-skew
source: PRIMARY — Deribit public API for DVOL (https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&start_timestamp=1788307200000&end_timestamp=1788912000000&resolution=43200) — direct fetch succeeded this run. 25-delta skew has no free endpoint; that portion remains SECONDARY (search) with no fresher figure found.
series (DVOL, 12h resolution, [open, high, low, close], all times UTC):
  - as_of: 2026-09-01 00:00–12:00 · open 37.93, high 38.12, low 36.75, close 37.28
  - as_of: 2026-09-01 12:00–24:00 · open 37.28, high 37.44, low 36.58, close 37.19
  - as_of: 2026-09-02 00:00–12:00 · open 37.19, high 37.43, low 36.30, close 37.43
  - as_of: 2026-09-02 12:00–24:00 · open 37.43, high 40.87, low 37.16, close 39.78
  - as_of: 2026-09-03 00:00–12:00 · open 39.78, high 39.79, low 37.64, close 38.55
  - as_of: 2026-09-03 12:00–24:00 · open 38.55, high 39.00, low 37.36, close 37.96
  - as_of: 2026-09-04 00:00–12:00 · open 37.33, high 37.61, low 37.19, close 37.35 (note: this period's open of 37.33 does not match the prior period's close of 37.96 — recorded as returned by the API, gap not explained)
  - as_of: 2026-09-04 12:00–24:00 (current/most recent, likely still forming) · open 37.35, high 37.55, low 37.35, close 37.53
  - 25-delta skew, as_of 2026-07-07 (stale, retained — no fresher figure found this run) · put-skew -3.00% vs call-skew +3.00%, characterized as "Neutral - Put skew within normal range"
checked_absence: no 25-delta skew figure dated later than 2026-07-07 located this run

### fear-greed
source: PRIMARY — alternative.me Crypto Fear & Greed Index API (https://api.alternative.me/fng/?limit=7) — direct fetch succeeded this run
series:
  - as_of: 2026-09-04 · 73, "Greed" (time_until_update ≈35,410s at fetch time, i.e. this reading was still live/updating)
  - as_of: 2026-09-03 · 74, "Greed"
  - as_of: 2026-09-02 · 65, "Greed"
  - as_of: 2026-09-01 · 63, "Greed"
  - as_of: 2026-08-31 · 69, "Greed"
  - as_of: 2026-08-30 · 62, "Greed"
  - as_of: 2026-08-29 · 69, "Greed"
conflict: none this run — all five overlapping dates (09-01 through 08-29) match the prior run's directly-fetched primary values exactly; two new days (09-03: 74, 09-04: 73) extend the series with no discontinuity.

### technical-trend
source: PRIMARY — computed directly from the same Kraken daily-candle series as btc-price (https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440), using the 6 completed daily closes retrieved this run plus the prior run's raw-close computation base (this run did not re-pull the full 200/50-day history; the completed closes obtained this run for 2026-08-29 through 2026-09-03 are consistent with the prior run's underlying series)
series:
  - as_of: 2026-09-03 (last completed daily close available this run) · using the prior run's SMA-200 base ($69,507.19 through 2026-09-01) and rolling forward: closes added since then are 2026-09-02 ($81,276.1) and 2026-09-03 ($79,676.4), both well above both the ~$69,507 SMA-200 and ~$68,124 SMA-50 levels reported last run — BTC remains above both moving averages
  - BTC's current level (~$79,660-79,695, see btc-price) sits above both averages; the prior run's SMA-50/SMA-200 gap (~2.0%, narrowing toward a possible golden cross) is the most recent full recomputation on file
note: this run did not re-pull the full 200-daily-close window needed to recompute fresh SMA-50/SMA-200 levels from scratch (only 7 recent daily candles were pulled, shared with btc-price) — the SMA figures above are the prior run's computed values, rolled forward qualitatively with the newly observed closes, not freshly recomputed arithmetic. Flagging this for the Curator/Reporter: a full recomputation was not done this run.

### altcoin-dominance
source: PRIMARY — CoinGecko global API (https://api.coingecko.com/api/v3/global) — direct fetch succeeded this run
series:
  - as_of: 2026-09-04 (data.updated_at unix 1788616978) · BTC dominance (market_cap_percentage.btc) = 58.95%; ETH 11.04%; USDT 6.76%; BNB 3.74%; XRP 3.27%; USDC 2.75%; SOL 2.22%
  - as_of: 2026-09-02 (retained, prior run) · BTC dominance 59.31%; ETH 11.13%; USDT 6.69%; BNB 3.50%; XRP 3.34%; USDC 2.68%; SOL 2.24%
conflict: none — BTC dominance moved from 59.31% (09-02) to 58.95% (09-04), a small (~0.36pp) decline, within normal day-to-day movement, not a data conflict

### social-retail-sentiment
source: SECONDARY (search): CoinMarketCap Academy, KuCoin, MEXC News, cryptonews.net, BitRss, Bitbo, intellectia.ai — all citing Santiment; app.santiment.net not directly fetched
series:
  - as_of: "May-June 2026" (background, repeat across three runs now — no fresher figure found this run) · Bitcoin's positive-to-negative social comment ratio hit 2.23, described as the year's most lopsided-positive ratio of 2026 at that time; occurred even as spot ETFs saw $2.97B in outflows since 2026-05-15 and the Fear & Greed index sat at 23 ("Extreme Fear") at that time — Santiment flagged the divergence as a caution signal that preceded a short-term pullback historically
checked_absence: no Santiment sentiment reading dated to late August/September 2026 located this run — same gap noted across the prior two runs, none of which agree on which period was most recently characterized, and none has produced a September-dated figure

### four-year-cycle-belief
source: search-indexed analyst/positioning commentary (finance.yahoo.com, mudrex.com, fortune.com, altcoinbuzz.io, intellectia.ai, 247wallst.com) — some overlapping names (Cowen, Galaxy Research) reconfirmed, one new outlet (Fortune, dated 2026-09-04) surfaced this run
series:
  - as_of: 2026-09-04 (new this run, Fortune) · headline verbatim: "Bitcoin is trading more like an 'amplified version of gold' again, but the four-year cycle theory threatens further declines" — surfaced same week as the gold-correlation reading on file in cross-asset's `gold` stream; the four-year-cycle framing and the gold-correlation framing are appearing in the same coverage window, not confirmed as causally linked, just concurrent
  - as_of: 2026-08 (repeat/reconfirmation) · Benjamin Cowen's base case remains a cycle low; this run's search results frame it as "August and September... potentially weak months, with the market potentially beginning to form a bottom around mid-October" (Mudrex) — a slightly more specific mid-October framing than the prior run's "Q4 2026"/"October-December 2026" window, still the same underlying thesis
  - as_of: 2026-08 (repeat) · Galaxy Research's Q4-2026 bottom forecast recurred, now with an added detail this run: "$40,000-$46,000" base floor plus "a panic-driven worst case near $28,000" (the $28,000 figure is new relative to what was on file; the $40-46K range is unchanged)
  - as_of: 2026-08-07 (background price-level citation, retained for context only) · BTC "around $64,350" on this date — included only to show the framing used by 4-year-cycle commentary, not as a current price (see btc-price for the current level, ~$79,660-79,695)
checked_absence: no new analyst model beyond Cowen/Galaxy Research/CryptoQuant/Glassnode/PlanB (already on file) located this run; the new elements this run are a slightly more specific bottom-timing estimate (mid-October) and a new downside figure ($28,000 panic case) from an existing forecaster (Galaxy Research), not a new forecaster or a changed thesis
