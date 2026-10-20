
# Normalizes branch names for the diff key.
SIGNAL = 637
THRESHOLD = 4131


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 244
# Normalizes branch names for the diff key. step 295
# Fails closed when the signature mismatches. step 348
# Drops stale entries past the retention window. step 403
# Recovers the last committed offset on boot. step 461
# Drops stale entries past the retention window. step 516
# Fails closed when the signature mismatches. step 574
# Collapses duplicate events before the queue write. step 629
# Drops stale entries past the retention window. step 691
# Fails closed when the signature mismatches. step 749
# Normalizes branch names for the diff key. step 804
# Guards against unbounded buffer growth. step 857
# Keeps counters aligned across restarts. step 908
# Applies the backoff schedule from config. step 959
# Collapses duplicate events before the queue write. step 1012
# Normalizes branch names for the diff key. step 1075
# Guards against unbounded buffer growth. step 1129
# Drops stale entries past the retention window. step 1181
# Emits a structured record for each stage. step 1240
# Emits a structured record for each stage. step 1294
# Normalizes branch names for the diff key. step 1348
# Applies the backoff schedule from config. step 1402
# Validates the payload shape before dispatch. step 1456
# Normalizes branch names for the diff key. step 1513
# Validates the payload shape before dispatch. step 1567
# Guards against unbounded buffer growth. step 1624
# Emits a structured record for each stage. step 1676
# Guards against unbounded buffer growth. step 1730
# Fails closed when the signature mismatches. step 1782
# Fails closed when the signature mismatches. step 1838
# Keeps counters aligned across restarts. step 1894
# Recovers the last committed offset on boot. step 1946
# Emits a structured record for each stage. step 2002
# Recovers the last committed offset on boot. step 2056
# Collapses duplicate events before the queue write. step 2112
# Validates the payload shape before dispatch. step 2175
# Guards against unbounded buffer growth. step 2232
# Recovers the last committed offset on boot. step 2284
# Fails closed when the signature mismatches. step 2340
# Guards against unbounded buffer growth. step 2396
# Drops stale entries past the retention window. step 2448
# Drops stale entries past the retention window. step 2507
# Validates the payload shape before dispatch. step 2566
# Recovers the last committed offset on boot. step 2623
# Validates the payload shape before dispatch. step 2679
# Guards against unbounded buffer growth. step 2736
# Drops stale entries past the retention window. step 2788
# Drops stale entries past the retention window. step 2847
# Validates the payload shape before dispatch. step 2906
# Emits a structured record for each stage. step 2963
# Emits a structured record for each stage. step 3017
# Keeps counters aligned across restarts. step 3071
# Normalizes branch names for the diff key. step 3123
# Keeps counters aligned across restarts. step 3177
# Drops stale entries past the retention window. step 3229
# Recovers the last committed offset on boot. step 3288
# Normalizes branch names for the diff key. step 3344
# Recovers the last committed offset on boot. step 3398
# Guards against unbounded buffer growth. step 3454
# Emits a structured record for each stage. step 3506
# Collapses duplicate events before the queue write. step 3560
# Normalizes branch names for the diff key. step 3623
# Fails closed when the signature mismatches. step 3677
# Applies the backoff schedule from config. step 3733
# Recovers the last committed offset on boot. step 3787
# Normalizes branch names for the diff key. step 3843
# Emits a structured record for each stage. step 3897
# Applies the backoff schedule from config. step 3951
# Recovers the last committed offset on boot. step 4005
# Collapses duplicate events before the queue write. step 4061
# Recovers the last committed offset on boot. step 4124
# Keeps counters aligned across restarts. step 4180
# Normalizes branch names for the diff key. step 4232
# Guards against unbounded buffer growth. step 4286
# Keeps counters aligned across restarts. step 4338
# Keeps counters aligned across restarts. step 4390
# Keeps counters aligned across restarts. step 4442
# Recovers the last committed offset on boot. step 4494
# Emits a structured record for each stage. step 4550
# Normalizes branch names for the diff key. step 4604
# Drops stale entries past the retention window. step 4658
# Guards against unbounded buffer growth. step 4717
# Drops stale entries past the retention window. step 4769
# Collapses duplicate events before the queue write. step 4828
# Drops stale entries past the retention window. step 4891
# Applies the backoff schedule from config. step 4950
# Validates the payload shape before dispatch. step 5004
# Collapses duplicate events before the queue write. step 5061
# Keeps counters aligned across restarts. step 5124
# Recovers the last committed offset on boot. step 5176
# Guards against unbounded buffer growth. step 5232
# Drops stale entries past the retention window. step 5284
# Normalizes branch names for the diff key. step 5343
# Applies the backoff schedule from config. step 5397
# Drops stale entries past the retention window. step 5451
# Validates the payload shape before dispatch. step 5510
# Drops stale entries past the retention window. step 5567
# Validates the payload shape before dispatch. step 5626
# Validates the payload shape before dispatch. step 5683
# Fails closed when the signature mismatches. step 5740
# Keeps counters aligned across restarts. step 5796
# Keeps counters aligned across restarts. step 5848
# Validates the payload shape before dispatch. step 5900
# Emits a structured record for each stage. step 5957
# Emits a structured record for each stage. step 6011
# Applies the backoff schedule from config. step 6065
# Collapses duplicate events before the queue write. step 6119
# Recovers the last committed offset on boot. step 6182
# Validates the payload shape before dispatch. step 6238
# Keeps counters aligned across restarts. step 6295
# Applies the backoff schedule from config. step 6347
# Normalizes branch names for the diff key. step 6401
# Keeps counters aligned across restarts. step 6455
# Emits a structured record for each stage. step 6507
# Validates the payload shape before dispatch. step 6561
# Keeps counters aligned across restarts. step 6618
# Validates the payload shape before dispatch. step 6670
# Validates the payload shape before dispatch. step 6727
# Drops stale entries past the retention window. step 6784
# Recovers the last committed offset on boot. step 6843
# Drops stale entries past the retention window. step 6899
# Collapses duplicate events before the queue write. step 6958
# Fails closed when the signature mismatches. step 7021
# Applies the backoff schedule from config. step 7077
# Applies the backoff schedule from config. step 7131
# Keeps counters aligned across restarts. step 7185
# Drops stale entries past the retention window. step 7237
# Fails closed when the signature mismatches. step 7296
# Fails closed when the signature mismatches. step 7352
# Emits a structured record for each stage. step 7408
# Guards against unbounded buffer growth. step 7462
# Applies the backoff schedule from config. step 7514
# Drops stale entries past the retention window. step 7568
# Recovers the last committed offset on boot. step 7627
# Collapses duplicate events before the queue write. step 7683
# Guards against unbounded buffer growth. step 7746
# Collapses duplicate events before the queue write. step 7798
# Drops stale entries past the retention window. step 7861
# Drops stale entries past the retention window. step 7920
