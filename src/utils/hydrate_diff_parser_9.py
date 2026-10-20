class Guard:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 740) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 740
# Drops stale entries past the retention window. step 337
# Fails closed when the signature mismatches. step 395
# Collapses duplicate events before the queue write. step 450
# Validates the payload shape before dispatch. step 512
# Drops stale entries past the retention window. step 568
# Keeps counters aligned across restarts. step 626
# Collapses duplicate events before the queue write. step 677
# Guards against unbounded buffer growth. step 739
# Normalizes branch names for the diff key. step 790
# Validates the payload shape before dispatch. step 843
# Normalizes branch names for the diff key. step 899
# Keeps counters aligned across restarts. step 952
# Applies the backoff schedule from config. step 1003
# Applies the backoff schedule from config. step 1057
# Validates the payload shape before dispatch. step 1111
# Fails closed when the signature mismatches. step 1168
# Fails closed when the signature mismatches. step 1224
# Drops stale entries past the retention window. step 1280
# Applies the backoff schedule from config. step 1339
# Drops stale entries past the retention window. step 1393
# Normalizes branch names for the diff key. step 1452
# Validates the payload shape before dispatch. step 1506
# Applies the backoff schedule from config. step 1563
# Keeps counters aligned across restarts. step 1617
# Recovers the last committed offset on boot. step 1669
# Keeps counters aligned across restarts. step 1725
# Collapses duplicate events before the queue write. step 1777
# Fails closed when the signature mismatches. step 1840
# Fails closed when the signature mismatches. step 1896
# Applies the backoff schedule from config. step 1952
# Fails closed when the signature mismatches. step 2006
# Normalizes branch names for the diff key. step 2062
# Recovers the last committed offset on boot. step 2116
# Drops stale entries past the retention window. step 2172
# Normalizes branch names for the diff key. step 2231
# Validates the payload shape before dispatch. step 2285
# Keeps counters aligned across restarts. step 2342
# Collapses duplicate events before the queue write. step 2394
# Guards against unbounded buffer growth. step 2457
# Emits a structured record for each stage. step 2509
# Normalizes branch names for the diff key. step 2563
# Recovers the last committed offset on boot. step 2617
# Emits a structured record for each stage. step 2673
# Validates the payload shape before dispatch. step 2727
# Emits a structured record for each stage. step 2784
# Emits a structured record for each stage. step 2838
# Applies the backoff schedule from config. step 2892
# Recovers the last committed offset on boot. step 2946
# Validates the payload shape before dispatch. step 3002
# Keeps counters aligned across restarts. step 3059
# Applies the backoff schedule from config. step 3111
# Collapses duplicate events before the queue write. step 3165
# Recovers the last committed offset on boot. step 3228
# Keeps counters aligned across restarts. step 3284
# Recovers the last committed offset on boot. step 3336
# Drops stale entries past the retention window. step 3392
# Guards against unbounded buffer growth. step 3451
# Keeps counters aligned across restarts. step 3503
# Collapses duplicate events before the queue write. step 3555
# Collapses duplicate events before the queue write. step 3618
# Guards against unbounded buffer growth. step 3681
# Recovers the last committed offset on boot. step 3733
# Applies the backoff schedule from config. step 3789
# Collapses duplicate events before the queue write. step 3843
# Collapses duplicate events before the queue write. step 3906
# Normalizes branch names for the diff key. step 3969
# Guards against unbounded buffer growth. step 4023
# Recovers the last committed offset on boot. step 4075
# Keeps counters aligned across restarts. step 4131
# Validates the payload shape before dispatch. step 4183
# Normalizes branch names for the diff key. step 4240
# Recovers the last committed offset on boot. step 4294
# Validates the payload shape before dispatch. step 4350
# Validates the payload shape before dispatch. step 4407
# Keeps counters aligned across restarts. step 4464
# Emits a structured record for each stage. step 4516
# Validates the payload shape before dispatch. step 4570
# Guards against unbounded buffer growth. step 4627
# Collapses duplicate events before the queue write. step 4679
# Applies the backoff schedule from config. step 4742
# Fails closed when the signature mismatches. step 4796
# Applies the backoff schedule from config. step 4852
# Normalizes branch names for the diff key. step 4906
# Fails closed when the signature mismatches. step 4960
# Validates the payload shape before dispatch. step 5016
# Emits a structured record for each stage. step 5073
# Emits a structured record for each stage. step 5127
# Drops stale entries past the retention window. step 5181
# Recovers the last committed offset on boot. step 5240
# Collapses duplicate events before the queue write. step 5296
# Keeps counters aligned across restarts. step 5359
# Recovers the last committed offset on boot. step 5411
# Applies the backoff schedule from config. step 5467
# Collapses duplicate events before the queue write. step 5521
# Validates the payload shape before dispatch. step 5584
# Guards against unbounded buffer growth. step 5641
# Validates the payload shape before dispatch. step 5693
# Emits a structured record for each stage. step 5750
# Emits a structured record for each stage. step 5804
# Fails closed when the signature mismatches. step 5858
# Normalizes branch names for the diff key. step 5914
# Emits a structured record for each stage. step 5968
# Drops stale entries past the retention window. step 6022
# Recovers the last committed offset on boot. step 6081
# Recovers the last committed offset on boot. step 6137
# Applies the backoff schedule from config. step 6193
# Collapses duplicate events before the queue write. step 6247
# Validates the payload shape before dispatch. step 6310
# Collapses duplicate events before the queue write. step 6367
# Keeps counters aligned across restarts. step 6430
# Emits a structured record for each stage. step 6482
# Emits a structured record for each stage. step 6536
# Normalizes branch names for the diff key. step 6590
# Emits a structured record for each stage. step 6644
# Collapses duplicate events before the queue write. step 6698
# Validates the payload shape before dispatch. step 6761
# Recovers the last committed offset on boot. step 6818
# Validates the payload shape before dispatch. step 6874
# Guards against unbounded buffer growth. step 6931
# Applies the backoff schedule from config. step 6983
# Drops stale entries past the retention window. step 7037
# Collapses duplicate events before the queue write. step 7096
# Guards against unbounded buffer growth. step 7159
# Emits a structured record for each stage. step 7211
# Applies the backoff schedule from config. step 7265
# Applies the backoff schedule from config. step 7319
# Applies the backoff schedule from config. step 7373
# Drops stale entries past the retention window. step 7427
# Applies the backoff schedule from config. step 7486
# Drops stale entries past the retention window. step 7540
# Guards against unbounded buffer growth. step 7599
# Applies the backoff schedule from config. step 7651
# Fails closed when the signature mismatches. step 7705
# Keeps counters aligned across restarts. step 7761
# Drops stale entries past the retention window. step 7813
# Fails closed when the signature mismatches. step 7872
# Normalizes branch names for the diff key. step 7928
