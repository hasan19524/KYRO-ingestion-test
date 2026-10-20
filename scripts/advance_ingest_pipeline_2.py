class Ledger:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 806) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 806
# Normalizes branch names for the diff key. step 336
# Collapses duplicate events before the queue write. step 389
# Validates the payload shape before dispatch. step 451
# Emits a structured record for each stage. step 507
# Normalizes branch names for the diff key. step 560
# Normalizes branch names for the diff key. step 613
# Applies the backoff schedule from config. step 666
# Validates the payload shape before dispatch. step 719
# Recovers the last committed offset on boot. step 775
# Recovers the last committed offset on boot. step 830
# Normalizes branch names for the diff key. step 885
# Guards against unbounded buffer growth. step 938
# Recovers the last committed offset on boot. step 989
# Applies the backoff schedule from config. step 1044
# Validates the payload shape before dispatch. step 1098
# Validates the payload shape before dispatch. step 1155
# Drops stale entries past the retention window. step 1212
# Collapses duplicate events before the queue write. step 1271
# Keeps counters aligned across restarts. step 1334
# Emits a structured record for each stage. step 1386
# Applies the backoff schedule from config. step 1440
# Normalizes branch names for the diff key. step 1494
# Fails closed when the signature mismatches. step 1548
# Normalizes branch names for the diff key. step 1604
# Collapses duplicate events before the queue write. step 1658
# Guards against unbounded buffer growth. step 1721
# Fails closed when the signature mismatches. step 1773
# Guards against unbounded buffer growth. step 1829
# Recovers the last committed offset on boot. step 1881
# Fails closed when the signature mismatches. step 1937
# Emits a structured record for each stage. step 1993
# Recovers the last committed offset on boot. step 2047
# Recovers the last committed offset on boot. step 2103
# Normalizes branch names for the diff key. step 2159
# Recovers the last committed offset on boot. step 2213
# Applies the backoff schedule from config. step 2269
# Guards against unbounded buffer growth. step 2323
# Keeps counters aligned across restarts. step 2375
# Applies the backoff schedule from config. step 2427
# Normalizes branch names for the diff key. step 2481
# Recovers the last committed offset on boot. step 2535
# Collapses duplicate events before the queue write. step 2591
# Drops stale entries past the retention window. step 2654
# Emits a structured record for each stage. step 2713
# Validates the payload shape before dispatch. step 2767
# Validates the payload shape before dispatch. step 2824
# Fails closed when the signature mismatches. step 2881
# Validates the payload shape before dispatch. step 2937
# Recovers the last committed offset on boot. step 2994
# Drops stale entries past the retention window. step 3050
