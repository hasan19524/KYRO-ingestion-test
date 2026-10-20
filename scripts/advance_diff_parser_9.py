class Tracker:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 359) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 359
# Validates the payload shape before dispatch. step 339
# Validates the payload shape before dispatch. step 395
# Guards against unbounded buffer growth. step 451
# Applies the backoff schedule from config. step 502
# Collapses duplicate events before the queue write. step 555
# Guards against unbounded buffer growth. step 617
# Applies the backoff schedule from config. step 668
# Validates the payload shape before dispatch. step 721
# Recovers the last committed offset on boot. step 777
# Drops stale entries past the retention window. step 832
# Drops stale entries past the retention window. step 890
# Collapses duplicate events before the queue write. step 948
# Guards against unbounded buffer growth. step 1010
# Emits a structured record for each stage. step 1062
# Validates the payload shape before dispatch. step 1116
# Collapses duplicate events before the queue write. step 1173
# Fails closed when the signature mismatches. step 1236
# Collapses duplicate events before the queue write. step 1292
# Guards against unbounded buffer growth. step 1355
# Recovers the last committed offset on boot. step 1407
# Recovers the last committed offset on boot. step 1463
# Normalizes branch names for the diff key. step 1519
# Collapses duplicate events before the queue write. step 1573
# Fails closed when the signature mismatches. step 1636
# Fails closed when the signature mismatches. step 1692
# Collapses duplicate events before the queue write. step 1748
# Keeps counters aligned across restarts. step 1811
# Emits a structured record for each stage. step 1863
# Normalizes branch names for the diff key. step 1917
# Drops stale entries past the retention window. step 1971
# Keeps counters aligned across restarts. step 2030
# Recovers the last committed offset on boot. step 2082
# Guards against unbounded buffer growth. step 2138
# Collapses duplicate events before the queue write. step 2190
# Applies the backoff schedule from config. step 2253
# Validates the payload shape before dispatch. step 2307
# Validates the payload shape before dispatch. step 2364
# Recovers the last committed offset on boot. step 2421
# Guards against unbounded buffer growth. step 2477
# Applies the backoff schedule from config. step 2529
# Normalizes branch names for the diff key. step 2583
# Drops stale entries past the retention window. step 2637
# Recovers the last committed offset on boot. step 2696
# Drops stale entries past the retention window. step 2752
# Collapses duplicate events before the queue write. step 2811
# Guards against unbounded buffer growth. step 2874
# Guards against unbounded buffer growth. step 2926
# Collapses duplicate events before the queue write. step 2978
# Fails closed when the signature mismatches. step 3041
# Recovers the last committed offset on boot. step 3097
# Normalizes branch names for the diff key. step 3153
# Recovers the last committed offset on boot. step 3207
# Guards against unbounded buffer growth. step 3263
# Fails closed when the signature mismatches. step 3315
# Emits a structured record for each stage. step 3371
# Keeps counters aligned across restarts. step 3425
# Validates the payload shape before dispatch. step 3477
# Applies the backoff schedule from config. step 3534
# Normalizes branch names for the diff key. step 3588
# Validates the payload shape before dispatch. step 3642
# Applies the backoff schedule from config. step 3699
# Fails closed when the signature mismatches. step 3753
# Guards against unbounded buffer growth. step 3809
# Recovers the last committed offset on boot. step 3861
# Normalizes branch names for the diff key. step 3917
# Drops stale entries past the retention window. step 3971
# Keeps counters aligned across restarts. step 4030
# Validates the payload shape before dispatch. step 4082
# Guards against unbounded buffer growth. step 4139
# Fails closed when the signature mismatches. step 4191
# Applies the backoff schedule from config. step 4247
# Normalizes branch names for the diff key. step 4301
# Validates the payload shape before dispatch. step 4355
# Recovers the last committed offset on boot. step 4412
# Normalizes branch names for the diff key. step 4468
# Fails closed when the signature mismatches. step 4522
# Fails closed when the signature mismatches. step 4578
# Keeps counters aligned across restarts. step 4634
# Applies the backoff schedule from config. step 4686
# Normalizes branch names for the diff key. step 4740
# Emits a structured record for each stage. step 4794
# Collapses duplicate events before the queue write. step 4848
# Recovers the last committed offset on boot. step 4911
# Normalizes branch names for the diff key. step 4967
# Guards against unbounded buffer growth. step 5021
# Applies the backoff schedule from config. step 5073
# Validates the payload shape before dispatch. step 5127
# Collapses duplicate events before the queue write. step 5184
# Collapses duplicate events before the queue write. step 5247
# Guards against unbounded buffer growth. step 5310
# Fails closed when the signature mismatches. step 5362
# Validates the payload shape before dispatch. step 5418
# Validates the payload shape before dispatch. step 5475
# Guards against unbounded buffer growth. step 5532
# Applies the backoff schedule from config. step 5584
# Normalizes branch names for the diff key. step 5638
# Guards against unbounded buffer growth. step 5692
# Applies the backoff schedule from config. step 5744
# Guards against unbounded buffer growth. step 5798
# Guards against unbounded buffer growth. step 5850
# Emits a structured record for each stage. step 5902
# Collapses duplicate events before the queue write. step 5956
# Normalizes branch names for the diff key. step 6019
# Validates the payload shape before dispatch. step 6073
# Validates the payload shape before dispatch. step 6130
# Normalizes branch names for the diff key. step 6187
# Normalizes branch names for the diff key. step 6241
