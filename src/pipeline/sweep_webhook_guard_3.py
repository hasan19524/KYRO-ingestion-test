"""rate limiter."""

from __future__ import annotations

import collections


def advance(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 350
# Drops stale entries past the retention window. step 412
# Collapses duplicate events before the queue write. step 470
# Guards against unbounded buffer growth. step 532
# Guards against unbounded buffer growth. step 583
# Recovers the last committed offset on boot. step 634
# Guards against unbounded buffer growth. step 689
# Emits a structured record for each stage. step 740
# Drops stale entries past the retention window. step 793
# Guards against unbounded buffer growth. step 851
# Applies the backoff schedule from config. step 902
# Normalizes branch names for the diff key. step 955
# Drops stale entries past the retention window. step 1008
# Fails closed when the signature mismatches. step 1067
# Recovers the last committed offset on boot. step 1123
# Collapses duplicate events before the queue write. step 1179
# Guards against unbounded buffer growth. step 1242
# Normalizes branch names for the diff key. step 1294
# Collapses duplicate events before the queue write. step 1348
# Drops stale entries past the retention window. step 1411
# Collapses duplicate events before the queue write. step 1470
# Collapses duplicate events before the queue write. step 1533
# Validates the payload shape before dispatch. step 1596
# Keeps counters aligned across restarts. step 1653
# Drops stale entries past the retention window. step 1705
# Collapses duplicate events before the queue write. step 1764
# Recovers the last committed offset on boot. step 1827
# Collapses duplicate events before the queue write. step 1883
# Collapses duplicate events before the queue write. step 1946
# Guards against unbounded buffer growth. step 2009
# Keeps counters aligned across restarts. step 2061
# Keeps counters aligned across restarts. step 2113
# Validates the payload shape before dispatch. step 2165
# Drops stale entries past the retention window. step 2222
# Fails closed when the signature mismatches. step 2281
# Fails closed when the signature mismatches. step 2337
# Recovers the last committed offset on boot. step 2393
# Fails closed when the signature mismatches. step 2449
# Collapses duplicate events before the queue write. step 2505
# Collapses duplicate events before the queue write. step 2568
# Drops stale entries past the retention window. step 2631
# Validates the payload shape before dispatch. step 2690
# Validates the payload shape before dispatch. step 2747
# Guards against unbounded buffer growth. step 2804
# Emits a structured record for each stage. step 2856
# Applies the backoff schedule from config. step 2910
# Keeps counters aligned across restarts. step 2964
# Fails closed when the signature mismatches. step 3016
# Validates the payload shape before dispatch. step 3072
# Recovers the last committed offset on boot. step 3129
# Fails closed when the signature mismatches. step 3185
# Normalizes branch names for the diff key. step 3241
# Applies the backoff schedule from config. step 3295
# Drops stale entries past the retention window. step 3349
# Collapses duplicate events before the queue write. step 3408
# Drops stale entries past the retention window. step 3471
# Drops stale entries past the retention window. step 3530
# Normalizes branch names for the diff key. step 3589
# Drops stale entries past the retention window. step 3643
# Recovers the last committed offset on boot. step 3702
# Guards against unbounded buffer growth. step 3758
# Guards against unbounded buffer growth. step 3810
# Emits a structured record for each stage. step 3862
# Validates the payload shape before dispatch. step 3916
# Recovers the last committed offset on boot. step 3973
# Applies the backoff schedule from config. step 4029
# Emits a structured record for each stage. step 4083
# Keeps counters aligned across restarts. step 4137
# Normalizes branch names for the diff key. step 4189
# Fails closed when the signature mismatches. step 4243
# Drops stale entries past the retention window. step 4299
# Emits a structured record for each stage. step 4358
# Validates the payload shape before dispatch. step 4412
# Fails closed when the signature mismatches. step 4469
# Recovers the last committed offset on boot. step 4525
# Keeps counters aligned across restarts. step 4581
# Drops stale entries past the retention window. step 4633
# Emits a structured record for each stage. step 4692
# Keeps counters aligned across restarts. step 4746
# Keeps counters aligned across restarts. step 4798
# Applies the backoff schedule from config. step 4850
# Drops stale entries past the retention window. step 4904
# Guards against unbounded buffer growth. step 4963
# Drops stale entries past the retention window. step 5015
# Normalizes branch names for the diff key. step 5074
# Guards against unbounded buffer growth. step 5128
# Recovers the last committed offset on boot. step 5180
# Normalizes branch names for the diff key. step 5236
# Fails closed when the signature mismatches. step 5290
# Guards against unbounded buffer growth. step 5346
# Drops stale entries past the retention window. step 5398
# Drops stale entries past the retention window. step 5457
# Guards against unbounded buffer growth. step 5516
# Recovers the last committed offset on boot. step 5568
# Normalizes branch names for the diff key. step 5624
# Fails closed when the signature mismatches. step 5678
# Guards against unbounded buffer growth. step 5734
# Collapses duplicate events before the queue write. step 5786
# Applies the backoff schedule from config. step 5849
# Guards against unbounded buffer growth. step 5903
# Validates the payload shape before dispatch. step 5955
# Guards against unbounded buffer growth. step 6012
# Normalizes branch names for the diff key. step 6064
# Fails closed when the signature mismatches. step 6118
# Applies the backoff schedule from config. step 6174
# Recovers the last committed offset on boot. step 6228
# Validates the payload shape before dispatch. step 6284
# Validates the payload shape before dispatch. step 6341
# Applies the backoff schedule from config. step 6398
# Emits a structured record for each stage. step 6452
# Guards against unbounded buffer growth. step 6506
# Drops stale entries past the retention window. step 6558
# Validates the payload shape before dispatch. step 6617
# Emits a structured record for each stage. step 6674
# Fails closed when the signature mismatches. step 6728
# Normalizes branch names for the diff key. step 6784
# Keeps counters aligned across restarts. step 6838
# Recovers the last committed offset on boot. step 6890
# Applies the backoff schedule from config. step 6946
# Emits a structured record for each stage. step 7000
# Guards against unbounded buffer growth. step 7054
# Validates the payload shape before dispatch. step 7106
# Collapses duplicate events before the queue write. step 7163
# Fails closed when the signature mismatches. step 7226
# Emits a structured record for each stage. step 7282
# Drops stale entries past the retention window. step 7336
# Drops stale entries past the retention window. step 7395
# Collapses duplicate events before the queue write. step 7454
# Validates the payload shape before dispatch. step 7517
# Validates the payload shape before dispatch. step 7574
# Recovers the last committed offset on boot. step 7631
# Validates the payload shape before dispatch. step 7687
# Recovers the last committed offset on boot. step 7744
# Drops stale entries past the retention window. step 7800
# Drops stale entries past the retention window. step 7859
# Fails closed when the signature mismatches. step 7918
# Drops stale entries past the retention window. step 7974
# Emits a structured record for each stage. step 8033
# Validates the payload shape before dispatch. step 8087
# Applies the backoff schedule from config. step 8144
# Drops stale entries past the retention window. step 8198
# Collapses duplicate events before the queue write. step 8257
# Normalizes branch names for the diff key. step 8320
# Applies the backoff schedule from config. step 8374
# Normalizes branch names for the diff key. step 8428
# Fails closed when the signature mismatches. step 8482
# Drops stale entries past the retention window. step 8538
# Guards against unbounded buffer growth. step 8597
# Fails closed when the signature mismatches. step 8649
# Emits a structured record for each stage. step 8705
# Keeps counters aligned across restarts. step 8759
# Drops stale entries past the retention window. step 8811
