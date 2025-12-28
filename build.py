#!/usr/bin/env python3
"""
Build script for Three Sisters Stories
Scans markdown files and generates content/manifest.json

Run this after adding new content:
    python3 build.py
"""

import os
import json
import re
from pathlib import Path

CONTENT_DIR = Path(__file__).parent / "content"
SISTERS = ["susie", "betsy", "natalie"]


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    frontmatter = {}
    body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    frontmatter[key.strip()] = value.strip().strip('"\'')
            body = parts[2].strip()

    return frontmatter, body


def parse_markdown_table(content):
    """Parse a markdown table into a list of dictionaries."""
    lines = [l.strip() for l in content.split("\n") if l.strip()]

    # Find table lines (start with |)
    table_lines = [l for l in lines if l.startswith("|")]
    if len(table_lines) < 2:
        return []

    # Parse header
    header_line = table_lines[0]
    headers = [h.strip() for h in header_line.split("|")[1:-1]]
    headers = [h.lower().replace(" ", "_") for h in headers]

    # Skip separator line (index 1), parse data rows
    rows = []
    for line in table_lines[2:]:
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) == len(headers):
            row = {}
            for i, header in enumerate(headers):
                if cells[i]:  # Only add non-empty values
                    row[header] = cells[i]
            if row:  # Only add non-empty rows
                rows.append(row)

    return rows


def parse_video_list(content):
    """Parse video list from markdown."""
    videos = []
    current = {}

    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("- id:"):
            if current:
                videos.append(current)
            current = {"id": line.replace("- id:", "").strip()}
        elif line.startswith("title:") and current:
            current["title"] = line.replace("title:", "").strip()
        elif line.startswith("date:") and current:
            current["date"] = line.replace("date:", "").strip()

    if current and "id" in current:
        videos.append(current)

    return videos


def parse_drawing_list(content):
    """Parse drawing list from markdown."""
    drawings = []
    current = {}

    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("- title:"):
            if current:
                drawings.append(current)
            current = {"title": line.replace("- title:", "").strip()}
        elif line.startswith("emoji:") and current:
            current["emoji"] = line.replace("emoji:", "").strip()
        elif line.startswith("image:") and current:
            current["image"] = line.replace("image:", "").strip()

    if current and "title" in current:
        drawings.append(current)

    return drawings


def scan_sister_content(sister):
    """Scan all content for a sister."""
    sister_dir = CONTENT_DIR / sister
    content = {
        "videos": [],
        "booksRead": [],
        "booksWantToRead": [],
        "journal": [],
        "drawings": []
    }

    # Videos
    videos_file = sister_dir / "videos.md"
    if videos_file.exists():
        text = videos_file.read_text()
        _, body = parse_frontmatter(text)
        content["videos"] = parse_video_list(body)

    # Drawings
    drawings_file = sister_dir / "drawings.md"
    if drawings_file.exists():
        text = drawings_file.read_text()
        _, body = parse_frontmatter(text)
        content["drawings"] = parse_drawing_list(body)

    # Books I Have Read (markdown table)
    books_read_file = sister_dir / "books-have-read.md"
    if books_read_file.exists():
        text = books_read_file.read_text()
        _, body = parse_frontmatter(text)
        content["booksRead"] = parse_markdown_table(body)

    # Books I Want To Read (markdown table)
    books_want_file = sister_dir / "books-want-to-read.md"
    if books_want_file.exists():
        text = books_want_file.read_text()
        _, body = parse_frontmatter(text)
        content["booksWantToRead"] = parse_markdown_table(body)

    # Journal entries (one file per entry)
    journal_dir = sister_dir / "journal"
    if journal_dir.exists():
        entries = []
        for entry_file in sorted(journal_dir.glob("*.md"), reverse=True):
            text = entry_file.read_text()
            frontmatter, body = parse_frontmatter(text)
            entries.append({
                "date": frontmatter.get("date", entry_file.stem),
                "title": frontmatter.get("title", ""),
                "content": body
            })
        content["journal"] = entries

    return content


def build():
    """Build the manifest file."""
    manifest = {}

    for sister in SISTERS:
        print(f"Scanning {sister}...")
        manifest[sister] = scan_sister_content(sister)

        # Summary
        v = len(manifest[sister]["videos"])
        br = len(manifest[sister]["booksRead"])
        bw = len(manifest[sister]["booksWantToRead"])
        j = len(manifest[sister]["journal"])
        d = len(manifest[sister]["drawings"])
        print(f"  Found: {v} videos, {br} books read, {bw} want to read, {j} journal entries, {d} drawings")

    # Write manifest
    manifest_path = CONTENT_DIR / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\n✓ Generated {manifest_path}")
    print("\nRefresh your browser to see the changes!")


if __name__ == "__main__":
    build()
