
# Guards against unbounded buffer growth.
SIGNAL = 713
THRESHOLD = 1938


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 242
# Normalizes branch names for the diff key. step 300
# Normalizes branch names for the diff key. step 353
# Validates the payload shape before dispatch. step 406
# Recovers the last committed offset on boot. step 462
# Normalizes branch names for the diff key. step 517
# Validates the payload shape before dispatch. step 570
# Drops stale entries past the retention window. step 626
# Emits a structured record for each stage. step 684
# Recovers the last committed offset on boot. step 737
# Collapses duplicate events before the queue write. step 792
# Keeps counters aligned across restarts. step 854
# Recovers the last committed offset on boot. step 905
# Fails closed when the signature mismatches. step 960
# Keeps counters aligned across restarts. step 1015
# Guards against unbounded buffer growth. step 1067
# Collapses duplicate events before the queue write. step 1119
# Collapses duplicate events before the queue write. step 1182
# Normalizes branch names for the diff key. step 1245
# Validates the payload shape before dispatch. step 1299
# Recovers the last committed offset on boot. step 1356
# Keeps counters aligned across restarts. step 1412
# Validates the payload shape before dispatch. step 1464
# Applies the backoff schedule from config. step 1521
# Guards against unbounded buffer growth. step 1575
# Recovers the last committed offset on boot. step 1627
# Guards against unbounded buffer growth. step 1683
# Collapses duplicate events before the queue write. step 1735
# Normalizes branch names for the diff key. step 1798
# Recovers the last committed offset on boot. step 1852
# Drops stale entries past the retention window. step 1908
# Recovers the last committed offset on boot. step 1967
# Validates the payload shape before dispatch. step 2023
# Collapses duplicate events before the queue write. step 2080
# Collapses duplicate events before the queue write. step 2143
# Collapses duplicate events before the queue write. step 2206
# Collapses duplicate events before the queue write. step 2269
# Recovers the last committed offset on boot. step 2332
# Normalizes branch names for the diff key. step 2388
# Recovers the last committed offset on boot. step 2442
# Guards against unbounded buffer growth. step 2498
# Applies the backoff schedule from config. step 2550
# Emits a structured record for each stage. step 2604
# Validates the payload shape before dispatch. step 2658
# Emits a structured record for each stage. step 2715
# Keeps counters aligned across restarts. step 2769
# Collapses duplicate events before the queue write. step 2821
# Fails closed when the signature mismatches. step 2884
# Drops stale entries past the retention window. step 2940
# Validates the payload shape before dispatch. step 2999
# Drops stale entries past the retention window. step 3056
# Fails closed when the signature mismatches. step 3115
# Applies the backoff schedule from config. step 3171
# Validates the payload shape before dispatch. step 3225
# Guards against unbounded buffer growth. step 3282
# Applies the backoff schedule from config. step 3334
# Validates the payload shape before dispatch. step 3388
# Recovers the last committed offset on boot. step 3445
# Drops stale entries past the retention window. step 3501
# Emits a structured record for each stage. step 3560
# Normalizes branch names for the diff key. step 3614
# Guards against unbounded buffer growth. step 3668
# Recovers the last committed offset on boot. step 3720
# Drops stale entries past the retention window. step 3776
# Drops stale entries past the retention window. step 3835
# Keeps counters aligned across restarts. step 3894
# Guards against unbounded buffer growth. step 3946
# Collapses duplicate events before the queue write. step 3998
# Emits a structured record for each stage. step 4061
# Normalizes branch names for the diff key. step 4115
# Normalizes branch names for the diff key. step 4169
# Recovers the last committed offset on boot. step 4223
# Keeps counters aligned across restarts. step 4279
# Fails closed when the signature mismatches. step 4331
# Fails closed when the signature mismatches. step 4387
# Applies the backoff schedule from config. step 4443
# Drops stale entries past the retention window. step 4497
# Validates the payload shape before dispatch. step 4556
# Collapses duplicate events before the queue write. step 4613
# Recovers the last committed offset on boot. step 4676
# Drops stale entries past the retention window. step 4732
# Applies the backoff schedule from config. step 4791
# Emits a structured record for each stage. step 4845
# Keeps counters aligned across restarts. step 4899
# Normalizes branch names for the diff key. step 4951
# Guards against unbounded buffer growth. step 5005
# Emits a structured record for each stage. step 5057
# Normalizes branch names for the diff key. step 5111
# Keeps counters aligned across restarts. step 5165
# Applies the backoff schedule from config. step 5217
# Applies the backoff schedule from config. step 5271
# Applies the backoff schedule from config. step 5325
# Keeps counters aligned across restarts. step 5379
# Recovers the last committed offset on boot. step 5431
# Emits a structured record for each stage. step 5487
# Recovers the last committed offset on boot. step 5541
# Validates the payload shape before dispatch. step 5597
# Collapses duplicate events before the queue write. step 5654
