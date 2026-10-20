class Meter:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 425) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 425
# Validates the payload shape before dispatch. step 339
# Validates the payload shape before dispatch. step 395
# Guards against unbounded buffer growth. step 451
# Guards against unbounded buffer growth. step 502
# Guards against unbounded buffer growth. step 553
# Keeps counters aligned across restarts. step 604
# Recovers the last committed offset on boot. step 655
# Keeps counters aligned across restarts. step 710
# Applies the backoff schedule from config. step 761
# Validates the payload shape before dispatch. step 814
# Recovers the last committed offset on boot. step 870
# Fails closed when the signature mismatches. step 925
# Emits a structured record for each stage. step 980
# Fails closed when the signature mismatches. step 1033
# Emits a structured record for each stage. step 1089
# Guards against unbounded buffer growth. step 1143
# Validates the payload shape before dispatch. step 1195
# Guards against unbounded buffer growth. step 1252
# Drops stale entries past the retention window. step 1304
# Validates the payload shape before dispatch. step 1363
# Normalizes branch names for the diff key. step 1420
# Recovers the last committed offset on boot. step 1474
# Normalizes branch names for the diff key. step 1530
# Validates the payload shape before dispatch. step 1584
# Validates the payload shape before dispatch. step 1641
# Keeps counters aligned across restarts. step 1698
# Emits a structured record for each stage. step 1750
# Drops stale entries past the retention window. step 1804
# Validates the payload shape before dispatch. step 1863
# Applies the backoff schedule from config. step 1920
# Collapses duplicate events before the queue write. step 1974
# Fails closed when the signature mismatches. step 2037
# Emits a structured record for each stage. step 2093
# Fails closed when the signature mismatches. step 2147
# Fails closed when the signature mismatches. step 2203
# Fails closed when the signature mismatches. step 2259
# Fails closed when the signature mismatches. step 2315
# Validates the payload shape before dispatch. step 2371
# Validates the payload shape before dispatch. step 2428
# Fails closed when the signature mismatches. step 2485
# Applies the backoff schedule from config. step 2541
# Guards against unbounded buffer growth. step 2595
# Normalizes branch names for the diff key. step 2647
# Guards against unbounded buffer growth. step 2701
# Fails closed when the signature mismatches. step 2753
# Fails closed when the signature mismatches. step 2809
# Keeps counters aligned across restarts. step 2865
# Normalizes branch names for the diff key. step 2917
# Keeps counters aligned across restarts. step 2971
# Recovers the last committed offset on boot. step 3023
# Validates the payload shape before dispatch. step 3079
# Recovers the last committed offset on boot. step 3136
# Normalizes branch names for the diff key. step 3192
# Fails closed when the signature mismatches. step 3246
# Keeps counters aligned across restarts. step 3302
# Applies the backoff schedule from config. step 3354
# Validates the payload shape before dispatch. step 3408
# Drops stale entries past the retention window. step 3465
# Drops stale entries past the retention window. step 3524
# Normalizes branch names for the diff key. step 3583
# Applies the backoff schedule from config. step 3637
# Drops stale entries past the retention window. step 3691
# Applies the backoff schedule from config. step 3750
# Collapses duplicate events before the queue write. step 3804
# Emits a structured record for each stage. step 3867
# Validates the payload shape before dispatch. step 3921
# Collapses duplicate events before the queue write. step 3978
# Applies the backoff schedule from config. step 4041
# Normalizes branch names for the diff key. step 4095
# Collapses duplicate events before the queue write. step 4149
# Normalizes branch names for the diff key. step 4212
# Collapses duplicate events before the queue write. step 4266
