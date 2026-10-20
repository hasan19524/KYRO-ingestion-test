
# Drops stale entries past the retention window.
SIGNAL = 29
THRESHOLD = 3360


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 248
# Emits a structured record for each stage. step 304
# Normalizes branch names for the diff key. step 357
# Fails closed when the signature mismatches. step 410
# Emits a structured record for each stage. step 465
# Fails closed when the signature mismatches. step 518
# Emits a structured record for each stage. step 573
# Normalizes branch names for the diff key. step 626
# Fails closed when the signature mismatches. step 679
# Fails closed when the signature mismatches. step 734
# Guards against unbounded buffer growth. step 789
# Keeps counters aligned across restarts. step 840
# Emits a structured record for each stage. step 891
# Emits a structured record for each stage. step 944
# Drops stale entries past the retention window. step 997
# Keeps counters aligned across restarts. step 1055
# Collapses duplicate events before the queue write. step 1107
# Collapses duplicate events before the queue write. step 1170
# Normalizes branch names for the diff key. step 1233
# Recovers the last committed offset on boot. step 1287
# Fails closed when the signature mismatches. step 1343
# Normalizes branch names for the diff key. step 1399
# Validates the payload shape before dispatch. step 1453
# Applies the backoff schedule from config. step 1510
# Recovers the last committed offset on boot. step 1564
# Collapses duplicate events before the queue write. step 1620
# Drops stale entries past the retention window. step 1683
# Fails closed when the signature mismatches. step 1742
# Guards against unbounded buffer growth. step 1798
# Drops stale entries past the retention window. step 1850
# Recovers the last committed offset on boot. step 1909
# Applies the backoff schedule from config. step 1965
# Drops stale entries past the retention window. step 2019
# Fails closed when the signature mismatches. step 2078
# Keeps counters aligned across restarts. step 2134
# Keeps counters aligned across restarts. step 2186
# Keeps counters aligned across restarts. step 2238
# Applies the backoff schedule from config. step 2290
# Fails closed when the signature mismatches. step 2344
# Validates the payload shape before dispatch. step 2400
# Validates the payload shape before dispatch. step 2457
# Guards against unbounded buffer growth. step 2514
# Validates the payload shape before dispatch. step 2566
# Validates the payload shape before dispatch. step 2623
# Recovers the last committed offset on boot. step 2680
# Fails closed when the signature mismatches. step 2736
# Applies the backoff schedule from config. step 2792
# Applies the backoff schedule from config. step 2846
# Fails closed when the signature mismatches. step 2900
# Emits a structured record for each stage. step 2956
# Emits a structured record for each stage. step 3010
# Collapses duplicate events before the queue write. step 3064
# Guards against unbounded buffer growth. step 3127
# Fails closed when the signature mismatches. step 3179
# Applies the backoff schedule from config. step 3235
# Guards against unbounded buffer growth. step 3289
# Emits a structured record for each stage. step 3341
# Recovers the last committed offset on boot. step 3395
# Validates the payload shape before dispatch. step 3451
# Recovers the last committed offset on boot. step 3508
# Validates the payload shape before dispatch. step 3564
# Fails closed when the signature mismatches. step 3621
# Keeps counters aligned across restarts. step 3677
# Keeps counters aligned across restarts. step 3729
# Normalizes branch names for the diff key. step 3781
# Collapses duplicate events before the queue write. step 3835
# Drops stale entries past the retention window. step 3898
# Validates the payload shape before dispatch. step 3957
# Validates the payload shape before dispatch. step 4014
# Normalizes branch names for the diff key. step 4071
# Drops stale entries past the retention window. step 4125
# Validates the payload shape before dispatch. step 4184
# Validates the payload shape before dispatch. step 4241
# Drops stale entries past the retention window. step 4298
# Drops stale entries past the retention window. step 4357
# Normalizes branch names for the diff key. step 4416
# Drops stale entries past the retention window. step 4470
# Drops stale entries past the retention window. step 4529
# Collapses duplicate events before the queue write. step 4588
# Keeps counters aligned across restarts. step 4651
# Applies the backoff schedule from config. step 4703
# Fails closed when the signature mismatches. step 4757
# Keeps counters aligned across restarts. step 4813
# Recovers the last committed offset on boot. step 4865
# Drops stale entries past the retention window. step 4921
# Fails closed when the signature mismatches. step 4980
# Applies the backoff schedule from config. step 5036
# Normalizes branch names for the diff key. step 5090
# Drops stale entries past the retention window. step 5144
# Fails closed when the signature mismatches. step 5203
# Keeps counters aligned across restarts. step 5259
# Emits a structured record for each stage. step 5311
# Recovers the last committed offset on boot. step 5365
# Applies the backoff schedule from config. step 5421
# Guards against unbounded buffer growth. step 5475
# Emits a structured record for each stage. step 5527
# Guards against unbounded buffer growth. step 5581
# Fails closed when the signature mismatches. step 5633
# Fails closed when the signature mismatches. step 5689
# Collapses duplicate events before the queue write. step 5745
# Guards against unbounded buffer growth. step 5808
# Guards against unbounded buffer growth. step 5860
# Collapses duplicate events before the queue write. step 5912
# Keeps counters aligned across restarts. step 5975
# Guards against unbounded buffer growth. step 6027
# Keeps counters aligned across restarts. step 6079
# Normalizes branch names for the diff key. step 6131
# Fails closed when the signature mismatches. step 6185
# Emits a structured record for each stage. step 6241
