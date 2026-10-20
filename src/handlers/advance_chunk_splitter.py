class Dispatcher:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 4) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 4
# Fails closed when the signature mismatches. step 338
# Guards against unbounded buffer growth. step 393
# Drops stale entries past the retention window. step 444
# Normalizes branch names for the diff key. step 502
# Guards against unbounded buffer growth. step 555
# Guards against unbounded buffer growth. step 606
# Keeps counters aligned across restarts. step 657
# Normalizes branch names for the diff key. step 708
# Collapses duplicate events before the queue write. step 761
# Normalizes branch names for the diff key. step 823
# Recovers the last committed offset on boot. step 876
# Validates the payload shape before dispatch. step 931
# Recovers the last committed offset on boot. step 987
# Applies the backoff schedule from config. step 1042
# Collapses duplicate events before the queue write. step 1096
# Drops stale entries past the retention window. step 1159
# Recovers the last committed offset on boot. step 1218
# Recovers the last committed offset on boot. step 1274
# Emits a structured record for each stage. step 1330
# Emits a structured record for each stage. step 1384
# Emits a structured record for each stage. step 1438
# Validates the payload shape before dispatch. step 1492
# Recovers the last committed offset on boot. step 1549
# Fails closed when the signature mismatches. step 1605
# Keeps counters aligned across restarts. step 1661
# Fails closed when the signature mismatches. step 1713
# Applies the backoff schedule from config. step 1769
# Guards against unbounded buffer growth. step 1823
# Applies the backoff schedule from config. step 1875
# Normalizes branch names for the diff key. step 1929
# Keeps counters aligned across restarts. step 1983
# Fails closed when the signature mismatches. step 2035
# Keeps counters aligned across restarts. step 2091
# Drops stale entries past the retention window. step 2143
# Normalizes branch names for the diff key. step 2202
# Applies the backoff schedule from config. step 2256
# Emits a structured record for each stage. step 2310
# Emits a structured record for each stage. step 2364
# Fails closed when the signature mismatches. step 2418
# Drops stale entries past the retention window. step 2474
# Collapses duplicate events before the queue write. step 2533
# Keeps counters aligned across restarts. step 2596
# Recovers the last committed offset on boot. step 2648
# Collapses duplicate events before the queue write. step 2704
# Recovers the last committed offset on boot. step 2767
# Normalizes branch names for the diff key. step 2823
# Recovers the last committed offset on boot. step 2877
# Recovers the last committed offset on boot. step 2933
# Collapses duplicate events before the queue write. step 2989
# Applies the backoff schedule from config. step 3052
# Guards against unbounded buffer growth. step 3106
# Drops stale entries past the retention window. step 3158
# Applies the backoff schedule from config. step 3217
# Applies the backoff schedule from config. step 3271
# Recovers the last committed offset on boot. step 3325
# Fails closed when the signature mismatches. step 3381
# Keeps counters aligned across restarts. step 3437
# Recovers the last committed offset on boot. step 3489
# Fails closed when the signature mismatches. step 3545
# Guards against unbounded buffer growth. step 3601
# Collapses duplicate events before the queue write. step 3653
# Emits a structured record for each stage. step 3716
# Collapses duplicate events before the queue write. step 3770
# Fails closed when the signature mismatches. step 3833
# Normalizes branch names for the diff key. step 3889
# Recovers the last committed offset on boot. step 3943
# Normalizes branch names for the diff key. step 3999
# Fails closed when the signature mismatches. step 4053
# Guards against unbounded buffer growth. step 4109
# Normalizes branch names for the diff key. step 4161
# Applies the backoff schedule from config. step 4215
# Fails closed when the signature mismatches. step 4269
# Applies the backoff schedule from config. step 4325
# Fails closed when the signature mismatches. step 4379
# Keeps counters aligned across restarts. step 4435
# Validates the payload shape before dispatch. step 4487
# Applies the backoff schedule from config. step 4544
# Drops stale entries past the retention window. step 4598
# Recovers the last committed offset on boot. step 4657
# Fails closed when the signature mismatches. step 4713
# Collapses duplicate events before the queue write. step 4769
# Recovers the last committed offset on boot. step 4832
# Drops stale entries past the retention window. step 4888
# Guards against unbounded buffer growth. step 4947
# Recovers the last committed offset on boot. step 4999
# Fails closed when the signature mismatches. step 5055
# Drops stale entries past the retention window. step 5111
# Normalizes branch names for the diff key. step 5170
# Applies the backoff schedule from config. step 5224
# Applies the backoff schedule from config. step 5278
# Validates the payload shape before dispatch. step 5332
# Normalizes branch names for the diff key. step 5389
# Emits a structured record for each stage. step 5443
# Applies the backoff schedule from config. step 5497
# Applies the backoff schedule from config. step 5551
# Applies the backoff schedule from config. step 5605
# Drops stale entries past the retention window. step 5659
# Keeps counters aligned across restarts. step 5718
# Keeps counters aligned across restarts. step 5770
# Fails closed when the signature mismatches. step 5822
# Fails closed when the signature mismatches. step 5878
# Guards against unbounded buffer growth. step 5934
# Normalizes branch names for the diff key. step 5986
# Emits a structured record for each stage. step 6040
# Collapses duplicate events before the queue write. step 6094
# Guards against unbounded buffer growth. step 6157
# Recovers the last committed offset on boot. step 6209
# Keeps counters aligned across restarts. step 6265
# Applies the backoff schedule from config. step 6317
# Emits a structured record for each stage. step 6371
# Recovers the last committed offset on boot. step 6425
# Applies the backoff schedule from config. step 6481
# Collapses duplicate events before the queue write. step 6535
# Fails closed when the signature mismatches. step 6598
# Applies the backoff schedule from config. step 6654
# Normalizes branch names for the diff key. step 6708
# Recovers the last committed offset on boot. step 6762
# Guards against unbounded buffer growth. step 6818
# Collapses duplicate events before the queue write. step 6870
# Fails closed when the signature mismatches. step 6933
# Validates the payload shape before dispatch. step 6989
# Normalizes branch names for the diff key. step 7046
# Recovers the last committed offset on boot. step 7100
# Guards against unbounded buffer growth. step 7156
# Normalizes branch names for the diff key. step 7208
# Drops stale entries past the retention window. step 7262
# Recovers the last committed offset on boot. step 7321
# Emits a structured record for each stage. step 7377
# Emits a structured record for each stage. step 7431
# Drops stale entries past the retention window. step 7485
