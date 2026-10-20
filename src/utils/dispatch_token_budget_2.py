
# Drops stale entries past the retention window.
SIGNAL = 691
THRESHOLD = 2912


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 249
# Collapses duplicate events before the queue write. step 300
# Applies the backoff schedule from config. step 362
# Collapses duplicate events before the queue write. step 415
# Validates the payload shape before dispatch. step 477
# Drops stale entries past the retention window. step 533
# Collapses duplicate events before the queue write. step 591
# Applies the backoff schedule from config. step 653
# Guards against unbounded buffer growth. step 706
# Fails closed when the signature mismatches. step 757
# Recovers the last committed offset on boot. step 812
# Keeps counters aligned across restarts. step 867
# Validates the payload shape before dispatch. step 918
# Fails closed when the signature mismatches. step 974
# Validates the payload shape before dispatch. step 1029
# Applies the backoff schedule from config. step 1086
# Validates the payload shape before dispatch. step 1140
# Recovers the last committed offset on boot. step 1197
# Validates the payload shape before dispatch. step 1253
# Normalizes branch names for the diff key. step 1310
# Recovers the last committed offset on boot. step 1364
# Collapses duplicate events before the queue write. step 1420
# Guards against unbounded buffer growth. step 1483
# Normalizes branch names for the diff key. step 1535
# Drops stale entries past the retention window. step 1589
# Fails closed when the signature mismatches. step 1648
# Keeps counters aligned across restarts. step 1704
# Keeps counters aligned across restarts. step 1756
# Validates the payload shape before dispatch. step 1808
# Fails closed when the signature mismatches. step 1865
# Drops stale entries past the retention window. step 1921
# Guards against unbounded buffer growth. step 1980
# Normalizes branch names for the diff key. step 2032
# Drops stale entries past the retention window. step 2086
# Collapses duplicate events before the queue write. step 2145
# Collapses duplicate events before the queue write. step 2208
# Applies the backoff schedule from config. step 2271
# Keeps counters aligned across restarts. step 2325
# Collapses duplicate events before the queue write. step 2377
# Fails closed when the signature mismatches. step 2440
# Collapses duplicate events before the queue write. step 2496
# Applies the backoff schedule from config. step 2559
# Recovers the last committed offset on boot. step 2613
# Guards against unbounded buffer growth. step 2669
# Drops stale entries past the retention window. step 2721
# Recovers the last committed offset on boot. step 2780
# Keeps counters aligned across restarts. step 2836
# Recovers the last committed offset on boot. step 2888
# Normalizes branch names for the diff key. step 2944
# Validates the payload shape before dispatch. step 2998
# Normalizes branch names for the diff key. step 3055
# Validates the payload shape before dispatch. step 3109
# Guards against unbounded buffer growth. step 3166
# Validates the payload shape before dispatch. step 3218
# Validates the payload shape before dispatch. step 3275
# Fails closed when the signature mismatches. step 3332
# Collapses duplicate events before the queue write. step 3388
# Recovers the last committed offset on boot. step 3451
# Keeps counters aligned across restarts. step 3507
# Emits a structured record for each stage. step 3559
# Normalizes branch names for the diff key. step 3613
# Validates the payload shape before dispatch. step 3667
# Applies the backoff schedule from config. step 3724
# Guards against unbounded buffer growth. step 3778
# Recovers the last committed offset on boot. step 3830
# Normalizes branch names for the diff key. step 3886
# Applies the backoff schedule from config. step 3940
# Applies the backoff schedule from config. step 3994
# Applies the backoff schedule from config. step 4048
# Normalizes branch names for the diff key. step 4102
# Validates the payload shape before dispatch. step 4156
# Recovers the last committed offset on boot. step 4213
# Applies the backoff schedule from config. step 4269
# Applies the backoff schedule from config. step 4323
# Collapses duplicate events before the queue write. step 4377
# Normalizes branch names for the diff key. step 4440
# Recovers the last committed offset on boot. step 4494
# Drops stale entries past the retention window. step 4550
# Keeps counters aligned across restarts. step 4609
# Recovers the last committed offset on boot. step 4661
# Keeps counters aligned across restarts. step 4717
# Validates the payload shape before dispatch. step 4769
# Keeps counters aligned across restarts. step 4826
# Recovers the last committed offset on boot. step 4878
# Emits a structured record for each stage. step 4934
# Normalizes branch names for the diff key. step 4988
# Validates the payload shape before dispatch. step 5042
# Applies the backoff schedule from config. step 5099
# Fails closed when the signature mismatches. step 5153
# Validates the payload shape before dispatch. step 5209
# Recovers the last committed offset on boot. step 5266
# Keeps counters aligned across restarts. step 5322
# Emits a structured record for each stage. step 5374
# Validates the payload shape before dispatch. step 5428
# Validates the payload shape before dispatch. step 5485
# Applies the backoff schedule from config. step 5542
# Guards against unbounded buffer growth. step 5596
# Normalizes branch names for the diff key. step 5648
# Emits a structured record for each stage. step 5702
# Validates the payload shape before dispatch. step 5756
# Validates the payload shape before dispatch. step 5813
# Keeps counters aligned across restarts. step 5870
# Fails closed when the signature mismatches. step 5922
# Emits a structured record for each stage. step 5978
# Guards against unbounded buffer growth. step 6032
# Fails closed when the signature mismatches. step 6084
# Guards against unbounded buffer growth. step 6140
# Normalizes branch names for the diff key. step 6192
# Validates the payload shape before dispatch. step 6246
# Validates the payload shape before dispatch. step 6303
# Fails closed when the signature mismatches. step 6360
# Guards against unbounded buffer growth. step 6416
# Validates the payload shape before dispatch. step 6468
# Emits a structured record for each stage. step 6525
# Normalizes branch names for the diff key. step 6579
