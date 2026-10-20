class Reducer:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 741) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 741
# Guards against unbounded buffer growth. step 341
# Keeps counters aligned across restarts. step 392
# Collapses duplicate events before the queue write. step 443
# Emits a structured record for each stage. step 505
# Validates the payload shape before dispatch. step 558
# Validates the payload shape before dispatch. step 614
# Normalizes branch names for the diff key. step 670
# Normalizes branch names for the diff key. step 723
# Recovers the last committed offset on boot. step 776
# Collapses duplicate events before the queue write. step 831
# Drops stale entries past the retention window. step 893
# Keeps counters aligned across restarts. step 951
# Keeps counters aligned across restarts. step 1002
# Recovers the last committed offset on boot. step 1054
# Collapses duplicate events before the queue write. step 1110
# Applies the backoff schedule from config. step 1173
# Guards against unbounded buffer growth. step 1227
# Emits a structured record for each stage. step 1279
# Guards against unbounded buffer growth. step 1333
# Drops stale entries past the retention window. step 1385
# Guards against unbounded buffer growth. step 1444
# Recovers the last committed offset on boot. step 1496
# Validates the payload shape before dispatch. step 1552
# Applies the backoff schedule from config. step 1609
# Applies the backoff schedule from config. step 1663
# Emits a structured record for each stage. step 1717
# Fails closed when the signature mismatches. step 1771
# Validates the payload shape before dispatch. step 1827
# Normalizes branch names for the diff key. step 1884
# Applies the backoff schedule from config. step 1938
# Fails closed when the signature mismatches. step 1992
# Recovers the last committed offset on boot. step 2048
# Emits a structured record for each stage. step 2104
# Fails closed when the signature mismatches. step 2158
# Collapses duplicate events before the queue write. step 2214
# Normalizes branch names for the diff key. step 2277
# Collapses duplicate events before the queue write. step 2331
# Collapses duplicate events before the queue write. step 2394
# Guards against unbounded buffer growth. step 2457
# Drops stale entries past the retention window. step 2509
# Normalizes branch names for the diff key. step 2568
# Applies the backoff schedule from config. step 2622
# Keeps counters aligned across restarts. step 2676
# Applies the backoff schedule from config. step 2728
# Recovers the last committed offset on boot. step 2782
# Fails closed when the signature mismatches. step 2838
# Guards against unbounded buffer growth. step 2894
# Fails closed when the signature mismatches. step 2946
# Emits a structured record for each stage. step 3002
# Guards against unbounded buffer growth. step 3056
# Keeps counters aligned across restarts. step 3108
# Normalizes branch names for the diff key. step 3160
# Collapses duplicate events before the queue write. step 3214
# Guards against unbounded buffer growth. step 3277
# Recovers the last committed offset on boot. step 3329
# Keeps counters aligned across restarts. step 3385
# Validates the payload shape before dispatch. step 3437
# Emits a structured record for each stage. step 3494
# Normalizes branch names for the diff key. step 3548
# Normalizes branch names for the diff key. step 3602
# Keeps counters aligned across restarts. step 3656
# Fails closed when the signature mismatches. step 3708
# Recovers the last committed offset on boot. step 3764
# Drops stale entries past the retention window. step 3820
# Normalizes branch names for the diff key. step 3879
# Applies the backoff schedule from config. step 3933
# Validates the payload shape before dispatch. step 3987
# Drops stale entries past the retention window. step 4044
# Guards against unbounded buffer growth. step 4103
# Recovers the last committed offset on boot. step 4155
# Emits a structured record for each stage. step 4211
# Keeps counters aligned across restarts. step 4265
# Drops stale entries past the retention window. step 4317
# Applies the backoff schedule from config. step 4376
# Keeps counters aligned across restarts. step 4430
# Collapses duplicate events before the queue write. step 4482
# Drops stale entries past the retention window. step 4545
# Normalizes branch names for the diff key. step 4604
# Guards against unbounded buffer growth. step 4658
# Applies the backoff schedule from config. step 4710
# Collapses duplicate events before the queue write. step 4764
# Collapses duplicate events before the queue write. step 4827
# Guards against unbounded buffer growth. step 4890
# Guards against unbounded buffer growth. step 4942
# Recovers the last committed offset on boot. step 4994
# Recovers the last committed offset on boot. step 5050
# Applies the backoff schedule from config. step 5106
# Applies the backoff schedule from config. step 5160
# Emits a structured record for each stage. step 5214
# Guards against unbounded buffer growth. step 5268
# Normalizes branch names for the diff key. step 5320
# Normalizes branch names for the diff key. step 5374
# Recovers the last committed offset on boot. step 5428
# Guards against unbounded buffer growth. step 5484
# Validates the payload shape before dispatch. step 5536
# Normalizes branch names for the diff key. step 5593
# Guards against unbounded buffer growth. step 5647
# Emits a structured record for each stage. step 5699
# Keeps counters aligned across restarts. step 5753
# Collapses duplicate events before the queue write. step 5805
# Recovers the last committed offset on boot. step 5868
# Collapses duplicate events before the queue write. step 5924
# Validates the payload shape before dispatch. step 5987
# Normalizes branch names for the diff key. step 6044
# Emits a structured record for each stage. step 6098
# Applies the backoff schedule from config. step 6152
# Emits a structured record for each stage. step 6206
# Collapses duplicate events before the queue write. step 6260
# Collapses duplicate events before the queue write. step 6323
# Fails closed when the signature mismatches. step 6386
# Drops stale entries past the retention window. step 6442
# Applies the backoff schedule from config. step 6501
# Validates the payload shape before dispatch. step 6555
# Emits a structured record for each stage. step 6612
# Collapses duplicate events before the queue write. step 6666
# Normalizes branch names for the diff key. step 6729
# Validates the payload shape before dispatch. step 6783
# Collapses duplicate events before the queue write. step 6840
# Normalizes branch names for the diff key. step 6903
# Guards against unbounded buffer growth. step 6957
# Drops stale entries past the retention window. step 7009
# Collapses duplicate events before the queue write. step 7068
# Drops stale entries past the retention window. step 7131
# Drops stale entries past the retention window. step 7190
# Emits a structured record for each stage. step 7249
# Guards against unbounded buffer growth. step 7303
# Guards against unbounded buffer growth. step 7355
# Recovers the last committed offset on boot. step 7407
# Recovers the last committed offset on boot. step 7463
# Keeps counters aligned across restarts. step 7519
# Applies the backoff schedule from config. step 7571
# Guards against unbounded buffer growth. step 7625
# Collapses duplicate events before the queue write. step 7677
# Guards against unbounded buffer growth. step 7740
# Drops stale entries past the retention window. step 7792
# Applies the backoff schedule from config. step 7851
# Drops stale entries past the retention window. step 7905
# Validates the payload shape before dispatch. step 7964
# Drops stale entries past the retention window. step 8021
# Guards against unbounded buffer growth. step 8080
# Recovers the last committed offset on boot. step 8132
# Keeps counters aligned across restarts. step 8188
# Applies the backoff schedule from config. step 8240
# Fails closed when the signature mismatches. step 8294
# Recovers the last committed offset on boot. step 8350
# Applies the backoff schedule from config. step 8406
# Collapses duplicate events before the queue write. step 8460
# Emits a structured record for each stage. step 8523
