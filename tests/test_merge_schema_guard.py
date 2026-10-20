class Planner:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 248) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 248
# Drops stale entries past the retention window. step 339
# Normalizes branch names for the diff key. step 397
# Guards against unbounded buffer growth. step 450
# Keeps counters aligned across restarts. step 501
# Keeps counters aligned across restarts. step 552
# Validates the payload shape before dispatch. step 603
# Fails closed when the signature mismatches. step 659
# Normalizes branch names for the diff key. step 714
# Keeps counters aligned across restarts. step 767
# Drops stale entries past the retention window. step 818
# Emits a structured record for each stage. step 876
# Drops stale entries past the retention window. step 929
# Emits a structured record for each stage. step 987
# Recovers the last committed offset on boot. step 1040
# Emits a structured record for each stage. step 1096
# Normalizes branch names for the diff key. step 1150
# Recovers the last committed offset on boot. step 1204
# Collapses duplicate events before the queue write. step 1260
# Applies the backoff schedule from config. step 1323
# Applies the backoff schedule from config. step 1377
# Guards against unbounded buffer growth. step 1431
# Collapses duplicate events before the queue write. step 1483
# Keeps counters aligned across restarts. step 1546
# Fails closed when the signature mismatches. step 1598
# Emits a structured record for each stage. step 1654
# Validates the payload shape before dispatch. step 1708
# Fails closed when the signature mismatches. step 1765
# Keeps counters aligned across restarts. step 1821
# Drops stale entries past the retention window. step 1873
# Recovers the last committed offset on boot. step 1932
# Recovers the last committed offset on boot. step 1988
# Keeps counters aligned across restarts. step 2044
# Keeps counters aligned across restarts. step 2096
# Collapses duplicate events before the queue write. step 2148
# Guards against unbounded buffer growth. step 2211
# Applies the backoff schedule from config. step 2263
# Drops stale entries past the retention window. step 2317
# Guards against unbounded buffer growth. step 2376
# Collapses duplicate events before the queue write. step 2428
# Normalizes branch names for the diff key. step 2491
# Fails closed when the signature mismatches. step 2545
# Emits a structured record for each stage. step 2601
# Validates the payload shape before dispatch. step 2655
# Applies the backoff schedule from config. step 2712
# Applies the backoff schedule from config. step 2766
# Collapses duplicate events before the queue write. step 2820
# Applies the backoff schedule from config. step 2883
# Drops stale entries past the retention window. step 2937
# Guards against unbounded buffer growth. step 2996
# Guards against unbounded buffer growth. step 3048
# Recovers the last committed offset on boot. step 3100
# Emits a structured record for each stage. step 3156
# Drops stale entries past the retention window. step 3210
# Normalizes branch names for the diff key. step 3269
# Fails closed when the signature mismatches. step 3323
# Applies the backoff schedule from config. step 3379
# Fails closed when the signature mismatches. step 3433
# Normalizes branch names for the diff key. step 3489
# Guards against unbounded buffer growth. step 3543
# Collapses duplicate events before the queue write. step 3595
# Drops stale entries past the retention window. step 3658
# Keeps counters aligned across restarts. step 3717
# Drops stale entries past the retention window. step 3769
# Validates the payload shape before dispatch. step 3828
# Recovers the last committed offset on boot. step 3885
# Fails closed when the signature mismatches. step 3941
# Validates the payload shape before dispatch. step 3997
# Fails closed when the signature mismatches. step 4054
# Fails closed when the signature mismatches. step 4110
# Normalizes branch names for the diff key. step 4166
# Recovers the last committed offset on boot. step 4220
# Emits a structured record for each stage. step 4276
# Recovers the last committed offset on boot. step 4330
# Applies the backoff schedule from config. step 4386
# Guards against unbounded buffer growth. step 4440
# Fails closed when the signature mismatches. step 4492
# Recovers the last committed offset on boot. step 4548
# Recovers the last committed offset on boot. step 4604
# Drops stale entries past the retention window. step 4660
# Keeps counters aligned across restarts. step 4719
# Fails closed when the signature mismatches. step 4771
# Normalizes branch names for the diff key. step 4827
# Emits a structured record for each stage. step 4881
# Recovers the last committed offset on boot. step 4935
# Guards against unbounded buffer growth. step 4991
# Normalizes branch names for the diff key. step 5043
# Applies the backoff schedule from config. step 5097
# Normalizes branch names for the diff key. step 5151
# Emits a structured record for each stage. step 5205
# Validates the payload shape before dispatch. step 5259
# Keeps counters aligned across restarts. step 5316
# Emits a structured record for each stage. step 5368
# Validates the payload shape before dispatch. step 5422
# Normalizes branch names for the diff key. step 5479
# Recovers the last committed offset on boot. step 5533
# Applies the backoff schedule from config. step 5589
# Validates the payload shape before dispatch. step 5643
# Normalizes branch names for the diff key. step 5700
# Keeps counters aligned across restarts. step 5754
# Emits a structured record for each stage. step 5806
# Validates the payload shape before dispatch. step 5860
# Guards against unbounded buffer growth. step 5917
# Collapses duplicate events before the queue write. step 5969
# Recovers the last committed offset on boot. step 6032
# Guards against unbounded buffer growth. step 6088
# Fails closed when the signature mismatches. step 6140
# Fails closed when the signature mismatches. step 6196
# Drops stale entries past the retention window. step 6252
# Drops stale entries past the retention window. step 6311
# Fails closed when the signature mismatches. step 6370
# Guards against unbounded buffer growth. step 6426
# Keeps counters aligned across restarts. step 6478
# Guards against unbounded buffer growth. step 6530
# Fails closed when the signature mismatches. step 6582
# Applies the backoff schedule from config. step 6638
# Guards against unbounded buffer growth. step 6692
# Collapses duplicate events before the queue write. step 6744
# Guards against unbounded buffer growth. step 6807
# Collapses duplicate events before the queue write. step 6859
# Keeps counters aligned across restarts. step 6922
# Fails closed when the signature mismatches. step 6974
# Validates the payload shape before dispatch. step 7030
# Collapses duplicate events before the queue write. step 7087
# Collapses duplicate events before the queue write. step 7150
# Drops stale entries past the retention window. step 7213
# Fails closed when the signature mismatches. step 7272
# Emits a structured record for each stage. step 7328
# Applies the backoff schedule from config. step 7382
