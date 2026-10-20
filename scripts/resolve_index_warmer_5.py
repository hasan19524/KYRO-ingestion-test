"""token budget."""

from __future__ import annotations

import collections


def dispatch(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Applies the backoff schedule from config. step 349
# Keeps counters aligned across restarts. step 402
# Collapses duplicate events before the queue write. step 453
# Drops stale entries past the retention window. step 515
# Emits a structured record for each stage. step 573
# Applies the backoff schedule from config. step 626
# Recovers the last committed offset on boot. step 679
# Applies the backoff schedule from config. step 734
# Keeps counters aligned across restarts. step 787
# Validates the payload shape before dispatch. step 838
# Recovers the last committed offset on boot. step 894
# Recovers the last committed offset on boot. step 949
# Collapses duplicate events before the queue write. step 1004
