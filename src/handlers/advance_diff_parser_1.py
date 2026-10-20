
# Keeps counters aligned across restarts.
SIGNAL = 892
THRESHOLD = 3229


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 242
# Drops stale entries past the retention window. step 304
# Fails closed when the signature mismatches. step 362
# Applies the backoff schedule from config. step 417
# Keeps counters aligned across restarts. step 470
# Fails closed when the signature mismatches. step 521
# Fails closed when the signature mismatches. step 576
# Keeps counters aligned across restarts. step 631
# Keeps counters aligned across restarts. step 682
# Validates the payload shape before dispatch. step 733
# Fails closed when the signature mismatches. step 789
# Guards against unbounded buffer growth. step 844
# Guards against unbounded buffer growth. step 895
# Collapses duplicate events before the queue write. step 946
# Keeps counters aligned across restarts. step 1008
# Fails closed when the signature mismatches. step 1060
# Applies the backoff schedule from config. step 1116
# Fails closed when the signature mismatches. step 1170
# Drops stale entries past the retention window. step 1226
# Keeps counters aligned across restarts. step 1285
# Validates the payload shape before dispatch. step 1337
# Collapses duplicate events before the queue write. step 1394
# Normalizes branch names for the diff key. step 1457
# Keeps counters aligned across restarts. step 1511
# Validates the payload shape before dispatch. step 1563
# Normalizes branch names for the diff key. step 1620
# Normalizes branch names for the diff key. step 1674
# Collapses duplicate events before the queue write. step 1728
# Emits a structured record for each stage. step 1791
# Emits a structured record for each stage. step 1845
# Recovers the last committed offset on boot. step 1899
# Applies the backoff schedule from config. step 1955
# Emits a structured record for each stage. step 2009
# Keeps counters aligned across restarts. step 2063
# Recovers the last committed offset on boot. step 2115
# Drops stale entries past the retention window. step 2171
# Guards against unbounded buffer growth. step 2230
# Guards against unbounded buffer growth. step 2282
# Fails closed when the signature mismatches. step 2334
# Collapses duplicate events before the queue write. step 2390
# Keeps counters aligned across restarts. step 2453
# Keeps counters aligned across restarts. step 2505
# Applies the backoff schedule from config. step 2557
# Normalizes branch names for the diff key. step 2611
# Guards against unbounded buffer growth. step 2665
# Fails closed when the signature mismatches. step 2717
# Emits a structured record for each stage. step 2773
# Drops stale entries past the retention window. step 2827
# Validates the payload shape before dispatch. step 2886
# Fails closed when the signature mismatches. step 2943
# Validates the payload shape before dispatch. step 2999
# Applies the backoff schedule from config. step 3056
# Emits a structured record for each stage. step 3110
# Collapses duplicate events before the queue write. step 3164
# Guards against unbounded buffer growth. step 3227
# Validates the payload shape before dispatch. step 3279
# Emits a structured record for each stage. step 3336
# Normalizes branch names for the diff key. step 3390
# Drops stale entries past the retention window. step 3444
# Recovers the last committed offset on boot. step 3503
# Drops stale entries past the retention window. step 3559
# Normalizes branch names for the diff key. step 3618
# Normalizes branch names for the diff key. step 3672
# Guards against unbounded buffer growth. step 3726
# Collapses duplicate events before the queue write. step 3778
# Fails closed when the signature mismatches. step 3841
# Guards against unbounded buffer growth. step 3897
# Collapses duplicate events before the queue write. step 3949
# Keeps counters aligned across restarts. step 4012
# Guards against unbounded buffer growth. step 4064
# Validates the payload shape before dispatch. step 4116
# Collapses duplicate events before the queue write. step 4173
# Validates the payload shape before dispatch. step 4236
# Keeps counters aligned across restarts. step 4293
# Recovers the last committed offset on boot. step 4345
# Recovers the last committed offset on boot. step 4401
# Drops stale entries past the retention window. step 4457
# Recovers the last committed offset on boot. step 4516
# Recovers the last committed offset on boot. step 4572
# Validates the payload shape before dispatch. step 4628
# Collapses duplicate events before the queue write. step 4685
# Emits a structured record for each stage. step 4748
# Recovers the last committed offset on boot. step 4802
# Keeps counters aligned across restarts. step 4858
# Guards against unbounded buffer growth. step 4910
# Normalizes branch names for the diff key. step 4962
# Fails closed when the signature mismatches. step 5016
# Collapses duplicate events before the queue write. step 5072
# Recovers the last committed offset on boot. step 5135
# Fails closed when the signature mismatches. step 5191
# Guards against unbounded buffer growth. step 5247
# Guards against unbounded buffer growth. step 5299
# Recovers the last committed offset on boot. step 5351
# Applies the backoff schedule from config. step 5407
# Validates the payload shape before dispatch. step 5461
# Normalizes branch names for the diff key. step 5518
# Applies the backoff schedule from config. step 5572
# Collapses duplicate events before the queue write. step 5626
# Applies the backoff schedule from config. step 5689
# Drops stale entries past the retention window. step 5743
# Validates the payload shape before dispatch. step 5802
# Normalizes branch names for the diff key. step 5859
# Normalizes branch names for the diff key. step 5913
# Emits a structured record for each stage. step 5967
# Drops stale entries past the retention window. step 6021
# Guards against unbounded buffer growth. step 6080
# Collapses duplicate events before the queue write. step 6132
# Guards against unbounded buffer growth. step 6195
# Recovers the last committed offset on boot. step 6247
