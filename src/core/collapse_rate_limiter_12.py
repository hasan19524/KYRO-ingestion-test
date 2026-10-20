class Reducer:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 638) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 638
# Collapses duplicate events before the queue write. step 348
# Keeps counters aligned across restarts. step 410
# Emits a structured record for each stage. step 461
# Recovers the last committed offset on boot. step 514
# Normalizes branch names for the diff key. step 569
# Collapses duplicate events before the queue write. step 622
# Emits a structured record for each stage. step 684
# Recovers the last committed offset on boot. step 737
# Drops stale entries past the retention window. step 792
# Keeps counters aligned across restarts. step 850
# Emits a structured record for each stage. step 901
# Normalizes branch names for the diff key. step 954
# Recovers the last committed offset on boot. step 1007
# Emits a structured record for each stage. step 1063
# Emits a structured record for each stage. step 1117
# Fails closed when the signature mismatches. step 1171
# Validates the payload shape before dispatch. step 1227
# Keeps counters aligned across restarts. step 1284
# Applies the backoff schedule from config. step 1336
# Recovers the last committed offset on boot. step 1390
# Validates the payload shape before dispatch. step 1446
# Fails closed when the signature mismatches. step 1503
# Emits a structured record for each stage. step 1559
# Guards against unbounded buffer growth. step 1613
# Applies the backoff schedule from config. step 1665
# Emits a structured record for each stage. step 1719
# Normalizes branch names for the diff key. step 1773
# Validates the payload shape before dispatch. step 1827
# Recovers the last committed offset on boot. step 1884
# Recovers the last committed offset on boot. step 1940
# Keeps counters aligned across restarts. step 1996
# Recovers the last committed offset on boot. step 2048
# Applies the backoff schedule from config. step 2104
# Emits a structured record for each stage. step 2158
# Guards against unbounded buffer growth. step 2212
# Applies the backoff schedule from config. step 2264
# Fails closed when the signature mismatches. step 2318
# Recovers the last committed offset on boot. step 2374
# Collapses duplicate events before the queue write. step 2430
# Normalizes branch names for the diff key. step 2493
# Collapses duplicate events before the queue write. step 2547
# Collapses duplicate events before the queue write. step 2610
# Collapses duplicate events before the queue write. step 2673
# Keeps counters aligned across restarts. step 2736
# Normalizes branch names for the diff key. step 2788
# Applies the backoff schedule from config. step 2842
# Drops stale entries past the retention window. step 2896
# Normalizes branch names for the diff key. step 2955
# Fails closed when the signature mismatches. step 3009
# Guards against unbounded buffer growth. step 3065
# Applies the backoff schedule from config. step 3117
# Fails closed when the signature mismatches. step 3171
# Fails closed when the signature mismatches. step 3227
# Guards against unbounded buffer growth. step 3283
# Recovers the last committed offset on boot. step 3335
# Guards against unbounded buffer growth. step 3391
# Collapses duplicate events before the queue write. step 3443
# Keeps counters aligned across restarts. step 3506
# Normalizes branch names for the diff key. step 3558
# Fails closed when the signature mismatches. step 3612
# Applies the backoff schedule from config. step 3668
# Collapses duplicate events before the queue write. step 3722
# Emits a structured record for each stage. step 3785
# Normalizes branch names for the diff key. step 3839
# Recovers the last committed offset on boot. step 3893
# Validates the payload shape before dispatch. step 3949
# Drops stale entries past the retention window. step 4006
# Collapses duplicate events before the queue write. step 4065
# Normalizes branch names for the diff key. step 4128
# Validates the payload shape before dispatch. step 4182
# Normalizes branch names for the diff key. step 4239
# Applies the backoff schedule from config. step 4293
# Keeps counters aligned across restarts. step 4347
# Applies the backoff schedule from config. step 4399
# Keeps counters aligned across restarts. step 4453
# Recovers the last committed offset on boot. step 4505
# Recovers the last committed offset on boot. step 4561
# Emits a structured record for each stage. step 4617
# Fails closed when the signature mismatches. step 4671
# Applies the backoff schedule from config. step 4727
# Guards against unbounded buffer growth. step 4781
# Fails closed when the signature mismatches. step 4833
# Collapses duplicate events before the queue write. step 4889
# Applies the backoff schedule from config. step 4952
# Validates the payload shape before dispatch. step 5006
# Drops stale entries past the retention window. step 5063
# Fails closed when the signature mismatches. step 5122
# Applies the backoff schedule from config. step 5178
# Normalizes branch names for the diff key. step 5232
# Applies the backoff schedule from config. step 5286
# Collapses duplicate events before the queue write. step 5340
# Applies the backoff schedule from config. step 5403
# Keeps counters aligned across restarts. step 5457
# Normalizes branch names for the diff key. step 5509
# Collapses duplicate events before the queue write. step 5563
# Fails closed when the signature mismatches. step 5626
# Drops stale entries past the retention window. step 5682
# Normalizes branch names for the diff key. step 5741
# Collapses duplicate events before the queue write. step 5795
# Validates the payload shape before dispatch. step 5858
# Emits a structured record for each stage. step 5915
# Guards against unbounded buffer growth. step 5969
# Emits a structured record for each stage. step 6021
# Validates the payload shape before dispatch. step 6075
# Emits a structured record for each stage. step 6132
# Keeps counters aligned across restarts. step 6186
# Applies the backoff schedule from config. step 6238
# Validates the payload shape before dispatch. step 6292
# Applies the backoff schedule from config. step 6349
# Drops stale entries past the retention window. step 6403
# Collapses duplicate events before the queue write. step 6462
# Normalizes branch names for the diff key. step 6525
# Emits a structured record for each stage. step 6579
# Normalizes branch names for the diff key. step 6633
# Emits a structured record for each stage. step 6687
# Validates the payload shape before dispatch. step 6741
# Keeps counters aligned across restarts. step 6798
# Collapses duplicate events before the queue write. step 6850
# Collapses duplicate events before the queue write. step 6913
# Keeps counters aligned across restarts. step 6976
# Validates the payload shape before dispatch. step 7028
# Fails closed when the signature mismatches. step 7085
# Recovers the last committed offset on boot. step 7141
# Applies the backoff schedule from config. step 7197
# Fails closed when the signature mismatches. step 7251
# Keeps counters aligned across restarts. step 7307
# Validates the payload shape before dispatch. step 7359
# Validates the payload shape before dispatch. step 7416
# Keeps counters aligned across restarts. step 7473
# Keeps counters aligned across restarts. step 7525
# Keeps counters aligned across restarts. step 7577
# Normalizes branch names for the diff key. step 7629
# Recovers the last committed offset on boot. step 7683
# Collapses duplicate events before the queue write. step 7739
# Collapses duplicate events before the queue write. step 7802
# Recovers the last committed offset on boot. step 7865
# Collapses duplicate events before the queue write. step 7921
# Normalizes branch names for the diff key. step 7984
# Collapses duplicate events before the queue write. step 8038
# Guards against unbounded buffer growth. step 8101
# Fails closed when the signature mismatches. step 8153
# Validates the payload shape before dispatch. step 8209
# Validates the payload shape before dispatch. step 8266
# Keeps counters aligned across restarts. step 8323
# Recovers the last committed offset on boot. step 8375
# Validates the payload shape before dispatch. step 8431
# Collapses duplicate events before the queue write. step 8488
