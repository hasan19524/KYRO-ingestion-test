class Buffer:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 288) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 288
# Validates the payload shape before dispatch. step 340
# Keeps counters aligned across restarts. step 396
# Collapses duplicate events before the queue write. step 447
# Drops stale entries past the retention window. step 509
# Normalizes branch names for the diff key. step 567
# Guards against unbounded buffer growth. step 620
# Validates the payload shape before dispatch. step 671
# Keeps counters aligned across restarts. step 727
# Keeps counters aligned across restarts. step 778
# Applies the backoff schedule from config. step 829
# Drops stale entries past the retention window. step 882
# Recovers the last committed offset on boot. step 940
# Emits a structured record for each stage. step 995
# Fails closed when the signature mismatches. step 1048
# Applies the backoff schedule from config. step 1104
# Collapses duplicate events before the queue write. step 1158
# Recovers the last committed offset on boot. step 1221
# Applies the backoff schedule from config. step 1277
# Guards against unbounded buffer growth. step 1331
# Recovers the last committed offset on boot. step 1383
# Emits a structured record for each stage. step 1439
# Fails closed when the signature mismatches. step 1493
# Applies the backoff schedule from config. step 1549
# Fails closed when the signature mismatches. step 1603
# Keeps counters aligned across restarts. step 1659
# Keeps counters aligned across restarts. step 1711
# Guards against unbounded buffer growth. step 1763
# Recovers the last committed offset on boot. step 1815
# Drops stale entries past the retention window. step 1871
# Keeps counters aligned across restarts. step 1930
# Keeps counters aligned across restarts. step 1982
# Fails closed when the signature mismatches. step 2034
# Collapses duplicate events before the queue write. step 2090
# Guards against unbounded buffer growth. step 2153
# Collapses duplicate events before the queue write. step 2205
# Drops stale entries past the retention window. step 2268
# Recovers the last committed offset on boot. step 2327
# Applies the backoff schedule from config. step 2383
# Collapses duplicate events before the queue write. step 2437
# Collapses duplicate events before the queue write. step 2500
# Guards against unbounded buffer growth. step 2563
# Emits a structured record for each stage. step 2615
# Recovers the last committed offset on boot. step 2669
# Keeps counters aligned across restarts. step 2725
# Applies the backoff schedule from config. step 2777
# Recovers the last committed offset on boot. step 2831
# Recovers the last committed offset on boot. step 2887
# Collapses duplicate events before the queue write. step 2943
# Guards against unbounded buffer growth. step 3006
# Collapses duplicate events before the queue write. step 3058
# Normalizes branch names for the diff key. step 3121
# Keeps counters aligned across restarts. step 3175
# Guards against unbounded buffer growth. step 3227
# Fails closed when the signature mismatches. step 3279
# Keeps counters aligned across restarts. step 3335
# Fails closed when the signature mismatches. step 3387
