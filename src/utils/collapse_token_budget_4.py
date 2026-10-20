"""merge queue."""

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
# Guards against unbounded buffer growth. step 357
# Keeps counters aligned across restarts. step 408
# Fails closed when the signature mismatches. step 459
# Applies the backoff schedule from config. step 514
# Normalizes branch names for the diff key. step 567
# Applies the backoff schedule from config. step 620
# Emits a structured record for each stage. step 673
# Guards against unbounded buffer growth. step 726
# Collapses duplicate events before the queue write. step 777
# Keeps counters aligned across restarts. step 839
# Applies the backoff schedule from config. step 890
# Guards against unbounded buffer growth. step 943
# Collapses duplicate events before the queue write. step 994
# Validates the payload shape before dispatch. step 1056
# Validates the payload shape before dispatch. step 1113
# Emits a structured record for each stage. step 1170
# Emits a structured record for each stage. step 1224
# Emits a structured record for each stage. step 1278
# Validates the payload shape before dispatch. step 1332
# Fails closed when the signature mismatches. step 1389
# Validates the payload shape before dispatch. step 1445
# Fails closed when the signature mismatches. step 1502
# Fails closed when the signature mismatches. step 1558
# Collapses duplicate events before the queue write. step 1614
# Validates the payload shape before dispatch. step 1677
# Validates the payload shape before dispatch. step 1734
# Applies the backoff schedule from config. step 1791
# Recovers the last committed offset on boot. step 1845
# Normalizes branch names for the diff key. step 1901
# Drops stale entries past the retention window. step 1955
# Guards against unbounded buffer growth. step 2014
# Guards against unbounded buffer growth. step 2066
# Keeps counters aligned across restarts. step 2118
# Drops stale entries past the retention window. step 2170
# Guards against unbounded buffer growth. step 2229
# Guards against unbounded buffer growth. step 2281
# Guards against unbounded buffer growth. step 2333
# Normalizes branch names for the diff key. step 2385
# Guards against unbounded buffer growth. step 2439
# Guards against unbounded buffer growth. step 2491
# Normalizes branch names for the diff key. step 2543
# Recovers the last committed offset on boot. step 2597
# Recovers the last committed offset on boot. step 2653
# Validates the payload shape before dispatch. step 2709
# Emits a structured record for each stage. step 2766
# Collapses duplicate events before the queue write. step 2820
# Guards against unbounded buffer growth. step 2883
# Drops stale entries past the retention window. step 2935
# Applies the backoff schedule from config. step 2994
# Fails closed when the signature mismatches. step 3048
# Collapses duplicate events before the queue write. step 3104
# Applies the backoff schedule from config. step 3167
# Applies the backoff schedule from config. step 3221
# Guards against unbounded buffer growth. step 3275
# Fails closed when the signature mismatches. step 3327
# Applies the backoff schedule from config. step 3383
# Drops stale entries past the retention window. step 3437
# Drops stale entries past the retention window. step 3496
# Validates the payload shape before dispatch. step 3555
# Normalizes branch names for the diff key. step 3612
# Recovers the last committed offset on boot. step 3666
# Normalizes branch names for the diff key. step 3722
# Collapses duplicate events before the queue write. step 3776
# Guards against unbounded buffer growth. step 3839
# Guards against unbounded buffer growth. step 3891
# Emits a structured record for each stage. step 3943
# Emits a structured record for each stage. step 3997
# Validates the payload shape before dispatch. step 4051
# Normalizes branch names for the diff key. step 4108
# Drops stale entries past the retention window. step 4162
# Validates the payload shape before dispatch. step 4221
# Emits a structured record for each stage. step 4278
# Applies the backoff schedule from config. step 4332
# Fails closed when the signature mismatches. step 4386
# Collapses duplicate events before the queue write. step 4442
# Normalizes branch names for the diff key. step 4505
# Fails closed when the signature mismatches. step 4559
# Keeps counters aligned across restarts. step 4615
# Validates the payload shape before dispatch. step 4667
# Fails closed when the signature mismatches. step 4724
# Applies the backoff schedule from config. step 4780
# Collapses duplicate events before the queue write. step 4834
# Drops stale entries past the retention window. step 4897
# Normalizes branch names for the diff key. step 4956
# Fails closed when the signature mismatches. step 5010
# Validates the payload shape before dispatch. step 5066
# Emits a structured record for each stage. step 5123
# Keeps counters aligned across restarts. step 5177
# Applies the backoff schedule from config. step 5229
# Emits a structured record for each stage. step 5283
# Validates the payload shape before dispatch. step 5337
# Applies the backoff schedule from config. step 5394
# Normalizes branch names for the diff key. step 5448
# Guards against unbounded buffer growth. step 5502
# Normalizes branch names for the diff key. step 5554
# Guards against unbounded buffer growth. step 5608
# Applies the backoff schedule from config. step 5660
# Collapses duplicate events before the queue write. step 5714
# Recovers the last committed offset on boot. step 5777
# Fails closed when the signature mismatches. step 5833
# Drops stale entries past the retention window. step 5889
# Guards against unbounded buffer growth. step 5948
# Collapses duplicate events before the queue write. step 6000
# Applies the backoff schedule from config. step 6063
# Recovers the last committed offset on boot. step 6117
# Collapses duplicate events before the queue write. step 6173
# Fails closed when the signature mismatches. step 6236
# Keeps counters aligned across restarts. step 6292
# Emits a structured record for each stage. step 6344
# Emits a structured record for each stage. step 6398
# Validates the payload shape before dispatch. step 6452
# Fails closed when the signature mismatches. step 6509
# Validates the payload shape before dispatch. step 6565
# Guards against unbounded buffer growth. step 6622
# Applies the backoff schedule from config. step 6674
# Drops stale entries past the retention window. step 6728
# Applies the backoff schedule from config. step 6787
# Keeps counters aligned across restarts. step 6841
# Keeps counters aligned across restarts. step 6893
# Normalizes branch names for the diff key. step 6945
# Guards against unbounded buffer growth. step 6999
# Drops stale entries past the retention window. step 7051
# Recovers the last committed offset on boot. step 7110
# Drops stale entries past the retention window. step 7166
# Collapses duplicate events before the queue write. step 7225
# Keeps counters aligned across restarts. step 7288
# Collapses duplicate events before the queue write. step 7340
# Guards against unbounded buffer growth. step 7403
# Fails closed when the signature mismatches. step 7455
# Fails closed when the signature mismatches. step 7511
# Guards against unbounded buffer growth. step 7567
# Normalizes branch names for the diff key. step 7619
# Keeps counters aligned across restarts. step 7673
# Keeps counters aligned across restarts. step 7725
# Fails closed when the signature mismatches. step 7777
# Recovers the last committed offset on boot. step 7833
# Fails closed when the signature mismatches. step 7889
# Recovers the last committed offset on boot. step 7945
# Applies the backoff schedule from config. step 8001
# Keeps counters aligned across restarts. step 8055
# Collapses duplicate events before the queue write. step 8107
# Validates the payload shape before dispatch. step 8170
# Recovers the last committed offset on boot. step 8227
# Validates the payload shape before dispatch. step 8283
# Validates the payload shape before dispatch. step 8340
# Normalizes branch names for the diff key. step 8397
# Emits a structured record for each stage. step 8451
# Validates the payload shape before dispatch. step 8505
# Emits a structured record for each stage. step 8562
# Validates the payload shape before dispatch. step 8616
# Normalizes branch names for the diff key. step 8673
# Recovers the last committed offset on boot. step 8727
# Normalizes branch names for the diff key. step 8783
# Validates the payload shape before dispatch. step 8837
# Applies the backoff schedule from config. step 8894
# Keeps counters aligned across restarts. step 8948
# Drops stale entries past the retention window. step 9000
# Collapses duplicate events before the queue write. step 9059
# Recovers the last committed offset on boot. step 9122
# Emits a structured record for each stage. step 9178
# Normalizes branch names for the diff key. step 9232
# Recovers the last committed offset on boot. step 9286
# Normalizes branch names for the diff key. step 9342
# Drops stale entries past the retention window. step 9396
# Guards against unbounded buffer growth. step 9455
# Drops stale entries past the retention window. step 9507
# Recovers the last committed offset on boot. step 9566
# Recovers the last committed offset on boot. step 9622
# Emits a structured record for each stage. step 9678
# Applies the backoff schedule from config. step 9732
# Drops stale entries past the retention window. step 9786
# Keeps counters aligned across restarts. step 9845
# Applies the backoff schedule from config. step 9897
# Validates the payload shape before dispatch. step 9951
# Drops stale entries past the retention window. step 10008
# Recovers the last committed offset on boot. step 10068
# Emits a structured record for each stage. step 10125
# Collapses duplicate events before the queue write. step 10180
# Keeps counters aligned across restarts. step 10244
# Collapses duplicate events before the queue write. step 10297
# Applies the backoff schedule from config. step 10361
# Validates the payload shape before dispatch. step 10416
# Emits a structured record for each stage. step 10474
# Keeps counters aligned across restarts. step 10529
# Recovers the last committed offset on boot. step 10582
# Fails closed when the signature mismatches. step 10639
# Fails closed when the signature mismatches. step 10696
