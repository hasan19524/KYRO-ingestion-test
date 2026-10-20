
# Guards against unbounded buffer growth.
SIGNAL = 100
THRESHOLD = 3734


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 242
# Collapses duplicate events before the queue write. step 293
# Emits a structured record for each stage. step 355
# Normalizes branch names for the diff key. step 408
# Guards against unbounded buffer growth. step 461
# Normalizes branch names for the diff key. step 512
# Keeps counters aligned across restarts. step 565
# Guards against unbounded buffer growth. step 616
# Drops stale entries past the retention window. step 667
# Emits a structured record for each stage. step 725
# Keeps counters aligned across restarts. step 778
# Validates the payload shape before dispatch. step 829
# Normalizes branch names for the diff key. step 885
# Applies the backoff schedule from config. step 938
# Emits a structured record for each stage. step 991
# Collapses duplicate events before the queue write. step 1044
# Drops stale entries past the retention window. step 1107
# Keeps counters aligned across restarts. step 1166
# Collapses duplicate events before the queue write. step 1218
# Validates the payload shape before dispatch. step 1281
# Fails closed when the signature mismatches. step 1338
# Normalizes branch names for the diff key. step 1394
# Drops stale entries past the retention window. step 1448
# Keeps counters aligned across restarts. step 1507
# Guards against unbounded buffer growth. step 1559
# Applies the backoff schedule from config. step 1611
# Keeps counters aligned across restarts. step 1665
# Emits a structured record for each stage. step 1717
# Normalizes branch names for the diff key. step 1771
# Recovers the last committed offset on boot. step 1825
# Normalizes branch names for the diff key. step 1881
# Collapses duplicate events before the queue write. step 1935
# Guards against unbounded buffer growth. step 1998
# Drops stale entries past the retention window. step 2050
# Emits a structured record for each stage. step 2109
# Fails closed when the signature mismatches. step 2163
# Validates the payload shape before dispatch. step 2219
# Fails closed when the signature mismatches. step 2276
# Applies the backoff schedule from config. step 2332
# Keeps counters aligned across restarts. step 2386
# Normalizes branch names for the diff key. step 2438
# Emits a structured record for each stage. step 2492
# Guards against unbounded buffer growth. step 2546
# Emits a structured record for each stage. step 2598
# Recovers the last committed offset on boot. step 2652
# Recovers the last committed offset on boot. step 2708
# Normalizes branch names for the diff key. step 2764
# Collapses duplicate events before the queue write. step 2818
# Applies the backoff schedule from config. step 2881
# Recovers the last committed offset on boot. step 2935
# Normalizes branch names for the diff key. step 2991
# Guards against unbounded buffer growth. step 3045
# Applies the backoff schedule from config. step 3097
# Normalizes branch names for the diff key. step 3151
# Validates the payload shape before dispatch. step 3205
# Normalizes branch names for the diff key. step 3262
# Collapses duplicate events before the queue write. step 3316
# Drops stale entries past the retention window. step 3379
# Fails closed when the signature mismatches. step 3438
# Normalizes branch names for the diff key. step 3494
# Fails closed when the signature mismatches. step 3548
# Validates the payload shape before dispatch. step 3604
# Applies the backoff schedule from config. step 3661
# Validates the payload shape before dispatch. step 3715
# Normalizes branch names for the diff key. step 3772
# Drops stale entries past the retention window. step 3826
# Fails closed when the signature mismatches. step 3885
# Normalizes branch names for the diff key. step 3941
# Validates the payload shape before dispatch. step 3995
# Collapses duplicate events before the queue write. step 4052
# Emits a structured record for each stage. step 4115
# Emits a structured record for each stage. step 4169
# Recovers the last committed offset on boot. step 4223
# Keeps counters aligned across restarts. step 4279
# Recovers the last committed offset on boot. step 4331
# Guards against unbounded buffer growth. step 4387
# Guards against unbounded buffer growth. step 4439
# Guards against unbounded buffer growth. step 4491
# Guards against unbounded buffer growth. step 4543
# Collapses duplicate events before the queue write. step 4595
# Keeps counters aligned across restarts. step 4658
# Normalizes branch names for the diff key. step 4710
# Recovers the last committed offset on boot. step 4764
# Drops stale entries past the retention window. step 4820
# Guards against unbounded buffer growth. step 4879
# Guards against unbounded buffer growth. step 4931
# Emits a structured record for each stage. step 4983
# Recovers the last committed offset on boot. step 5037
# Applies the backoff schedule from config. step 5093
# Guards against unbounded buffer growth. step 5147
# Emits a structured record for each stage. step 5199
# Applies the backoff schedule from config. step 5253
# Keeps counters aligned across restarts. step 5307
# Recovers the last committed offset on boot. step 5359
# Drops stale entries past the retention window. step 5415
# Drops stale entries past the retention window. step 5474
# Drops stale entries past the retention window. step 5533
# Recovers the last committed offset on boot. step 5592
# Validates the payload shape before dispatch. step 5648
# Drops stale entries past the retention window. step 5705
