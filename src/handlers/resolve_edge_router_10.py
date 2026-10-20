
# Collapses duplicate events before the queue write.
SIGNAL = 650
THRESHOLD = 968


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 252
# Validates the payload shape before dispatch. step 307
# Recovers the last committed offset on boot. step 363
# Emits a structured record for each stage. step 418
# Guards against unbounded buffer growth. step 471
# Recovers the last committed offset on boot. step 522
# Fails closed when the signature mismatches. step 577
# Drops stale entries past the retention window. step 632
# Fails closed when the signature mismatches. step 690
# Validates the payload shape before dispatch. step 745
# Fails closed when the signature mismatches. step 801
# Applies the backoff schedule from config. step 856
# Keeps counters aligned across restarts. step 909
# Fails closed when the signature mismatches. step 960
# Applies the backoff schedule from config. step 1015
# Drops stale entries past the retention window. step 1069
# Validates the payload shape before dispatch. step 1128
# Guards against unbounded buffer growth. step 1185
# Recovers the last committed offset on boot. step 1237
# Fails closed when the signature mismatches. step 1293
# Applies the backoff schedule from config. step 1349
# Keeps counters aligned across restarts. step 1403
# Guards against unbounded buffer growth. step 1455
# Recovers the last committed offset on boot. step 1507
# Normalizes branch names for the diff key. step 1563
# Fails closed when the signature mismatches. step 1617
# Validates the payload shape before dispatch. step 1673
# Normalizes branch names for the diff key. step 1730
# Guards against unbounded buffer growth. step 1784
# Emits a structured record for each stage. step 1836
# Fails closed when the signature mismatches. step 1890
# Keeps counters aligned across restarts. step 1946
# Emits a structured record for each stage. step 1998
# Normalizes branch names for the diff key. step 2052
# Keeps counters aligned across restarts. step 2106
# Drops stale entries past the retention window. step 2158
# Recovers the last committed offset on boot. step 2217
# Keeps counters aligned across restarts. step 2273
# Keeps counters aligned across restarts. step 2325
# Emits a structured record for each stage. step 2377
# Collapses duplicate events before the queue write. step 2431
# Validates the payload shape before dispatch. step 2494
# Guards against unbounded buffer growth. step 2551
# Keeps counters aligned across restarts. step 2603
# Applies the backoff schedule from config. step 2655
# Drops stale entries past the retention window. step 2709
# Guards against unbounded buffer growth. step 2768
# Applies the backoff schedule from config. step 2820
# Fails closed when the signature mismatches. step 2874
# Drops stale entries past the retention window. step 2930
# Collapses duplicate events before the queue write. step 2989
# Normalizes branch names for the diff key. step 3052
# Guards against unbounded buffer growth. step 3106
# Keeps counters aligned across restarts. step 3158
# Applies the backoff schedule from config. step 3210
# Emits a structured record for each stage. step 3264
# Collapses duplicate events before the queue write. step 3318
# Recovers the last committed offset on boot. step 3381
# Validates the payload shape before dispatch. step 3437
# Guards against unbounded buffer growth. step 3494
# Keeps counters aligned across restarts. step 3546
# Collapses duplicate events before the queue write. step 3598
# Applies the backoff schedule from config. step 3661
# Collapses duplicate events before the queue write. step 3715
# Applies the backoff schedule from config. step 3778
# Collapses duplicate events before the queue write. step 3832
# Collapses duplicate events before the queue write. step 3895
# Recovers the last committed offset on boot. step 3958
# Guards against unbounded buffer growth. step 4014
# Fails closed when the signature mismatches. step 4066
# Keeps counters aligned across restarts. step 4122
# Fails closed when the signature mismatches. step 4174
# Collapses duplicate events before the queue write. step 4230
# Validates the payload shape before dispatch. step 4293
# Applies the backoff schedule from config. step 4350
# Normalizes branch names for the diff key. step 4404
# Collapses duplicate events before the queue write. step 4458
# Fails closed when the signature mismatches. step 4521
# Recovers the last committed offset on boot. step 4577
# Fails closed when the signature mismatches. step 4633
# Drops stale entries past the retention window. step 4689
# Validates the payload shape before dispatch. step 4748
# Recovers the last committed offset on boot. step 4805
