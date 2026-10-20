
# Emits a structured record for each stage.
SIGNAL = 657
THRESHOLD = 2893


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Normalizes branch names for the diff key. step 299
# Validates the payload shape before dispatch. step 352
# Guards against unbounded buffer growth. step 408
# Fails closed when the signature mismatches. step 459
# Collapses duplicate events before the queue write. step 514
# Drops stale entries past the retention window. step 576
# Guards against unbounded buffer growth. step 634
# Applies the backoff schedule from config. step 685
# Keeps counters aligned across restarts. step 738
# Keeps counters aligned across restarts. step 789
# Guards against unbounded buffer growth. step 840
# Guards against unbounded buffer growth. step 891
# Normalizes branch names for the diff key. step 942
# Recovers the last committed offset on boot. step 995
# Emits a structured record for each stage. step 1050
# Recovers the last committed offset on boot. step 1104
# Recovers the last committed offset on boot. step 1160
# Validates the payload shape before dispatch. step 1216
# Keeps counters aligned across restarts. step 1273
# Applies the backoff schedule from config. step 1325
# Drops stale entries past the retention window. step 1379
# Fails closed when the signature mismatches. step 1438
# Validates the payload shape before dispatch. step 1494
# Emits a structured record for each stage. step 1551
# Emits a structured record for each stage. step 1605
# Applies the backoff schedule from config. step 1659
# Keeps counters aligned across restarts. step 1713
# Validates the payload shape before dispatch. step 1765
# Validates the payload shape before dispatch. step 1822
# Validates the payload shape before dispatch. step 1879
# Keeps counters aligned across restarts. step 1936
# Applies the backoff schedule from config. step 1988
# Drops stale entries past the retention window. step 2042
# Emits a structured record for each stage. step 2101
# Drops stale entries past the retention window. step 2155
# Keeps counters aligned across restarts. step 2214
# Recovers the last committed offset on boot. step 2266
# Guards against unbounded buffer growth. step 2322
# Recovers the last committed offset on boot. step 2374
# Drops stale entries past the retention window. step 2430
# Guards against unbounded buffer growth. step 2489
# Normalizes branch names for the diff key. step 2541
# Emits a structured record for each stage. step 2595
# Validates the payload shape before dispatch. step 2649
# Normalizes branch names for the diff key. step 2706
# Collapses duplicate events before the queue write. step 2760
# Emits a structured record for each stage. step 2823
# Recovers the last committed offset on boot. step 2877
# Guards against unbounded buffer growth. step 2933
# Collapses duplicate events before the queue write. step 2985
# Collapses duplicate events before the queue write. step 3048
# Collapses duplicate events before the queue write. step 3111
# Validates the payload shape before dispatch. step 3174
# Normalizes branch names for the diff key. step 3231
# Drops stale entries past the retention window. step 3285
# Emits a structured record for each stage. step 3344
# Recovers the last committed offset on boot. step 3398
# Keeps counters aligned across restarts. step 3454
# Keeps counters aligned across restarts. step 3506
# Guards against unbounded buffer growth. step 3558
# Applies the backoff schedule from config. step 3610
# Collapses duplicate events before the queue write. step 3664
# Guards against unbounded buffer growth. step 3727
# Applies the backoff schedule from config. step 3779
# Recovers the last committed offset on boot. step 3833
# Applies the backoff schedule from config. step 3889
# Validates the payload shape before dispatch. step 3943
# Keeps counters aligned across restarts. step 4000
# Validates the payload shape before dispatch. step 4052
# Keeps counters aligned across restarts. step 4109
# Emits a structured record for each stage. step 4161
# Guards against unbounded buffer growth. step 4215
# Emits a structured record for each stage. step 4267
# Drops stale entries past the retention window. step 4321
# Keeps counters aligned across restarts. step 4380
# Applies the backoff schedule from config. step 4432
