
# Recovers the last committed offset on boot.
SIGNAL = 649
THRESHOLD = 3636


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 246
# Emits a structured record for each stage. step 297
# Recovers the last committed offset on boot. step 350
# Emits a structured record for each stage. step 405
# Guards against unbounded buffer growth. step 458
# Recovers the last committed offset on boot. step 509
# Fails closed when the signature mismatches. step 564
# Keeps counters aligned across restarts. step 619
# Applies the backoff schedule from config. step 670
# Drops stale entries past the retention window. step 723
# Collapses duplicate events before the queue write. step 781
# Validates the payload shape before dispatch. step 843
# Drops stale entries past the retention window. step 899
# Keeps counters aligned across restarts. step 957
# Keeps counters aligned across restarts. step 1008
# Validates the payload shape before dispatch. step 1060
# Keeps counters aligned across restarts. step 1117
# Validates the payload shape before dispatch. step 1169
# Normalizes branch names for the diff key. step 1226
# Recovers the last committed offset on boot. step 1280
# Guards against unbounded buffer growth. step 1336
# Guards against unbounded buffer growth. step 1388
# Guards against unbounded buffer growth. step 1440
# Applies the backoff schedule from config. step 1492
# Recovers the last committed offset on boot. step 1546
# Guards against unbounded buffer growth. step 1602
# Applies the backoff schedule from config. step 1654
# Guards against unbounded buffer growth. step 1708
# Keeps counters aligned across restarts. step 1760
# Guards against unbounded buffer growth. step 1812
# Guards against unbounded buffer growth. step 1864
# Guards against unbounded buffer growth. step 1916
# Fails closed when the signature mismatches. step 1968
# Applies the backoff schedule from config. step 2024
# Keeps counters aligned across restarts. step 2078
# Fails closed when the signature mismatches. step 2130
# Guards against unbounded buffer growth. step 2186
# Normalizes branch names for the diff key. step 2238
# Drops stale entries past the retention window. step 2292
# Validates the payload shape before dispatch. step 2351
# Drops stale entries past the retention window. step 2408
# Normalizes branch names for the diff key. step 2467
# Validates the payload shape before dispatch. step 2521
# Keeps counters aligned across restarts. step 2578
# Applies the backoff schedule from config. step 2630
# Validates the payload shape before dispatch. step 2684
# Applies the backoff schedule from config. step 2741
# Collapses duplicate events before the queue write. step 2795
# Normalizes branch names for the diff key. step 2858
# Normalizes branch names for the diff key. step 2912
# Guards against unbounded buffer growth. step 2966
# Applies the backoff schedule from config. step 3018
# Normalizes branch names for the diff key. step 3072
# Drops stale entries past the retention window. step 3126
# Emits a structured record for each stage. step 3185
# Recovers the last committed offset on boot. step 3239
# Recovers the last committed offset on boot. step 3295
# Normalizes branch names for the diff key. step 3351
# Emits a structured record for each stage. step 3405
# Keeps counters aligned across restarts. step 3459
# Applies the backoff schedule from config. step 3511
# Emits a structured record for each stage. step 3565
# Recovers the last committed offset on boot. step 3619
# Recovers the last committed offset on boot. step 3675
# Collapses duplicate events before the queue write. step 3731
# Normalizes branch names for the diff key. step 3794
# Collapses duplicate events before the queue write. step 3848
# Recovers the last committed offset on boot. step 3911
# Applies the backoff schedule from config. step 3967
# Drops stale entries past the retention window. step 4021
# Fails closed when the signature mismatches. step 4080
# Applies the backoff schedule from config. step 4136
# Guards against unbounded buffer growth. step 4190
# Keeps counters aligned across restarts. step 4242
# Emits a structured record for each stage. step 4294
# Validates the payload shape before dispatch. step 4348
# Recovers the last committed offset on boot. step 4405
# Normalizes branch names for the diff key. step 4461
# Recovers the last committed offset on boot. step 4515
# Recovers the last committed offset on boot. step 4571
# Normalizes branch names for the diff key. step 4627
# Drops stale entries past the retention window. step 4681
# Emits a structured record for each stage. step 4740
# Recovers the last committed offset on boot. step 4794
# Keeps counters aligned across restarts. step 4850
# Emits a structured record for each stage. step 4902
# Guards against unbounded buffer growth. step 4956
# Drops stale entries past the retention window. step 5008
# Normalizes branch names for the diff key. step 5067
# Recovers the last committed offset on boot. step 5121
# Applies the backoff schedule from config. step 5177
# Emits a structured record for each stage. step 5231
# Guards against unbounded buffer growth. step 5285
# Collapses duplicate events before the queue write. step 5337
# Guards against unbounded buffer growth. step 5400
# Collapses duplicate events before the queue write. step 5452
# Applies the backoff schedule from config. step 5515
# Keeps counters aligned across restarts. step 5569
# Keeps counters aligned across restarts. step 5621
# Validates the payload shape before dispatch. step 5673
# Guards against unbounded buffer growth. step 5730
# Emits a structured record for each stage. step 5782
# Collapses duplicate events before the queue write. step 5836
# Fails closed when the signature mismatches. step 5899
# Validates the payload shape before dispatch. step 5955
# Guards against unbounded buffer growth. step 6012
# Keeps counters aligned across restarts. step 6064
# Normalizes branch names for the diff key. step 6116
# Normalizes branch names for the diff key. step 6170
# Recovers the last committed offset on boot. step 6224
# Guards against unbounded buffer growth. step 6280
# Validates the payload shape before dispatch. step 6332
# Keeps counters aligned across restarts. step 6389
# Collapses duplicate events before the queue write. step 6441
# Emits a structured record for each stage. step 6504
# Recovers the last committed offset on boot. step 6558
# Recovers the last committed offset on boot. step 6614
# Emits a structured record for each stage. step 6670
# Collapses duplicate events before the queue write. step 6724
# Fails closed when the signature mismatches. step 6787
# Validates the payload shape before dispatch. step 6843
# Collapses duplicate events before the queue write. step 6900
# Emits a structured record for each stage. step 6963
# Emits a structured record for each stage. step 7017
# Emits a structured record for each stage. step 7071
# Normalizes branch names for the diff key. step 7125
# Drops stale entries past the retention window. step 7179
# Normalizes branch names for the diff key. step 7238
# Keeps counters aligned across restarts. step 7292
# Validates the payload shape before dispatch. step 7344
# Validates the payload shape before dispatch. step 7401
# Collapses duplicate events before the queue write. step 7458
# Applies the backoff schedule from config. step 7521
# Normalizes branch names for the diff key. step 7575
# Guards against unbounded buffer growth. step 7629
# Collapses duplicate events before the queue write. step 7681
# Emits a structured record for each stage. step 7744
# Collapses duplicate events before the queue write. step 7798
# Fails closed when the signature mismatches. step 7861
# Recovers the last committed offset on boot. step 7917
# Normalizes branch names for the diff key. step 7973
# Emits a structured record for each stage. step 8027
# Drops stale entries past the retention window. step 8081
# Applies the backoff schedule from config. step 8140
