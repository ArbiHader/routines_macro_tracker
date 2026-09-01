# macro-monetary readings — run 2026-09-01
fetcher: macro-monetary

### fed-funds-path
source:  CME FedWatch Tool (cmegroup.com, direct fetch blocked by egress proxy — values below via search-indexed secondary reporting of the CME tool: investing.com Fed Rate Monitor, KuCoin News, Forbes) + Polymarket "Fed Decision in September?" contract
series:
  - as_of: 2026-08-25 · CME FedWatch: 58.6% probability Fed holds at the Sept 16, 2026 meeting (implying ~41.4% probability of a move, direction not specified in this reading)
  - as_of: 2026-08-28 · CME FedWatch: 57% probability of a 25bp hike at the Sept 16, 2026 meeting (cited as "after the Jackson Hole speech")
  - as_of: 2026-08-29/31 · CME FedWatch: 66% probability of a 25bp hike at the Sept 16, 2026 meeting (Forbes, "CME FedWatch Provides A 66% Chance Fed Will Hike Rates In September")
  - as_of: 2026-09-01 · Polymarket "Fed Decision in September?" market: 66% priced on "No change" (hold)
  - as_of: undated (cited in a KuCoin News piece, exact date unclear) · Polymarket priced 53% odds of a Fed rate hike in September 2026, vs. 32% in futures markets — flagged as a separate reading, date not independently confirmed
next_release: 2026-09-16, 2:00 p.m. ET (FOMC rate decision, Sept 15–16, 2026 meeting)
conflict: CME FedWatch (66% hike, as of Aug 29–31) and Polymarket's "Fed Decision in September?" contract (66% no-change/hold, as of Sept 1) point in opposite directions as of essentially the same window. Could not resolve directly at cmegroup.com (blocked by egress proxy) or polymarket.com (not independently re-verified beyond search-indexed summary). Recorded both readings as found; the Reporter should treat the CME-vs-Polymarket divergence as an open question, not resolved here.
notes:   Direct access to cmegroup.com was blocked by the network egress proxy this run; all CME FedWatch figures above are as reported by secondary financial-news sources, not read directly off the tool.

### fomc-tone
source:  federalreserve.gov (direct fetch of individual statement/minutes pages was blocked by the network egress proxy this run — content below is reconstructed from search-indexed excerpts/quotes of the primary statements and minutes, via CNBC, Federal Reserve Board press-release search snippets, and other outlets citing the statements directly; verbatim full-statement text could not be retrieved this run) · vote composition and dissenters recorded where found
series:
  - as_of: 2025-12-10 (Dec 9-10, 2025 meeting, pre-Warsh/Powell era) · Fed cut rates; 3 dissents; Committee projected one cut in 2026 (Bloomberg headline/summary, not verbatim statement text)
  - as_of: 2026-01-28 · Held federal funds rate at 3-1/2 to 3-3/4 percent. Vote 10-2. Dissenters: Stephen I. Miran and Christopher J. Waller, both preferring to lower the target range by 1/4 percentage point (Miran's fourth consecutive dissent). Assessment language cited: "economic activity has been expanding at a solid pace," "job gains have remained low," "inflation remains somewhat elevated."
  - as_of: 2026-03-18 · Held federal funds rate at 3.50%–3.75%. Vote 11-1. Dissenter: Governor Stephen Miran, preferring a 25bp cut. Assessment language cited: growth described as "solid," inflation described as "somewhat elevated." Powell press conference: emphasized data dependence, said to take forecasts "with a grain of salt."
  - as_of: 2026-04-29 · Held federal funds rate at 3.5–3.75 percent. Vote 8-4 — the most dissents since October 1992. Dissenters: Governor Stephen Miran (preferred a 25bp cut) and regional presidents Beth Hammack (Cleveland), Neel Kashkari (Minneapolis), Lorie Logan (Dallas) (this trio supported holding the range but opposed inclusion of an easing bias in the statement).
  - as_of: 2026-05-22 · Not a scheduled FOMC statement — Kevin Warsh took the oath of office as Fed Chairman and was unanimously selected as FOMC chairman by the Committee this date (chair transition from Powell). Confirmed by Senate 54-45 (narrowest confirmation vote for the position in US history) on 2026-05-13.
  - as_of: 2026-06-17 · Held federal funds rate at 3-1/2 to 3-3/4 percent (Warsh's first meeting as chair). Vote 12-0, unanimous — no dissents (contrast to April's 8-4). Warsh characterized the statement as "a bit shorter, a bit simpler, and it dispenses with some older language."
  - as_of: 2026-07-29 · Held federal funds rate at 3-1/2 to 3-3/4 percent. Vote 9-3. Dissenters: Beth Hammack (Cleveland), Neel Kashkari (Minneapolis), Lorie Logan (Dallas) — all three preferred to raise the target range by 1/4 percentage point at this meeting. Cited language: "Economic activity is expanding at a solid pace despite elevated uncertainty that owes, in part, to the conflict in the Middle East. Productivity growth and capital investment are strong. Job gains have kept pace with the workforce, and the unemployment rate has changed little." Inflation described as "elevated relative to the Committee's 2 percent goal." Minutes (released 2026-08-19) reported: officials saw the need for a rate hike if inflation doesn't cool; minutes also recorded an "extensive discussion of the Fed's balance sheet and its various bond holdings," and discussion of reducing the meeting cadence from eight to six per year (Warsh's suggestion).
  - as_of: 2026-08-28 · Not an FOMC statement — Chairman Warsh's Jackson Hole keynote remarks. Verbatim quote obtained: "The Fed's price-stability objective of 2 percent, as measured by the personal consumption expenditures (PCE) price index, is a firm, fixed target." Coverage characterized the speech as warning inflation may require rate hikes and as providing "little guidance on rates" otherwise (secondary characterizations, flagged as such — not verbatim).
next_release: 2026-09-16 (FOMC statement, Sept 15-16, 2026 meeting) — minutes typically follow ~3 weeks later
notes:   Only 8 of the requested "last 12 releases" were located this run (Dec 2025 through Aug 2026 Jackson Hole remarks); federalreserve.gov direct access was blocked, so entries above rely on secondary reporting of primary statement text rather than the verbatim source document itself — flagged per the "never a secondary characterization" standard. Full verbatim statement/minutes text should be re-attempted next run if direct federalreserve.gov access becomes available.

### fed-balance-sheet
source:  Federal Reserve H.4.1 release (federalreserve.gov/releases/h41/ — direct fetch blocked by egress proxy; figures below via search-indexed secondary reporting of the H.4.1 series, e.g. macroradar.io, bizstats-dashboard.com, and search-result summaries of the Fed's own release)
series:
  - as_of: 2026-08-06 · H.4.1 release (weekly, Thursday 4:30pm) — release exists per federalreserve.gov release-dates index; specific total-assets figure for this date not independently retrieved
  - as_of: 2026-08-13 · H.4.1 release — release exists per federalreserve.gov release-dates index; specific figure not independently retrieved
  - as_of: 2026-08-20 · H.4.1 release — release exists per federalreserve.gov release-dates index; specific figure not independently retrieved
  - as_of: 2026-08-26/27 · Total assets: $6.73 trillion, per H.4.1 release dated 2026-08-27 (covering data through 2026-08-26) — down 25-27% from the $8.97 trillion April 2022 record (two secondary sources gave 25% and 27% for the same comparison; both cited, unreconciled)
status:  QT (quantitative tightening) ended December 2025, per secondary reporting (only about half of pandemic-era balance-sheet growth had been reversed by that point). As of this run there is no confirmed QE or fresh QT announcement; some officials, including Chair Warsh, are reported (secondary sourcing) to be discussing a further balance-sheet reduction, with commentary suggesting "groundwork is being laid to potentially restart a gradual process of QT as soon as later next year" — this is analyst/press characterization, not a Fed announcement, and is recorded as such.
next_release: weekly, Thursday 4:30pm ET — next release expected 2026-09-03 (per the Thursday cadence; not independently confirmed against the federalreserve.gov release calendar this run since direct access was blocked)
conflict: two secondary sources gave different percentage declines (25% vs. 27%) from the same 2022 peak to the same 2026-08-26 level ($6.73T) — the underlying dollar figures are consistent, only the stated percentage differs; noting for the Reporter, not resolving.
notes:   federalreserve.gov/releases/h41/ was blocked by the network egress proxy this run; total-assets figures are as reported by secondary aggregators of the H.4.1 series rather than read directly off the release.

### global-m2
source:  MacroMicro "World - Major Central Bank M2 Money Supply" series (aggregated Fed + ECB + BOJ + PBOC), en.macromicro.me/series/4675
series:
  - as_of: 2026-03 (March 2026) · combined M2 of the four major central banks: 100,742.27 billion (currency/units not stated in source snippet — flagged, needs unit confirmation)
  - as_of: 2026-06 (June 2026) · combined M2: two figures cited by the same source in different search snippets — 102,663.81 billion and 102,622 billion / 102,578 billion (three slightly different figures for the same or adjacent months surfaced across search results; not reconciled)
  - as_of: 2026-07 (July 2026) · no combined-four-bank figure located; only the US-only M2 component was found for this month (see below)
conflict: multiple slightly different June 2026 combined-M2 figures surfaced (102,663.81B, 102,622B, 102,578B) from the same MacroMicro series across different search-result snippets — could not access the live MacroMicro chart directly to reconcile (not attempted via WebFetch this run); recorded as found.
notes:   Supplementary US-only data point: US M2 (FRED M2SL) was $23.2 trillion in July 2026 (a series record high, per secondary reporting of FRED, since fred.stlouisfed.org was blocked by the egress proxy this run), up from ~$23.1 trillion in June 2026; YoY growth cited variously as 4.9% and 5.4% in different secondary sources (unreconciled). This is the US component only, not the full aggregated global-M2 series the stream calls for — recorded as a supplementary data point.

### real-yields
source:  FRED DFII10 (10-year TIPS real yield) — fred.stlouisfed.org was blocked by the network egress proxy this run; values below are as reported by secondary trackers of the same FRED series (convextrade.com, advisorperspectives.com/dshort search snippet, gurufocus.com, tradingeconomics.com)
series:
  - as_of: 2026-07 (July 2026, monthly average) · 2.31% (GuruFocus, citing FRED monthly series)
  - as_of: 2026-08-20 · 2.35% (convextrade.com, "10-Year Real Yield (TIPS) Today")
  - as_of: 2026-08-27 · 2.34% (cited via an Advisor Perspectives "Treasury Yields Snapshot: August 28, 2026" search-result summary; direct page fetch was blocked by the egress proxy)
  - as_of: 2026-08 (August 2026, monthly, exact date unclear) · 2.41% (TradingEconomics)
conflict: four secondary sources give a range of 2.31%–2.41% for late July/August 2026, not fully reconcilable to daily closes without direct FRED access (fred.stlouisfed.org blocked this run). Could not obtain the requested 5 individual daily closes from the primary source; recorded the closest available secondary data points instead and flagged the source-substitution explicitly per protocol.
notes:   Primary source (FRED) was unreachable via WebFetch this run (egress-blocked); this is a secondary-source substitution, flagged as required.

### treasury-issuance
source:  U.S. Department of the Treasury — quarterly refunding statements and buyback press releases (home.treasury.gov)
status:  Q3 2026 quarterly refunding announcement (Aug 2026): Treasury offered $125 billion of securities to refund ~$96.3 billion of privately-held notes/bonds maturing 2026-08-15 (3-year auctioned 2026-08-11, 10-year auctioned 2026-08-12, 30-year auctioned 2026-08-13). Buyback program: initially the refunding announcement said buybacks would continue at the same size, but ~2 weeks later Treasury announced it is increasing the size of liquidity-support buyback operations for longer-dated nominal coupon securities (10y–20y and 20y–30y sectors), raising the per-operation cap from $2 billion to at least $4 billion, effective 2026-09-09, running through the end of the refunding quarter (2026-11-04).
change log:
  - 2026-08 (specific date within refunding announcement, not independently pinned) · initial refunding announcement: buybacks unchanged in size
  - 2026-08-19 (per Bloomberg headline "US Treasury's Expanded Bond Buybacks Complicate Short-Term Bill Supply") · Treasury signaled expansion of buyback operations
  - press release sb0607 (home.treasury.gov) · formal announcement of the doubled ($2B → $4B) long-end liquidity-support buyback size, effective 2026-09-09
next_release: next quarterly refunding announcement 2026-11-02 (Q4 2026); Treasury's quarterly refunding press conference is typically the first Wednesday of Feb/May/Aug/Nov
notes:   —

### cpi
source:  BLS CPI News Release (bls.gov/news.release/cpi.htm)
series:
  - as_of: 2026-05 (May 2026, released 2026-06-10) · headline CPI +0.5% m/m, +4.2% y/y (largest 12-month increase since April 2023's 4.9%); core CPI (ex food & energy) +0.2% m/m, +2.9% y/y; energy +23.5% y/y (up from +17.9% y/y through April 2026)
  - as_of: 2026-06 (June 2026, released ~2026-07-14) · headline CPI annual rate 3.5% (first decline in five months, down from 4.2% in May); core CPI figure cited in one secondary source as easing to 2.5% y/y — this conflicts with the May print's reported 2.9% core y/y implying a large one-month drop; flagged as unreconciled, see conflict note. Energy costs +15.7% y/y in June, down from +23.5% in May, attributed by the source to the US-Iran ceasefire.
  - as_of: 2026-07 (July 2026, released ~2026-08-13) · headline CPI +0.1% m/m, +3.4% y/y (continuing a downward trend from the 3.8% April 2026 peak); core CPI +0.2% m/m, +2.5% y/y. Matched Dow Jones consensus across all four metrics per this source.
conflict: June 2026 core CPI y/y was reported in one search result as easing "to 2.5% from 2.6% in the previous month" — but the primary May 2026 release itself states core CPI was 2.9% y/y. A drop from 2.9% (May) to 2.5%-2.6% (June) in one month is a large, currently unverified move; could not independently confirm the June core figure against bls.gov directly this run (site was reachable for search-indexed content but not independently re-verified via WebFetch). Flagging for the Reporter — do not treat the June core CPI figure as confirmed without further check.
next_release: 2026-09-11, 8:30 a.m. ET (August 2026 CPI)
notes:   —

### core-pce
source:  BEA Personal Income and Outlays release (bea.gov/news/2026/personal-income-and-outlays-<month>-2026)
series:
  - as_of: 2026-05 (May 2026) · core PCE (ex food & energy) y/y: 3.4%, per BEA
  - as_of: 2026-06 (June 2026) · core PCE y/y: 3.3%, per BEA (a 0.1pp decline from May's 3.4%). One secondary source separately reported "Core PCE inflation rises 2.8% in June" — this conflicts with the 3.3% figure sourced closer to the BEA release; flagged, not reconciled (see conflict note). Headline PCE price index -0.1% m/m (per a separate secondary summary); consumer spending +0.3% m/m.
  - as_of: 2026-07 (July 2026) · core PCE y/y: 3.3% (unchanged from June per this reading — note this conflicts with the June 3.3%/2.8% ambiguity above). Personal income +$115.1B (+0.4% m/m); disposable personal income +$125.9B (+0.5%); PCE (spending) +$36.3B (+0.2% m/m); personal saving rate 3.0%; real PCE +$1.3B (<0.1% m/m).
conflict: June 2026 core PCE y/y was reported as both 3.3% (BEA-adjacent sourcing) and 2.8% (a Seeking Alpha headline, "Core PCE Inflation Rises 2.8% In June, Higher Than Expected") — a 0.5pp discrepancy for the same month. Per this stream's own note ("verify forecast-vs-actual against a source that states the numbers explicitly before overwriting a prior reading"), this was not resolved this run; recommend the Reporter treat June core PCE as unconfirmed between 2.8% and 3.3% pending a direct bea.gov check (bea.gov itself was not blocked for search-indexed content, but a direct verifying fetch was not completed this run).
next_release: 2026-09-30, 8:30 a.m. EDT (August 2026 Personal Income and Outlays)
notes:   —

### labor-market
source:  BLS Employment Situation release (bls.gov/news.release/empsit.htm)
series:
  - as_of: 2026-06 (June 2026, released 2026-07-02) · nonfarm payrolls +57,000 (vs. ~115,000 expected); unemployment rate 4.2%. Downward revisions: April revised down 31,000 to +148,000; May revised down 43,000 to +129,000 (two-month combined revision: -74,000). Average hourly earnings +$0.13 (+0.3% m/m) to $37.64; +3.5% y/y.
  - as_of: 2026-07 (July 2026, released ~2026-08-01) · nonfarm payrolls -23,000 (a decline); unemployment rate 4.1% (down 10bp from June's 4.19%). Sector detail: gains in health & social assistance (+22,600), construction (+22,000), professional/business services (+14,600); declines in government (-53,000), leisure & hospitality (-40,000), retail trade (-19,400). Labor force participation rate 61.4%; employment-population ratio 58.9% (both little changed).
  - as_of: 2026-08 (August 2026) · not yet released as of this run
next_release: 2026-09-04, 8:30 a.m. ET (August 2026 Employment Situation)
notes:   Only 2 of the requested 3 monthly prints were available; the August 2026 report is scheduled for 2026-09-04, three days after this run.

### ism-pmi
source:  ISM Manufacturing PMI / Services PMI reports via PR Newswire (prnewswire.com) — the primary ISM/PR Newswire release, per the stream's instruction to avoid secondary characterization
series (Manufacturing):
  - as_of: 2026-05 (May 2026) · Manufacturing PMI 54.0% (expansion)
  - as_of: 2026-06 (June 2026) · Manufacturing PMI 53.3% (expansion)
  - as_of: 2026-07 (July 2026) · Manufacturing PMI 55.6% (expansion) — 2.3 points above June, highest reading since May 2022, 7th consecutive month of expansion
  - as_of: 2026-08 (August 2026) · scheduled for release today, 2026-09-01, 10:00 a.m. ET — not yet available in search results as of this fetch; no current value found as of 2026-09-01
series (Services, supplementary — same fetch spec covers "ISM Manufacturing / Services PMI"):
  - as_of: 2026-07 (July 2026) · Services PMI 54.1% (expansion, 25th consecutive month); Business Activity Index 59.1 (+3.7pp from June's 55.4); New Orders Index 57.2 (+2.1pp from June's 55.1); Employment Index fell back into contraction at 47.4 (-3.8pp)
next_release: Manufacturing PMI for August 2026 — 2026-09-01, 10:00 a.m. ET (today; not yet published at fetch time)
notes:   The August 2026 Manufacturing PMI print was scheduled to publish today at 10:00 a.m. ET, the same day as this run — recorded as "no current value found as of 2026-09-01" per protocol rather than guessed. Re-check next run.

### gdp
source:  BEA GDP release (bea.gov/news/2026/gdp-...)
series:
  - as_of: 2026-Q1 (third estimate, released 2026-06-25) · real GDP +2.1% annualized (revised up from the 2.0% advance estimate and further revised up 0.5pp from the second estimate, primarily reflecting a downward revision to imports)
  - as_of: 2026-Q2 (second estimate, released 2026-08-26) · real GDP +1.5% annualized (same as the advance estimate). Contributors: increases in consumer spending, exports, investment, partly offset by a decrease in government spending; imports increased (a subtraction to GDP). Price index for gross domestic purchases +5.7% (vs. +3.6% in Q1); PCE price index +5.1% (vs. +4.6% in Q1); core PCE price index (ex food & energy) +3.4% (vs. +4.4% in Q1) — note this GDP-report core-PCE print differs from the standalone core-PCE release figures recorded under the core-pce stream; not reconciled here (different release, different vintage).
next_release: BEA Q3 2026 advance GDP estimate — exact date not confirmed this run; typically ~4 weeks after quarter-end, so expected late October 2026 (not independently verified against the BEA release calendar since bea.gov's schedule page was not directly re-fetched)
notes:   —

### consumer-sentiment
source:  University of Michigan Surveys of Consumers (data.sca.isr.umich.edu) + The Conference Board Consumer Confidence Index (conference-board.org)
series (UMich):
  - as_of: 2026-08 (August 2026, final, released 2026-08-28) · Index of Consumer Sentiment 51.7 (revised up from a preliminary 51.0), a 6.3% decrease from July. Current Economic Conditions Index 51.9 (-5.3%); Consumer Expectations Index 51.5 (-7.0%). One-year business expectations -10%; five-year outlook -13%. One-year inflation expectations 4.0% (down from 4.2%); long-run (5-year) inflation expectations 3.3%, steady for a third straight month.
series (Conference Board):
  - as_of: 2026-07 (July 2026) · Consumer Confidence Index 90.2
  - as_of: 2026-08 (August 2026) · Consumer Confidence Index 89.4 (-0.8 pts, weakest since January, a seven-month low). Present Situation Index 121.2 (+6.8 pts, after three straight monthly declines). Expectations Index 68.2 (-5.8 pts) — below the 80 threshold the Conference Board associates with recession risk within a year. One-year-ahead household inflation expectations 5.8% (up from 5.6% the prior month). Cited driver context: elevated mentions of prices/energy costs, armed conflict, geopolitical tensions, food costs, trade issues, employment concerns.
next_release: UMich preliminary September 2026 reading — 2026-09-11 (per search-indexed schedule; not independently re-verified against umich.edu's release calendar via direct fetch)
notes:   Only 2 UMich monthly prints (Aug final + implicitly July as the prior-month comparison, not independently pulled as a standalone print) and 2 Conference Board prints were located, short of the requested "last 3 monthly prints" for both. Recommend a follow-up search next run for the July 2026 UMich standalone figure and June 2026 Conference Board figure to complete the series.
