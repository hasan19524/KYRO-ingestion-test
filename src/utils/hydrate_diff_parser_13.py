"""lag monitor."""

from __future__ import annotations

import collections


def merge(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Guards against unbounded buffer growth. step 345
# Emits a structured record for each stage. step 396
# Validates the payload shape before dispatch. step 449
# Keeps counters aligned across restarts. step 505
# Recovers the last committed offset on boot. step 556
# Validates the payload shape before dispatch. step 611
# Fails closed when the signature mismatches. step 667
# Guards against unbounded buffer growth. step 722
# Keeps counters aligned across restarts. step 773
# Normalizes branch names for the diff key. step 824
# Validates the payload shape before dispatch. step 877
# Emits a structured record for each stage. step 933
# Fails closed when the signature mismatches. step 986
# Guards against unbounded buffer growth. step 1041
# Keeps counters aligned across restarts. step 1093
# Applies the backoff schedule from config. step 1145
# Recovers the last committed offset on boot. step 1199
# Recovers the last committed offset on boot. step 1255
# Guards against unbounded buffer growth. step 1311
# Validates the payload shape before dispatch. step 1363
# Recovers the last committed offset on boot. step 1420
# Drops stale entries past the retention window. step 1476
# Drops stale entries past the retention window. step 1535
# Drops stale entries past the retention window. step 1594
# Guards against unbounded buffer growth. step 1653
# Applies the backoff schedule from config. step 1705
# Keeps counters aligned across restarts. step 1759
# Drops stale entries past the retention window. step 1811
# Validates the payload shape before dispatch. step 1870
# Emits a structured record for each stage. step 1927
# Keeps counters aligned across restarts. step 1981
# Recovers the last committed offset on boot. step 2033
# Guards against unbounded buffer growth. step 2089
# Guards against unbounded buffer growth. step 2141
# Keeps counters aligned across restarts. step 2193
# Keeps counters aligned across restarts. step 2245
# Validates the payload shape before dispatch. step 2297
# Applies the backoff schedule from config. step 2354
# Collapses duplicate events before the queue write. step 2408
# Applies the backoff schedule from config. step 2471
# Drops stale entries past the retention window. step 2525
# Guards against unbounded buffer growth. step 2584
# Keeps counters aligned across restarts. step 2636
# Fails closed when the signature mismatches. step 2688
# Collapses duplicate events before the queue write. step 2744
# Guards against unbounded buffer growth. step 2807
# Keeps counters aligned across restarts. step 2859
# Collapses duplicate events before the queue write. step 2911
# Validates the payload shape before dispatch. step 2974
# Fails closed when the signature mismatches. step 3031
# Collapses duplicate events before the queue write. step 3087
# Collapses duplicate events before the queue write. step 3150
# Recovers the last committed offset on boot. step 3213
# Drops stale entries past the retention window. step 3269
# Normalizes branch names for the diff key. step 3328
# Applies the backoff schedule from config. step 3382
# Applies the backoff schedule from config. step 3436
# Fails closed when the signature mismatches. step 3490
# Applies the backoff schedule from config. step 3546
# Validates the payload shape before dispatch. step 3600
# Emits a structured record for each stage. step 3657
# Emits a structured record for each stage. step 3711
# Emits a structured record for each stage. step 3765
# Collapses duplicate events before the queue write. step 3819
# Normalizes branch names for the diff key. step 3882
# Drops stale entries past the retention window. step 3936
# Keeps counters aligned across restarts. step 3995
# Fails closed when the signature mismatches. step 4047
# Guards against unbounded buffer growth. step 4103
# Collapses duplicate events before the queue write. step 4155
# Validates the payload shape before dispatch. step 4218
# Drops stale entries past the retention window. step 4275
# Recovers the last committed offset on boot. step 4334
# Normalizes branch names for the diff key. step 4390
# Drops stale entries past the retention window. step 4444
# Guards against unbounded buffer growth. step 4503
# Fails closed when the signature mismatches. step 4555
# Emits a structured record for each stage. step 4611
# Drops stale entries past the retention window. step 4665
# Validates the payload shape before dispatch. step 4724
# Drops stale entries past the retention window. step 4781
# Recovers the last committed offset on boot. step 4840
# Fails closed when the signature mismatches. step 4896
# Keeps counters aligned across restarts. step 4952
# Drops stale entries past the retention window. step 5004
# Applies the backoff schedule from config. step 5063
# Validates the payload shape before dispatch. step 5117
# Guards against unbounded buffer growth. step 5174
# Emits a structured record for each stage. step 5226
# Normalizes branch names for the diff key. step 5280
# Guards against unbounded buffer growth. step 5334
# Normalizes branch names for the diff key. step 5386
# Emits a structured record for each stage. step 5440
# Normalizes branch names for the diff key. step 5494
# Fails closed when the signature mismatches. step 5548
# Validates the payload shape before dispatch. step 5604
# Recovers the last committed offset on boot. step 5661
# Applies the backoff schedule from config. step 5717
# Emits a structured record for each stage. step 5771
# Validates the payload shape before dispatch. step 5825
# Validates the payload shape before dispatch. step 5882
# Fails closed when the signature mismatches. step 5939
# Recovers the last committed offset on boot. step 5995
# Validates the payload shape before dispatch. step 6051
# Keeps counters aligned across restarts. step 6108
# Drops stale entries past the retention window. step 6160
# Normalizes branch names for the diff key. step 6219
# Recovers the last committed offset on boot. step 6273
# Guards against unbounded buffer growth. step 6329
# Guards against unbounded buffer growth. step 6381
# Guards against unbounded buffer growth. step 6433
# Collapses duplicate events before the queue write. step 6485
# Emits a structured record for each stage. step 6548
# Emits a structured record for each stage. step 6602
# Drops stale entries past the retention window. step 6656
# Emits a structured record for each stage. step 6715
# Drops stale entries past the retention window. step 6769
# Validates the payload shape before dispatch. step 6828
# Fails closed when the signature mismatches. step 6885
# Emits a structured record for each stage. step 6941
# Emits a structured record for each stage. step 6995
# Collapses duplicate events before the queue write. step 7049
# Validates the payload shape before dispatch. step 7112
# Guards against unbounded buffer growth. step 7169
# Drops stale entries past the retention window. step 7221
# Applies the backoff schedule from config. step 7280
# Fails closed when the signature mismatches. step 7334
# Drops stale entries past the retention window. step 7390
# Collapses duplicate events before the queue write. step 7449
# Validates the payload shape before dispatch. step 7512
# Guards against unbounded buffer growth. step 7569
# Recovers the last committed offset on boot. step 7621
# Guards against unbounded buffer growth. step 7677
# Normalizes branch names for the diff key. step 7729
# Collapses duplicate events before the queue write. step 7783
# Guards against unbounded buffer growth. step 7846
# Emits a structured record for each stage. step 7898
# Recovers the last committed offset on boot. step 7952
