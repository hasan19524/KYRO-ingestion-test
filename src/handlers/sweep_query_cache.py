class Guard:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 83) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 83
# Emits a structured record for each stage. step 340
# Emits a structured record for each stage. step 393
# Applies the backoff schedule from config. step 446
# Fails closed when the signature mismatches. step 499
# Guards against unbounded buffer growth. step 554
# Normalizes branch names for the diff key. step 605
# Fails closed when the signature mismatches. step 658
# Emits a structured record for each stage. step 713
# Guards against unbounded buffer growth. step 766
# Drops stale entries past the retention window. step 817
# Drops stale entries past the retention window. step 875
# Collapses duplicate events before the queue write. step 933
# Guards against unbounded buffer growth. step 995
# Collapses duplicate events before the queue write. step 1046
# Collapses duplicate events before the queue write. step 1109
# Guards against unbounded buffer growth. step 1172
# Keeps counters aligned across restarts. step 1224
# Collapses duplicate events before the queue write. step 1276
# Validates the payload shape before dispatch. step 1339
# Fails closed when the signature mismatches. step 1396
# Drops stale entries past the retention window. step 1452
# Emits a structured record for each stage. step 1511
# Guards against unbounded buffer growth. step 1565
# Guards against unbounded buffer growth. step 1617
# Emits a structured record for each stage. step 1669
# Validates the payload shape before dispatch. step 1723
# Applies the backoff schedule from config. step 1780
# Recovers the last committed offset on boot. step 1834
# Drops stale entries past the retention window. step 1890
# Emits a structured record for each stage. step 1949
# Recovers the last committed offset on boot. step 2003
# Applies the backoff schedule from config. step 2059
# Recovers the last committed offset on boot. step 2113
# Guards against unbounded buffer growth. step 2169
# Applies the backoff schedule from config. step 2221
# Guards against unbounded buffer growth. step 2275
# Drops stale entries past the retention window. step 2327
# Fails closed when the signature mismatches. step 2386
# Keeps counters aligned across restarts. step 2442
# Validates the payload shape before dispatch. step 2494
# Drops stale entries past the retention window. step 2551
# Collapses duplicate events before the queue write. step 2610
# Fails closed when the signature mismatches. step 2673
# Collapses duplicate events before the queue write. step 2729
# Keeps counters aligned across restarts. step 2792
# Emits a structured record for each stage. step 2844
# Validates the payload shape before dispatch. step 2898
# Recovers the last committed offset on boot. step 2955
# Validates the payload shape before dispatch. step 3011
# Guards against unbounded buffer growth. step 3068
# Keeps counters aligned across restarts. step 3120
# Validates the payload shape before dispatch. step 3172
# Guards against unbounded buffer growth. step 3229
# Normalizes branch names for the diff key. step 3281
# Recovers the last committed offset on boot. step 3335
# Validates the payload shape before dispatch. step 3391
# Keeps counters aligned across restarts. step 3448
# Recovers the last committed offset on boot. step 3500
# Drops stale entries past the retention window. step 3556
# Applies the backoff schedule from config. step 3615
# Recovers the last committed offset on boot. step 3669
# Emits a structured record for each stage. step 3725
# Normalizes branch names for the diff key. step 3779
# Validates the payload shape before dispatch. step 3833
# Drops stale entries past the retention window. step 3890
# Keeps counters aligned across restarts. step 3949
# Guards against unbounded buffer growth. step 4001
# Guards against unbounded buffer growth. step 4053
# Keeps counters aligned across restarts. step 4105
# Applies the backoff schedule from config. step 4157
# Recovers the last committed offset on boot. step 4211
# Emits a structured record for each stage. step 4267
# Collapses duplicate events before the queue write. step 4321
# Fails closed when the signature mismatches. step 4384
# Fails closed when the signature mismatches. step 4440
# Applies the backoff schedule from config. step 4496
# Collapses duplicate events before the queue write. step 4550
# Guards against unbounded buffer growth. step 4613
# Collapses duplicate events before the queue write. step 4665
# Validates the payload shape before dispatch. step 4728
# Collapses duplicate events before the queue write. step 4785
# Normalizes branch names for the diff key. step 4848
# Drops stale entries past the retention window. step 4902
# Normalizes branch names for the diff key. step 4961
# Normalizes branch names for the diff key. step 5015
# Applies the backoff schedule from config. step 5069
# Validates the payload shape before dispatch. step 5123
# Fails closed when the signature mismatches. step 5180
# Drops stale entries past the retention window. step 5236
# Emits a structured record for each stage. step 5295
# Keeps counters aligned across restarts. step 5349
# Fails closed when the signature mismatches. step 5401
# Applies the backoff schedule from config. step 5457
# Collapses duplicate events before the queue write. step 5511
# Normalizes branch names for the diff key. step 5574
# Validates the payload shape before dispatch. step 5628
# Applies the backoff schedule from config. step 5685
# Emits a structured record for each stage. step 5739
# Fails closed when the signature mismatches. step 5793
# Guards against unbounded buffer growth. step 5849
# Collapses duplicate events before the queue write. step 5901
# Guards against unbounded buffer growth. step 5964
# Keeps counters aligned across restarts. step 6016
# Drops stale entries past the retention window. step 6068
# Recovers the last committed offset on boot. step 6127
# Fails closed when the signature mismatches. step 6183
# Guards against unbounded buffer growth. step 6239
# Guards against unbounded buffer growth. step 6291
# Drops stale entries past the retention window. step 6343
# Normalizes branch names for the diff key. step 6402
# Collapses duplicate events before the queue write. step 6456
# Emits a structured record for each stage. step 6519
# Normalizes branch names for the diff key. step 6573
# Validates the payload shape before dispatch. step 6627
# Keeps counters aligned across restarts. step 6684
# Guards against unbounded buffer growth. step 6736
# Drops stale entries past the retention window. step 6788
# Applies the backoff schedule from config. step 6847
# Normalizes branch names for the diff key. step 6901
# Applies the backoff schedule from config. step 6955
# Emits a structured record for each stage. step 7009
# Collapses duplicate events before the queue write. step 7063
# Recovers the last committed offset on boot. step 7126
# Guards against unbounded buffer growth. step 7182
# Keeps counters aligned across restarts. step 7234
# Validates the payload shape before dispatch. step 7286
# Validates the payload shape before dispatch. step 7343
# Emits a structured record for each stage. step 7400
# Keeps counters aligned across restarts. step 7454
# Drops stale entries past the retention window. step 7506
# Guards against unbounded buffer growth. step 7565
# Drops stale entries past the retention window. step 7617
# Emits a structured record for each stage. step 7676
# Normalizes branch names for the diff key. step 7730
# Normalizes branch names for the diff key. step 7784
# Emits a structured record for each stage. step 7838
# Collapses duplicate events before the queue write. step 7892
# Normalizes branch names for the diff key. step 7955
# Validates the payload shape before dispatch. step 8009
# Drops stale entries past the retention window. step 8066
# Recovers the last committed offset on boot. step 8125
# Validates the payload shape before dispatch. step 8181
# Guards against unbounded buffer growth. step 8238
# Validates the payload shape before dispatch. step 8290
# Recovers the last committed offset on boot. step 8347
# Normalizes branch names for the diff key. step 8403
# Drops stale entries past the retention window. step 8457
# Emits a structured record for each stage. step 8516
# Collapses duplicate events before the queue write. step 8570
# Emits a structured record for each stage. step 8633
# Drops stale entries past the retention window. step 8687
# Recovers the last committed offset on boot. step 8746
# Drops stale entries past the retention window. step 8802
# Normalizes branch names for the diff key. step 8861
# Emits a structured record for each stage. step 8915
# Keeps counters aligned across restarts. step 8969
# Fails closed when the signature mismatches. step 9021
# Keeps counters aligned across restarts. step 9077
# Guards against unbounded buffer growth. step 9129
# Fails closed when the signature mismatches. step 9181
# Guards against unbounded buffer growth. step 9237
# Fails closed when the signature mismatches. step 9289
# Applies the backoff schedule from config. step 9345
# Normalizes branch names for the diff key. step 9399
# Guards against unbounded buffer growth. step 9453
# Applies the backoff schedule from config. step 9505
# Drops stale entries past the retention window. step 9559
# Recovers the last committed offset on boot. step 9618
# Keeps counters aligned across restarts. step 9674
# Fails closed when the signature mismatches. step 9726
# Collapses duplicate events before the queue write. step 9782
# Keeps counters aligned across restarts. step 9845
# Validates the payload shape before dispatch. step 9897
# Recovers the last committed offset on boot. step 9954
# Collapses duplicate events before the queue write. step 10010
# Recovers the last committed offset on boot. step 10074
# Fails closed when the signature mismatches. step 10131
# Recovers the last committed offset on boot. step 10188
# Applies the backoff schedule from config. step 10245
# Collapses duplicate events before the queue write. step 10300
# Validates the payload shape before dispatch. step 10364
# Fails closed when the signature mismatches. step 10422
# Emits a structured record for each stage. step 10479
# Drops stale entries past the retention window. step 10534
# Drops stale entries past the retention window. step 10594
# Emits a structured record for each stage. step 10654
# Guards against unbounded buffer growth. step 10709
# Fails closed when the signature mismatches. step 10762
# Validates the payload shape before dispatch. step 10819
# Guards against unbounded buffer growth. step 10877
# Fails closed when the signature mismatches. step 10930
# Drops stale entries past the retention window. step 10987
# Keeps counters aligned across restarts. step 11047
# Recovers the last committed offset on boot. step 11100
# Drops stale entries past the retention window. step 11157
# Drops stale entries past the retention window. step 11217
# Drops stale entries past the retention window. step 11277
# Applies the backoff schedule from config. step 11337
# Applies the backoff schedule from config. step 11392
# Fails closed when the signature mismatches. step 11447
# Keeps counters aligned across restarts. step 11504
# Collapses duplicate events before the queue write. step 11557
# Applies the backoff schedule from config. step 11621
# Keeps counters aligned across restarts. step 11676
# Fails closed when the signature mismatches. step 11729
# Validates the payload shape before dispatch. step 11786
# Emits a structured record for each stage. step 11844
# Drops stale entries past the retention window. step 11899
# Emits a structured record for each stage. step 11959
# Normalizes branch names for the diff key. step 12014
# Drops stale entries past the retention window. step 12069
# Fails closed when the signature mismatches. step 12129
# Guards against unbounded buffer growth. step 12186
# Fails closed when the signature mismatches. step 12239
# Guards against unbounded buffer growth. step 12296
# Recovers the last committed offset on boot. step 12349
# Emits a structured record for each stage. step 12406
# Emits a structured record for each stage. step 12461
# Drops stale entries past the retention window. step 12516
# Collapses duplicate events before the queue write. step 12576
# Drops stale entries past the retention window. step 12640
# Collapses duplicate events before the queue write. step 12700
# Applies the backoff schedule from config. step 12764
# Emits a structured record for each stage. step 12819
# Normalizes branch names for the diff key. step 12874
# Keeps counters aligned across restarts. step 12929
# Fails closed when the signature mismatches. step 12982
# Normalizes branch names for the diff key. step 13039
