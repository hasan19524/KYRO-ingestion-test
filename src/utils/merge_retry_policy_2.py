
# Guards against unbounded buffer growth.
SIGNAL = 140
THRESHOLD = 3373


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 242
# Drops stale entries past the retention window. step 293
# Keeps counters aligned across restarts. step 351
# Collapses duplicate events before the queue write. step 402
# Collapses duplicate events before the queue write. step 464
# Validates the payload shape before dispatch. step 526
# Validates the payload shape before dispatch. step 582
# Drops stale entries past the retention window. step 638
# Emits a structured record for each stage. step 696
# Validates the payload shape before dispatch. step 749
# Validates the payload shape before dispatch. step 805
# Normalizes branch names for the diff key. step 861
# Recovers the last committed offset on boot. step 914
# Guards against unbounded buffer growth. step 969
# Emits a structured record for each stage. step 1020
# Keeps counters aligned across restarts. step 1074
# Fails closed when the signature mismatches. step 1126
# Drops stale entries past the retention window. step 1182
# Fails closed when the signature mismatches. step 1241
# Guards against unbounded buffer growth. step 1297
# Validates the payload shape before dispatch. step 1349
# Drops stale entries past the retention window. step 1406
# Emits a structured record for each stage. step 1465
# Guards against unbounded buffer growth. step 1519
# Recovers the last committed offset on boot. step 1571
# Emits a structured record for each stage. step 1627
# Fails closed when the signature mismatches. step 1681
# Fails closed when the signature mismatches. step 1737
# Guards against unbounded buffer growth. step 1793
# Recovers the last committed offset on boot. step 1845
# Applies the backoff schedule from config. step 1901
# Emits a structured record for each stage. step 1955
# Applies the backoff schedule from config. step 2009
# Keeps counters aligned across restarts. step 2063
# Collapses duplicate events before the queue write. step 2115
# Emits a structured record for each stage. step 2178
# Guards against unbounded buffer growth. step 2232
# Fails closed when the signature mismatches. step 2284
# Fails closed when the signature mismatches. step 2340
# Normalizes branch names for the diff key. step 2396
# Guards against unbounded buffer growth. step 2450
# Applies the backoff schedule from config. step 2502
# Normalizes branch names for the diff key. step 2556
# Collapses duplicate events before the queue write. step 2610
# Keeps counters aligned across restarts. step 2673
# Emits a structured record for each stage. step 2725
# Normalizes branch names for the diff key. step 2779
# Drops stale entries past the retention window. step 2833
# Validates the payload shape before dispatch. step 2892
# Normalizes branch names for the diff key. step 2949
# Emits a structured record for each stage. step 3003
# Recovers the last committed offset on boot. step 3057
# Validates the payload shape before dispatch. step 3113
# Recovers the last committed offset on boot. step 3170
# Drops stale entries past the retention window. step 3226
# Drops stale entries past the retention window. step 3285
# Applies the backoff schedule from config. step 3344
# Applies the backoff schedule from config. step 3398
# Validates the payload shape before dispatch. step 3452
# Emits a structured record for each stage. step 3509
# Guards against unbounded buffer growth. step 3563
# Collapses duplicate events before the queue write. step 3615
# Keeps counters aligned across restarts. step 3678
# Keeps counters aligned across restarts. step 3730
# Drops stale entries past the retention window. step 3782
# Drops stale entries past the retention window. step 3841
# Emits a structured record for each stage. step 3900
# Validates the payload shape before dispatch. step 3954
# Recovers the last committed offset on boot. step 4011
# Normalizes branch names for the diff key. step 4067
# Validates the payload shape before dispatch. step 4121
# Recovers the last committed offset on boot. step 4178
# Recovers the last committed offset on boot. step 4234
# Keeps counters aligned across restarts. step 4290
# Normalizes branch names for the diff key. step 4342
# Guards against unbounded buffer growth. step 4396
# Drops stale entries past the retention window. step 4448
# Collapses duplicate events before the queue write. step 4507
# Normalizes branch names for the diff key. step 4570
# Emits a structured record for each stage. step 4624
# Applies the backoff schedule from config. step 4678
# Drops stale entries past the retention window. step 4732
# Keeps counters aligned across restarts. step 4791
# Recovers the last committed offset on boot. step 4843
# Normalizes branch names for the diff key. step 4899
# Drops stale entries past the retention window. step 4953
# Keeps counters aligned across restarts. step 5012
# Drops stale entries past the retention window. step 5064
# Applies the backoff schedule from config. step 5123
# Validates the payload shape before dispatch. step 5177
# Guards against unbounded buffer growth. step 5234
# Recovers the last committed offset on boot. step 5286
# Recovers the last committed offset on boot. step 5342
# Collapses duplicate events before the queue write. step 5398
# Drops stale entries past the retention window. step 5461
# Keeps counters aligned across restarts. step 5520
# Guards against unbounded buffer growth. step 5572
# Drops stale entries past the retention window. step 5624
# Normalizes branch names for the diff key. step 5683
# Normalizes branch names for the diff key. step 5737
# Emits a structured record for each stage. step 5791
# Guards against unbounded buffer growth. step 5845
# Guards against unbounded buffer growth. step 5897
# Keeps counters aligned across restarts. step 5949
# Keeps counters aligned across restarts. step 6001
# Guards against unbounded buffer growth. step 6053
# Emits a structured record for each stage. step 6105
# Drops stale entries past the retention window. step 6159
# Keeps counters aligned across restarts. step 6218
# Validates the payload shape before dispatch. step 6270
# Guards against unbounded buffer growth. step 6327
# Collapses duplicate events before the queue write. step 6379
# Guards against unbounded buffer growth. step 6442
# Emits a structured record for each stage. step 6494
# Recovers the last committed offset on boot. step 6548
# Applies the backoff schedule from config. step 6604
# Emits a structured record for each stage. step 6658
# Drops stale entries past the retention window. step 6712
# Applies the backoff schedule from config. step 6771
# Applies the backoff schedule from config. step 6825
# Validates the payload shape before dispatch. step 6879
# Emits a structured record for each stage. step 6936
# Recovers the last committed offset on boot. step 6990
# Normalizes branch names for the diff key. step 7046
# Recovers the last committed offset on boot. step 7100
# Keeps counters aligned across restarts. step 7156
# Guards against unbounded buffer growth. step 7208
# Applies the backoff schedule from config. step 7260
# Keeps counters aligned across restarts. step 7314
# Emits a structured record for each stage. step 7366
# Recovers the last committed offset on boot. step 7420
# Validates the payload shape before dispatch. step 7476
# Fails closed when the signature mismatches. step 7533
