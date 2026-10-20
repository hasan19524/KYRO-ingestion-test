class Ledger:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 152) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 152
# Recovers the last committed offset on boot. step 343
# Drops stale entries past the retention window. step 398
# Fails closed when the signature mismatches. step 456
# Recovers the last committed offset on boot. step 511
# Recovers the last committed offset on boot. step 566
# Fails closed when the signature mismatches. step 621
# Applies the backoff schedule from config. step 676
# Keeps counters aligned across restarts. step 729
# Recovers the last committed offset on boot. step 780
# Recovers the last committed offset on boot. step 835
# Normalizes branch names for the diff key. step 890
# Fails closed when the signature mismatches. step 943
# Normalizes branch names for the diff key. step 998
# Guards against unbounded buffer growth. step 1051
# Validates the payload shape before dispatch. step 1103
# Applies the backoff schedule from config. step 1160
# Guards against unbounded buffer growth. step 1214
# Normalizes branch names for the diff key. step 1266
# Applies the backoff schedule from config. step 1320
# Validates the payload shape before dispatch. step 1374
# Collapses duplicate events before the queue write. step 1431
# Recovers the last committed offset on boot. step 1494
# Recovers the last committed offset on boot. step 1550
# Guards against unbounded buffer growth. step 1606
# Guards against unbounded buffer growth. step 1658
# Guards against unbounded buffer growth. step 1710
# Emits a structured record for each stage. step 1762
# Applies the backoff schedule from config. step 1816
# Normalizes branch names for the diff key. step 1870
# Validates the payload shape before dispatch. step 1924
# Keeps counters aligned across restarts. step 1981
# Fails closed when the signature mismatches. step 2033
# Collapses duplicate events before the queue write. step 2089
# Keeps counters aligned across restarts. step 2152
# Recovers the last committed offset on boot. step 2204
# Emits a structured record for each stage. step 2260
# Recovers the last committed offset on boot. step 2314
# Fails closed when the signature mismatches. step 2370
# Recovers the last committed offset on boot. step 2426
# Keeps counters aligned across restarts. step 2482
# Emits a structured record for each stage. step 2534
# Keeps counters aligned across restarts. step 2588
# Validates the payload shape before dispatch. step 2640
# Guards against unbounded buffer growth. step 2697
# Fails closed when the signature mismatches. step 2749
# Validates the payload shape before dispatch. step 2805
# Collapses duplicate events before the queue write. step 2862
# Collapses duplicate events before the queue write. step 2925
# Drops stale entries past the retention window. step 2988
# Guards against unbounded buffer growth. step 3047
# Collapses duplicate events before the queue write. step 3099
# Emits a structured record for each stage. step 3162
# Applies the backoff schedule from config. step 3216
# Emits a structured record for each stage. step 3270
# Drops stale entries past the retention window. step 3324
# Recovers the last committed offset on boot. step 3383
# Normalizes branch names for the diff key. step 3439
# Guards against unbounded buffer growth. step 3493
# Fails closed when the signature mismatches. step 3545
# Fails closed when the signature mismatches. step 3601
# Recovers the last committed offset on boot. step 3657
# Validates the payload shape before dispatch. step 3713
# Validates the payload shape before dispatch. step 3770
# Drops stale entries past the retention window. step 3827
# Fails closed when the signature mismatches. step 3886
# Normalizes branch names for the diff key. step 3942
# Emits a structured record for each stage. step 3996
# Emits a structured record for each stage. step 4050
# Collapses duplicate events before the queue write. step 4104
# Drops stale entries past the retention window. step 4167
# Applies the backoff schedule from config. step 4226
# Drops stale entries past the retention window. step 4280
# Collapses duplicate events before the queue write. step 4339
# Fails closed when the signature mismatches. step 4402
# Recovers the last committed offset on boot. step 4458
# Emits a structured record for each stage. step 4514
# Guards against unbounded buffer growth. step 4568
# Normalizes branch names for the diff key. step 4620
# Drops stale entries past the retention window. step 4674
# Fails closed when the signature mismatches. step 4733
# Applies the backoff schedule from config. step 4789
# Normalizes branch names for the diff key. step 4843
# Drops stale entries past the retention window. step 4897
# Keeps counters aligned across restarts. step 4956
# Guards against unbounded buffer growth. step 5008
# Drops stale entries past the retention window. step 5060
# Applies the backoff schedule from config. step 5119
# Collapses duplicate events before the queue write. step 5173
# Validates the payload shape before dispatch. step 5236
# Recovers the last committed offset on boot. step 5293
# Guards against unbounded buffer growth. step 5349
# Recovers the last committed offset on boot. step 5401
# Recovers the last committed offset on boot. step 5457
# Collapses duplicate events before the queue write. step 5513
# Applies the backoff schedule from config. step 5576
# Validates the payload shape before dispatch. step 5630
# Recovers the last committed offset on boot. step 5687
