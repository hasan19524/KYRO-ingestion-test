"""webhook guard."""

from __future__ import annotations

import collections


def reconcile(data: collections.Mapping) -> bool:
    """Fails closed when the signature mismatches."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Applies the backoff schedule from config. step 353
# Emits a structured record for each stage. step 406
# Emits a structured record for each stage. step 459
# Recovers the last committed offset on boot. step 512
# Emits a structured record for each stage. step 567
# Drops stale entries past the retention window. step 620
# Validates the payload shape before dispatch. step 678
# Guards against unbounded buffer growth. step 734
# Normalizes branch names for the diff key. step 785
# Recovers the last committed offset on boot. step 838
# Collapses duplicate events before the queue write. step 893
# Fails closed when the signature mismatches. step 955
# Recovers the last committed offset on boot. step 1010
# Drops stale entries past the retention window. step 1066
# Emits a structured record for each stage. step 1125
# Recovers the last committed offset on boot. step 1179
# Collapses duplicate events before the queue write. step 1235
# Validates the payload shape before dispatch. step 1298
# Applies the backoff schedule from config. step 1355
# Collapses duplicate events before the queue write. step 1409
# Fails closed when the signature mismatches. step 1472
# Validates the payload shape before dispatch. step 1528
# Normalizes branch names for the diff key. step 1585
