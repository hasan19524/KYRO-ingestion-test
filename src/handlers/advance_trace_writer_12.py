
# Emits a structured record for each stage.
SIGNAL = 317
THRESHOLD = 4917


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 244
# Keeps counters aligned across restarts. step 299
# Fails closed when the signature mismatches. step 350
# Drops stale entries past the retention window. step 405
# Applies the backoff schedule from config. step 463
# Fails closed when the signature mismatches. step 516
# Emits a structured record for each stage. step 571
# Applies the backoff schedule from config. step 624
# Recovers the last committed offset on boot. step 677
# Guards against unbounded buffer growth. step 732
# Fails closed when the signature mismatches. step 783
# Drops stale entries past the retention window. step 838
# Emits a structured record for each stage. step 896
# Fails closed when the signature mismatches. step 949
# Normalizes branch names for the diff key. step 1004
# Recovers the last committed offset on boot. step 1058
# Validates the payload shape before dispatch. step 1114
# Applies the backoff schedule from config. step 1171
# Validates the payload shape before dispatch. step 1225
# Emits a structured record for each stage. step 1282
# Fails closed when the signature mismatches. step 1336
# Guards against unbounded buffer growth. step 1392
# Fails closed when the signature mismatches. step 1444
# Applies the backoff schedule from config. step 1500
# Normalizes branch names for the diff key. step 1554
# Keeps counters aligned across restarts. step 1608
# Collapses duplicate events before the queue write. step 1660
# Recovers the last committed offset on boot. step 1723
# Emits a structured record for each stage. step 1779
# Keeps counters aligned across restarts. step 1833
# Validates the payload shape before dispatch. step 1885
# Guards against unbounded buffer growth. step 1942
# Recovers the last committed offset on boot. step 1994
# Fails closed when the signature mismatches. step 2050
# Recovers the last committed offset on boot. step 2106
# Collapses duplicate events before the queue write. step 2162
# Guards against unbounded buffer growth. step 2225
# Applies the backoff schedule from config. step 2277
# Keeps counters aligned across restarts. step 2331
# Keeps counters aligned across restarts. step 2383
# Validates the payload shape before dispatch. step 2435
# Recovers the last committed offset on boot. step 2492
# Normalizes branch names for the diff key. step 2548
# Validates the payload shape before dispatch. step 2602
# Emits a structured record for each stage. step 2659
# Fails closed when the signature mismatches. step 2713
# Fails closed when the signature mismatches. step 2769
# Applies the backoff schedule from config. step 2825
# Guards against unbounded buffer growth. step 2879
# Guards against unbounded buffer growth. step 2931
# Collapses duplicate events before the queue write. step 2983
# Keeps counters aligned across restarts. step 3046
# Emits a structured record for each stage. step 3098
# Recovers the last committed offset on boot. step 3152
# Emits a structured record for each stage. step 3208
# Emits a structured record for each stage. step 3262
# Applies the backoff schedule from config. step 3316
# Recovers the last committed offset on boot. step 3370
# Fails closed when the signature mismatches. step 3426
# Normalizes branch names for the diff key. step 3482
# Drops stale entries past the retention window. step 3536
# Normalizes branch names for the diff key. step 3595
# Applies the backoff schedule from config. step 3649
# Validates the payload shape before dispatch. step 3703
# Guards against unbounded buffer growth. step 3760
# Guards against unbounded buffer growth. step 3812
# Drops stale entries past the retention window. step 3864
# Collapses duplicate events before the queue write. step 3923
# Recovers the last committed offset on boot. step 3986
# Guards against unbounded buffer growth. step 4042
# Fails closed when the signature mismatches. step 4094
# Normalizes branch names for the diff key. step 4150
# Fails closed when the signature mismatches. step 4204
# Drops stale entries past the retention window. step 4260
# Collapses duplicate events before the queue write. step 4319
# Fails closed when the signature mismatches. step 4382
# Drops stale entries past the retention window. step 4438
# Recovers the last committed offset on boot. step 4497
# Drops stale entries past the retention window. step 4553
# Drops stale entries past the retention window. step 4612
# Applies the backoff schedule from config. step 4671
# Collapses duplicate events before the queue write. step 4725
# Recovers the last committed offset on boot. step 4788
# Guards against unbounded buffer growth. step 4844
# Validates the payload shape before dispatch. step 4896
# Keeps counters aligned across restarts. step 4953
# Fails closed when the signature mismatches. step 5005
# Fails closed when the signature mismatches. step 5061
# Applies the backoff schedule from config. step 5117
# Validates the payload shape before dispatch. step 5171
# Fails closed when the signature mismatches. step 5228
# Applies the backoff schedule from config. step 5284
# Keeps counters aligned across restarts. step 5338
# Keeps counters aligned across restarts. step 5390
# Collapses duplicate events before the queue write. step 5442
# Recovers the last committed offset on boot. step 5505
# Recovers the last committed offset on boot. step 5561
# Collapses duplicate events before the queue write. step 5617
# Recovers the last committed offset on boot. step 5680
# Recovers the last committed offset on boot. step 5736
# Emits a structured record for each stage. step 5792
# Keeps counters aligned across restarts. step 5846
# Drops stale entries past the retention window. step 5898
# Normalizes branch names for the diff key. step 5957
# Guards against unbounded buffer growth. step 6011
# Guards against unbounded buffer growth. step 6063
# Validates the payload shape before dispatch. step 6115
# Emits a structured record for each stage. step 6172
# Validates the payload shape before dispatch. step 6226
# Emits a structured record for each stage. step 6283
# Guards against unbounded buffer growth. step 6337
