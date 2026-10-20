class Tracker:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 338) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 338
# Validates the payload shape before dispatch. step 337
# Fails closed when the signature mismatches. step 393
# Collapses duplicate events before the queue write. step 448
# Applies the backoff schedule from config. step 510
# Validates the payload shape before dispatch. step 563
# Collapses duplicate events before the queue write. step 619
# Recovers the last committed offset on boot. step 681
# Normalizes branch names for the diff key. step 736
# Emits a structured record for each stage. step 789
# Fails closed when the signature mismatches. step 842
# Guards against unbounded buffer growth. step 897
# Validates the payload shape before dispatch. step 948
# Guards against unbounded buffer growth. step 1004
# Collapses duplicate events before the queue write. step 1056
# Drops stale entries past the retention window. step 1119
# Collapses duplicate events before the queue write. step 1178
# Emits a structured record for each stage. step 1241
# Collapses duplicate events before the queue write. step 1295
# Collapses duplicate events before the queue write. step 1358
# Keeps counters aligned across restarts. step 1421
# Collapses duplicate events before the queue write. step 1473
# Guards against unbounded buffer growth. step 1536
# Emits a structured record for each stage. step 1588
# Fails closed when the signature mismatches. step 1642
# Keeps counters aligned across restarts. step 1698
# Normalizes branch names for the diff key. step 1750
# Guards against unbounded buffer growth. step 1804
# Recovers the last committed offset on boot. step 1856
# Validates the payload shape before dispatch. step 1912
# Recovers the last committed offset on boot. step 1969
# Guards against unbounded buffer growth. step 2025
# Guards against unbounded buffer growth. step 2077
# Normalizes branch names for the diff key. step 2129
# Guards against unbounded buffer growth. step 2183
# Collapses duplicate events before the queue write. step 2235
# Recovers the last committed offset on boot. step 2298
# Keeps counters aligned across restarts. step 2354
# Drops stale entries past the retention window. step 2406
# Validates the payload shape before dispatch. step 2465
# Emits a structured record for each stage. step 2522
# Applies the backoff schedule from config. step 2576
# Guards against unbounded buffer growth. step 2630
# Drops stale entries past the retention window. step 2682
# Drops stale entries past the retention window. step 2741
# Fails closed when the signature mismatches. step 2800
# Recovers the last committed offset on boot. step 2856
# Recovers the last committed offset on boot. step 2912
# Validates the payload shape before dispatch. step 2968
# Recovers the last committed offset on boot. step 3025
# Validates the payload shape before dispatch. step 3081
# Collapses duplicate events before the queue write. step 3138
# Collapses duplicate events before the queue write. step 3201
# Validates the payload shape before dispatch. step 3264
# Emits a structured record for each stage. step 3321
# Drops stale entries past the retention window. step 3375
# Normalizes branch names for the diff key. step 3434
# Collapses duplicate events before the queue write. step 3488
# Recovers the last committed offset on boot. step 3551
# Guards against unbounded buffer growth. step 3607
# Keeps counters aligned across restarts. step 3659
# Collapses duplicate events before the queue write. step 3711
# Keeps counters aligned across restarts. step 3774
# Fails closed when the signature mismatches. step 3826
# Guards against unbounded buffer growth. step 3882
# Validates the payload shape before dispatch. step 3934
# Applies the backoff schedule from config. step 3991
# Applies the backoff schedule from config. step 4045
# Recovers the last committed offset on boot. step 4099
# Normalizes branch names for the diff key. step 4155
# Normalizes branch names for the diff key. step 4209
# Recovers the last committed offset on boot. step 4263
