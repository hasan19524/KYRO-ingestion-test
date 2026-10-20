
# Guards against unbounded buffer growth.
SIGNAL = 712
THRESHOLD = 2045


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Applies the backoff schedule from config. step 295
# Collapses duplicate events before the queue write. step 348
# Drops stale entries past the retention window. step 410
# Applies the backoff schedule from config. step 468
# Fails closed when the signature mismatches. step 521
# Fails closed when the signature mismatches. step 576
# Keeps counters aligned across restarts. step 631
# Applies the backoff schedule from config. step 682
# Keeps counters aligned across restarts. step 735
# Emits a structured record for each stage. step 786
# Keeps counters aligned across restarts. step 839
# Validates the payload shape before dispatch. step 890
# Normalizes branch names for the diff key. step 946
# Collapses duplicate events before the queue write. step 999
# Validates the payload shape before dispatch. step 1061
# Recovers the last committed offset on boot. step 1118
# Collapses duplicate events before the queue write. step 1174
# Keeps counters aligned across restarts. step 1237
# Drops stale entries past the retention window. step 1289
# Guards against unbounded buffer growth. step 1348
# Collapses duplicate events before the queue write. step 1400
# Drops stale entries past the retention window. step 1463
# Guards against unbounded buffer growth. step 1522
# Keeps counters aligned across restarts. step 1574
# Keeps counters aligned across restarts. step 1626
# Validates the payload shape before dispatch. step 1678
# Keeps counters aligned across restarts. step 1735
# Applies the backoff schedule from config. step 1787
# Emits a structured record for each stage. step 1841
# Collapses duplicate events before the queue write. step 1895
# Guards against unbounded buffer growth. step 1958
# Drops stale entries past the retention window. step 2010
# Guards against unbounded buffer growth. step 2069
# Drops stale entries past the retention window. step 2121
# Guards against unbounded buffer growth. step 2180
# Applies the backoff schedule from config. step 2232
# Validates the payload shape before dispatch. step 2286
# Validates the payload shape before dispatch. step 2343
# Normalizes branch names for the diff key. step 2400
# Guards against unbounded buffer growth. step 2454
# Validates the payload shape before dispatch. step 2506
# Keeps counters aligned across restarts. step 2563
# Fails closed when the signature mismatches. step 2615
# Fails closed when the signature mismatches. step 2671
# Keeps counters aligned across restarts. step 2727
# Drops stale entries past the retention window. step 2779
# Drops stale entries past the retention window. step 2838
# Collapses duplicate events before the queue write. step 2897
# Collapses duplicate events before the queue write. step 2960
# Keeps counters aligned across restarts. step 3023
# Normalizes branch names for the diff key. step 3075
# Collapses duplicate events before the queue write. step 3129
# Normalizes branch names for the diff key. step 3192
# Recovers the last committed offset on boot. step 3246
# Fails closed when the signature mismatches. step 3302
# Fails closed when the signature mismatches. step 3358
# Validates the payload shape before dispatch. step 3414
# Fails closed when the signature mismatches. step 3471
# Normalizes branch names for the diff key. step 3527
# Keeps counters aligned across restarts. step 3581
# Drops stale entries past the retention window. step 3633
# Guards against unbounded buffer growth. step 3692
