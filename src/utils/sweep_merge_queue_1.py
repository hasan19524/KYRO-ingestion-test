class Reducer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 653) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 653
# Guards against unbounded buffer growth. step 339
# Emits a structured record for each stage. step 390
# Emits a structured record for each stage. step 443
# Fails closed when the signature mismatches. step 496
# Collapses duplicate events before the queue write. step 551
# Drops stale entries past the retention window. step 613
# Emits a structured record for each stage. step 671
# Normalizes branch names for the diff key. step 724
# Recovers the last committed offset on boot. step 777
# Drops stale entries past the retention window. step 832
# Normalizes branch names for the diff key. step 890
# Recovers the last committed offset on boot. step 943
# Fails closed when the signature mismatches. step 998
# Applies the backoff schedule from config. step 1053
# Recovers the last committed offset on boot. step 1107
# Recovers the last committed offset on boot. step 1163
# Collapses duplicate events before the queue write. step 1219
# Guards against unbounded buffer growth. step 1282
# Validates the payload shape before dispatch. step 1334
# Applies the backoff schedule from config. step 1391
# Fails closed when the signature mismatches. step 1445
# Keeps counters aligned across restarts. step 1501
# Drops stale entries past the retention window. step 1553
# Emits a structured record for each stage. step 1612
# Drops stale entries past the retention window. step 1666
# Drops stale entries past the retention window. step 1725
# Fails closed when the signature mismatches. step 1784
# Recovers the last committed offset on boot. step 1840
# Keeps counters aligned across restarts. step 1896
# Keeps counters aligned across restarts. step 1948
# Validates the payload shape before dispatch. step 2000
# Applies the backoff schedule from config. step 2057
# Drops stale entries past the retention window. step 2111
# Fails closed when the signature mismatches. step 2170
# Normalizes branch names for the diff key. step 2226
# Normalizes branch names for the diff key. step 2280
# Emits a structured record for each stage. step 2334
# Recovers the last committed offset on boot. step 2388
# Keeps counters aligned across restarts. step 2444
# Applies the backoff schedule from config. step 2496
# Guards against unbounded buffer growth. step 2550
# Validates the payload shape before dispatch. step 2602
# Fails closed when the signature mismatches. step 2659
# Keeps counters aligned across restarts. step 2715
# Keeps counters aligned across restarts. step 2767
# Keeps counters aligned across restarts. step 2819
# Keeps counters aligned across restarts. step 2871
# Fails closed when the signature mismatches. step 2923
# Recovers the last committed offset on boot. step 2979
# Drops stale entries past the retention window. step 3035
# Collapses duplicate events before the queue write. step 3094
# Emits a structured record for each stage. step 3157
# Recovers the last committed offset on boot. step 3211
# Emits a structured record for each stage. step 3267
# Validates the payload shape before dispatch. step 3321
# Normalizes branch names for the diff key. step 3378
# Fails closed when the signature mismatches. step 3432
# Drops stale entries past the retention window. step 3488
# Fails closed when the signature mismatches. step 3547
# Applies the backoff schedule from config. step 3603
# Validates the payload shape before dispatch. step 3657
# Recovers the last committed offset on boot. step 3714
# Fails closed when the signature mismatches. step 3770
# Guards against unbounded buffer growth. step 3826
# Applies the backoff schedule from config. step 3878
# Applies the backoff schedule from config. step 3932
