#!/usr/bin/env python3
"""
png_to_ul.py
============

Command-line converter between PNG (or any Pillow-supported format) and the
custom .ul format.

Usage:
    Convert a single PNG to .ul:
        python png_to_ul.py to-ul input.png output.ul
        python png_to_ul.py to-ul input.png output.ul --no-compress
        python png_to_ul.py to-ul input.png output.ul --rgba

    Convert a .ul file back to PNG:
        python png_to_ul.py to-png input.ul output.png

    Batch-convert every PNG in a folder to .ul (same base filenames):
        python png_to_ul.py batch ./my_pngs ./my_ul_files
"""

import argparse
import os
import sys

from PIL import Image

from ul_format import write_ul_file, read_ul_file, UlFormatError


def convert_image_to_ul(input_path: str, output_path: str,
                         compress: bool = True, force_rgba: bool = False) -> None:
    img = Image.open(input_path)

    if force_rgba:
        img = img.convert("RGBA")
        channels = 4
    else:
        # Keep alpha if the source image has it, otherwise use RGB.
        if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
            img = img.convert("RGBA")
            channels = 4
        else:
            img = img.convert("RGB")
            channels = 3

    width, height = img.size
    pixels = img.tobytes()  # row-major, matches our .ul spec

    write_ul_file(output_path, width, height, channels, pixels, compress=compress)

    src_size = os.path.getsize(input_path)
    dst_size = os.path.getsize(output_path)
    print(f"Wrote {output_path}  ({width}x{height}, {channels}ch, "
          f"{'zlib' if compress else 'raw'})  "
          f"[{src_size} bytes -> {dst_size} bytes]")


def convert_ul_to_image(input_path: str, output_path: str) -> None:
    ul_img = read_ul_file(input_path)
    mode = "RGBA" if ul_img.channels == 4 else "RGB"
    img = Image.frombytes(mode, (ul_img.width, ul_img.height), ul_img.pixels)
    img.save(output_path)
    print(f"Wrote {output_path}  ({ul_img.width}x{ul_img.height}, {mode})")


def batch_convert(input_dir: str, output_dir: str, compress: bool = True) -> None:
    os.makedirs(output_dir, exist_ok=True)
    exts = (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp", ".tif", ".tiff")
    files = [f for f in sorted(os.listdir(input_dir)) if f.lower().endswith(exts)]

    if not files:
        print(f"No image files found in {input_dir}")
        return

    for fname in files:
        in_path = os.path.join(input_dir, fname)
        out_name = os.path.splitext(fname)[0] + ".ul"
        out_path = os.path.join(output_dir, out_name)
        try:
            convert_image_to_ul(in_path, out_path, compress=compress)
        except Exception as e:
            print(f"  FAILED: {fname}: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Convert between PNG/images and .ul format")
    sub = parser.add_subparsers(dest="command", required=True)

    p_to_ul = sub.add_parser("to-ul", help="Convert an image (e.g. PNG) to .ul")
    p_to_ul.add_argument("input", help="Path to input image (PNG, JPG, etc.)")
    p_to_ul.add_argument("output", help="Path to output .ul file")
    p_to_ul.add_argument("--no-compress", action="store_true", help="Store pixels uncompressed")
    p_to_ul.add_argument("--rgba", action="store_true", help="Force RGBA (keep/add alpha channel)")

    p_to_png = sub.add_parser("to-png", help="Convert a .ul file back to an image")
    p_to_png.add_argument("input", help="Path to input .ul file")
    p_to_png.add_argument("output", help="Path to output image (e.g. output.png)")

    p_batch = sub.add_parser("batch", help="Convert every image in a folder to .ul")
    p_batch.add_argument("input_dir", help="Folder containing source images")
    p_batch.add_argument("output_dir", help="Folder to write .ul files into")
    p_batch.add_argument("--no-compress", action="store_true", help="Store pixels uncompressed")

    args = parser.parse_args()

    try:
        if args.command == "to-ul":
            convert_image_to_ul(args.input, args.output,
                                 compress=not args.no_compress, force_rgba=args.rgba)
        elif args.command == "to-png":
            convert_ul_to_image(args.input, args.output)
        elif args.command == "batch":
            batch_convert(args.input_dir, args.output_dir, compress=not args.no_compress)
    except (UlFormatError, FileNotFoundError, OSError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
