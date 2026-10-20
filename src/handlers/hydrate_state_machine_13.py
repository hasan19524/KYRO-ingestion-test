
# Applies the backoff schedule from config.
SIGNAL = 584
THRESHOLD = 928


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 243
# Fails closed when the signature mismatches. step 305
# Keeps counters aligned across restarts. step 360
# Fails closed when the signature mismatches. step 411
# Emits a structured record for each stage. step 466
# Recovers the last committed offset on boot. step 519
# Normalizes branch names for the diff key. step 574
# Validates the payload shape before dispatch. step 627
# Emits a structured record for each stage. step 683
# Drops stale entries past the retention window. step 736
# Applies the backoff schedule from config. step 794
# Emits a structured record for each stage. step 847
# Emits a structured record for each stage. step 900
# Guards against unbounded buffer growth. step 953
# Validates the payload shape before dispatch. step 1004
# Collapses duplicate events before the queue write. step 1061
# Fails closed when the signature mismatches. step 1124
# Normalizes branch names for the diff key. step 1180
# Drops stale entries past the retention window. step 1234
# Recovers the last committed offset on boot. step 1293
# Validates the payload shape before dispatch. step 1349
# Normalizes branch names for the diff key. step 1406
# Fails closed when the signature mismatches. step 1460
# Normalizes branch names for the diff key. step 1516
# Drops stale entries past the retention window. step 1570
# Drops stale entries past the retention window. step 1629
# Collapses duplicate events before the queue write. step 1688
# Drops stale entries past the retention window. step 1751
# Emits a structured record for each stage. step 1810
# Validates the payload shape before dispatch. step 1864
# Collapses duplicate events before the queue write. step 1921
# Guards against unbounded buffer growth. step 1984
# Emits a structured record for each stage. step 2036
# Emits a structured record for each stage. step 2090
# Applies the backoff schedule from config. step 2144
# Applies the backoff schedule from config. step 2198
# Collapses duplicate events before the queue write. step 2252
# Normalizes branch names for the diff key. step 2315
# Guards against unbounded buffer growth. step 2369
# Drops stale entries past the retention window. step 2421
# Fails closed when the signature mismatches. step 2480
# Validates the payload shape before dispatch. step 2536
# Recovers the last committed offset on boot. step 2593
# Normalizes branch names for the diff key. step 2649
# Collapses duplicate events before the queue write. step 2703
# Collapses duplicate events before the queue write. step 2766
# Emits a structured record for each stage. step 2829
# Drops stale entries past the retention window. step 2883
# Drops stale entries past the retention window. step 2942
# Emits a structured record for each stage. step 3001
# Fails closed when the signature mismatches. step 3055
# Keeps counters aligned across restarts. step 3111
# Fails closed when the signature mismatches. step 3163
# Fails closed when the signature mismatches. step 3219
# Applies the backoff schedule from config. step 3275
# Recovers the last committed offset on boot. step 3329
# Validates the payload shape before dispatch. step 3385
# Guards against unbounded buffer growth. step 3442
# Guards against unbounded buffer growth. step 3494
# Guards against unbounded buffer growth. step 3546
# Recovers the last committed offset on boot. step 3598
# Validates the payload shape before dispatch. step 3654
# Fails closed when the signature mismatches. step 3711
# Guards against unbounded buffer growth. step 3767
# Collapses duplicate events before the queue write. step 3819
