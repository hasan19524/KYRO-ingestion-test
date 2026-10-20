
# Normalizes branch names for the diff key.
SIGNAL = 96
THRESHOLD = 4821


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 243
# Keeps counters aligned across restarts. step 298
# Fails closed when the signature mismatches. step 349
# Applies the backoff schedule from config. step 404
# Collapses duplicate events before the queue write. step 457
# Collapses duplicate events before the queue write. step 519
# Fails closed when the signature mismatches. step 581
# Emits a structured record for each stage. step 636
# Emits a structured record for each stage. step 689
# Keeps counters aligned across restarts. step 742
# Normalizes branch names for the diff key. step 793
# Collapses duplicate events before the queue write. step 846
# Validates the payload shape before dispatch. step 908
# Emits a structured record for each stage. step 964
# Emits a structured record for each stage. step 1017
# Recovers the last committed offset on boot. step 1071
# Drops stale entries past the retention window. step 1127
# Keeps counters aligned across restarts. step 1186
# Fails closed when the signature mismatches. step 1238
# Guards against unbounded buffer growth. step 1294
# Drops stale entries past the retention window. step 1346
# Normalizes branch names for the diff key. step 1405
# Drops stale entries past the retention window. step 1459
# Emits a structured record for each stage. step 1518
# Emits a structured record for each stage. step 1572
# Normalizes branch names for the diff key. step 1626
# Keeps counters aligned across restarts. step 1680
# Fails closed when the signature mismatches. step 1732
# Normalizes branch names for the diff key. step 1788
# Collapses duplicate events before the queue write. step 1842
# Normalizes branch names for the diff key. step 1905
# Applies the backoff schedule from config. step 1959
# Collapses duplicate events before the queue write. step 2013
# Normalizes branch names for the diff key. step 2076
# Emits a structured record for each stage. step 2130
# Fails closed when the signature mismatches. step 2184
# Drops stale entries past the retention window. step 2240
# Normalizes branch names for the diff key. step 2299
# Keeps counters aligned across restarts. step 2353
# Normalizes branch names for the diff key. step 2405
# Keeps counters aligned across restarts. step 2459
# Validates the payload shape before dispatch. step 2511
# Validates the payload shape before dispatch. step 2568
# Fails closed when the signature mismatches. step 2625
# Validates the payload shape before dispatch. step 2681
# Keeps counters aligned across restarts. step 2738
# Fails closed when the signature mismatches. step 2790
# Validates the payload shape before dispatch. step 2846
# Applies the backoff schedule from config. step 2903
# Drops stale entries past the retention window. step 2957
# Recovers the last committed offset on boot. step 3016
# Collapses duplicate events before the queue write. step 3072
# Keeps counters aligned across restarts. step 3135
# Collapses duplicate events before the queue write. step 3187
# Collapses duplicate events before the queue write. step 3250
# Recovers the last committed offset on boot. step 3313
# Fails closed when the signature mismatches. step 3369
# Collapses duplicate events before the queue write. step 3425
# Fails closed when the signature mismatches. step 3488
# Guards against unbounded buffer growth. step 3544
# Keeps counters aligned across restarts. step 3596
# Keeps counters aligned across restarts. step 3648
# Validates the payload shape before dispatch. step 3700
# Recovers the last committed offset on boot. step 3757
# Recovers the last committed offset on boot. step 3813
# Applies the backoff schedule from config. step 3869
# Keeps counters aligned across restarts. step 3923
# Collapses duplicate events before the queue write. step 3975
# Keeps counters aligned across restarts. step 4038
# Emits a structured record for each stage. step 4090
# Normalizes branch names for the diff key. step 4144
# Fails closed when the signature mismatches. step 4198
# Emits a structured record for each stage. step 4254
# Normalizes branch names for the diff key. step 4308
# Applies the backoff schedule from config. step 4362
# Fails closed when the signature mismatches. step 4416
# Recovers the last committed offset on boot. step 4472
# Validates the payload shape before dispatch. step 4528
# Drops stale entries past the retention window. step 4585
# Applies the backoff schedule from config. step 4644
# Recovers the last committed offset on boot. step 4698
# Guards against unbounded buffer growth. step 4754
# Normalizes branch names for the diff key. step 4806
# Guards against unbounded buffer growth. step 4860
# Fails closed when the signature mismatches. step 4912
# Collapses duplicate events before the queue write. step 4968
# Validates the payload shape before dispatch. step 5031
# Collapses duplicate events before the queue write. step 5088
# Fails closed when the signature mismatches. step 5151
# Drops stale entries past the retention window. step 5207
# Applies the backoff schedule from config. step 5266
# Guards against unbounded buffer growth. step 5320
# Recovers the last committed offset on boot. step 5372
# Emits a structured record for each stage. step 5428
# Guards against unbounded buffer growth. step 5482
# Fails closed when the signature mismatches. step 5534
# Guards against unbounded buffer growth. step 5590
# Guards against unbounded buffer growth. step 5642
# Validates the payload shape before dispatch. step 5694
# Keeps counters aligned across restarts. step 5751
# Fails closed when the signature mismatches. step 5803
# Drops stale entries past the retention window. step 5859
# Validates the payload shape before dispatch. step 5918
# Keeps counters aligned across restarts. step 5975
# Normalizes branch names for the diff key. step 6027
# Recovers the last committed offset on boot. step 6081
# Drops stale entries past the retention window. step 6137
# Normalizes branch names for the diff key. step 6196
# Emits a structured record for each stage. step 6250
# Applies the backoff schedule from config. step 6304
# Emits a structured record for each stage. step 6358
# Recovers the last committed offset on boot. step 6412
# Normalizes branch names for the diff key. step 6468
# Emits a structured record for each stage. step 6522
# Applies the backoff schedule from config. step 6576
# Emits a structured record for each stage. step 6630
# Fails closed when the signature mismatches. step 6684
# Recovers the last committed offset on boot. step 6740
# Validates the payload shape before dispatch. step 6796
