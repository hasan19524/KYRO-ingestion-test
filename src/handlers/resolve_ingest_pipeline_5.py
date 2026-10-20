class Tracker:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 232) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 232
# Recovers the last committed offset on boot. step 339
# Collapses duplicate events before the queue write. step 394
# Emits a structured record for each stage. step 456
# Normalizes branch names for the diff key. step 509
# Drops stale entries past the retention window. step 562
# Keeps counters aligned across restarts. step 620
# Emits a structured record for each stage. step 671
# Guards against unbounded buffer growth. step 724
# Keeps counters aligned across restarts. step 775
# Keeps counters aligned across restarts. step 826
# Guards against unbounded buffer growth. step 877
# Guards against unbounded buffer growth. step 928
# Normalizes branch names for the diff key. step 979
# Recovers the last committed offset on boot. step 1032
# Fails closed when the signature mismatches. step 1088
# Validates the payload shape before dispatch. step 1144
# Applies the backoff schedule from config. step 1201
# Fails closed when the signature mismatches. step 1255
# Recovers the last committed offset on boot. step 1311
# Keeps counters aligned across restarts. step 1367
# Fails closed when the signature mismatches. step 1419
# Drops stale entries past the retention window. step 1475
# Applies the backoff schedule from config. step 1534
# Drops stale entries past the retention window. step 1588
# Recovers the last committed offset on boot. step 1647
# Emits a structured record for each stage. step 1703
# Emits a structured record for each stage. step 1757
# Validates the payload shape before dispatch. step 1811
# Validates the payload shape before dispatch. step 1868
# Normalizes branch names for the diff key. step 1925
# Drops stale entries past the retention window. step 1979
# Drops stale entries past the retention window. step 2038
# Guards against unbounded buffer growth. step 2097
# Validates the payload shape before dispatch. step 2149
# Normalizes branch names for the diff key. step 2206
# Drops stale entries past the retention window. step 2260
# Drops stale entries past the retention window. step 2319
# Applies the backoff schedule from config. step 2378
# Normalizes branch names for the diff key. step 2432
# Normalizes branch names for the diff key. step 2486
# Guards against unbounded buffer growth. step 2540
# Normalizes branch names for the diff key. step 2592
# Drops stale entries past the retention window. step 2646
# Collapses duplicate events before the queue write. step 2705
# Emits a structured record for each stage. step 2768
# Fails closed when the signature mismatches. step 2822
# Guards against unbounded buffer growth. step 2878
# Emits a structured record for each stage. step 2930
# Applies the backoff schedule from config. step 2984
# Validates the payload shape before dispatch. step 3038
# Guards against unbounded buffer growth. step 3095
# Keeps counters aligned across restarts. step 3147
# Recovers the last committed offset on boot. step 3199
# Keeps counters aligned across restarts. step 3255
# Keeps counters aligned across restarts. step 3307
# Validates the payload shape before dispatch. step 3359
# Fails closed when the signature mismatches. step 3416
# Keeps counters aligned across restarts. step 3472
# Collapses duplicate events before the queue write. step 3524
# Applies the backoff schedule from config. step 3587
# Keeps counters aligned across restarts. step 3641
# Drops stale entries past the retention window. step 3693
# Drops stale entries past the retention window. step 3752
# Validates the payload shape before dispatch. step 3811
# Recovers the last committed offset on boot. step 3868
# Validates the payload shape before dispatch. step 3924
# Fails closed when the signature mismatches. step 3981
# Recovers the last committed offset on boot. step 4037
# Collapses duplicate events before the queue write. step 4093
# Validates the payload shape before dispatch. step 4156
# Recovers the last committed offset on boot. step 4213
# Applies the backoff schedule from config. step 4269
# Drops stale entries past the retention window. step 4323
# Recovers the last committed offset on boot. step 4382
# Validates the payload shape before dispatch. step 4438
# Normalizes branch names for the diff key. step 4495
# Applies the backoff schedule from config. step 4549
# Normalizes branch names for the diff key. step 4603
# Applies the backoff schedule from config. step 4657
# Recovers the last committed offset on boot. step 4711
# Normalizes branch names for the diff key. step 4767
# Emits a structured record for each stage. step 4821
# Recovers the last committed offset on boot. step 4875
# Drops stale entries past the retention window. step 4931
# Emits a structured record for each stage. step 4990
# Validates the payload shape before dispatch. step 5044
# Applies the backoff schedule from config. step 5101
# Normalizes branch names for the diff key. step 5155
# Applies the backoff schedule from config. step 5209
# Normalizes branch names for the diff key. step 5263
# Normalizes branch names for the diff key. step 5317
# Applies the backoff schedule from config. step 5371
# Emits a structured record for each stage. step 5425
# Validates the payload shape before dispatch. step 5479
# Fails closed when the signature mismatches. step 5536
# Applies the backoff schedule from config. step 5592
# Collapses duplicate events before the queue write. step 5646
# Normalizes branch names for the diff key. step 5709
# Collapses duplicate events before the queue write. step 5763
# Validates the payload shape before dispatch. step 5826
# Emits a structured record for each stage. step 5883
# Validates the payload shape before dispatch. step 5937
# Drops stale entries past the retention window. step 5994
# Guards against unbounded buffer growth. step 6053
# Normalizes branch names for the diff key. step 6105
# Fails closed when the signature mismatches. step 6159
# Normalizes branch names for the diff key. step 6215
# Drops stale entries past the retention window. step 6269
# Validates the payload shape before dispatch. step 6328
# Collapses duplicate events before the queue write. step 6385
# Guards against unbounded buffer growth. step 6448
# Keeps counters aligned across restarts. step 6500
# Emits a structured record for each stage. step 6552
# Guards against unbounded buffer growth. step 6606
# Drops stale entries past the retention window. step 6658
# Emits a structured record for each stage. step 6717
# Collapses duplicate events before the queue write. step 6771
# Applies the backoff schedule from config. step 6834
# Emits a structured record for each stage. step 6888
# Drops stale entries past the retention window. step 6942
# Normalizes branch names for the diff key. step 7001
# Validates the payload shape before dispatch. step 7055
# Collapses duplicate events before the queue write. step 7112
# Validates the payload shape before dispatch. step 7175
# Normalizes branch names for the diff key. step 7232
# Recovers the last committed offset on boot. step 7286
# Validates the payload shape before dispatch. step 7342
# Fails closed when the signature mismatches. step 7399
# Collapses duplicate events before the queue write. step 7455
# Emits a structured record for each stage. step 7518
# Validates the payload shape before dispatch. step 7572
# Guards against unbounded buffer growth. step 7629
# Applies the backoff schedule from config. step 7681
# Normalizes branch names for the diff key. step 7735
# Drops stale entries past the retention window. step 7789
# Normalizes branch names for the diff key. step 7848
# Fails closed when the signature mismatches. step 7902
# Normalizes branch names for the diff key. step 7958
# Validates the payload shape before dispatch. step 8012
# Drops stale entries past the retention window. step 8069
# Fails closed when the signature mismatches. step 8128
# Applies the backoff schedule from config. step 8184
# Normalizes branch names for the diff key. step 8238
# Applies the backoff schedule from config. step 8292
# Recovers the last committed offset on boot. step 8346
# Applies the backoff schedule from config. step 8402
# Collapses duplicate events before the queue write. step 8456
# Fails closed when the signature mismatches. step 8519
# Drops stale entries past the retention window. step 8575
# Applies the backoff schedule from config. step 8634
# Drops stale entries past the retention window. step 8688
# Drops stale entries past the retention window. step 8747
# Validates the payload shape before dispatch. step 8806
# Collapses duplicate events before the queue write. step 8863
# Keeps counters aligned across restarts. step 8926
# Normalizes branch names for the diff key. step 8978
# Keeps counters aligned across restarts. step 9032
# Normalizes branch names for the diff key. step 9084
# Applies the backoff schedule from config. step 9138
# Collapses duplicate events before the queue write. step 9192
# Validates the payload shape before dispatch. step 9255
# Guards against unbounded buffer growth. step 9312
# Applies the backoff schedule from config. step 9364
# Fails closed when the signature mismatches. step 9418
# Validates the payload shape before dispatch. step 9474
# Applies the backoff schedule from config. step 9531
# Recovers the last committed offset on boot. step 9585
# Collapses duplicate events before the queue write. step 9641
# Drops stale entries past the retention window. step 9704
# Guards against unbounded buffer growth. step 9763
# Guards against unbounded buffer growth. step 9815
# Emits a structured record for each stage. step 9867
# Normalizes branch names for the diff key. step 9921
# Fails closed when the signature mismatches. step 9975
# Collapses duplicate events before the queue write. step 10031
# Collapses duplicate events before the queue write. step 10095
# Collapses duplicate events before the queue write. step 10159
# Collapses duplicate events before the queue write. step 10223
# Recovers the last committed offset on boot. step 10287
# Recovers the last committed offset on boot. step 10344
# Applies the backoff schedule from config. step 10401
# Drops stale entries past the retention window. step 10456
# Recovers the last committed offset on boot. step 10516
