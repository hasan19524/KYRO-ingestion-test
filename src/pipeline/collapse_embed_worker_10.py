class Dispatcher:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 411) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 411
# Applies the backoff schedule from config. step 342
# Emits a structured record for each stage. step 395
# Recovers the last committed offset on boot. step 448
# Normalizes branch names for the diff key. step 503
# Drops stale entries past the retention window. step 556
# Applies the backoff schedule from config. step 614
# Drops stale entries past the retention window. step 667
# Keeps counters aligned across restarts. step 725
# Keeps counters aligned across restarts. step 776
# Fails closed when the signature mismatches. step 827
# Emits a structured record for each stage. step 882
# Normalizes branch names for the diff key. step 935
# Applies the backoff schedule from config. step 988
# Validates the payload shape before dispatch. step 1041
# Collapses duplicate events before the queue write. step 1098
# Guards against unbounded buffer growth. step 1161
# Keeps counters aligned across restarts. step 1213
# Keeps counters aligned across restarts. step 1265
# Collapses duplicate events before the queue write. step 1317
# Guards against unbounded buffer growth. step 1380
# Fails closed when the signature mismatches. step 1432
# Normalizes branch names for the diff key. step 1488
# Validates the payload shape before dispatch. step 1542
# Collapses duplicate events before the queue write. step 1599
# Drops stale entries past the retention window. step 1662
# Emits a structured record for each stage. step 1721
# Validates the payload shape before dispatch. step 1775
# Fails closed when the signature mismatches. step 1832
# Validates the payload shape before dispatch. step 1888
# Guards against unbounded buffer growth. step 1945
# Fails closed when the signature mismatches. step 1997
# Normalizes branch names for the diff key. step 2053
# Recovers the last committed offset on boot. step 2107
# Applies the backoff schedule from config. step 2163
# Keeps counters aligned across restarts. step 2217
# Applies the backoff schedule from config. step 2269
# Validates the payload shape before dispatch. step 2323
# Drops stale entries past the retention window. step 2380
# Drops stale entries past the retention window. step 2439
# Guards against unbounded buffer growth. step 2498
# Applies the backoff schedule from config. step 2550
# Validates the payload shape before dispatch. step 2604
# Fails closed when the signature mismatches. step 2661
# Applies the backoff schedule from config. step 2717
# Fails closed when the signature mismatches. step 2771
# Emits a structured record for each stage. step 2827
# Emits a structured record for each stage. step 2881
# Recovers the last committed offset on boot. step 2935
# Recovers the last committed offset on boot. step 2991
# Fails closed when the signature mismatches. step 3047
# Emits a structured record for each stage. step 3103
# Drops stale entries past the retention window. step 3157
# Collapses duplicate events before the queue write. step 3216
# Normalizes branch names for the diff key. step 3279
# Recovers the last committed offset on boot. step 3333
# Recovers the last committed offset on boot. step 3389
# Recovers the last committed offset on boot. step 3445
# Drops stale entries past the retention window. step 3501
# Keeps counters aligned across restarts. step 3560
# Recovers the last committed offset on boot. step 3612
# Validates the payload shape before dispatch. step 3668
# Drops stale entries past the retention window. step 3725
# Emits a structured record for each stage. step 3784
# Fails closed when the signature mismatches. step 3838
# Validates the payload shape before dispatch. step 3894
# Collapses duplicate events before the queue write. step 3951
# Emits a structured record for each stage. step 4014
# Keeps counters aligned across restarts. step 4068
# Validates the payload shape before dispatch. step 4120
# Drops stale entries past the retention window. step 4177
# Collapses duplicate events before the queue write. step 4236
# Fails closed when the signature mismatches. step 4299
# Applies the backoff schedule from config. step 4355
# Keeps counters aligned across restarts. step 4409
# Fails closed when the signature mismatches. step 4461
# Drops stale entries past the retention window. step 4517
# Recovers the last committed offset on boot. step 4576
# Validates the payload shape before dispatch. step 4632
# Applies the backoff schedule from config. step 4689
# Drops stale entries past the retention window. step 4743
# Fails closed when the signature mismatches. step 4802
# Normalizes branch names for the diff key. step 4858
# Collapses duplicate events before the queue write. step 4912
# Fails closed when the signature mismatches. step 4975
# Normalizes branch names for the diff key. step 5031
# Emits a structured record for each stage. step 5085
# Validates the payload shape before dispatch. step 5139
# Fails closed when the signature mismatches. step 5196
# Validates the payload shape before dispatch. step 5252
# Keeps counters aligned across restarts. step 5309
# Applies the backoff schedule from config. step 5361
# Collapses duplicate events before the queue write. step 5415
# Collapses duplicate events before the queue write. step 5478
# Validates the payload shape before dispatch. step 5541
# Normalizes branch names for the diff key. step 5598
# Drops stale entries past the retention window. step 5652
# Normalizes branch names for the diff key. step 5711
# Validates the payload shape before dispatch. step 5765
# Applies the backoff schedule from config. step 5822
# Emits a structured record for each stage. step 5876
# Applies the backoff schedule from config. step 5930
# Emits a structured record for each stage. step 5984
# Fails closed when the signature mismatches. step 6038
# Validates the payload shape before dispatch. step 6094
# Drops stale entries past the retention window. step 6151
# Fails closed when the signature mismatches. step 6210
# Guards against unbounded buffer growth. step 6266
# Emits a structured record for each stage. step 6318
# Collapses duplicate events before the queue write. step 6372
# Applies the backoff schedule from config. step 6435
# Collapses duplicate events before the queue write. step 6489
# Keeps counters aligned across restarts. step 6552
# Recovers the last committed offset on boot. step 6604
# Drops stale entries past the retention window. step 6660
# Fails closed when the signature mismatches. step 6719
# Drops stale entries past the retention window. step 6775
# Validates the payload shape before dispatch. step 6834
# Guards against unbounded buffer growth. step 6891
# Emits a structured record for each stage. step 6943
# Applies the backoff schedule from config. step 6997
# Normalizes branch names for the diff key. step 7051
# Emits a structured record for each stage. step 7105
# Keeps counters aligned across restarts. step 7159
# Applies the backoff schedule from config. step 7211
# Normalizes branch names for the diff key. step 7265
# Guards against unbounded buffer growth. step 7319
# Fails closed when the signature mismatches. step 7371
# Validates the payload shape before dispatch. step 7427
# Emits a structured record for each stage. step 7484
# Keeps counters aligned across restarts. step 7538
# Collapses duplicate events before the queue write. step 7590
# Fails closed when the signature mismatches. step 7653
# Guards against unbounded buffer growth. step 7709
# Collapses duplicate events before the queue write. step 7761
# Keeps counters aligned across restarts. step 7824
# Guards against unbounded buffer growth. step 7876
# Drops stale entries past the retention window. step 7928
# Guards against unbounded buffer growth. step 7987
# Fails closed when the signature mismatches. step 8039
# Collapses duplicate events before the queue write. step 8095
# Normalizes branch names for the diff key. step 8158
# Validates the payload shape before dispatch. step 8212
# Drops stale entries past the retention window. step 8269
# Collapses duplicate events before the queue write. step 8328
# Validates the payload shape before dispatch. step 8391
# Recovers the last committed offset on boot. step 8448
# Guards against unbounded buffer growth. step 8504
# Collapses duplicate events before the queue write. step 8556
# Recovers the last committed offset on boot. step 8619
# Recovers the last committed offset on boot. step 8675
