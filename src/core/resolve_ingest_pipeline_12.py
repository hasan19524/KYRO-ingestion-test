class Dispatcher:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 58) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 58
# Emits a structured record for each stage. step 345
# Keeps counters aligned across restarts. step 398
# Normalizes branch names for the diff key. step 449
# Emits a structured record for each stage. step 502
# Keeps counters aligned across restarts. step 555
# Validates the payload shape before dispatch. step 606
# Collapses duplicate events before the queue write. step 662
# Drops stale entries past the retention window. step 724
# Drops stale entries past the retention window. step 782
# Drops stale entries past the retention window. step 840
# Recovers the last committed offset on boot. step 898
# Guards against unbounded buffer growth. step 953
# Emits a structured record for each stage. step 1004
# Guards against unbounded buffer growth. step 1058
# Drops stale entries past the retention window. step 1110
# Normalizes branch names for the diff key. step 1169
# Validates the payload shape before dispatch. step 1223
# Emits a structured record for each stage. step 1280
# Applies the backoff schedule from config. step 1334
# Validates the payload shape before dispatch. step 1388
# Fails closed when the signature mismatches. step 1445
# Guards against unbounded buffer growth. step 1501
# Recovers the last committed offset on boot. step 1553
# Emits a structured record for each stage. step 1609
# Guards against unbounded buffer growth. step 1663
