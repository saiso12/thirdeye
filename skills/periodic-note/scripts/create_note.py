#!/usr/bin/env python3
"""
Create periodic notes from Obsidian templates with Templater variable processing.

Usage:
    python create_note.py <type> [--date YYYY-MM-DD] [--vault PATH]

Types: daily, weekly, monthly, quarterly, yearly

Examples:
    python create_note.py daily                    # Today's daily note
    python create_note.py daily --date 2025-01-15  # Specific date
    python create_note.py weekly                   # Current week
    python create_note.py monthly                  # Current month
"""

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path


# Configuration
DEFAULT_VAULT = Path.home() / "Documents/thirdeye"

TEMPLATES = {
    "daily": "templates/daily.md",
    "weekly": "templates/weekly.md",
    "monthly": "templates/monthly.md",
    "quarterly": "templates/quarterly.md",
    "yearly": "templates/yearly.md",
}

OUTPUT_DIRS = {
    "daily": "reviews/daily",
    "weekly": "reviews/weekly",
    "monthly": "reviews/monthly",
    "quarterly": "reviews/quarterly",
    "yearly": "reviews/yearly",
}


def get_week_number(dt: datetime) -> int:
    """Get ISO week number."""
    return dt.isocalendar()[1]


def get_quarter(dt: datetime) -> int:
    """Get quarter number (1-4)."""
    return (dt.month - 1) // 3 + 1


def get_filename(note_type: str, dt: datetime) -> str:
    """Generate filename based on note type and date."""
    if note_type == "daily":
        return f"{dt.strftime('%Y-%m-%d')}.md"
    elif note_type == "weekly":
        return f"Weekly Review {dt.year}-W{get_week_number(dt):02d}.md"
    elif note_type == "monthly":
        return f"Monthly Review {dt.strftime('%Y-%m')}.md"
    elif note_type == "quarterly":
        return f"Quarterly Review {dt.year}-Q{get_quarter(dt)}.md"
    elif note_type == "yearly":
        return f"Yearly Review {dt.year}.md"
    else:
        raise ValueError(f"Unknown note type: {note_type}")


def get_file_title(note_type: str, dt: datetime) -> str:
    """Get the file title (filename without .md extension)."""
    filename = get_filename(note_type, dt)
    return filename.rsplit(".", 1)[0]


def format_date(dt: datetime, fmt: str) -> str:
    """Convert Moment.js format to Python strftime and format date."""
    # Moment.js to strftime mapping
    replacements = [
        ("YYYY", "%Y"),
        ("YY", "%y"),
        ("MMMM", "%B"),
        ("MMM", "%b"),
        ("MM", "%m"),
        ("M", "%-m"),
        ("dddd", "%A"),
        ("ddd", "%a"),
        ("DD", "%d"),
        ("D", "%-d"),
        ("HH", "%H"),
        ("mm", "%M"),
        ("ss", "%S"),
        ("ww", "{week:02d}"),  # ISO week number
    ]

    result = fmt
    for moment_fmt, py_fmt in replacements:
        result = result.replace(moment_fmt, py_fmt)

    # Format the date
    formatted = dt.strftime(result)

    # Handle week number separately
    if "{week:02d}" in formatted:
        formatted = formatted.replace("{week:02d}", f"{get_week_number(dt):02d}")

    return formatted


def parse_duration(duration_str: str) -> timedelta:
    """Parse duration strings like 'P-1M' (minus 1 month) or '-7' (minus 7 days)."""
    if duration_str.startswith("P"):
        # ISO 8601 duration like P-1M
        match = re.match(r"P(-?\d+)([YMWD])", duration_str)
        if match:
            value = int(match.group(1))
            unit = match.group(2)
            if unit == "Y":
                return timedelta(days=value * 365)
            elif unit == "M":
                return timedelta(days=value * 30)
            elif unit == "W":
                return timedelta(weeks=value)
            elif unit == "D":
                return timedelta(days=value)
    else:
        # Simple offset like -7 or 0
        try:
            return timedelta(days=int(duration_str))
        except ValueError:
            pass
    return timedelta(0)


def process_templater_date(match: re.Match, base_date: datetime, file_title: str) -> str:
    """Process tp.date.now() calls."""
    fmt = match.group(1)
    offset_str = match.group(2) if match.lastindex >= 2 else None

    dt = base_date
    if offset_str:
        offset_str = offset_str.strip().strip(",").strip('"').strip("'")
        if offset_str:
            dt = base_date + parse_duration(offset_str)

    return format_date(dt, fmt)


def process_templater_weekday(match: re.Match, base_date: datetime) -> str:
    """Process tp.date.weekday() calls."""
    fmt = match.group(1)
    offset = int(match.group(2)) if match.lastindex >= 2 else 0

    # Get the start of the week (Monday) and add offset
    start_of_week = base_date - timedelta(days=base_date.weekday())
    target_date = start_of_week + timedelta(days=offset)

    return format_date(target_date, fmt)


def process_template(content: str, note_type: str, dt: datetime) -> str:
    """Process Templater variables in template content."""
    file_title = get_file_title(note_type, dt)

    # Remove the tp.file.move line (we handle file location ourselves)
    content = re.sub(r'.*<% await tp\.file\.move\([^)]+\) %>.*\n?', '', content)

    # Replace tp.file.title
    content = content.replace("<% tp.file.title %>", file_title)

    # Process tp.date.now with various argument patterns
    # Pattern: tp.date.now("format") or tp.date.now("format", offset) or tp.date.now("format", offset, ref)
    def replace_date_now(m):
        full_match = m.group(0)
        fmt = m.group(1)
        rest = m.group(2) if m.lastindex >= 2 and m.group(2) else ""

        # Parse offset if present
        offset_match = re.search(r'[-\d]+|"P[^"]+"', rest)
        offset = 0
        if offset_match:
            offset_str = offset_match.group().strip('"')
            if offset_str.startswith("P"):
                delta = parse_duration(offset_str)
                target_dt = dt + delta
            else:
                try:
                    offset = int(offset_str)
                    target_dt = dt + timedelta(days=offset)
                except ValueError:
                    target_dt = dt
        else:
            target_dt = dt

        return format_date(target_dt, fmt)

    content = re.sub(
        r'<% tp\.date\.now\("([^"]+)"(?:,([^)]*))?\)\s*,?\s*%>',
        replace_date_now,
        content
    )

    # Process tp.date.weekday
    def replace_weekday(m):
        fmt = m.group(1)
        offset = int(m.group(2)) if m.group(2) else 0
        start_of_week = dt - timedelta(days=dt.weekday())
        target_date = start_of_week + timedelta(days=offset + 6)  # Adjust for Sunday-Saturday week
        return format_date(target_date, fmt)

    content = re.sub(
        r'<% tp\.date\.weekday\("([^"]+)"(?:,\s*(-?\d+))?\)\s*%>',
        replace_weekday,
        content
    )

    # Clean up any remaining simple date patterns
    content = content.replace("{{date:YYYY-MM-DD}}", dt.strftime("%Y-%m-%d"))

    return content


def create_note(note_type: str, target_date: datetime, vault_path: Path, dry_run: bool = False) -> Path:
    """Create a periodic note from template."""
    template_path = vault_path / TEMPLATES[note_type]
    output_dir = vault_path / OUTPUT_DIRS[note_type]
    filename = get_filename(note_type, target_date)
    output_path = output_dir / filename

    # Check if template exists
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    # Check if note already exists
    if output_path.exists():
        raise FileExistsError(f"Note already exists: {output_path}")

    # Read and process template
    template_content = template_path.read_text()
    processed_content = process_template(template_content, note_type, target_date)

    if dry_run:
        print(f"Would create: {output_path}")
        print("---")
        print(processed_content[:500])
        if len(processed_content) > 500:
            print(f"... ({len(processed_content)} chars total)")
        return output_path

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write the note
    output_path.write_text(processed_content)

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Create periodic notes from Obsidian templates")
    parser.add_argument("type", choices=["daily", "weekly", "monthly", "quarterly", "yearly"],
                        help="Type of note to create")
    parser.add_argument("--date", type=str, default=None,
                        help="Target date (YYYY-MM-DD format, defaults to today)")
    parser.add_argument("--vault", type=str, default=str(DEFAULT_VAULT),
                        help=f"Path to Obsidian vault (default: {DEFAULT_VAULT})")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without creating file")

    args = parser.parse_args()

    # Parse target date
    if args.date:
        try:
            target_date = datetime.strptime(args.date, "%Y-%m-%d")
        except ValueError:
            print(f"Error: Invalid date format '{args.date}'. Use YYYY-MM-DD.", file=sys.stderr)
            sys.exit(1)
    else:
        target_date = datetime.now()

    vault_path = Path(args.vault)
    if not vault_path.exists():
        print(f"Error: Vault not found at {vault_path}", file=sys.stderr)
        sys.exit(1)

    try:
        output_path = create_note(args.type, target_date, vault_path, args.dry_run)
        if not args.dry_run:
            print(f"Created: {output_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except FileExistsError as e:
        print(f"Note already exists: {e}", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
