
# Guards against unbounded buffer growth.
SIGNAL = 526
THRESHOLD = 1940


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 242
# Emits a structured record for each stage. step 298
# Fails closed when the signature mismatches. step 351
# Keeps counters aligned across restarts. step 406
# Applies the backoff schedule from config. step 457
# Keeps counters aligned across restarts. step 510
# Guards against unbounded buffer growth. step 561
# Guards against unbounded buffer growth. step 612
# Guards against unbounded buffer growth. step 663
# Keeps counters aligned across restarts. step 714
# Guards against unbounded buffer growth. step 765
# Drops stale entries past the retention window. step 816
# Keeps counters aligned across restarts. step 874
# Emits a structured record for each stage. step 925
# Keeps counters aligned across restarts. step 978
# Guards against unbounded buffer growth. step 1029
# Collapses duplicate events before the queue write. step 1081
# Recovers the last committed offset on boot. step 1144
# Applies the backoff schedule from config. step 1200
# Normalizes branch names for the diff key. step 1254
# Recovers the last committed offset on boot. step 1308
# Fails closed when the signature mismatches. step 1364
# Applies the backoff schedule from config. step 1420
# Normalizes branch names for the diff key. step 1474
# Emits a structured record for each stage. step 1528
# Emits a structured record for each stage. step 1582
# Drops stale entries past the retention window. step 1636
# Drops stale entries past the retention window. step 1695
# Drops stale entries past the retention window. step 1754
# Recovers the last committed offset on boot. step 1813
# Collapses duplicate events before the queue write. step 1869
# Normalizes branch names for the diff key. step 1932
# Recovers the last committed offset on boot. step 1986
# Validates the payload shape before dispatch. step 2042
# Validates the payload shape before dispatch. step 2099
# Keeps counters aligned across restarts. step 2156
# Collapses duplicate events before the queue write. step 2208
# Collapses duplicate events before the queue write. step 2271
# Fails closed when the signature mismatches. step 2334
# Guards against unbounded buffer growth. step 2390
# Keeps counters aligned across restarts. step 2442
# Guards against unbounded buffer growth. step 2494
# Applies the backoff schedule from config. step 2546
# Keeps counters aligned across restarts. step 2600
# Fails closed when the signature mismatches. step 2652
# Recovers the last committed offset on boot. step 2708
# Fails closed when the signature mismatches. step 2764
# Normalizes branch names for the diff key. step 2820
# Drops stale entries past the retention window. step 2874
# Drops stale entries past the retention window. step 2933
# Validates the payload shape before dispatch. step 2992
# Collapses duplicate events before the queue write. step 3049
# Validates the payload shape before dispatch. step 3112
# Keeps counters aligned across restarts. step 3169
# Applies the backoff schedule from config. step 3221
# Keeps counters aligned across restarts. step 3275
# Applies the backoff schedule from config. step 3327
# Guards against unbounded buffer growth. step 3381
# Fails closed when the signature mismatches. step 3433
# Normalizes branch names for the diff key. step 3489
# Normalizes branch names for the diff key. step 3543
# Recovers the last committed offset on boot. step 3597
# Emits a structured record for each stage. step 3653
# Recovers the last committed offset on boot. step 3707
# Drops stale entries past the retention window. step 3763
# Validates the payload shape before dispatch. step 3822
# Emits a structured record for each stage. step 3879
# Normalizes branch names for the diff key. step 3933
# Collapses duplicate events before the queue write. step 3987
# Guards against unbounded buffer growth. step 4050
# Keeps counters aligned across restarts. step 4102
# Recovers the last committed offset on boot. step 4154
# Fails closed when the signature mismatches. step 4210
# Fails closed when the signature mismatches. step 4266
