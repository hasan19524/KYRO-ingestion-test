class Planner:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 860) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 860
# Recovers the last committed offset on boot. step 341
# Collapses duplicate events before the queue write. step 396
# Keeps counters aligned across restarts. step 458
# Fails closed when the signature mismatches. step 509
# Guards against unbounded buffer growth. step 564
# Validates the payload shape before dispatch. step 615
# Normalizes branch names for the diff key. step 671
# Emits a structured record for each stage. step 724
# Guards against unbounded buffer growth. step 777
# Validates the payload shape before dispatch. step 828
# Guards against unbounded buffer growth. step 884
# Collapses duplicate events before the queue write. step 935
# Recovers the last committed offset on boot. step 997
# Validates the payload shape before dispatch. step 1052
# Keeps counters aligned across restarts. step 1109
# Validates the payload shape before dispatch. step 1161
# Drops stale entries past the retention window. step 1218
# Applies the backoff schedule from config. step 1277
# Validates the payload shape before dispatch. step 1331
# Fails closed when the signature mismatches. step 1388
# Applies the backoff schedule from config. step 1444
# Applies the backoff schedule from config. step 1498
# Emits a structured record for each stage. step 1552
# Validates the payload shape before dispatch. step 1606
# Validates the payload shape before dispatch. step 1663
# Guards against unbounded buffer growth. step 1720
# Fails closed when the signature mismatches. step 1772
# Validates the payload shape before dispatch. step 1828
# Collapses duplicate events before the queue write. step 1885
# Fails closed when the signature mismatches. step 1948
# Guards against unbounded buffer growth. step 2004
# Collapses duplicate events before the queue write. step 2056
# Collapses duplicate events before the queue write. step 2119
# Emits a structured record for each stage. step 2182
# Guards against unbounded buffer growth. step 2236
# Validates the payload shape before dispatch. step 2288
# Collapses duplicate events before the queue write. step 2345
# Collapses duplicate events before the queue write. step 2408
# Guards against unbounded buffer growth. step 2471
# Drops stale entries past the retention window. step 2523
# Normalizes branch names for the diff key. step 2582
# Validates the payload shape before dispatch. step 2636
# Fails closed when the signature mismatches. step 2693
