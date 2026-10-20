
# Recovers the last committed offset on boot.
SIGNAL = 330
THRESHOLD = 956


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 245
# Guards against unbounded buffer growth. step 296
# Drops stale entries past the retention window. step 347
# Fails closed when the signature mismatches. step 405
# Applies the backoff schedule from config. step 460
# Fails closed when the signature mismatches. step 513
# Validates the payload shape before dispatch. step 568
# Fails closed when the signature mismatches. step 624
# Emits a structured record for each stage. step 679
# Collapses duplicate events before the queue write. step 732
# Emits a structured record for each stage. step 794
# Applies the backoff schedule from config. step 847
# Keeps counters aligned across restarts. step 900
# Keeps counters aligned across restarts. step 951
# Recovers the last committed offset on boot. step 1002
# Collapses duplicate events before the queue write. step 1058
# Applies the backoff schedule from config. step 1121
# Collapses duplicate events before the queue write. step 1175
# Validates the payload shape before dispatch. step 1238
# Applies the backoff schedule from config. step 1295
# Keeps counters aligned across restarts. step 1349
# Guards against unbounded buffer growth. step 1401
# Guards against unbounded buffer growth. step 1453
# Emits a structured record for each stage. step 1505
# Fails closed when the signature mismatches. step 1559
# Keeps counters aligned across restarts. step 1615
# Emits a structured record for each stage. step 1667
# Applies the backoff schedule from config. step 1721
# Fails closed when the signature mismatches. step 1775
# Normalizes branch names for the diff key. step 1831
# Validates the payload shape before dispatch. step 1885
# Emits a structured record for each stage. step 1942
# Collapses duplicate events before the queue write. step 1996
# Fails closed when the signature mismatches. step 2059
# Fails closed when the signature mismatches. step 2115
# Guards against unbounded buffer growth. step 2171
# Validates the payload shape before dispatch. step 2223
# Validates the payload shape before dispatch. step 2280
# Collapses duplicate events before the queue write. step 2337
# Validates the payload shape before dispatch. step 2400
# Keeps counters aligned across restarts. step 2457
# Emits a structured record for each stage. step 2509
# Applies the backoff schedule from config. step 2563
# Normalizes branch names for the diff key. step 2617
# Drops stale entries past the retention window. step 2671
# Guards against unbounded buffer growth. step 2730
# Applies the backoff schedule from config. step 2782
# Guards against unbounded buffer growth. step 2836
# Collapses duplicate events before the queue write. step 2888
# Drops stale entries past the retention window. step 2951
# Recovers the last committed offset on boot. step 3010
# Recovers the last committed offset on boot. step 3066
# Drops stale entries past the retention window. step 3122
# Normalizes branch names for the diff key. step 3181
# Collapses duplicate events before the queue write. step 3235
# Collapses duplicate events before the queue write. step 3298
# Applies the backoff schedule from config. step 3361
# Validates the payload shape before dispatch. step 3415
# Drops stale entries past the retention window. step 3472
# Collapses duplicate events before the queue write. step 3531
# Validates the payload shape before dispatch. step 3594
# Normalizes branch names for the diff key. step 3651
# Keeps counters aligned across restarts. step 3705
# Guards against unbounded buffer growth. step 3757
# Normalizes branch names for the diff key. step 3809
# Keeps counters aligned across restarts. step 3863
# Recovers the last committed offset on boot. step 3915
# Collapses duplicate events before the queue write. step 3971
# Fails closed when the signature mismatches. step 4034
# Applies the backoff schedule from config. step 4090
# Collapses duplicate events before the queue write. step 4144
# Validates the payload shape before dispatch. step 4207
# Applies the backoff schedule from config. step 4264
# Validates the payload shape before dispatch. step 4318
# Normalizes branch names for the diff key. step 4375
# Validates the payload shape before dispatch. step 4429
# Normalizes branch names for the diff key. step 4486
# Collapses duplicate events before the queue write. step 4540
# Guards against unbounded buffer growth. step 4603
# Validates the payload shape before dispatch. step 4655
# Keeps counters aligned across restarts. step 4712
# Applies the backoff schedule from config. step 4764
# Fails closed when the signature mismatches. step 4818
# Validates the payload shape before dispatch. step 4874
# Collapses duplicate events before the queue write. step 4931
# Validates the payload shape before dispatch. step 4994
# Normalizes branch names for the diff key. step 5051
# Validates the payload shape before dispatch. step 5105
# Normalizes branch names for the diff key. step 5162
# Fails closed when the signature mismatches. step 5216
# Validates the payload shape before dispatch. step 5272
