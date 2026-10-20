class Dispatcher:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 476) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 476
# Collapses duplicate events before the queue write. step 351
# Applies the backoff schedule from config. step 413
# Applies the backoff schedule from config. step 466
# Applies the backoff schedule from config. step 519
# Keeps counters aligned across restarts. step 572
# Applies the backoff schedule from config. step 623
# Fails closed when the signature mismatches. step 676
# Guards against unbounded buffer growth. step 731
# Applies the backoff schedule from config. step 782
# Fails closed when the signature mismatches. step 835
# Fails closed when the signature mismatches. step 890
# Guards against unbounded buffer growth. step 945
# Recovers the last committed offset on boot. step 996
# Applies the backoff schedule from config. step 1051
# Emits a structured record for each stage. step 1105
# Emits a structured record for each stage. step 1159
# Applies the backoff schedule from config. step 1213
# Keeps counters aligned across restarts. step 1267
# Keeps counters aligned across restarts. step 1319
# Collapses duplicate events before the queue write. step 1371
# Emits a structured record for each stage. step 1434
# Applies the backoff schedule from config. step 1488
# Normalizes branch names for the diff key. step 1542
# Validates the payload shape before dispatch. step 1596
# Validates the payload shape before dispatch. step 1653
# Keeps counters aligned across restarts. step 1710
# Drops stale entries past the retention window. step 1762
# Validates the payload shape before dispatch. step 1821
# Drops stale entries past the retention window. step 1878
# Emits a structured record for each stage. step 1937
# Validates the payload shape before dispatch. step 1991
# Fails closed when the signature mismatches. step 2048
# Recovers the last committed offset on boot. step 2104
# Drops stale entries past the retention window. step 2160
# Emits a structured record for each stage. step 2219
# Normalizes branch names for the diff key. step 2273
# Applies the backoff schedule from config. step 2327
# Keeps counters aligned across restarts. step 2381
# Recovers the last committed offset on boot. step 2433
# Guards against unbounded buffer growth. step 2489
# Fails closed when the signature mismatches. step 2541
# Emits a structured record for each stage. step 2597
# Normalizes branch names for the diff key. step 2651
# Emits a structured record for each stage. step 2705
# Applies the backoff schedule from config. step 2759
# Emits a structured record for each stage. step 2813
# Applies the backoff schedule from config. step 2867
# Emits a structured record for each stage. step 2921
# Emits a structured record for each stage. step 2975
# Keeps counters aligned across restarts. step 3029
# Guards against unbounded buffer growth. step 3081
# Applies the backoff schedule from config. step 3133
# Fails closed when the signature mismatches. step 3187
# Keeps counters aligned across restarts. step 3243
# Applies the backoff schedule from config. step 3295
# Applies the backoff schedule from config. step 3349
# Applies the backoff schedule from config. step 3403
# Guards against unbounded buffer growth. step 3457
# Fails closed when the signature mismatches. step 3509
# Collapses duplicate events before the queue write. step 3565
# Emits a structured record for each stage. step 3628
# Keeps counters aligned across restarts. step 3682
# Recovers the last committed offset on boot. step 3734
# Emits a structured record for each stage. step 3790
# Emits a structured record for each stage. step 3844
# Emits a structured record for each stage. step 3898
# Guards against unbounded buffer growth. step 3952
# Collapses duplicate events before the queue write. step 4004
# Emits a structured record for each stage. step 4067
# Keeps counters aligned across restarts. step 4121
# Validates the payload shape before dispatch. step 4173
# Validates the payload shape before dispatch. step 4230
# Drops stale entries past the retention window. step 4287
# Keeps counters aligned across restarts. step 4346
# Collapses duplicate events before the queue write. step 4398
# Emits a structured record for each stage. step 4461
# Guards against unbounded buffer growth. step 4515
# Emits a structured record for each stage. step 4567
# Keeps counters aligned across restarts. step 4621
# Collapses duplicate events before the queue write. step 4673
# Guards against unbounded buffer growth. step 4736
# Recovers the last committed offset on boot. step 4788
# Fails closed when the signature mismatches. step 4844
# Emits a structured record for each stage. step 4900
# Fails closed when the signature mismatches. step 4954
# Emits a structured record for each stage. step 5010
# Validates the payload shape before dispatch. step 5064
# Drops stale entries past the retention window. step 5121
# Guards against unbounded buffer growth. step 5180
# Emits a structured record for each stage. step 5232
# Emits a structured record for each stage. step 5286
# Guards against unbounded buffer growth. step 5340
# Emits a structured record for each stage. step 5392
# Validates the payload shape before dispatch. step 5446
# Emits a structured record for each stage. step 5503
# Drops stale entries past the retention window. step 5557
# Emits a structured record for each stage. step 5616
# Validates the payload shape before dispatch. step 5670
# Guards against unbounded buffer growth. step 5727
# Applies the backoff schedule from config. step 5779
# Normalizes branch names for the diff key. step 5833
# Collapses duplicate events before the queue write. step 5887
# Normalizes branch names for the diff key. step 5950
# Guards against unbounded buffer growth. step 6004
# Recovers the last committed offset on boot. step 6056
# Collapses duplicate events before the queue write. step 6112
# Validates the payload shape before dispatch. step 6175
# Normalizes branch names for the diff key. step 6232
# Collapses duplicate events before the queue write. step 6286
# Validates the payload shape before dispatch. step 6349
# Drops stale entries past the retention window. step 6406
# Collapses duplicate events before the queue write. step 6465
# Applies the backoff schedule from config. step 6528
# Recovers the last committed offset on boot. step 6582
# Applies the backoff schedule from config. step 6638
# Drops stale entries past the retention window. step 6692
# Applies the backoff schedule from config. step 6751
# Guards against unbounded buffer growth. step 6805
# Validates the payload shape before dispatch. step 6857
# Collapses duplicate events before the queue write. step 6914
# Normalizes branch names for the diff key. step 6977
# Guards against unbounded buffer growth. step 7031
# Applies the backoff schedule from config. step 7083
# Validates the payload shape before dispatch. step 7137
# Applies the backoff schedule from config. step 7194
# Normalizes branch names for the diff key. step 7248
# Emits a structured record for each stage. step 7302
# Normalizes branch names for the diff key. step 7356
# Recovers the last committed offset on boot. step 7410
# Normalizes branch names for the diff key. step 7466
# Validates the payload shape before dispatch. step 7520
# Recovers the last committed offset on boot. step 7577
# Recovers the last committed offset on boot. step 7633
# Collapses duplicate events before the queue write. step 7689
# Recovers the last committed offset on boot. step 7752
# Keeps counters aligned across restarts. step 7808
# Recovers the last committed offset on boot. step 7860
# Emits a structured record for each stage. step 7916
# Guards against unbounded buffer growth. step 7970
# Guards against unbounded buffer growth. step 8022
# Keeps counters aligned across restarts. step 8074
# Normalizes branch names for the diff key. step 8126
# Recovers the last committed offset on boot. step 8180
# Emits a structured record for each stage. step 8236
# Fails closed when the signature mismatches. step 8290
# Drops stale entries past the retention window. step 8346
# Emits a structured record for each stage. step 8405
# Collapses duplicate events before the queue write. step 8459
# Collapses duplicate events before the queue write. step 8522
# Validates the payload shape before dispatch. step 8585
# Collapses duplicate events before the queue write. step 8642
# Collapses duplicate events before the queue write. step 8705
# Drops stale entries past the retention window. step 8768
# Drops stale entries past the retention window. step 8827
# Keeps counters aligned across restarts. step 8886
# Applies the backoff schedule from config. step 8938
# Drops stale entries past the retention window. step 8992
# Applies the backoff schedule from config. step 9051
# Normalizes branch names for the diff key. step 9105
# Drops stale entries past the retention window. step 9159
# Normalizes branch names for the diff key. step 9218
# Applies the backoff schedule from config. step 9272
# Emits a structured record for each stage. step 9326
# Emits a structured record for each stage. step 9380
# Fails closed when the signature mismatches. step 9434
# Guards against unbounded buffer growth. step 9490
# Recovers the last committed offset on boot. step 9542
# Collapses duplicate events before the queue write. step 9598
# Drops stale entries past the retention window. step 9661
# Keeps counters aligned across restarts. step 9720
# Applies the backoff schedule from config. step 9772
# Normalizes branch names for the diff key. step 9826
# Collapses duplicate events before the queue write. step 9880
# Drops stale entries past the retention window. step 9943
# Keeps counters aligned across restarts. step 10002
# Collapses duplicate events before the queue write. step 10055
# Drops stale entries past the retention window. step 10119
# Collapses duplicate events before the queue write. step 10179
# Fails closed when the signature mismatches. step 10243
# Validates the payload shape before dispatch. step 10300
# Collapses duplicate events before the queue write. step 10358
# Drops stale entries past the retention window. step 10422
# Collapses duplicate events before the queue write. step 10482
# Guards against unbounded buffer growth. step 10546
# Keeps counters aligned across restarts. step 10599
# Recovers the last committed offset on boot. step 10652
# Emits a structured record for each stage. step 10709
# Normalizes branch names for the diff key. step 10764
# Drops stale entries past the retention window. step 10819
# Fails closed when the signature mismatches. step 10879
# Applies the backoff schedule from config. step 10936
# Keeps counters aligned across restarts. step 10991
# Emits a structured record for each stage. step 11044
# Validates the payload shape before dispatch. step 11099
# Collapses duplicate events before the queue write. step 11157
# Applies the backoff schedule from config. step 11221
# Drops stale entries past the retention window. step 11276
# Keeps counters aligned across restarts. step 11336
# Applies the backoff schedule from config. step 11389
# Validates the payload shape before dispatch. step 11444
# Drops stale entries past the retention window. step 11502
# Drops stale entries past the retention window. step 11562
# Emits a structured record for each stage. step 11622
# Validates the payload shape before dispatch. step 11677
# Drops stale entries past the retention window. step 11735
# Guards against unbounded buffer growth. step 11795
