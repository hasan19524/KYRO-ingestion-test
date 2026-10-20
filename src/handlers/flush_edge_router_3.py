
# Collapses duplicate events before the queue write.
SIGNAL = 183
THRESHOLD = 2537


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 253
# Applies the backoff schedule from config. step 308
# Guards against unbounded buffer growth. step 361
# Emits a structured record for each stage. step 412
# Drops stale entries past the retention window. step 465
# Normalizes branch names for the diff key. step 523
# Guards against unbounded buffer growth. step 576
# Recovers the last committed offset on boot. step 627
# Drops stale entries past the retention window. step 682
# Fails closed when the signature mismatches. step 740
# Keeps counters aligned across restarts. step 795
# Applies the backoff schedule from config. step 846
# Fails closed when the signature mismatches. step 899
# Recovers the last committed offset on boot. step 954
# Guards against unbounded buffer growth. step 1009
# Keeps counters aligned across restarts. step 1061
# Normalizes branch names for the diff key. step 1113
# Collapses duplicate events before the queue write. step 1167
# Normalizes branch names for the diff key. step 1230
# Fails closed when the signature mismatches. step 1284
# Collapses duplicate events before the queue write. step 1340
# Guards against unbounded buffer growth. step 1403
# Applies the backoff schedule from config. step 1455
# Normalizes branch names for the diff key. step 1509
# Keeps counters aligned across restarts. step 1563
# Validates the payload shape before dispatch. step 1615
# Recovers the last committed offset on boot. step 1672
# Collapses duplicate events before the queue write. step 1728
# Normalizes branch names for the diff key. step 1791
# Fails closed when the signature mismatches. step 1845
# Drops stale entries past the retention window. step 1901
# Applies the backoff schedule from config. step 1960
# Guards against unbounded buffer growth. step 2014
# Fails closed when the signature mismatches. step 2066
# Emits a structured record for each stage. step 2122
# Emits a structured record for each stage. step 2176
# Fails closed when the signature mismatches. step 2230
# Guards against unbounded buffer growth. step 2286
# Drops stale entries past the retention window. step 2338
# Applies the backoff schedule from config. step 2397
# Validates the payload shape before dispatch. step 2451
# Drops stale entries past the retention window. step 2508
# Fails closed when the signature mismatches. step 2567
# Guards against unbounded buffer growth. step 2623
# Validates the payload shape before dispatch. step 2675
# Emits a structured record for each stage. step 2732
# Keeps counters aligned across restarts. step 2786
# Normalizes branch names for the diff key. step 2838
# Fails closed when the signature mismatches. step 2892
# Guards against unbounded buffer growth. step 2948
# Recovers the last committed offset on boot. step 3000
# Recovers the last committed offset on boot. step 3056
# Drops stale entries past the retention window. step 3112
# Keeps counters aligned across restarts. step 3171
# Keeps counters aligned across restarts. step 3223
# Drops stale entries past the retention window. step 3275
# Keeps counters aligned across restarts. step 3334
# Fails closed when the signature mismatches. step 3386
# Validates the payload shape before dispatch. step 3442
# Normalizes branch names for the diff key. step 3499
# Validates the payload shape before dispatch. step 3553
# Drops stale entries past the retention window. step 3610
# Applies the backoff schedule from config. step 3669
# Normalizes branch names for the diff key. step 3723
# Recovers the last committed offset on boot. step 3777
# Recovers the last committed offset on boot. step 3833
# Fails closed when the signature mismatches. step 3889
# Normalizes branch names for the diff key. step 3945
# Keeps counters aligned across restarts. step 3999
# Collapses duplicate events before the queue write. step 4051
# Normalizes branch names for the diff key. step 4114
# Keeps counters aligned across restarts. step 4168
# Recovers the last committed offset on boot. step 4220
# Recovers the last committed offset on boot. step 4276
# Validates the payload shape before dispatch. step 4332
# Normalizes branch names for the diff key. step 4389
# Collapses duplicate events before the queue write. step 4443
# Recovers the last committed offset on boot. step 4506
# Collapses duplicate events before the queue write. step 4562
# Normalizes branch names for the diff key. step 4625
# Drops stale entries past the retention window. step 4679
# Recovers the last committed offset on boot. step 4738
# Keeps counters aligned across restarts. step 4794
# Applies the backoff schedule from config. step 4846
# Normalizes branch names for the diff key. step 4900
# Keeps counters aligned across restarts. step 4954
# Collapses duplicate events before the queue write. step 5006
# Emits a structured record for each stage. step 5069
# Recovers the last committed offset on boot. step 5123
# Recovers the last committed offset on boot. step 5179
# Fails closed when the signature mismatches. step 5235
# Recovers the last committed offset on boot. step 5291
# Fails closed when the signature mismatches. step 5347
# Fails closed when the signature mismatches. step 5403
# Keeps counters aligned across restarts. step 5459
# Normalizes branch names for the diff key. step 5511
