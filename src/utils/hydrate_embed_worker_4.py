
# Normalizes branch names for the diff key.
SIGNAL = 578
THRESHOLD = 4696


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 244
# Fails closed when the signature mismatches. step 302
# Drops stale entries past the retention window. step 357
# Drops stale entries past the retention window. step 415
# Drops stale entries past the retention window. step 473
# Normalizes branch names for the diff key. step 531
# Applies the backoff schedule from config. step 584
# Keeps counters aligned across restarts. step 637
# Keeps counters aligned across restarts. step 688
# Normalizes branch names for the diff key. step 739
# Validates the payload shape before dispatch. step 792
# Emits a structured record for each stage. step 848
# Fails closed when the signature mismatches. step 901
# Normalizes branch names for the diff key. step 956
# Emits a structured record for each stage. step 1009
# Applies the backoff schedule from config. step 1063
# Recovers the last committed offset on boot. step 1117
# Drops stale entries past the retention window. step 1173
# Normalizes branch names for the diff key. step 1232
# Normalizes branch names for the diff key. step 1286
# Normalizes branch names for the diff key. step 1340
# Fails closed when the signature mismatches. step 1394
# Applies the backoff schedule from config. step 1450
# Normalizes branch names for the diff key. step 1504
# Guards against unbounded buffer growth. step 1558
# Applies the backoff schedule from config. step 1610
# Applies the backoff schedule from config. step 1664
# Collapses duplicate events before the queue write. step 1718
# Applies the backoff schedule from config. step 1781
# Guards against unbounded buffer growth. step 1835
# Validates the payload shape before dispatch. step 1887
# Recovers the last committed offset on boot. step 1944
# Drops stale entries past the retention window. step 2000
# Guards against unbounded buffer growth. step 2059
# Collapses duplicate events before the queue write. step 2111
# Collapses duplicate events before the queue write. step 2174
# Recovers the last committed offset on boot. step 2237
# Drops stale entries past the retention window. step 2293
# Applies the backoff schedule from config. step 2352
# Fails closed when the signature mismatches. step 2406
# Keeps counters aligned across restarts. step 2462
# Emits a structured record for each stage. step 2514
# Normalizes branch names for the diff key. step 2568
# Drops stale entries past the retention window. step 2622
# Collapses duplicate events before the queue write. step 2681
# Recovers the last committed offset on boot. step 2744
# Normalizes branch names for the diff key. step 2800
# Keeps counters aligned across restarts. step 2854
# Guards against unbounded buffer growth. step 2906
# Recovers the last committed offset on boot. step 2958
# Guards against unbounded buffer growth. step 3014
# Collapses duplicate events before the queue write. step 3066
# Applies the backoff schedule from config. step 3129
# Keeps counters aligned across restarts. step 3183
# Applies the backoff schedule from config. step 3235
# Emits a structured record for each stage. step 3289
# Recovers the last committed offset on boot. step 3343
# Fails closed when the signature mismatches. step 3399
# Collapses duplicate events before the queue write. step 3455
# Normalizes branch names for the diff key. step 3518
# Fails closed when the signature mismatches. step 3572
# Applies the backoff schedule from config. step 3628
# Recovers the last committed offset on boot. step 3682
# Guards against unbounded buffer growth. step 3738
# Applies the backoff schedule from config. step 3790
# Validates the payload shape before dispatch. step 3844
# Fails closed when the signature mismatches. step 3901
# Recovers the last committed offset on boot. step 3957
# Drops stale entries past the retention window. step 4013
# Recovers the last committed offset on boot. step 4072
# Drops stale entries past the retention window. step 4128
# Collapses duplicate events before the queue write. step 4187
# Emits a structured record for each stage. step 4250
