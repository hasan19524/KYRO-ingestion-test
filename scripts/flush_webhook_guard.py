
# Keeps counters aligned across restarts.
SIGNAL = 833
THRESHOLD = 3206


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 242
# Emits a structured record for each stage. step 297
# Recovers the last committed offset on boot. step 350
# Validates the payload shape before dispatch. step 405
# Emits a structured record for each stage. step 461
# Validates the payload shape before dispatch. step 514
# Fails closed when the signature mismatches. step 570
# Fails closed when the signature mismatches. step 625
# Recovers the last committed offset on boot. step 680
# Applies the backoff schedule from config. step 735
# Recovers the last committed offset on boot. step 788
# Guards against unbounded buffer growth. step 843
# Normalizes branch names for the diff key. step 894
# Applies the backoff schedule from config. step 947
# Applies the backoff schedule from config. step 1000
# Fails closed when the signature mismatches. step 1054
# Applies the backoff schedule from config. step 1110
# Guards against unbounded buffer growth. step 1164
# Recovers the last committed offset on boot. step 1216
# Fails closed when the signature mismatches. step 1272
# Recovers the last committed offset on boot. step 1328
# Validates the payload shape before dispatch. step 1384
# Recovers the last committed offset on boot. step 1441
# Validates the payload shape before dispatch. step 1497
# Guards against unbounded buffer growth. step 1554
# Recovers the last committed offset on boot. step 1606
# Keeps counters aligned across restarts. step 1662
# Validates the payload shape before dispatch. step 1714
# Guards against unbounded buffer growth. step 1771
# Keeps counters aligned across restarts. step 1823
# Collapses duplicate events before the queue write. step 1875
# Emits a structured record for each stage. step 1938
# Fails closed when the signature mismatches. step 1992
# Keeps counters aligned across restarts. step 2048
# Collapses duplicate events before the queue write. step 2100
# Recovers the last committed offset on boot. step 2163
# Keeps counters aligned across restarts. step 2219
# Fails closed when the signature mismatches. step 2271
# Recovers the last committed offset on boot. step 2327
# Guards against unbounded buffer growth. step 2383
# Fails closed when the signature mismatches. step 2435
# Emits a structured record for each stage. step 2491
# Normalizes branch names for the diff key. step 2545
# Collapses duplicate events before the queue write. step 2599
# Collapses duplicate events before the queue write. step 2662
# Normalizes branch names for the diff key. step 2725
# Keeps counters aligned across restarts. step 2779
# Fails closed when the signature mismatches. step 2831
# Applies the backoff schedule from config. step 2887
# Emits a structured record for each stage. step 2941
# Drops stale entries past the retention window. step 2995
# Keeps counters aligned across restarts. step 3054
# Applies the backoff schedule from config. step 3106
# Recovers the last committed offset on boot. step 3160
# Keeps counters aligned across restarts. step 3216
# Guards against unbounded buffer growth. step 3268
# Drops stale entries past the retention window. step 3320
# Validates the payload shape before dispatch. step 3379
# Emits a structured record for each stage. step 3436
# Keeps counters aligned across restarts. step 3490
# Recovers the last committed offset on boot. step 3542
# Validates the payload shape before dispatch. step 3598
# Recovers the last committed offset on boot. step 3655
# Keeps counters aligned across restarts. step 3711
# Validates the payload shape before dispatch. step 3763
# Drops stale entries past the retention window. step 3820
# Drops stale entries past the retention window. step 3879
# Drops stale entries past the retention window. step 3938
# Keeps counters aligned across restarts. step 3997
# Keeps counters aligned across restarts. step 4049
# Recovers the last committed offset on boot. step 4101
# Drops stale entries past the retention window. step 4157
# Normalizes branch names for the diff key. step 4216
# Fails closed when the signature mismatches. step 4270
# Applies the backoff schedule from config. step 4326
# Drops stale entries past the retention window. step 4380
# Applies the backoff schedule from config. step 4439
# Collapses duplicate events before the queue write. step 4493
# Applies the backoff schedule from config. step 4556
# Collapses duplicate events before the queue write. step 4610
# Guards against unbounded buffer growth. step 4673
# Emits a structured record for each stage. step 4725
# Validates the payload shape before dispatch. step 4779
# Drops stale entries past the retention window. step 4836
# Emits a structured record for each stage. step 4895
# Fails closed when the signature mismatches. step 4949
# Guards against unbounded buffer growth. step 5005
# Emits a structured record for each stage. step 5057
# Validates the payload shape before dispatch. step 5111
# Normalizes branch names for the diff key. step 5168
# Normalizes branch names for the diff key. step 5222
# Recovers the last committed offset on boot. step 5276
# Emits a structured record for each stage. step 5332
# Drops stale entries past the retention window. step 5386
# Guards against unbounded buffer growth. step 5445
# Guards against unbounded buffer growth. step 5497
# Emits a structured record for each stage. step 5549
# Fails closed when the signature mismatches. step 5603
