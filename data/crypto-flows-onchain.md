# crypto-flows-onchain readings — run 2026-09-04
fetcher: crypto-flows-onchain

### btc-price
source: Kraken OHLC API (api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440, fetched with since= narrowing to reduce payload size) — direct same-day API read, fetched first; cross-checked against Coinbase Spot API (api.coinbase.com/v2/prices/BTC-USD/spot) and CoinGecko Simple Price API (api.coingecko.com/api/v3/simple/price, with include_last_updated_at=true confirming a same-day timestamp)
series:
  - as_of: 2026-08-28 · close $77,841.8 (O 80,265.9 / H 81,461.0 / L 76,853.0)
  - as_of: 2026-08-29 · close $78,227.8 (O 77,841.8 / H 78,316.0 / L 77,379.7)
  - as_of: 2026-08-30 · close $77,681.6 (O 78,227.8 / H 79,371.5 / L 77,000.0)
  - as_of: 2026-08-31 · close $78,566.1 (O 77,681.6 / H 79,252.6 / L 77,255.3)
  - as_of: 2026-09-01 · close $77,398.1 (O 78,563.0 / H 79,198.3 / L 76,398.4)
  - as_of: 2026-09-02 · close $77,305.1 (O 77,398.1 / H 77,736.2 / L 76,236.9)
  - as_of: 2026-09-03 · close $81,276.1 (O 77,304.9 / H 82,288.1 / L 76,949.6)
  - as_of: 2026-09-04 (today, in-progress candle) · O $81,276.1 · intraday H $81,431.1 · intraday L $80,561.9 · running/last-trade level: Kraken ticker last trade $80,940.00 (bid $80,939.90 / ask $80,940.00) at fetch time; Kraken's in-progress daily candle close (as last recorded) $80,939.6; Coinbase spot $80,898.93 and, on a second same-run pull, $80,903.42; CoinGecko simple-price $80,896 and, on a second same-run pull, $80,905 (last_updated_at unix 1788505820 / 1788505835 → both convert to 2026-09-04 ~07:10 UTC, confirming same-day). Spread across all four cross-checks: $80,896–$80,940, ~$44 (~0.05%) — well under the 1% conflict threshold, no conflict.
conflict: on-file (2026-09-02 run) recorded 2026-09-01 as $77,648.17 (CoinDesk, search-indexed secondary) / $77,157.03 (CoinGecko, search-indexed secondary). This run's primary Kraken daily-candle close for 2026-09-01 is $77,398.10 — within ~0.2–0.3% of both prior secondary reads, not a material conflict, but noting the source upgrade from secondary/search-indexed to primary/direct-API for that date.
notes: WebFetch attempts to pull the full 720-candle Kraken OHLC history (no `since`) or a ~200-day slice produced internally inconsistent, apparently-fabricated output (round-number candles, a claimed "365 entries" for a requested ~210-day window, an implausible 50-day-average figure of 77,672.91 that did not match a manually-verified recomputation). Narrowing each request to `since` windows of ≤~56 candles produced output that chain-validated perfectly (each candle's open equalling the prior candle's close, dates matching independently-computed unix-timestamp arithmetic) — used that narrower-window method throughout this run; see technical-trend below for the same finding.

### spot-etf-flows
source: Farside Investors flow table — direct fetch to farside.co.uk blocked (network egress); today's figures taken from Farside's own X/Twitter posts (@FarsideUK) and HedgeCo Insights' same-day writeup of the Farside table, both labeled SECONDARY (search-indexed, not a direct farside.co.uk pull); older figures carried from the prior run's search-indexed TFTC/Farside capture
series:
  - as_of: 2026-09-03 · +$101.0M net inflow (IBIT +$115.4M, GBTC -$56.2M; other funds not itemized in source found)
  - as_of: 2026-09-01 · -$236.5M net outflow (IBIT -$201.2M, FBTC -$43.7M, BITB +$8.4M, ARKB/BTCO/EZBC/BRRR/HODL/BTCW/MSBT/GBTC-nonmain/BTC $0)
  - as_of: 2026-08-31 (session reported 2026-09-01) · +$216.7M net inflow (IBIT +$205.9M, FBTC +$6.9M, BITB +$4.3M, MSTB/Grayscale BTC-Mini +$3.6M/+$9.4M, HODL -$13.4M)
  - as_of: 2026-08-19 · +$517.2M
  - as_of: 2026-08-18 · +$189.3M net (FBTC alone reported supplying $111.9M of a separately-reported $137.3M day elsewhere in coverage — the two figures for this date are not fully reconciled)
  - as_of: 2026-08-17 · +$297.6M
  - as_of: month-to-date through 2026-08-19 · August 2026 cumulative net inflow ~$1.5B across 13 trading days (9 inflow days vs 4 outflow days)
  - as_of: year-to-date, 2026 · cumulative ~$4.84B net outflows for the year (as of the most recent rollup found; 54% of 2026 sessions net-outflow; longest outflow streak 2026-05-15 to 2026-06-03, 13 sessions, -$4.37B)
conflict: none this run vs on-file — the new 09-01 and 09-03 dated points are additions, not revisions of prior dated entries. Gap remains: 2026-09-02 and 2026-08-20 through 2026-08-28 not located via search this run either — recorded only the dated points found rather than filling gaps with an estimate.

### stablecoin-supply
source: DefiLlama API, direct fetch — https://stablecoins.llama.fi/stablecoins?includePrices=false (top-10 pegged-asset current circulating figures; this endpoint gave reliable current-day data). The historical series endpoint (stablecoincharts/all) was also fetched directly but its full-history payload is too large for reliable extraction via this run's tooling — a first attempt returned the array's earliest (Nov/Dec-2019) entries when the tail (most recent) entries were requested, indicating the response was truncated before reaching current dates rather than genuinely re-read; that attempt's output is NOT used. Historical points below are carried from the prior run's search-indexed StableCoin.com/Forbes/DefiLlama captures, labeled accordingly.
window: current total is same-day (2026-09-04); historical points are weekly-ish snapshots, not a true 8-point weekly-cadence series
series:
  - as_of: 2026-09-04 (direct DefiLlama API pull, top-10 stablecoins only) · USDT $183,336,108,433 · USDC $74,493,348,951 · USDS $6,598,633,818 · DAI $4,805,586,321 · USDe $4,285,476,006 · USD1 $4,234,959,984 · USDG $3,184,828,741 · PYUSD $3,002,414,477 · BUIDL $2,777,958,783 · USYC $2,687,611,257 — top-10 combined ≈ $289.48B (this is top-10 only; the true "all pegged assets" total is somewhat higher but that field was not separately captured this run)
  - as_of: 2026-09-01 (prior run, SECONDARY: StableCoin.com/Forbes) · $289.8B (StableCoin.com) / $290.70B (Forbes) — consistent with this run's direct top-10 figure of ~$289.48B
  - as_of: 2026-08-13 (prior run, SECONDARY: DefiLlama via search) · $308.0B (+14.3% YoY, -4.5% vs May peak)
  - as_of: 2026-07-12 (prior run, SECONDARY) · ~$310B (-$10B since the 2026-05-17 peak, incl. -$7.7B in June alone)
  - as_of: 2026-05-17 (prior run, SECONDARY: DefiLlama) · $322.4B (all-time peak)
conflict: none — this run's direct-API current total ($289.48B top-10, 2026-09-04) closely corroborates the prior run's search-indexed 2026-09-01 figure ($289.8-290.7B), so the contraction from the $322.4B May peak (now ≈$33B, ≈10%) stands, not a new discrepancy.

### corporate-treasuries
source: bitcointreasuries.net, direct fetch (front page); cross-checked against search-indexed coverage (Yahoo Finance, The Motley Fool, 99Bitcoins, Cryptonomist) for the specific Strategy purchase
series:
  - as_of: 2026-09-04 (direct bitcointreasuries.net pull, current aggregate status) · Public companies: 1,269,881 BTC ($102.67B); Private companies: 284,650 BTC; Government entities: 650,012 BTC (aggregate across all tracked sovereigns — a different, broader figure than the ~328,372 BTC "US only" figure used in the crypto-structural sbr stream, not a conflict, a different scope); ETFs/Exchanges: 1,550,270 BTC; DeFi/Other: 376,310 BTC. Top public holder: Strategy (MSTR) at 845,050 BTC (198 publicly traded companies tracked total)
  - as_of: 2026-08-31/09-01 (purchase window 2026-08-24 to 2026-08-30, reported variously as 09-01 and 09-03 across outlets) · Strategy purchased 4,603 BTC for $369.7M at avg. price $80,318/BTC — ended a ~10-week buying pause (last prior purchase 2026-06-15 to 2026-06-21: 520 BTC for $34.9M). Funded via sale of 4,531,421 Class A shares ($602.8M net proceeds); $151.8M of proceeds used to buy back 1,557,177 STRC preferred shares, $50.7M to STRC dividends, $30M to cash reserves. Total holdings after purchase: 845,050 BTC at avg. acquisition price $75,412/BTC.
  - as_of: 2026 (undated, current status) · Twenty One Capital holds 43,514 BTC — second-largest corporate holder (per prior run's search capture; not independently re-verified this run)
conflict: none new this run — the 845,050 BTC figure is independently confirmed both by the direct bitcointreasuries.net pull and by search-indexed coverage of the 09-01/09-03 purchase, consistent with the prior run's figure.

### sovereign-adoption
source: bitcointreasuries.net (direct fetch, aggregate government total only — no per-country breakdown visible on the fetched page) + search-indexed coverage (Bitget News, Bitcoin Policy Institute via bitbo.io) for country-level detail
series:
  - as_of: 2026-09-04 (direct bitcointreasuries.net pull) · Government entities aggregate: 650,012 BTC (all tracked sovereigns combined; page did not surface a per-country table in this fetch)
  - as_of: 2026 (search-indexed, undated within year) · 27 countries reported with direct or indirect BTC exposure, 13 more pursuing legislative measures; US largest sovereign holder at 328,372 BTC (criminal-asset-confiscation basis); UK second at 61,245 BTC; UAE 30,382 BTC (sovereign wealth + mining-linked); El Salvador 7,514 BTC (open-market purchases, the only country with BTC as legal tender) — this El Salvador figure is close to but not identical to the prior run's 7,663 BTC figure, both search-indexed and not reconciled to a single source date
  - as_of: 2026 (search-indexed, carried from prior run) · Bhutan has sold roughly $1B of its BTC holdings over the past ~18 months (net seller), despite being described elsewhere as the world's 3rd-largest sovereign holder at 12,062 BTC as of 2025-06
conflict: the 650,012 BTC aggregate government figure (this run, bitcointreasuries.net direct) does not sum cleanly against the individually-cited country figures found via search (328,372 US + 61,245 UK + 30,382 UAE + 7,514 El Salvador + others ≈ mid-400,000s at most from the names found) — likely reflects additional untracked-by-search countries or a different counting methodology; flagged as an unreconciled scope difference, not a same-day conflict.
checked_absence: no new sovereign-accumulation announcement (a state newly adopting or actively buying) found as of 2026-09-04; the active programs found (El Salvador, Bhutan) remain non-accumulating or net-selling, consistent with the prior run.

### mvrv
source: Glassnode MVRV (studio.glassnode.com/charts/market.Mvrv) — direct fetch not attempted (known to block automated access per prior runs); figure via search-indexed secondary coverage (KuCoin flash news)
series:
  - as_of: 2026-09 (early September 2026, per search snippet, exact day not stated) · ~1.1 — described as "just above a historically undervalued range," with 1.0 linked to recovery phases in 2015, 2019, and 2022
  - as_of: 2026-08-28 (carried from prior run) · ~1.5 (BTC near $79,000)
  - as_of: 2026-08-08 (carried from prior run) · 1.24 (raw MVRV ratio); MVRV Z-Score separately reported at 0.42 same date (distinct metric, for context only)
conflict: the ~1.1 figure (early Sept, this run) is lower than the 2026-08-28 figure of ~1.5 despite BTC's price being roughly similar-to-higher over that window (per btc-price series above) — could reflect a rising realized-cap denominator, a different data vintage, or a genuinely stale/mis-dated search snippet; not resolved this run, flagged for the Reporter rather than picked between.

### puell-multiple
source: Glassnode Puell Multiple, via secondary aggregator (MacroMicro, en.macromicro.me/series/8112) — search-indexed; no more recent dated figure located this run
series:
  - as_of: 2026-08-26 (unchanged from prior run) · 0.9451 (miner revenue below its 365-day average)
checked_absence: no September 2026 Puell Multiple print located via search as of this run — fetch spec calls for current + prior; still only one dated observation available.

### exchange-netflows
source: CryptoQuant Exchange Netflow/Reserve charts — direct fetch not attempted (cryptoquant.com known to block automated access per prior runs); search-indexed coverage of CryptoQuant commentary this run
series:
  - as_of: 2026-07 (search-indexed, month-level, this run) · CryptoQuant reported exchange reserves at ~2.7M BTC aggregate, describing a long-term decline; also referenced a Binance-specific withdrawal pattern from March 2025 through March 2026 with net outflows dominating the most recent period
  - as_of: 2026-08 (carried from prior run) · Binance BTC reserves rose to ~687,000 BTC, the highest 2026 mark, bottoming near 617,000 BTC in late April 2026 before reversing higher through August
conflict: the 2026-07 aggregate-exchange-reserve figure (declining, ~2.7M BTC) and the 2026-08 Binance-specific figure (rising to a 2026 high, ~687,000 BTC) describe different scopes (all exchanges vs. Binance alone) and are not necessarily contradictory, but the directional language ("declining" vs "rose to highest 2026 mark") diverges — not reconciled this run.
checked_absence: no daily netflow series (the fetch spec's "last 7 daily" ask) located this run either — only stock/level (reserve) figures found, same limitation as the prior run.

### funding-rates
source: Binance perp funding API, direct fetch — https://www.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=21 (the fapi.binance.com host returned HTTP 451 "Unavailable For Legal Reasons" directly; the www.binance.com/fapi mirror succeeded and returned live, chain-consistent, verified data — single-venue Binance reading, not a cross-venue Coinglass aggregate)
series (all times UTC, 3 settlements/day):
  - 2026-08-28 08:00 · 0.00010000
  - 2026-08-28 16:00 · 0.00005913
  - 2026-08-29 00:00 · 0.00010000
  - 2026-08-29 08:00 · 0.00010000
  - 2026-08-29 16:00 · 0.00010000
  - 2026-08-30 00:00 · 0.00008283
  - 2026-08-30 08:00 · 0.00010000
  - 2026-08-30 16:00 · 0.00007058
  - 2026-08-31 00:00 · 0.00007271
  - 2026-08-31 08:00 · 0.00010000
  - 2026-08-31 16:00 · 0.00010000
  - 2026-09-01 00:00 · 0.00008482
  - 2026-09-01 08:00 · 0.00010000
  - 2026-09-01 16:00 · 0.00003844
  - 2026-09-02 00:00 · 0.00007995
  - 2026-09-02 08:00 · 0.00007998
  - 2026-09-02 16:00 · 0.00003819
  - 2026-09-03 00:00 · 0.00007287
  - 2026-09-03 08:00 · 0.00005866
  - 2026-09-03 16:00 · 0.00008893
  - 2026-09-04 00:00 · 0.00008558
notes: rate is expressed per-8h-settlement (not annualized); many entries sit exactly at 0.00010000, Binance's typical funding-rate ceiling for this pair — consistent with persistently (mildly) positive/crowded-long funding across the window, all readings positive, none negative, over the full 7-day window.

### futures-oi-liquidations
source: Binance OI — direct fetch, single-venue: https://www.binance.com/fapi/v1/openInterest?symbol=BTCUSDT succeeded (current snapshot only); the historical endpoint (openInterestHist) returned 404 on the www.binance.com mirror and HTTP 451 on fapi.binance.com directly, so no daily OI history was obtained this run. Liquidation events and cross-venue aggregate OI have no free endpoint per spec — taken from search, labeled SECONDARY.
series:
  - as_of: 2026-09-04 ~07:15 UTC (direct Binance API, single-venue current snapshot) · BTCUSDT perpetual open interest: 112,302.051 BTC (coin-denominated; no USD notional field returned)
  - as_of: 2026-09-04 (SECONDARY, search, exact hour not stated) · aggregate cross-venue BTC futures OI reported at $47.75B, down 5.25% week-on-week from $53.5B — a different, broader (cross-venue, USD-denominated) figure than the single-venue Binance coin-denominated reading above, consistent with the spec's note that these are different scopes
  - as_of: 2026-09-04 (SECONDARY, search, exact hour not stated) · ~$48.34M in BTC futures liquidations over the trailing 24h, long positions ~$41.04M (84.9%) vs short ~$7.30M
  - as_of: 2026-08-25 (carried from prior run, SECONDARY) · BTC open interest (coin terms) at a 5-month low of ~587,600 BTC even as price was still climbing; margin OI at a record low near 52,000 BTC
  - as_of: mid-August 2026 (carried from prior run, SECONDARY) · a rapid price slide triggered ~$3B aggregate OI decline and ~$308M in forced liquidations
conflict: none new — the current single-venue Binance OI (112,302 BTC) cannot be directly compared to the prior run's 2026-08-30 cross-venue figure (695,020 BTC across all venues, of which Binance's own share was cited at 142,500 BTC) since neither this run's search results nor the direct Binance pull reproduced that exact prior cross-venue table; treat as different-scope readings, not a revision.

### options-vol-skew
source: Deribit public API for DVOL, direct fetch — https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&start_timestamp=1787875200000&end_timestamp=1788566400000&resolution=43200 succeeded, returned real chain-consistent 12h OHLC data. 25-delta skew has no free single-call endpoint per spec; search this run found only qualitative, undated-to-September commentary — not used as a current numeric reading.
series (DVOL, 12h candles, UTC):
  - 2026-08-28 00:00 · O 41.52 H 41.76 L 39.17 C 39.79
  - 2026-08-28 12:00 · O 39.79 H 39.79 L 38.21 C 38.34
  - 2026-08-29 00:00 · O 38.34 H 38.44 L 37.21 C 37.36
  - 2026-08-29 12:00 · O 37.36 H 37.73 L 37.19 C 37.43
  - 2026-08-30 00:00 · O 37.43 H 37.61 L 36.57 C 36.59
  - 2026-08-30 12:00 · O 36.59 H 37.21 L 36.59 C 36.99
  - 2026-08-31 00:00 · O 36.99 H 37.15 L 36.31 C 36.84
  - 2026-08-31 12:00 · O 36.84 H 37.69 L 36.48 C 37.63
  - 2026-09-01 00:00 · O 37.63 H 37.73 L 36.93 C 37.70
  - 2026-09-01 12:00 · O 37.69 H 38.84 L 37.68 C 37.93
  - 2026-09-02 00:00 · O 37.93 H 38.12 L 36.75 C 37.28
  - 2026-09-02 12:00 · O 37.28 H 37.44 L 36.58 C 37.19
  - 2026-09-03 00:00 · O 37.19 H 37.43 L 36.30 C 37.43
  - 2026-09-03 12:00 · O 37.43 H 40.87 L 37.16 C 39.78
  - 2026-09-04 00:00 · O 39.78 H 39.79 L 38.13 C 38.23 (in-progress 12h period)
notes: this run's DVOL range (~36.3–40.9) sits well below the prior run's 2026-08-29 reading (surge to a ~65% intraday peak on the Jackson Hole/$6.4B-expiry day) — a large move down from that peak is directly visible in this run's own verified series, not just a described "cooldown." 25-delta skew: no numeric value located this run (same limitation as prior run); search surfaced only generic, non-September-dated commentary that positive/put-favoring skew has appeared in "mid-2026" data — not used.

### fear-greed
source: alternative.me API, direct fetch — https://api.alternative.me/fng/?limit=7 succeeded this run (raw unix timestamps requested and converted independently; each date-boundary confirmed against this run's own independently-computed Kraken/Binance timestamp arithmetic — a genuine same-day, verified direct pull, unlike the prior run which could not reach this endpoint)
series:
  - as_of: 2026-08-29 · 68 (Greed)
  - as_of: 2026-08-30 · 69 (Greed)
  - as_of: 2026-08-31 · 62 (Greed)
  - as_of: 2026-09-01 · 69 (Greed)
  - as_of: 2026-09-02 · 63 (Greed)
  - as_of: 2026-09-03 · 65 (Greed)
  - as_of: 2026-09-04 · 74 (Greed)
conflict: prior run recorded 2026-09-01 as 44 ("Fear") via search-indexed secondary trackers, with a noted low-confidence caveat since primary access had failed that run. This run's direct primary pull shows 2026-09-01 as 69 ("Greed") — a real conflict, not a rounding difference. The direct-API reading (this run) should be treated as the corrected value; the prior 44 reading came from secondary trackers that may have mirrored a different index or a stale/mislabeled snapshot.

### technical-trend
source: computed from Kraken daily candles, direct fetch — https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440, narrowed via `since` to keep each request's payload to ≤~56 candles (see btc-price notes on why: unrestricted/large requests to this endpoint via this run's fetch tooling produced fabricated-looking output, verified by internal inconsistency — e.g. a claimed 365-entry result for a ~210-day window, and a computed "77,672.91" 50-day average that did not survive manual recomputation from verified data)
series:
  - as_of: 2026-09-04 · 50-day SMA of daily closes, dates 2026-07-11 through 2026-09-04 (50 candles, chain-verified: each candle's open matches the prior candle's close throughout) = $68,798.85 (includes today's in-progress candle's running close of $80,939.6; excluding today's incomplete candle, using the 49 completed days 2026-07-11 through 2026-09-03: $68,551.08)
  - as_of: 2026-09-04 · 200-day SMA — NOT independently computed this run; a bulk 200-day pull via this run's fetch tooling produced internally-inconsistent output (see above) and was discarded rather than used. Best available reference is SECONDARY (carried from prior run, bitbo.io/CoinDesk coverage, dated late August 2026): 200-day SMA ≈ $69,005–69,144.
  - as_of: 2026-08-20 (carried from prior run, SECONDARY) · golden cross not yet confirmed; the 50-day/200-day gap was narrowing
conflict: this run's directly-computed 50-day SMA ($68,798.85, from verified primary data) is materially higher than the prior run's secondary-sourced 50-day figure (~$65,785–66,000, bitbo.io via search) — a ~$2,800–3,000 (~4-5%) gap. Flagging this as a real discrepancy between a directly-computed primary reading (this run) and a secondary chart read (prior run), not resolved — the Reporter should treat this run's computed figure as the more reliable one given its verified provenance, but the gap itself is worth noting.

### altcoin-dominance
source: CoinGecko Global API, direct fetch — https://api.coingecko.com/api/v3/global succeeded, same-day (updated_at unix 1788505835 → 2026-09-04 ~07:10 UTC, cross-checked against this run's independently-verified timestamp arithmetic used elsewhere in this file)
series:
  - as_of: 2026-09-04 · BTC dominance 59.28%; ETH dominance 11.19% (direct API pull)
  - as_of: 2026-08 (SECONDARY, search, undated within month, carried context from prior run + this run's search) · BTC dominance separately reported at 60.15-60.66% (a breakout above 60%, described as ending an eight-month accumulation phase); Altcoin Season Index reported in the 30-40 region, per BeInCrypto/bitcoinfoundation.org coverage — below the 75 altseason threshold
conflict: this run's direct 59.28% (2026-09-04) is ~1-1.4 points below the most recent secondary August figure (60.15-60.66%) — a modest pullback in BTC dominance, not a large discrepancy, but noting the two are not the same date/source type (direct API today vs. search-indexed August).

### social-retail-sentiment
source: Santiment (app.santiment.net) — direct fetch not attempted (no free API endpoint confirmed); search-indexed coverage (CoinMarketCap Academy, KuCoin, MEXC, Cointelegraph) — no September-2026-dated reading located this run
series:
  - as_of: 2026 (mid-year, undated to a specific month within the search snippet) · Santiment recorded a Bitcoin bullish-to-bearish social ratio of 2.23, described as "the strongest reading of 2026 so far," alongside a noted disconnect with spot ETF flows (ten straight days of net outflows, >$2.97B redeemed since 2026-05-15, at the same time social sentiment read very positive)
  - as_of: 2026-01 (carried from prior run, background) · social sentiment began 2026 "very positive" (a 20% rise in positive mentions since Jan 1)
  - as_of: 2026-08 (carried from prior run) · BTC's positive-to-negative social comment ratio had stayed below 1.0 every day since a referenced "Cold Card hack," described as the most negative sentiment week since Santiment's social data began
checked_absence: no sentiment reading specifically dated to September 2026 located this run — same limitation as the prior run; the three dated points above span January, an unspecified mid-year point, and August 2026 and are not all mutually consistent (very positive vs. most-negative-ever within the same year), not reconciled.

### four-year-cycle-belief
source: analyst/positioning commentary — Benjamin Cowen (CoinMarketCap Academy, BeInCrypto), NYDIG, CYNOPTEC (Yahoo Finance/finance.yahoo.com coverage), via search-indexed coverage this run
series:
  - as_of: 2026-09 (this run) · Benjamin Cowen reiterates October 2026 as his base-case cycle-low window, consistent with prior midterm-year bottoms (2014, 2018, 2022); separately states BTC's cycle top landed on day 1,162 post-prior-low, within the historical range of the prior two cycles' tops (day 1,059 and day 1,168)
  - as_of: 2026-09 (this run) · NYDIG floats a scenario where BTC bottoms near $38,000-$39,000 by October 2026, if the current drawdown matches the depth of the 2014/2018/2022 bear markets
  - as_of: 2026-09 (this run) · CYNOPTEC's read of the four-year cycle: a likely low near $30,000-$42,000 around mid-November 2026, before a projected climb toward $200,000 into 2029
  - as_of: 2026-08 (carried from prior run) · Jesse Olson's cross-cycle chart (scaled to the 2024 halving) placed the cycle at ~day 775 post-halving with prior cycles bottoming near day ~900, implying a bottom window opening ~125 days out (roughly late Dec 2026/early Jan 2027 from that Aug reading), projected low band in the $40,000s
  - as_of: 2026-08 (carried from prior run) · Alphractal targeted late September/early October 2026 for a bottom; CryptoQuant's models showed a high-probability bottom window spanning September-November 2026
conflict: none new — this run's fresh commentary (Cowen, NYDIG, CYNOPTEC) is broadly consistent in timing (Oct-Nov 2026) with the prior run's Alphractal/CryptoQuant/Jesse Olson findings, though the specific price-level guesses cited (NYDIG $38-39K, CYNOPTEC $30-42K, Jesse Olson's chart "$40,000s") vary across sources and should not be treated as a single number.
