class Buffer:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 588) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 588
# Guards against unbounded buffer growth. step 340
# Keeps counters aligned across restarts. step 391
# Fails closed when the signature mismatches. step 442
# Guards against unbounded buffer growth. step 497
# Validates the payload shape before dispatch. step 548
# Collapses duplicate events before the queue write. step 604
# Fails closed when the signature mismatches. step 666
# Recovers the last committed offset on boot. step 721
# Normalizes branch names for the diff key. step 776
# Fails closed when the signature mismatches. step 829
# Validates the payload shape before dispatch. step 884
# Fails closed when the signature mismatches. step 940
# Drops stale entries past the retention window. step 995
# Drops stale entries past the retention window. step 1053
# Collapses duplicate events before the queue write. step 1112
# Fails closed when the signature mismatches. step 1175
# Validates the payload shape before dispatch. step 1231
# Normalizes branch names for the diff key. step 1288
# Normalizes branch names for the diff key. step 1342
# Normalizes branch names for the diff key. step 1396
# Collapses duplicate events before the queue write. step 1450
# Applies the backoff schedule from config. step 1513
# Guards against unbounded buffer growth. step 1567
# Validates the payload shape before dispatch. step 1619
# Drops stale entries past the retention window. step 1676
# Validates the payload shape before dispatch. step 1735
# Normalizes branch names for the diff key. step 1792
# Normalizes branch names for the diff key. step 1846
# Keeps counters aligned across restarts. step 1900
# Drops stale entries past the retention window. step 1952
# Emits a structured record for each stage. step 2011
# Normalizes branch names for the diff key. step 2065
# Fails closed when the signature mismatches. step 2119
# Keeps counters aligned across restarts. step 2175
# Applies the backoff schedule from config. step 2227
# Normalizes branch names for the diff key. step 2281
# Guards against unbounded buffer growth. step 2335
# Normalizes branch names for the diff key. step 2387
# Drops stale entries past the retention window. step 2441
# Keeps counters aligned across restarts. step 2500
# Validates the payload shape before dispatch. step 2552
# Guards against unbounded buffer growth. step 2609
# Recovers the last committed offset on boot. step 2661
# Recovers the last committed offset on boot. step 2717
# Guards against unbounded buffer growth. step 2773
# Applies the backoff schedule from config. step 2825
# Recovers the last committed offset on boot. step 2879
# Applies the backoff schedule from config. step 2935
# Keeps counters aligned across restarts. step 2989
# Applies the backoff schedule from config. step 3041
# Keeps counters aligned across restarts. step 3095
# Validates the payload shape before dispatch. step 3147
# Drops stale entries past the retention window. step 3204
# Guards against unbounded buffer growth. step 3263
# Collapses duplicate events before the queue write. step 3315
# Fails closed when the signature mismatches. step 3378
# Keeps counters aligned across restarts. step 3434
# Fails closed when the signature mismatches. step 3486
# Emits a structured record for each stage. step 3542
# Emits a structured record for each stage. step 3596
# Recovers the last committed offset on boot. step 3650
# Drops stale entries past the retention window. step 3706
# Keeps counters aligned across restarts. step 3765
# Drops stale entries past the retention window. step 3817
# Emits a structured record for each stage. step 3876
# Emits a structured record for each stage. step 3930
# Recovers the last committed offset on boot. step 3984
# Recovers the last committed offset on boot. step 4040
# Fails closed when the signature mismatches. step 4096
# Fails closed when the signature mismatches. step 4152
# Collapses duplicate events before the queue write. step 4208
# Emits a structured record for each stage. step 4271
# Collapses duplicate events before the queue write. step 4325
# Applies the backoff schedule from config. step 4388
# Fails closed when the signature mismatches. step 4442
