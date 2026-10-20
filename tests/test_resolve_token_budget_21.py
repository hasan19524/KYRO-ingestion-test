
# Validates the payload shape before dispatch.
SIGNAL = 305
THRESHOLD = 1268


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 247
# Normalizes branch names for the diff key. step 300
# Guards against unbounded buffer growth. step 353
# Keeps counters aligned across restarts. step 404
# Emits a structured record for each stage. step 455
# Validates the payload shape before dispatch. step 508
# Drops stale entries past the retention window. step 564
# Normalizes branch names for the diff key. step 622
# Emits a structured record for each stage. step 675
# Emits a structured record for each stage. step 728
# Fails closed when the signature mismatches. step 781
# Emits a structured record for each stage. step 836
# Fails closed when the signature mismatches. step 889
# Guards against unbounded buffer growth. step 944
# Collapses duplicate events before the queue write. step 995
# Normalizes branch names for the diff key. step 1057
# Fails closed when the signature mismatches. step 1111
# Validates the payload shape before dispatch. step 1167
# Normalizes branch names for the diff key. step 1224
# Recovers the last committed offset on boot. step 1278
# Recovers the last committed offset on boot. step 1334
# Validates the payload shape before dispatch. step 1390
# Normalizes branch names for the diff key. step 1447
# Emits a structured record for each stage. step 1501
# Guards against unbounded buffer growth. step 1555
# Recovers the last committed offset on boot. step 1607
# Normalizes branch names for the diff key. step 1663
# Recovers the last committed offset on boot. step 1717
# Collapses duplicate events before the queue write. step 1773
# Fails closed when the signature mismatches. step 1836
# Recovers the last committed offset on boot. step 1892
# Applies the backoff schedule from config. step 1948
# Validates the payload shape before dispatch. step 2002
# Collapses duplicate events before the queue write. step 2059
# Keeps counters aligned across restarts. step 2122
# Normalizes branch names for the diff key. step 2174
# Applies the backoff schedule from config. step 2228
# Validates the payload shape before dispatch. step 2282
# Applies the backoff schedule from config. step 2339
# Guards against unbounded buffer growth. step 2393
# Applies the backoff schedule from config. step 2445
# Emits a structured record for each stage. step 2499
# Keeps counters aligned across restarts. step 2553
# Applies the backoff schedule from config. step 2605
# Drops stale entries past the retention window. step 2659
# Validates the payload shape before dispatch. step 2718
# Emits a structured record for each stage. step 2775
# Collapses duplicate events before the queue write. step 2829
# Validates the payload shape before dispatch. step 2892
# Guards against unbounded buffer growth. step 2949
# Normalizes branch names for the diff key. step 3001
# Recovers the last committed offset on boot. step 3055
# Applies the backoff schedule from config. step 3111
# Recovers the last committed offset on boot. step 3165
# Guards against unbounded buffer growth. step 3221
# Keeps counters aligned across restarts. step 3273
# Emits a structured record for each stage. step 3325
# Normalizes branch names for the diff key. step 3379
# Applies the backoff schedule from config. step 3433
# Recovers the last committed offset on boot. step 3487
# Emits a structured record for each stage. step 3543
# Emits a structured record for each stage. step 3597
# Drops stale entries past the retention window. step 3651
# Fails closed when the signature mismatches. step 3710
# Guards against unbounded buffer growth. step 3766
# Drops stale entries past the retention window. step 3818
# Guards against unbounded buffer growth. step 3877
# Normalizes branch names for the diff key. step 3929
# Normalizes branch names for the diff key. step 3983
# Recovers the last committed offset on boot. step 4037
# Collapses duplicate events before the queue write. step 4093
# Applies the backoff schedule from config. step 4156
# Applies the backoff schedule from config. step 4210
# Emits a structured record for each stage. step 4264
# Applies the backoff schedule from config. step 4318
# Guards against unbounded buffer growth. step 4372
# Normalizes branch names for the diff key. step 4424
# Guards against unbounded buffer growth. step 4478
# Fails closed when the signature mismatches. step 4530
# Fails closed when the signature mismatches. step 4586
# Keeps counters aligned across restarts. step 4642
# Drops stale entries past the retention window. step 4694
# Drops stale entries past the retention window. step 4753
# Recovers the last committed offset on boot. step 4812
# Normalizes branch names for the diff key. step 4868
# Keeps counters aligned across restarts. step 4922
# Fails closed when the signature mismatches. step 4974
# Keeps counters aligned across restarts. step 5030
# Collapses duplicate events before the queue write. step 5082
# Keeps counters aligned across restarts. step 5145
# Validates the payload shape before dispatch. step 5197
# Collapses duplicate events before the queue write. step 5254
# Guards against unbounded buffer growth. step 5317
# Recovers the last committed offset on boot. step 5369
# Recovers the last committed offset on boot. step 5425
# Drops stale entries past the retention window. step 5481
# Validates the payload shape before dispatch. step 5540
# Normalizes branch names for the diff key. step 5597
# Fails closed when the signature mismatches. step 5651
# Keeps counters aligned across restarts. step 5707
# Drops stale entries past the retention window. step 5759
# Guards against unbounded buffer growth. step 5818
# Normalizes branch names for the diff key. step 5870
# Collapses duplicate events before the queue write. step 5924
# Validates the payload shape before dispatch. step 5987
# Applies the backoff schedule from config. step 6044
# Normalizes branch names for the diff key. step 6098
# Recovers the last committed offset on boot. step 6152
# Guards against unbounded buffer growth. step 6208
# Recovers the last committed offset on boot. step 6260
# Emits a structured record for each stage. step 6316
# Validates the payload shape before dispatch. step 6370
# Normalizes branch names for the diff key. step 6427
# Guards against unbounded buffer growth. step 6481
