#!/usr/bin/env python3
"""Render report.md into report.html via report-template.html.

Stdlib-only (no pip install) so the daily routine's tail step never needs an
unlisted Bash permission to fetch a dependency. Handles the Markdown subset
the `reporter` subagent actually produces: h1-h4, hr, bold-label paragraph
blocks (line breaks preserved), bullet lists, pipe tables (wrapped in
.table-scroll per the template's contract), and inline **bold**, `code`,
[text](url).
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORT_MD = ROOT / "report.md"
TEMPLATE = ROOT / "report-template.html"
REPORT_HTML = ROOT / "report.html"

INLINE_CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def render_inline(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = INLINE_CODE_RE.sub(lambda m: f"<code>{m.group(1)}</code>", escaped)
    escaped = BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", escaped)
    escaped = LINK_RE.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', escaped)
    return escaped


def is_table_separator(line: str) -> bool:
    return bool(re.fullmatch(r"\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?", line.strip()))


def split_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def render_table(lines: list[str]) -> str:
    header_cells = split_row(lines[0])
    body_rows = [split_row(line) for line in lines[2:]]
    thead = "<tr>" + "".join(f"<th>{render_inline(c)}</th>" for c in header_cells) + "</tr>"
    tbody = "".join(
        "<tr>" + "".join(f"<td>{render_inline(c)}</td>" for c in row) + "</tr>"
        for row in body_rows
    )
    return (
        '<div class="table-scroll"><table><thead>' + thead + "</thead><tbody>"
        + tbody + "</tbody></table></div>"
    )


def render(md_text: str) -> str:
    lines = md_text.split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)
    paragraph_buf: list[str] = []

    def flush_paragraph():
        if paragraph_buf:
            joined = "<br />\n".join(render_inline(l) for l in paragraph_buf)
            out.append(f"<p>{joined}</p>")
            paragraph_buf.clear()

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped == "":
            flush_paragraph()
            i += 1
            continue

        header_match = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if header_match:
            flush_paragraph()
            level = len(header_match.group(1))
            out.append(f"<h{level}>{render_inline(header_match.group(2))}</h{level}>")
            i += 1
            continue

        if re.fullmatch(r"-{3,}", stripped):
            flush_paragraph()
            out.append("<hr />")
            i += 1
            continue

        if (
            stripped.startswith("|")
            and i + 1 < n
            and is_table_separator(lines[i + 1])
        ):
            flush_paragraph()
            table_lines = [lines[i], lines[i + 1]]
            j = i + 2
            while j < n and lines[j].strip().startswith("|"):
                table_lines.append(lines[j])
                j += 1
            out.append(render_table(table_lines))
            i = j
            continue

        if re.match(r"^[-*]\s+", stripped):
            flush_paragraph()
            items = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(re.match(r"^[-*]\s+(.*)$", lines[i].strip()).group(1))
                i += 1
            out.append("<ul>" + "".join(f"<li>{render_inline(it)}</li>" for it in items) + "</ul>")
            continue

        paragraph_buf.append(stripped)
        i += 1

    flush_paragraph()
    return "\n".join(out)


def main() -> int:
    if not REPORT_MD.exists():
        print(f"error: {REPORT_MD} not found", file=sys.stderr)
        return 1
    if not TEMPLATE.exists():
        print(f"error: {TEMPLATE} not found", file=sys.stderr)
        return 1

    md_text = REPORT_MD.read_text(encoding="utf-8")
    body_html = render(md_text)
    template = TEMPLATE.read_text(encoding="utf-8")
    if "<!-- REPORT_CONTENT -->" not in template:
        print("error: report-template.html is missing the REPORT_CONTENT placeholder", file=sys.stderr)
        return 1

    out = template.replace("<!-- REPORT_CONTENT -->", body_html)
    REPORT_HTML.write_text(out, encoding="utf-8")
    print(f"wrote {REPORT_HTML} ({len(out)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
