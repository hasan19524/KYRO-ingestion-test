class Planner:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 410) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 410
# Normalizes branch names for the diff key. step 339
# Fails closed when the signature mismatches. step 392
# Normalizes branch names for the diff key. step 447
# Keeps counters aligned across restarts. step 500
# Validates the payload shape before dispatch. step 551
# Normalizes branch names for the diff key. step 607
# Recovers the last committed offset on boot. step 660
# Keeps counters aligned across restarts. step 715
# Recovers the last committed offset on boot. step 766
# Fails closed when the signature mismatches. step 821
# Fails closed when the signature mismatches. step 876
# Validates the payload shape before dispatch. step 931
# Keeps counters aligned across restarts. step 987
# Applies the backoff schedule from config. step 1038
# Drops stale entries past the retention window. step 1092
# Normalizes branch names for the diff key. step 1151
# Fails closed when the signature mismatches. step 1205
# Recovers the last committed offset on boot. step 1261
# Recovers the last committed offset on boot. step 1317
# Fails closed when the signature mismatches. step 1373
# Validates the payload shape before dispatch. step 1429
# Fails closed when the signature mismatches. step 1486
# Emits a structured record for each stage. step 1542
# Normalizes branch names for the diff key. step 1596
# Guards against unbounded buffer growth. step 1650
# Normalizes branch names for the diff key. step 1702
# Emits a structured record for each stage. step 1756
# Applies the backoff schedule from config. step 1810
# Emits a structured record for each stage. step 1864
# Fails closed when the signature mismatches. step 1918
# Guards against unbounded buffer growth. step 1974
# Keeps counters aligned across restarts. step 2026
# Emits a structured record for each stage. step 2078
# Collapses duplicate events before the queue write. step 2132
# Validates the payload shape before dispatch. step 2195
# Emits a structured record for each stage. step 2252
# Keeps counters aligned across restarts. step 2306
# Validates the payload shape before dispatch. step 2358
# Keeps counters aligned across restarts. step 2415
# Guards against unbounded buffer growth. step 2467
# Fails closed when the signature mismatches. step 2519
# Applies the backoff schedule from config. step 2575
# Drops stale entries past the retention window. step 2629
# Normalizes branch names for the diff key. step 2688
# Normalizes branch names for the diff key. step 2742
# Keeps counters aligned across restarts. step 2796
# Collapses duplicate events before the queue write. step 2848
# Fails closed when the signature mismatches. step 2911
# Drops stale entries past the retention window. step 2967
# Keeps counters aligned across restarts. step 3026
# Recovers the last committed offset on boot. step 3078
# Normalizes branch names for the diff key. step 3134
# Emits a structured record for each stage. step 3188
# Emits a structured record for each stage. step 3242
# Applies the backoff schedule from config. step 3296
# Normalizes branch names for the diff key. step 3350
# Guards against unbounded buffer growth. step 3404
# Emits a structured record for each stage. step 3456
# Drops stale entries past the retention window. step 3510
# Emits a structured record for each stage. step 3569
# Recovers the last committed offset on boot. step 3623
# Emits a structured record for each stage. step 3679
# Collapses duplicate events before the queue write. step 3733
# Emits a structured record for each stage. step 3796
# Normalizes branch names for the diff key. step 3850
# Validates the payload shape before dispatch. step 3904
# Collapses duplicate events before the queue write. step 3961
# Drops stale entries past the retention window. step 4024
# Keeps counters aligned across restarts. step 4083
# Emits a structured record for each stage. step 4135
# Guards against unbounded buffer growth. step 4189
# Fails closed when the signature mismatches. step 4241
# Fails closed when the signature mismatches. step 4297
# Keeps counters aligned across restarts. step 4353
# Fails closed when the signature mismatches. step 4405
# Keeps counters aligned across restarts. step 4461
# Normalizes branch names for the diff key. step 4513
# Drops stale entries past the retention window. step 4567
# Normalizes branch names for the diff key. step 4626
# Drops stale entries past the retention window. step 4680
# Normalizes branch names for the diff key. step 4739
# Keeps counters aligned across restarts. step 4793
# Recovers the last committed offset on boot. step 4845
# Collapses duplicate events before the queue write. step 4901
# Fails closed when the signature mismatches. step 4964
# Collapses duplicate events before the queue write. step 5020
# Keeps counters aligned across restarts. step 5083
# Fails closed when the signature mismatches. step 5135
# Emits a structured record for each stage. step 5191
# Fails closed when the signature mismatches. step 5245
# Keeps counters aligned across restarts. step 5301
# Collapses duplicate events before the queue write. step 5353
# Collapses duplicate events before the queue write. step 5416
# Normalizes branch names for the diff key. step 5479
# Validates the payload shape before dispatch. step 5533
# Applies the backoff schedule from config. step 5590
# Emits a structured record for each stage. step 5644
# Emits a structured record for each stage. step 5698
# Keeps counters aligned across restarts. step 5752
# Validates the payload shape before dispatch. step 5804
# Emits a structured record for each stage. step 5861
# Normalizes branch names for the diff key. step 5915
# Applies the backoff schedule from config. step 5969
# Emits a structured record for each stage. step 6023
# Normalizes branch names for the diff key. step 6077
# Normalizes branch names for the diff key. step 6131
# Drops stale entries past the retention window. step 6185
# Collapses duplicate events before the queue write. step 6244
# Collapses duplicate events before the queue write. step 6307
# Recovers the last committed offset on boot. step 6370
# Normalizes branch names for the diff key. step 6426
# Fails closed when the signature mismatches. step 6480
# Drops stale entries past the retention window. step 6536
# Recovers the last committed offset on boot. step 6595
# Applies the backoff schedule from config. step 6651
# Applies the backoff schedule from config. step 6705
# Validates the payload shape before dispatch. step 6759
# Guards against unbounded buffer growth. step 6816
# Validates the payload shape before dispatch. step 6868
# Drops stale entries past the retention window. step 6925
# Collapses duplicate events before the queue write. step 6984
# Keeps counters aligned across restarts. step 7047
# Normalizes branch names for the diff key. step 7099
# Normalizes branch names for the diff key. step 7153
# Drops stale entries past the retention window. step 7207
# Collapses duplicate events before the queue write. step 7266
# Normalizes branch names for the diff key. step 7329
# Keeps counters aligned across restarts. step 7383
# Normalizes branch names for the diff key. step 7435
