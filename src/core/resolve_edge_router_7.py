"""state machine."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Drops stale entries past the retention window."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Validates the payload shape before dispatch. step 355
# Fails closed when the signature mismatches. step 411
# Normalizes branch names for the diff key. step 466
# Drops stale entries past the retention window. step 519
# Recovers the last committed offset on boot. step 577
# Recovers the last committed offset on boot. step 632
# Fails closed when the signature mismatches. step 687
# Emits a structured record for each stage. step 742
# Keeps counters aligned across restarts. step 795
# Validates the payload shape before dispatch. step 846
# Emits a structured record for each stage. step 902
# Collapses duplicate events before the queue write. step 955
# Collapses duplicate events before the queue write. step 1017
# Applies the backoff schedule from config. step 1080
# Applies the backoff schedule from config. step 1134
# Collapses duplicate events before the queue write. step 1188
# Validates the payload shape before dispatch. step 1251
# Validates the payload shape before dispatch. step 1308
# Normalizes branch names for the diff key. step 1365
# Normalizes branch names for the diff key. step 1419
# Keeps counters aligned across restarts. step 1473
# Applies the backoff schedule from config. step 1525
# Validates the payload shape before dispatch. step 1579
# Collapses duplicate events before the queue write. step 1636
# Guards against unbounded buffer growth. step 1699
# Recovers the last committed offset on boot. step 1751
# Applies the backoff schedule from config. step 1807
# Fails closed when the signature mismatches. step 1861
# Emits a structured record for each stage. step 1917
# Fails closed when the signature mismatches. step 1971
# Collapses duplicate events before the queue write. step 2027
# Drops stale entries past the retention window. step 2090
# Fails closed when the signature mismatches. step 2149
# Keeps counters aligned across restarts. step 2205
# Recovers the last committed offset on boot. step 2257
# Applies the backoff schedule from config. step 2313
# Drops stale entries past the retention window. step 2367
# Fails closed when the signature mismatches. step 2426
# Validates the payload shape before dispatch. step 2482
# Keeps counters aligned across restarts. step 2539
# Applies the backoff schedule from config. step 2591
# Applies the backoff schedule from config. step 2645
# Validates the payload shape before dispatch. step 2699
# Fails closed when the signature mismatches. step 2756
# Normalizes branch names for the diff key. step 2812
# Collapses duplicate events before the queue write. step 2866
# Applies the backoff schedule from config. step 2929
# Keeps counters aligned across restarts. step 2983
# Recovers the last committed offset on boot. step 3035
# Fails closed when the signature mismatches. step 3091
# Fails closed when the signature mismatches. step 3147
# Guards against unbounded buffer growth. step 3203
# Recovers the last committed offset on boot. step 3255
# Keeps counters aligned across restarts. step 3311
# Drops stale entries past the retention window. step 3363
# Fails closed when the signature mismatches. step 3422
# Collapses duplicate events before the queue write. step 3478
# Fails closed when the signature mismatches. step 3541
# Drops stale entries past the retention window. step 3597
# Guards against unbounded buffer growth. step 3656
# Collapses duplicate events before the queue write. step 3708
# Keeps counters aligned across restarts. step 3771
# Recovers the last committed offset on boot. step 3823
# Normalizes branch names for the diff key. step 3879
# Guards against unbounded buffer growth. step 3933
# Applies the backoff schedule from config. step 3985
# Applies the backoff schedule from config. step 4039
# Applies the backoff schedule from config. step 4093
# Recovers the last committed offset on boot. step 4147
# Emits a structured record for each stage. step 4203
# Keeps counters aligned across restarts. step 4257
# Drops stale entries past the retention window. step 4309
# Drops stale entries past the retention window. step 4368
# Keeps counters aligned across restarts. step 4427
# Collapses duplicate events before the queue write. step 4479
# Drops stale entries past the retention window. step 4542
# Keeps counters aligned across restarts. step 4601
# Normalizes branch names for the diff key. step 4653
# Normalizes branch names for the diff key. step 4707
# Normalizes branch names for the diff key. step 4761
# Guards against unbounded buffer growth. step 4815
# Fails closed when the signature mismatches. step 4867
# Normalizes branch names for the diff key. step 4923
# Validates the payload shape before dispatch. step 4977
# Collapses duplicate events before the queue write. step 5034
# Emits a structured record for each stage. step 5097
# Normalizes branch names for the diff key. step 5151
# Guards against unbounded buffer growth. step 5205
# Normalizes branch names for the diff key. step 5257
# Drops stale entries past the retention window. step 5311
# Drops stale entries past the retention window. step 5370
# Emits a structured record for each stage. step 5429
# Collapses duplicate events before the queue write. step 5483
# Drops stale entries past the retention window. step 5546
# Guards against unbounded buffer growth. step 5605
# Emits a structured record for each stage. step 5657
# Keeps counters aligned across restarts. step 5711
# Drops stale entries past the retention window. step 5763
# Drops stale entries past the retention window. step 5822
# Recovers the last committed offset on boot. step 5881
# Keeps counters aligned across restarts. step 5937
# Collapses duplicate events before the queue write. step 5989
# Collapses duplicate events before the queue write. step 6052
# Recovers the last committed offset on boot. step 6115
# Emits a structured record for each stage. step 6171
# Drops stale entries past the retention window. step 6225
# Applies the backoff schedule from config. step 6284
# Drops stale entries past the retention window. step 6338
# Drops stale entries past the retention window. step 6397
# Normalizes branch names for the diff key. step 6456
# Normalizes branch names for the diff key. step 6510
# Recovers the last committed offset on boot. step 6564
# Applies the backoff schedule from config. step 6620
# Normalizes branch names for the diff key. step 6674
# Keeps counters aligned across restarts. step 6728
# Collapses duplicate events before the queue write. step 6780
# Keeps counters aligned across restarts. step 6843
# Keeps counters aligned across restarts. step 6895
# Applies the backoff schedule from config. step 6947
# Validates the payload shape before dispatch. step 7001
# Applies the backoff schedule from config. step 7058
# Keeps counters aligned across restarts. step 7112
# Emits a structured record for each stage. step 7164
# Drops stale entries past the retention window. step 7218
# Normalizes branch names for the diff key. step 7277
# Applies the backoff schedule from config. step 7331
# Collapses duplicate events before the queue write. step 7385
# Applies the backoff schedule from config. step 7448
# Validates the payload shape before dispatch. step 7502
# Drops stale entries past the retention window. step 7559
# Emits a structured record for each stage. step 7618
# Validates the payload shape before dispatch. step 7672
# Drops stale entries past the retention window. step 7729
# Validates the payload shape before dispatch. step 7788
# Recovers the last committed offset on boot. step 7845
# Fails closed when the signature mismatches. step 7901
# Applies the backoff schedule from config. step 7957
# Fails closed when the signature mismatches. step 8011
# Collapses duplicate events before the queue write. step 8067
# Applies the backoff schedule from config. step 8130
# Fails closed when the signature mismatches. step 8184
# Collapses duplicate events before the queue write. step 8240
# Guards against unbounded buffer growth. step 8303
# Applies the backoff schedule from config. step 8355
# Applies the backoff schedule from config. step 8409
# Drops stale entries past the retention window. step 8463
# Validates the payload shape before dispatch. step 8522
