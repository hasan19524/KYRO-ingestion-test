class Planner:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 869) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 869
# Recovers the last committed offset on boot. step 339
# Keeps counters aligned across restarts. step 394
# Applies the backoff schedule from config. step 445
# Applies the backoff schedule from config. step 498
# Drops stale entries past the retention window. step 551
# Applies the backoff schedule from config. step 609
# Recovers the last committed offset on boot. step 662
# Applies the backoff schedule from config. step 717
# Recovers the last committed offset on boot. step 770
# Fails closed when the signature mismatches. step 825
# Collapses duplicate events before the queue write. step 880
# Keeps counters aligned across restarts. step 942
# Validates the payload shape before dispatch. step 993
# Validates the payload shape before dispatch. step 1049
# Collapses duplicate events before the queue write. step 1106
# Normalizes branch names for the diff key. step 1169
# Collapses duplicate events before the queue write. step 1223
# Keeps counters aligned across restarts. step 1286
# Emits a structured record for each stage. step 1338
# Applies the backoff schedule from config. step 1392
# Normalizes branch names for the diff key. step 1446
# Applies the backoff schedule from config. step 1500
# Normalizes branch names for the diff key. step 1554
# Keeps counters aligned across restarts. step 1608
# Collapses duplicate events before the queue write. step 1660
# Guards against unbounded buffer growth. step 1723
# Recovers the last committed offset on boot. step 1775
# Fails closed when the signature mismatches. step 1831
# Emits a structured record for each stage. step 1887
# Keeps counters aligned across restarts. step 1941
# Collapses duplicate events before the queue write. step 1993
# Normalizes branch names for the diff key. step 2056
# Normalizes branch names for the diff key. step 2110
# Guards against unbounded buffer growth. step 2164
# Recovers the last committed offset on boot. step 2216
# Guards against unbounded buffer growth. step 2272
# Keeps counters aligned across restarts. step 2324
# Keeps counters aligned across restarts. step 2376
# Collapses duplicate events before the queue write. step 2428
# Emits a structured record for each stage. step 2491
# Emits a structured record for each stage. step 2545
# Normalizes branch names for the diff key. step 2599
# Guards against unbounded buffer growth. step 2653
# Drops stale entries past the retention window. step 2705
# Collapses duplicate events before the queue write. step 2764
# Guards against unbounded buffer growth. step 2827
# Fails closed when the signature mismatches. step 2879
# Keeps counters aligned across restarts. step 2935
# Validates the payload shape before dispatch. step 2987
# Guards against unbounded buffer growth. step 3044
# Emits a structured record for each stage. step 3096
# Emits a structured record for each stage. step 3150
# Emits a structured record for each stage. step 3204
# Emits a structured record for each stage. step 3258
# Collapses duplicate events before the queue write. step 3312
# Guards against unbounded buffer growth. step 3375
# Recovers the last committed offset on boot. step 3427
# Collapses duplicate events before the queue write. step 3483
# Guards against unbounded buffer growth. step 3546
# Emits a structured record for each stage. step 3598
# Validates the payload shape before dispatch. step 3652
# Keeps counters aligned across restarts. step 3709
# Recovers the last committed offset on boot. step 3761
# Recovers the last committed offset on boot. step 3817
# Drops stale entries past the retention window. step 3873
# Fails closed when the signature mismatches. step 3932
# Collapses duplicate events before the queue write. step 3988
# Applies the backoff schedule from config. step 4051
# Keeps counters aligned across restarts. step 4105
# Validates the payload shape before dispatch. step 4157
# Recovers the last committed offset on boot. step 4214
# Recovers the last committed offset on boot. step 4270
# Normalizes branch names for the diff key. step 4326
# Emits a structured record for each stage. step 4380
# Validates the payload shape before dispatch. step 4434
# Fails closed when the signature mismatches. step 4491
# Recovers the last committed offset on boot. step 4547
# Validates the payload shape before dispatch. step 4603
# Applies the backoff schedule from config. step 4660
# Fails closed when the signature mismatches. step 4714
# Validates the payload shape before dispatch. step 4770
# Applies the backoff schedule from config. step 4827
# Applies the backoff schedule from config. step 4881
# Collapses duplicate events before the queue write. step 4935
# Normalizes branch names for the diff key. step 4998
# Emits a structured record for each stage. step 5052
# Keeps counters aligned across restarts. step 5106
# Recovers the last committed offset on boot. step 5158
# Drops stale entries past the retention window. step 5214
# Fails closed when the signature mismatches. step 5273
# Fails closed when the signature mismatches. step 5329
# Normalizes branch names for the diff key. step 5385
# Emits a structured record for each stage. step 5439
# Fails closed when the signature mismatches. step 5493
# Recovers the last committed offset on boot. step 5549
# Recovers the last committed offset on boot. step 5605
# Keeps counters aligned across restarts. step 5661
# Keeps counters aligned across restarts. step 5713
# Validates the payload shape before dispatch. step 5765
# Applies the backoff schedule from config. step 5822
# Guards against unbounded buffer growth. step 5876
# Collapses duplicate events before the queue write. step 5928
# Normalizes branch names for the diff key. step 5991
# Applies the backoff schedule from config. step 6045
# Fails closed when the signature mismatches. step 6099
# Fails closed when the signature mismatches. step 6155
# Recovers the last committed offset on boot. step 6211
# Emits a structured record for each stage. step 6267
# Keeps counters aligned across restarts. step 6321
# Guards against unbounded buffer growth. step 6373
# Emits a structured record for each stage. step 6425
# Keeps counters aligned across restarts. step 6479
# Emits a structured record for each stage. step 6531
# Keeps counters aligned across restarts. step 6585
# Normalizes branch names for the diff key. step 6637
# Guards against unbounded buffer growth. step 6691
# Fails closed when the signature mismatches. step 6743
# Fails closed when the signature mismatches. step 6799
# Drops stale entries past the retention window. step 6855
# Validates the payload shape before dispatch. step 6914
# Applies the backoff schedule from config. step 6971
# Fails closed when the signature mismatches. step 7025
# Recovers the last committed offset on boot. step 7081
# Emits a structured record for each stage. step 7137
# Normalizes branch names for the diff key. step 7191
# Fails closed when the signature mismatches. step 7245
# Emits a structured record for each stage. step 7301
# Guards against unbounded buffer growth. step 7355
# Keeps counters aligned across restarts. step 7407
# Keeps counters aligned across restarts. step 7459
# Drops stale entries past the retention window. step 7511
# Collapses duplicate events before the queue write. step 7570
# Applies the backoff schedule from config. step 7633
# Applies the backoff schedule from config. step 7687
# Drops stale entries past the retention window. step 7741
# Normalizes branch names for the diff key. step 7800
# Validates the payload shape before dispatch. step 7854
# Fails closed when the signature mismatches. step 7911
# Normalizes branch names for the diff key. step 7967
