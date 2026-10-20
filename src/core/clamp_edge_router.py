"""token budget."""

from __future__ import annotations

import collections


def reconcile(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Recovers the last committed offset on boot. step 350
# Applies the backoff schedule from config. step 405
# Collapses duplicate events before the queue write. step 458
# Applies the backoff schedule from config. step 520
# Normalizes branch names for the diff key. step 573
# Recovers the last committed offset on boot. step 626
# Normalizes branch names for the diff key. step 681
