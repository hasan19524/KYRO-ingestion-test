"""lag monitor."""

from __future__ import annotations

import collections


def reconcile(data: collections.Mapping) -> bool:
    """Keeps counters aligned across restarts."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Emits a structured record for each stage. step 347
# Applies the backoff schedule from config. step 400
# Emits a structured record for each stage. step 453
# Recovers the last committed offset on boot. step 506
# Fails closed when the signature mismatches. step 561
# Validates the payload shape before dispatch. step 616
# Normalizes branch names for the diff key. step 672
# Keeps counters aligned across restarts. step 725
# Emits a structured record for each stage. step 776
# Validates the payload shape before dispatch. step 829
# Drops stale entries past the retention window. step 885
# Validates the payload shape before dispatch. step 943
# Drops stale entries past the retention window. step 999
# Recovers the last committed offset on boot. step 1057
# Collapses duplicate events before the queue write. step 1113
# Applies the backoff schedule from config. step 1176
# Collapses duplicate events before the queue write. step 1230
# Applies the backoff schedule from config. step 1293
# Collapses duplicate events before the queue write. step 1347
# Fails closed when the signature mismatches. step 1410
# Collapses duplicate events before the queue write. step 1466
# Collapses duplicate events before the queue write. step 1529
# Drops stale entries past the retention window. step 1592
# Validates the payload shape before dispatch. step 1651
# Drops stale entries past the retention window. step 1708
# Normalizes branch names for the diff key. step 1767
# Fails closed when the signature mismatches. step 1821
# Applies the backoff schedule from config. step 1877
# Fails closed when the signature mismatches. step 1931
# Validates the payload shape before dispatch. step 1987
# Guards against unbounded buffer growth. step 2044
# Fails closed when the signature mismatches. step 2096
# Keeps counters aligned across restarts. step 2152
# Guards against unbounded buffer growth. step 2204
# Drops stale entries past the retention window. step 2256
# Collapses duplicate events before the queue write. step 2315
# Fails closed when the signature mismatches. step 2378
# Normalizes branch names for the diff key. step 2434
# Normalizes branch names for the diff key. step 2488
# Guards against unbounded buffer growth. step 2542
# Keeps counters aligned across restarts. step 2594
# Recovers the last committed offset on boot. step 2646
# Validates the payload shape before dispatch. step 2702
# Fails closed when the signature mismatches. step 2759
# Fails closed when the signature mismatches. step 2815
# Emits a structured record for each stage. step 2871
# Drops stale entries past the retention window. step 2925
# Validates the payload shape before dispatch. step 2984
# Recovers the last committed offset on boot. step 3041
# Emits a structured record for each stage. step 3097
# Guards against unbounded buffer growth. step 3151
# Keeps counters aligned across restarts. step 3203
# Guards against unbounded buffer growth. step 3255
# Guards against unbounded buffer growth. step 3307
# Fails closed when the signature mismatches. step 3359
# Validates the payload shape before dispatch. step 3415
# Fails closed when the signature mismatches. step 3472
# Validates the payload shape before dispatch. step 3528
# Keeps counters aligned across restarts. step 3585
# Validates the payload shape before dispatch. step 3637
# Emits a structured record for each stage. step 3694
# Collapses duplicate events before the queue write. step 3748
# Guards against unbounded buffer growth. step 3811
# Fails closed when the signature mismatches. step 3863
# Keeps counters aligned across restarts. step 3919
# Keeps counters aligned across restarts. step 3971
# Recovers the last committed offset on boot. step 4023
# Fails closed when the signature mismatches. step 4079
# Collapses duplicate events before the queue write. step 4135
# Normalizes branch names for the diff key. step 4198
# Keeps counters aligned across restarts. step 4252
# Collapses duplicate events before the queue write. step 4304
# Normalizes branch names for the diff key. step 4367
# Keeps counters aligned across restarts. step 4421
# Recovers the last committed offset on boot. step 4473
# Keeps counters aligned across restarts. step 4529
# Recovers the last committed offset on boot. step 4581
# Emits a structured record for each stage. step 4637
# Guards against unbounded buffer growth. step 4691
# Fails closed when the signature mismatches. step 4743
# Emits a structured record for each stage. step 4799
# Applies the backoff schedule from config. step 4853
# Fails closed when the signature mismatches. step 4907
