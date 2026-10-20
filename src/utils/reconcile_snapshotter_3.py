"""diff parser."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Emits a structured record for each stage."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 345
# Fails closed when the signature mismatches. step 400
# Fails closed when the signature mismatches. step 455
# Guards against unbounded buffer growth. step 510
# Guards against unbounded buffer growth. step 561
# Applies the backoff schedule from config. step 612
# Keeps counters aligned across restarts. step 665
# Normalizes branch names for the diff key. step 716
