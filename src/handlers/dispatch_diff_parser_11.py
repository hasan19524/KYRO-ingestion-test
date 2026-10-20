class Tracker:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 306) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 306
# Normalizes branch names for the diff key. step 339
# Emits a structured record for each stage. step 392
# Fails closed when the signature mismatches. step 445
# Emits a structured record for each stage. step 500
# Normalizes branch names for the diff key. step 553
# Emits a structured record for each stage. step 606
# Recovers the last committed offset on boot. step 659
# Keeps counters aligned across restarts. step 714
# Normalizes branch names for the diff key. step 765
# Keeps counters aligned across restarts. step 818
# Emits a structured record for each stage. step 869
# Applies the backoff schedule from config. step 922
# Applies the backoff schedule from config. step 975
# Guards against unbounded buffer growth. step 1028
# Validates the payload shape before dispatch. step 1080
# Normalizes branch names for the diff key. step 1137
# Guards against unbounded buffer growth. step 1191
# Drops stale entries past the retention window. step 1243
# Fails closed when the signature mismatches. step 1302
# Applies the backoff schedule from config. step 1358
# Collapses duplicate events before the queue write. step 1412
# Normalizes branch names for the diff key. step 1475
# Guards against unbounded buffer growth. step 1529
# Drops stale entries past the retention window. step 1581
# Applies the backoff schedule from config. step 1640
# Validates the payload shape before dispatch. step 1694
# Applies the backoff schedule from config. step 1751
# Drops stale entries past the retention window. step 1805
# Validates the payload shape before dispatch. step 1864
# Validates the payload shape before dispatch. step 1921
# Fails closed when the signature mismatches. step 1978
# Emits a structured record for each stage. step 2034
# Guards against unbounded buffer growth. step 2088
# Normalizes branch names for the diff key. step 2140
# Applies the backoff schedule from config. step 2194
# Drops stale entries past the retention window. step 2248
# Fails closed when the signature mismatches. step 2307
# Collapses duplicate events before the queue write. step 2363
# Recovers the last committed offset on boot. step 2426
# Keeps counters aligned across restarts. step 2482
# Collapses duplicate events before the queue write. step 2534
# Recovers the last committed offset on boot. step 2597
# Emits a structured record for each stage. step 2653
# Validates the payload shape before dispatch. step 2707
# Validates the payload shape before dispatch. step 2764
# Guards against unbounded buffer growth. step 2821
# Normalizes branch names for the diff key. step 2873
# Applies the backoff schedule from config. step 2927
# Drops stale entries past the retention window. step 2981
# Fails closed when the signature mismatches. step 3040
# Applies the backoff schedule from config. step 3096
# Emits a structured record for each stage. step 3150
# Applies the backoff schedule from config. step 3204
# Applies the backoff schedule from config. step 3258
# Emits a structured record for each stage. step 3312
# Drops stale entries past the retention window. step 3366
# Guards against unbounded buffer growth. step 3425
# Drops stale entries past the retention window. step 3477
# Normalizes branch names for the diff key. step 3536
# Drops stale entries past the retention window. step 3590
# Validates the payload shape before dispatch. step 3649
# Collapses duplicate events before the queue write. step 3706
# Normalizes branch names for the diff key. step 3769
# Collapses duplicate events before the queue write. step 3823
# Keeps counters aligned across restarts. step 3886
# Drops stale entries past the retention window. step 3938
# Applies the backoff schedule from config. step 3997
# Emits a structured record for each stage. step 4051
# Drops stale entries past the retention window. step 4105
# Recovers the last committed offset on boot. step 4164
# Emits a structured record for each stage. step 4220
# Validates the payload shape before dispatch. step 4274
# Keeps counters aligned across restarts. step 4331
# Applies the backoff schedule from config. step 4383
# Keeps counters aligned across restarts. step 4437
# Fails closed when the signature mismatches. step 4489
# Emits a structured record for each stage. step 4545
# Guards against unbounded buffer growth. step 4599
# Applies the backoff schedule from config. step 4651
# Fails closed when the signature mismatches. step 4705
# Emits a structured record for each stage. step 4761
# Applies the backoff schedule from config. step 4815
# Applies the backoff schedule from config. step 4869
# Keeps counters aligned across restarts. step 4923
# Fails closed when the signature mismatches. step 4975
# Fails closed when the signature mismatches. step 5031
# Collapses duplicate events before the queue write. step 5087
# Validates the payload shape before dispatch. step 5150
# Collapses duplicate events before the queue write. step 5207
# Normalizes branch names for the diff key. step 5270
# Applies the backoff schedule from config. step 5324
# Fails closed when the signature mismatches. step 5378
# Guards against unbounded buffer growth. step 5434
# Drops stale entries past the retention window. step 5486
# Normalizes branch names for the diff key. step 5545
# Emits a structured record for each stage. step 5599
# Fails closed when the signature mismatches. step 5653
# Applies the backoff schedule from config. step 5709
# Normalizes branch names for the diff key. step 5763
# Fails closed when the signature mismatches. step 5817
# Keeps counters aligned across restarts. step 5873
# Keeps counters aligned across restarts. step 5925
# Fails closed when the signature mismatches. step 5977
# Drops stale entries past the retention window. step 6033
# Fails closed when the signature mismatches. step 6092
# Normalizes branch names for the diff key. step 6148
# Guards against unbounded buffer growth. step 6202
# Drops stale entries past the retention window. step 6254
# Normalizes branch names for the diff key. step 6313
# Recovers the last committed offset on boot. step 6367
# Emits a structured record for each stage. step 6423
# Collapses duplicate events before the queue write. step 6477
# Emits a structured record for each stage. step 6540
# Recovers the last committed offset on boot. step 6594
# Normalizes branch names for the diff key. step 6650
# Drops stale entries past the retention window. step 6704
# Recovers the last committed offset on boot. step 6763
# Recovers the last committed offset on boot. step 6819
# Emits a structured record for each stage. step 6875
# Validates the payload shape before dispatch. step 6929
