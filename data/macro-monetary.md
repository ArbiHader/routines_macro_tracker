# macro-monetary readings — run 2026-09-03
fetcher: macro-monetary

### fed-funds-path
source:  Polymarket "Fed Decision in September?" — direct fetch of polymarket.com/event/fed-decision-in-september-762 succeeded this run (prior runs were blocked); CME FedWatch (cmegroup.com) direct fetch returned HTTP 503 this run — CME figures below are via search-indexed secondary reporting (KuCoin, news.bitcoin.com, Forbes, techtimes.com)
series:
  - as_of: 2026-09-03 · Polymarket "Fed Decision in September?" (direct read): No change 59% · 25bp increase 42% · 50+bp increase <1% (0.6%) · 25bp decrease <1% (0.5%) · 50+bp decrease <1% (0.2%)
  - as_of: 2026-08-28 (post-Jackson-Hole) · CME FedWatch: 57% probability of a 25bp hike at the Sept 16, 2026 meeting (KuCoin/news.bitcoin.com headline, "Fedwatch Turns Hawkish With 57% Odds of September Rate Increase")
  - as_of: 2026-08-31 · CME FedWatch: 66% probability of a 25bp hike at the Sept 16, 2026 meeting (Forbes, "CME FedWatch Provides A 66% Chance Fed Will Hike Rates In September")
  - as_of: 2026-09-01 · CME FedWatch: ~65-68% hike odds reported ("as of the open Tuesday"), hold probability ~43% cited separately in the same secondary roundup — the hike and hold figures as reported do not sum cleanly to 100%, unreconciled (techtimes.com)
next_release: 2026-09-16, 2:00 p.m. ET (FOMC rate decision, Sept 15-16, 2026 meeting)
conflict: (1) RESOLVED this run for Polymarket specifically — a direct fetch of the named contract (no longer blocked) gives one clean, internally consistent reading: 59% no-change / 42% 25bp-hike / <1% each other outcome, as of 2026-09-03. This supersedes last run's three irreconcilable Polymarket figures (59% hike / 58.5% no-change / 66% no-change) as the current state. (2) CME FedWatch remains a live conflict — direct cmegroup.com fetch failed (503) again this run, and secondary reports continue to disagree with each other on the exact hike probability (57% Aug 28, 66% Aug 31, ~65-68% Sept 1, with an accompanying "43% hold" figure that doesn't reconcile against a ~65-68% hike figure). The overall picture: post-Jackson-Hole CME sourcing shows hike odds trending up into the high 50s/60s%, while Polymarket (now directly confirmed) sits lower, at 42% hike / 59% hold — CME and Polymarket disagree on the current split, not just on the trend.
notes:   Polymarket direct fetch succeeded this run (egress proxy did not block it, unlike the prior two runs). CME FedWatch (cmegroup.com) remains unreachable via direct fetch.

### fomc-tone
source:  federalreserve.gov — direct fetch succeeded this run for two specific documents: the July 29, 2026 FOMC statement (federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm) and Chairman Warsh's Aug 28, 2026 Jackson Hole keynote (federalreserve.gov/newsevents/speech/warsh20260828a.htm), both retrieved verbatim in full. No new FOMC statement exists since last run (no meeting between July 29 and the upcoming Sept 15-16 meeting); prior 10 statements (June 2025-June 2026) not re-fetched this run, carried forward from last run's file (sourced there via secondary reporting, not verbatim).
series:
  - as_of: 2026-07-29 · VERBATIM (direct fetch, upgrading last run's secondary-sourced entry): "The Committee decided to maintain the target range for the federal funds rate at 3-1/2 to 3-3/4 percent, in support of the Federal Reserve's dual mandate." Vote: approved 9-3. Dissenters: Beth M. Hammack, Neel Kashkari, and Lorie K. Logan, all preferring to raise the federal funds rate by 1/4 percentage point. Assessment: economic expansion proceeding "at a solid rate" despite Middle East-related uncertainty, "strong productivity growth and capital investment," employment gains matching workforce growth, unemployment relatively stable; inflation "remains elevated relative to the Committee's 2 percent goal," partly attributed to supply-driven price increases in sectors like energy. Reserves: "The Committee is continuing its policy of maintaining ample reserves in the banking system."
  - as_of: 2026-08-28 · VERBATIM (direct fetch, full text obtained — Chairman Warsh's Jackson Hole keynote, "Preparing for Future Policy Conjunctures / Forward Guidance and Its Stand-ins / Key Principles / The Economy Today"). Selected verbatim passages: "The Fed's price-stability objective of 2 percent, as measured by the personal consumption expenditures (PCE) price index, is a firm, fixed target." / "I am impressed by the overall performance of the economy, which appears to have strengthened." / "The Fed's preferred measure of inflation, the 12-month change in the PCE price index, stands at 3.7 percent, while the six-month change is 4.1 percent... Inflation is running above our 2 percent target. So the Fed's predominant focus right now should be on prices." / "And while this summer's PCE and CPI readings were better than expected, they do not tell me that underlying trends have meaningfully improved." / On disaggregation: "Over the past 12 months, 54 percent of goods and services in the PCE basket showed price increases above 3 percent... Looking over just the past six months... 49 percent showed annualized price increases above 3 percent." / "We must be confident that underlying inflation is moving to our objective, clearly and at sufficient speed. Otherwise, we have work to do." / On forward guidance: "I stand here today committed to a discipline, not to a decision." / On communications: "a quieter Fed, more purposeful in its communications, is better able to meet its objectives." / July minutes reference (paraphrased within the speech, not verbatim minutes text): "the unanimous view of the FOMC: Labor markets were stable, and output was solid. But inflation remained too high." / Labor market: "The jobless rate, at 4.1 percent, remains low by historical standards." / Financial conditions: "I would be hard pressed to describe broad financial conditions as restrictive." This is a full-text verbatim upgrade of last run's partial/secondary-sourced quotes for the same speech.
next_release: 2026-09-16 (FOMC statement, Sept 15-16, 2026 meeting) — minutes typically follow ~3 weeks later. No Warsh public remarks located between Aug 28 (Jackson Hole) and this run (2026-09-03).
notes:   This run upgraded two of the twelve on-file entries (July 29 statement, Aug 28 speech) from secondary-sourced to full verbatim primary text via direct federalreserve.gov fetch — the proxy did not block these two specific URLs this run. The remaining 10 statements (June 2025 - June 2026) are carried forward unchanged from last run's file and remain secondary-sourced; re-verify verbatim if federalreserve.gov access holds up in a future run. No new FOMC statement or Warsh remarks since Aug 28 as of this run.

### fed-balance-sheet
source:  Federal Reserve H.4.1 release (federalreserve.gov/releases/h41/current/) — direct fetch succeeded this run
series:
  - as_of: 2026-08-27 (release date, covering data through 2026-08-26) · Total assets: $6,730,912 million (~$6.73 trillion), down $14,787 million from the prior week (this run's direct-fetch figure matches last run's figure of ~$6.73T / "down $15 billion," now confirmed via direct primary fetch rather than secondary reporting)
status:  QT (balance-sheet runoff) reported stopped per last run's secondary sourcing (unreconciled date: Oct 2025 vs. Dec 2025 across sources — not re-investigated this run). No new Fed announcement on balance-sheet policy located this run beyond what is already on file (the Dec 2025 $40B/month T-bill purchase program through April 15, 2026, and analyst characterization of Chair Warsh's intent to shrink the balance sheet again from Q4 2026 at the earliest).
next_release: weekly, Thursday 4:30 p.m. ET — the next release is today, 2026-09-03 (covering the week through 2026-09-02), not yet posted as of this run (fetched earlier in the day, before the 4:30pm ET release time)
conflict: carried forward, unresolved — (1) two secondary sources cited last run gave different percentage declines (25% vs. 27%) from the 2022 peak; not re-investigated this run. (2) the QT-stop date discrepancy (Oct 2025 vs. Dec 2025) also carried forward, not re-investigated this run.
notes:   Direct fetch of federalreserve.gov/releases/h41/current/ succeeded this run, confirming last run's secondary-sourced total-assets figure exactly — no revision needed to the level itself.

### global-m2
source:  MacroMicro "World - Major Central Bank M2 Money Supply" series (en.macromicro.me/series/4675) — no new combined-M2 print located this run; direct MacroMicro fetch not attempted (not in this run's batch)
series:
  - as_of: 2026-03 (March 2026) · combined 4-bank M2: 100,742.27 billion (unit not confirmed) — unchanged from last run
  - as_of: 2026-06 (June 2026) · combined 4-bank M2: 102,663.81 billion — the figure most consistently repeated across secondary sources this run (the other June variants from last run, 102,622B / 102,578B, did not reappear in this run's search results)
  - as_of: 2026-07/08 (July/August 2026) · no combined 4-bank figure located this run either — MacroMicro's most recent available figure remains June 2026; search results explicitly note September 2026 data is not yet available and MacroMicro "typically updates their data around the end of each month"
conflict: last run's three-way June 2026 conflict (102,663.81B / 102,622B / 102,578B) narrowed this run to a single figure (102,663.81B) appearing consistently — treating that as the more supported reading, though not confirmed via a direct MacroMicro fetch this run.
notes:   Still short of the requested "last 3 monthly prints" — only March and June 2026 are on file, an unfilled gap that has persisted across runs. US-only M2 supplementary data (FRED M2SL) not re-fetched this run; last run's figure ($23.22T, July 2026, +5.4% y/y) carried forward unverified.

### real-yields
source:  FRED CSV — https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10&cosd=2026-08-20 — direct fetch succeeded this run (unlike the prior two runs, which were egress-blocked)
window:  daily close, no rolling window
series:
  - as_of: 2026-09-01 · 2.44%
  - as_of: 2026-08-31 · 2.44%
  - as_of: 2026-08-28 · 2.42%
  - as_of: 2026-08-27 · 2.34%
  - as_of: 2026-08-26 · 2.34%
  - as_of: 2026-08-25 · 2.32%
  - as_of: 2026-08-24 · 2.38%
  - as_of: 2026-08-21 · 2.40%
  - as_of: 2026-08-20 · 2.35%
conflict: RESOLVED this run — direct primary fetch confirms the Aug 27/Aug 28 values from last run's secondary sourcing (2.34% and 2.42% respectively) exactly, and extends the series two more days to 2.44% (Aug 31 and Sept 1, both unchanged day-over-day). No 2026-09-02 close available yet in this pull (likely not yet posted, or a holiday — Sept 2 is the day after Labor Day; TIPS market may have had abbreviated activity).
notes:   Primary source (FRED) reachable via direct WebFetch this run for the first time in three runs — full 5+ daily-close depth now satisfied without secondary substitution.

### treasury-issuance
source:  U.S. Department of the Treasury press release sb0607 (home.treasury.gov/news/press-releases/sb0607) — content below via search-indexed secondary reporting (Yahoo Finance, CNBC, babypips.com, unusualwhales.com); direct fetch of the Treasury quarterly-refunding overview page succeeded but did not surface the specific announcement document
status:  Q3 2026 quarterly refunding (Aug 2026): Treasury offered $125 billion of securities to refund ~$96.3 billion of privately-held notes/bonds maturing 2026-08-15. Separately, Treasury press release sb0607 (2026-08-19) announced an increase in the size of liquidity-support buyback operations for longer-dated nominal coupon securities (the 10y-20y and 20y-30y sectors), raising the per-operation cap from $2 billion to at least $4 billion — this run adds a confirmed end date: effective 2026-09-09, remaining in effect through 2026-11-04 (i.e., through the end of the current refunding quarter, consistent with last run's "through end of the refunding quarter" language, now dated explicitly). No further change located since sb0607 as of this run (2026-09-03).
change log:
  - 2026-08 (specific date within refunding announcement, not independently pinned) · initial refunding announcement: buybacks unchanged in size
  - 2026-08-19 · Treasury press release sb0607: formal announcement of the doubled ($2B to $4B) long-end liquidity-support buyback size, effective 2026-09-09 through 2026-11-04
next_release: next quarterly refunding announcement/press conference 2026-11-04 (Q4 2026) — unchanged from last run, and now also confirmed as the buyback-size window's end date, consistent with the two events coinciding
notes:   Direct fetch of home.treasury.gov's quarterly-refunding overview page succeeded this run but returned only a navigational description, not the underlying announcement document — content above still relies on secondary reporting of sb0607.

### govt-shutdown
source:  whitehouse.gov ("Congressional Bill H.R. 6500 Signed into Law" briefing) + wire coverage (Fox News, NPR, The Hill, Washington Post, iHeart) — confirmed via search this run; whitehouse.gov briefing page not independently direct-fetched
series:
  - as_of: 2026-09-02 · President signed H.R. 6500, the "Continuing Appropriations and Extensions Act, 2027," into law — confirmed directly via a White House briefing-statements page (whitehouse.gov) plus independent wire corroboration (Fox News, NPR, The Hill, Washington Post, iHeart), resolving last run's "awaiting signature" status. The bill provides a short-term continuing resolution funding federal agencies through 2026-12-11, and separately extends authorities for surface transportation and veterans' programs. Passed Senate 90-6, House 370-48 (unchanged from last run's figures, now with the signature confirmed).
next_release: n/a (status stream) — next decision point is 2026-12-11, when the CR expires; only 2 of 12 FY2027 appropriations bills have passed the House and none the Senate as of this run, per last run's reporting (not re-verified this run)
conflict: none — this run's finding (signed 2026-09-02) is consistent with and confirms last run's "awaiting signature" note, not a contradiction.
notes:   Status updated from "awaiting signature" (last run) to "signed into law" (this run). The Oct 1 FY2027 cliff remains defused through Dec 11, 2026; the Dec 11 date is the next tracking point, unchanged from last run's assessment.

### cpi
source:  BLS CPI News Release (bls.gov/news.release/cpi.nr0.htm) — direct fetch succeeded this run
series:
  - as_of: 2026-05 (May 2026, released 2026-06-10) · headline CPI +0.5% m/m, +4.2% y/y; core CPI +0.2% m/m, +2.9% y/y — carried forward from last run, not re-fetched this run
  - as_of: 2026-06 (June 2026, released ~2026-07-14) · headline CPI 3.5% y/y; core CPI figure disputed (2.5% vs. 2.9% y/y) — carried forward from last run, unresolved, not re-investigated this run
  - as_of: 2026-07 (July 2026, released 2026-08-12) · headline CPI +0.1% m/m, +3.4% y/y ("increased 0.1 percent on a seasonally adjusted basis in July after falling 0.4 percent in June" — verbatim from direct fetch); core CPI +0.2% m/m, +2.5% y/y. This run's direct fetch confirms last run's figures exactly and adds the exact release date (Aug 12, 2026, correcting last run's "~2026-08-13" approximation) and the verbatim m/m context quote.
conflict: carried forward, unresolved — June 2026 core CPI y/y remains disputed between 2.5% (one secondary source) and 2.9% (implied by the May release's own stated y/y figure); not re-investigated this run.
next_release: 2026-09-11, 8:30 a.m. ET (August 2026 CPI) — confirmed again via direct fetch, unchanged from last run
notes:   August 2026 CPI not yet released as of this run (due 2026-09-11).

### core-pce
source:  BEA Personal Income and Outlays release (bea.gov/news/2026/personal-income-and-outlays-july-2026) — direct fetch succeeded this run
series:
  - as_of: 2026-05 (May 2026) · core PCE (ex food & energy) y/y: 3.4% — carried forward from last run, not re-fetched this run
  - as_of: 2026-06 (June 2026) · core PCE y/y: 3.3% — carried forward from last run (resolved in that run), not re-fetched this run
  - as_of: 2026-07 (July 2026) · core PCE: +0.2% m/m, +3.3% y/y (VERBATIM, direct fetch: "increased 0.2 percent" m/m, "increased 3.3 percent" y/y). Headline PCE price index: +0.2% m/m, +3.7% y/y (verbatim: "increased 0.2 percent" m/m, "increased 3.7 percent" y/y).
conflict: RESOLVED this run — last run recorded July 2026 core PCE as +0.1% m/m ("below the 0.2% forecast cited by one source"). This run's direct primary fetch of bea.gov states unambiguously "increased 0.2 percent" m/m for core PCE, matching consensus exactly (also corroborated independently by a Yahoo Finance search summary: "core in line," "landed exactly where analysts had expected"). Last run's 0.1% m/m figure was incorrect — treat 0.2% m/m as the correct, primary-confirmed July reading; the y/y figure (3.3%) was already correct and is unchanged.
next_release: 2026-09-30, 8:30 a.m. ET (August 2026 Personal Income and Outlays) — unchanged from last run
notes:   Per the stream's standing instruction to verify forecast-vs-actual against a source stating the numbers explicitly before overwriting a prior reading — this run's direct bea.gov fetch is exactly that verification, and it corrects last run's on-file m/m figure.

### labor-market
source:  BLS Employment Situation release (bls.gov/news.release/empsit.nr0.htm) — direct fetch succeeded this run; August 2026 report not yet released as of this run
series:
  - as_of: 2026-06 (June 2026, released 2026-07-02) · nonfarm payrolls +57,000; unemployment rate 4.2% — carried forward from last run, not re-fetched this run
  - as_of: 2026-07 (July 2026) · nonfarm payrolls -23,000; unemployment rate 4.1% ("little change from prior month"). This run's direct fetch confirms last run's figures but gives a release date of 2026-08-07, which conflicts with last run's "~2026-08-01" approximation — flagging as a minor, unresolved release-date discrepancy (the payroll/unemployment figures themselves are not in dispute). Sector detail from direct fetch: declines concentrated in local government education (-50,000) and retail trade (-19,000); health care added 22,000 — this is a partially different breakdown from last run's on-file sector detail (which cited government -53,000, leisure & hospitality -40,000, retail -19,400, construction +22,000, professional/business services +14,600) — the two sourcings do not fully agree on sector-level detail beyond retail trade's decline, unreconciled.
  - as_of: 2026-08 (August 2026) · not yet released as of this run (2026-09-03, due tomorrow 2026-09-04)
next_release: 2026-09-04, 8:30 a.m. ET (August 2026 Employment Situation)
conflict: (1) July 2026 release-date discrepancy: 2026-08-07 (this run, direct fetch) vs. ~2026-08-01 (last run). (2) July 2026 sector-level breakdown differs between this run's direct fetch and last run's on-file detail beyond the retail-trade figure — not reconciled.
notes:   Only 2 of the requested 3 monthly prints remain on file (August due tomorrow). Headline payroll/unemployment figures for June and July are not in dispute; only release date and sector detail for July show discrepancies this run.

### ism-pmi
source:  ISM Services PMI report via PR Newswire (prnewswire.com/news-releases/services-pmi-at-55-4-august-2026-ism-services-pmi-report-302868046.html) — direct fetch of prnewswire.com not attempted this run; figures below via search corroborated across multiple outlets independently citing the same release (TTNews, cryptobriefing.com, ISM Chair Steve Miller quote). Manufacturing PMI not re-fetched this run (no new print due until ~Oct 1, 2026 for September data).
series (Manufacturing — carried forward, unchanged from last run):
  - as_of: 2026-07 (July 2026) · Manufacturing PMI 55.6% (expansion)
  - as_of: 2026-08 (August 2026, released 2026-09-01) · Manufacturing PMI 54.6% (expansion, 8th consecutive month), vs. 55.2% consensus
series (Services):
  - as_of: 2026-07 (July 2026) · Services PMI 54.1% (expansion, 25th consecutive month) — carried forward from last run
  - as_of: 2026-08 (August 2026, released 2026-09-03, i.e. today) · Services PMI 55.4% (expansion, 26th consecutive month), up 1.3pp from July's 54.1%, vs. ~54.3% consensus. Business Activity Index 61.7% (+2.6pp from July's 59.1%); New Orders Index 60.9% (+3.7pp from July's 57.2%); Employment Index 47.8% (contraction, 2nd consecutive month, essentially flat vs. July's 47.4%); Prices Index at a "mid-2022 high" (exact figure not located this run). ISM Chair Steve Miller quote (per secondary reporting, flagged as such): the August Services PMI "corresponds to a 2.3-percentage point increase in real GDP on an annualized basis."
next_release: ISM Manufacturing PMI (September 2026 data) — expected ~2026-10-01. ISM Services PMI (September 2026 data) — expected ~2026-10-01 to 10-03 (not independently confirmed this run).
notes:   Services PMI for August 2026 (released today, 2026-09-03) is now on file, resolving last run's "not yet available" entry — this fills the "last 3 monthly prints" gap only partially (July and August on file; June not re-located this run). Direct prnewswire.com fetch not attempted this run; figures remain corroborated secondary reporting per the stream's standard.

### gdp
source:  BEA GDP release (bea.gov/data/gdp/gross-domestic-product) — direct fetch succeeded this run for the current print; release-schedule detail via search
series:
  - as_of: 2026-Q1 (third estimate, released 2026-06-25) · real GDP +2.1% annualized — carried forward from last run, not re-fetched this run
  - as_of: 2026-Q2 (second estimate, released 2026-08-26) · real GDP +1.5% annualized (VERBATIM, direct fetch: "Real gross domestic product (GDP) increased at an annual rate of 1.5 percent in the second quarter of 2026"). Growth attributed to increases in consumer spending, exports, and investment, partly offset by decreased government spending — matches last run's figures exactly, now confirmed via direct fetch. Price-index detail (gross domestic purchases, PCE, core PCE deflators) not re-fetched this run — carried forward from last run.
next_release: BEA Q3 2026 advance GDP estimate — 2026-10-29, 8:30 a.m. ET (confirmed via search this run, matching last run's figure). Note: this run's direct bea.gov fetch initially returned "2026-09-30" as the "next release date," which is incorrect — that date is the next Personal Income and Outlays (PCE) release, not GDP; the page appears to have conflated the two release schedules. Corrected via independent search confirmation to 2026-10-29.
conflict: this run's own direct-fetch tool surfaced a wrong next-release date (2026-09-30, which belongs to the PCE release) before search correction to 2026-10-29 — flagging the direct-fetch tool's own error for transparency, not a genuine external-source conflict.
notes:   —

### consumer-sentiment
source:  University of Michigan Surveys of Consumers (data.sca.isr.umich.edu) + The Conference Board Consumer Confidence Index (conference-board.org) — no new prints since last run; neither site independently direct-fetched this run
series (UMich — unchanged from last run):
  - as_of: 2026-08 (August 2026, final, released 2026-08-28) · Index of Consumer Sentiment 51.7 (revised up from a preliminary 51.0)
series (Conference Board — unchanged from last run):
  - as_of: 2026-07 (July 2026) · Consumer Confidence Index 90.2
  - as_of: 2026-08 (August 2026) · Consumer Confidence Index 89.4
next_release: UMich preliminary September 2026 reading — conflicting dates found this run: one search result states 2026-09-11 (matching last run's figure), another states 2026-09-25, within the same search summary — unreconciled, flagging both. Conference Board Consumer Confidence, September 2026 — 2026-09-29, 10:00 a.m. ET, unchanged from last run.
conflict: new this run — UMich's own preliminary-September release date is reported inconsistently (2026-09-11 vs. 2026-09-25) even within a single search result set; could not resolve via direct fetch of data.sca.isr.umich.edu this run (not attempted in this run's batch).
notes:   Only 1 UMich monthly print and 2 Conference Board prints remain on file, short of the requested "last 3 monthly prints" for both — unchanged gap from last run.
