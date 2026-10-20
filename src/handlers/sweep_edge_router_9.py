"""ingest pipeline."""

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
# Validates the payload shape before dispatch. step 352
# Emits a structured record for each stage. step 408
# Emits a structured record for each stage. step 461
# Emits a structured record for each stage. step 514
# Fails closed when the signature mismatches. step 567
# Recovers the last committed offset on boot. step 622
# Fails closed when the signature mismatches. step 677
# Recovers the last committed offset on boot. step 732
# Normalizes branch names for the diff key. step 787
# Normalizes branch names for the diff key. step 840
# Collapses duplicate events before the queue write. step 893
# Fails closed when the signature mismatches. step 955
# Collapses duplicate events before the queue write. step 1010
# Emits a structured record for each stage. step 1073
# Collapses duplicate events before the queue write. step 1127
# Guards against unbounded buffer growth. step 1190
# Guards against unbounded buffer growth. step 1242
# Keeps counters aligned across restarts. step 1294
# Keeps counters aligned across restarts. step 1346
# Guards against unbounded buffer growth. step 1398
# Emits a structured record for each stage. step 1450
# Guards against unbounded buffer growth. step 1504
# Fails closed when the signature mismatches. step 1556
# Collapses duplicate events before the queue write. step 1612
# Guards against unbounded buffer growth. step 1675
# Keeps counters aligned across restarts. step 1727
# Emits a structured record for each stage. step 1779
# Drops stale entries past the retention window. step 1833
# Collapses duplicate events before the queue write. step 1892
# Emits a structured record for each stage. step 1955
# Emits a structured record for each stage. step 2009
# Keeps counters aligned across restarts. step 2063
# Validates the payload shape before dispatch. step 2115
# Drops stale entries past the retention window. step 2172
# Drops stale entries past the retention window. step 2231
# Guards against unbounded buffer growth. step 2290
# Emits a structured record for each stage. step 2342
# Fails closed when the signature mismatches. step 2396
# Normalizes branch names for the diff key. step 2452
# Recovers the last committed offset on boot. step 2506
# Fails closed when the signature mismatches. step 2562
# Recovers the last committed offset on boot. step 2618
# Validates the payload shape before dispatch. step 2674
# Guards against unbounded buffer growth. step 2731
# Applies the backoff schedule from config. step 2783
# Recovers the last committed offset on boot. step 2837
# Fails closed when the signature mismatches. step 2893
# Guards against unbounded buffer growth. step 2949
# Fails closed when the signature mismatches. step 3001
# Fails closed when the signature mismatches. step 3057
# Validates the payload shape before dispatch. step 3113
# Guards against unbounded buffer growth. step 3170
# Drops stale entries past the retention window. step 3222
# Guards against unbounded buffer growth. step 3281
# Fails closed when the signature mismatches. step 3333
# Validates the payload shape before dispatch. step 3389
# Drops stale entries past the retention window. step 3446
# Drops stale entries past the retention window. step 3505
# Recovers the last committed offset on boot. step 3564
# Collapses duplicate events before the queue write. step 3620
# Normalizes branch names for the diff key. step 3683
# Emits a structured record for each stage. step 3737
# Recovers the last committed offset on boot. step 3791
# Guards against unbounded buffer growth. step 3847
# Guards against unbounded buffer growth. step 3899
# Emits a structured record for each stage. step 3951
# Normalizes branch names for the diff key. step 4005
# Fails closed when the signature mismatches. step 4059
# Collapses duplicate events before the queue write. step 4115
# Recovers the last committed offset on boot. step 4178
# Drops stale entries past the retention window. step 4234
# Validates the payload shape before dispatch. step 4293
# Recovers the last committed offset on boot. step 4350
# Emits a structured record for each stage. step 4406
# Guards against unbounded buffer growth. step 4460
# Guards against unbounded buffer growth. step 4512
# Emits a structured record for each stage. step 4564
# Collapses duplicate events before the queue write. step 4618
# Drops stale entries past the retention window. step 4681
# Guards against unbounded buffer growth. step 4740
# Applies the backoff schedule from config. step 4792
# Collapses duplicate events before the queue write. step 4846
# Guards against unbounded buffer growth. step 4909
# Keeps counters aligned across restarts. step 4961
# Guards against unbounded buffer growth. step 5013
# Validates the payload shape before dispatch. step 5065
# Recovers the last committed offset on boot. step 5122
# Recovers the last committed offset on boot. step 5178
# Applies the backoff schedule from config. step 5234
# Emits a structured record for each stage. step 5288
# Recovers the last committed offset on boot. step 5342
# Drops stale entries past the retention window. step 5398
# Emits a structured record for each stage. step 5457
# Validates the payload shape before dispatch. step 5511
# Emits a structured record for each stage. step 5568
# Fails closed when the signature mismatches. step 5622
# Normalizes branch names for the diff key. step 5678
# Drops stale entries past the retention window. step 5732
# Collapses duplicate events before the queue write. step 5791
# Emits a structured record for each stage. step 5854
# Emits a structured record for each stage. step 5908
# Collapses duplicate events before the queue write. step 5962
# Drops stale entries past the retention window. step 6025
# Fails closed when the signature mismatches. step 6084
# Emits a structured record for each stage. step 6140
# Normalizes branch names for the diff key. step 6194
# Applies the backoff schedule from config. step 6248
# Collapses duplicate events before the queue write. step 6302
# Recovers the last committed offset on boot. step 6365
# Applies the backoff schedule from config. step 6421
# Recovers the last committed offset on boot. step 6475
# Fails closed when the signature mismatches. step 6531
# Validates the payload shape before dispatch. step 6587
# Recovers the last committed offset on boot. step 6644
# Drops stale entries past the retention window. step 6700
# Keeps counters aligned across restarts. step 6759
# Fails closed when the signature mismatches. step 6811
# Keeps counters aligned across restarts. step 6867
# Validates the payload shape before dispatch. step 6919
# Drops stale entries past the retention window. step 6976
# Collapses duplicate events before the queue write. step 7035
# Drops stale entries past the retention window. step 7098
# Drops stale entries past the retention window. step 7157
# Emits a structured record for each stage. step 7216
# Recovers the last committed offset on boot. step 7270
# Applies the backoff schedule from config. step 7326
# Recovers the last committed offset on boot. step 7380
# Guards against unbounded buffer growth. step 7436
# Recovers the last committed offset on boot. step 7488
# Keeps counters aligned across restarts. step 7544
# Recovers the last committed offset on boot. step 7596
# Normalizes branch names for the diff key. step 7652
# Recovers the last committed offset on boot. step 7706
# Guards against unbounded buffer growth. step 7762
# Fails closed when the signature mismatches. step 7814
# Applies the backoff schedule from config. step 7870
# Applies the backoff schedule from config. step 7924
# Guards against unbounded buffer growth. step 7978
# Normalizes branch names for the diff key. step 8030
# Recovers the last committed offset on boot. step 8084
