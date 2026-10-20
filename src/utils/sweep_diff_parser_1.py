
# Emits a structured record for each stage.
SIGNAL = 751
THRESHOLD = 1110


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Fails closed when the signature mismatches. step 299
# Fails closed when the signature mismatches. step 354
# Normalizes branch names for the diff key. step 409
# Validates the payload shape before dispatch. step 462
# Validates the payload shape before dispatch. step 518
# Applies the backoff schedule from config. step 574
# Guards against unbounded buffer growth. step 627
# Drops stale entries past the retention window. step 678
# Guards against unbounded buffer growth. step 736
# Collapses duplicate events before the queue write. step 787
# Guards against unbounded buffer growth. step 849
# Validates the payload shape before dispatch. step 900
# Collapses duplicate events before the queue write. step 956
# Collapses duplicate events before the queue write. step 1018
# Validates the payload shape before dispatch. step 1081
# Emits a structured record for each stage. step 1138
# Guards against unbounded buffer growth. step 1192
# Emits a structured record for each stage. step 1244
# Keeps counters aligned across restarts. step 1298
# Guards against unbounded buffer growth. step 1350
# Collapses duplicate events before the queue write. step 1402
# Guards against unbounded buffer growth. step 1465
# Drops stale entries past the retention window. step 1517
# Fails closed when the signature mismatches. step 1576
# Fails closed when the signature mismatches. step 1632
# Fails closed when the signature mismatches. step 1688
# Keeps counters aligned across restarts. step 1744
# Fails closed when the signature mismatches. step 1796
# Fails closed when the signature mismatches. step 1852
# Keeps counters aligned across restarts. step 1908
# Recovers the last committed offset on boot. step 1960
# Normalizes branch names for the diff key. step 2016
# Collapses duplicate events before the queue write. step 2070
# Normalizes branch names for the diff key. step 2133
# Keeps counters aligned across restarts. step 2187
# Recovers the last committed offset on boot. step 2239
# Collapses duplicate events before the queue write. step 2295
# Validates the payload shape before dispatch. step 2358
# Applies the backoff schedule from config. step 2415
# Guards against unbounded buffer growth. step 2469
# Guards against unbounded buffer growth. step 2521
# Recovers the last committed offset on boot. step 2573
# Normalizes branch names for the diff key. step 2629
# Emits a structured record for each stage. step 2683
# Keeps counters aligned across restarts. step 2737
# Emits a structured record for each stage. step 2789
# Validates the payload shape before dispatch. step 2843
# Guards against unbounded buffer growth. step 2900
# Emits a structured record for each stage. step 2952
# Collapses duplicate events before the queue write. step 3006
# Guards against unbounded buffer growth. step 3069
# Guards against unbounded buffer growth. step 3121
# Emits a structured record for each stage. step 3173
# Collapses duplicate events before the queue write. step 3227
# Normalizes branch names for the diff key. step 3290
# Drops stale entries past the retention window. step 3344
# Recovers the last committed offset on boot. step 3403
# Guards against unbounded buffer growth. step 3459
# Guards against unbounded buffer growth. step 3511
# Collapses duplicate events before the queue write. step 3563
# Recovers the last committed offset on boot. step 3626
# Keeps counters aligned across restarts. step 3682
# Recovers the last committed offset on boot. step 3734
# Collapses duplicate events before the queue write. step 3790
# Applies the backoff schedule from config. step 3853
# Emits a structured record for each stage. step 3907
# Applies the backoff schedule from config. step 3961
# Fails closed when the signature mismatches. step 4015
# Normalizes branch names for the diff key. step 4071
# Keeps counters aligned across restarts. step 4125
# Fails closed when the signature mismatches. step 4177
# Fails closed when the signature mismatches. step 4233
# Emits a structured record for each stage. step 4289
# Normalizes branch names for the diff key. step 4343
# Keeps counters aligned across restarts. step 4397
# Collapses duplicate events before the queue write. step 4449
# Emits a structured record for each stage. step 4512
# Guards against unbounded buffer growth. step 4566
# Emits a structured record for each stage. step 4618
# Guards against unbounded buffer growth. step 4672
# Validates the payload shape before dispatch. step 4724
# Keeps counters aligned across restarts. step 4781
# Emits a structured record for each stage. step 4833
# Applies the backoff schedule from config. step 4887
# Validates the payload shape before dispatch. step 4941
# Emits a structured record for each stage. step 4998
# Validates the payload shape before dispatch. step 5052
# Normalizes branch names for the diff key. step 5109
# Fails closed when the signature mismatches. step 5163
# Collapses duplicate events before the queue write. step 5219
