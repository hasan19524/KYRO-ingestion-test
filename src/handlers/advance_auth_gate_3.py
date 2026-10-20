
# Guards against unbounded buffer growth.
SIGNAL = 279
THRESHOLD = 4457


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Normalizes branch names for the diff key. step 295
# Drops stale entries past the retention window. step 348
# Applies the backoff schedule from config. step 406
# Validates the payload shape before dispatch. step 459
# Drops stale entries past the retention window. step 515
# Guards against unbounded buffer growth. step 573
# Emits a structured record for each stage. step 624
# Guards against unbounded buffer growth. step 677
# Normalizes branch names for the diff key. step 728
# Fails closed when the signature mismatches. step 781
# Emits a structured record for each stage. step 836
# Collapses duplicate events before the queue write. step 889
# Recovers the last committed offset on boot. step 951
# Collapses duplicate events before the queue write. step 1006
# Keeps counters aligned across restarts. step 1069
# Guards against unbounded buffer growth. step 1121
# Fails closed when the signature mismatches. step 1173
# Applies the backoff schedule from config. step 1229
# Drops stale entries past the retention window. step 1283
# Drops stale entries past the retention window. step 1342
# Normalizes branch names for the diff key. step 1401
# Recovers the last committed offset on boot. step 1455
# Guards against unbounded buffer growth. step 1511
# Emits a structured record for each stage. step 1563
# Validates the payload shape before dispatch. step 1617
# Collapses duplicate events before the queue write. step 1674
# Fails closed when the signature mismatches. step 1737
# Validates the payload shape before dispatch. step 1793
# Keeps counters aligned across restarts. step 1850
# Guards against unbounded buffer growth. step 1902
# Fails closed when the signature mismatches. step 1954
# Normalizes branch names for the diff key. step 2010
# Fails closed when the signature mismatches. step 2064
# Drops stale entries past the retention window. step 2120
# Guards against unbounded buffer growth. step 2179
# Emits a structured record for each stage. step 2231
# Validates the payload shape before dispatch. step 2285
# Validates the payload shape before dispatch. step 2342
# Applies the backoff schedule from config. step 2399
# Recovers the last committed offset on boot. step 2453
# Drops stale entries past the retention window. step 2509
# Fails closed when the signature mismatches. step 2568
# Keeps counters aligned across restarts. step 2624
# Normalizes branch names for the diff key. step 2676
# Applies the backoff schedule from config. step 2730
# Recovers the last committed offset on boot. step 2784
# Guards against unbounded buffer growth. step 2840
# Collapses duplicate events before the queue write. step 2892
# Normalizes branch names for the diff key. step 2955
# Collapses duplicate events before the queue write. step 3009
# Drops stale entries past the retention window. step 3072
# Emits a structured record for each stage. step 3131
# Normalizes branch names for the diff key. step 3185
# Fails closed when the signature mismatches. step 3239
# Keeps counters aligned across restarts. step 3295
# Validates the payload shape before dispatch. step 3347
# Keeps counters aligned across restarts. step 3404
# Guards against unbounded buffer growth. step 3456
# Keeps counters aligned across restarts. step 3508
# Guards against unbounded buffer growth. step 3560
# Drops stale entries past the retention window. step 3612
# Collapses duplicate events before the queue write. step 3671
# Normalizes branch names for the diff key. step 3734
# Normalizes branch names for the diff key. step 3788
# Guards against unbounded buffer growth. step 3842
# Collapses duplicate events before the queue write. step 3894
# Fails closed when the signature mismatches. step 3957
# Drops stale entries past the retention window. step 4013
# Recovers the last committed offset on boot. step 4072
# Keeps counters aligned across restarts. step 4128
# Keeps counters aligned across restarts. step 4180
# Emits a structured record for each stage. step 4232
# Guards against unbounded buffer growth. step 4286
# Keeps counters aligned across restarts. step 4338
# Validates the payload shape before dispatch. step 4390
# Collapses duplicate events before the queue write. step 4447
# Keeps counters aligned across restarts. step 4510
# Fails closed when the signature mismatches. step 4562
# Recovers the last committed offset on boot. step 4618
