# macro-monetary readings — run 2026-09-05
fetcher: macro-monetary

### fed-funds-path
source:  Polymarket "Fed Decision in September?" (direct fetch of polymarket.com/event/fed-decision-in-september-762) + CME FedWatch (cmegroup.com direct fetch returned HTTP 503 again this run — figures below via search-indexed secondary reporting, CNBC/Forbes/techtimes/defirate.com)
series:
  - as_of: 2026-09-05 · Polymarket "Fed Decision in September?" (direct read): 25bp increase 50% · No change 49% · 50+bp increase <1% · 25bp decrease <1% · 50+bp decrease <1%
  - as_of: 2026-09-05 (post-August-jobs-report) · secondary-reported prediction-market odds (defirate.com roundup, not independently distinguished from Polymarket): No change 56.9% · 25bp increase 42.1% — this figure conflicts with the same-day direct Polymarket read above (49%/50%)
  - as_of: 2026-09-03 (pre-jobs-report) · CME FedWatch: ~65-68% hike odds (carried forward from last run, techtimes.com/Forbes secondary reporting) — CME FedWatch itself not re-confirmed this run (cmegroup.com 503)
  - as_of: 2026-08-31 · CME FedWatch: 66% probability of a 25bp hike at the Sept 16, 2026 meeting (Forbes) — carried forward, unchanged
next_release: 2026-09-16, 2:00 p.m. ET (FOMC rate decision, Sept 15-16, 2026 meeting)
conflict: new this run — two same-day (2026-09-05) readings disagree on the current split: a direct Polymarket fetch gives 50% hike / 49% hold, while a secondary-reported "prediction markets" figure (defirate.com, citing post-jobs-report movement) gives 42.1% hike / 56.9% hold. Both are dated to the period just after the strong Aug jobs report (payrolls +162,000 vs. ~53,000 consensus, released 2026-09-04) but the secondary figure may reflect an earlier snapshot before further movement, or a different market/methodology (not clearly labeled as Polymarket vs. a futures-implied calc) — not reconciled this run. Separately, CME FedWatch remains unreachable via direct fetch for a second consecutive run (503); the on-file 65-68%/66% figures predate the Sept 4 jobs report and have not been re-verified against it.
notes:   The Aug 29 (Fri, Sept 4) jobs report — payrolls +162,000, well above the ~53,000 consensus, unemployment steady at 4.1% — is a new, potentially odds-moving data point since last run's 2026-09-03 reading; both odds series above are dated after that release, but the CME figure carried forward is not.

### fomc-tone
source:  federalreserve.gov press-release index (federalreserve.gov/newsevents/pressreleases/2026-press.htm) — checked this run for any new FOMC statement or Warsh remarks between 2026-08-28 and 2026-09-05; direct fetch succeeded
series:
  - as_of: 2026-07-29 · VERBATIM (carried forward unchanged from last run, direct-fetched last run from monetary20260729a.htm): "The Committee decided to maintain the target range for the federal funds rate at 3-1/2 to 3-3/4 percent, in support of the Federal Reserve's dual mandate." Vote: approved 9-3. Dissenters: Beth M. Hammack, Neel Kashkari, and Lorie K. Logan, all preferring to raise the federal funds rate by 1/4 percentage point.
  - as_of: 2026-08-28 · VERBATIM (carried forward unchanged from last run, direct-fetched last run from warsh20260828a.htm, Jackson Hole keynote) — key passages already on file: "The Fed's price-stability objective of 2 percent, as measured by the personal consumption expenditures (PCE) price index, is a firm, fixed target." / "Inflation is running above our 2 percent target. So the Fed's predominant focus right now should be on prices." / "I stand here today committed to a discipline, not to a decision."
  - as_of: 2026-09-04 · new this run, not a monetary-policy item: "Federal Reserve Board announces termination of enforcement actions with United Texas Bank, Quontic Bank Acquisition Corp., and Quontic Bank Holdings Corp." (enforcement20260904a.htm) — a supervisory/enforcement release, not FOMC statement or Chair remarks; included for completeness but out of scope for tone-tracking.
next_release: 2026-09-16 (FOMC statement, Sept 15-16, 2026 meeting) — minutes typically follow ~3 weeks later. No new FOMC statement or Warsh public remarks located between 2026-08-28 and 2026-09-05.
notes:   No change to the tone series this run — the July 29 statement and Aug 28 Jackson Hole speech remain the most recent monetary-policy communications on file. The remaining 10 of the requested 12 statements (June 2025-June 2026) remain carried forward from prior runs, sourced secondarily, not re-verified this run.

### fed-balance-sheet
source:  Federal Reserve H.4.1 release (federalreserve.gov/releases/h41/current/) — direct fetch succeeded this run
series:
  - as_of: 2026-09-03 (release date, covering the week ended 2026-09-02) · Total assets: $6,737,204 million (~$6.74 trillion), up $6,292 million from the prior week
  - as_of: 2026-08-27 (prior release, covering week through 2026-08-26) · Total assets: $6,730,912 million — carried forward from last run
status:  This run's reading shows a small weekly increase (+$6.3B), the first up-week on file after a prior down-week (-$14.8B) — consistent with, and does not resolve, the carried-forward QT-stop-date discrepancy (Oct 2025 vs. Dec 2025 across secondary sources; not re-investigated this run). No new Fed announcement on balance-sheet policy located this run.
next_release: weekly, Thursday 4:30 p.m. ET — next release 2026-09-10 (covering the week through 2026-09-09)
conflict: carried forward, unresolved from prior runs — (1) two secondary sources disagree on the percentage decline from the 2022 peak (25% vs. 27%); (2) the QT-stop date discrepancy (Oct 2025 vs. Dec 2025). Neither re-investigated this run.
notes:   The week-over-week direction flipped from a decline (last run) to a small increase (this run) — recorded plainly as a level change; whether this reflects a shift in stance or routine weekly noise is not established by this reading alone.

### global-m2
source:  MacroMicro "World - Major Central Bank M2 Money Supply" series (en.macromicro.me/series/4675) — no new combined-M2 print located this run; direct MacroMicro fetch not attempted (search-indexed secondary reporting only)
series:
  - as_of: 2026-03 (March 2026) · combined 4-bank M2: 100,742.27 billion (unit not confirmed) — unchanged from last run
  - as_of: 2026-06 (June 2026) · combined 4-bank M2: 102,663.81 billion — unchanged from last run, still the most recent figure located
  - as_of: 2026-07 (July 2026) · no combined-level figure located this run, but a related metric appeared: M2 growth rate for major central banks (YoY) reported at 4.67% for July 2026 (MacroMicro, via search) — this is a growth-rate reading, not a comparable level to the "combined 4-bank M2" series above; do not merge the two without reconciling units.
  - as_of: 2026-08 (August 2026) · not located this run — search results explicitly note August 2026 data is not yet publicly available as of this run (2026-09-05)
conflict: none new this run.
notes:   Still short of the requested "last 3 monthly prints" as directly comparable levels — March and June 2026 remain the only levels on file; July's new figure is a YoY growth rate, not a level, so it does not close the gap. US-only M2 supplementary data (FRED M2SL) not re-fetched this run; last on-file figure ($23.22T, July 2026, +5.4% y/y) carried forward unverified.

### real-yields
source:  FRED CSV — https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10&cosd=2026-08-22 — direct fetch succeeded this run
window:  daily close, no rolling window
series:
  - as_of: 2026-09-03 · 2.42%
  - as_of: 2026-09-02 · 2.45%
  - as_of: 2026-09-01 · 2.44%
  - as_of: 2026-08-31 · 2.44%
  - as_of: 2026-08-28 · 2.42%
  - as_of: 2026-08-27 · 2.34%
  - as_of: 2026-08-26 · 2.34%
  - as_of: 2026-08-25 · 2.32%
  - as_of: 2026-08-24 · 2.38%
conflict: none — this run's pull extends and confirms last run's series (2026-08-24 through 2026-09-01 unchanged) and adds two new closes (2026-09-02: 2.45%, 2026-09-03: 2.42%). No 2026-09-04 close available yet in this pull.
notes:   Primary source (FRED) reachable via direct fetch this run, as last run.

### treasury-issuance
source:  U.S. Department of the Treasury press release sb0607 (home.treasury.gov/news/press-releases/sb0607) — content confirmed via search-indexed secondary reporting (Yahoo Finance) this run; direct fetch of the specific announcement document not attempted this run
status:  Unchanged from last run — Treasury's increase in long-end (10y-20y and 20y-30y sector) liquidity-support buyback operation caps from $2 billion to at least $4 billion per operation remains effective 2026-09-09 through 2026-11-04 (end of the current refunding quarter). No further change located since sb0607 as of this run (2026-09-05).
change log:
  - 2026-08-19 · Treasury press release sb0607: formal announcement of the doubled ($2B to $4B) long-end liquidity-support buyback size, effective 2026-09-09 through 2026-11-04 — unchanged, carried forward
next_release: next quarterly refunding announcement/press conference 2026-11-04 (Q4 2026) — unchanged from last run
notes:   No new information located this run beyond what was already on file; not independently re-verified via direct fetch of the sb0607 document itself.

### govt-shutdown
source:  wire coverage (Al Jazeera, NBC News, Military Times, Federal News Network, NPR, Defense One) — confirmed via search this run; consistent with, and does not change, last run's whitehouse.gov-sourced signature confirmation
series:
  - as_of: 2026-09-02 · unchanged from last run — H.R. 6500, the "Continuing Appropriations and Extensions Act, 2027," was signed into law, funding federal agencies through 2026-12-11. Passed Senate 90-6, House 370-48. No new legislative action located this run.
next_release: n/a (status stream) — next decision point remains 2026-12-11, when the CR expires; per prior reporting (not re-verified this run), only 2 of 12 FY2027 appropriations bills had passed the House and none the Senate.
conflict: none — this run's search confirms last run's status without contradiction.
notes:   No status change since last run; funding remains in place through Dec 11, 2026.

### cpi
source:  BLS CPI News Release (bls.gov/news.release/cpi.nr0.htm) — not re-fetched this run; no new release due until 2026-09-11
series:
  - as_of: 2026-05 (May 2026) · headline CPI +0.5% m/m, +4.2% y/y; core CPI +0.2% m/m, +2.9% y/y — carried forward, unchanged
  - as_of: 2026-06 (June 2026) · headline CPI 3.5% y/y; core CPI figure disputed (2.5% vs. 2.9% y/y) — carried forward, unresolved
  - as_of: 2026-07 (July 2026, released 2026-08-12) · headline CPI +0.1% m/m, +3.4% y/y; core CPI +0.2% m/m, +2.5% y/y — carried forward, unchanged
conflict: carried forward, unresolved — June 2026 core CPI y/y remains disputed between 2.5% and 2.9%; not re-investigated this run.
next_release: 2026-09-11, 8:30 a.m. ET (August 2026 CPI) — unchanged from last run, not yet released as of this run
notes:   No new print this run; August 2026 CPI due 2026-09-11 (six days after this run).

### core-pce
source:  BEA Personal Income and Outlays release (bea.gov/news/2026/personal-income-and-outlays-july-2026) — not re-fetched this run; no new release due until 2026-09-30
series:
  - as_of: 2026-05 (May 2026) · core PCE (ex food & energy) y/y: 3.4% — carried forward, unchanged
  - as_of: 2026-06 (June 2026) · core PCE y/y: 3.3% — carried forward, unchanged
  - as_of: 2026-07 (July 2026) · core PCE: +0.2% m/m, +3.3% y/y; headline PCE: +0.2% m/m, +3.7% y/y — carried forward, unchanged (this figure was corrected last run from an earlier erroneous 0.1% m/m reading; correction stands)
next_release: 2026-09-30, 8:30 a.m. ET (August 2026 Personal Income and Outlays) — unchanged from last run
notes:   No new print this run; August 2026 reading due 2026-09-30.

### labor-market
source:  BLS Employment Situation release (bls.gov/news.release/empsit.nr0.htm) — direct fetch succeeded this run; August 2026 report released as scheduled 2026-09-04, confirmed independently via CNBC
series:
  - as_of: 2026-06 (June 2026) · nonfarm payrolls revised up this run from +57,000 to +31,000 per the August report's stated revision ("June... revised upward by 11,000, from +20,000 to +31,000") — this run's direct-fetch language for the June revision base (+20,000) does not match last run's on-file June headline (+57,000); flagging as an unreconciled discrepancy in the June baseline figure itself, separate from the revision amount.
  - as_of: 2026-07 (July 2026) · nonfarm payrolls revised up this run from -23,000 to +21,000 ("revised up by 44,000, from -23,000 to +21,000" per the August release, corroborated independently by CNBC); unemployment rate 4.1% (unchanged, carried forward). This resolves last run's on-file July figure (-23,000) as now-superseded by BLS's own revision.
  - as_of: 2026-08 (August 2026, released 2026-09-04) · nonfarm payrolls +162,000 (vs. ~53,000 consensus per CNBC); unemployment rate unchanged at 4.1%. Sector detail (direct fetch, verbatim): food services and drinking places +59,000; local government education +42,000; information industry -23,000; manufacturing +16,000; health care +13,000 (slower than prior 12-month average).
next_release: 2026-10-02 (approx., September 2026 Employment Situation) — exact date not confirmed this run
conflict: (1) new this run — the June 2026 payrolls baseline used in the August release's revision language (+20,000, revised to +31,000) does not match the +57,000 June figure that has been on file since at least two runs ago; not reconciled. (2) last run's July figure (-23,000) is now directly superseded by BLS's own subsequent revision to +21,000 — recorded as a revision, not a conflict between sources.
notes:   All three requested monthly prints (June, July, August) are now on file. The August reading is a large upside surprise vs. consensus (+162,000 vs. ~+53,000) and follows an upward revision to July (from -23,000 to +21,000) and June (baseline discrepancy noted above).

### ism-pmi
source:  ISM Manufacturing PMI report via PR Newswire (prnewswire.com/news-releases/manufacturing-pmi-at-54-6-august-2026-ism-manufacturing-pmi-report-302865127.html) and ISM Services PMI report via PR Newswire (prnewswire.com/news-releases/services-pmi-at-55-4-august-2026-ism-services-pmi-report-302868046.html) — direct fetch of the Services release succeeded this run (via WebFetch); Manufacturing release content via search-indexed secondary reporting (Textile World, TD Economics, Vantage Markets) citing the same PR Newswire release
series (Manufacturing):
  - as_of: 2026-07 (July 2026) · Manufacturing PMI 55.6% (expansion) — carried forward, unchanged
  - as_of: 2026-08 (August 2026, released 2026-09-02) · Manufacturing PMI 54.6% (expansion, 8th consecutive month; overall economy in expansion for the 22nd month running), down 1.0pp from July. Sub-indices: New Orders 53.7% (-3.0pp); Backlog of Orders 51.8% (-3.2pp); Production 58.3% (-0.2pp); Employment 51.2% (-1.6pp from 52.8%, still expansion). Chair: Susan Spence.
series (Services):
  - as_of: 2026-07 (July 2026) · Services PMI 54.1% (expansion, 25th consecutive month) — carried forward, unchanged
  - as_of: 2026-08 (August 2026, released 2026-09-03) · Services PMI 55.4% (expansion, 26th consecutive month), up 1.3pp from July's 54.1%. Sub-indices (VERBATIM table, direct fetch): Business Activity 61.7% (+2.6); New Orders 60.9% (+3.7); Employment 47.8% (contraction, 2nd consecutive month, +0.4 vs. July's 47.4%); Supplier Deliveries 51.3% (-1.5); Inventories 56.7% (+5.3); Prices 72.6% (+2.3, "above 70 percent for the fifth time in six months"); Backlog of Orders 55.6% (+4.7); New Export Orders 56.3% (+4.3); Imports 56.3% (+4.5); Inventory Sentiment 54.1% (+1.6). Chair Steve Miller (verbatim): "The Services PMI® registered 55.4 percent, an increase of 1.3 percentage points compared to July's figure of 54.1 percent." / "The Employment Index contracted for a second straight month with a reading of 47.8 percent."
next_release: ISM Manufacturing and Services PMI (September 2026 data) — expected ~2026-10-01 to 10-03 (not independently confirmed this run)
notes:   August prints for both Manufacturing and Services are now fully on file with sub-index detail; this fills the "last 3 monthly prints" gap for Services (July, August on file — June still missing) and partially for Manufacturing (July, August on file — June still missing).

### gdp
source:  BEA GDP release (bea.gov/data/gdp/gross-domestic-product) — direct fetch succeeded this run; no new print since last run
series:
  - as_of: 2026-Q1 (third estimate, released 2026-06-25) · real GDP +2.1% annualized — carried forward, unchanged
  - as_of: 2026-Q2 (second estimate, released 2026-08-26) · real GDP +1.5% annualized (VERBATIM: "Real gross domestic product (GDP) increased at an annual rate of 1.5 percent in the second quarter of 2026") — carried forward, unchanged, re-confirmed via direct fetch this run
next_release: BEA Q3 2026 advance GDP estimate — 2026-10-29, 8:30 a.m. ET, per last run's search-confirmed figure. Note: this run's direct bea.gov fetch again returned "2026-09-30" as a "next release date" field on the page — as flagged last run, that date belongs to the Personal Income and Outlays (PCE) release, not GDP; treating 2026-10-29 as correct per last run's independent search confirmation (not re-verified via search this run).
conflict: carried forward — the bea.gov page's own "next release" field continues to show a value (2026-09-30) that appears to belong to a different release series; not a genuine external-source conflict, flagged for transparency.
notes:   No change to GDP figures this run.

### consumer-sentiment
source:  University of Michigan Surveys of Consumers (data.sca.isr.umich.edu) + The Conference Board Consumer Confidence Index (conference-board.org) — no new prints since last run; neither site independently direct-fetched this run; next-release-date conflict from last run narrowed via search
series (UMich — unchanged from last run):
  - as_of: 2026-08 (August 2026, final, released 2026-08-28) · Index of Consumer Sentiment 51.7 (revised up from a preliminary 51.0)
series (Conference Board — unchanged from last run):
  - as_of: 2026-07 (July 2026) · Consumer Confidence Index 90.2
  - as_of: 2026-08 (August 2026) · Consumer Confidence Index 89.4
next_release: UMich preliminary September 2026 reading — this run's search converges on 2026-09-11, 10:00 a.m. ET, resolving last run's two-way conflict (2026-09-11 vs. 2026-09-25) in favor of the earlier date, though not via a direct fetch of data.sca.isr.umich.edu. Conference Board Consumer Confidence, September 2026 — 2026-09-29, 10:00 a.m. ET, unchanged from last run.
conflict: RESOLVED (partially) — last run's UMich next-release-date conflict (09-11 vs. 09-25) now shows a single, consistently repeated date (09-11) in this run's search results; not confirmed via direct primary fetch, so treat as narrowed rather than fully verified.
notes:   Only 1 UMich monthly print and 2 Conference Board prints remain on file, short of the requested "last 3 monthly prints" for both — unchanged gap from last run. Next UMich preliminary print (2026-09-11) will also be the first new data point since 2026-08-28.
