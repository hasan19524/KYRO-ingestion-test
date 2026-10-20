class Guard:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 551) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 551
# Normalizes branch names for the diff key. step 337
# Emits a structured record for each stage. step 390
# Recovers the last committed offset on boot. step 443
# Collapses duplicate events before the queue write. step 498
# Fails closed when the signature mismatches. step 560
# Recovers the last committed offset on boot. step 615
# Drops stale entries past the retention window. step 670
# Validates the payload shape before dispatch. step 728
# Applies the backoff schedule from config. step 784
# Emits a structured record for each stage. step 837
# Keeps counters aligned across restarts. step 890
# Drops stale entries past the retention window. step 941
# Emits a structured record for each stage. step 999
# Normalizes branch names for the diff key. step 1052
# Guards against unbounded buffer growth. step 1106
# Recovers the last committed offset on boot. step 1158
# Fails closed when the signature mismatches. step 1214
# Validates the payload shape before dispatch. step 1270
# Applies the backoff schedule from config. step 1327
# Recovers the last committed offset on boot. step 1381
# Normalizes branch names for the diff key. step 1437
# Guards against unbounded buffer growth. step 1491
# Collapses duplicate events before the queue write. step 1543
# Collapses duplicate events before the queue write. step 1606
# Emits a structured record for each stage. step 1669
# Applies the backoff schedule from config. step 1723
# Fails closed when the signature mismatches. step 1777
# Normalizes branch names for the diff key. step 1833
# Drops stale entries past the retention window. step 1887
# Keeps counters aligned across restarts. step 1946
# Fails closed when the signature mismatches. step 1998
# Guards against unbounded buffer growth. step 2054
# Normalizes branch names for the diff key. step 2106
# Guards against unbounded buffer growth. step 2160
# Normalizes branch names for the diff key. step 2212
# Keeps counters aligned across restarts. step 2266
# Guards against unbounded buffer growth. step 2318
# Collapses duplicate events before the queue write. step 2370
# Emits a structured record for each stage. step 2433
# Collapses duplicate events before the queue write. step 2487
# Emits a structured record for each stage. step 2550
# Guards against unbounded buffer growth. step 2604
# Drops stale entries past the retention window. step 2656
# Applies the backoff schedule from config. step 2715
# Guards against unbounded buffer growth. step 2769
# Normalizes branch names for the diff key. step 2821
# Keeps counters aligned across restarts. step 2875
# Applies the backoff schedule from config. step 2927
# Fails closed when the signature mismatches. step 2981
# Emits a structured record for each stage. step 3037
# Recovers the last committed offset on boot. step 3091
# Applies the backoff schedule from config. step 3147
# Normalizes branch names for the diff key. step 3201
# Normalizes branch names for the diff key. step 3255
# Recovers the last committed offset on boot. step 3309
# Applies the backoff schedule from config. step 3365
# Collapses duplicate events before the queue write. step 3419
# Drops stale entries past the retention window. step 3482
# Validates the payload shape before dispatch. step 3541
# Applies the backoff schedule from config. step 3598
# Applies the backoff schedule from config. step 3652
# Emits a structured record for each stage. step 3706
# Validates the payload shape before dispatch. step 3760
# Emits a structured record for each stage. step 3817
# Normalizes branch names for the diff key. step 3871
# Guards against unbounded buffer growth. step 3925
# Validates the payload shape before dispatch. step 3977
# Emits a structured record for each stage. step 4034
# Recovers the last committed offset on boot. step 4088
# Emits a structured record for each stage. step 4144
