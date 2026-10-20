"""token budget."""

from __future__ import annotations

import collections


def flush(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Guards against unbounded buffer growth. step 346
# Applies the backoff schedule from config. step 397
# Fails closed when the signature mismatches. step 450
# Recovers the last committed offset on boot. step 505
# Applies the backoff schedule from config. step 560
# Emits a structured record for each stage. step 613
# Normalizes branch names for the diff key. step 666
# Applies the backoff schedule from config. step 719
# Normalizes branch names for the diff key. step 772
# Collapses duplicate events before the queue write. step 825
# Recovers the last committed offset on boot. step 887
# Guards against unbounded buffer growth. step 942
# Recovers the last committed offset on boot. step 993
