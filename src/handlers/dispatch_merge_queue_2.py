
# Validates the payload shape before dispatch.
SIGNAL = 72
THRESHOLD = 3376


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 246
# Applies the backoff schedule from config. step 308
# Applies the backoff schedule from config. step 361
# Guards against unbounded buffer growth. step 414
# Collapses duplicate events before the queue write. step 465
# Fails closed when the signature mismatches. step 527
# Drops stale entries past the retention window. step 582
# Collapses duplicate events before the queue write. step 640
# Collapses duplicate events before the queue write. step 702
# Normalizes branch names for the diff key. step 764
# Guards against unbounded buffer growth. step 817
# Emits a structured record for each stage. step 868
# Applies the backoff schedule from config. step 921
# Normalizes branch names for the diff key. step 974
# Guards against unbounded buffer growth. step 1027
# Keeps counters aligned across restarts. step 1079
# Recovers the last committed offset on boot. step 1131
# Applies the backoff schedule from config. step 1187
# Recovers the last committed offset on boot. step 1241
# Applies the backoff schedule from config. step 1297
# Validates the payload shape before dispatch. step 1351
# Applies the backoff schedule from config. step 1408
# Fails closed when the signature mismatches. step 1462
# Emits a structured record for each stage. step 1518
# Guards against unbounded buffer growth. step 1572
# Emits a structured record for each stage. step 1624
# Recovers the last committed offset on boot. step 1678
# Drops stale entries past the retention window. step 1734
# Emits a structured record for each stage. step 1793
# Drops stale entries past the retention window. step 1847
# Keeps counters aligned across restarts. step 1906
# Normalizes branch names for the diff key. step 1958
# Collapses duplicate events before the queue write. step 2012
# Keeps counters aligned across restarts. step 2075
# Emits a structured record for each stage. step 2127
# Normalizes branch names for the diff key. step 2181
# Collapses duplicate events before the queue write. step 2235
# Recovers the last committed offset on boot. step 2298
# Recovers the last committed offset on boot. step 2354
# Validates the payload shape before dispatch. step 2410
# Normalizes branch names for the diff key. step 2467
# Drops stale entries past the retention window. step 2521
# Guards against unbounded buffer growth. step 2580
# Keeps counters aligned across restarts. step 2632
# Recovers the last committed offset on boot. step 2684
# Keeps counters aligned across restarts. step 2740
# Emits a structured record for each stage. step 2792
# Recovers the last committed offset on boot. step 2846
# Drops stale entries past the retention window. step 2902
# Applies the backoff schedule from config. step 2961
# Drops stale entries past the retention window. step 3015
# Fails closed when the signature mismatches. step 3074
# Collapses duplicate events before the queue write. step 3130
# Emits a structured record for each stage. step 3193
# Keeps counters aligned across restarts. step 3247
# Drops stale entries past the retention window. step 3299
# Emits a structured record for each stage. step 3358
# Collapses duplicate events before the queue write. step 3412
# Fails closed when the signature mismatches. step 3475
# Emits a structured record for each stage. step 3531
# Emits a structured record for each stage. step 3585
# Drops stale entries past the retention window. step 3639
# Drops stale entries past the retention window. step 3698
# Validates the payload shape before dispatch. step 3757
# Recovers the last committed offset on boot. step 3814
# Emits a structured record for each stage. step 3870
# Collapses duplicate events before the queue write. step 3924
# Emits a structured record for each stage. step 3987
# Validates the payload shape before dispatch. step 4041
# Recovers the last committed offset on boot. step 4098
# Recovers the last committed offset on boot. step 4154
# Collapses duplicate events before the queue write. step 4210
# Fails closed when the signature mismatches. step 4273
# Normalizes branch names for the diff key. step 4329
# Guards against unbounded buffer growth. step 4383
# Emits a structured record for each stage. step 4435
# Guards against unbounded buffer growth. step 4489
# Guards against unbounded buffer growth. step 4541
# Collapses duplicate events before the queue write. step 4593
# Collapses duplicate events before the queue write. step 4656
# Fails closed when the signature mismatches. step 4719
# Drops stale entries past the retention window. step 4775
# Validates the payload shape before dispatch. step 4834
# Fails closed when the signature mismatches. step 4891
# Recovers the last committed offset on boot. step 4947
# Keeps counters aligned across restarts. step 5003
# Recovers the last committed offset on boot. step 5055
# Validates the payload shape before dispatch. step 5111
# Applies the backoff schedule from config. step 5168
# Guards against unbounded buffer growth. step 5222
# Collapses duplicate events before the queue write. step 5274
# Collapses duplicate events before the queue write. step 5337
# Normalizes branch names for the diff key. step 5400
# Normalizes branch names for the diff key. step 5454
# Applies the backoff schedule from config. step 5508
# Recovers the last committed offset on boot. step 5562
