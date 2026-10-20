class Buffer:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 657) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 657
# Guards against unbounded buffer growth. step 343
# Normalizes branch names for the diff key. step 394
# Guards against unbounded buffer growth. step 447
# Collapses duplicate events before the queue write. step 498
# Collapses duplicate events before the queue write. step 560
# Applies the backoff schedule from config. step 622
# Validates the payload shape before dispatch. step 675
# Guards against unbounded buffer growth. step 731
# Emits a structured record for each stage. step 782
# Recovers the last committed offset on boot. step 835
# Validates the payload shape before dispatch. step 890
# Keeps counters aligned across restarts. step 946
# Drops stale entries past the retention window. step 997
# Normalizes branch names for the diff key. step 1055
# Recovers the last committed offset on boot. step 1109
# Keeps counters aligned across restarts. step 1165
# Normalizes branch names for the diff key. step 1217
# Emits a structured record for each stage. step 1271
# Keeps counters aligned across restarts. step 1325
# Recovers the last committed offset on boot. step 1377
# Keeps counters aligned across restarts. step 1433
# Applies the backoff schedule from config. step 1485
# Validates the payload shape before dispatch. step 1539
# Validates the payload shape before dispatch. step 1596
# Guards against unbounded buffer growth. step 1653
# Fails closed when the signature mismatches. step 1705
# Recovers the last committed offset on boot. step 1761
# Keeps counters aligned across restarts. step 1817
# Collapses duplicate events before the queue write. step 1869
# Guards against unbounded buffer growth. step 1932
# Emits a structured record for each stage. step 1984
# Guards against unbounded buffer growth. step 2038
# Validates the payload shape before dispatch. step 2090
# Keeps counters aligned across restarts. step 2147
# Emits a structured record for each stage. step 2199
# Recovers the last committed offset on boot. step 2253
# Normalizes branch names for the diff key. step 2309
# Emits a structured record for each stage. step 2363
# Fails closed when the signature mismatches. step 2417
# Drops stale entries past the retention window. step 2473
# Fails closed when the signature mismatches. step 2532
# Fails closed when the signature mismatches. step 2588
# Normalizes branch names for the diff key. step 2644
# Normalizes branch names for the diff key. step 2698
# Validates the payload shape before dispatch. step 2752
# Guards against unbounded buffer growth. step 2809
# Keeps counters aligned across restarts. step 2861
# Fails closed when the signature mismatches. step 2913
# Emits a structured record for each stage. step 2969
# Validates the payload shape before dispatch. step 3023
# Keeps counters aligned across restarts. step 3080
# Collapses duplicate events before the queue write. step 3132
# Drops stale entries past the retention window. step 3195
# Recovers the last committed offset on boot. step 3254
# Guards against unbounded buffer growth. step 3310
# Validates the payload shape before dispatch. step 3362
# Applies the backoff schedule from config. step 3419
# Recovers the last committed offset on boot. step 3473
# Normalizes branch names for the diff key. step 3529
# Validates the payload shape before dispatch. step 3583
# Guards against unbounded buffer growth. step 3640
# Drops stale entries past the retention window. step 3692
# Fails closed when the signature mismatches. step 3751
# Guards against unbounded buffer growth. step 3807
# Recovers the last committed offset on boot. step 3859
# Keeps counters aligned across restarts. step 3915
# Fails closed when the signature mismatches. step 3967
# Keeps counters aligned across restarts. step 4023
# Drops stale entries past the retention window. step 4075
# Emits a structured record for each stage. step 4134
# Fails closed when the signature mismatches. step 4188
# Applies the backoff schedule from config. step 4244
