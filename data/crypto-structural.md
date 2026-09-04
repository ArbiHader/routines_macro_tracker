# crypto-structural readings — run 2026-09-03
fetcher: crypto-structural

### mt-gox
source:  Arkham Intelligence wallet data, via The Block (theblock.co — two articles fetched directly this run: post/379197 and news/business/2026-06-02-mt-gox-moves-739-million-btc-403296), cross-checked against search-indexed coverage (Yahoo Finance, Decrypt, CoinDesk, bcointalk.com, cryptorank.io). Arkham's own site (arkm.com/explorer/entity/mt-gox) returned HTTP 403 to direct WebFetch this run — could not read the primary dashboard directly.
window:  —
series:
  - as_of: 2025-11-17/18 · theblock.co (fetched directly): a "late night Monday" transfer of 10,608 BTC (~$956M) — 10,422 BTC to an unmarked wallet, 185.5 BTC to Mt. Gox's own hot wallet; total balance stated as 34,689 BTC (~$3.1B) as of the Nov 18, 2025 article publish date
  - as_of: 2026-06-02 · theblock.co (fetched directly): 10,422.65 BTC (~$739M) transfer to a new wallet ahead of the deadline; balance stated as 34,504 BTC (~$2.43B/"over $2.4B" depending on the BTC price used)
  - as_of: undated within this run · bcointalk.com headline "Mt. Gox Transfers $2.4B Bitcoin Amid $82K BTC Price: Arkham" (site 403-blocked to direct WebFetch, read only via search snippet) describing "$2.4B in bitcoin to two wallets," "over 30,000 BTC from one wallet to a new wallet," "$200M to a Mt. Gox cold wallet" — could not confirm an exact date, and the $2.4B figure/BTC-count is consistent with a restatement of the June 2026 34,504 BTC balance at a later BTC price (~$78-82K, which matches today's ~$78-81K spot level) rather than clearly evidencing a distinct new transfer event; flagged as unconfirmed, not treated as a new balance figure
status: repayment deadline Oct 31, 2026 (third postponement from the original 2023 deadline, unchanged); ~19,500 creditors repaid to date per trustee/Blockworks reporting (unchanged from prior run, no newer creditor-count figure found this run); base/early-lump-sum/intermediate repayment "largely completed" for creditors who completed eligibility procedures without issue
conflict: current balance figures remain inconsistent across dated sources: 34,689 BTC (Nov 2025), 34,504 BTC (June 2026), and an unresolved, undated "35,583 BTC" figure recurring in some theblock.co article titles (post/347884, not independently dated this run) and an Arkham-tweet-sourced "$1.95B/$2.19B wallet" reference (also undated/unclear this run). No single current-as-of-September-2026 figure was obtained directly from Arkham (site 403-blocked). The bcointalk.com "$2.4B transfer" headline could not be reconciled as a new event vs. a restated balance — flagging for the Reporter/Curator rather than picking a number.

### strategic-bitcoin-reserve
source:  Unchained Crypto, Wikipedia (U.S. Strategic Bitcoin Reserve), The Block ("What Is the U.S. Strategic Bitcoin Reserve?"), TheStreet Crypto, TradingView (Bloomberg-sourced), Bitcoin Foundation, Crypto Impact Hub, Yahoo Finance, Bitcoin Magazine — Treasury.gov/White House primary statements and congress.gov not independently reachable this run for this stream (no new primary text found beyond what was already logged prior run)
window:  —
series:
  - as_of: 2025-03-06 · Executive Order 14233 signed, establishing the Strategic Bitcoin Reserve + US Digital Asset Stockpile, capitalized by Treasury-forfeited BTC, envisioned as housed inside Treasury
  - as_of: 2026-05 (undated more precisely within this run) · TheStreet Crypto (White House digital-asset adviser Patrick Witt, via search index): administration "planned to share significant news about the Strategic Bitcoin Reserve in the near term," stating his team had "cleared a key legal hurdle" — no follow-up announcement found in this run's results
  - as_of: 2026-07-06 · Bloomberg/coindesk.com (carried from prior run, unchanged): reserve "remains unbuilt," Treasury's 60-day statutory evaluation report still undelivered ("more than a year past its deadline"), Treasury and Commerce both seeking to administer it, DOJ Office of Legal Counsel reviewing legal authority
  - as_of: 2026-09 (undated within this run) · Unchained Crypto headline: "Sixteen months after Trump ordered a Strategic Bitcoin Reserve created, Treasury and Commerce are still fighting over who runs it" — describes holdings as "over 300,000 BTC, worth about $21 billion," consistent in order of magnitude with the on-file ~328,372 BTC figure
status: hold-only directive as of this run, no open-market accumulation found; Treasury has stated the US "won't be buying" more (unchanged). Treasury/Commerce turf war remains unresolved as of the most recent dated coverage (2026-07-06); no newer dated status update for August/September 2026 located this run beyond the undated "still fighting" Unchained headline above. Legislative track unchanged: BITCOIN Act (S.954, Lummis, Senate Banking Committee) would mandate 1M BTC purchased over 5 years if enacted; ARMA Act of 2026 (Begich/Golden, House, introduced 2026-05-21) proposes a parallel path (up to 1M BTC over 5 years per some secondary coverage, though the underlying bill text — per prior run's more careful read — frames it as a 20-year hold minimum plus a study of budget-neutral acquisition strategies, not a hard purchase mandate; treat specific BTC-amount targets from secondary crypto-media as unconfirmed, consistent with the streams.md note). No Senate or House floor action on either bill found this run.
conflict: one search result this run (undated, low-confidence) cited total US government BTC holdings as "approximately 198,000 BTC," materially below the on-file ~328,372 BTC and this run's "over 300,000 BTC" figures — could not verify this lower figure's source or date; flagging it rather than adopting it, as the ~300,000-328,372 BTC range remains better corroborated across independently-dated sources.
checked_absence: no announcement found of a resolution to the Treasury/Commerce administration dispute, and no news found of open-market BTC purchases, as of 2026-09-03

### halving-timeline
source:  mempool.space API — https://mempool.space/api/blocks/tip/height (current block height, fetched directly) and https://mempool.space/api/v1/difficulty-adjustment (fetched directly, for average block time); cross-checked in direction against prior-run trackers (CoinGecko, bitdegree.org, watcher.guru)
window:  —
series:
  - as_of: 2026-09-03 · current block height 965,356 (mempool.space API, direct read, same-day); next halving at block height 1,050,000 (210,000-block interval, mechanical); 84,644 blocks remaining; current difficulty-epoch average block time 594,351 ms (~9.9 min/block) per the difficulty-adjustment endpoint; at that pace, ~84,644 blocks ≈ 582 days ≈ estimated early-to-mid April 2028 (consistent with, and a modest refinement of, the prior run's 2028-04-17 estimate); block reward will drop from 3.125 BTC to 1.5625 BTC at halving
status: no change in mechanics from prior run — the 210,000-block interval is exact, the calendar date is a projection that shifts with network hashrate/difficulty

### miner-behavior
source:  CryptoQuant (cryptoquant.com quicktake pages — both the one located this run and the one located last run returned HTTP 403 to direct WebFetch), cross-referenced via search-indexed CryptoQuant-attributed coverage (news.bitcoin.com, TradingView/newsbtc, The Block headline, beincrypto.com)
window:  —
series:
  - as_of: 2026-05-25 (most recent directly-dated CryptoQuant reading found, carried from prior run — no newer dated figure located this run) · CryptoQuant quicktake: miner reserves "lowest level since two months ago," BTC trading near $77,000; Binance Pool miner reserve also falling
  - as_of: undated within this run · a CryptoQuant quicktake titled "Bitcoin Miner Selling Pressure Nears Its End — Supply Contraction Signals the Next Uptrend Phase" was located via search (URL: cryptoquant.com/insights/quicktake/69e294a16aae2d16bb46e107) but the page 403-blocked direct WebFetch this run; only the title was obtained, not the body/data/date — recorded verbatim as found, not corroborated
  - as_of: 2026-08 (undated more precisely within this run) · news.bitcoin.com, citing CryptoQuant: "wallets with 100+ BTC added 60,000 bitcoin in August while smaller holders sold roughly 47,000 BTC combined" — this is described as a large-holder/whale-wallet metric (100+ BTC threshold), not explicitly the miner-wallet-labeled subset this stream tracks; flagging the distinction rather than conflating it with miner reserves
status: no miner-specific reading newer than May 2026 was directly corroborated this run; cryptoquant.com itself remained unreachable via WebFetch (403) for both the older and a newly located quicktake URL — flagged as a continuing data-freshness gap for the Reporter, same limitation as the prior run
checked_absence: no miner-capitulation event found as of 2026-09-03

### legacy-whale-movements
source:  on-chain dormant-supply / exchange-inflow tracking via Arkham/Galaxy Research/CryptoQuant, as reported by CoinDesk, KuCoin, Yahoo Finance, cryptonomist.ch, techtimes.com, bitcoinfoundation.org, crypto.news, yellow.com, bitcoinsistemi.com, news.bitcoin.com (cryptonomist.ch and bcointalk.com 403-blocked direct WebFetch this run; figures below via search index)
window:  —
series:
  - as_of: 2026-08-04 · CoinDesk (search-indexed, not directly fetched): a Bitcoin wallet dormant since 2013 moved ~$31M, described as "not the only one" in a wave of old-coin movements following a Coldcard hardware-wallet hack — new this run, not on prior file
  - as_of: 2026-07-16 (carried, unchanged) · a 5,908 BTC address dormant since 2017 moved ~$383M, routed to a new wallet (not a known exchange), consistent with a custody upgrade
  - as_of: 2026-08-10 (carried, unchanged) · a wallet dormant since January 2014 (26.96 BTC) swept to a fresh address at block 961845, 07:03 UTC — no exchange destination identified
  - as_of: 2026-08-16–08-26 (carried, re-confirmed via a fresh search this run) · six wallets last active 2011–2014 moved 553.59 BTC (~$40M/$40.15M) combined; five of six to non-exchange addresses; one 40 BTC wallet last touched May 2012 sent to a known venue (Boerse Stuttgart Digital, per prior run's more specific read)
  - as_of: 2026-08 (undated more precisely within this run) · news.bitcoin.com, citing CryptoQuant: wallets with 100+ BTC added a combined ~60,000 BTC over August 2026 while sub-100-BTC holders sold ~47,000 BTC combined — a net whale-accumulation reading for the month, distinct from the individual dormant-coin moves above
  - as_of: 2026-08-17 (carried, unchanged) · 3,832 BTC (~$246.6M) net inflow to exchanges per Swiss Whale Intelligence daily reading
  - as_of: 2026-08-18 (carried, unchanged) · Bloomberg/CryptoQuant: large holders/whales added ~43,000 BTC (~$2.75B) over the trailing 60 days
status: same mixed pattern as prior run continues — isolated dormant-coin movements mostly routed to non-exchange/OTC/custody addresses, alongside one single-day net exchange-inflow spike, and now two separately-sourced whale-accumulation readings (43,000 BTC/60-day and 60,000 BTC/August) pointing the same direction (net accumulation); no single unambiguous current-trend value from one dashboard found as of 2026-09-03
checked_absence: no large-scale coordinated dormant-supply-to-exchange event found as of 2026-09-03 beyond the individual movements logged above

### clarity-act
source:  The Block (theblock.co, search-indexed — "Majority Leader Thune files cloture on Clarity Act" article), Congress.gov (H.R.3633 bill page fetched directly but its "all-actions" sub-page returned HTTP 403), Motley Fool/Yahoo Finance, ir-impact.com, coinpedia.org, bitcoinfoundation.org, CCN, predictionhunt.com, defirate.com, coinotag.com, crypto.news, disruptionbanking.com, yellow.com (all via search index — Polymarket/Kalshi themselves and predictionhunt.com/defirate.com were not directly reachable to WebFetch this run)
window:  —
series:
  - as_of: 2026-08-08 · Senate Majority Leader Thune filed cloture on the motion to proceed to the CLARITY Act just before the August recess, setting up the Sept 15 vote
  - as_of: 2026-08-21 · Motley Fool/Yahoo: cloture vote confirmed for Sept 15; Coinbase CEO Brian Armstrong quoted predicting passage
  - as_of: 2026-08-31 · predictionhunt.com (search-indexed only, page not directly reachable): "Clarity Act Senate Odds Drop to 26% Before Cloture" — Kalshi 22% / Polymarket 29%, blended ~26%, framed as odds of clearing Senate cloture on Sept 15
  - as_of: 2026-08-31/09-01 (multiple outlets, search-indexed) · a cluster of differing figures for what outlets frame as the same Sept-15-window question: Polymarket "13%" (CCN, described as a collapse from 82% in February), CCN headline "19.5%," defirate.com "16%" (fact-sheet page title) and separately "13-14%" (H.R.3633-signed-into-law framing), Galaxy Digital "10%," coinotag.com "15%"
  - as_of: 2026-09-01 (search-index only) · Kalshi separately prices ~91% probability the Senate holds a vote before Oct 1, but only ~22% that the legislation actually passes
  - as_of: 2026-09-02 (search-indexed) · House leadership canceled the chamber's last two weeks of September; House will be out of session by Sept 17, two days after the Senate's scheduled Sept 15 cloture vote — raising the risk of no House vote until a post-midterms lame-duck session
next_release: cloture vote on the motion to proceed, 2026-09-15, 2:15pm ET (this run's sources consistently give 2:15pm, resolving last run's 2pm/2:15pm ambiguity); 60 votes needed (Republicans hold 53 seats, so at least 7 Democrats/independents required)
conflict: unresolved, same as prior run — at least six distinct numeric odds readings now circulate for ostensibly the Sept-15 cloture window (26% predictionhunt/Kalshi-Polymarket blend, 19.5% CCN, 16% defirate, 13-14% defirate/"signed into law" framing, 13% CCN/Polymarket-only, 10% Galaxy Digital, 15% coinotag), plus Kalshi's separate 91%-vote-happens/22%-passes split. None of Polymarket, Kalshi, predictionhunt.com, or defirate.com were directly reachable this run to establish a single authoritative cloture-specific figure — flagging for the Reporter/Curator; the streams.md note's "~13-14%, stable" characterization should not be treated as current or stable without a direct read.

### stablecoin-regulation
source:  U.S. Treasury press release, fetched directly — https://home.treasury.gov/news/press-releases/sb0605; SEC.gov/Federal Register cross-reference for comment-period mechanics; OCC Bulletin 2026-3 (occ.gov, via prior run, unchanged)
window:  —
series:
  - as_of: 2026-08-17 · Treasury press release (fetched directly): NPRM implementing GENIUS Act Section 3, governing who may issue/offer/sell payment stablecoins to US persons; Treasury Secretary Bessent quoted: framework aims to "provide the regulatory certainty businesses need to innovate" while maintaining "the role of the U.S. dollar as the world's reserve currency"; builds on a September 2025 advance notice
  - as_of: 2026-08-18 · rule published in the Federal Register as "GENIUS Act Regulations on Payment Stablecoin Issuance, Offer, and Sale"
status: implementation in progress, unchanged from prior run — beginning 2027-01-18, issuers must hold a federal/state license to issue payment stablecoins in the US; starting 2028-07-18, only licensed issuers' stablecoins may be sold to US persons by digital asset service providers. No restrictive/adversarial turn found this run — continued build-out of the existing supportive framework.
next_release: public comment period on the Section 3 NPRM closes 2026-10-19 (60 days from Federal Register publication, confirmed)

### sec-cftc-posture
source:  SEC.gov press release, fetched directly — https://www.sec.gov/newsroom/press-releases/2026-76-sec-proposes-new-regulation-crypto-assets; Federal Register cross-reference (federalregister.gov redirected to an unblock interstitial this run, not independently re-confirmed — comment-close date taken from the 60-day-from-publication statement in the SEC press release and prior run's Federal Register read); Thompson Coburn client alert, Latham & Watkins US Crypto Policy Tracker
window:  —
series:
  - as_of: 2026-03 (carried, unchanged) · SEC Chair Atkins and CFTC Chair Selig signed an inter-agency MOU ("Project Crypto," six coordination areas); SEC issued interpretation 33-11412
  - as_of: 2026-05-29 (carried, unchanged) · CFTC issued releases approving/guiding crypto-asset perpetual futures contracts
  - as_of: 2026-08-18 · SEC press release 2026-76 (fetched directly): "Regulation Crypto Assets" proposed (file S7-2026-27); two proposed Securities Act registration exemptions — a $5M/4-year "startup exemption" and a $75M/12-month "fundraising exemption"; a conditional safe harbor deeming certain crypto assets outside the "investment contract" definition; state securities-law preemption for offerings made under the regulation; Chairman Atkins quoted on a safe harbor once "essential managerial efforts" cease; accompanied by statements from Commissioners Peirce and Uyeda and Chairman Atkins
status: posture continues to read as accommodation/coordination, unchanged direction from prior run — no hostile-turn events found this run
next_release: public comment period on Regulation Crypto Assets (S7-2026-27) closes 2026-10-20 (60 days from Federal Register publication, per the SEC press release)
checked_absence: no new enforcement crackdown or adversarial rulemaking found as of 2026-09-03

### sbr-legal-durability
source:  Wikipedia (U.S. Strategic Bitcoin Reserve), Law360, cryptoslate.com (Executive Order 14233 law profile), Lexology, National Law Review, GovInfo (DCPD-202500335), news.bitcoin.com (Bloomberg-sourced), TheStreet Crypto — no active litigation directly challenging the SBR executive order found this run; a fresh search targeted specifically at "lawsuit"/"legal challenge" again returned only the Treasury-vs-Commerce administrative dispute, not court filings
window:  —
series:
  - as_of: 2025-03-06 (carried) · Executive Order 14233 signed (GovInfo DCPD-202500335, primary text record)
  - as_of: 2026-07-06 (carried, unchanged) · Treasury and Commerce both seeking to administer the reserve; Treasury officials questioning whether they have legal authority to oversee the SBR at all; DOJ Office of Legal Counsel reviewing; Treasury's statutory 60-day evaluation report still undelivered, over a year past deadline
  - as_of: 2026-05 (undated more precisely within this run) · TheStreet Crypto (Patrick Witt, White House digital-asset adviser): team had "cleared a key legal hurdle," anticipated a forthcoming announcement — no follow-up located this run confirming what hurdle was cleared or whether an announcement followed
status: as of this run, no court case/lawsuit was found directly challenging Executive Order 14233 or the SBR itself, unchanged from prior run — legal-durability risk in current coverage remains an intra-executive-branch authority dispute (Treasury vs. Commerce, pending DOJ OLC review), not litigation
checked_absence: no new court filing directly challenging the SBR executive order found as of 2026-09-03
