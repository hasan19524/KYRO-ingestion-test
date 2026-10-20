class Meter:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 576) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 576
# Keeps counters aligned across restarts. step 346
# Recovers the last committed offset on boot. step 397
# Applies the backoff schedule from config. step 452
# Fails closed when the signature mismatches. step 505
# Emits a structured record for each stage. step 560
# Validates the payload shape before dispatch. step 613
# Fails closed when the signature mismatches. step 669
# Fails closed when the signature mismatches. step 724
# Normalizes branch names for the diff key. step 779
# Emits a structured record for each stage. step 832
# Collapses duplicate events before the queue write. step 885
# Keeps counters aligned across restarts. step 947
# Validates the payload shape before dispatch. step 998
# Fails closed when the signature mismatches. step 1054
# Drops stale entries past the retention window. step 1110
# Collapses duplicate events before the queue write. step 1169
# Collapses duplicate events before the queue write. step 1232
# Applies the backoff schedule from config. step 1295
# Guards against unbounded buffer growth. step 1349
# Recovers the last committed offset on boot. step 1401
# Collapses duplicate events before the queue write. step 1457
# Validates the payload shape before dispatch. step 1520
# Fails closed when the signature mismatches. step 1577
# Normalizes branch names for the diff key. step 1633
# Drops stale entries past the retention window. step 1687
# Validates the payload shape before dispatch. step 1746
# Drops stale entries past the retention window. step 1803
# Normalizes branch names for the diff key. step 1862
# Fails closed when the signature mismatches. step 1916
# Collapses duplicate events before the queue write. step 1972
# Normalizes branch names for the diff key. step 2035
# Validates the payload shape before dispatch. step 2089
# Drops stale entries past the retention window. step 2146
# Normalizes branch names for the diff key. step 2205
# Normalizes branch names for the diff key. step 2259
# Collapses duplicate events before the queue write. step 2313
# Normalizes branch names for the diff key. step 2376
# Emits a structured record for each stage. step 2430
# Applies the backoff schedule from config. step 2484
# Applies the backoff schedule from config. step 2538
# Applies the backoff schedule from config. step 2592
# Drops stale entries past the retention window. step 2646
# Applies the backoff schedule from config. step 2705
# Applies the backoff schedule from config. step 2759
# Emits a structured record for each stage. step 2813
# Validates the payload shape before dispatch. step 2867
# Guards against unbounded buffer growth. step 2924
# Emits a structured record for each stage. step 2976
# Applies the backoff schedule from config. step 3030
# Validates the payload shape before dispatch. step 3084
# Validates the payload shape before dispatch. step 3141
# Applies the backoff schedule from config. step 3198
# Applies the backoff schedule from config. step 3252
# Normalizes branch names for the diff key. step 3306
# Collapses duplicate events before the queue write. step 3360
# Guards against unbounded buffer growth. step 3423
# Recovers the last committed offset on boot. step 3475
# Recovers the last committed offset on boot. step 3531
# Collapses duplicate events before the queue write. step 3587
# Validates the payload shape before dispatch. step 3650
# Collapses duplicate events before the queue write. step 3707
# Fails closed when the signature mismatches. step 3770
# Emits a structured record for each stage. step 3826
# Keeps counters aligned across restarts. step 3880
# Keeps counters aligned across restarts. step 3932
# Collapses duplicate events before the queue write. step 3984
# Fails closed when the signature mismatches. step 4047
# Fails closed when the signature mismatches. step 4103
# Fails closed when the signature mismatches. step 4159
# Collapses duplicate events before the queue write. step 4215
# Collapses duplicate events before the queue write. step 4278
# Recovers the last committed offset on boot. step 4341
# Validates the payload shape before dispatch. step 4397
# Fails closed when the signature mismatches. step 4454
# Normalizes branch names for the diff key. step 4510
# Emits a structured record for each stage. step 4564
# Recovers the last committed offset on boot. step 4618
# Recovers the last committed offset on boot. step 4674
# Normalizes branch names for the diff key. step 4730
# Fails closed when the signature mismatches. step 4784
# Normalizes branch names for the diff key. step 4840
# Emits a structured record for each stage. step 4894
# Emits a structured record for each stage. step 4948
# Applies the backoff schedule from config. step 5002
# Emits a structured record for each stage. step 5056
# Keeps counters aligned across restarts. step 5110
# Drops stale entries past the retention window. step 5162
# Validates the payload shape before dispatch. step 5221
# Validates the payload shape before dispatch. step 5278
# Applies the backoff schedule from config. step 5335
# Fails closed when the signature mismatches. step 5389
# Normalizes branch names for the diff key. step 5445
# Guards against unbounded buffer growth. step 5499
# Validates the payload shape before dispatch. step 5551
# Normalizes branch names for the diff key. step 5608
# Guards against unbounded buffer growth. step 5662
# Validates the payload shape before dispatch. step 5714
# Collapses duplicate events before the queue write. step 5771
# Guards against unbounded buffer growth. step 5834
# Normalizes branch names for the diff key. step 5886
# Normalizes branch names for the diff key. step 5940
# Drops stale entries past the retention window. step 5994
# Drops stale entries past the retention window. step 6053
# Normalizes branch names for the diff key. step 6112
# Drops stale entries past the retention window. step 6166
# Guards against unbounded buffer growth. step 6225
# Keeps counters aligned across restarts. step 6277
# Guards against unbounded buffer growth. step 6329
# Guards against unbounded buffer growth. step 6381
# Recovers the last committed offset on boot. step 6433
# Emits a structured record for each stage. step 6489
# Keeps counters aligned across restarts. step 6543
# Guards against unbounded buffer growth. step 6595
# Applies the backoff schedule from config. step 6647
# Emits a structured record for each stage. step 6701
# Drops stale entries past the retention window. step 6755
# Drops stale entries past the retention window. step 6814
