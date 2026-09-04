# Macro Radar — stream catalog

Seed catalog extracted from `macro-radar-tracker.md` into the five-field schema (see
`project/conventions/project-schemas.md`), 2026-08-29. For review — the Curator maintains it from here.
Retired streams move to `archive.md`.

<!-- ============================ macro-monetary ============================ -->

### fed-funds-path: Fed policy rate path & odds
category:  macro-monetary
impact:    dxy
polarity:  single-direction: the Fed sets the price of money, so a path toward rate cuts weakens the dollar — a path toward cuts is bullish, a path toward hikes is bearish
fetch:     source: FOMC decisions + CME FedWatch / Polymarket meeting-odds · depth: current odds + last 2 readings · type: numeric
notes:     —

### fomc-tone: FOMC statement tone
category:  macro-monetary
impact:    fed-funds-path
polarity:  single-direction: the Fed's communicated stance sets rate-path expectations, so a more dovish tone (more inclined to hold or cut) is bullish
fetch:     source: FOMC statement + minutes, federalreserve.gov · depth: last 12 releases, with vote composition and dissenters · type: text
notes:     tone is a DIFF across the statement series — the Reporter judges it; the Fetcher stores statements verbatim only. Chair changed Powell → Kevin Warsh (took office 2026-05-22); Warsh has signaled he wants markets relying less on explicit Fed forward guidance (pre-2008-style ambiguity) — expect statements/minutes to carry less of the prior explicit reaction-function language, so DIFF against Warsh-era statements, not the Powell-era baseline. His 2026-08-28 Jackson Hole remarks read hawkish on inflation ("firm, fixed" 2% PCE target).

### fed-balance-sheet: Fed balance sheet / QT-QE stance
category:  macro-monetary
impact:    BTC price
polarity:  event-resolution: the Fed adding liquidity back (ending QT, or QE) is bullish; active tightening is bearish
fetch:     source: Fed H.4.1 release + FOMC statements · depth: current stance + change log · type: status
notes:     —

### global-m2: Global M2 money supply
category:  macro-monetary
impact:    BTC price
polarity:  single-direction: more money in the system (rising global M2) is bullish
fetch:     source: aggregated central-bank M2 (a tracked global-M2 series) · depth: last 3 monthly prints · type: numeric
notes:     —

### real-yields: Real 10-year Treasury yield
category:  macro-monetary
impact:    BTC price
polarity:  single-direction: lower real yields make non-yielding assets like BTC relatively more attractive, so falling real yields are bullish
fetch:     source: FRED CSV — https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10&cosd=<today-14d> (10y TIPS real yield, the official daily series; no key needed) · depth: last 5 daily closes · type: numeric
notes:     —

### treasury-issuance: Treasury issuance & buybacks
category:  macro-monetary
impact:    BTC price
polarity:  conditional: depends — buybacks/issuance shifts that raise demand for scarce assets (the Bessent bond-buyback channel) are mildly bullish; heavy issuance draining liquidity is bearish
fetch:     source: Treasury quarterly refunding announcements + buyback operations · depth: current + change log · type: status
notes:     —

### cpi: CPI / Core CPI
category:  macro-monetary
impact:    fed-funds-path
polarity:  scope-to-impact: falling inflation is bullish — scored only through the Fed channel, where cooler CPI makes easing likelier
fetch:     source: BLS CPI release (bls.gov) · depth: last 3 monthly prints · type: numeric
notes:     —

### core-pce: PCE / Core PCE
category:  macro-monetary
impact:    fed-funds-path
polarity:  scope-to-impact: falling core inflation is bullish via the Fed easing channel
fetch:     source: BEA Personal Income & Outlays release (bea.gov) · depth: last 3 monthly prints (headline + core) · type: numeric
notes:     verify forecast-vs-actual against a source that states the numbers explicitly before overwriting a prior reading (the Core PCE re-check)

### labor-market: US labor market (jobs, unemployment)
category:  macro-monetary
impact:    fed-funds-path
polarity:  scope-to-impact: employment is half the Fed's mandate, so weaker jobs push it toward a cut (this row's only channel), and a cut is bullish — so weaker jobs is bullish; the "cooling economy" reading is a separate channel, not scored here
fetch:     source: BLS Employment Situation release (bls.gov) · depth: last 3 monthly prints (payrolls + unemployment rate) · type: numeric
notes:     scope to the Fed channel to keep the direction single — once left as an unresolved "helps or hurts"

### ism-pmi: ISM Manufacturing / Services PMI
category:  macro-monetary
impact:    fed-funds-path
polarity:  single-direction: factories/services growing (PMI above 50 and rising) is bullish, via a more supportive Fed reaction
fetch:     source: the ISM / PR Newswire monthly release (never a secondary characterization) · depth: last 3 monthly prints · type: numeric
notes:     verify against the primary ISM release each run — a secondary "months shrinking" read was wrong once and flipped the lean

### gdp: US GDP
category:  macro-monetary
impact:    fed-funds-path
polarity:  scope-to-impact: weaker growth is bullish through the Fed channel only (it makes easing likelier); the demand-destruction reading is a separate channel not scored here
fetch:     source: BEA GDP release (bea.gov) · depth: last 2 quarterly prints · type: numeric
notes:     —

### consumer-sentiment: Consumer sentiment
category:  macro-monetary
impact:    fed-funds-path
polarity:  scope-to-impact: weakening sentiment is mildly bullish via the Fed channel (softer demand → easier policy)
fetch:     source: UMich Surveys of Consumers + Conference Board · depth: last 3 monthly prints · type: numeric
notes:     —

<!-- ============================ cross-asset ============================ -->

### dxy: US dollar index (DXY)
category:  cross-asset
impact:    BTC price
polarity:  single-direction: a weaker dollar loosens financial conditions and lifts dollar-priced risk assets, so a falling dollar is bullish
fetch:     source: ICE DXY (DX-Y.NYB) via a primary market-data source — no free unauthenticated endpoint is known, so search is expected here; label the reading secondary · depth: last 5 daily closes · type: numeric
notes:     do NOT substitute FRED's DTWEXBGS or DTWEXAFEGS: those are trade-weighted broad-dollar indices, a different index from ICE DXY on a different scale. Swapping them silently changes both the level and the series.

### btc-nasdaq-corr: BTC–Nasdaq correlation
category:  cross-asset
impact:    BTC price
polarity:  single-direction: BTC trading less like a tech stock (a lower reading) is mildly bullish — but a low reading in a calm week is weak evidence it would hold in a real stress event, when cross-asset correlations tend to rise
fetch:     source: 90-day rolling correlation of daily returns, K33 via The Block · depth: last 4 weekly readings · type: numeric
notes:     always name the window (90-day) and source; a single-window reading is not a structural fact

### equity-valuation: Equity valuation (Shiller CAPE)
category:  cross-asset
impact:    BTC price
polarity:  single-direction: a cheaper, less stretched stock market is bullish — a stretched market (high CAPE) is what could drag BTC down through the equity-correlation channel
fetch:     source: Shiller CAPE (multpl.com / Yale) · depth: current + prior print · type: numeric
notes:     —

### gold: Gold price (and BTC–gold correlation)
category:  cross-asset
impact:    BTC price
polarity:  conditional: depends — BTC starting to follow gold's rise (a rising BTC–gold correlation) would be bullish; the trend has strengthened but a single-window correlation reading is still not proof it holds
fetch:     source: spot gold + BTC–gold 90-day correlation · depth: last 5 daily + the latest correlation reading · type: numeric
notes:     the conditional trigger has strengthened materially since seed: the 90-day BTC–gold correlation reached ~0.86 in the first week of September 2026 (a 6-year high, since Covid-2020), up from the ~0.52 5-year-high reading at catalog seed — confirmed independently across multiple outlets (The Block, Yahoo Finance, Bloomingbit, TFTC). Gold itself is near all-time highs (~$4,540/oz). Coverage frames this as a "debasement trade" (BTC and gold both bid on fiat-purchasing-power concerns) coinciding with BTC's correlation to the S&P 500 falling to ~0.18 over the same window — i.e. BTC is reportedly decoupling from equities and coupling to gold at the same time. Treat as a strengthening pattern, not yet a structural fact — a few weeks of one macro regime is not a permanent correlation.

### boj-carry-trade: BOJ policy & yen carry-trade unwind risk
category:  cross-asset
impact:    BTC price (fast path)
polarity:  event-resolution: a hawkish surprise (an outsized BOJ hike) risks forcing a rapid unwind of yen-funded leveraged positions across global risk assets — the Aug-2024 BOJ-hike precedent, when a comparable unwind produced a sharp, fast BTC selloff alongside equities — so a dovish/as-priced outcome is bullish and a larger-than-expected hike is bearish
fetch:     source: Bank of Japan policy statement (boj.or.jp) + USD/JPY spot + primary coverage of carry-trade positioning (Reuters/Bloomberg) · depth: current status + change log · type: status
notes:     added 2026-09-04 (verified across Bloomberg, CNBC, Vantage Markets, FXStreet, independently of each other): BOJ held its policy rate at 1% on 2026-07-31 but officials (Ueda, Takata, Himino) spent the following month talking up the odds of a hike at the next decision, 2026-09-18; the yen has already firmed on carry-trade-unwind flows and intervention talk (Bloomberg reported a "carry trade exodus" as of 2026-09-04). This is a live, dated trigger — track the Sept-18 decision and the size of any hike relative to what's priced, not a generic BOJ-watch.

### credit-spreads: Credit spreads
category:  cross-asset
impact:    BTC price
polarity:  single-direction: tighter/narrower spreads signal healthy risk appetite and are bullish; widening spreads are bearish
fetch:     source: FRED CSV — https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2&cosd=<today-14d> (ICE BofA US High Yield OAS, the official daily series; no key needed) · depth: last 5 daily · type: numeric
notes:     —

<!-- ===================== crypto-structural (supply + regulatory) ===================== -->

### mt-gox: Mt. Gox distribution overhang
category:  crypto-structural
impact:    BTC price
polarity:  time-phased-pivot: creditor coins reaching the market are direct sell-side supply, so it is bearish while the payout runs; turns bullish once complete — soft, since the deadline has slipped twice
fetch:     source: Arkham on-chain wallet balance via The Block · depth: current + change log · type: status
notes:     the ~34,504 BTC figure is a direct wallet balance, not a subtraction; treat the Oct 31, 2026 deadline as soft — this is the third postponement from the original 2023 deadline (2024 → 2025 → 2026)

### strategic-bitcoin-reserve: US Strategic Bitcoin Reserve policy
category:  crypto-structural
impact:    BTC price
polarity:  event-resolution: the government keeping its coins instead of selling them (and any accumulation) is bullish
fetch:     source: SBR executive order + Treasury/White House statements · depth: current + change log · type: status
notes:     as of this run the SBR is a hold-only directive (~328,372 BTC from seizures/forfeitures), not an accumulation mandate — Treasury stated the US "won't be buying" more; Treasury and Commerce are in an unresolved turf war over who administers it. Open-market purchases would require the BITCOIN Act (Senate) or its House companion (Begich's ARMA) to pass — track passage odds, not the current hold-only baseline, as the bullish trigger.

### halving-timeline: Halving schedule
category:  crypto-structural
impact:    BTC price
polarity:  single-direction: the mid-2028 halving cuts new supply, bullish over a long horizon
fetch:     source: Bitcoin protocol schedule (block height) · depth: current status · type: status
notes:     halving-relative timing is a timing-only input, never a price input (backtest lesson 2)

### miner-behavior: Miner behavior
category:  crypto-structural
impact:    BTC price
polarity:  single-direction: miners holding is bullish; miner capitulation/selling into weakness is bearish added supply
fetch:     source: on-chain miner flows (Glassnode / CryptoQuant) · depth: last few readings · type: numeric
notes:     —

### legacy-whale-movements: Legacy / dormant whale movements
category:  crypto-structural
impact:    BTC price
polarity:  single-direction: long-dormant coins moving to exchanges is bearish (potential supply); staying put is neutral-to-bullish
fetch:     source: on-chain dormant-supply / exchange-inflow trackers (Arkham / Glassnode) · depth: current + change log · type: status
notes:     —

### clarity-act: CLARITY Act (market-structure bill)
category:  crypto-structural
impact:    BTC price
polarity:  event-resolution: the law passing is bullish (regulatory clarity for the asset class)
fetch:     source: Senate whip count + Polymarket Sept-15 cloture-vote contract · depth: current odds + last reading · type: status
notes:     track the Sept-15 cloture contract only (~13–14%, stable); other CLARITY Polymarket contracts answer different questions — do not swap them in

### stablecoin-regulation: Stablecoin regulation
category:  crypto-structural
impact:    BTC price
polarity:  event-resolution: clear, supportive stablecoin rules are bullish (they deepen on-ramps); a restrictive turn is bearish
fetch:     source: relevant legislation + Treasury/regulatory statements · depth: current + change log · type: status
notes:     GENIUS Act implementation is progressing on schedule (confirmed via federalregister.gov + occ.gov, not just secondary coverage): Treasury issued a Notice of Proposed Rulemaking 2026-08-18 on when a stablecoin is "issued" in the US and what counts as offering/selling to a US person; comments due 2026-10-19; the Act takes effect 2026-01-18, with unlicensed-issuer stablecoins barred from US offer/sale starting 2028-07-18. Distinct from the separate stablecoin-supply stream's yield-elimination effect — this row tracks the regulatory-clarity channel, not the flow-magnitude channel.

### sec-cftc-posture: SEC / CFTC posture
category:  crypto-structural
impact:    BTC price
polarity:  event-resolution: a more accommodative enforcement/rulemaking posture is bullish; a hostile turn is bearish
fetch:     source: SEC / CFTC actions and statements · depth: current + change log · type: status
notes:     on 2026-08-18 the SEC proposed "Regulation Crypto Assets" (confirmed via sec.gov press release + commissioner statements, independent of secondary coverage) — a tailored offering regime with a startup exemption (up to $5M/4yr), a fundraising exemption (up to $75M/12mo), and a conditional safe harbor letting an issuer "delink" a token from its original investment-contract status; public comments due 2026-10-20. Read as a continuation of the accommodative posture, not a reversal.

### sbr-legal-durability: SBR legal durability
category:  crypto-structural
impact:    strategic-bitcoin-reserve
polarity:  single-direction: legal challenges that threaten the reserve's durability are bearish for it; the order surviving is bullish
fetch:     source: court filings / legal coverage of the SBR order · depth: current + change log · type: status
notes:     —

<!-- ===================== crypto-flows-onchain (flows + derivatives + sentiment) ===================== -->

### btc-price: Bitcoin spot price
category:  crypto-flows-onchain
impact:    — (this IS BTC price — the terminal node every other stream points toward)
polarity:  — (anchor, not a driver: the price is the level "bullish/bearish" is measured against, so it has no direction of its own)
fetch:     source: Kraken OHLC API — https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440 (721 daily candles, oldest first: [time, open, high, low, close, vwap, volume, count]); cross-check the latest level against https://api.coinbase.com/v2/prices/BTC-USD/spot and https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd · depth: last 7 daily closes + the latest candle's intraday high/low · type: numeric
notes:     the report's anchor — the Reporter states the current level and trend and sorts the table toward it; every other stream's Steps count is its distance to this row. HARD REQUIREMENT: this stream must come from a same-day direct API read. A search-sourced, secondary, or previous-day price is NOT acceptable as the anchor — see the Fetcher's anchor rule. The coindesk.com and coingecko.com HTML pages 403/429 automated fetch; never fall back to them.

### spot-etf-flows: Spot ETF flows
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  single-direction: net inflows are bullish — but as a Tier-4b amplifier (moved by price as much as it moves price), read it as magnitude, not an independent cause
fetch:     source: NO free primary endpoint exists — Farside (farside.co.uk/btc/) is the reference table but 403s automated fetch and publishes no public API, and SoSoValue/CoinGlass require a key. Use search-indexed coverage of Farside/SoSoValue and label the reading secondary in `source` · depth: last 10 daily · type: numeric
notes:     —

### stablecoin-supply: Aggregate stablecoin supply
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  single-direction: aggregate stablecoin market cap is the pool of fiat-equivalent, ready-to-deploy on-ramp liquidity sitting in the crypto system, so a growing supply is bullish and a contracting one (net redemptions leaving crypto rails) is bearish — read as flow magnitude, not an independent macro cause
fetch:     source: DefiLlama API — https://stablecoins.llama.fi/stablecoincharts/all (daily series of totalCirculatingUSD.peggedUSD, oldest first; the defillama.com dashboard 403s automated fetch, the API does not) · depth: last 8 weekly readings, sampled from the daily series · type: numeric
notes:     added 2026-09-01 after supply fell ~$14.6B from the May-2026 $322B peak, the sharpest contraction since Terra (confirmed via news.bitcoin.com, cryptonews.net, gncrypto.news independently) — driven by new federal stablecoin rules eliminating yield on USDT/USDC, pushing yield-seeking capital into tokenized T-bill/money-market products. Distinguish that kind of adjacent rotation (less clearly bearish, capital stays crypto-adjacent) from capital actually exiting crypto entirely — the source data alone won't make that distinction, so flag it as a judgment call for the Reporter.

### corporate-treasuries: Corporate treasury accumulation
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  single-direction: companies adding BTC to treasuries is bullish; forced selling is bearish — an amplifier, not an independent driver
fetch:     source: corporate filings + treasury trackers (bitcointreasuries.net) · depth: current + change log · type: status
notes:     —

### sovereign-adoption: Sovereign adoption
category:  crypto-flows-onchain
impact:    BTC price
polarity:  event-resolution: a state adopting or accumulating BTC is bullish
fetch:     source: official announcements + coverage · depth: current + change log · type: status
notes:     —

### mvrv: MVRV ratio
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  contrarian: a very high MVRV (large unrealized profit) is a bearish overheating sign; a low MVRV is bullish — an amplifier read off price, not a cause
fetch:     source: Glassnode MVRV · depth: current + prior · type: numeric
notes:     —

### puell-multiple: Puell Multiple
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  contrarian: a high Puell (miner revenue stretched) is bearish; a low reading is bullish — a derived amplifier
fetch:     source: Glassnode Puell Multiple · depth: current + prior · type: numeric
notes:     —

### exchange-netflows: Exchange netflows
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  single-direction: coins leaving exchanges (net outflows) reduce ready sell supply and are bullish; net inflows are bearish — an amplifier
fetch:     source: on-chain exchange netflow (CryptoQuant / Glassnode) · depth: last 7 daily · type: numeric
notes:     —

### funding-rates: Perpetual funding rates
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  contrarian: very high positive funding (crowded longs) is a bearish squeeze risk; neutral/negative funding is healthier — an amplifier
fetch:     source: Binance perp funding API — https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=21 (three 8h settlements per day). This is a SINGLE-VENUE primary reading, not the Coinglass cross-venue aggregate the stream was originally specified against — say so in `source` · depth: last 7 daily · type: numeric
notes:     —

### futures-oi-liquidations: Futures open interest & liquidations (leverage)
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  amplifier: not one direction — leverage makes the next big move stronger whichever way it goes, and it cuts both ways
fetch:     source: Binance OI history — https://fapi.binance.com/futures/data/openInterestHist?symbol=BTCUSDT&period=1d&limit=7 (single-venue primary, not the Coinglass aggregate — say so in `source`). Liquidation events have no free endpoint: take them from search and label them secondary · depth: current OI + recent liquidation events · type: numeric
notes:     currently meaningfully de-risked vs mid-August; keep downside-amplification reasoning dialled back

### options-vol-skew: Options implied vol & skew
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  amplifier: rising implied vol / heavy put skew signals defensive positioning and bigger moves ahead — magnitude, not direction
fetch:     source: Deribit public API for DVOL — https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&start_timestamp=<ms>&end_timestamp=<ms>&resolution=43200 (returns [ts, open, high, low, close]). 25-delta skew has no free single-call endpoint (deriving it needs per-instrument greeks): take skew from search and label it secondary · depth: current + prior · type: numeric
notes:     —

### fear-greed: Fear & Greed index
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  contrarian: this index works backwards — extreme fear (near the bottom) is bullish, extreme greed (near the top) is bearish
fetch:     source: alternative.me API — https://api.alternative.me/fng/?limit=7 (value + value_classification per day, newest first) · depth: last 7 daily · type: numeric
notes:     name the historical echo when elevated (near the pre-Oct-2025-liquidation zone), not just "Greed = bearish"

### technical-trend: Technical trend (50/200-day moving averages)
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  self-fulfilling: enough of the market (CTAs, systematic funds, retail) trades moving-average crosses that the signal becomes real flow, so price above the 200-day average (or a golden cross firing) is bullish — watched, therefore it moves price, it does not predict it
fetch:     source: computed from the same Kraken daily candles as btc-price — https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440 (721 candles, enough for a 200-day SMA). Record the SMA levels and BTC's position relative to each; arithmetic on the raw closes is not interpretation, but state the closes' date range so the Reporter can check the window · depth: current + prior print · type: numeric
notes:     an amplifier (feedback), never predictive — frame as "watched, so it creates flow"

### altcoin-dominance: Altcoin dominance
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  conditional: depends on where the cycle is — currently resolves to neutral (matching what's expected now)
fetch:     source: CoinGecko global API — https://api.coingecko.com/api/v3/global (data.market_cap_percentage.btc) · depth: current + prior · type: numeric
notes:     —

### social-retail-sentiment: Social / retail sentiment
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  contrarian: euphoric retail/social sentiment is a mild bearish overheating sign; capitulation is bullish — an amplifier
fetch:     source: social-sentiment trackers (LunarCrush / Santiment) · depth: current + recent · type: status
notes:     —

### four-year-cycle-belief: 4-year-cycle belief & positioning
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  self-fulfilling: traders positioning around a believed Oct/Nov 2026 cycle low can make it partly self-fulfilling — tracked as one data point, not proof of a price level
fetch:     source: analyst/positioning commentary on the 4-year cycle · depth: current + recent · type: status
notes:     this is one sentiment/positioning data point, NOT a thesis to reaffirm/strengthen/weaken

<!-- ============================ geopolitical ============================ -->

### iran-hormuz: Iran / Strait of Hormuz
category:  geopolitical
impact:    BTC price (fast path)
polarity:  event-resolution: the conflict/blockade calming down is bullish; escalation (tanker attacks, closure) is bearish via a fast risk-off shock
fetch:     source: multiple outlets, primary where possible · depth: current status + recent-change log · type: status
notes:     this is no longer a latent risk — an active US-Iran war ("Operation Epic Fury") began 2026-02-28 and passed its 6-month mark in late August 2026; Iran claims the Strait remains closed and requires its coordination for passage, shipping traffic stays well below normal, and 70+ attacks on commercial shipping have been recorded. Oman/Qatar are mediating a possible temporary shipping corridor. Track for a ceasefire/corridor deal (bullish) vs. further escalation (bearish), not a binary "war starts" trigger — that already happened. Escalated further as of early Sept 2026 (confirmed via UN News, NPR, NBC's ship-traffic tracker): a brief April ceasefire broke down in July; the Strait is now effectively closed (~6 ships/day transiting vs. ~85/day normal, ~465 vessels holding position, ~6,000 seafarers stranded); Iran has widened its shipping blacklist to 56 vessels and moved to formally ban US/Israeli-linked ships while charging a toll to others; further tanker attacks (incl. one killing two Filipino seafarers) have occurred. No corridor/ceasefire deal has materialized — read the trend as still escalating, not stabilized. Sharp new escalation confirmed 2026-09-01/02 (independently via Axios, Al Jazeera, Gulf News, Reuters/RFE-RL, Times of Israel, thenationalnews.com, globalsecurity.org — this is well beyond a single-source claim): the US struck ~100 IRGC targets including, for the first time, two Iranian government tankers, under a new Trump-approved "tanker for tanker" policy (a US strike on an Iranian tanker for every Iranian attack on a transiting tanker); Iran retaliated with ~25 ballistic missiles and drones against US-linked targets in Bahrain (Sheikh Isa Airbase), Kuwait (Ali Al Salem airbase command/residence), Jordan (13 missiles entered airspace, 10 intercepted), and Erbil, Iraq — no US casualties reported, Iranian state media claims strikes killed civilians incl. a wedding party. The conflict has now materially broadened beyond Hormuz/shipping into direct exchanges with Gulf-state and Iraqi territory. Iran's FM stated (late Aug) the two sides do "not have anything like a ceasefire"; Qatar/Pakistan are passing messages but this is not active negotiation. Read as still escalating and now wider in scope, not stabilizing.

### russia-nato: Russia–NATO tension
category:  geopolitical
impact:    BTC price (fast path)
polarity:  background-probability: a deliberately ambiguous incident against a NATO member would raise Article-5 questions and hit risk assets fast, so no incident is bullish and an incident is bearish — the Lean states a quantified probability, not a direction
fetch:     source: multiple outlets (CBS/CNN/WSJ), primary where possible · depth: current status + change log · type: status
notes:     verify user-supplied leads independently; a single expert or historical parallel is not confirmation; the drone-site claim traces to a single investigation. Since then, confirmed via multiple outlets (NATO.int, ABC News, Al Jazeera): a pattern of Russian drone/missile incursions into NATO airspace has continued through August 2026 — four interceptions over Romania (by Aug 17), a NATO jet shootdown over Latvia (Aug 14), an unexploded drone hitting a Ukrainian cargo plane at Germany's Leipzig/Halle airport (Aug 4) — and NATO allies formally condemned the violations (Aug 12 statement) without invoking Article 5. Treat this as an escalating frequency of ambiguous incidents still below the Article-5 threshold, not a resolved risk — the background probability this stream tracks has risen, not fired.

### russia-ukraine: Russia–Ukraine war
category:  geopolitical
impact:    BTC price (fast path)
polarity:  event-resolution: a genuine diplomatic breakthrough / de-escalation is bullish; major escalation is bearish
fetch:     source: multiple outlets, primary where possible · depth: current status + change log · type: status
notes:     mostly below the threshold that moves BTC on its own. As of late Aug 2026 (Reuters/Kyiv sources), Ukraine's Budanov floated a possible resumption of trilateral (Russia-Ukraine-US) talks in September covering a ceasefire and security guarantees, but Russia's Lavrov has publicly rejected any ceasefire that freezes the current front line — track for an actual signed deal (bullish) vs. this remaining talk-about-talks (no change), not a photo-op or an announced-but-unsigned framework. As of this run, the Kremlin has separately stated talks are on hold with no new proposals on the table — read as stalled, not advancing toward the floated September trilateral.

### china-taiwan: China–Taiwan tensions
category:  geopolitical
impact:    BTC price (fast path)
polarity:  event-resolution: tensions easing is bullish; a blockade or military action is bearish via a fast shock
fetch:     source: multiple outlets, primary where possible · depth: current status + change log · type: status
notes:     Xi Jinping is scheduled for a White House summit with Trump on Sept 24, 2026 (his first US visit since 2023, following Trump's May 2026 Beijing visit) — confirmed independently (Fox News, US News). Arms-sales-to-Taiwan disputes have twice caused US concessions ahead of Trump-Xi meetings this year; watch this date for either a de-escalatory signal or a fresh flashpoint if arms sales are announced beforehand.

### north-korea: North Korea
category:  geopolitical
impact:    BTC price (fast path)
polarity:  event-resolution: quiet is bullish; a major provocation is a small bearish risk
fetch:     source: multiple outlets · depth: current status + change log · type: status
notes:     —

### venezuela-cuba: Venezuela / Cuba
category:  geopolitical
impact:    BTC price (fast path)
polarity:  event-resolution: things returning to normal is bullish; a regional flare-up is bearish
fetch:     source: multiple outlets · depth: current status + change log · type: status
notes:     the acute shock already happened — US forces captured Maduro on 2026-01-03 in a large-scale strike ("Operation Absolute Resolve"); he faces narco-terrorism charges in the SDNY. Delcy Rodríguez is acting president; the US (via Rubio) is running a 3-phase stabilization/transition plan, with talks that began 2026-08-06. Situation remains domestically unstable (reports of intensified repression) but there is no active US military conflict as of this run — watch for a fresh flare-up (bearish) or a settled transition (bullish), not the already-priced capture event. Confirmed independently (Congress.gov CRS report, rsbnetwork.com, Fox News) as of this run: Trump announced a deal with the interim government granting the US control over 65M barrels of Venezuelan oil, described as not impeding the "democratic transition"; opposition figures González Urrutia and Machado remain excluded from power with no sign the interim regime will open institutions to them; a June 24, 2026 pair of earthquakes killed 6,100+ and has complicated stabilization efforts. Net effect is still no active US military conflict — a step toward economic normalization, offset by continued exclusion of the opposition and a fresh humanitarian shock.

### us-infra-cyber: US critical-infrastructure cyberattack risk
category:  geopolitical
impact:    BTC price (fast path)
polarity:  event-resolution: no attack happening is bullish; a major confirmed attack is bearish via a fast shock
fetch:     source: CISA/FBI/EPA advisories + coverage · depth: current status + change log · type: status
notes:     —

### trade-policy-tariffs: Trade policy / tariffs
category:  geopolitical
impact:    BTC price (fast path)
polarity:  event-resolution: de-escalating trade policy is bullish; a fresh tariff shock is bearish via risk-off
fetch:     source: official announcements + coverage · depth: current status + change log · type: status
notes:     as of this run, Trump is weighing a new ~7.5% tariff on China for underpriced/dumped exports, layered on top of the 10-12.5% Section-301 tariffs on 60 countries effective 2026-07-24 — officials are calibrating the size specifically to avoid derailing the year-old US-China trade truce or the planned Trump-Xi White House summit (~Sept 24, see china-taiwan); confirmed independently (AP/Yahoo, Fortune). Watch for the announced size/timing as the next decision point, not just a binary "new tariff" trigger.

<!-- ============================ idiosyncratic ============================ -->

### idiosyncratic-scan: Idiosyncratic / tail-event scan
category:  idiosyncratic
impact:    BTC price (fast path)
polarity:  event-resolution: no bad surprises is bullish; a fresh hack, depeg, major-figure death/scandal, or corporate/bank collapse is bearish
fetch:     source: broad open-ended search (not a fixed list) · depth: current + recent-change log · type: status
notes:     open-ended every run; log "searched, nothing new" as a checked absence. A live event (e.g. an exchange hack) gets promoted to its own stream
