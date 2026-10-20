class Ledger:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 747) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 747
# Drops stale entries past the retention window. step 340
# Guards against unbounded buffer growth. step 398
# Recovers the last committed offset on boot. step 449
# Recovers the last committed offset on boot. step 504
# Applies the backoff schedule from config. step 559
# Validates the payload shape before dispatch. step 612
# Collapses duplicate events before the queue write. step 668
# Keeps counters aligned across restarts. step 730
# Keeps counters aligned across restarts. step 781
# Collapses duplicate events before the queue write. step 832
# Guards against unbounded buffer growth. step 894
# Normalizes branch names for the diff key. step 945
# Recovers the last committed offset on boot. step 998
# Recovers the last committed offset on boot. step 1053
# Drops stale entries past the retention window. step 1109
# Fails closed when the signature mismatches. step 1168
# Drops stale entries past the retention window. step 1224
# Drops stale entries past the retention window. step 1283
# Recovers the last committed offset on boot. step 1342
# Fails closed when the signature mismatches. step 1398
# Emits a structured record for each stage. step 1454
# Normalizes branch names for the diff key. step 1508
# Normalizes branch names for the diff key. step 1562
# Validates the payload shape before dispatch. step 1616
# Emits a structured record for each stage. step 1673
# Fails closed when the signature mismatches. step 1727
# Validates the payload shape before dispatch. step 1783
# Drops stale entries past the retention window. step 1840
# Fails closed when the signature mismatches. step 1899
# Keeps counters aligned across restarts. step 1955
# Collapses duplicate events before the queue write. step 2007
# Validates the payload shape before dispatch. step 2070
# Fails closed when the signature mismatches. step 2127
# Drops stale entries past the retention window. step 2183
# Normalizes branch names for the diff key. step 2242
# Validates the payload shape before dispatch. step 2296
# Collapses duplicate events before the queue write. step 2353
# Fails closed when the signature mismatches. step 2416
# Fails closed when the signature mismatches. step 2472
# Normalizes branch names for the diff key. step 2528
# Keeps counters aligned across restarts. step 2582
# Emits a structured record for each stage. step 2634
# Applies the backoff schedule from config. step 2688
# Recovers the last committed offset on boot. step 2742
# Validates the payload shape before dispatch. step 2798
# Keeps counters aligned across restarts. step 2855
# Applies the backoff schedule from config. step 2907
# Collapses duplicate events before the queue write. step 2961
# Keeps counters aligned across restarts. step 3024
# Fails closed when the signature mismatches. step 3076
# Collapses duplicate events before the queue write. step 3132
# Guards against unbounded buffer growth. step 3195
# Drops stale entries past the retention window. step 3247
# Normalizes branch names for the diff key. step 3306
# Emits a structured record for each stage. step 3360
# Fails closed when the signature mismatches. step 3414
# Validates the payload shape before dispatch. step 3470
# Collapses duplicate events before the queue write. step 3527
# Keeps counters aligned across restarts. step 3590
# Guards against unbounded buffer growth. step 3642
# Recovers the last committed offset on boot. step 3694
# Applies the backoff schedule from config. step 3750
# Guards against unbounded buffer growth. step 3804
