#!/usr/bin/env python3
"""Dependency-free structural smoke check (not an HTML/CSS validator)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
INDEX = PUBLIC / "index.html"

EXPECTED = {
    "container-queries", "grid-auto-fit", "aspect-ratio",
    "has-state", "nesting", "color-mix", "property",
    "scroll-driven", "scroll-snap", "anchor",
    "starting-style", "masks",
}


class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.cards = []
        self.links = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        ident = values.get("id")
        if ident:
            if ident in self.ids:
                self.errors.append("Duplicate ID: " + ident)
            self.ids.add(ident)
        if "card" in values.get("class", "").split():
            self.cards.append(ident)
        for attr in ("href", "src"):
            if values.get(attr):
                self.links.append(values[attr])


def main():
    if not INDEX.is_file():
        print("ERROR: missing public/index.html")
        return 1

    parser = Inspector()
    parser.feed(INDEX.read_text(encoding="utf-8"))
    errors = parser.errors[:]
    if set(parser.cards) != EXPECTED or len(parser.cards) != 12:
        errors.append(f"Expected 12 known experiment cards, got {parser.cards}")

    for link in parser.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or link.startswith("//"):
            continue
        path = unquote(url.path)
        dest = (PUBLIC / path).resolve() if path else INDEX.resolve()
        if not dest.is_relative_to(PUBLIC.resolve()):
            errors.append("Outside public/: " + link)
            continue
        if path and not dest.is_file():
            errors.append("Missing local file: " + link)
        if url.fragment and (not path or dest == INDEX.resolve()):
            if unquote(url.fragment) not in parser.ids:
                errors.append("Missing anchor: " + link)

    css_files = [PUBLIC / "styles/site.css", PUBLIC / "styles/experiments.css"]
    for file in [*css_files, PUBLIC / "favicon.svg"]:
        if not file.is_file():
            errors.append("Missing required file: " + str(file))
    if all(p.is_file() for p in css_files):
        css = "\n".join(p.read_text(encoding="utf-8") for p in css_files)
        if len(css.encode("utf-8")) <= INDEX.stat().st_size:
            errors.append("CSS code size must exceed the HTML file")
        for feature in ("@container", "@property", "@starting-style", "scroll-snap-type", "anchor-name", "color-mix(", "mask-image:"):
            if feature not in css:
                errors.append("Missing CSS experiment " + feature)

    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(f"OK: {len(parser.cards)} experiments; {len(parser.ids)} unique IDs; local references and CSS checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
