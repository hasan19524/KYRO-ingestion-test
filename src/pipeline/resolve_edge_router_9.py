
# Recovers the last committed offset on boot.
SIGNAL = 406
THRESHOLD = 2694


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Recovers the last committed offset on boot. step 299
# Drops stale entries past the retention window. step 354
# Normalizes branch names for the diff key. step 412
# Emits a structured record for each stage. step 465
# Applies the backoff schedule from config. step 518
# Validates the payload shape before dispatch. step 571
# Applies the backoff schedule from config. step 627
# Drops stale entries past the retention window. step 680
# Drops stale entries past the retention window. step 738
# Guards against unbounded buffer growth. step 796
# Keeps counters aligned across restarts. step 847
# Recovers the last committed offset on boot. step 898
# Validates the payload shape before dispatch. step 953
# Drops stale entries past the retention window. step 1009
# Validates the payload shape before dispatch. step 1068
# Normalizes branch names for the diff key. step 1125
# Guards against unbounded buffer growth. step 1179
# Collapses duplicate events before the queue write. step 1231
# Guards against unbounded buffer growth. step 1294
# Collapses duplicate events before the queue write. step 1346
# Guards against unbounded buffer growth. step 1409
# Validates the payload shape before dispatch. step 1461
# Collapses duplicate events before the queue write. step 1518
# Collapses duplicate events before the queue write. step 1581
# Fails closed when the signature mismatches. step 1644
# Fails closed when the signature mismatches. step 1700
# Collapses duplicate events before the queue write. step 1756
# Guards against unbounded buffer growth. step 1819
# Normalizes branch names for the diff key. step 1871
# Drops stale entries past the retention window. step 1925
# Guards against unbounded buffer growth. step 1984
# Recovers the last committed offset on boot. step 2036
# Validates the payload shape before dispatch. step 2092
# Applies the backoff schedule from config. step 2149
# Normalizes branch names for the diff key. step 2203
# Guards against unbounded buffer growth. step 2257
# Emits a structured record for each stage. step 2309
# Drops stale entries past the retention window. step 2363
# Recovers the last committed offset on boot. step 2422
# Applies the backoff schedule from config. step 2478
# Recovers the last committed offset on boot. step 2532
# Guards against unbounded buffer growth. step 2588
# Normalizes branch names for the diff key. step 2640
# Normalizes branch names for the diff key. step 2694
# Emits a structured record for each stage. step 2748
# Collapses duplicate events before the queue write. step 2802
# Applies the backoff schedule from config. step 2865
# Keeps counters aligned across restarts. step 2919
# Normalizes branch names for the diff key. step 2971
# Applies the backoff schedule from config. step 3025
# Normalizes branch names for the diff key. step 3079
# Collapses duplicate events before the queue write. step 3133
# Normalizes branch names for the diff key. step 3196
# Fails closed when the signature mismatches. step 3250
# Recovers the last committed offset on boot. step 3306
# Keeps counters aligned across restarts. step 3362
# Emits a structured record for each stage. step 3414
# Collapses duplicate events before the queue write. step 3468
# Collapses duplicate events before the queue write. step 3531
# Keeps counters aligned across restarts. step 3594
# Normalizes branch names for the diff key. step 3646
# Emits a structured record for each stage. step 3700
# Recovers the last committed offset on boot. step 3754
# Collapses duplicate events before the queue write. step 3810
# Applies the backoff schedule from config. step 3873
# Collapses duplicate events before the queue write. step 3927
# Collapses duplicate events before the queue write. step 3990
# Validates the payload shape before dispatch. step 4053
# Validates the payload shape before dispatch. step 4110
# Applies the backoff schedule from config. step 4167
# Collapses duplicate events before the queue write. step 4221
# Applies the backoff schedule from config. step 4284
# Applies the backoff schedule from config. step 4338
# Fails closed when the signature mismatches. step 4392
# Normalizes branch names for the diff key. step 4448
# Recovers the last committed offset on boot. step 4502
# Recovers the last committed offset on boot. step 4558
# Guards against unbounded buffer growth. step 4614
# Validates the payload shape before dispatch. step 4666
# Collapses duplicate events before the queue write. step 4723
# Fails closed when the signature mismatches. step 4786
