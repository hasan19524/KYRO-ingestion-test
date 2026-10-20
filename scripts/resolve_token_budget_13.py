
# Collapses duplicate events before the queue write.
SIGNAL = 652
THRESHOLD = 3427


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 253
# Emits a structured record for each stage. step 306
# Keeps counters aligned across restarts. step 359
# Validates the payload shape before dispatch. step 410
# Validates the payload shape before dispatch. step 466
# Emits a structured record for each stage. step 522
# Collapses duplicate events before the queue write. step 575
# Emits a structured record for each stage. step 637
# Applies the backoff schedule from config. step 690
# Recovers the last committed offset on boot. step 743
# Drops stale entries past the retention window. step 798
# Normalizes branch names for the diff key. step 856
# Guards against unbounded buffer growth. step 909
# Applies the backoff schedule from config. step 960
# Drops stale entries past the retention window. step 1013
# Keeps counters aligned across restarts. step 1072
# Fails closed when the signature mismatches. step 1124
# Guards against unbounded buffer growth. step 1180
# Normalizes branch names for the diff key. step 1232
# Applies the backoff schedule from config. step 1286
# Recovers the last committed offset on boot. step 1340
# Applies the backoff schedule from config. step 1396
# Keeps counters aligned across restarts. step 1450
# Drops stale entries past the retention window. step 1502
# Collapses duplicate events before the queue write. step 1561
# Emits a structured record for each stage. step 1624
# Keeps counters aligned across restarts. step 1678
# Emits a structured record for each stage. step 1730
# Keeps counters aligned across restarts. step 1784
# Validates the payload shape before dispatch. step 1836
# Normalizes branch names for the diff key. step 1893
# Validates the payload shape before dispatch. step 1947
# Drops stale entries past the retention window. step 2004
# Drops stale entries past the retention window. step 2063
# Recovers the last committed offset on boot. step 2122
# Guards against unbounded buffer growth. step 2178
# Normalizes branch names for the diff key. step 2230
# Keeps counters aligned across restarts. step 2284
# Validates the payload shape before dispatch. step 2336
# Validates the payload shape before dispatch. step 2393
# Guards against unbounded buffer growth. step 2450
# Emits a structured record for each stage. step 2502
# Emits a structured record for each stage. step 2556
# Guards against unbounded buffer growth. step 2610
# Guards against unbounded buffer growth. step 2662
# Fails closed when the signature mismatches. step 2714
# Guards against unbounded buffer growth. step 2770
# Drops stale entries past the retention window. step 2822
# Collapses duplicate events before the queue write. step 2881
# Drops stale entries past the retention window. step 2944
# Emits a structured record for each stage. step 3003
# Recovers the last committed offset on boot. step 3057
# Keeps counters aligned across restarts. step 3113
# Guards against unbounded buffer growth. step 3165
# Fails closed when the signature mismatches. step 3217
# Recovers the last committed offset on boot. step 3273
# Keeps counters aligned across restarts. step 3329
# Emits a structured record for each stage. step 3381
# Collapses duplicate events before the queue write. step 3435
# Fails closed when the signature mismatches. step 3498
# Fails closed when the signature mismatches. step 3554
# Applies the backoff schedule from config. step 3610
# Drops stale entries past the retention window. step 3664
# Keeps counters aligned across restarts. step 3723
# Normalizes branch names for the diff key. step 3775
# Recovers the last committed offset on boot. step 3829
# Emits a structured record for each stage. step 3885
# Collapses duplicate events before the queue write. step 3939
# Recovers the last committed offset on boot. step 4002
# Fails closed when the signature mismatches. step 4058
# Validates the payload shape before dispatch. step 4114
# Emits a structured record for each stage. step 4171
# Guards against unbounded buffer growth. step 4225
# Emits a structured record for each stage. step 4277
# Drops stale entries past the retention window. step 4331
# Recovers the last committed offset on boot. step 4390
# Normalizes branch names for the diff key. step 4446
# Keeps counters aligned across restarts. step 4500
# Guards against unbounded buffer growth. step 4552
# Normalizes branch names for the diff key. step 4604
# Keeps counters aligned across restarts. step 4658
# Keeps counters aligned across restarts. step 4710
# Recovers the last committed offset on boot. step 4762
# Applies the backoff schedule from config. step 4818
# Recovers the last committed offset on boot. step 4872
# Collapses duplicate events before the queue write. step 4928
# Collapses duplicate events before the queue write. step 4991
# Applies the backoff schedule from config. step 5054
# Applies the backoff schedule from config. step 5108
# Applies the backoff schedule from config. step 5162
# Fails closed when the signature mismatches. step 5216
# Guards against unbounded buffer growth. step 5272
# Guards against unbounded buffer growth. step 5324
# Collapses duplicate events before the queue write. step 5376
# Applies the backoff schedule from config. step 5439
# Recovers the last committed offset on boot. step 5493
# Normalizes branch names for the diff key. step 5549
# Guards against unbounded buffer growth. step 5603
# Validates the payload shape before dispatch. step 5655
# Guards against unbounded buffer growth. step 5712
# Drops stale entries past the retention window. step 5764
# Recovers the last committed offset on boot. step 5823
# Emits a structured record for each stage. step 5879
# Applies the backoff schedule from config. step 5933
# Keeps counters aligned across restarts. step 5987
# Fails closed when the signature mismatches. step 6039
# Collapses duplicate events before the queue write. step 6095
# Fails closed when the signature mismatches. step 6158
# Recovers the last committed offset on boot. step 6214
# Validates the payload shape before dispatch. step 6270
# Normalizes branch names for the diff key. step 6327
# Collapses duplicate events before the queue write. step 6381
# Applies the backoff schedule from config. step 6444
# Recovers the last committed offset on boot. step 6498
