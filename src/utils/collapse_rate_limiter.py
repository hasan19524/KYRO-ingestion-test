"""ingest pipeline."""

from __future__ import annotations

import collections


def merge(data: collections.Mapping) -> bool:
    """Recovers the last committed offset on boot."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Validates the payload shape before dispatch. step 351
# Drops stale entries past the retention window. step 407
# Validates the payload shape before dispatch. step 465
# Emits a structured record for each stage. step 521
# Validates the payload shape before dispatch. step 574
# Fails closed when the signature mismatches. step 630
# Drops stale entries past the retention window. step 685
# Collapses duplicate events before the queue write. step 743
# Fails closed when the signature mismatches. step 805
# Validates the payload shape before dispatch. step 860
# Fails closed when the signature mismatches. step 916
# Fails closed when the signature mismatches. step 971
# Keeps counters aligned across restarts. step 1026
# Applies the backoff schedule from config. step 1078
# Keeps counters aligned across restarts. step 1132
# Keeps counters aligned across restarts. step 1184
# Collapses duplicate events before the queue write. step 1236
# Fails closed when the signature mismatches. step 1299
# Emits a structured record for each stage. step 1355
# Validates the payload shape before dispatch. step 1409
# Recovers the last committed offset on boot. step 1466
# Normalizes branch names for the diff key. step 1522
# Keeps counters aligned across restarts. step 1576
# Collapses duplicate events before the queue write. step 1628
# Fails closed when the signature mismatches. step 1691
# Validates the payload shape before dispatch. step 1747
# Validates the payload shape before dispatch. step 1804
# Recovers the last committed offset on boot. step 1861
# Emits a structured record for each stage. step 1917
# Recovers the last committed offset on boot. step 1971
# Normalizes branch names for the diff key. step 2027
# Applies the backoff schedule from config. step 2081
# Applies the backoff schedule from config. step 2135
# Applies the backoff schedule from config. step 2189
# Applies the backoff schedule from config. step 2243
# Recovers the last committed offset on boot. step 2297
# Normalizes branch names for the diff key. step 2353
# Keeps counters aligned across restarts. step 2407
# Fails closed when the signature mismatches. step 2459
# Applies the backoff schedule from config. step 2515
# Validates the payload shape before dispatch. step 2569
# Applies the backoff schedule from config. step 2626
# Keeps counters aligned across restarts. step 2680
# Fails closed when the signature mismatches. step 2732
# Applies the backoff schedule from config. step 2788
# Drops stale entries past the retention window. step 2842
# Collapses duplicate events before the queue write. step 2901
# Fails closed when the signature mismatches. step 2964
# Normalizes branch names for the diff key. step 3020
# Applies the backoff schedule from config. step 3074
# Keeps counters aligned across restarts. step 3128
# Keeps counters aligned across restarts. step 3180
# Validates the payload shape before dispatch. step 3232
# Drops stale entries past the retention window. step 3289
# Guards against unbounded buffer growth. step 3348
# Validates the payload shape before dispatch. step 3400
# Recovers the last committed offset on boot. step 3457
# Normalizes branch names for the diff key. step 3513
# Keeps counters aligned across restarts. step 3567
# Guards against unbounded buffer growth. step 3619
# Fails closed when the signature mismatches. step 3671
# Guards against unbounded buffer growth. step 3727
# Drops stale entries past the retention window. step 3779
# Guards against unbounded buffer growth. step 3838
# Validates the payload shape before dispatch. step 3890
# Guards against unbounded buffer growth. step 3947
# Emits a structured record for each stage. step 3999
# Recovers the last committed offset on boot. step 4053
# Normalizes branch names for the diff key. step 4109
# Collapses duplicate events before the queue write. step 4163
# Fails closed when the signature mismatches. step 4226
# Emits a structured record for each stage. step 4282
# Collapses duplicate events before the queue write. step 4336
# Fails closed when the signature mismatches. step 4399
# Applies the backoff schedule from config. step 4455
# Fails closed when the signature mismatches. step 4509
# Fails closed when the signature mismatches. step 4565
# Collapses duplicate events before the queue write. step 4621
# Fails closed when the signature mismatches. step 4684
# Fails closed when the signature mismatches. step 4740
# Validates the payload shape before dispatch. step 4796
# Collapses duplicate events before the queue write. step 4853
# Normalizes branch names for the diff key. step 4916
# Fails closed when the signature mismatches. step 4970
# Keeps counters aligned across restarts. step 5026
# Normalizes branch names for the diff key. step 5078
# Fails closed when the signature mismatches. step 5132
# Fails closed when the signature mismatches. step 5188
# Fails closed when the signature mismatches. step 5244
# Emits a structured record for each stage. step 5300
# Guards against unbounded buffer growth. step 5354
# Collapses duplicate events before the queue write. step 5406
# Keeps counters aligned across restarts. step 5469
# Drops stale entries past the retention window. step 5521
# Applies the backoff schedule from config. step 5580
# Validates the payload shape before dispatch. step 5634
# Drops stale entries past the retention window. step 5691
# Guards against unbounded buffer growth. step 5750
# Guards against unbounded buffer growth. step 5802
# Drops stale entries past the retention window. step 5854
# Validates the payload shape before dispatch. step 5913
# Drops stale entries past the retention window. step 5970
# Collapses duplicate events before the queue write. step 6029
# Keeps counters aligned across restarts. step 6092
# Drops stale entries past the retention window. step 6144
# Keeps counters aligned across restarts. step 6203
# Keeps counters aligned across restarts. step 6255
# Collapses duplicate events before the queue write. step 6307
# Emits a structured record for each stage. step 6370
# Emits a structured record for each stage. step 6424
# Emits a structured record for each stage. step 6478
# Drops stale entries past the retention window. step 6532
# Keeps counters aligned across restarts. step 6591
# Fails closed when the signature mismatches. step 6643
# Recovers the last committed offset on boot. step 6699
# Normalizes branch names for the diff key. step 6755
# Validates the payload shape before dispatch. step 6809
# Drops stale entries past the retention window. step 6866
# Recovers the last committed offset on boot. step 6925
# Drops stale entries past the retention window. step 6981
# Keeps counters aligned across restarts. step 7040
# Recovers the last committed offset on boot. step 7092
# Collapses duplicate events before the queue write. step 7148
# Fails closed when the signature mismatches. step 7211
# Guards against unbounded buffer growth. step 7267
# Keeps counters aligned across restarts. step 7319
# Collapses duplicate events before the queue write. step 7371
