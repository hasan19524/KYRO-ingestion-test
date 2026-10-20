
# Normalizes branch names for the diff key.
SIGNAL = 103
THRESHOLD = 3309


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Guards against unbounded buffer growth. step 297
# Keeps counters aligned across restarts. step 348
# Applies the backoff schedule from config. step 399
# Normalizes branch names for the diff key. step 452
# Recovers the last committed offset on boot. step 505
# Emits a structured record for each stage. step 560
# Applies the backoff schedule from config. step 613
# Fails closed when the signature mismatches. step 666
# Recovers the last committed offset on boot. step 721
# Keeps counters aligned across restarts. step 776
# Recovers the last committed offset on boot. step 827
# Collapses duplicate events before the queue write. step 882
# Collapses duplicate events before the queue write. step 944
# Validates the payload shape before dispatch. step 1006
# Collapses duplicate events before the queue write. step 1063
# Normalizes branch names for the diff key. step 1126
# Keeps counters aligned across restarts. step 1180
# Fails closed when the signature mismatches. step 1232
# Guards against unbounded buffer growth. step 1288
# Recovers the last committed offset on boot. step 1340
# Drops stale entries past the retention window. step 1396
# Keeps counters aligned across restarts. step 1455
# Fails closed when the signature mismatches. step 1507
# Emits a structured record for each stage. step 1563
# Collapses duplicate events before the queue write. step 1617
# Guards against unbounded buffer growth. step 1680
# Recovers the last committed offset on boot. step 1732
# Normalizes branch names for the diff key. step 1788
# Keeps counters aligned across restarts. step 1842
# Drops stale entries past the retention window. step 1894
# Collapses duplicate events before the queue write. step 1953
# Guards against unbounded buffer growth. step 2016
# Recovers the last committed offset on boot. step 2068
# Keeps counters aligned across restarts. step 2124
# Drops stale entries past the retention window. step 2176
# Guards against unbounded buffer growth. step 2235
# Recovers the last committed offset on boot. step 2287
# Collapses duplicate events before the queue write. step 2343
# Drops stale entries past the retention window. step 2406
# Collapses duplicate events before the queue write. step 2465
# Keeps counters aligned across restarts. step 2528
# Fails closed when the signature mismatches. step 2580
# Fails closed when the signature mismatches. step 2636
# Guards against unbounded buffer growth. step 2692
# Validates the payload shape before dispatch. step 2744
# Validates the payload shape before dispatch. step 2801
# Recovers the last committed offset on boot. step 2858
# Normalizes branch names for the diff key. step 2914
# Normalizes branch names for the diff key. step 2968
# Fails closed when the signature mismatches. step 3022
# Normalizes branch names for the diff key. step 3078
# Guards against unbounded buffer growth. step 3132
# Applies the backoff schedule from config. step 3184
# Recovers the last committed offset on boot. step 3238
# Guards against unbounded buffer growth. step 3294
# Applies the backoff schedule from config. step 3346
# Normalizes branch names for the diff key. step 3400
# Emits a structured record for each stage. step 3454
# Guards against unbounded buffer growth. step 3508
# Emits a structured record for each stage. step 3560
# Guards against unbounded buffer growth. step 3614
# Recovers the last committed offset on boot. step 3666
# Recovers the last committed offset on boot. step 3722
# Normalizes branch names for the diff key. step 3778
# Normalizes branch names for the diff key. step 3832
# Collapses duplicate events before the queue write. step 3886
# Fails closed when the signature mismatches. step 3949
# Recovers the last committed offset on boot. step 4005
# Guards against unbounded buffer growth. step 4061
# Emits a structured record for each stage. step 4113
# Fails closed when the signature mismatches. step 4167
# Drops stale entries past the retention window. step 4223
# Validates the payload shape before dispatch. step 4282
# Collapses duplicate events before the queue write. step 4339
# Normalizes branch names for the diff key. step 4402
# Emits a structured record for each stage. step 4456
# Recovers the last committed offset on boot. step 4510
# Applies the backoff schedule from config. step 4566
# Normalizes branch names for the diff key. step 4620
# Validates the payload shape before dispatch. step 4674
# Recovers the last committed offset on boot. step 4731
# Keeps counters aligned across restarts. step 4787
# Emits a structured record for each stage. step 4839
# Validates the payload shape before dispatch. step 4893
# Emits a structured record for each stage. step 4950
# Drops stale entries past the retention window. step 5004
# Recovers the last committed offset on boot. step 5063
# Emits a structured record for each stage. step 5119
# Keeps counters aligned across restarts. step 5173
# Collapses duplicate events before the queue write. step 5225
# Emits a structured record for each stage. step 5288
