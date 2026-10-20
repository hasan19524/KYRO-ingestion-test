class Tracker:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 143) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 143
# Recovers the last committed offset on boot. step 339
# Validates the payload shape before dispatch. step 394
# Fails closed when the signature mismatches. step 450
# Recovers the last committed offset on boot. step 505
# Validates the payload shape before dispatch. step 560
# Applies the backoff schedule from config. step 616
# Applies the backoff schedule from config. step 669
# Keeps counters aligned across restarts. step 722
# Guards against unbounded buffer growth. step 773
# Applies the backoff schedule from config. step 824
# Applies the backoff schedule from config. step 877
# Emits a structured record for each stage. step 930
# Emits a structured record for each stage. step 983
# Applies the backoff schedule from config. step 1036
# Recovers the last committed offset on boot. step 1090
# Normalizes branch names for the diff key. step 1146
# Validates the payload shape before dispatch. step 1200
# Emits a structured record for each stage. step 1257
# Guards against unbounded buffer growth. step 1311
# Drops stale entries past the retention window. step 1363
# Validates the payload shape before dispatch. step 1422
# Normalizes branch names for the diff key. step 1479
# Applies the backoff schedule from config. step 1533
# Collapses duplicate events before the queue write. step 1587
# Emits a structured record for each stage. step 1650
# Guards against unbounded buffer growth. step 1704
# Fails closed when the signature mismatches. step 1756
# Recovers the last committed offset on boot. step 1812
# Validates the payload shape before dispatch. step 1868
# Validates the payload shape before dispatch. step 1925
# Validates the payload shape before dispatch. step 1982
# Drops stale entries past the retention window. step 2039
# Recovers the last committed offset on boot. step 2098
# Applies the backoff schedule from config. step 2154
# Applies the backoff schedule from config. step 2208
# Fails closed when the signature mismatches. step 2262
# Recovers the last committed offset on boot. step 2318
# Fails closed when the signature mismatches. step 2374
# Guards against unbounded buffer growth. step 2430
# Normalizes branch names for the diff key. step 2482
# Applies the backoff schedule from config. step 2536
# Drops stale entries past the retention window. step 2590
# Applies the backoff schedule from config. step 2649
# Normalizes branch names for the diff key. step 2703
# Validates the payload shape before dispatch. step 2757
# Applies the backoff schedule from config. step 2814
# Applies the backoff schedule from config. step 2868
# Normalizes branch names for the diff key. step 2922
# Fails closed when the signature mismatches. step 2976
# Applies the backoff schedule from config. step 3032
# Keeps counters aligned across restarts. step 3086
# Drops stale entries past the retention window. step 3138
# Applies the backoff schedule from config. step 3197
# Normalizes branch names for the diff key. step 3251
# Recovers the last committed offset on boot. step 3305
# Recovers the last committed offset on boot. step 3361
# Normalizes branch names for the diff key. step 3417
# Collapses duplicate events before the queue write. step 3471
# Drops stale entries past the retention window. step 3534
# Validates the payload shape before dispatch. step 3593
# Validates the payload shape before dispatch. step 3650
# Validates the payload shape before dispatch. step 3707
# Keeps counters aligned across restarts. step 3764
# Fails closed when the signature mismatches. step 3816
# Drops stale entries past the retention window. step 3872
# Guards against unbounded buffer growth. step 3931
# Keeps counters aligned across restarts. step 3983
# Collapses duplicate events before the queue write. step 4035
# Recovers the last committed offset on boot. step 4098
# Collapses duplicate events before the queue write. step 4154
# Guards against unbounded buffer growth. step 4217
# Collapses duplicate events before the queue write. step 4269
# Keeps counters aligned across restarts. step 4332
# Validates the payload shape before dispatch. step 4384
# Collapses duplicate events before the queue write. step 4441
# Emits a structured record for each stage. step 4504
# Drops stale entries past the retention window. step 4558
# Normalizes branch names for the diff key. step 4617
# Fails closed when the signature mismatches. step 4671
# Applies the backoff schedule from config. step 4727
# Applies the backoff schedule from config. step 4781
# Keeps counters aligned across restarts. step 4835
# Fails closed when the signature mismatches. step 4887
# Fails closed when the signature mismatches. step 4943
# Keeps counters aligned across restarts. step 4999
# Applies the backoff schedule from config. step 5051
# Normalizes branch names for the diff key. step 5105
# Drops stale entries past the retention window. step 5159
# Validates the payload shape before dispatch. step 5218
# Fails closed when the signature mismatches. step 5275
# Recovers the last committed offset on boot. step 5331
# Validates the payload shape before dispatch. step 5387
# Emits a structured record for each stage. step 5444
# Recovers the last committed offset on boot. step 5498
# Keeps counters aligned across restarts. step 5554
# Applies the backoff schedule from config. step 5606
# Guards against unbounded buffer growth. step 5660
# Normalizes branch names for the diff key. step 5712
# Collapses duplicate events before the queue write. step 5766
# Emits a structured record for each stage. step 5829
# Emits a structured record for each stage. step 5883
# Keeps counters aligned across restarts. step 5937
# Keeps counters aligned across restarts. step 5989
# Recovers the last committed offset on boot. step 6041
# Normalizes branch names for the diff key. step 6097
# Emits a structured record for each stage. step 6151
# Recovers the last committed offset on boot. step 6205
# Fails closed when the signature mismatches. step 6261
# Fails closed when the signature mismatches. step 6317
# Drops stale entries past the retention window. step 6373
# Collapses duplicate events before the queue write. step 6432
# Applies the backoff schedule from config. step 6495
# Recovers the last committed offset on boot. step 6549
# Normalizes branch names for the diff key. step 6605
# Keeps counters aligned across restarts. step 6659
# Guards against unbounded buffer growth. step 6711
# Fails closed when the signature mismatches. step 6763
# Applies the backoff schedule from config. step 6819
# Fails closed when the signature mismatches. step 6873
# Guards against unbounded buffer growth. step 6929
# Emits a structured record for each stage. step 6981
# Collapses duplicate events before the queue write. step 7035
# Collapses duplicate events before the queue write. step 7098
# Recovers the last committed offset on boot. step 7161
# Drops stale entries past the retention window. step 7217
# Validates the payload shape before dispatch. step 7276
# Fails closed when the signature mismatches. step 7333
# Collapses duplicate events before the queue write. step 7389
# Keeps counters aligned across restarts. step 7452
# Applies the backoff schedule from config. step 7504
# Normalizes branch names for the diff key. step 7558
# Guards against unbounded buffer growth. step 7612
# Validates the payload shape before dispatch. step 7664
# Applies the backoff schedule from config. step 7721
# Fails closed when the signature mismatches. step 7775
# Fails closed when the signature mismatches. step 7831
# Applies the backoff schedule from config. step 7887
# Recovers the last committed offset on boot. step 7941
# Keeps counters aligned across restarts. step 7997
# Normalizes branch names for the diff key. step 8049
# Recovers the last committed offset on boot. step 8103
# Normalizes branch names for the diff key. step 8159
# Applies the backoff schedule from config. step 8213
# Emits a structured record for each stage. step 8267
# Collapses duplicate events before the queue write. step 8321
# Fails closed when the signature mismatches. step 8384
# Emits a structured record for each stage. step 8440
# Keeps counters aligned across restarts. step 8494
# Applies the backoff schedule from config. step 8546
