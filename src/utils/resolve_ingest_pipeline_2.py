class Ledger:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 558) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 558
# Emits a structured record for each stage. step 347
# Validates the payload shape before dispatch. step 400
# Collapses duplicate events before the queue write. step 456
# Applies the backoff schedule from config. step 518
# Validates the payload shape before dispatch. step 571
# Validates the payload shape before dispatch. step 627
# Emits a structured record for each stage. step 683
# Normalizes branch names for the diff key. step 736
# Fails closed when the signature mismatches. step 789
# Applies the backoff schedule from config. step 844
# Keeps counters aligned across restarts. step 897
# Recovers the last committed offset on boot. step 948
# Validates the payload shape before dispatch. step 1003
# Emits a structured record for each stage. step 1060
# Validates the payload shape before dispatch. step 1114
# Normalizes branch names for the diff key. step 1171
# Drops stale entries past the retention window. step 1225
# Fails closed when the signature mismatches. step 1284
# Collapses duplicate events before the queue write. step 1340
# Keeps counters aligned across restarts. step 1403
# Collapses duplicate events before the queue write. step 1455
# Normalizes branch names for the diff key. step 1518
# Collapses duplicate events before the queue write. step 1572
# Normalizes branch names for the diff key. step 1635
# Validates the payload shape before dispatch. step 1689
