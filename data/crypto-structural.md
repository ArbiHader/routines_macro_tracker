# crypto-structural readings — run 2026-09-02
fetcher: crypto-structural

### mt-gox
source:  Arkham Intelligence wallet tracking, as reported via The Block, Blockworks "Gox Watch," CoinDesk, KuCoin, Decrypt, CoinMarketCap Academy (theblock.co, congress.gov, cryptoquant.com, predictionhunt.com, defirate.com, ccn.com all returned EGRESS_BLOCKED via WebFetch this run — used search-indexed secondary reporting of Arkham on-chain data, consistent with last run's access pattern)
window:  —
series:
  - as_of: 2026-06-02 · 34,504 BTC (~$2.43B) remaining balance per CoinDesk/KuCoin, after a 10,422.65 BTC (~$739M) transfer to a new wallet ahead of the deadline
  - as_of: 2026-08-29 (most recent search result date carried over from prior run, no newer dated figure found this run) · Arkham-labeled wallets "around 35,000 BTC" (~$3.2B) per Blockworks; a separately-dated figure (undated within this run's results, appears to recur from CoinMarketCap Academy background copy) states 34,689 BTC
status: repayment deadline Oct 31, 2026 (third postponement, per streams.md notes, unchanged); ~19,500 creditors repaid to date per Blockworks/trustee announcements, described by the trustee as base/early-lump-sum/intermediate repayment "largely completed" for creditors who completed eligibility procedures without issue; per Blockworks "Gox Watch" cumulative repayment progress, one dated update cites 39% complete with $5.4B left to go, a separate Blockworks headline cites "$3B down, $5.8B left to go" — these two Blockworks figures are inconsistent with each other and neither carries a clear as-of date in this run's search results
conflict: no change from prior run's flagged conflict — a previously-seen "44,878 BTC / $3.19B" figure did not resurface this run. The ~34,500–35,000 BTC range remains the best-corroborated current balance (multiple independently-dated sources: CoinDesk June 2026, Blockworks Aug 2026). Could not reach Arkham's own site or theblock.co directly this run (both egress-blocked) to resolve the exact current figure or the two conflicting Blockworks repayment-progress percentages — flagging both progress figures (39%/$5.4B remaining vs. $3B down/$5.8B remaining) for the Reporter/Curator, as neither could be dated or reconciled this run.

### strategic-bitcoin-reserve
source:  Bloomberg (via news.bitcoin.com, unchainedcrypto.com, atlas21.com, Yahoo Finance, KuCoin), coindesk.com/policy, cryptoimpacthub.com, bitcoinfoundation.org — Treasury.gov / SBR primary statements not independently reachable this run (congress.gov also egress-blocked); relying on secondary coverage of the executive order, agency statements, and legislative trackers
window:  —
series:
  - as_of: 2025-03-06 · Executive Order 14233 signed, establishing the Strategic Bitcoin Reserve + US Digital Asset Stockpile, capitalized by Treasury-forfeited BTC
  - as_of: 2026-02 · total US government BTC holdings ~328,372 BTC (per Bitcoinfoundation.org citing prior reporting); cryptoimpacthub.com separately describes officials as having given holdings figures "differing by 130,000 BTC" (undated within this run's results)
  - as_of: 2026-07-06 · Bloomberg (via coindesk.com/policy and multiple outlets): reserve "remains unbuilt"/"still a work-in-progress"; Treasury's 60-day statutory evaluation report remains undelivered, "more than a year past its deadline"; Treasury and Commerce departments both seeking to administer it; DOJ Office of Legal Counsel reviewing which department has legal authority; no agency formally designated as of that date
status: hold-only directive as of this run, no open-market accumulation; Treasury has stated the US "won't be buying" more (consistent with on-file note); Treasury/Commerce turf war unresolved as of the most recent dated coverage found (2026-07-06) — no newer status update located for August/September 2026 in this search pass. Legislative track: BITCOIN Act (S.954, Lummis) would codify the reserve under Treasury and mandate 1M BTC purchased over 5 years; a separately-introduced bipartisan ARMA Act of 2026 (Begich/Golden, House) proposes accumulating up to 1M BTC over 5 years. One source (bitcoinfoundation.org, undated within this run) states neither bill is expected to move in 2026 given the CLARITY Act's stall and a thin post-Sept-14 Senate floor calendar.
checked_absence: no announcement found of a resolution to the Treasury/Commerce administration dispute, and no news found of open-market BTC purchases, as of 2026-09-02

### halving-timeline
source:  block-height halving trackers (CoinGecko, bitdegree.org, watcher.guru, bitcoinfoundation.org) — protocol schedule is mechanical, cross-checked across multiple trackers
window:  —
series:
  - as_of: 2026-09-02 · current block height reported at 964,592 as of 2026-08-26 (most recent dated reading found); next halving estimated 2028-04-17, at block height 1,050,000, ~85,408 blocks remaining from the 2026-08-26 height; block reward will drop from 3.125 BTC to 1.5625 BTC
status: no change from prior run's logic — 210,000-block interval is exact, calendar date is an estimate that shifts with network hashrate

### miner-behavior
source:  CryptoQuant Miner Reserve / Miner Flows charts (cryptoquant.com — egress-blocked to WebFetch this run), cross-referenced via search-indexed CryptoQuant "quicktake" summaries and TradingView/newsbtc coverage
window:  —
series:
  - as_of: 2026-05-25 (most recent dated reading found this run) · CryptoQuant quicktake: miner reserves continuing a decline, "lowest level since two months ago," coinciding with BTC trading near $77,000; Binance Pool miner reserve also reported falling, described as miners "continuing to trim what they hold in reserve"
status: no reading newer than late May 2026 located this run (prior run's July 2026 figure of ~1.1943M BTC / +1% net inflow, and April 2026's 61,000 BTC reserve drawdown, are carried on file from the prior run but could not be refreshed or corroborated with a September-dated figure — cryptoquant.com itself was unreachable via WebFetch this run, egress-blocked)
checked_absence: no miner-capitulation event found as of 2026-09-02; no direct primary-source (cryptoquant.com) read achieved this run — flagged as a data-freshness gap for the Reporter, not a confirmed reversal from the prior (July 2026 accumulation) reading

### legacy-whale-movements
source:  on-chain dormant-supply / exchange-inflow tracking via Arkham, Galaxy Research, as reported by Yahoo Finance, KuCoin, techtimes.com, bitcoinfoundation.org, crypto.news, yellow.com, bitcoinsistemi.com
window:  —
series:
  - as_of: 2026-07-16 · a 5,908 BTC address dormant since 2017 moved ~$383M, routed to a new wallet (not a known exchange), described as consistent with a custody upgrade
  - as_of: 2026-08-10 · a wallet dormant since January 2014 (26.96 BTC) swept to a fresh address at block 961845, 07:03 UTC — no exchange destination identified
  - as_of: 2026-08-16–08-26 (carried from prior run, unchanged — no newer figure found) · six wallets last active 2011–2014 moved 553.59 BTC (~$40M) combined; five of six to non-exchange addresses, one sent 40 BTC to Boerse Stuttgart Digital (custody/trading venue)
  - as_of: 2026-08-17 (carried from prior run, unchanged) · 3,832 BTC (~$246.6M) net inflow to exchanges per Swiss Whale Intelligence daily reading
  - as_of: 2026-08-18 (carried from prior run, unchanged) · Bloomberg/CryptoQuant: large holders/whales added ~43,000 BTC (~$2.75B) over the trailing 60 days, i.e. net whale accumulation over that window
status: mixed recent readings continue — isolated dormant-coin movements mostly routed to non-exchange/OTC/custody addresses, alongside at least one single-day net exchange-inflow spike and a longer-window net accumulation figure; no single unambiguous current-trend value from one dashboard found as of 2026-09-02; Galaxy Research pattern-level observation (via techtimes.com) reaffirms "most transfers went to unidentified addresses rather than exchanges, suggesting security upgrades or OTC prep rather than immediate sales"
checked_absence: no large-scale coordinated dormant-supply-to-exchange event found as of 2026-09-02 beyond the individual movements logged above

### clarity-act
source:  Polymarket + Kalshi cloture-vote/passage contracts, as reported by CCN, news.bitcoin.com, coinotag.com, cryptonews.com, bitcoinfoundation.org (predictionhunt.com, defirate.com, ccn.com, congress.gov, and Polymarket itself were unreachable to WebFetch directly — network egress blocked — so all figures below are via search-indexed secondary reporting, not a direct primary-source read this run, same limitation as the prior run)
window:  —
series:
  - as_of: 2026-08-05 · Polymarket odds (unspecified contract label) cited at "16%, down from 82% in February 2026"
  - as_of: 2026-08-07 · Senate adjourned without voting on CLARITY Act; Democrats signaling they'd withhold cloture support absent movement on three unresolved issues (ethics/officials' crypto profits provision, DeFi regulatory reach, AML provisions — a fourth sticking point cited elsewhere is bank stablecoin-reward rules)
  - as_of: 2026-08-31 · per predictionhunt.com (via search index, same figure as prior run — page itself unreachable this run to re-verify): "Clarity Act Senate Odds Drop to 26% Before Cloture" — described as Kalshi 22% / Polymarket 29%, blended ~26%, framed specifically as odds of "clearing Senate cloture on September 15"
  - as_of: 2026-08-31/09-01 (multiple outlets, via search index) · a separate, lower figure — Polymarket's "H.R. 3633 signed into law in 2026" contract at 13–14% (defirate.com framing) / Galaxy Digital cut to "10%" / CCN headline cites "odds fall to 19.5%" for what it describes as the Sept-15 vote — three different numeric readings (13–14%, 19.5%, 10%) circulating in coverage of ostensibly the same window
  - as_of: 2026-09-01 (search-index only, via Kalshi order-book description) · Kalshi separately prices ~91% probability the Senate holds a vote on CLARITY Act before Oct 1, but only ~22% that the legislation actually passes — a "vote happens" vs. "law passes" distinction
next_release: cloture vote on the motion to proceed, 2026-09-15, 2:00–2:15pm ET (Sen. Lummis and prior reporting give slightly different times, 2pm vs 2:15pm — unresolved which is exact)
conflict: unresolved from prior run, and worse this run — coverage now shows at least four distinct numeric odds readings for ostensibly the same Sept-15 window (26% predictionhunt/cloture-labeled, 19.5% CCN, 13–14% defirate/"signed into law", 10% Galaxy Digital, plus Kalshi's split 91% vote-happens/22% passes reading). The streams.md note says to track "the Sept-15 cloture-vote contract only (~13–14%, stable)" but stability is no longer supported — figures diverge by outlet and none of predictionhunt.com, defirate.com, ccn.com, or Polymarket itself were directly reachable this run to establish which number is the correct cloture-specific contract. Flagging this explicitly for the Reporter/Curator: the on-file "~13-14%, stable" characterization should not be treated as current without a direct Polymarket read, which this run could not obtain (egress-blocked).

### stablecoin-regulation
source:  U.S. Treasury press release (home.treasury.gov), OCC Bulletin 2026-3 (occ.gov), Federal Register, The Block, Morgan Lewis client alert
window:  —
series:
  - as_of: 2026-08-17 · Treasury issued a Notice of Proposed Rulemaking under GENIUS Act Section 3 and opened public comment; NPRM aims to clarify when a stablecoin is "issued" in the US and when an issuer/service provider is "offering or selling" a payment stablecoin to a US person
  - as_of: 2026-08-18 · rule published in the Federal Register: "GENIUS Act Regulations on Payment Stablecoin Issuance, Offer, and Sale"; this NPRM builds on an advance notice of proposed rulemaking issued by Treasury in September 2025
status: implementation in progress — GENIUS Act itself expected to take effect 2027-01-18; issuers generally barred from offering payment stablecoins in the US without a federal/state license; digital asset service providers generally barred from offering/selling payment stablecoins to US persons unless issued by a licensed issuer, phasing in 2028-07-18. No restrictive/adversarial turn found this run — status reads as continued build-out of the existing supportive framework, unchanged from prior run.
next_release: public comment period on the Section 3 NPRM closes 2026-10-19

### sec-cftc-posture
source:  SEC.gov press releases (2026-76, S7-2026-27), Federal Register, Norton Rose Fulbright and Benesch Law summaries of the SEC-CFTC MOU/joint interpretation, Latham & Watkins US Crypto Policy Tracker, Thompson Coburn client alert
window:  —
series:
  - as_of: 2026-03 · SEC Chair Paul Atkins and CFTC Chair Michael Selig signed a Memorandum of Understanding on inter-agency coordination ("Project Crypto," six core areas: joint interpretations/rulemakings, modernizing clearing/margin frameworks, reducing frictions for exchanges/intermediaries, coordinating enforcement); SEC issued an interpretation (33-11412) clarifying how federal securities laws apply to certain crypto assets/transactions
  - as_of: 2026-05-29 · CFTC issued releases approving/providing initial guidance for crypto-asset perpetual futures contracts, a product class the search summary describes as having developed almost entirely on offshore venues due to prior regulatory uncertainty
  - as_of: 2026-08-18 · SEC proposed new rules titled "Regulation Crypto Assets" (press release 2026-76, file S7-2026-27; Federal Register publication dated 2026-08-21), including two proposed Securities Act registration exemptions for certain crypto-asset investment contracts: a one-time $5M/4-year exemption and a $75M/12-month exemption; accompanied by a public statement from Commissioner Peirce ("Filling the Regulatory Tank")
status: posture described in current coverage as continued accommodation/coordination — search summaries note "many enforcement actions and investigations have been withdrawn under the SEC's new leadership," and DOJ-level signals described elsewhere as "further restraint in DOJ-led crypto enforcement." No hostile-turn events found this run — unchanged direction from prior run.
next_release: public comment period on Regulation Crypto Assets (S7-2026-27) closes 2026-10-20 (60 days from Federal Register publication)
checked_absence: no new enforcement crackdown or adversarial rulemaking found as of 2026-09-02

### sbr-legal-durability
source:  Bloomberg (via theblock.co headline, news.bitcoin.com, unchainedcrypto.com), kucoin.com, cryptowisser.com, cryptoimpacthub.com — court-filing search again found no active litigation directly challenging the SBR executive order; legal-durability coverage continues to center on an intra-executive-branch authority dispute
window:  —
series:
  - as_of: 2026-07-06 · Bloomberg (via theblock.co: "Trump strategic bitcoin reserve hits legal and jurisdictional snag"): Treasury and Commerce departments both seeking to administer the reserve (~300,000+ BTC, ~$21B); Treasury officials questioning whether they have legal authority to oversee the SBR at all; DOJ Office of Legal Counsel reviewing the legal framework; Treasury's statutorily-required 60-day evaluation report remains undelivered, over a year past its deadline
  - as_of: 2026-07 (undated more precisely within this run) · cryptoimpacthub.com "18 Months In" retrospective: officials have given holdings figures differing by 130,000 BTC; the founding audit found private keys stored in desk drawers; one custodian was exploited for over $60M
status: as of this run, no court case/lawsuit was found directly challenging Executive Order 14233 or the SBR itself, unchanged from prior run — the "legal durability" risk currently found in coverage remains an administrative/executive-branch authority dispute (Treasury vs. Commerce, pending DOJ OLC review), not litigation. No new litigation-framed headline (the btcc.com "Legal Battle" headline flagged last run) resurfaced in this run's search results.
checked_absence: no new court filing directly challenging the SBR executive order found as of 2026-09-02
