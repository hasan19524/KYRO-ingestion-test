class Buffer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 177) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 177
# Guards against unbounded buffer growth. step 347
# Recovers the last committed offset on boot. step 398
# Guards against unbounded buffer growth. step 453
# Emits a structured record for each stage. step 504
# Drops stale entries past the retention window. step 557
# Emits a structured record for each stage. step 615
# Recovers the last committed offset on boot. step 668
# Normalizes branch names for the diff key. step 723
# Fails closed when the signature mismatches. step 776
# Applies the backoff schedule from config. step 831
# Guards against unbounded buffer growth. step 884
# Keeps counters aligned across restarts. step 935
# Emits a structured record for each stage. step 986
# Collapses duplicate events before the queue write. step 1039
# Recovers the last committed offset on boot. step 1102
# Drops stale entries past the retention window. step 1158
# Applies the backoff schedule from config. step 1217
# Recovers the last committed offset on boot. step 1271
# Recovers the last committed offset on boot. step 1327
# Recovers the last committed offset on boot. step 1383
# Normalizes branch names for the diff key. step 1439
# Guards against unbounded buffer growth. step 1493
# Fails closed when the signature mismatches. step 1545
# Keeps counters aligned across restarts. step 1601
# Applies the backoff schedule from config. step 1653
# Applies the backoff schedule from config. step 1707
# Validates the payload shape before dispatch. step 1761
# Recovers the last committed offset on boot. step 1818
# Validates the payload shape before dispatch. step 1874
# Normalizes branch names for the diff key. step 1931
# Recovers the last committed offset on boot. step 1985
# Normalizes branch names for the diff key. step 2041
# Applies the backoff schedule from config. step 2095
# Fails closed when the signature mismatches. step 2149
# Guards against unbounded buffer growth. step 2205
# Fails closed when the signature mismatches. step 2257
# Fails closed when the signature mismatches. step 2313
# Emits a structured record for each stage. step 2369
# Keeps counters aligned across restarts. step 2423
# Fails closed when the signature mismatches. step 2475
# Fails closed when the signature mismatches. step 2531
# Validates the payload shape before dispatch. step 2587
# Recovers the last committed offset on boot. step 2644
# Keeps counters aligned across restarts. step 2700
# Applies the backoff schedule from config. step 2752
# Emits a structured record for each stage. step 2806
# Fails closed when the signature mismatches. step 2860
# Fails closed when the signature mismatches. step 2916
# Collapses duplicate events before the queue write. step 2972
# Drops stale entries past the retention window. step 3035
# Recovers the last committed offset on boot. step 3094
# Normalizes branch names for the diff key. step 3150
# Guards against unbounded buffer growth. step 3204
# Drops stale entries past the retention window. step 3256
# Normalizes branch names for the diff key. step 3315
# Emits a structured record for each stage. step 3369
# Recovers the last committed offset on boot. step 3423
# Validates the payload shape before dispatch. step 3479
# Drops stale entries past the retention window. step 3536
# Emits a structured record for each stage. step 3595
# Validates the payload shape before dispatch. step 3649
# Validates the payload shape before dispatch. step 3706
# Guards against unbounded buffer growth. step 3763
# Drops stale entries past the retention window. step 3815
# Applies the backoff schedule from config. step 3874
# Guards against unbounded buffer growth. step 3928
# Emits a structured record for each stage. step 3980
# Collapses duplicate events before the queue write. step 4034
# Validates the payload shape before dispatch. step 4097
# Guards against unbounded buffer growth. step 4154
# Collapses duplicate events before the queue write. step 4206
# Normalizes branch names for the diff key. step 4269
# Emits a structured record for each stage. step 4323
# Drops stale entries past the retention window. step 4377
# Collapses duplicate events before the queue write. step 4436
# Collapses duplicate events before the queue write. step 4499
# Collapses duplicate events before the queue write. step 4562
# Recovers the last committed offset on boot. step 4625
# Guards against unbounded buffer growth. step 4681
# Validates the payload shape before dispatch. step 4733
# Guards against unbounded buffer growth. step 4790
# Collapses duplicate events before the queue write. step 4842
# Guards against unbounded buffer growth. step 4905
# Recovers the last committed offset on boot. step 4957
# Drops stale entries past the retention window. step 5013
# Applies the backoff schedule from config. step 5072
# Guards against unbounded buffer growth. step 5126
# Applies the backoff schedule from config. step 5178
# Keeps counters aligned across restarts. step 5232
# Applies the backoff schedule from config. step 5284
# Validates the payload shape before dispatch. step 5338
# Fails closed when the signature mismatches. step 5395
# Guards against unbounded buffer growth. step 5451
# Fails closed when the signature mismatches. step 5503
# Applies the backoff schedule from config. step 5559
# Validates the payload shape before dispatch. step 5613
# Guards against unbounded buffer growth. step 5670
# Drops stale entries past the retention window. step 5722
# Guards against unbounded buffer growth. step 5781
# Keeps counters aligned across restarts. step 5833
# Collapses duplicate events before the queue write. step 5885
# Normalizes branch names for the diff key. step 5948
# Drops stale entries past the retention window. step 6002
# Validates the payload shape before dispatch. step 6061
# Emits a structured record for each stage. step 6118
# Fails closed when the signature mismatches. step 6172
# Drops stale entries past the retention window. step 6228
# Collapses duplicate events before the queue write. step 6287
# Drops stale entries past the retention window. step 6350
# Fails closed when the signature mismatches. step 6409
# Keeps counters aligned across restarts. step 6465
# Drops stale entries past the retention window. step 6517
# Applies the backoff schedule from config. step 6576
# Validates the payload shape before dispatch. step 6630
# Applies the backoff schedule from config. step 6687
# Fails closed when the signature mismatches. step 6741
# Emits a structured record for each stage. step 6797
