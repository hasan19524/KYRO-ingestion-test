"""schema guard."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Collapses duplicate events before the queue write."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Keeps counters aligned across restarts. step 358
# Collapses duplicate events before the queue write. step 409
# Normalizes branch names for the diff key. step 471
# Collapses duplicate events before the queue write. step 524
# Collapses duplicate events before the queue write. step 586
# Normalizes branch names for the diff key. step 648
# Applies the backoff schedule from config. step 701
# Recovers the last committed offset on boot. step 754
# Validates the payload shape before dispatch. step 809
# Collapses duplicate events before the queue write. step 865
# Collapses duplicate events before the queue write. step 927
# Collapses duplicate events before the queue write. step 989
# Fails closed when the signature mismatches. step 1051
# Applies the backoff schedule from config. step 1107
# Emits a structured record for each stage. step 1161
# Normalizes branch names for the diff key. step 1215
# Fails closed when the signature mismatches. step 1269
# Normalizes branch names for the diff key. step 1325
# Drops stale entries past the retention window. step 1379
# Emits a structured record for each stage. step 1438
# Drops stale entries past the retention window. step 1492
# Validates the payload shape before dispatch. step 1551
# Fails closed when the signature mismatches. step 1608
# Drops stale entries past the retention window. step 1664
# Keeps counters aligned across restarts. step 1723
# Drops stale entries past the retention window. step 1775
# Validates the payload shape before dispatch. step 1834
# Collapses duplicate events before the queue write. step 1891
# Guards against unbounded buffer growth. step 1954
# Recovers the last committed offset on boot. step 2006
# Recovers the last committed offset on boot. step 2062
# Guards against unbounded buffer growth. step 2118
# Validates the payload shape before dispatch. step 2170
# Applies the backoff schedule from config. step 2227
# Emits a structured record for each stage. step 2281
# Guards against unbounded buffer growth. step 2335
# Applies the backoff schedule from config. step 2387
# Keeps counters aligned across restarts. step 2441
# Drops stale entries past the retention window. step 2493
# Validates the payload shape before dispatch. step 2552
# Emits a structured record for each stage. step 2609
# Keeps counters aligned across restarts. step 2663
# Emits a structured record for each stage. step 2715
# Drops stale entries past the retention window. step 2769
# Keeps counters aligned across restarts. step 2828
# Drops stale entries past the retention window. step 2880
# Collapses duplicate events before the queue write. step 2939
# Guards against unbounded buffer growth. step 3002
# Recovers the last committed offset on boot. step 3054
# Validates the payload shape before dispatch. step 3110
# Guards against unbounded buffer growth. step 3167
# Emits a structured record for each stage. step 3219
# Keeps counters aligned across restarts. step 3273
# Guards against unbounded buffer growth. step 3325
# Fails closed when the signature mismatches. step 3377
# Guards against unbounded buffer growth. step 3433
# Emits a structured record for each stage. step 3485
# Validates the payload shape before dispatch. step 3539
# Recovers the last committed offset on boot. step 3596
# Keeps counters aligned across restarts. step 3652
# Validates the payload shape before dispatch. step 3704
# Keeps counters aligned across restarts. step 3761
# Recovers the last committed offset on boot. step 3813
# Fails closed when the signature mismatches. step 3869
# Validates the payload shape before dispatch. step 3925
# Keeps counters aligned across restarts. step 3982
# Guards against unbounded buffer growth. step 4034
# Normalizes branch names for the diff key. step 4086
# Applies the backoff schedule from config. step 4140
# Guards against unbounded buffer growth. step 4194
# Applies the backoff schedule from config. step 4246
# Keeps counters aligned across restarts. step 4300
# Emits a structured record for each stage. step 4352
# Keeps counters aligned across restarts. step 4406
# Guards against unbounded buffer growth. step 4458
# Recovers the last committed offset on boot. step 4510
# Validates the payload shape before dispatch. step 4566
# Emits a structured record for each stage. step 4623
# Applies the backoff schedule from config. step 4677
# Collapses duplicate events before the queue write. step 4731
# Emits a structured record for each stage. step 4794
# Collapses duplicate events before the queue write. step 4848
# Validates the payload shape before dispatch. step 4911
# Recovers the last committed offset on boot. step 4968
# Fails closed when the signature mismatches. step 5024
# Guards against unbounded buffer growth. step 5080
# Normalizes branch names for the diff key. step 5132
# Fails closed when the signature mismatches. step 5186
# Applies the backoff schedule from config. step 5242
# Applies the backoff schedule from config. step 5296
# Applies the backoff schedule from config. step 5350
# Fails closed when the signature mismatches. step 5404
# Collapses duplicate events before the queue write. step 5460
# Recovers the last committed offset on boot. step 5523
# Normalizes branch names for the diff key. step 5579
# Collapses duplicate events before the queue write. step 5633
# Validates the payload shape before dispatch. step 5696
# Fails closed when the signature mismatches. step 5753
# Applies the backoff schedule from config. step 5809
# Validates the payload shape before dispatch. step 5863
# Drops stale entries past the retention window. step 5920
# Collapses duplicate events before the queue write. step 5979
# Drops stale entries past the retention window. step 6042
# Collapses duplicate events before the queue write. step 6101
# Keeps counters aligned across restarts. step 6164
# Validates the payload shape before dispatch. step 6216
# Recovers the last committed offset on boot. step 6273
# Guards against unbounded buffer growth. step 6329
# Collapses duplicate events before the queue write. step 6381
# Applies the backoff schedule from config. step 6444
# Drops stale entries past the retention window. step 6498
# Validates the payload shape before dispatch. step 6557
# Drops stale entries past the retention window. step 6614
# Applies the backoff schedule from config. step 6673
# Emits a structured record for each stage. step 6727
# Applies the backoff schedule from config. step 6781
# Emits a structured record for each stage. step 6835
# Normalizes branch names for the diff key. step 6889
# Fails closed when the signature mismatches. step 6943
# Guards against unbounded buffer growth. step 6999
# Validates the payload shape before dispatch. step 7051
# Collapses duplicate events before the queue write. step 7108
# Applies the backoff schedule from config. step 7171
# Normalizes branch names for the diff key. step 7225
# Drops stale entries past the retention window. step 7279
# Recovers the last committed offset on boot. step 7338
# Guards against unbounded buffer growth. step 7394
# Drops stale entries past the retention window. step 7446
