# .ul Image Format — Converter & Viewer

A tiny custom image format (`.ul`) plus tools to create and view it.

## Setup

```bash
pip install -r requirements.txt
```

## Format spec (`ul_format.py`)

Header (20 bytes, little-endian) + pixel data (optionally zlib-compressed):

| Offset | Size | Field                                   |
|--------|------|------------------------------------------|
| 0      | 4    | Magic `"ULIM"`                            |
| 4      | 1    | Version (1)                               |
| 5      | 1    | Channels (3=RGB, 4=RGBA)                  |
| 6      | 1    | Compression (0=none, 1=zlib)              |
| 7      | 1    | Reserved (0)                              |
| 8      | 4    | Width (uint32)                            |
| 12     | 4    | Height (uint32)                           |
| 16     | 4    | Payload length in bytes                   |
| 20     | N    | Pixel data (row-major RGB/RGBA bytes)     |

## Convert PNG -> .ul (command line)

```bash
python png_to_ul.py to-ul input.png output.ul
python png_to_ul.py to-ul input.png output.ul --rgba          # force alpha channel
python png_to_ul.py to-ul input.png output.ul --no-compress   # skip zlib
python png_to_ul.py to-png output.ul back_to.png               # reverse
python png_to_ul.py batch ./pngs_folder ./ul_folder            # batch convert a folder
```

## View .ul files (GUI)

```bash
python ul_viewer.py
python ul_viewer.py path/to/image.ul   # open a file directly
```

In the viewer:
- **File > Open...** — browse for a `.ul` file (or just drag-and-drop one onto the window)
- **File > Import PNG/Image...** — pick any PNG/JPG/etc., converts it to `.ul`, saves it, and opens it
- **File > Export as PNG...** — save the currently open `.ul` image back out as PNG
- **View menu / toolbar** — Zoom In, Zoom Out, Actual Size, Fit to Window

## Notes

- Compression uses zlib on raw pixel bytes — simple and always round-trips exactly,
  but for photographic images it typically won't beat real PNG compression.
  This is by design: it's a straightforward, easy-to-extend format rather than an
  optimized one. If you want a smaller/faster format later, ideas to explore:
  run-length encoding, per-row filtering (like PNG's own filters) before zlib, or
  swapping zlib for `lz4`/`zstd`.
