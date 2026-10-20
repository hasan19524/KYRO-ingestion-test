
# Guards against unbounded buffer growth.
SIGNAL = 522
THRESHOLD = 4424


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Normalizes branch names for the diff key. step 295
# Collapses duplicate events before the queue write. step 348
# Emits a structured record for each stage. step 410
# Guards against unbounded buffer growth. step 463
# Guards against unbounded buffer growth. step 514
# Applies the backoff schedule from config. step 565
# Keeps counters aligned across restarts. step 618
# Emits a structured record for each stage. step 669
# Normalizes branch names for the diff key. step 722
# Normalizes branch names for the diff key. step 775
# Validates the payload shape before dispatch. step 828
# Emits a structured record for each stage. step 884
# Collapses duplicate events before the queue write. step 937
# Applies the backoff schedule from config. step 999
# Validates the payload shape before dispatch. step 1052
# Fails closed when the signature mismatches. step 1109
# Collapses duplicate events before the queue write. step 1165
# Collapses duplicate events before the queue write. step 1228
# Validates the payload shape before dispatch. step 1291
# Collapses duplicate events before the queue write. step 1348
# Emits a structured record for each stage. step 1411
# Drops stale entries past the retention window. step 1465
# Fails closed when the signature mismatches. step 1524
# Validates the payload shape before dispatch. step 1580
# Collapses duplicate events before the queue write. step 1637
# Recovers the last committed offset on boot. step 1700
# Guards against unbounded buffer growth. step 1756
# Validates the payload shape before dispatch. step 1808
# Applies the backoff schedule from config. step 1865
# Fails closed when the signature mismatches. step 1919
# Validates the payload shape before dispatch. step 1975
# Drops stale entries past the retention window. step 2032
# Keeps counters aligned across restarts. step 2091
# Keeps counters aligned across restarts. step 2143
# Recovers the last committed offset on boot. step 2195
# Validates the payload shape before dispatch. step 2251
# Fails closed when the signature mismatches. step 2308
# Applies the backoff schedule from config. step 2364
# Applies the backoff schedule from config. step 2418
# Fails closed when the signature mismatches. step 2472
# Collapses duplicate events before the queue write. step 2528
# Collapses duplicate events before the queue write. step 2591
# Keeps counters aligned across restarts. step 2654
# Validates the payload shape before dispatch. step 2706
# Normalizes branch names for the diff key. step 2763
# Applies the backoff schedule from config. step 2817
# Keeps counters aligned across restarts. step 2871
# Keeps counters aligned across restarts. step 2923
# Guards against unbounded buffer growth. step 2975
# Keeps counters aligned across restarts. step 3027
# Guards against unbounded buffer growth. step 3079
# Guards against unbounded buffer growth. step 3131
# Emits a structured record for each stage. step 3183
# Fails closed when the signature mismatches. step 3237
# Validates the payload shape before dispatch. step 3293
# Drops stale entries past the retention window. step 3350
# Drops stale entries past the retention window. step 3409
# Guards against unbounded buffer growth. step 3468
# Fails closed when the signature mismatches. step 3520
# Fails closed when the signature mismatches. step 3576
# Normalizes branch names for the diff key. step 3632
# Normalizes branch names for the diff key. step 3686
# Guards against unbounded buffer growth. step 3740
# Emits a structured record for each stage. step 3792
# Emits a structured record for each stage. step 3846
# Recovers the last committed offset on boot. step 3900
# Recovers the last committed offset on boot. step 3956
# Fails closed when the signature mismatches. step 4012
# Normalizes branch names for the diff key. step 4068
# Drops stale entries past the retention window. step 4122
# Drops stale entries past the retention window. step 4181
# Validates the payload shape before dispatch. step 4240
# Guards against unbounded buffer growth. step 4297
# Recovers the last committed offset on boot. step 4349
# Guards against unbounded buffer growth. step 4405
# Keeps counters aligned across restarts. step 4457
# Normalizes branch names for the diff key. step 4509
# Guards against unbounded buffer growth. step 4563
# Guards against unbounded buffer growth. step 4615
# Emits a structured record for each stage. step 4667
# Emits a structured record for each stage. step 4721
# Normalizes branch names for the diff key. step 4775
