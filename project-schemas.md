# Project Schemas

The three file shapes that are the contract between pipeline stages. Structure is in
`project/context/architecture.md`; the decisions behind these are D-6…D-11. Two invariants hold across
all of them: the **fact layer** (`streams.md`, `data/*`) never carries assumptions (D-9), and text
observations are stored **verbatim, never summarized** (D-7).

---

## 1. `streams.md` — the stream catalog

Curator writes; Fetcher + Reporter read. One entry per **active** stream (retired ones move to
`archive.md`). The entry is the stream's stable definition — *what* it is, *how* it is read, *how* it is
fetched. It carries no live value (that lives in `data/*`). **Five fields** (D-11):

```
### <id>: <name>
category:  macro-monetary | cross-asset | crypto-structural | crypto-flows-onchain | geopolitical | idiosyncratic
impact:    BTC price | BTC price (fast path) | BTC price (feedback) | <another stream id>
polarity:  <shape>: <why this stream moves its impact target, and which reading is bullish/bearish>
fetch:     source: <primary source + url hint> · depth: <N + cadence | status phrase> · type: numeric | text | status
notes:     <optional durable per-stream correction>
```

- **`category`** routes the stream to one of the six Fetcher instances — its only job.
- **`impact`** is the causal backbone: which stream (or BTC) this feeds. Its tags carry what separate
  fields used to: `(fast path)` = a fast Tier-0 shock; `(feedback)` = reflexive, an amplifier only,
  never predictive. The hop-count ("Steps") is computed from the chain, not stored.
- **`polarity`** is one plain-word sentence carrying both the **transmission** (why the edge to `impact`
  exists — writing it *is* the inclusion test: no statable rule, no stream, D-6) and the **resolved
  direction**. It opens with a **shape**, one of: `single-direction` · `time-phased-pivot` ·
  `scope-to-impact` · `amplifier` · `conditional` · `background-probability` · `self-fulfilling` ·
  `contrarian`. Forcing one shape is what forbids an unresolved bullish-and-bearish reading. Scoped to
  the `impact` target; directions compose along the chain to BTC.
- **`fetch.depth`** is the series knob: `1` for latest-only, `N + cadence` for a series (what lets the
  Reporter read trend), or a phrase for a status stream.
- **`notes`** holds durable per-stream corrections (Mt. Gox soft-deadline, ISM primary-source, …).

**Examples** — each shows a different shape + payload type; real starter entries:

```
### labor-market: US labor market (jobs, unemployment)
category:  macro-monetary
impact:    fed-funds-path
polarity:  scope-to-impact: employment is half the Fed's mandate, so weaker jobs push it toward a cut (this row's only channel), and a cut is bullish — so weaker jobs is bullish; the "cooling economy" reading is a separate channel, not scored here
fetch:     source: BLS Employment Situation release (bls.gov) · depth: last 3 monthly prints (payrolls + unemployment rate) · type: numeric
notes:     scope to the Fed channel to keep the direction single — once left as an unresolved "helps or hurts"

### dxy: US dollar index (DXY)
category:  cross-asset
impact:    BTC price
polarity:  single-direction: a weaker dollar loosens financial conditions and lifts dollar-priced risk assets, so a falling dollar is bullish
fetch:     source: ICE DXY via a primary market-data source · depth: last 5 daily closes · type: numeric
notes:     —

### mt-gox: Mt. Gox distribution overhang
category:  crypto-structural
impact:    BTC price
polarity:  time-phased-pivot: creditor coins reaching the market are direct sell-side supply, so it is bearish while the payout runs; turns bullish once complete — soft, since the deadline has slipped twice
fetch:     source: Arkham on-chain wallet balance via The Block · depth: current + change log · type: status
notes:     the ~34,504 BTC figure is a direct wallet balance, not a subtraction; treat Oct 31 as soft (two prior extensions)

### russia-nato: Russia–NATO tension
category:  geopolitical
impact:    BTC price (fast path)
polarity:  background-probability: a deliberately ambiguous incident against a NATO member would raise Article-5 questions and hit risk assets fast, so no incident is bullish and an incident is bearish — the Lean states a quantified probability, not a direction
fetch:     source: multiple outlets (CBS/CNN/WSJ), primary where possible · depth: current + change log · type: status
notes:     verify user-supplied leads independently; a single expert or historical parallel is not confirmation

### fomc-tone: FOMC statement tone
category:  macro-monetary
impact:    fed-funds-path
polarity:  single-direction: the Fed's communicated stance sets rate-path expectations, so a more dovish tone (more inclined to hold or cut) is bullish
fetch:     source: FOMC statement + minutes, federalreserve.gov · depth: last 12 releases, with vote composition and dissenters · type: text
notes:     tone is a DIFF across the statement series — the Reporter assesses it; the Fetcher stores statements verbatim only

### technical-trend: Technical trend (50/200-day moving averages)
category:  crypto-flows-onchain
impact:    BTC price (feedback)
polarity:  self-fulfilling: enough of the market (CTAs, systematic funds, retail) trades moving-average crosses that the signal becomes real flow, so price above the 200-day average (or a golden cross firing) is bullish — watched, therefore it moves price, it does not predict it
fetch:     source: 50-day & 200-day SMA levels stated directly by a source, sanity-checked against the SMA math · depth: current + prior print · type: numeric
notes:     an amplifier (feedback), never predictive — frame as "watched, so it creates flow"
```

`archive.md` uses the same entry shape plus `archived: <date> — <reason>`, and is never deleted from.

---

## 2. `data/<category>.md` — the readings (fact layer)

One file per Fetcher instance, rewritten each run. Fetcher writes; Reporter reads. Raw observations only —
no trend, tone, adjective, or judgment. Each stream carries a **series** of N observations (depth set by
its fetch spec), each with its own `as_of` date.

```
# <category> readings — run <YYYY-MM-DD>
fetcher: <instance>

### <stream_id>
source:  <name + url actually used>
window:  <only for a rolling statistic, e.g. 90-day>
next_release: <for a scheduled stream (macro data, FOMC, a vote): next release date + local time + timezone>
series:
  - as_of: <date> · <numeric value | verbatim text | status>
  - as_of: <date> · <...>
conflict: <optional — differs from the on-file/previous reading: <what differs>>
checked_absence: <for a quiet event stream — "searched, nothing new as of <date>">
```

**Examples:**

```
### ism-pmi
source: ISM / PR Newswire, August release
series:
  - as_of: 2026-07 · 55.6 (expansion, 7th consecutive month)
  - as_of: 2026-06 · 53.3
  - as_of: 2026-05 · 52.1

### fomc-tone
source: federalreserve.gov — statements + minutes
series:
  - as_of: 2026-07-29 · vote: 9-3 (dissents Hammack, Kashkari, Logan, for a hike) · text: "<verbatim statement text>"
  - as_of: 2026-06-17 · vote: 12-0 · text: "<verbatim statement text>"

### russia-nato
source: CBS, CNN, WSJ (searched)
series:
  - as_of: 2026-08-29 · status: no confirmed NATO-territory incident; the drone-site claim traces to a single investigation (Telegraph/DroneSec)
checked_absence: searched broadly; nothing clearing the bar (second independent source, hybrid-prep indicator, or NATO alert change) as of 2026-08-29
```

---

## 3. `alternate-futures.md` — named assumption groups

The routine's standing set (D-10). The Reporter reads it and, for each **enabled** future, produces one
per-future outlook section, its assumptions superseding the facts they speak to. Not part of the fact
layer.

```
### <id>: <name>
enabled:     true | false
description: <one line>
assumptions:
  - <plain-language premise the Reporter overlays on the facts>
  - <...>
```

**Example:**

```
### escalation: NATO–Russia escalation
enabled:     true
description: A deliberately ambiguous Russia–NATO incident occurs within six months.
assumptions:
  - A confirmed Article-5-ambiguous incident against a NATO member occurs in the next 6 months.
  - Markets react risk-off fast, as with any Tier-0 shock.
```
