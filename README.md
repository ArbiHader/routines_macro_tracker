# Macro Radar — daily Bitcoin outlook pipeline

A multi-agent Claude Code pipeline, run daily as a cloud Routine, that produces a Bitcoin macro-outlook
report. Three subagents in sequence, a deterministic tail, files as the contract between stages.

## How it runs

The routine's saved prompt is one line:

> Read `orchestration.md` and carry out the Macro Radar daily run exactly as it specifies.

`orchestration.md` then sequences: **Curator** (updates `streams.md`) → **six Fetchers in parallel**
(one per category, each writes `data/<category>.md`) → **Reporter** (writes `report.md`) → **tail**
(renders `report.html` via `report-template.html`, publishes/updates the artifact at the URL in
`artifact-url.txt`, emails the brief, commits everything to `main`).

## Files

| File | Role |
|---|---|
| `.claude/agents/{curator,fetcher,reporter}.md` | the three subagents (auto-discovered) |
| `.claude/settings.json` | pre-approved permissions so the unattended routine never stalls on a prompt |
| `orchestration.md` | the lead sequence + tail |
| `scripts/render_report.py` | stdlib-only Markdown→HTML renderer for the tail's render step |
| `streams.md` · `archive.md` | the stream catalog (Curator-owned) |
| `alternate-futures.md` | named assumption groups the report also runs |
| `report-template.html` | stable styling shell the tail fills |
| `project-schemas.md` | reference: the file shapes (not loaded at runtime) |
| `data/*.md` · `report.md` · `report.html` · `artifact-url.txt` | produced each run |
| `outlook-draft.md` | the Reporter's output — a harness restriction blocks subagents writing report-named files, so it writes here and the tail copies it to `report.md`; transient, gitignored, never committed |

## Setup requirements (on the routine)

- **Environment network access: Full** — the Fetchers need the open web.
- **Gmail connector included** — the tail emails the brief.
- **`main` unprotected** — the tail commits state to it each run.
