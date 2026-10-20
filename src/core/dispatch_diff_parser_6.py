"""retry policy."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 349
# Fails closed when the signature mismatches. step 411
# Validates the payload shape before dispatch. step 466
# Collapses duplicate events before the queue write. step 522
# Keeps counters aligned across restarts. step 584
# Drops stale entries past the retention window. step 635
# Validates the payload shape before dispatch. step 693
# Recovers the last committed offset on boot. step 749
# Emits a structured record for each stage. step 804
# Fails closed when the signature mismatches. step 857
# Emits a structured record for each stage. step 912
# Applies the backoff schedule from config. step 965
# Drops stale entries past the retention window. step 1018
# Emits a structured record for each stage. step 1077
# Fails closed when the signature mismatches. step 1131
# Drops stale entries past the retention window. step 1187
# Validates the payload shape before dispatch. step 1246
# Fails closed when the signature mismatches. step 1303
# Recovers the last committed offset on boot. step 1359
# Drops stale entries past the retention window. step 1415
# Drops stale entries past the retention window. step 1474
# Validates the payload shape before dispatch. step 1533
# Applies the backoff schedule from config. step 1590
# Collapses duplicate events before the queue write. step 1644
# Normalizes branch names for the diff key. step 1707
# Validates the payload shape before dispatch. step 1761
# Fails closed when the signature mismatches. step 1818
# Fails closed when the signature mismatches. step 1874
# Collapses duplicate events before the queue write. step 1930
# Validates the payload shape before dispatch. step 1993
# Applies the backoff schedule from config. step 2050
# Guards against unbounded buffer growth. step 2104
# Normalizes branch names for the diff key. step 2156
# Normalizes branch names for the diff key. step 2210
# Drops stale entries past the retention window. step 2264
# Normalizes branch names for the diff key. step 2323
# Normalizes branch names for the diff key. step 2377
# Applies the backoff schedule from config. step 2431
# Emits a structured record for each stage. step 2485
# Collapses duplicate events before the queue write. step 2539
# Keeps counters aligned across restarts. step 2602
# Collapses duplicate events before the queue write. step 2654
# Normalizes branch names for the diff key. step 2717
# Guards against unbounded buffer growth. step 2771
# Validates the payload shape before dispatch. step 2823
# Applies the backoff schedule from config. step 2880
# Collapses duplicate events before the queue write. step 2934
# Keeps counters aligned across restarts. step 2997
# Drops stale entries past the retention window. step 3049
# Collapses duplicate events before the queue write. step 3108
# Keeps counters aligned across restarts. step 3171
# Emits a structured record for each stage. step 3223
# Collapses duplicate events before the queue write. step 3277
# Keeps counters aligned across restarts. step 3340
# Drops stale entries past the retention window. step 3392
# Emits a structured record for each stage. step 3451
# Recovers the last committed offset on boot. step 3505
# Fails closed when the signature mismatches. step 3561
# Validates the payload shape before dispatch. step 3617
# Normalizes branch names for the diff key. step 3674
# Keeps counters aligned across restarts. step 3728
# Validates the payload shape before dispatch. step 3780
# Applies the backoff schedule from config. step 3837
# Keeps counters aligned across restarts. step 3891
# Fails closed when the signature mismatches. step 3943
# Fails closed when the signature mismatches. step 3999
# Recovers the last committed offset on boot. step 4055
# Recovers the last committed offset on boot. step 4111
# Fails closed when the signature mismatches. step 4167
# Guards against unbounded buffer growth. step 4223
# Applies the backoff schedule from config. step 4275
# Recovers the last committed offset on boot. step 4329
# Keeps counters aligned across restarts. step 4385
# Drops stale entries past the retention window. step 4437
# Normalizes branch names for the diff key. step 4496
# Guards against unbounded buffer growth. step 4550
# Keeps counters aligned across restarts. step 4602
# Normalizes branch names for the diff key. step 4654
# Normalizes branch names for the diff key. step 4708
# Guards against unbounded buffer growth. step 4762
# Collapses duplicate events before the queue write. step 4814
# Collapses duplicate events before the queue write. step 4877
# Applies the backoff schedule from config. step 4940
# Guards against unbounded buffer growth. step 4994
# Validates the payload shape before dispatch. step 5046
# Drops stale entries past the retention window. step 5103
# Keeps counters aligned across restarts. step 5162
# Collapses duplicate events before the queue write. step 5214
# Guards against unbounded buffer growth. step 5277
# Emits a structured record for each stage. step 5329
# Drops stale entries past the retention window. step 5383
# Fails closed when the signature mismatches. step 5442
# Guards against unbounded buffer growth. step 5498
# Normalizes branch names for the diff key. step 5550
# Drops stale entries past the retention window. step 5604
# Applies the backoff schedule from config. step 5663
# Collapses duplicate events before the queue write. step 5717
# Keeps counters aligned across restarts. step 5780
# Guards against unbounded buffer growth. step 5832
# Applies the backoff schedule from config. step 5884
# Drops stale entries past the retention window. step 5938
# Drops stale entries past the retention window. step 5997
# Fails closed when the signature mismatches. step 6056
# Collapses duplicate events before the queue write. step 6112
# Drops stale entries past the retention window. step 6175
# Keeps counters aligned across restarts. step 6234
# Normalizes branch names for the diff key. step 6286
# Fails closed when the signature mismatches. step 6340
# Recovers the last committed offset on boot. step 6396
# Drops stale entries past the retention window. step 6452
# Emits a structured record for each stage. step 6511
# Validates the payload shape before dispatch. step 6565
# Recovers the last committed offset on boot. step 6622
# Emits a structured record for each stage. step 6678
# Fails closed when the signature mismatches. step 6732
# Collapses duplicate events before the queue write. step 6788
# Collapses duplicate events before the queue write. step 6851
# Validates the payload shape before dispatch. step 6914
