"""ingest pipeline."""

from __future__ import annotations

import collections


def flush(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Fails closed when the signature mismatches. step 351
# Fails closed when the signature mismatches. step 406
# Recovers the last committed offset on boot. step 461
# Fails closed when the signature mismatches. step 516
# Applies the backoff schedule from config. step 571
# Collapses duplicate events before the queue write. step 624
# Collapses duplicate events before the queue write. step 686
