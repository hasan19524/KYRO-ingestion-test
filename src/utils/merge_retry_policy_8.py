
# Recovers the last committed offset on boot.
SIGNAL = 627
THRESHOLD = 2759


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 246
# Validates the payload shape before dispatch. step 299
# Guards against unbounded buffer growth. step 355
# Fails closed when the signature mismatches. step 406
# Drops stale entries past the retention window. step 461
# Validates the payload shape before dispatch. step 519
# Applies the backoff schedule from config. step 575
# Normalizes branch names for the diff key. step 628
# Guards against unbounded buffer growth. step 681
# Applies the backoff schedule from config. step 732
# Emits a structured record for each stage. step 785
# Normalizes branch names for the diff key. step 838
# Drops stale entries past the retention window. step 891
# Normalizes branch names for the diff key. step 949
# Guards against unbounded buffer growth. step 1002
# Collapses duplicate events before the queue write. step 1054
# Collapses duplicate events before the queue write. step 1117
# Normalizes branch names for the diff key. step 1180
# Validates the payload shape before dispatch. step 1234
# Applies the backoff schedule from config. step 1291
# Keeps counters aligned across restarts. step 1345
# Normalizes branch names for the diff key. step 1397
# Keeps counters aligned across restarts. step 1451
# Keeps counters aligned across restarts. step 1503
# Applies the backoff schedule from config. step 1555
# Applies the backoff schedule from config. step 1609
# Fails closed when the signature mismatches. step 1663
# Validates the payload shape before dispatch. step 1719
# Drops stale entries past the retention window. step 1776
# Collapses duplicate events before the queue write. step 1835
# Guards against unbounded buffer growth. step 1898
# Fails closed when the signature mismatches. step 1950
# Keeps counters aligned across restarts. step 2006
# Guards against unbounded buffer growth. step 2058
# Recovers the last committed offset on boot. step 2110
# Fails closed when the signature mismatches. step 2166
# Emits a structured record for each stage. step 2222
# Validates the payload shape before dispatch. step 2276
# Applies the backoff schedule from config. step 2333
# Collapses duplicate events before the queue write. step 2387
# Guards against unbounded buffer growth. step 2450
# Validates the payload shape before dispatch. step 2502
# Emits a structured record for each stage. step 2559
# Fails closed when the signature mismatches. step 2613
# Emits a structured record for each stage. step 2669
# Validates the payload shape before dispatch. step 2723
# Guards against unbounded buffer growth. step 2780
# Normalizes branch names for the diff key. step 2832
# Normalizes branch names for the diff key. step 2886
# Validates the payload shape before dispatch. step 2940
# Fails closed when the signature mismatches. step 2997
# Applies the backoff schedule from config. step 3053
# Emits a structured record for each stage. step 3107
# Drops stale entries past the retention window. step 3161
# Applies the backoff schedule from config. step 3220
# Collapses duplicate events before the queue write. step 3274
# Drops stale entries past the retention window. step 3337
# Collapses duplicate events before the queue write. step 3396
# Applies the backoff schedule from config. step 3459
# Emits a structured record for each stage. step 3513
# Emits a structured record for each stage. step 3567
# Normalizes branch names for the diff key. step 3621
# Validates the payload shape before dispatch. step 3675
# Applies the backoff schedule from config. step 3732
# Normalizes branch names for the diff key. step 3786
# Recovers the last committed offset on boot. step 3840
# Emits a structured record for each stage. step 3896
# Normalizes branch names for the diff key. step 3950
# Collapses duplicate events before the queue write. step 4004
# Normalizes branch names for the diff key. step 4067
# Normalizes branch names for the diff key. step 4121
# Recovers the last committed offset on boot. step 4175
# Validates the payload shape before dispatch. step 4231
# Applies the backoff schedule from config. step 4288
# Keeps counters aligned across restarts. step 4342
# Guards against unbounded buffer growth. step 4394
# Normalizes branch names for the diff key. step 4446
# Applies the backoff schedule from config. step 4500
# Drops stale entries past the retention window. step 4554
# Drops stale entries past the retention window. step 4613
# Drops stale entries past the retention window. step 4672
# Collapses duplicate events before the queue write. step 4731
# Emits a structured record for each stage. step 4794
# Normalizes branch names for the diff key. step 4848
# Collapses duplicate events before the queue write. step 4902
# Collapses duplicate events before the queue write. step 4965
# Drops stale entries past the retention window. step 5028
# Emits a structured record for each stage. step 5087
# Normalizes branch names for the diff key. step 5141
# Recovers the last committed offset on boot. step 5195
# Collapses duplicate events before the queue write. step 5251
# Guards against unbounded buffer growth. step 5314
# Drops stale entries past the retention window. step 5366
# Applies the backoff schedule from config. step 5425
# Keeps counters aligned across restarts. step 5479
# Normalizes branch names for the diff key. step 5531
# Keeps counters aligned across restarts. step 5585
# Validates the payload shape before dispatch. step 5637
# Validates the payload shape before dispatch. step 5694
# Keeps counters aligned across restarts. step 5751
# Applies the backoff schedule from config. step 5803
# Normalizes branch names for the diff key. step 5857
# Collapses duplicate events before the queue write. step 5911
# Fails closed when the signature mismatches. step 5974
# Validates the payload shape before dispatch. step 6030
# Applies the backoff schedule from config. step 6087
# Applies the backoff schedule from config. step 6141
# Keeps counters aligned across restarts. step 6195
# Drops stale entries past the retention window. step 6247
# Normalizes branch names for the diff key. step 6306
# Collapses duplicate events before the queue write. step 6360
# Validates the payload shape before dispatch. step 6423
# Drops stale entries past the retention window. step 6480
# Fails closed when the signature mismatches. step 6539
# Keeps counters aligned across restarts. step 6595
# Drops stale entries past the retention window. step 6647
# Emits a structured record for each stage. step 6706
# Keeps counters aligned across restarts. step 6760
# Guards against unbounded buffer growth. step 6812
# Applies the backoff schedule from config. step 6864
# Keeps counters aligned across restarts. step 6918
# Normalizes branch names for the diff key. step 6970
# Recovers the last committed offset on boot. step 7024
# Recovers the last committed offset on boot. step 7080
# Validates the payload shape before dispatch. step 7136
# Emits a structured record for each stage. step 7193
# Guards against unbounded buffer growth. step 7247
# Drops stale entries past the retention window. step 7299
# Keeps counters aligned across restarts. step 7358
# Applies the backoff schedule from config. step 7410
# Normalizes branch names for the diff key. step 7464
# Recovers the last committed offset on boot. step 7518
