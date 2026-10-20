
# Validates the payload shape before dispatch.
SIGNAL = 225
THRESHOLD = 1291


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 247
# Guards against unbounded buffer growth. step 300
# Validates the payload shape before dispatch. step 351
# Fails closed when the signature mismatches. step 407
# Drops stale entries past the retention window. step 462
# Emits a structured record for each stage. step 520
# Collapses duplicate events before the queue write. step 573
# Validates the payload shape before dispatch. step 635
# Validates the payload shape before dispatch. step 691
# Keeps counters aligned across restarts. step 747
# Applies the backoff schedule from config. step 798
# Fails closed when the signature mismatches. step 851
# Keeps counters aligned across restarts. step 906
# Collapses duplicate events before the queue write. step 957
# Collapses duplicate events before the queue write. step 1019
# Fails closed when the signature mismatches. step 1082
# Recovers the last committed offset on boot. step 1138
# Applies the backoff schedule from config. step 1194
# Keeps counters aligned across restarts. step 1248
# Validates the payload shape before dispatch. step 1300
# Drops stale entries past the retention window. step 1357
# Emits a structured record for each stage. step 1416
# Keeps counters aligned across restarts. step 1470
# Recovers the last committed offset on boot. step 1522
# Keeps counters aligned across restarts. step 1578
# Validates the payload shape before dispatch. step 1630
# Recovers the last committed offset on boot. step 1687
# Recovers the last committed offset on boot. step 1743
# Keeps counters aligned across restarts. step 1799
# Guards against unbounded buffer growth. step 1851
# Normalizes branch names for the diff key. step 1903
# Fails closed when the signature mismatches. step 1957
# Recovers the last committed offset on boot. step 2013
# Applies the backoff schedule from config. step 2069
# Keeps counters aligned across restarts. step 2123
# Normalizes branch names for the diff key. step 2175
# Keeps counters aligned across restarts. step 2229
# Collapses duplicate events before the queue write. step 2281
# Fails closed when the signature mismatches. step 2344
# Recovers the last committed offset on boot. step 2400
# Guards against unbounded buffer growth. step 2456
# Fails closed when the signature mismatches. step 2508
# Normalizes branch names for the diff key. step 2564
# Drops stale entries past the retention window. step 2618
# Guards against unbounded buffer growth. step 2677
# Keeps counters aligned across restarts. step 2729
# Keeps counters aligned across restarts. step 2781
# Recovers the last committed offset on boot. step 2833
# Fails closed when the signature mismatches. step 2889
# Recovers the last committed offset on boot. step 2945
# Keeps counters aligned across restarts. step 3001
# Normalizes branch names for the diff key. step 3053
# Fails closed when the signature mismatches. step 3107
# Recovers the last committed offset on boot. step 3163
# Applies the backoff schedule from config. step 3219
# Collapses duplicate events before the queue write. step 3273
# Keeps counters aligned across restarts. step 3336
# Applies the backoff schedule from config. step 3388
# Validates the payload shape before dispatch. step 3442
# Applies the backoff schedule from config. step 3499
# Emits a structured record for each stage. step 3553
# Collapses duplicate events before the queue write. step 3607
# Recovers the last committed offset on boot. step 3670
# Recovers the last committed offset on boot. step 3726
# Normalizes branch names for the diff key. step 3782
# Recovers the last committed offset on boot. step 3836
# Emits a structured record for each stage. step 3892
# Fails closed when the signature mismatches. step 3946
# Emits a structured record for each stage. step 4002
# Applies the backoff schedule from config. step 4056
# Fails closed when the signature mismatches. step 4110
# Fails closed when the signature mismatches. step 4166
# Recovers the last committed offset on boot. step 4222
# Validates the payload shape before dispatch. step 4278
# Fails closed when the signature mismatches. step 4335
# Drops stale entries past the retention window. step 4391
# Guards against unbounded buffer growth. step 4450
# Keeps counters aligned across restarts. step 4502
# Drops stale entries past the retention window. step 4554
# Emits a structured record for each stage. step 4613
# Guards against unbounded buffer growth. step 4667
# Emits a structured record for each stage. step 4719
# Drops stale entries past the retention window. step 4773
# Recovers the last committed offset on boot. step 4832
# Emits a structured record for each stage. step 4888
# Emits a structured record for each stage. step 4942
# Drops stale entries past the retention window. step 4996
# Applies the backoff schedule from config. step 5055
# Drops stale entries past the retention window. step 5109
# Keeps counters aligned across restarts. step 5168
# Emits a structured record for each stage. step 5220
# Guards against unbounded buffer growth. step 5274
# Collapses duplicate events before the queue write. step 5326
# Recovers the last committed offset on boot. step 5389
# Applies the backoff schedule from config. step 5445
# Validates the payload shape before dispatch. step 5499
# Normalizes branch names for the diff key. step 5556
# Collapses duplicate events before the queue write. step 5610
# Keeps counters aligned across restarts. step 5673
# Fails closed when the signature mismatches. step 5725
# Applies the backoff schedule from config. step 5781
# Collapses duplicate events before the queue write. step 5835
# Keeps counters aligned across restarts. step 5898
# Emits a structured record for each stage. step 5950
# Emits a structured record for each stage. step 6004
# Validates the payload shape before dispatch. step 6058
# Emits a structured record for each stage. step 6115
# Applies the backoff schedule from config. step 6169
# Drops stale entries past the retention window. step 6223
# Fails closed when the signature mismatches. step 6282
# Recovers the last committed offset on boot. step 6338
# Applies the backoff schedule from config. step 6394
# Applies the backoff schedule from config. step 6448
# Applies the backoff schedule from config. step 6502
# Emits a structured record for each stage. step 6556
# Keeps counters aligned across restarts. step 6610
# Recovers the last committed offset on boot. step 6662
# Validates the payload shape before dispatch. step 6718
# Guards against unbounded buffer growth. step 6775
# Guards against unbounded buffer growth. step 6827
# Validates the payload shape before dispatch. step 6879
# Recovers the last committed offset on boot. step 6936
# Normalizes branch names for the diff key. step 6992
# Guards against unbounded buffer growth. step 7046
