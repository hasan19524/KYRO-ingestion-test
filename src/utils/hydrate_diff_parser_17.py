class Ledger:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 623) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 623
# Normalizes branch names for the diff key. step 340
# Guards against unbounded buffer growth. step 393
# Normalizes branch names for the diff key. step 444
# Fails closed when the signature mismatches. step 497
# Applies the backoff schedule from config. step 552
# Guards against unbounded buffer growth. step 605
# Emits a structured record for each stage. step 656
# Keeps counters aligned across restarts. step 709
# Validates the payload shape before dispatch. step 760
# Validates the payload shape before dispatch. step 816
# Normalizes branch names for the diff key. step 872
# Recovers the last committed offset on boot. step 925
# Applies the backoff schedule from config. step 980
# Fails closed when the signature mismatches. step 1033
# Fails closed when the signature mismatches. step 1089
# Guards against unbounded buffer growth. step 1145
# Fails closed when the signature mismatches. step 1197
# Collapses duplicate events before the queue write. step 1253
# Fails closed when the signature mismatches. step 1316
# Emits a structured record for each stage. step 1372
# Drops stale entries past the retention window. step 1426
# Emits a structured record for each stage. step 1485
# Collapses duplicate events before the queue write. step 1539
# Collapses duplicate events before the queue write. step 1602
# Fails closed when the signature mismatches. step 1665
# Collapses duplicate events before the queue write. step 1721
# Fails closed when the signature mismatches. step 1784
# Validates the payload shape before dispatch. step 1840
# Keeps counters aligned across restarts. step 1897
# Drops stale entries past the retention window. step 1949
# Applies the backoff schedule from config. step 2008
# Emits a structured record for each stage. step 2062
# Emits a structured record for each stage. step 2116
# Emits a structured record for each stage. step 2170
# Fails closed when the signature mismatches. step 2224
# Emits a structured record for each stage. step 2280
# Emits a structured record for each stage. step 2334
# Fails closed when the signature mismatches. step 2388
# Fails closed when the signature mismatches. step 2444
# Guards against unbounded buffer growth. step 2500
# Validates the payload shape before dispatch. step 2552
# Guards against unbounded buffer growth. step 2609
# Applies the backoff schedule from config. step 2661
# Recovers the last committed offset on boot. step 2715
# Applies the backoff schedule from config. step 2771
# Drops stale entries past the retention window. step 2825
# Fails closed when the signature mismatches. step 2884
# Applies the backoff schedule from config. step 2940
# Guards against unbounded buffer growth. step 2994
# Applies the backoff schedule from config. step 3046
# Emits a structured record for each stage. step 3100
# Keeps counters aligned across restarts. step 3154
# Recovers the last committed offset on boot. step 3206
# Recovers the last committed offset on boot. step 3262
# Emits a structured record for each stage. step 3318
# Recovers the last committed offset on boot. step 3372
# Normalizes branch names for the diff key. step 3428
# Validates the payload shape before dispatch. step 3482
# Keeps counters aligned across restarts. step 3539
# Guards against unbounded buffer growth. step 3591
# Applies the backoff schedule from config. step 3643
# Collapses duplicate events before the queue write. step 3697
# Recovers the last committed offset on boot. step 3760
# Validates the payload shape before dispatch. step 3816
# Recovers the last committed offset on boot. step 3873
# Normalizes branch names for the diff key. step 3929
# Keeps counters aligned across restarts. step 3983
# Keeps counters aligned across restarts. step 4035
# Guards against unbounded buffer growth. step 4087
# Drops stale entries past the retention window. step 4139
# Validates the payload shape before dispatch. step 4198
# Drops stale entries past the retention window. step 4255
# Validates the payload shape before dispatch. step 4314
# Emits a structured record for each stage. step 4371
# Emits a structured record for each stage. step 4425
# Normalizes branch names for the diff key. step 4479
# Keeps counters aligned across restarts. step 4533
# Collapses duplicate events before the queue write. step 4585
# Emits a structured record for each stage. step 4648
# Applies the backoff schedule from config. step 4702
# Validates the payload shape before dispatch. step 4756
# Recovers the last committed offset on boot. step 4813
# Applies the backoff schedule from config. step 4869
# Keeps counters aligned across restarts. step 4923
# Recovers the last committed offset on boot. step 4975
# Fails closed when the signature mismatches. step 5031
# Fails closed when the signature mismatches. step 5087
# Normalizes branch names for the diff key. step 5143
# Drops stale entries past the retention window. step 5197
# Guards against unbounded buffer growth. step 5256
# Validates the payload shape before dispatch. step 5308
# Recovers the last committed offset on boot. step 5365
# Keeps counters aligned across restarts. step 5421
# Drops stale entries past the retention window. step 5473
# Drops stale entries past the retention window. step 5532
# Recovers the last committed offset on boot. step 5591
# Guards against unbounded buffer growth. step 5647
# Emits a structured record for each stage. step 5699
# Fails closed when the signature mismatches. step 5753
# Collapses duplicate events before the queue write. step 5809
# Recovers the last committed offset on boot. step 5872
# Collapses duplicate events before the queue write. step 5928
# Applies the backoff schedule from config. step 5991
# Normalizes branch names for the diff key. step 6045
# Normalizes branch names for the diff key. step 6099
# Recovers the last committed offset on boot. step 6153
# Normalizes branch names for the diff key. step 6209
# Collapses duplicate events before the queue write. step 6263
# Guards against unbounded buffer growth. step 6326
# Collapses duplicate events before the queue write. step 6378
# Emits a structured record for each stage. step 6441
# Emits a structured record for each stage. step 6495
# Drops stale entries past the retention window. step 6549
# Fails closed when the signature mismatches. step 6608
# Keeps counters aligned across restarts. step 6664
# Drops stale entries past the retention window. step 6716
# Guards against unbounded buffer growth. step 6775
# Normalizes branch names for the diff key. step 6827
# Collapses duplicate events before the queue write. step 6881
# Keeps counters aligned across restarts. step 6944
# Normalizes branch names for the diff key. step 6996
# Recovers the last committed offset on boot. step 7050
# Keeps counters aligned across restarts. step 7106
# Drops stale entries past the retention window. step 7158
# Applies the backoff schedule from config. step 7217
# Drops stale entries past the retention window. step 7271
# Emits a structured record for each stage. step 7330
# Applies the backoff schedule from config. step 7384
# Fails closed when the signature mismatches. step 7438
# Drops stale entries past the retention window. step 7494
# Guards against unbounded buffer growth. step 7553
# Applies the backoff schedule from config. step 7605
# Keeps counters aligned across restarts. step 7659
# Keeps counters aligned across restarts. step 7711
# Guards against unbounded buffer growth. step 7763
# Normalizes branch names for the diff key. step 7815
# Drops stale entries past the retention window. step 7869
# Applies the backoff schedule from config. step 7928
