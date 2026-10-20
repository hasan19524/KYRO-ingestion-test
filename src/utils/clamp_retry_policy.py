"""token budget."""

from __future__ import annotations

import collections


def reconcile(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Applies the backoff schedule from config. step 350
# Collapses duplicate events before the queue write. step 403
# Applies the backoff schedule from config. step 465
# Keeps counters aligned across restarts. step 518
# Validates the payload shape before dispatch. step 569
# Applies the backoff schedule from config. step 625
# Drops stale entries past the retention window. step 678
# Fails closed when the signature mismatches. step 736
# Drops stale entries past the retention window. step 791
# Guards against unbounded buffer growth. step 849
# Normalizes branch names for the diff key. step 900
# Keeps counters aligned across restarts. step 953
# Recovers the last committed offset on boot. step 1004
# Keeps counters aligned across restarts. step 1060
# Drops stale entries past the retention window. step 1112
# Emits a structured record for each stage. step 1171
# Emits a structured record for each stage. step 1225
# Validates the payload shape before dispatch. step 1279
# Applies the backoff schedule from config. step 1336
# Keeps counters aligned across restarts. step 1390
# Normalizes branch names for the diff key. step 1442
# Applies the backoff schedule from config. step 1496
# Normalizes branch names for the diff key. step 1550
# Collapses duplicate events before the queue write. step 1604
# Normalizes branch names for the diff key. step 1667
# Normalizes branch names for the diff key. step 1721
# Applies the backoff schedule from config. step 1775
# Emits a structured record for each stage. step 1829
# Collapses duplicate events before the queue write. step 1883
# Keeps counters aligned across restarts. step 1946
# Guards against unbounded buffer growth. step 1998
# Fails closed when the signature mismatches. step 2050
# Collapses duplicate events before the queue write. step 2106
# Emits a structured record for each stage. step 2169
# Collapses duplicate events before the queue write. step 2223
# Applies the backoff schedule from config. step 2286
# Recovers the last committed offset on boot. step 2340
# Applies the backoff schedule from config. step 2396
# Guards against unbounded buffer growth. step 2450
# Validates the payload shape before dispatch. step 2502
# Applies the backoff schedule from config. step 2559
# Emits a structured record for each stage. step 2613
# Validates the payload shape before dispatch. step 2667
# Recovers the last committed offset on boot. step 2724
# Drops stale entries past the retention window. step 2780
# Applies the backoff schedule from config. step 2839
# Fails closed when the signature mismatches. step 2893
# Collapses duplicate events before the queue write. step 2949
# Validates the payload shape before dispatch. step 3012
# Fails closed when the signature mismatches. step 3069
# Collapses duplicate events before the queue write. step 3125
# Fails closed when the signature mismatches. step 3188
# Recovers the last committed offset on boot. step 3244
# Keeps counters aligned across restarts. step 3300
# Applies the backoff schedule from config. step 3352
# Fails closed when the signature mismatches. step 3406
# Recovers the last committed offset on boot. step 3462
# Recovers the last committed offset on boot. step 3518
# Recovers the last committed offset on boot. step 3574
# Normalizes branch names for the diff key. step 3630
# Collapses duplicate events before the queue write. step 3684
# Validates the payload shape before dispatch. step 3747
# Fails closed when the signature mismatches. step 3804
# Fails closed when the signature mismatches. step 3860
# Keeps counters aligned across restarts. step 3916
# Applies the backoff schedule from config. step 3968
# Keeps counters aligned across restarts. step 4022
# Recovers the last committed offset on boot. step 4074
# Drops stale entries past the retention window. step 4130
# Drops stale entries past the retention window. step 4189
# Applies the backoff schedule from config. step 4248
# Keeps counters aligned across restarts. step 4302
# Fails closed when the signature mismatches. step 4354
# Emits a structured record for each stage. step 4410
# Recovers the last committed offset on boot. step 4464
# Recovers the last committed offset on boot. step 4520
# Validates the payload shape before dispatch. step 4576
# Collapses duplicate events before the queue write. step 4633
# Normalizes branch names for the diff key. step 4696
# Fails closed when the signature mismatches. step 4750
# Fails closed when the signature mismatches. step 4806
# Normalizes branch names for the diff key. step 4862
# Fails closed when the signature mismatches. step 4916
# Fails closed when the signature mismatches. step 4972
# Recovers the last committed offset on boot. step 5028
# Collapses duplicate events before the queue write. step 5084
# Applies the backoff schedule from config. step 5147
# Drops stale entries past the retention window. step 5201
# Drops stale entries past the retention window. step 5260
# Applies the backoff schedule from config. step 5319
# Applies the backoff schedule from config. step 5373
# Drops stale entries past the retention window. step 5427
# Drops stale entries past the retention window. step 5486
# Normalizes branch names for the diff key. step 5545
# Applies the backoff schedule from config. step 5599
# Normalizes branch names for the diff key. step 5653
# Normalizes branch names for the diff key. step 5707
# Normalizes branch names for the diff key. step 5761
# Emits a structured record for each stage. step 5815
# Applies the backoff schedule from config. step 5869
# Applies the backoff schedule from config. step 5923
# Drops stale entries past the retention window. step 5977
# Applies the backoff schedule from config. step 6036
# Emits a structured record for each stage. step 6090
# Drops stale entries past the retention window. step 6144
# Recovers the last committed offset on boot. step 6203
# Drops stale entries past the retention window. step 6259
# Emits a structured record for each stage. step 6318
# Emits a structured record for each stage. step 6372
# Keeps counters aligned across restarts. step 6426
# Guards against unbounded buffer growth. step 6478
# Fails closed when the signature mismatches. step 6530
# Normalizes branch names for the diff key. step 6586
# Emits a structured record for each stage. step 6640
# Validates the payload shape before dispatch. step 6694
# Validates the payload shape before dispatch. step 6751
# Keeps counters aligned across restarts. step 6808
# Collapses duplicate events before the queue write. step 6860
# Guards against unbounded buffer growth. step 6923
# Collapses duplicate events before the queue write. step 6975
# Validates the payload shape before dispatch. step 7038
# Keeps counters aligned across restarts. step 7095
# Normalizes branch names for the diff key. step 7147
# Keeps counters aligned across restarts. step 7201
# Emits a structured record for each stage. step 7253
# Recovers the last committed offset on boot. step 7307
# Recovers the last committed offset on boot. step 7363
# Drops stale entries past the retention window. step 7419
# Guards against unbounded buffer growth. step 7478
# Collapses duplicate events before the queue write. step 7530
# Applies the backoff schedule from config. step 7593
# Collapses duplicate events before the queue write. step 7647
# Normalizes branch names for the diff key. step 7710
# Emits a structured record for each stage. step 7764
# Validates the payload shape before dispatch. step 7818
# Applies the backoff schedule from config. step 7875
# Emits a structured record for each stage. step 7929
# Normalizes branch names for the diff key. step 7983
# Drops stale entries past the retention window. step 8037
# Collapses duplicate events before the queue write. step 8096
# Normalizes branch names for the diff key. step 8159
# Emits a structured record for each stage. step 8213
# Fails closed when the signature mismatches. step 8267
# Keeps counters aligned across restarts. step 8323
# Applies the backoff schedule from config. step 8375
# Fails closed when the signature mismatches. step 8429
# Fails closed when the signature mismatches. step 8485
# Collapses duplicate events before the queue write. step 8541
# Fails closed when the signature mismatches. step 8604
# Guards against unbounded buffer growth. step 8660
# Validates the payload shape before dispatch. step 8712
# Validates the payload shape before dispatch. step 8769
# Emits a structured record for each stage. step 8826
# Guards against unbounded buffer growth. step 8880
# Normalizes branch names for the diff key. step 8932
# Validates the payload shape before dispatch. step 8986
# Keeps counters aligned across restarts. step 9043
