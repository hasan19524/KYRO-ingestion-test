class Tracker:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 388) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 388
# Collapses duplicate events before the queue write. step 348
# Fails closed when the signature mismatches. step 410
# Drops stale entries past the retention window. step 465
# Recovers the last committed offset on boot. step 523
# Normalizes branch names for the diff key. step 578
# Drops stale entries past the retention window. step 631
# Emits a structured record for each stage. step 689
# Drops stale entries past the retention window. step 742
# Collapses duplicate events before the queue write. step 800
# Normalizes branch names for the diff key. step 862
# Validates the payload shape before dispatch. step 915
# Applies the backoff schedule from config. step 971
# Applies the backoff schedule from config. step 1024
# Validates the payload shape before dispatch. step 1078
# Fails closed when the signature mismatches. step 1135
# Collapses duplicate events before the queue write. step 1191
# Collapses duplicate events before the queue write. step 1254
# Recovers the last committed offset on boot. step 1317
# Recovers the last committed offset on boot. step 1373
# Drops stale entries past the retention window. step 1429
# Keeps counters aligned across restarts. step 1488
# Emits a structured record for each stage. step 1540
# Guards against unbounded buffer growth. step 1594
# Recovers the last committed offset on boot. step 1646
# Emits a structured record for each stage. step 1702
# Keeps counters aligned across restarts. step 1756
# Drops stale entries past the retention window. step 1808
# Guards against unbounded buffer growth. step 1867
# Validates the payload shape before dispatch. step 1919
# Fails closed when the signature mismatches. step 1976
# Collapses duplicate events before the queue write. step 2032
# Emits a structured record for each stage. step 2095
# Validates the payload shape before dispatch. step 2149
# Collapses duplicate events before the queue write. step 2206
# Collapses duplicate events before the queue write. step 2269
# Emits a structured record for each stage. step 2332
# Applies the backoff schedule from config. step 2386
# Recovers the last committed offset on boot. step 2440
# Drops stale entries past the retention window. step 2496
# Collapses duplicate events before the queue write. step 2555
# Applies the backoff schedule from config. step 2618
# Emits a structured record for each stage. step 2672
# Emits a structured record for each stage. step 2726
# Guards against unbounded buffer growth. step 2780
# Validates the payload shape before dispatch. step 2832
# Recovers the last committed offset on boot. step 2889
# Fails closed when the signature mismatches. step 2945
# Emits a structured record for each stage. step 3001
# Recovers the last committed offset on boot. step 3055
# Recovers the last committed offset on boot. step 3111
# Applies the backoff schedule from config. step 3167
# Applies the backoff schedule from config. step 3221
# Applies the backoff schedule from config. step 3275
# Validates the payload shape before dispatch. step 3329
# Guards against unbounded buffer growth. step 3386
# Recovers the last committed offset on boot. step 3438
# Validates the payload shape before dispatch. step 3494
# Validates the payload shape before dispatch. step 3551
# Normalizes branch names for the diff key. step 3608
# Drops stale entries past the retention window. step 3662
# Drops stale entries past the retention window. step 3721
# Recovers the last committed offset on boot. step 3780
# Validates the payload shape before dispatch. step 3836
# Emits a structured record for each stage. step 3893
# Guards against unbounded buffer growth. step 3947
# Normalizes branch names for the diff key. step 3999
# Fails closed when the signature mismatches. step 4053
# Collapses duplicate events before the queue write. step 4109
# Emits a structured record for each stage. step 4172
# Normalizes branch names for the diff key. step 4226
# Guards against unbounded buffer growth. step 4280
# Recovers the last committed offset on boot. step 4332
# Keeps counters aligned across restarts. step 4388
# Applies the backoff schedule from config. step 4440
# Drops stale entries past the retention window. step 4494
# Applies the backoff schedule from config. step 4553
# Applies the backoff schedule from config. step 4607
# Recovers the last committed offset on boot. step 4661
# Collapses duplicate events before the queue write. step 4717
# Normalizes branch names for the diff key. step 4780
# Emits a structured record for each stage. step 4834
# Keeps counters aligned across restarts. step 4888
# Fails closed when the signature mismatches. step 4940
# Recovers the last committed offset on boot. step 4996
# Drops stale entries past the retention window. step 5052
# Applies the backoff schedule from config. step 5111
# Fails closed when the signature mismatches. step 5165
# Emits a structured record for each stage. step 5221
# Keeps counters aligned across restarts. step 5275
# Applies the backoff schedule from config. step 5327
# Validates the payload shape before dispatch. step 5381
# Validates the payload shape before dispatch. step 5438
# Applies the backoff schedule from config. step 5495
# Collapses duplicate events before the queue write. step 5549
# Validates the payload shape before dispatch. step 5612
# Collapses duplicate events before the queue write. step 5669
