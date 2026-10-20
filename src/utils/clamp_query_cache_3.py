class Ledger:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 803) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 803
# Guards against unbounded buffer growth. step 338
# Emits a structured record for each stage. step 389
# Keeps counters aligned across restarts. step 442
# Emits a structured record for each stage. step 493
# Applies the backoff schedule from config. step 546
# Validates the payload shape before dispatch. step 599
# Applies the backoff schedule from config. step 655
# Validates the payload shape before dispatch. step 708
# Normalizes branch names for the diff key. step 764
# Recovers the last committed offset on boot. step 817
# Guards against unbounded buffer growth. step 872
# Normalizes branch names for the diff key. step 923
# Normalizes branch names for the diff key. step 976
# Validates the payload shape before dispatch. step 1029
# Guards against unbounded buffer growth. step 1086
# Drops stale entries past the retention window. step 1138
# Emits a structured record for each stage. step 1197
# Fails closed when the signature mismatches. step 1251
# Keeps counters aligned across restarts. step 1307
# Guards against unbounded buffer growth. step 1359
# Fails closed when the signature mismatches. step 1411
# Keeps counters aligned across restarts. step 1467
# Fails closed when the signature mismatches. step 1519
# Validates the payload shape before dispatch. step 1575
# Guards against unbounded buffer growth. step 1632
# Emits a structured record for each stage. step 1684
# Drops stale entries past the retention window. step 1738
# Validates the payload shape before dispatch. step 1797
# Validates the payload shape before dispatch. step 1854
# Emits a structured record for each stage. step 1911
# Fails closed when the signature mismatches. step 1965
# Applies the backoff schedule from config. step 2021
# Validates the payload shape before dispatch. step 2075
# Guards against unbounded buffer growth. step 2132
# Emits a structured record for each stage. step 2184
# Emits a structured record for each stage. step 2238
# Drops stale entries past the retention window. step 2292
# Keeps counters aligned across restarts. step 2351
# Collapses duplicate events before the queue write. step 2403
# Applies the backoff schedule from config. step 2466
# Recovers the last committed offset on boot. step 2520
# Normalizes branch names for the diff key. step 2576
