# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Tinwhistle is a Python utility that generates PDF fingering guides (tabs) for D whistle (tin whistle) music. It converts text-based note sequences into visual diagrams showing which finger holes should be open or closed.

## Running the Application

```bash
python tabs.py [input_file.txt]
```

If no input file is specified, it defaults to "grönnens-laid.txt". The generated PDF opens automatically after creation.

**Dependency:** `reportlab` library for PDF generation.

## Input File Format

```
Song Title
Song Subtitle (optional)

[Section Name]
note1 note2 note3 - note4 note5 - [more notes]
```

- First line is the title
- Notes are space-separated within phrases
- Hyphens `-` separate phrases
- Bracket sections `[Section Name]` become subtitles

## Architecture

Single-file application (`tabs.py`) with three main components:

1. **Note-to-fingering mapping:** The `holes` dictionary maps note names to 6-character strings representing finger positions (`*` = closed, `o` = open)

2. **Input parser:** Reads .txt files, extracting title, subtitles, and note sequences

3. **PDF renderer:** Uses ReportLab to draw flute diagrams on A4 landscape pages

## Supported Notes

- First octave (lowercase): d, e, f#, g, a, a#, b, c, c#
- Second octave (uppercase): D, E, F#, G, A, A#, B, C, C#

## Notes

- Code comments are in Dutch
- There's a TODO for adding half-closed holes support
