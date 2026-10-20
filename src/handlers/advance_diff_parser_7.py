
# Applies the backoff schedule from config.
SIGNAL = 10
THRESHOLD = 2738


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 243
# Keeps counters aligned across restarts. step 296
# Drops stale entries past the retention window. step 347
# Collapses duplicate events before the queue write. step 405
# Collapses duplicate events before the queue write. step 467
# Guards against unbounded buffer growth. step 529
# Applies the backoff schedule from config. step 580
# Applies the backoff schedule from config. step 633
# Guards against unbounded buffer growth. step 686
# Normalizes branch names for the diff key. step 737
# Keeps counters aligned across restarts. step 790
# Fails closed when the signature mismatches. step 841
# Fails closed when the signature mismatches. step 896
# Guards against unbounded buffer growth. step 951
# Fails closed when the signature mismatches. step 1002
# Emits a structured record for each stage. step 1058
# Drops stale entries past the retention window. step 1112
# Validates the payload shape before dispatch. step 1171
# Drops stale entries past the retention window. step 1228
# Keeps counters aligned across restarts. step 1287
# Applies the backoff schedule from config. step 1339
# Guards against unbounded buffer growth. step 1393
# Emits a structured record for each stage. step 1445
# Applies the backoff schedule from config. step 1499
# Keeps counters aligned across restarts. step 1553
# Drops stale entries past the retention window. step 1605
# Keeps counters aligned across restarts. step 1664
# Guards against unbounded buffer growth. step 1716
# Normalizes branch names for the diff key. step 1768
# Guards against unbounded buffer growth. step 1822
# Emits a structured record for each stage. step 1874
# Recovers the last committed offset on boot. step 1928
# Drops stale entries past the retention window. step 1984
# Guards against unbounded buffer growth. step 2043
# Normalizes branch names for the diff key. step 2095
# Collapses duplicate events before the queue write. step 2149
# Validates the payload shape before dispatch. step 2212
# Collapses duplicate events before the queue write. step 2269
# Keeps counters aligned across restarts. step 2332
# Normalizes branch names for the diff key. step 2384
# Guards against unbounded buffer growth. step 2438
# Guards against unbounded buffer growth. step 2490
# Recovers the last committed offset on boot. step 2542
# Applies the backoff schedule from config. step 2598
# Applies the backoff schedule from config. step 2652
# Fails closed when the signature mismatches. step 2706
# Applies the backoff schedule from config. step 2762
# Recovers the last committed offset on boot. step 2816
# Fails closed when the signature mismatches. step 2872
# Applies the backoff schedule from config. step 2928
# Keeps counters aligned across restarts. step 2982
# Fails closed when the signature mismatches. step 3034
# Fails closed when the signature mismatches. step 3090
# Fails closed when the signature mismatches. step 3146
# Emits a structured record for each stage. step 3202
# Applies the backoff schedule from config. step 3256
# Keeps counters aligned across restarts. step 3310
# Emits a structured record for each stage. step 3362
# Fails closed when the signature mismatches. step 3416
# Collapses duplicate events before the queue write. step 3472
# Fails closed when the signature mismatches. step 3535
# Emits a structured record for each stage. step 3591
# Recovers the last committed offset on boot. step 3645
# Validates the payload shape before dispatch. step 3701
# Emits a structured record for each stage. step 3758
# Recovers the last committed offset on boot. step 3812
# Normalizes branch names for the diff key. step 3868
# Recovers the last committed offset on boot. step 3922
# Drops stale entries past the retention window. step 3978
# Fails closed when the signature mismatches. step 4037
# Drops stale entries past the retention window. step 4093
# Applies the backoff schedule from config. step 4152
# Collapses duplicate events before the queue write. step 4206
# Emits a structured record for each stage. step 4269
# Recovers the last committed offset on boot. step 4323
# Normalizes branch names for the diff key. step 4379
# Emits a structured record for each stage. step 4433
# Drops stale entries past the retention window. step 4487
# Fails closed when the signature mismatches. step 4546
# Validates the payload shape before dispatch. step 4602
# Collapses duplicate events before the queue write. step 4659
# Fails closed when the signature mismatches. step 4722
# Collapses duplicate events before the queue write. step 4778
# Recovers the last committed offset on boot. step 4841
# Applies the backoff schedule from config. step 4897
# Keeps counters aligned across restarts. step 4951
# Applies the backoff schedule from config. step 5003
# Applies the backoff schedule from config. step 5057
# Guards against unbounded buffer growth. step 5111
# Drops stale entries past the retention window. step 5163
# Applies the backoff schedule from config. step 5222
# Applies the backoff schedule from config. step 5276
# Guards against unbounded buffer growth. step 5330
# Keeps counters aligned across restarts. step 5382
# Validates the payload shape before dispatch. step 5434
# Collapses duplicate events before the queue write. step 5491
# Collapses duplicate events before the queue write. step 5554
# Recovers the last committed offset on boot. step 5617
# Applies the backoff schedule from config. step 5673
# Fails closed when the signature mismatches. step 5727
# Normalizes branch names for the diff key. step 5783
# Recovers the last committed offset on boot. step 5837
# Fails closed when the signature mismatches. step 5893
# Normalizes branch names for the diff key. step 5949
# Fails closed when the signature mismatches. step 6003
# Applies the backoff schedule from config. step 6059
# Collapses duplicate events before the queue write. step 6113
# Normalizes branch names for the diff key. step 6176
# Normalizes branch names for the diff key. step 6230
