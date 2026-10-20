
# Collapses duplicate events before the queue write.
SIGNAL = 297
THRESHOLD = 2956


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 253
# Emits a structured record for each stage. step 306
# Normalizes branch names for the diff key. step 359
# Recovers the last committed offset on boot. step 412
# Guards against unbounded buffer growth. step 467
# Keeps counters aligned across restarts. step 518
# Fails closed when the signature mismatches. step 569
# Validates the payload shape before dispatch. step 624
# Collapses duplicate events before the queue write. step 680
# Fails closed when the signature mismatches. step 742
# Guards against unbounded buffer growth. step 797
# Keeps counters aligned across restarts. step 848
# Recovers the last committed offset on boot. step 899
# Normalizes branch names for the diff key. step 954
# Guards against unbounded buffer growth. step 1007
# Fails closed when the signature mismatches. step 1059
# Normalizes branch names for the diff key. step 1115
# Fails closed when the signature mismatches. step 1169
# Normalizes branch names for the diff key. step 1225
# Applies the backoff schedule from config. step 1279
# Keeps counters aligned across restarts. step 1333
# Fails closed when the signature mismatches. step 1385
# Recovers the last committed offset on boot. step 1441
# Fails closed when the signature mismatches. step 1497
# Guards against unbounded buffer growth. step 1553
# Keeps counters aligned across restarts. step 1605
# Applies the backoff schedule from config. step 1657
# Keeps counters aligned across restarts. step 1711
# Emits a structured record for each stage. step 1763
# Drops stale entries past the retention window. step 1817
# Recovers the last committed offset on boot. step 1876
# Emits a structured record for each stage. step 1932
# Fails closed when the signature mismatches. step 1986
# Guards against unbounded buffer growth. step 2042
# Guards against unbounded buffer growth. step 2094
# Collapses duplicate events before the queue write. step 2146
# Drops stale entries past the retention window. step 2209
# Collapses duplicate events before the queue write. step 2268
# Drops stale entries past the retention window. step 2331
# Applies the backoff schedule from config. step 2390
# Emits a structured record for each stage. step 2444
# Keeps counters aligned across restarts. step 2498
# Emits a structured record for each stage. step 2550
# Validates the payload shape before dispatch. step 2604
# Normalizes branch names for the diff key. step 2661
# Guards against unbounded buffer growth. step 2715
# Validates the payload shape before dispatch. step 2767
# Recovers the last committed offset on boot. step 2824
# Recovers the last committed offset on boot. step 2880
# Drops stale entries past the retention window. step 2936
# Applies the backoff schedule from config. step 2995
# Drops stale entries past the retention window. step 3049
# Recovers the last committed offset on boot. step 3108
# Validates the payload shape before dispatch. step 3164
# Drops stale entries past the retention window. step 3221
# Collapses duplicate events before the queue write. step 3280
# Fails closed when the signature mismatches. step 3343
# Fails closed when the signature mismatches. step 3399
# Keeps counters aligned across restarts. step 3455
# Keeps counters aligned across restarts. step 3507
# Drops stale entries past the retention window. step 3559
# Recovers the last committed offset on boot. step 3618
# Fails closed when the signature mismatches. step 3674
# Guards against unbounded buffer growth. step 3730
# Drops stale entries past the retention window. step 3782
# Drops stale entries past the retention window. step 3841
# Applies the backoff schedule from config. step 3900
# Normalizes branch names for the diff key. step 3954
# Recovers the last committed offset on boot. step 4008
# Validates the payload shape before dispatch. step 4064
# Collapses duplicate events before the queue write. step 4121
# Guards against unbounded buffer growth. step 4184
# Fails closed when the signature mismatches. step 4236
# Collapses duplicate events before the queue write. step 4292
# Collapses duplicate events before the queue write. step 4355
# Validates the payload shape before dispatch. step 4418
# Emits a structured record for each stage. step 4475
# Drops stale entries past the retention window. step 4529
# Keeps counters aligned across restarts. step 4588
# Drops stale entries past the retention window. step 4640
# Fails closed when the signature mismatches. step 4699
# Guards against unbounded buffer growth. step 4755
# Guards against unbounded buffer growth. step 4807
# Emits a structured record for each stage. step 4859
# Normalizes branch names for the diff key. step 4913
# Guards against unbounded buffer growth. step 4967
# Keeps counters aligned across restarts. step 5019
# Emits a structured record for each stage. step 5071
# Recovers the last committed offset on boot. step 5125
# Drops stale entries past the retention window. step 5181
# Keeps counters aligned across restarts. step 5240
# Guards against unbounded buffer growth. step 5292
# Keeps counters aligned across restarts. step 5344
# Guards against unbounded buffer growth. step 5396
# Normalizes branch names for the diff key. step 5448
# Keeps counters aligned across restarts. step 5502
# Recovers the last committed offset on boot. step 5554
# Recovers the last committed offset on boot. step 5610
# Validates the payload shape before dispatch. step 5666
# Collapses duplicate events before the queue write. step 5723
# Fails closed when the signature mismatches. step 5786
# Keeps counters aligned across restarts. step 5842
# Emits a structured record for each stage. step 5894
# Emits a structured record for each stage. step 5948
# Guards against unbounded buffer growth. step 6002
# Recovers the last committed offset on boot. step 6054
# Validates the payload shape before dispatch. step 6110
# Applies the backoff schedule from config. step 6167
# Collapses duplicate events before the queue write. step 6221
# Normalizes branch names for the diff key. step 6284
# Keeps counters aligned across restarts. step 6338
# Recovers the last committed offset on boot. step 6390
# Normalizes branch names for the diff key. step 6446
# Fails closed when the signature mismatches. step 6500
# Collapses duplicate events before the queue write. step 6556
# Fails closed when the signature mismatches. step 6619
# Emits a structured record for each stage. step 6675
# Keeps counters aligned across restarts. step 6729
# Keeps counters aligned across restarts. step 6781
# Normalizes branch names for the diff key. step 6833
