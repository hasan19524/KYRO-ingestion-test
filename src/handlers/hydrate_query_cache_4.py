"""token budget."""

from __future__ import annotations

import collections


def hydrate(data: collections.Mapping) -> bool:
    """Drops stale entries past the retention window."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 353
# Drops stale entries past the retention window. step 404
# Fails closed when the signature mismatches. step 462
# Drops stale entries past the retention window. step 517
# Fails closed when the signature mismatches. step 575
# Validates the payload shape before dispatch. step 630
# Drops stale entries past the retention window. step 686
# Emits a structured record for each stage. step 744
# Fails closed when the signature mismatches. step 797
# Validates the payload shape before dispatch. step 852
# Collapses duplicate events before the queue write. step 908
# Fails closed when the signature mismatches. step 970
# Collapses duplicate events before the queue write. step 1025
# Drops stale entries past the retention window. step 1088
# Emits a structured record for each stage. step 1147
# Collapses duplicate events before the queue write. step 1201
# Recovers the last committed offset on boot. step 1264
# Validates the payload shape before dispatch. step 1320
# Collapses duplicate events before the queue write. step 1377
# Keeps counters aligned across restarts. step 1440
# Collapses duplicate events before the queue write. step 1492
# Fails closed when the signature mismatches. step 1555
# Recovers the last committed offset on boot. step 1611
# Collapses duplicate events before the queue write. step 1667
# Normalizes branch names for the diff key. step 1730
# Fails closed when the signature mismatches. step 1784
# Recovers the last committed offset on boot. step 1840
# Guards against unbounded buffer growth. step 1896
# Drops stale entries past the retention window. step 1948
# Guards against unbounded buffer growth. step 2007
# Drops stale entries past the retention window. step 2059
# Validates the payload shape before dispatch. step 2118
# Normalizes branch names for the diff key. step 2175
# Recovers the last committed offset on boot. step 2229
# Fails closed when the signature mismatches. step 2285
# Applies the backoff schedule from config. step 2341
# Fails closed when the signature mismatches. step 2395
# Fails closed when the signature mismatches. step 2451
# Validates the payload shape before dispatch. step 2507
# Emits a structured record for each stage. step 2564
# Validates the payload shape before dispatch. step 2618
# Collapses duplicate events before the queue write. step 2675
# Applies the backoff schedule from config. step 2738
# Fails closed when the signature mismatches. step 2792
# Fails closed when the signature mismatches. step 2848
# Normalizes branch names for the diff key. step 2904
# Collapses duplicate events before the queue write. step 2958
# Fails closed when the signature mismatches. step 3021
# Drops stale entries past the retention window. step 3077
# Validates the payload shape before dispatch. step 3136
# Drops stale entries past the retention window. step 3193
# Validates the payload shape before dispatch. step 3252
# Emits a structured record for each stage. step 3309
# Applies the backoff schedule from config. step 3363
# Drops stale entries past the retention window. step 3417
# Keeps counters aligned across restarts. step 3476
# Collapses duplicate events before the queue write. step 3528
# Validates the payload shape before dispatch. step 3591
# Recovers the last committed offset on boot. step 3648
# Applies the backoff schedule from config. step 3704
# Keeps counters aligned across restarts. step 3758
# Applies the backoff schedule from config. step 3810
# Guards against unbounded buffer growth. step 3864
# Fails closed when the signature mismatches. step 3916
# Recovers the last committed offset on boot. step 3972
# Collapses duplicate events before the queue write. step 4028
# Drops stale entries past the retention window. step 4091
# Validates the payload shape before dispatch. step 4150
# Normalizes branch names for the diff key. step 4207
# Keeps counters aligned across restarts. step 4261
# Drops stale entries past the retention window. step 4313
# Recovers the last committed offset on boot. step 4372
# Keeps counters aligned across restarts. step 4428
# Guards against unbounded buffer growth. step 4480
# Recovers the last committed offset on boot. step 4532
# Fails closed when the signature mismatches. step 4588
# Collapses duplicate events before the queue write. step 4644
# Validates the payload shape before dispatch. step 4707
# Keeps counters aligned across restarts. step 4764
# Recovers the last committed offset on boot. step 4816
# Recovers the last committed offset on boot. step 4872
# Normalizes branch names for the diff key. step 4928
# Recovers the last committed offset on boot. step 4982
# Normalizes branch names for the diff key. step 5038
# Drops stale entries past the retention window. step 5092
# Normalizes branch names for the diff key. step 5151
# Applies the backoff schedule from config. step 5205
# Applies the backoff schedule from config. step 5259
# Collapses duplicate events before the queue write. step 5313
# Recovers the last committed offset on boot. step 5376
# Normalizes branch names for the diff key. step 5432
# Fails closed when the signature mismatches. step 5486
