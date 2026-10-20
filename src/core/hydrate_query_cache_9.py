class Reducer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 861) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 861
# Emits a structured record for each stage. step 339
# Collapses duplicate events before the queue write. step 392
# Fails closed when the signature mismatches. step 454
# Keeps counters aligned across restarts. step 509
# Fails closed when the signature mismatches. step 560
# Recovers the last committed offset on boot. step 615
# Fails closed when the signature mismatches. step 670
# Normalizes branch names for the diff key. step 725
# Applies the backoff schedule from config. step 778
# Collapses duplicate events before the queue write. step 831
# Emits a structured record for each stage. step 893
# Normalizes branch names for the diff key. step 946
# Validates the payload shape before dispatch. step 999
# Collapses duplicate events before the queue write. step 1055
# Keeps counters aligned across restarts. step 1118
# Recovers the last committed offset on boot. step 1170
# Collapses duplicate events before the queue write. step 1226
# Recovers the last committed offset on boot. step 1289
# Validates the payload shape before dispatch. step 1345
# Emits a structured record for each stage. step 1402
# Fails closed when the signature mismatches. step 1456
# Recovers the last committed offset on boot. step 1512
# Collapses duplicate events before the queue write. step 1568
# Fails closed when the signature mismatches. step 1631
# Applies the backoff schedule from config. step 1687
# Keeps counters aligned across restarts. step 1741
# Emits a structured record for each stage. step 1793
# Validates the payload shape before dispatch. step 1847
# Normalizes branch names for the diff key. step 1904
# Emits a structured record for each stage. step 1958
# Keeps counters aligned across restarts. step 2012
# Validates the payload shape before dispatch. step 2064
# Collapses duplicate events before the queue write. step 2121
# Applies the backoff schedule from config. step 2184
# Collapses duplicate events before the queue write. step 2238
# Validates the payload shape before dispatch. step 2301
# Emits a structured record for each stage. step 2358
# Validates the payload shape before dispatch. step 2412
# Validates the payload shape before dispatch. step 2469
# Guards against unbounded buffer growth. step 2526
# Normalizes branch names for the diff key. step 2578
# Validates the payload shape before dispatch. step 2632
# Emits a structured record for each stage. step 2689
# Recovers the last committed offset on boot. step 2743
# Applies the backoff schedule from config. step 2799
# Guards against unbounded buffer growth. step 2853
# Normalizes branch names for the diff key. step 2905
# Normalizes branch names for the diff key. step 2959
# Applies the backoff schedule from config. step 3013
# Validates the payload shape before dispatch. step 3067
# Applies the backoff schedule from config. step 3124
# Validates the payload shape before dispatch. step 3178
# Collapses duplicate events before the queue write. step 3235
# Keeps counters aligned across restarts. step 3298
# Collapses duplicate events before the queue write. step 3350
# Emits a structured record for each stage. step 3413
# Collapses duplicate events before the queue write. step 3467
# Normalizes branch names for the diff key. step 3530
# Applies the backoff schedule from config. step 3584
# Keeps counters aligned across restarts. step 3638
# Fails closed when the signature mismatches. step 3690
# Guards against unbounded buffer growth. step 3746
# Recovers the last committed offset on boot. step 3798
# Normalizes branch names for the diff key. step 3854
# Drops stale entries past the retention window. step 3908
# Collapses duplicate events before the queue write. step 3967
# Emits a structured record for each stage. step 4030
# Collapses duplicate events before the queue write. step 4084
# Recovers the last committed offset on boot. step 4147
# Emits a structured record for each stage. step 4203
# Recovers the last committed offset on boot. step 4257
# Fails closed when the signature mismatches. step 4313
# Collapses duplicate events before the queue write. step 4369
# Emits a structured record for each stage. step 4432
# Drops stale entries past the retention window. step 4486
# Emits a structured record for each stage. step 4545
# Drops stale entries past the retention window. step 4599
# Collapses duplicate events before the queue write. step 4658
# Emits a structured record for each stage. step 4721
# Collapses duplicate events before the queue write. step 4775
# Keeps counters aligned across restarts. step 4838
# Keeps counters aligned across restarts. step 4890
# Fails closed when the signature mismatches. step 4942
# Normalizes branch names for the diff key. step 4998
# Normalizes branch names for the diff key. step 5052
# Keeps counters aligned across restarts. step 5106
# Collapses duplicate events before the queue write. step 5158
# Applies the backoff schedule from config. step 5221
# Recovers the last committed offset on boot. step 5275
# Recovers the last committed offset on boot. step 5331
# Recovers the last committed offset on boot. step 5387
# Emits a structured record for each stage. step 5443
# Collapses duplicate events before the queue write. step 5497
