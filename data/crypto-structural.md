# crypto-structural readings — run 2026-09-05
fetcher: crypto-structural

### mt-gox
source:  search-indexed coverage of Arkham Intelligence wallet data via The Block (theblock.co), Decrypt, CoinDesk, CryptoRank.io, Yahoo Finance, Financemagnates.com — Arkham's own dashboard (arkm.com/explorer/entity/mt-gox) not directly reachable this run (not attempted via direct WebFetch this run; relying on search-indexed secondary coverage of Arkham data, consistent with the 403-block pattern established in prior runs)
window:  —
series:
  - as_of: 2025-11-17/18 · (carried, unchanged) theblock.co: a transfer of 10,608 BTC (~$956M) — 10,422 BTC to an unmarked wallet, 185.5 BTC to Mt. Gox's own hot wallet; total balance stated as 34,689 BTC (~$3.1B) as of publish date
  - as_of: 2026-06-02 · (carried, unchanged) theblock.co/coindesk.com: 10,422.65 BTC (~$739M) transfer to a new wallet ahead of the deadline; balance stated as 34,504 BTC (~$2.43B)
  - as_of: undated, recurring across multiple article titles (carried) · theblock.co post/347884 headline cites a separate, undated "35,583 BTC" balance figure not reconciled to a specific date this run either
  - as_of: 2026-09-05 · no new balance figure or transfer event located this run beyond the above — search results returned the same June 2026 34,504 BTC figure as the most recent dated reading
status: repayment deadline Oct 31, 2026 (third postponement from the original 2023 deadline, unchanged); ~19,500 creditors repaid to date per trustee reporting (unchanged, no newer creditor-count figure found); base/early-lump-sum/intermediate repayment "largely completed" for creditors who completed eligibility procedures without issue
conflict: same unresolved balance inconsistency as prior runs — 34,689 BTC (Nov 2025), 34,504 BTC (June 2026), and an undated "35,583 BTC" figure recurring in one theblock.co article title — no single current-as-of-September-2026 figure obtained from Arkham directly this run either; flagging for the Reporter/Curator rather than picking a number
checked_absence: no new transfer event or balance update found as of 2026-09-05 beyond the June 2026 reading already on file

### strategic-bitcoin-reserve
source:  cryptoimpacthub.com ("The Strategic Bitcoin Reserve, 18 Months In: Cold Wallets in Desk Drawers and No Authority to Buy," fetched directly), Unchained Crypto, Wikipedia (U.S. Strategic Bitcoin Reserve), TheStreet Crypto, coindesk.com/policy 2026-07-06 (carried) — Treasury.gov/White House primary statements not independently re-fetched this run beyond the Bessent quote carried via cryptoimpacthub.com's citation
window:  —
series:
  - as_of: 2025-03-06 · (carried, unchanged) Executive Order 14233 signed, establishing the Strategic Bitcoin Reserve + US Digital Asset Stockpile; contains no purchasing authorization, only permission to study acquisition mechanisms
  - as_of: 2025-04-05 (audit completed) / 2025-07-30 (report published) · new this run, cryptoimpacthub.com (fetched directly): the reserve's founding audit found "cold wallets stored in desk drawers across federal agencies," with "no unified custody standard, no consolidated inventory, and no consistent key-management practice"
  - as_of: late 2025 · new this run, cryptoimpacthub.com (fetched directly): a US Marshals Service-held custodian wallet was exploited, with losses stated as "more than $60 million" — cross-confirmed via WebSearch (insurancejournal.com, "US Marshals Are Investigating a Possible Digital-Asset Hack," 2026-01-29)
  - as_of: 2026-05-06 · (carried) White House digital-asset adviser Patrick Witt, at Consensus Miami: cited holdings of 328,372 BTC (~$25.4B)
  - as_of: undated, described by cryptoimpacthub.com as "mid-2026" · new this run: a separate, lower figure of ~198,000 BTC circulating for reserve holdings — cryptoimpacthub.com's own reconciliation: "the larger number counts everything the government has custody of, including seized assets still subject to proceedings that may be returned to victims. The smaller counts assets actually forfeited and therefore genuinely the government's" — i.e. a ~130,000 BTC (~$8B at cryptoimpacthub's cited price) gap explained as a custody-scope difference between the two figures, not a data error
  - as_of: 2026-07-06 · (carried, unchanged) Bloomberg/coindesk.com: reserve "remains unbuilt," Treasury's 60-day statutory evaluation report still undelivered ("more than a year past its deadline"), Treasury and Commerce both seeking to administer it, DOJ Office of Legal Counsel reviewing legal authority
  - as_of: 2026-09 (undated within this run, carried) · Unchained Crypto headline: "Sixteen months after Trump ordered a Strategic Bitcoin Reserve created, Treasury and Commerce are still fighting over who runs it" — describes holdings as "over 300,000 BTC, worth about $21 billion"
status: hold-only directive as of this run, no open-market accumulation found; Treasury Secretary Bessent quoted (via cryptoimpacthub.com): "We're not going to be buying that but are going to use confiscated assets" — consistent with prior runs' "won't be buying" reading. Treasury/Commerce turf war remains unresolved, no newer dated status update located this run beyond the still-fighting characterization. No statute underpins the reserve; it rests entirely on the executive order, per cryptoimpacthub.com. Legislative track unchanged: BITCOIN Act (S.954, Lummis, Senate Banking Committee) would mandate up to 1M BTC purchased over 5 years if enacted; ARMA Act of 2026 (H.R.8957, Begich/Golden, introduced 2026-05-21) was referred to the House Committee on Financial Services as of a June 2026 reading, no hearings scheduled and no September 2026 floor-vote information located this run — the bill proposes a 20-year minimum hold plus a study of budget-neutral acquisition strategies, per one search source explicitly noting it "drops the 1 million BTC target," consistent with streams.md's caution to treat specific BTC-amount targets from secondary crypto-media as unconfirmed.
conflict: cryptoimpacthub.com resolves what a prior run flagged as an unverified low-figure conflict (~198,000 BTC vs. ~328,372 BTC on file) by attributing it to a scope difference (gross custody vs. net-forfeited BTC) rather than a data error — recording both figures and the explanation rather than picking one as "the" holdings number
checked_absence: no announcement found of a resolution to the Treasury/Commerce administration dispute, and no news found of open-market BTC purchases, as of 2026-09-05; no active litigation against the SBR order found (see sbr-legal-durability)

### halving-timeline
source:  mempool.space API — https://mempool.space/api/blocks/tip/height (current block height, fetched directly, same-day) and https://mempool.space/api/v1/difficulty-adjustment (fetched directly, same-day)
window:  —
series:
  - as_of: 2026-09-05 · current block height 965,623 (mempool.space API, direct read, same-day); next halving at block height 1,050,000 (210,000-block interval, mechanical); 84,377 blocks remaining; current difficulty-epoch average block time 593,041 ms (~9.88 min/block) per the difficulty-adjustment endpoint (timeAvg field); current difficulty-epoch is 97.97% complete, 41 blocks to next retarget, with an expected +1.22% difficulty increase at that retarget; at the current ~9.88 min/block pace, 84,377 blocks ≈ ~579 days ≈ estimated early April 2028 (refines, and is broadly consistent with, the prior run's 2028-04-17 estimate); block reward will drop from 3.125 BTC to 1.5625 BTC at halving
status: no change in mechanics from prior run — the 210,000-block interval is exact, the calendar date is a projection that shifts with network hashrate/difficulty

### miner-behavior
source:  search-indexed CryptoQuant-attributed coverage (HTX Insights, AMBCrypto, cryptonews.net, coindesk.com, Galaxy Research via TradingView/Cointelegraph, coinpedia.org, ChinaTechNews.com, Pickaxe.io, shattered.io) — cryptoquant.com quicktake pages again returned HTTP 403 to a direct WebFetch attempt not repeated this run given the established pattern
window:  —
series:
  - as_of: 2026-07-16 · new this run, HTX Insights citing CryptoQuant: miner reserves at 1.1943M BTC (~$76.76B), a 1% increase with net inflow of 224+ BTC — read by the source as accumulation, miners "not yet distributing their holdings"; this is a more recent and directionally different reading than the prior run's most recent (2026-05-25) "miner reserves lowest level since two months ago" figure — flagged as a conflict, see below
  - as_of: 2026-08-01 · new this run, coindesk.com: mining difficulty down 14% from 2026's high as of Aug 1 ("plunging revenues force operators to pivot")
  - as_of: 2026-08-23 · new this run, multiple outlets (Yahoo Finance/KuCoin/shattered.io): difficulty at 125.81T, down 1.31% from the prior epoch and ~19.3-19.9% below the Oct 29, 2025 all-time-high of 155.97T — described as the second/third-deepest ASIC-era decline on record; hashprice quoted at ~$27.66/PH/s/day in late June, recovering to ~$38/PH/s/day by late August
  - as_of: Q1 2026 (carried context, re-confirmed this run) · Galaxy Research (via coinpedia.org, TradingView): publicly traded miners sold 32,000+ BTC in Q1 2026 alone (a single-quarter record exceeding all of 2025's combined sales); MARA sold 23,093 BTC and Riot sold 9,665 BTC in H1 2026; Galaxy Research (2026-06-21) characterized miners as in a "capitulation phase," operating on sub-5% margins
  - as_of: 2026-08 (undated more precisely) · news.bitcoin.com, citing CryptoQuant (carried from prior run): wallets with 100+ BTC (a whale-wallet metric, not the miner-labeled subset) added 60,000 BTC in August while smaller holders sold ~47,000 BTC combined — noted again as a distinct metric from miner reserves specifically
status: mixed/conflicting signals this run — a July 16 CryptoQuant-attributed reading shows miner reserves rising (+1%, accumulation), while difficulty continued falling through August (-19.3 to -19.9% from ATH) and Q1/H1 2026 data shows large public-miner selling; no single most-recent (September) miner-reserve print was located
conflict: the July 16, 2026 "+1% miner reserve increase / accumulation" reading (this run, via HTX/CryptoQuant) sits in tension with the May 25, 2026 "miner reserves lowest level since two months ago" reading carried from prior runs, and with the Q1/H1 2026 public-miner-selling data (32,000+ BTC sold) — these may reflect different miner cohorts (on-chain miner-labeled wallets vs. publicly traded mining companies) rather than a true contradiction, but no single reconciling source was found this run; flagging for the Reporter
checked_absence: no new large-scale miner-capitulation event (beyond the already-known Q1 2026 record-selling episode) found as of 2026-09-05

### legacy-whale-movements
source:  search-indexed coverage (Yahoo Finance, TheStreet Crypto, crypto.news, yellow.com, bitcoinsistemi.com, bitcoinfoundation.org, BingX, fxstreet.com) of on-chain dormant-supply/exchange-inflow tracking via Arkham/Galaxy Research/CryptoQuant
window:  —
series:
  - as_of: ~late Aug/early Sept 2026 ("approximately two weeks ago" per source, undated more precisely) · new this run, Yahoo Finance: a dormant Bitcoin wallet (11 years dormant) moved 1,214 BTC (~$86M) to new addresses with "no known exchange links"
  - as_of: undated within this run, new · BingX/Arkham data: a wallet dormant 7 years shifted 2,931 BTC (~$188M), market watching for potential selling — no destination/exchange confirmed in this result
  - as_of: undated within this run, new · yellow.com/bitcoinsistemi.com: separate reports of a 13-year-dormant wallet moving ~$85M and a 15-year-dormant wallet's coins "starting to move" — neither source in this run's results gave exact BTC counts or precise dates
  - as_of: 2026-08-04 · (carried, unchanged) CoinDesk: a wallet dormant since 2013 moved ~$31M, part of a wave of old-coin movements following a Coldcard hardware-wallet hack
  - as_of: 2026-07-16 · (carried, unchanged) 5,908 BTC address dormant since 2017 moved ~$383M to a new non-exchange wallet
  - as_of: 2026-08 (undated, carried) · news.bitcoin.com citing CryptoQuant: wallets with 100+ BTC added ~60,000 BTC over August while sub-100-BTC holders sold ~47,000 BTC combined
  - as_of: Q2 2026 (new context this run) · one search source (paraphrased, not directly quoted) states "sleeping Bitcoin" (legacy-coin) activity fell to its lowest level since Q3 2022 by Q2 2026 — a broader base-rate context distinct from the individual high-profile moves logged above; source did not name the specific tracker/dashboard, flagging as lower-confidence
status: same pattern as prior runs continues — isolated dormant-coin movements, mostly routed to non-exchange/new addresses (no clear seller-to-exchange pattern in this run's newly found moves), alongside the ongoing whale-accumulation reading (60,000 BTC/August, 100+ BTC cohort); no single unambiguous current-trend dashboard value obtained as of 2026-09-05
checked_absence: no large-scale coordinated dormant-supply-to-exchange event found as of 2026-09-05 beyond the individual movements logged above

### clarity-act
source:  predictionhunt.com (fetched directly — "Clarity Act Senate Odds Fall to 24% With 60-Vote Cloture Needed," 2026-09-02), defirate.com (fetched directly — "CLARITY Act Updates: Sept. 15 Senate Cloture Vote," reflecting Sept-5 reads of Polymarket/Kalshi), theblock.co (fetched directly — Thune cloture-filing article), search-indexed coverage (CCN, KuCoin, Yahoo Finance, cointribune.com, coinotag.com, americanbanker.com, thehill.com, cryptopotato.com)
window:  —
series:
  - as_of: 2026-08-08 · (carried) Senate Majority Leader Thune filed cloture on the motion to proceed to the CLARITY Act (H.R. 3633) before the August recess, setting up the Sept 15 vote; theblock.co (fetched directly, this run): "Invoking cloture would limit debate on the motion to proceed; it would not pass the bill or begin debate on the legislation itself"; 60 votes needed, Republicans hold 53 seats, so at least 7 Democrats/independents required
  - as_of: 2026-09-02 · new this run, predictionhunt.com (fetched directly): a Polymarket/Kalshi "Above 58" contract (i.e., odds that 59+ senators vote yes on the Sept 15 cloture motion) averaged 24% (Polymarket 26%, Kalshi 29%), down from 38% three days earlier; adjacent-threshold contracts on the same page: "Above 60" averaged 28% (Kalshi 27%, Polymarket 35%), "Above 50" averaged 30% (Kalshi 33%, Polymarket 37%), "Above 62" averaged 19% (Kalshi 20%, Polymarket 21%)
  - as_of: 2026-09-05, 07:03am ET · new this run, defirate.com (fetched directly): Polymarket's H.R. 3633-specific contract ("to be signed into law by Dec. 31, 2026") traded at 14-15% (14.5% midpoint), volume $13.988M
  - as_of: 2026-09-05, 02:56am ET · new this run, defirate.com (fetched directly): Kalshi's broader "crypto market-structure legislation to become law before Jan. 1, 2027" contract last traded 15%, bid/ask spread 15-16%, volume $1,384,005.64
  - as_of: 2026-09-05 (same defirate.com read) · new this run: Kalshi's separate near-term contract, "a Senate vote before Oct. 1, 2026," last traded 92% (this tracks whether a vote/debate occurs at all, not passage — resolves/refines prior run's "91%" figure)
  - as_of: 2026-09-02 (carried context) · Galaxy Research cut its odds of the CLARITY Act becoming law in 2026 from 50% to 30% "last month" (per theblock.co's Aug-8 article) — one search result this run states Galaxy's estimate was later cut further to 10%, not independently re-confirmed at a primary source this run
  - as_of: 2026-09-02 (carried, unchanged) · House leadership canceled the chamber's last two weeks of September; House will be out of session by Sept 17, two days after the Senate's scheduled Sept 15 cloture vote
next_release: cloture vote on the motion to proceed, 2026-09-15, 2:15pm ET (confirmed independently by theblock.co, predictionhunt.com, and defirate.com this run — consistent across sources); 60 votes needed
conflict: this run's direct fetches resolve some of the prior run's ambiguity by separating the CLARITY odds into three distinct question types rather than treating them as one number: (1) the Sept-15-cloture-specific "Above 58"-style contracts, ~24% as of Sept 2 (down from 38% three days prior); (2) full-passage/signed-into-law-by-year-end contracts, 14-16% as of Sept 5 (Polymarket 14-15%, Kalshi 15-16%); (3) a "will a vote happen at all" contract, 92% as of Sept 5. These are not the same question and should not be averaged or swapped for one another — the streams.md note's "~13-14%, stable" figure corresponds to category (2), not the cloture-specific (1) figure, which sits meaningfully higher (~24%) and has been falling faster (-14pts in 3 days as of Sept 2)

### stablecoin-regulation
source:  no new primary fetch this run beyond confirming via search that no material update has occurred since the prior run's direct reads of home.treasury.gov and federalregister.gov; cross-checked via WebSearch (theblock.co, morganlewis.com, occ.gov, tax.thomsonreuters.com, Wikipedia)
window:  —
series:
  - as_of: 2026-08-17 · (carried, unchanged) Treasury press release (home.treasury.gov/news/press-releases/sb0605): NPRM implementing GENIUS Act Section 3, governing who may issue/offer/sell payment stablecoins to US persons; docket TREAS-DO-2026-0496
  - as_of: 2026-08-18 · (carried, unchanged) rule published in the Federal Register as "GENIUS Act Regulations on Payment Stablecoin Issuance, Offer, and Sale"
status: implementation in progress, unchanged from prior run — issuers must hold a federal/state license to issue payment stablecoins in the US beginning 2027-01-18; starting 2028-07-18, only licensed issuers' stablecoins may be sold to US persons by digital asset service providers. No restrictive/adversarial turn found this run.
next_release: public comment period on the Section 3 NPRM closes 2026-10-19 (unchanged, confirmed again via search this run)
checked_absence: no new stablecoin-regulation event found beyond the on-file August 2026 NPRM as of 2026-09-05

### sec-cftc-posture
source:  no new primary fetch this run beyond confirming via search that no material update has occurred since the prior run's direct read of sec.gov; cross-checked via WebSearch (sec.gov press releases, Sidley Austin, cryptoninjas.net, fxstreet.com)
window:  —
series:
  - as_of: 2026-03 · (carried, unchanged) SEC Chair Atkins and CFTC Chair Selig signed an inter-agency MOU ("Project Crypto"); SEC issued interpretation 33-11412
  - as_of: 2026-05-29 · (carried, unchanged) CFTC issued releases approving/guiding crypto-asset perpetual futures contracts
  - as_of: 2026-08-18 · (carried, unchanged) SEC press release 2026-76: "Regulation Crypto Assets" proposed (file S7-2026-27); a $5M/4-year "startup exemption," a $75M/12-month "fundraising exemption," a conditional safe harbor around the "investment contract" definition, state-securities-law preemption; Atkins statement (2026-08-18, sec.gov, confirmed via search this run) frames the proposal as the SEC's "most historic step yet" toward making the US the "Crypto Capital of the World"
status: posture continues to read as accommodation/coordination, unchanged direction from prior run — no hostile-turn events found this run
next_release: public comment period on Regulation Crypto Assets (S7-2026-27) closes 2026-10-20 (unchanged, confirmed again via search this run)
checked_absence: no new enforcement crackdown or adversarial rulemaking found as of 2026-09-05

### sbr-legal-durability
source:  cryptoimpacthub.com (fetched directly, same source used for strategic-bitcoin-reserve this run), cross-checked via WebSearch (Lexology, cryptowisser.com, coinpedia.org, atlas21.com, news.bitcoin.com)
window:  —
series:
  - as_of: 2025-03-06 · (carried) Executive Order 14233 signed
  - as_of: 2025-04-05/2025-07-30 · new this run (see strategic-bitcoin-reserve, same source): founding audit found "cold wallets stored in desk drawers across federal agencies," no unified custody standard — a custody/operational-durability finding, not litigation
  - as_of: late 2025 · new this run: US Marshals Service custodian wallet exploit, losses "more than $60 million" — an operational-security durability issue, not litigation
  - as_of: 2026-07-06 · (carried, unchanged) Treasury and Commerce both seeking to administer the reserve; Treasury officials questioning their own legal authority to oversee the SBR; DOJ Office of Legal Counsel reviewing; Treasury's statutory 60-day evaluation report still undelivered, over a year past deadline
  - as_of: 2026-09-05 (this run's search) · cryptoimpacthub.com (fetched directly): "the whole structure sits on an executive order with no statute underneath it" — explicit statement that no statute currently underpins the reserve
status: as of this run, no court case/lawsuit was found directly challenging Executive Order 14233 or the SBR itself, unchanged from prior run — legal-durability risk in current coverage remains (a) an intra-executive-branch authority dispute (Treasury vs. Commerce, pending DOJ OLC review), (b) the absence of any statute underlying the order, and (c) operational/custody durability findings (desk-drawer key storage, the $60M+ Marshals-wallet exploit) rather than litigation
checked_absence: no new court filing directly challenging the SBR executive order found as of 2026-09-05
