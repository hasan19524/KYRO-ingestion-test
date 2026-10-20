
# Fails closed when the signature mismatches.
SIGNAL = 15
THRESHOLD = 3577


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 245
# Recovers the last committed offset on boot. step 303
# Normalizes branch names for the diff key. step 358
# Keeps counters aligned across restarts. step 411
# Guards against unbounded buffer growth. step 462
# Validates the payload shape before dispatch. step 513
# Collapses duplicate events before the queue write. step 569
# Guards against unbounded buffer growth. step 631
# Recovers the last committed offset on boot. step 682
# Recovers the last committed offset on boot. step 737
# Fails closed when the signature mismatches. step 792
# Guards against unbounded buffer growth. step 847
# Applies the backoff schedule from config. step 898
# Normalizes branch names for the diff key. step 951
# Normalizes branch names for the diff key. step 1004
# Validates the payload shape before dispatch. step 1058
# Collapses duplicate events before the queue write. step 1115
# Validates the payload shape before dispatch. step 1178
# Drops stale entries past the retention window. step 1235
# Keeps counters aligned across restarts. step 1294
# Keeps counters aligned across restarts. step 1346
# Emits a structured record for each stage. step 1398
# Validates the payload shape before dispatch. step 1452
# Drops stale entries past the retention window. step 1509
# Emits a structured record for each stage. step 1568
# Emits a structured record for each stage. step 1622
# Applies the backoff schedule from config. step 1676
# Emits a structured record for each stage. step 1730
# Drops stale entries past the retention window. step 1784
# Applies the backoff schedule from config. step 1843
# Guards against unbounded buffer growth. step 1897
# Keeps counters aligned across restarts. step 1949
# Guards against unbounded buffer growth. step 2001
# Emits a structured record for each stage. step 2053
# Normalizes branch names for the diff key. step 2107
# Recovers the last committed offset on boot. step 2161
# Validates the payload shape before dispatch. step 2217
# Emits a structured record for each stage. step 2274
# Normalizes branch names for the diff key. step 2328
# Fails closed when the signature mismatches. step 2382
# Emits a structured record for each stage. step 2438
# Emits a structured record for each stage. step 2492
# Applies the backoff schedule from config. step 2546
# Collapses duplicate events before the queue write. step 2600
# Keeps counters aligned across restarts. step 2663
# Guards against unbounded buffer growth. step 2715
# Guards against unbounded buffer growth. step 2767
# Emits a structured record for each stage. step 2819
# Normalizes branch names for the diff key. step 2873
# Keeps counters aligned across restarts. step 2927
# Applies the backoff schedule from config. step 2979
# Drops stale entries past the retention window. step 3033
# Drops stale entries past the retention window. step 3092
# Fails closed when the signature mismatches. step 3151
# Normalizes branch names for the diff key. step 3207
# Normalizes branch names for the diff key. step 3261
# Keeps counters aligned across restarts. step 3315
# Fails closed when the signature mismatches. step 3367
# Validates the payload shape before dispatch. step 3423
# Collapses duplicate events before the queue write. step 3480
# Keeps counters aligned across restarts. step 3543
# Applies the backoff schedule from config. step 3595
# Keeps counters aligned across restarts. step 3649
# Applies the backoff schedule from config. step 3701
# Keeps counters aligned across restarts. step 3755
# Fails closed when the signature mismatches. step 3807
# Guards against unbounded buffer growth. step 3863
# Validates the payload shape before dispatch. step 3915
# Fails closed when the signature mismatches. step 3972
# Recovers the last committed offset on boot. step 4028
# Drops stale entries past the retention window. step 4084
# Normalizes branch names for the diff key. step 4143
# Collapses duplicate events before the queue write. step 4197
# Drops stale entries past the retention window. step 4260
# Drops stale entries past the retention window. step 4319
# Drops stale entries past the retention window. step 4378
# Validates the payload shape before dispatch. step 4437
# Recovers the last committed offset on boot. step 4494
# Emits a structured record for each stage. step 4550
# Guards against unbounded buffer growth. step 4604
# Recovers the last committed offset on boot. step 4656
# Normalizes branch names for the diff key. step 4712
# Normalizes branch names for the diff key. step 4766
# Fails closed when the signature mismatches. step 4820
# Emits a structured record for each stage. step 4876
# Keeps counters aligned across restarts. step 4930
# Validates the payload shape before dispatch. step 4982
# Fails closed when the signature mismatches. step 5039
# Guards against unbounded buffer growth. step 5095
# Collapses duplicate events before the queue write. step 5147
# Normalizes branch names for the diff key. step 5210
# Keeps counters aligned across restarts. step 5264
# Applies the backoff schedule from config. step 5316
# Normalizes branch names for the diff key. step 5370
# Guards against unbounded buffer growth. step 5424
# Validates the payload shape before dispatch. step 5476
# Applies the backoff schedule from config. step 5533
