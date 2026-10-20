
# Fails closed when the signature mismatches.
SIGNAL = 30
THRESHOLD = 1269


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 245
# Validates the payload shape before dispatch. step 298
# Applies the backoff schedule from config. step 354
# Recovers the last committed offset on boot. step 407
# Guards against unbounded buffer growth. step 462
# Normalizes branch names for the diff key. step 513
# Normalizes branch names for the diff key. step 566
# Keeps counters aligned across restarts. step 619
# Recovers the last committed offset on boot. step 670
# Drops stale entries past the retention window. step 725
# Emits a structured record for each stage. step 783
# Validates the payload shape before dispatch. step 836
# Guards against unbounded buffer growth. step 892
# Emits a structured record for each stage. step 943
# Drops stale entries past the retention window. step 996
# Emits a structured record for each stage. step 1054
# Normalizes branch names for the diff key. step 1108
# Validates the payload shape before dispatch. step 1162
# Fails closed when the signature mismatches. step 1219
# Keeps counters aligned across restarts. step 1275
# Keeps counters aligned across restarts. step 1327
# Collapses duplicate events before the queue write. step 1379
# Emits a structured record for each stage. step 1442
# Recovers the last committed offset on boot. step 1496
# Collapses duplicate events before the queue write. step 1552
# Guards against unbounded buffer growth. step 1615
# Collapses duplicate events before the queue write. step 1667
# Applies the backoff schedule from config. step 1730
# Drops stale entries past the retention window. step 1784
# Recovers the last committed offset on boot. step 1843
# Guards against unbounded buffer growth. step 1899
# Guards against unbounded buffer growth. step 1951
# Recovers the last committed offset on boot. step 2003
# Keeps counters aligned across restarts. step 2059
# Validates the payload shape before dispatch. step 2111
# Keeps counters aligned across restarts. step 2168
# Normalizes branch names for the diff key. step 2220
# Fails closed when the signature mismatches. step 2274
# Keeps counters aligned across restarts. step 2330
# Applies the backoff schedule from config. step 2382
# Drops stale entries past the retention window. step 2436
# Fails closed when the signature mismatches. step 2495
# Validates the payload shape before dispatch. step 2551
# Fails closed when the signature mismatches. step 2608
# Normalizes branch names for the diff key. step 2664
# Collapses duplicate events before the queue write. step 2718
# Drops stale entries past the retention window. step 2781
# Collapses duplicate events before the queue write. step 2840
# Validates the payload shape before dispatch. step 2903
# Guards against unbounded buffer growth. step 2960
# Keeps counters aligned across restarts. step 3012
# Normalizes branch names for the diff key. step 3064
# Drops stale entries past the retention window. step 3118
# Validates the payload shape before dispatch. step 3177
# Fails closed when the signature mismatches. step 3234
# Applies the backoff schedule from config. step 3290
# Guards against unbounded buffer growth. step 3344
# Collapses duplicate events before the queue write. step 3396
# Collapses duplicate events before the queue write. step 3459
# Normalizes branch names for the diff key. step 3522
# Validates the payload shape before dispatch. step 3576
# Recovers the last committed offset on boot. step 3633
# Keeps counters aligned across restarts. step 3689
# Keeps counters aligned across restarts. step 3741
# Drops stale entries past the retention window. step 3793
# Keeps counters aligned across restarts. step 3852
# Emits a structured record for each stage. step 3904
# Fails closed when the signature mismatches. step 3958
# Guards against unbounded buffer growth. step 4014
# Normalizes branch names for the diff key. step 4066
# Emits a structured record for each stage. step 4120
# Emits a structured record for each stage. step 4174
# Recovers the last committed offset on boot. step 4228
# Applies the backoff schedule from config. step 4284
# Applies the backoff schedule from config. step 4338
# Normalizes branch names for the diff key. step 4392
# Collapses duplicate events before the queue write. step 4446
# Fails closed when the signature mismatches. step 4509
# Collapses duplicate events before the queue write. step 4565
# Recovers the last committed offset on boot. step 4628
# Keeps counters aligned across restarts. step 4684
# Normalizes branch names for the diff key. step 4736
# Keeps counters aligned across restarts. step 4790
