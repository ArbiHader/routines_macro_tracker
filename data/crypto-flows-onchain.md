# crypto-flows-onchain readings — run 2026-09-03
fetcher: crypto-flows-onchain

### btc-price
source: Kraken OHLC API (https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440) — direct same-day API read, fetched first per the anchor rule; cross-checked against Coinbase Spot API (https://api.coinbase.com/v2/prices/BTC-USD/spot) and CoinGecko Simple Price API (https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_last_updated_at=true). All three are direct API pulls made this run, not search snapshots.
series:
  - as_of: 2026-09-02 (Kraken UTC daily candle, still forming at fetch time) · open $77,304.9 · high $81,381.4 · low $76,949.6 · last close read $81,006.5–$81,010.2 (value shifted slightly between two consecutive fetches seconds apart, confirming the candle is live/in-progress, not a cached static value) · vwap ~$79,536–79,537 · volume ~3,485–3,487 BTC
  - as_of: 2026-09-01 (Kraken completed daily candle, UTC) · open $77,398.1 · high $77,736.2 · low $76,236.9 · close $77,305.1 · vwap $77,095.6 · volume 2,156.10 BTC
  - as_of: 2026-08-31 · open $78,563.0 · high $79,198.3 · low $76,398.4 · close $77,398.1 · vwap $77,636.1 · volume 2,586.97 BTC
  - as_of: 2026-08-30 · open $77,681.6 · high $79,252.6 · low $77,255.3 · close $78,566.1 · vwap $78,278.7 · volume 1,958.62 BTC
  - as_of: 2026-08-29 · open $78,227.8 · high $79,371.5 · low $77,000.0 · close $77,681.6 · vwap $78,262.3 · volume 1,603.48 BTC
  - as_of: 2026-08-28 · open $77,841.8 · high $78,316.0 · low $77,379.7 · close $78,227.8 · vwap $77,905.4 · volume 761.38 BTC
  - as_of: 2026-08-27 · open $80,265.9 · high $81,461.0 · low $76,853.0 · close $77,841.8 · vwap $78,757.2 · volume 4,692.78 BTC
  - cross-check, same run: Coinbase spot (direct API) $81,035.625; CoinGecko simple/price (direct API, last_updated_at unix 1788461130, ≈2026-09-02 ~18:45 UTC) $80,974–$80,981. Spread across the three direct sources (Kraken in-progress close $81,006.5–81,010.2, Coinbase $81,035.625, CoinGecko ~$80,974–80,981): max-min ≈ $62, ≈0.08% — well under the 1% conflict threshold, no conflict.
conflict: none for the anchor level itself. Note for the Reporter: the prior run's last confirmed close was $77,648 (2026-09-01, per that run's search-sourced reading) / $77,305.1 (this run's primary Kraken read for the same 2026-09-01 candle, a $343 / 0.4% difference between a search-indexed figure and the direct API figure for the same day — direct API is authoritative). Price has since moved from the ~$77,305 Sep-1 close to ~$81,000 in the Sep-2 (in-progress) session, a swing this run surfaced via direct API that the prior run's search-based anchor could not have seen.
note: Kraken's OHLC "last" pagination field returned 1788307200 (2026-09-01 00:00 UTC) even though the array's final entry is timestamped 1788393600 (2026-09-02 00:00 UTC) — standard Kraken behavior where the final array entry is the current/still-forming candle and "last" marks the last *completed* candle. Recorded both.

### spot-etf-flows
source: SECONDARY (search): HedgeCo Insights (hedgeco.net) and Bitget News citing Farside Investors data; CoinDesk live-updates page (coindesk.com/business/2026/09/02/...); newsbtc.com. farside.co.uk itself was not directly fetched this run (not attempted — prior runs confirm it 403s automated fetch).
series:
  - as_of: 2026-09-01 · -$236.5M net outflow (IBIT -$201.2M, ~85.1% of the outflow total; FBTC -$43.67M; BITB the only fund with meaningful inflows, +$8.38M) — reported 2026-09-02, with a caveat that only 3 of 13 eligible funds had reported at tally time, so the figure could still shift
  - as_of: 2026-09-02 ("as September trading opened") · a separate figure of +$142M net inflow was found (newsbtc.com headline) — this conflicts with the -$236.5M figure also dated in the Sep-1/Sep-2 window; the two figures were not reconciled from available sources (possible same-day reporting-cycle mismatch, not confirmed)
  - as_of: 2026-08-31 (session reported 2026-09-01, from prior run, retained for continuity) · +$216.7M net inflow (IBIT +$205.9M, FBTC +$6.9M, BITB +$4.3M, MSTB/BTC-Mini +$3.6M/+$9.4M, HODL -$13.4M)
  - as_of: week of 2026-09-22–09-26 (found via search, out of sequence/future-dated relative to this run — flagged, not used as current) · -$903M net weekly outflow (FBTC -$738M, IBIT +$174M) — this date is after the current run date of 2026-09-03 and should not be treated as a completed reading; included only because it surfaced in search results and its dating is suspect
conflict: the -$236.5M (Sep-1) vs +$142M ("Sep-2 open") figures were not reconciled — recorded both rather than picking one. Separately, a search result appears to reference a week dated 2026-09-22 to 09-26, which is in the future relative to this run's date (2026-09-03) — likely a search-index dating error upstream, flagged rather than used.

### stablecoin-supply
source: DefiLlama API attempted directly twice (https://stablecoins.llama.fi/stablecoincharts/all and with a query-string variant) — BOTH attempts returned internally-inconsistent, clearly stale data (first attempt: dates in Nov 2024 with ~$180B values; second attempt on the same URL pattern: dates in Nov 2019 with ~$2.8B values) that cannot be the current series; the API is not reliably returning current data via this fetch path this run. Falling back to SECONDARY (search): bitcoinfoundation.org, Forbes (via search snippets), and a DefiLlama X/Twitter post (x.com/DefiLlama) surfaced by search.
series:
  - as_of: 2026-09-01 (retained from prior run, no fresher primary figure obtained this run) · $289.8B (StableCoin.com) / $290.70B (Forbes)
  - as_of: 2026-08-13 · $308.0B (DefiLlama, cited via search) — up 14.3% YoY, described in the same search result as "4.5% below its May 2026 peak"
  - as_of: "late August 2026" (undated within month, from a search-model synthesis, not a single dated source) · a separate synthesis put current supply at "approximately $307-310B," explicitly contradicting the $290B figure
  - as_of: 2026-05-17 (peak, background) · $322.4B (DefiLlama, all-time peak)
  - a DefiLlama X post (undated by search; URL gives no date) claims total stablecoin market cap "just added $3.073B in the past week... new all-time high... most significant expansion since October" — cross-checked against other search results citing an ATH of "$321B" (April 2026, "third consecutive end-of-month record") and "$323B" (May 2026): this ATH-tweet almost certainly dates to April/May 2026, NOT the current period — NOT used as a current reading, flagged so it isn't mistaken for a September recovery signal
conflict: primary DefiLlama API access failed twice with implausible stale data (2019 and 2024 dates) rather than a clean error — recorded as a fetch-path failure, not a value to use. Among secondary sources, current-period figures range $289.8B–$310B depending on source/dating (StableCoin.com/Forbes ~$290B as of 2026-09-01 vs. a search-synthesis figure of ~$307-310B for "late August") — a real, unresolved spread of roughly $17-20B (~6%) between sources describing similar dates; could not establish a single correct current value via primary source this run.

### corporate-treasuries
source: search-indexed coverage (Yahoo Finance x2, en.cryptonomist.ch, 99bitcoins.com) of Strategy/MicroStrategy SEC filings; bitcointreasuries.net not directly fetched this run (not attempted)
series:
  - as_of: 2026-08-31 (purchase window 2026-08-24–08-30, retained/confirmed from prior run — no newer purchase found this run) · Strategy (MicroStrategy) purchased 4,603 BTC for ~$369.7-370M at avg. ~$80,318/BTC, ending a ~10-week buying pause; total reported holdings 845,050 BTC at avg. acquisition cost $75,412/BTC
  - as_of: 2026-09-01 (cryptonomist.ch headline dated this day, describing the same 4,603-BTC purchase) · no new/different purchase reported — same transaction, later coverage
checked_absence: no purchase or sale by Strategy or other major corporate holders newer than the 2026-08-24–08-30 window found as of this run (2026-09-03)
conflict: one older search snippet ("microstrategy buys 430 more bitcoins... total holdings top 629k btc") recurred in this run's results — confirmed stale (inconsistent with the 845,050 BTC current figure), not used, consistent with prior run's note

### sovereign-adoption
source: search-indexed coverage (Arab News, Unchained Crypto, DAWN, GL Insight, bleap.finance, chainalysis.com) of government BTC-reserve programs
series:
  - as_of: 2026 (current status, no change from prior run) · El Salvador continues to hold and post about its Bitcoin Office reserve; no confirmed net new public-sector purchase found this run either
  - as_of: 2025-05-28 (background, NOT new) · Pakistan's Strategic Bitcoin Reserve was announced at Bitcoin 2025 (Las Vegas) by Bilal Bin Saqib — this surfaced in this run's search results phrased as if current ("Pakistan announced... in 2026"), but the announcement itself dates to May 2025; Pakistan's parliament separately passed the Virtual Assets Act 2026 (Senate Feb 27, National Assembly Mar 3, 2026) formalizing crypto regulation — also background, not a September event
  - as_of: 2026-02 (background) · Brazil's Congress reintroduced RESBit (proposed national reserve targeting up to 1M BTC over 5 years) — no update on passage status found this run
checked_absence: no NEW sovereign BTC accumulation announcement or purchase (distinct from the above already-known programs) found as of 2026-09-03

### mvrv
source: SECONDARY (search): Glassnode MVRV chart (studio.glassnode.com/charts/market.Mvrv) as characterized by KuCoin/Newhedge/other aggregator coverage; direct fetch to studio.glassnode.com not attempted (established blocked-pattern from prior runs)
series:
  - as_of: 2026-08-08 (repeat of prior run's figure, no fresher dated reading found) · MVRV ≈ 1.24, BTC then near $64,000
  - as_of: 2026-08 (background, cycle-peak context) · this cycle's MVRV peak was ~2.524, printed January 2025 — well short of the ~3.5 threshold associated with prior major tops
checked_absence: no MVRV reading dated later than 2026-08-28 (the prior run's most recent, ~1.5) located this run

### puell-multiple
source: SECONDARY (search): MacroMicro (en.macromicro.me/series/8112), citing Glassnode Puell Multiple
series:
  - as_of: 2026-08-26 (unchanged from prior run — no fresher figure surfaced) · 0.9451 (miner revenue below its 365-day average)
checked_absence: no reading newer than 2026-08-26 or a distinct prior-period comparison value found this run

### exchange-netflows
source: SECONDARY (search): CryptoQuant-derived coverage via en.cryptonomist.ch, cryptobenelux.com, cryptobriefing.com, cryptotimes.io; direct fetch to cryptoquant.com not attempted
series:
  - as_of: 2026-08 ("highest level of 2026," specific day within August not given) · Binance BTC reserves ~687,000 BTC
  - as_of: 2026-08-11 · Binance BTC reserves 667,500 BTC, "a level not seen since February"
  - as_of: 2026-04 (background) · Binance BTC reserves ~616,000 BTC (the April low this year's rise is measured from)
conflict: fetch spec calls for last 7 daily netflow readings (a flow metric); only exchange-RESERVE levels (a stock, not a flow) were locatable again this run — same gap as the prior run. No daily netflow series found as of 2026-09-03.

### funding-rates
source: PRIMARY ATTEMPTED — Binance perp funding API (https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=21) returned HTTP 451 "Unavailable For Legal Reasons" (a geo/legal block at the fetch layer, distinct from a generic timeout) — could not get raw settlement data this run. Falling back to SECONDARY (search): KuCoin/Pluang coverage of a funding-rate flip, and background coverage of the Aug-20 short squeeze.
series:
  - as_of: "third week of August 2026" (not daily-resolved) · funding positive in 88 of the prior 90 eight-hour settlement windows, running at an annualized rate of roughly 8-15%
  - as_of: 2026-08-20 · a large short squeeze ($1.74B in liquidations per this source) marked the flip from predominantly negative to predominantly positive funding
checked_absence: no funding-rate figure specifically dated to late Aug/September 2026 (post-08-20) located this run beyond the qualitative "still running positive, 8-15% annualized" characterization above; the requested last-7-daily-readings series (numeric, per settlement) could not be obtained from Binance (451) or from search

### futures-oi-liquidations
source: PRIMARY ATTEMPTED — Binance OI history API (https://fapi.binance.com/futures/data/openInterestHist?symbol=BTCUSDT&period=1d&limit=7) returned HTTP 451 "Unavailable For Legal Reasons," same as funding-rates — could not get raw OI data this run. Falling back to SECONDARY (search) for both OI and liquidations, per spec allowance for liquidation events.
series:
  - as_of: 2026-08-30 (retained from prior run — no fresher OI figure found this run) · aggregate BTC futures open interest $54.82B (695,020 BTC) across venues (Binance 142,500 BTC/$11.24B 20.5% share, CME 116,040 BTC/$9.15B, MEXC $5.01B, Bybit $4.58B, Gate $4.57B, OKX $2.79B, Bitget $2.16B, KuCoin $1.62B)
  - as_of: 2026-09-02 · BTC down 1.38% on the day after a failed breakout attempt near $80K; long liquidations $41M, ~85% of that day's total liquidations (source: coinstats.app AI daily analysis, cited via search)
  - as_of: 2026-08-21 (background) · another ~$1B of short positions liquidated in 24h as BTC topped $75,000
  - as_of: 2026-06 (background, "2026 low") · total crypto liquidations topped $1B in 24h when BTC fell to a 2026 low of $59,018
checked_absence: no fresher primary-venue OI figure than 2026-08-30 obtained this run (Binance 451'd); the 2026-09-02 liquidation figure ($41M long liquidations) is the most current dated data point found

### options-vol-skew
source: PRIMARY — Deribit public API for DVOL (https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&start_timestamp=1787788800000&end_timestamp=1788393600000&resolution=43200) — direct fetch succeeded this run. 25-delta skew has no free endpoint; that portion is SECONDARY (search): Laevitas/Glassnode/theblock.co pages as characterized by search snippets (pages not directly fetched).
series (DVOL, 12h resolution, [open, high, low, close], all times UTC):
  - as_of: 2026-08-26 00:00–12:00 · open 40.37, high 43.63, low 39.51, close 41.93
  - as_of: 2026-08-26 12:00–24:00 · open 41.93, high 42.12, low 40.76, close 41.52
  - as_of: 2026-08-27 00:00–12:00 · open 41.52, high 41.76, low 39.17, close 39.79
  - as_of: 2026-08-27 12:00–24:00 · open 39.79, high 39.79, low 38.21, close 38.34
  - as_of: 2026-08-28 00:00–12:00 · open 38.34, high 38.44, low 37.21, close 37.36
  - as_of: 2026-08-28 12:00–24:00 · open 37.36, high 37.73, low 37.19, close 37.43
  - as_of: 2026-08-29 00:00–12:00 · open 37.43, high 37.61, low 36.57, close 36.59
  - as_of: 2026-08-29 12:00–24:00 · open 36.59, high 37.21, low 36.59, close 36.99
  - as_of: 2026-08-30 00:00–12:00 · open 36.99, high 37.15, low 36.31, close 36.84
  - as_of: 2026-08-30 12:00–24:00 · open 36.84, high 37.69, low 36.48, close 37.63
  - as_of: 2026-08-31 00:00–12:00 · open 37.63, high 37.73, low 36.93, close 37.70
  - as_of: 2026-08-31 12:00–24:00 · open 37.70, high 38.84, low 37.68, close 37.93
  - as_of: 2026-09-01 00:00–12:00 · open 37.93, high 38.12, low 36.75, close 37.28
  - as_of: 2026-09-01 12:00–24:00 · open 37.28, high 37.44, low 36.58, close 37.19
  - as_of: 2026-09-02 00:00–12:00 (current/most recent) · open 37.19, high 37.43, low 36.30, close 37.43
  - 25-delta skew, as_of 2026-07 (stale, no current figure found) · put-skew -3.00% vs call-skew +3.00%, characterized as "neutral" — this is a July reading, not current
conflict: the prior run recorded (via search) "DVOL surged from ~35% to a peak of ~65% intraday" on 2026-08-29, calling it "the sharpest DVOL move since early 2023." This run's PRIMARY direct pull of the same Deribit DVOL index for 2026-08-29 shows a close range of 36.59-36.99 with an intraday high of only 37.61 — no evidence of any move to 65% on that date in the primary series. Recording this discrepancy for the Reporter: the primary source data obtained this run does not corroborate the prior run's secondary-sourced 65% spike figure for 2026-08-29.

### fear-greed
source: PRIMARY — alternative.me Crypto Fear & Greed Index API (https://api.alternative.me/fng/?limit=7) — direct fetch succeeded this run (blocked in the prior run; working now)
series:
  - as_of: 2026-09-02 · 65, "Greed"
  - as_of: 2026-09-01 · 63, "Greed"
  - as_of: 2026-08-31 · 69, "Greed"
  - as_of: 2026-08-30 · 62, "Greed"
  - as_of: 2026-08-29 · 69, "Greed"
  - as_of: 2026-08-28 · 68, "Greed"
  - as_of: 2026-08-27 · 73, "Greed"
conflict: prior run (via secondary/blocked-primary characterization) recorded 44 ("Fear") as of 2026-09-01. This run's direct primary API pull for the same date (2026-09-01) shows 63 ("Greed") — a substantial discrepancy (44 vs 63, different classification entirely: Fear vs Greed) for the same as_of date. This run's reading is a direct primary-source pull; the prior run's was explicitly flagged as unverified secondary. Recording the primary value (63, Greed) as the corrected current reading per the "verify at primary source" rule, and flagging the conflict for the Reporter rather than silently overwriting.

### technical-trend
source: PRIMARY — computed directly from the same Kraken daily-candle series as btc-price (https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440&since=1770249600), 210 raw daily closes retrieved and summed by the Fetcher (not source-reported SMA figures)
series:
  - as_of: 2026-09-01 (most recent completed daily close used) · SMA-200 = $69,507.19, computed from the 200 daily closes spanning 2026-02-14 through 2026-09-01 (raw closes obtained directly from Kraken, summed in this run)
  - as_of: 2026-09-01 · SMA-50 = $68,124.45, computed from the 50 daily closes spanning 2026-07-14 through 2026-09-01
  - BTC's current level (~$81,000, see btc-price) sits above both averages; SMA-50 remains below SMA-200 by $1,382.74 (≈2.0%) — narrower than the prior run's reported gap (~$3,177 between its cited $65,785-66,000 / $69,005-69,144 range), i.e., the gap continues to narrow toward a possible golden cross, not yet crossed
note: this is the Fetcher's own arithmetic on raw Kraken closes (permitted per the stream's fetch spec — "arithmetic on the raw closes is not interpretation"). Date range stated above so the Reporter/Curator can verify the window. Today's in-progress 2026-09-02 candle was excluded from both averages (only completed daily closes through 2026-09-01 used).

### altcoin-dominance
source: PRIMARY — CoinGecko global API (https://api.coingecko.com/api/v3/global) — direct fetch succeeded this run
series:
  - as_of: 2026-09-02 (data.updated_at unix 1788461367) · BTC dominance (market_cap_percentage.btc) = 59.31%; ETH 11.13%; USDT 6.69%; BNB 3.50%; XRP 3.34%; USDC 2.68%; SOL 2.24%
conflict: prior run's search-sourced figures for BTC dominance ranged 58%-60.66% across sources, not reconciled to a single day. This run's primary API read (59.31%, as of 2026-09-02) falls within that range and is the single most reliable figure obtained across the two runs — recorded as current, no fresh conflict introduced.

### social-retail-sentiment
source: SECONDARY (search): CoinMarketCap Academy, KuCoin, cryptonews.net, MEXC News, Bitbo, BitRss — all citing Santiment; app.santiment.net not directly fetched
series:
  - as_of: "May-June 2026" (background, repeat of what search continues to surface — no fresher figure found this run) · Bitcoin's positive-to-negative social comment ratio hit 2.23, described as the year's most lopsided-positive ratio of 2026 at that time; occurred even as spot ETFs saw $2.97B in outflows since 2026-05-15 and the Fear & Greed index sat at 23 ("Extreme Fear") — Santiment flagged the divergence as a caution signal that preceded a short-term pullback historically
checked_absence: no Santiment sentiment reading dated to late August/September 2026 located this run — same gap noted in the prior run (which cited a different, also-undated "most negative week since Cold Card hack" note); the two runs' search results do not agree on which period was most recently characterized, and neither produced a September-dated figure

### four-year-cycle-belief
source: search-indexed analyst/positioning commentary (mudrex.com, Yahoo Finance/Fidelity, intellectia.ai/Galaxy Digital, tradingview.com) — same category of sourcing as prior run, some overlapping names (Cowen) reconfirmed
series:
  - as_of: 2026-08 (repeat/reconfirmation of prior run) · Benjamin Cowen's base case remains a cycle low, now framed as "Q4 2026" / "October-December 2026" in this run's search results (prior run said specifically "October 2026") — a narrowing-to-widening of the same window depending on source, not a changed thesis
  - as_of: 2026-08-07 (background price-level citation, for context only) · one source states BTC was trading "around $64,350" on this date, down ~50% from the Oct-2025 ATH of $126,000/$126,198 — included only to show the framing used by 4-year-cycle commentary, not as a current price (see btc-price for the current level, ~$81,000)
  - as_of: 2026-08 (repeat) · a $50,000-$55,000 historical-trend-based bottom range and Galaxy Digital's $40,000-$46,000 Q4-2026 bottom forecast both recur in this run's results, unchanged from the prior run
checked_absence: no new analyst model or positioning shift beyond what was already on file located this run — same set of forecasters/figures recurred
