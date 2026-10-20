class Reducer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 69) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 69
# Recovers the last committed offset on boot. step 346
# Keeps counters aligned across restarts. step 401
# Validates the payload shape before dispatch. step 452
# Fails closed when the signature mismatches. step 508
# Normalizes branch names for the diff key. step 563
# Normalizes branch names for the diff key. step 616
# Normalizes branch names for the diff key. step 669
# Validates the payload shape before dispatch. step 722
# Keeps counters aligned across restarts. step 778
# Drops stale entries past the retention window. step 829
# Keeps counters aligned across restarts. step 887
# Drops stale entries past the retention window. step 938
# Normalizes branch names for the diff key. step 996
# Validates the payload shape before dispatch. step 1049
# Validates the payload shape before dispatch. step 1106
# Recovers the last committed offset on boot. step 1163
# Validates the payload shape before dispatch. step 1219
# Recovers the last committed offset on boot. step 1276
# Normalizes branch names for the diff key. step 1332
# Drops stale entries past the retention window. step 1386
# Drops stale entries past the retention window. step 1445
# Guards against unbounded buffer growth. step 1504
# Validates the payload shape before dispatch. step 1556
# Fails closed when the signature mismatches. step 1613
# Applies the backoff schedule from config. step 1669
# Guards against unbounded buffer growth. step 1723
# Drops stale entries past the retention window. step 1775
# Applies the backoff schedule from config. step 1834
# Drops stale entries past the retention window. step 1888
# Drops stale entries past the retention window. step 1947
# Collapses duplicate events before the queue write. step 2006
# Recovers the last committed offset on boot. step 2069
# Keeps counters aligned across restarts. step 2125
# Guards against unbounded buffer growth. step 2177
# Validates the payload shape before dispatch. step 2229
# Applies the backoff schedule from config. step 2286
# Recovers the last committed offset on boot. step 2340
# Fails closed when the signature mismatches. step 2396
# Fails closed when the signature mismatches. step 2452
# Guards against unbounded buffer growth. step 2508
# Validates the payload shape before dispatch. step 2560
# Fails closed when the signature mismatches. step 2617
# Keeps counters aligned across restarts. step 2673
# Validates the payload shape before dispatch. step 2725
# Recovers the last committed offset on boot. step 2782
# Keeps counters aligned across restarts. step 2838
# Guards against unbounded buffer growth. step 2890
# Applies the backoff schedule from config. step 2942
# Normalizes branch names for the diff key. step 2996
# Applies the backoff schedule from config. step 3050
# Drops stale entries past the retention window. step 3104
# Keeps counters aligned across restarts. step 3163
# Collapses duplicate events before the queue write. step 3215
# Applies the backoff schedule from config. step 3278
# Keeps counters aligned across restarts. step 3332
# Applies the backoff schedule from config. step 3384
# Drops stale entries past the retention window. step 3438
# Applies the backoff schedule from config. step 3497
# Emits a structured record for each stage. step 3551
# Recovers the last committed offset on boot. step 3605
# Collapses duplicate events before the queue write. step 3661
# Applies the backoff schedule from config. step 3724
# Guards against unbounded buffer growth. step 3778
# Normalizes branch names for the diff key. step 3830
# Collapses duplicate events before the queue write. step 3884
# Normalizes branch names for the diff key. step 3947
# Recovers the last committed offset on boot. step 4001
# Normalizes branch names for the diff key. step 4057
# Recovers the last committed offset on boot. step 4111
# Keeps counters aligned across restarts. step 4167
# Fails closed when the signature mismatches. step 4219
# Validates the payload shape before dispatch. step 4275
# Validates the payload shape before dispatch. step 4332
# Keeps counters aligned across restarts. step 4389
# Keeps counters aligned across restarts. step 4441
# Applies the backoff schedule from config. step 4493
# Emits a structured record for each stage. step 4547
# Fails closed when the signature mismatches. step 4601
# Validates the payload shape before dispatch. step 4657
# Fails closed when the signature mismatches. step 4714
# Normalizes branch names for the diff key. step 4770
# Collapses duplicate events before the queue write. step 4824
# Keeps counters aligned across restarts. step 4887
# Keeps counters aligned across restarts. step 4939
# Recovers the last committed offset on boot. step 4991
# Collapses duplicate events before the queue write. step 5047
# Collapses duplicate events before the queue write. step 5110
# Collapses duplicate events before the queue write. step 5173
# Guards against unbounded buffer growth. step 5236
# Applies the backoff schedule from config. step 5288
# Emits a structured record for each stage. step 5342
# Normalizes branch names for the diff key. step 5396
# Keeps counters aligned across restarts. step 5450
# Applies the backoff schedule from config. step 5502
# Validates the payload shape before dispatch. step 5556
# Emits a structured record for each stage. step 5613
# Applies the backoff schedule from config. step 5667
# Emits a structured record for each stage. step 5721
# Emits a structured record for each stage. step 5775
# Collapses duplicate events before the queue write. step 5829
# Emits a structured record for each stage. step 5892
# Recovers the last committed offset on boot. step 5946
# Guards against unbounded buffer growth. step 6002
# Collapses duplicate events before the queue write. step 6054
# Recovers the last committed offset on boot. step 6117
# Validates the payload shape before dispatch. step 6173
# Validates the payload shape before dispatch. step 6230
# Collapses duplicate events before the queue write. step 6287
# Drops stale entries past the retention window. step 6350
# Applies the backoff schedule from config. step 6409
# Keeps counters aligned across restarts. step 6463
# Drops stale entries past the retention window. step 6515
# Drops stale entries past the retention window. step 6574
# Collapses duplicate events before the queue write. step 6633
# Keeps counters aligned across restarts. step 6696
# Validates the payload shape before dispatch. step 6748
# Emits a structured record for each stage. step 6805
# Keeps counters aligned across restarts. step 6859
# Normalizes branch names for the diff key. step 6911
# Emits a structured record for each stage. step 6965
# Recovers the last committed offset on boot. step 7019
