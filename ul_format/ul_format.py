"""
ul_format.py
============

Defines a small custom image format: ".ul"

File layout (all integers little-endian):

    Offset  Size  Field
    ------  ----  -----------------------------------------
    0       4     Magic bytes: b"ULIM"
    4       1     Version (currently 1)
    5       1     Channels (3 = RGB, 4 = RGBA)
    6       1     Compression (0 = none, 1 = zlib)
    7       1     Reserved (must be 0)
    8       4     Width  (uint32)
    12      4     Height (uint32)
    16      4     Data length in bytes, of what follows (uint32)
    20      N     Pixel data, row-major, top-to-bottom, left-to-right.
                  Raw bytes if Compression == 0, else zlib-compressed bytes.

This module has no GUI or CLI dependencies -- it's pure logic so both the
converter script and the viewer app can import it.
"""

import struct
import zlib
from dataclasses import dataclass

MAGIC = b"ULIM"
VERSION = 1

COMPRESSION_NONE = 0
COMPRESSION_ZLIB = 1

_HEADER_STRUCT = struct.Struct("<4sBBBBIII")  # magic, ver, channels, comp, reserved, w, h, data_len
HEADER_SIZE = _HEADER_STRUCT.size  # 20 bytes


class UlFormatError(ValueError):
    """Raised when a file is not a valid .ul file or is corrupted."""


@dataclass
class UlImage:
    width: int
    height: int
    channels: int  # 3 (RGB) or 4 (RGBA)
    pixels: bytes  # raw, decompressed pixel bytes, length == width*height*channels


def encode_ul(width: int, height: int, channels: int, pixels: bytes,
              compress: bool = True) -> bytes:
    """Build the raw bytes of a .ul file from raw pixel data."""
    if channels not in (3, 4):
        raise UlFormatError(f"channels must be 3 or 4, got {channels}")
    expected_len = width * height * channels
    if len(pixels) != expected_len:
        raise UlFormatError(
            f"pixel data length {len(pixels)} does not match "
            f"width*height*channels = {expected_len}"
        )

    if compress:
        payload = zlib.compress(pixels, level=6)
        compression = COMPRESSION_ZLIB
    else:
        payload = pixels
        compression = COMPRESSION_NONE

    header = _HEADER_STRUCT.pack(
        MAGIC, VERSION, channels, compression, 0,
        width, height, len(payload)
    )
    return header + payload


def decode_ul(data: bytes) -> UlImage:
    """Parse raw bytes of a .ul file and return a UlImage with decompressed pixels."""
    if len(data) < HEADER_SIZE:
        raise UlFormatError("file too short to contain a valid .ul header")

    magic, version, channels, compression, reserved, width, height, data_len = \
        _HEADER_STRUCT.unpack_from(data, 0)

    if magic != MAGIC:
        raise UlFormatError(f"bad magic bytes: {magic!r} (expected {MAGIC!r})")
    if version != VERSION:
        raise UlFormatError(f"unsupported .ul version: {version}")
    if channels not in (3, 4):
        raise UlFormatError(f"invalid channel count in header: {channels}")

    payload = data[HEADER_SIZE:HEADER_SIZE + data_len]
    if len(payload) != data_len:
        raise UlFormatError(
            f"truncated file: expected {data_len} bytes of payload, got {len(payload)}"
        )

    if compression == COMPRESSION_NONE:
        pixels = payload
    elif compression == COMPRESSION_ZLIB:
        try:
            pixels = zlib.decompress(payload)
        except zlib.error as e:
            raise UlFormatError(f"failed to decompress pixel data: {e}") from e
    else:
        raise UlFormatError(f"unknown compression type: {compression}")

    expected_len = width * height * channels
    if len(pixels) != expected_len:
        raise UlFormatError(
            f"decoded pixel data length {len(pixels)} does not match "
            f"width*height*channels = {expected_len}"
        )

    return UlImage(width=width, height=height, channels=channels, pixels=pixels)


def read_ul_file(path: str) -> UlImage:
    with open(path, "rb") as f:
        data = f.read()
    return decode_ul(data)


def write_ul_file(path: str, width: int, height: int, channels: int,
                   pixels: bytes, compress: bool = True) -> None:
    data = encode_ul(width, height, channels, pixels, compress=compress)
    with open(path, "wb") as f:
        f.write(data)
