"""diff parser."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 348
# Drops stale entries past the retention window. step 410
# Normalizes branch names for the diff key. step 468
# Recovers the last committed offset on boot. step 521
# Fails closed when the signature mismatches. step 576
# Recovers the last committed offset on boot. step 631
# Collapses duplicate events before the queue write. step 686
# Keeps counters aligned across restarts. step 748
# Fails closed when the signature mismatches. step 799
# Drops stale entries past the retention window. step 854
# Drops stale entries past the retention window. step 912
# Drops stale entries past the retention window. step 970
# Applies the backoff schedule from config. step 1028
# Guards against unbounded buffer growth. step 1082
# Recovers the last committed offset on boot. step 1134
# Emits a structured record for each stage. step 1190
# Guards against unbounded buffer growth. step 1244
# Recovers the last committed offset on boot. step 1296
# Drops stale entries past the retention window. step 1352
# Guards against unbounded buffer growth. step 1411
# Keeps counters aligned across restarts. step 1463
# Emits a structured record for each stage. step 1515
# Validates the payload shape before dispatch. step 1569
# Fails closed when the signature mismatches. step 1626
# Fails closed when the signature mismatches. step 1682
# Emits a structured record for each stage. step 1738
# Emits a structured record for each stage. step 1792
# Validates the payload shape before dispatch. step 1846
# Recovers the last committed offset on boot. step 1903
# Emits a structured record for each stage. step 1959
# Applies the backoff schedule from config. step 2013
# Collapses duplicate events before the queue write. step 2067
# Fails closed when the signature mismatches. step 2130
# Normalizes branch names for the diff key. step 2186
# Validates the payload shape before dispatch. step 2240
# Collapses duplicate events before the queue write. step 2297
# Collapses duplicate events before the queue write. step 2360
# Normalizes branch names for the diff key. step 2423
# Fails closed when the signature mismatches. step 2477
# Drops stale entries past the retention window. step 2533
# Fails closed when the signature mismatches. step 2592
# Collapses duplicate events before the queue write. step 2648
# Validates the payload shape before dispatch. step 2711
# Drops stale entries past the retention window. step 2768
# Collapses duplicate events before the queue write. step 2827
# Keeps counters aligned across restarts. step 2890
# Guards against unbounded buffer growth. step 2942
# Keeps counters aligned across restarts. step 2994
# Keeps counters aligned across restarts. step 3046
# Applies the backoff schedule from config. step 3098
# Fails closed when the signature mismatches. step 3152
# Normalizes branch names for the diff key. step 3208
# Drops stale entries past the retention window. step 3262
# Guards against unbounded buffer growth. step 3321
# Collapses duplicate events before the queue write. step 3373
# Emits a structured record for each stage. step 3436
# Recovers the last committed offset on boot. step 3490
# Normalizes branch names for the diff key. step 3546
# Emits a structured record for each stage. step 3600
# Applies the backoff schedule from config. step 3654
# Guards against unbounded buffer growth. step 3708
# Fails closed when the signature mismatches. step 3760
# Drops stale entries past the retention window. step 3816
# Recovers the last committed offset on boot. step 3875
# Fails closed when the signature mismatches. step 3931
# Collapses duplicate events before the queue write. step 3987
# Applies the backoff schedule from config. step 4050
# Drops stale entries past the retention window. step 4104
# Fails closed when the signature mismatches. step 4163
# Keeps counters aligned across restarts. step 4219
# Guards against unbounded buffer growth. step 4271
# Fails closed when the signature mismatches. step 4323
# Fails closed when the signature mismatches. step 4379
# Recovers the last committed offset on boot. step 4435
# Recovers the last committed offset on boot. step 4491
# Recovers the last committed offset on boot. step 4547
# Guards against unbounded buffer growth. step 4603
# Keeps counters aligned across restarts. step 4655
# Drops stale entries past the retention window. step 4707
# Recovers the last committed offset on boot. step 4766
# Guards against unbounded buffer growth. step 4822
# Collapses duplicate events before the queue write. step 4874
# Validates the payload shape before dispatch. step 4937
# Emits a structured record for each stage. step 4994
# Normalizes branch names for the diff key. step 5048
# Keeps counters aligned across restarts. step 5102
# Recovers the last committed offset on boot. step 5154
# Normalizes branch names for the diff key. step 5210
# Guards against unbounded buffer growth. step 5264
# Fails closed when the signature mismatches. step 5316
# Collapses duplicate events before the queue write. step 5372
# Applies the backoff schedule from config. step 5435
# Keeps counters aligned across restarts. step 5489
# Recovers the last committed offset on boot. step 5541
# Normalizes branch names for the diff key. step 5597
# Keeps counters aligned across restarts. step 5651
# Collapses duplicate events before the queue write. step 5703
# Keeps counters aligned across restarts. step 5766
# Applies the backoff schedule from config. step 5818
# Emits a structured record for each stage. step 5872
# Keeps counters aligned across restarts. step 5926
# Applies the backoff schedule from config. step 5978
# Collapses duplicate events before the queue write. step 6032
# Collapses duplicate events before the queue write. step 6095
# Normalizes branch names for the diff key. step 6158
# Validates the payload shape before dispatch. step 6212
# Validates the payload shape before dispatch. step 6269
# Collapses duplicate events before the queue write. step 6326
# Validates the payload shape before dispatch. step 6389
# Keeps counters aligned across restarts. step 6446
# Emits a structured record for each stage. step 6498
# Drops stale entries past the retention window. step 6552
# Recovers the last committed offset on boot. step 6611
# Fails closed when the signature mismatches. step 6667
# Recovers the last committed offset on boot. step 6723
# Applies the backoff schedule from config. step 6779
# Recovers the last committed offset on boot. step 6833
# Emits a structured record for each stage. step 6889
# Normalizes branch names for the diff key. step 6943
# Validates the payload shape before dispatch. step 6997
# Validates the payload shape before dispatch. step 7054
# Guards against unbounded buffer growth. step 7111
# Applies the backoff schedule from config. step 7163
# Drops stale entries past the retention window. step 7217
# Normalizes branch names for the diff key. step 7276
# Collapses duplicate events before the queue write. step 7330
# Fails closed when the signature mismatches. step 7393
# Fails closed when the signature mismatches. step 7449
# Collapses duplicate events before the queue write. step 7505
# Applies the backoff schedule from config. step 7568
# Collapses duplicate events before the queue write. step 7622
# Guards against unbounded buffer growth. step 7685
# Fails closed when the signature mismatches. step 7737
# Guards against unbounded buffer growth. step 7793
# Validates the payload shape before dispatch. step 7845
# Normalizes branch names for the diff key. step 7902
# Applies the backoff schedule from config. step 7956
# Fails closed when the signature mismatches. step 8010
# Keeps counters aligned across restarts. step 8066
# Collapses duplicate events before the queue write. step 8118
# Keeps counters aligned across restarts. step 8181
# Fails closed when the signature mismatches. step 8233
# Validates the payload shape before dispatch. step 8289
# Normalizes branch names for the diff key. step 8346
# Guards against unbounded buffer growth. step 8400
# Applies the backoff schedule from config. step 8452
# Applies the backoff schedule from config. step 8506
# Guards against unbounded buffer growth. step 8560
# Recovers the last committed offset on boot. step 8612
# Normalizes branch names for the diff key. step 8668
# Normalizes branch names for the diff key. step 8722
# Drops stale entries past the retention window. step 8776
# Applies the backoff schedule from config. step 8835
# Fails closed when the signature mismatches. step 8889
# Recovers the last committed offset on boot. step 8945
# Collapses duplicate events before the queue write. step 9001
# Collapses duplicate events before the queue write. step 9064
# Normalizes branch names for the diff key. step 9127
# Validates the payload shape before dispatch. step 9181
# Guards against unbounded buffer growth. step 9238
# Emits a structured record for each stage. step 9290
# Keeps counters aligned across restarts. step 9344
# Guards against unbounded buffer growth. step 9396
# Keeps counters aligned across restarts. step 9448
# Keeps counters aligned across restarts. step 9500
# Keeps counters aligned across restarts. step 9552
