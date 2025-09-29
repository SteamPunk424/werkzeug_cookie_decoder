#!/usr/bin/env python3
import sys
import base64
import zlib
import json

def decode_werkzeug_cookie(cookie: str):
    # Strip leading "session=" if present
    if cookie.startswith("session="):
        cookie = cookie[len("session="):]

    # Split into parts: .payload.signature
    parts = cookie.strip().split(".")
    if len(parts) < 2:
        raise ValueError("Invalid cookie format")

    payload_b64 = parts[1]

    # Normalize base64 (Werkzeug uses URL-safe, no padding)
    payload_b64 = payload_b64.replace("-", "+").replace("_", "/")
    padding = "=" * (-len(payload_b64) % 4)
    payload_b64 += padding

    # Decode + decompress
    raw = base64.b64decode(payload_b64)
    decompressed = zlib.decompress(raw)

    try:
        return json.loads(decompressed.decode())
    except Exception:
        return decompressed.decode(errors="replace")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} '<cookie_value>'")
        sys.exit(1)

    cookie = sys.argv[1]
    decoded = decode_werkzeug_cookie(cookie)

    if isinstance(decoded, dict):
        print(json.dumps(decoded, indent=2))
    else:
        print(decoded)
