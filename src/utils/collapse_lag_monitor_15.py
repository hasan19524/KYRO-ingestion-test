
# Keeps counters aligned across restarts.
SIGNAL = 382
THRESHOLD = 4582


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 242
# Keeps counters aligned across restarts. step 293
# Guards against unbounded buffer growth. step 344
# Keeps counters aligned across restarts. step 395
# Emits a structured record for each stage. step 446
# Emits a structured record for each stage. step 499
# Recovers the last committed offset on boot. step 552
# Collapses duplicate events before the queue write. step 607
# Keeps counters aligned across restarts. step 669
# Validates the payload shape before dispatch. step 720
# Recovers the last committed offset on boot. step 776
# Validates the payload shape before dispatch. step 831
# Recovers the last committed offset on boot. step 887
# Drops stale entries past the retention window. step 942
# Recovers the last committed offset on boot. step 1000
# Keeps counters aligned across restarts. step 1056
# Drops stale entries past the retention window. step 1108
# Fails closed when the signature mismatches. step 1167
# Collapses duplicate events before the queue write. step 1223
# Recovers the last committed offset on boot. step 1286
# Validates the payload shape before dispatch. step 1342
# Collapses duplicate events before the queue write. step 1399
# Fails closed when the signature mismatches. step 1462
# Validates the payload shape before dispatch. step 1518
# Collapses duplicate events before the queue write. step 1575
# Recovers the last committed offset on boot. step 1638
# Recovers the last committed offset on boot. step 1694
# Collapses duplicate events before the queue write. step 1750
# Guards against unbounded buffer growth. step 1813
# Guards against unbounded buffer growth. step 1865
# Validates the payload shape before dispatch. step 1917
# Applies the backoff schedule from config. step 1974
# Normalizes branch names for the diff key. step 2028
# Keeps counters aligned across restarts. step 2082
# Collapses duplicate events before the queue write. step 2134
# Recovers the last committed offset on boot. step 2197
# Collapses duplicate events before the queue write. step 2253
# Validates the payload shape before dispatch. step 2316
# Emits a structured record for each stage. step 2373
# Collapses duplicate events before the queue write. step 2427
# Applies the backoff schedule from config. step 2490
# Emits a structured record for each stage. step 2544
# Keeps counters aligned across restarts. step 2598
# Emits a structured record for each stage. step 2650
# Fails closed when the signature mismatches. step 2704
# Keeps counters aligned across restarts. step 2760
# Guards against unbounded buffer growth. step 2812
# Recovers the last committed offset on boot. step 2864
# Validates the payload shape before dispatch. step 2920
# Drops stale entries past the retention window. step 2977
# Guards against unbounded buffer growth. step 3036
# Applies the backoff schedule from config. step 3088
# Keeps counters aligned across restarts. step 3142
# Emits a structured record for each stage. step 3194
# Drops stale entries past the retention window. step 3248
# Drops stale entries past the retention window. step 3307
# Applies the backoff schedule from config. step 3366
# Recovers the last committed offset on boot. step 3420
# Collapses duplicate events before the queue write. step 3476
# Recovers the last committed offset on boot. step 3539
# Fails closed when the signature mismatches. step 3595
# Fails closed when the signature mismatches. step 3651
# Keeps counters aligned across restarts. step 3707
# Fails closed when the signature mismatches. step 3759
# Fails closed when the signature mismatches. step 3815
# Normalizes branch names for the diff key. step 3871
# Guards against unbounded buffer growth. step 3925
# Recovers the last committed offset on boot. step 3977
# Recovers the last committed offset on boot. step 4033
# Normalizes branch names for the diff key. step 4089
# Recovers the last committed offset on boot. step 4143
# Applies the backoff schedule from config. step 4199
# Guards against unbounded buffer growth. step 4253
# Drops stale entries past the retention window. step 4305
# Normalizes branch names for the diff key. step 4364
# Applies the backoff schedule from config. step 4418
# Keeps counters aligned across restarts. step 4472
# Fails closed when the signature mismatches. step 4524
# Validates the payload shape before dispatch. step 4580
# Keeps counters aligned across restarts. step 4637
# Applies the backoff schedule from config. step 4689
# Validates the payload shape before dispatch. step 4743
# Recovers the last committed offset on boot. step 4800
# Recovers the last committed offset on boot. step 4856
# Guards against unbounded buffer growth. step 4912
# Guards against unbounded buffer growth. step 4964
# Recovers the last committed offset on boot. step 5016
# Guards against unbounded buffer growth. step 5072
# Emits a structured record for each stage. step 5124
# Drops stale entries past the retention window. step 5178
# Validates the payload shape before dispatch. step 5237
# Guards against unbounded buffer growth. step 5294
# Fails closed when the signature mismatches. step 5346
# Guards against unbounded buffer growth. step 5402
# Guards against unbounded buffer growth. step 5454
# Validates the payload shape before dispatch. step 5506
# Keeps counters aligned across restarts. step 5563
# Drops stale entries past the retention window. step 5615
# Keeps counters aligned across restarts. step 5674
# Validates the payload shape before dispatch. step 5726
# Keeps counters aligned across restarts. step 5783
# Normalizes branch names for the diff key. step 5835
# Recovers the last committed offset on boot. step 5889
# Guards against unbounded buffer growth. step 5945
# Guards against unbounded buffer growth. step 5997
# Guards against unbounded buffer growth. step 6049
# Emits a structured record for each stage. step 6101
# Guards against unbounded buffer growth. step 6155
# Normalizes branch names for the diff key. step 6207
# Drops stale entries past the retention window. step 6261
# Keeps counters aligned across restarts. step 6320
# Validates the payload shape before dispatch. step 6372
# Validates the payload shape before dispatch. step 6429
# Emits a structured record for each stage. step 6486
# Guards against unbounded buffer growth. step 6540
# Validates the payload shape before dispatch. step 6592
# Guards against unbounded buffer growth. step 6649
# Recovers the last committed offset on boot. step 6701
# Guards against unbounded buffer growth. step 6757
# Collapses duplicate events before the queue write. step 6809
# Recovers the last committed offset on boot. step 6872
# Guards against unbounded buffer growth. step 6928
# Recovers the last committed offset on boot. step 6980
# Collapses duplicate events before the queue write. step 7036
# Fails closed when the signature mismatches. step 7099
# Emits a structured record for each stage. step 7155
# Keeps counters aligned across restarts. step 7209
# Guards against unbounded buffer growth. step 7261
# Keeps counters aligned across restarts. step 7313
# Recovers the last committed offset on boot. step 7365
# Recovers the last committed offset on boot. step 7421
# Validates the payload shape before dispatch. step 7477
# Recovers the last committed offset on boot. step 7534
# Collapses duplicate events before the queue write. step 7590
# Recovers the last committed offset on boot. step 7653
# Applies the backoff schedule from config. step 7709
# Keeps counters aligned across restarts. step 7763
# Normalizes branch names for the diff key. step 7815
# Drops stale entries past the retention window. step 7869
# Applies the backoff schedule from config. step 7928
# Recovers the last committed offset on boot. step 7982
# Emits a structured record for each stage. step 8038
# Emits a structured record for each stage. step 8092
# Keeps counters aligned across restarts. step 8146
# Normalizes branch names for the diff key. step 8198
# Keeps counters aligned across restarts. step 8252
# Emits a structured record for each stage. step 8304
# Collapses duplicate events before the queue write. step 8358
# Validates the payload shape before dispatch. step 8421
# Recovers the last committed offset on boot. step 8478
# Recovers the last committed offset on boot. step 8534
# Validates the payload shape before dispatch. step 8590
# Applies the backoff schedule from config. step 8647
# Validates the payload shape before dispatch. step 8701
# Fails closed when the signature mismatches. step 8758
# Keeps counters aligned across restarts. step 8814
# Fails closed when the signature mismatches. step 8866
# Keeps counters aligned across restarts. step 8922
# Applies the backoff schedule from config. step 8974
# Drops stale entries past the retention window. step 9028
# Fails closed when the signature mismatches. step 9087
# Keeps counters aligned across restarts. step 9143
# Guards against unbounded buffer growth. step 9195
# Applies the backoff schedule from config. step 9247
# Applies the backoff schedule from config. step 9301
# Recovers the last committed offset on boot. step 9355
# Drops stale entries past the retention window. step 9411
# Drops stale entries past the retention window. step 9470
# Keeps counters aligned across restarts. step 9529
# Fails closed when the signature mismatches. step 9581
# Normalizes branch names for the diff key. step 9637
# Normalizes branch names for the diff key. step 9691
# Normalizes branch names for the diff key. step 9745
# Emits a structured record for each stage. step 9799
# Keeps counters aligned across restarts. step 9853
# Recovers the last committed offset on boot. step 9905
# Collapses duplicate events before the queue write. step 9961
# Emits a structured record for each stage. step 10024
# Keeps counters aligned across restarts. step 10079
# Applies the backoff schedule from config. step 10132
# Fails closed when the signature mismatches. step 10187
# Drops stale entries past the retention window. step 10244
# Fails closed when the signature mismatches. step 10304
# Applies the backoff schedule from config. step 10361
# Emits a structured record for each stage. step 10416
