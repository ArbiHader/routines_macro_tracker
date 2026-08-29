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
notes:     tone is a DIFF across the statement series — the Reporter judges it; the Fetcher stores statements verbatim only

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
fetch:     source: TIPS-implied 10y real yield (FRED DFII10) · depth: last 5 daily closes · type: numeric
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
fetch:     source: ICE DXY via a primary market-data source · depth: last 5 daily closes · type: numeric
notes:     —

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
polarity:  conditional: depends — BTC starting to follow gold's rise (a rising BTC–gold correlation) would be bullish; not yet a confirmed trend
fetch:     source: spot gold + BTC–gold 90-day correlation · depth: last 5 daily + the latest correlation reading · type: numeric
notes:     the conditional trigger is BTC beginning to track gold (corr jumped to ~0.52, a 5y high)

### credit-spreads: Credit spreads
category:  cross-asset
impact:    BTC price
polarity:  single-direction: tighter/narrower spreads signal healthy risk appetite and are bullish; widening spreads are bearish
fetch:     source: ICE BofA US High Yield OAS (FRED) · depth: last 5 daily · type: numeric
notes:     —

<!-- ===================== crypto-structural (supply + regulatory) ===================== -->

### mt-gox: Mt. Gox distribution overhang
category:  crypto-structural
impact:    BTC price
polarity:  time-phased-pivot: creditor coins reaching the market are direct sell-side supply, so it is bearish while the payout runs; turns bullish once complete — soft, since the deadline has slipped twice
fetch:     source: Arkham on-chain wallet balance via The Block · depth: current + change log · type: status
notes:     the ~34,504 BTC figure is a direct wallet balance, not a subtraction; treat the Oct 31 deadline as soft (two prior extensions)

### strategic-bitcoin-reserve: US Strategic Bitcoin Reserve policy
category:  crypto-structural
impact:    BTC price
polarity:  event-resolution: the government keeping its coins instead of selling them (and any accumulation) is bullish
fetch:     source: SBR executive order + Treasury/White House statements · depth: current + change log · type: status
notes:     —

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
notes:     —

### sec-cftc-posture: SEC / CFTC posture
category:  crypto-structural
impact:    BTC price
polarity:  event-resolution: a more accommodative enforcement/rulemaking posture is bullish; a hostile turn is bearish
fetch:     source: SEC / CFTC actions and statements · depth: current + change log · type: status
notes:     —

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
fetch:     source: spot BTC from a primary exchange index (Coinbase / a reputable aggregate) · depth: last 7 daily closes + the latest intraday high/low · type: numeric
notes:     the report's anchor — the Reporter states the current level and trend and sorts the table toward it; every other stream's Steps count is its distance to this row

### spot-etf-flows: Spot ETF flows
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  single-direction: net inflows are bullish — but as a Tier-4b amplifier (moved by price as much as it moves price), read it as magnitude, not an independent cause
fetch:     source: daily ETF net-flow trackers (Farside / SoSoValue) · depth: last 10 daily · type: numeric
notes:     —

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
fetch:     source: aggregated perp funding (Coinglass) · depth: last 7 daily · type: numeric
notes:     —

### futures-oi-liquidations: Futures open interest & liquidations (leverage)
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  amplifier: not one direction — leverage makes the next big move stronger whichever way it goes, and it cuts both ways
fetch:     source: aggregated OI + liquidations (Coinglass) · depth: current OI + recent liquidation events · type: numeric
notes:     currently meaningfully de-risked vs mid-August; keep downside-amplification reasoning dialled back

### options-vol-skew: Options implied vol & skew
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  amplifier: rising implied vol / heavy put skew signals defensive positioning and bigger moves ahead — magnitude, not direction
fetch:     source: Deribit DVOL + 25-delta skew · depth: current + prior · type: numeric
notes:     —

### fear-greed: Fear & Greed index
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  contrarian: this index works backwards — extreme fear (near the bottom) is bullish, extreme greed (near the top) is bearish
fetch:     source: alternative.me Crypto Fear & Greed Index · depth: last 7 daily · type: numeric
notes:     name the historical echo when elevated (near the pre-Oct-2025-liquidation zone), not just "Greed = bearish"

### technical-trend: Technical trend (50/200-day moving averages)
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  self-fulfilling: enough of the market (CTAs, systematic funds, retail) trades moving-average crosses that the signal becomes real flow, so price above the 200-day average (or a golden cross firing) is bullish — watched, therefore it moves price, it does not predict it
fetch:     source: 50-day & 200-day SMA levels stated directly by a source, sanity-checked against the SMA math · depth: current + prior print · type: numeric
notes:     an amplifier (feedback), never predictive — frame as "watched, so it creates flow"

### altcoin-dominance: Altcoin dominance
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  conditional: depends on where the cycle is — currently resolves to neutral (matching what's expected now)
fetch:     source: BTC dominance / altcoin-season index · depth: current + prior · type: numeric
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
notes:     —

### russia-nato: Russia–NATO tension
category:  geopolitical
impact:    BTC price (fast path)
polarity:  background-probability: a deliberately ambiguous incident against a NATO member would raise Article-5 questions and hit risk assets fast, so no incident is bullish and an incident is bearish — the Lean states a quantified probability, not a direction
fetch:     source: multiple outlets (CBS/CNN/WSJ), primary where possible · depth: current status + change log · type: status
notes:     verify user-supplied leads independently; a single expert or historical parallel is not confirmation; the drone-site claim traces to a single investigation

### russia-ukraine: Russia–Ukraine war
category:  geopolitical
impact:    BTC price (fast path)
polarity:  event-resolution: a genuine diplomatic breakthrough / de-escalation is bullish; major escalation is bearish
fetch:     source: multiple outlets, primary where possible · depth: current status + change log · type: status
notes:     mostly below the threshold that moves BTC on its own

### china-taiwan: China–Taiwan tensions
category:  geopolitical
impact:    BTC price (fast path)
polarity:  event-resolution: tensions easing is bullish; a blockade or military action is bearish via a fast shock
fetch:     source: multiple outlets, primary where possible · depth: current status + change log · type: status
notes:     —

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
notes:     currently mostly settled / domestic-regional, not a global market mover

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
notes:     —

<!-- ============================ idiosyncratic ============================ -->

### idiosyncratic-scan: Idiosyncratic / tail-event scan
category:  idiosyncratic
impact:    BTC price (fast path)
polarity:  event-resolution: no bad surprises is bullish; a fresh hack, depeg, major-figure death/scandal, or corporate/bank collapse is bearish
fetch:     source: broad open-ended search (not a fixed list) · depth: current + recent-change log · type: status
notes:     open-ended every run; log "searched, nothing new" as a checked absence. A live event (e.g. an exchange hack) gets promoted to its own stream
