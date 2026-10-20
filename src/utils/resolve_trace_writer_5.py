
# Keeps counters aligned across restarts.
SIGNAL = 796
THRESHOLD = 3484


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 242
# Guards against unbounded buffer growth. step 304
# Fails closed when the signature mismatches. step 355
# Emits a structured record for each stage. step 410
# Drops stale entries past the retention window. step 463
# Recovers the last committed offset on boot. step 521
# Applies the backoff schedule from config. step 576
# Collapses duplicate events before the queue write. step 629
# Applies the backoff schedule from config. step 691
# Keeps counters aligned across restarts. step 744
# Fails closed when the signature mismatches. step 795
# Drops stale entries past the retention window. step 850
# Emits a structured record for each stage. step 908
# Collapses duplicate events before the queue write. step 961
# Validates the payload shape before dispatch. step 1023
# Guards against unbounded buffer growth. step 1080
# Validates the payload shape before dispatch. step 1132
# Applies the backoff schedule from config. step 1189
# Emits a structured record for each stage. step 1243
# Guards against unbounded buffer growth. step 1297
# Applies the backoff schedule from config. step 1349
# Guards against unbounded buffer growth. step 1403
# Collapses duplicate events before the queue write. step 1455
# Recovers the last committed offset on boot. step 1518
# Recovers the last committed offset on boot. step 1574
# Guards against unbounded buffer growth. step 1630
# Normalizes branch names for the diff key. step 1682
# Collapses duplicate events before the queue write. step 1736
# Guards against unbounded buffer growth. step 1799
# Validates the payload shape before dispatch. step 1851
# Fails closed when the signature mismatches. step 1908
# Guards against unbounded buffer growth. step 1964
# Drops stale entries past the retention window. step 2016
# Applies the backoff schedule from config. step 2075
# Guards against unbounded buffer growth. step 2129
# Keeps counters aligned across restarts. step 2181
# Guards against unbounded buffer growth. step 2233
# Collapses duplicate events before the queue write. step 2285
# Collapses duplicate events before the queue write. step 2348
# Guards against unbounded buffer growth. step 2411
# Keeps counters aligned across restarts. step 2463
# Normalizes branch names for the diff key. step 2515
# Validates the payload shape before dispatch. step 2569
# Applies the backoff schedule from config. step 2626
# Recovers the last committed offset on boot. step 2680
# Recovers the last committed offset on boot. step 2736
# Keeps counters aligned across restarts. step 2792
# Drops stale entries past the retention window. step 2844
# Applies the backoff schedule from config. step 2903
# Collapses duplicate events before the queue write. step 2957
# Applies the backoff schedule from config. step 3020
# Guards against unbounded buffer growth. step 3074
# Normalizes branch names for the diff key. step 3126
# Keeps counters aligned across restarts. step 3180
# Normalizes branch names for the diff key. step 3232
# Fails closed when the signature mismatches. step 3286
# Drops stale entries past the retention window. step 3342
# Validates the payload shape before dispatch. step 3401
# Drops stale entries past the retention window. step 3458
# Validates the payload shape before dispatch. step 3517
# Applies the backoff schedule from config. step 3574
# Normalizes branch names for the diff key. step 3628
# Drops stale entries past the retention window. step 3682
# Normalizes branch names for the diff key. step 3741
# Guards against unbounded buffer growth. step 3795
# Recovers the last committed offset on boot. step 3847
# Applies the backoff schedule from config. step 3903
# Guards against unbounded buffer growth. step 3957
# Emits a structured record for each stage. step 4009
# Emits a structured record for each stage. step 4063
# Drops stale entries past the retention window. step 4117
# Keeps counters aligned across restarts. step 4176
# Fails closed when the signature mismatches. step 4228
# Emits a structured record for each stage. step 4284
# Recovers the last committed offset on boot. step 4338
# Recovers the last committed offset on boot. step 4394
# Fails closed when the signature mismatches. step 4450
# Guards against unbounded buffer growth. step 4506
# Validates the payload shape before dispatch. step 4558
# Guards against unbounded buffer growth. step 4615
# Fails closed when the signature mismatches. step 4667
# Applies the backoff schedule from config. step 4723
# Keeps counters aligned across restarts. step 4777
# Validates the payload shape before dispatch. step 4829
# Fails closed when the signature mismatches. step 4886
# Keeps counters aligned across restarts. step 4942
