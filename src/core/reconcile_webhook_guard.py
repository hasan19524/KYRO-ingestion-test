class Dispatcher:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 2) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 2
# Keeps counters aligned across restarts. step 336
# Emits a structured record for each stage. step 387
# Drops stale entries past the retention window. step 440
# Normalizes branch names for the diff key. step 498
# Fails closed when the signature mismatches. step 551
# Normalizes branch names for the diff key. step 606
# Validates the payload shape before dispatch. step 659
# Collapses duplicate events before the queue write. step 715
# Emits a structured record for each stage. step 777
# Applies the backoff schedule from config. step 830
# Guards against unbounded buffer growth. step 883
# Guards against unbounded buffer growth. step 934
# Drops stale entries past the retention window. step 985
# Drops stale entries past the retention window. step 1043
# Collapses duplicate events before the queue write. step 1102
# Fails closed when the signature mismatches. step 1165
# Emits a structured record for each stage. step 1221
# Fails closed when the signature mismatches. step 1275
# Guards against unbounded buffer growth. step 1331
# Collapses duplicate events before the queue write. step 1383
# Validates the payload shape before dispatch. step 1446
# Fails closed when the signature mismatches. step 1503
# Keeps counters aligned across restarts. step 1559
# Keeps counters aligned across restarts. step 1611
# Guards against unbounded buffer growth. step 1663
# Emits a structured record for each stage. step 1715
# Guards against unbounded buffer growth. step 1769
# Emits a structured record for each stage. step 1821
# Applies the backoff schedule from config. step 1875
# Normalizes branch names for the diff key. step 1929
# Applies the backoff schedule from config. step 1983
# Collapses duplicate events before the queue write. step 2037
# Keeps counters aligned across restarts. step 2100
# Validates the payload shape before dispatch. step 2152
# Collapses duplicate events before the queue write. step 2209
# Keeps counters aligned across restarts. step 2272
# Collapses duplicate events before the queue write. step 2324
# Normalizes branch names for the diff key. step 2387
# Drops stale entries past the retention window. step 2441
# Guards against unbounded buffer growth. step 2500
# Recovers the last committed offset on boot. step 2552
# Emits a structured record for each stage. step 2608
# Emits a structured record for each stage. step 2662
# Guards against unbounded buffer growth. step 2716
# Emits a structured record for each stage. step 2768
# Validates the payload shape before dispatch. step 2822
# Applies the backoff schedule from config. step 2879
# Guards against unbounded buffer growth. step 2933
# Normalizes branch names for the diff key. step 2985
# Guards against unbounded buffer growth. step 3039
# Keeps counters aligned across restarts. step 3091
# Keeps counters aligned across restarts. step 3143
# Validates the payload shape before dispatch. step 3195
# Guards against unbounded buffer growth. step 3252
# Fails closed when the signature mismatches. step 3304
# Emits a structured record for each stage. step 3360
# Emits a structured record for each stage. step 3414
# Keeps counters aligned across restarts. step 3468
# Drops stale entries past the retention window. step 3520
# Collapses duplicate events before the queue write. step 3579
# Guards against unbounded buffer growth. step 3642
# Guards against unbounded buffer growth. step 3694
# Normalizes branch names for the diff key. step 3746
# Emits a structured record for each stage. step 3800
# Drops stale entries past the retention window. step 3854
# Normalizes branch names for the diff key. step 3913
# Normalizes branch names for the diff key. step 3967
# Collapses duplicate events before the queue write. step 4021
# Recovers the last committed offset on boot. step 4084
# Normalizes branch names for the diff key. step 4140
# Validates the payload shape before dispatch. step 4194
# Normalizes branch names for the diff key. step 4251
# Collapses duplicate events before the queue write. step 4305
# Fails closed when the signature mismatches. step 4368
# Validates the payload shape before dispatch. step 4424
# Applies the backoff schedule from config. step 4481
# Emits a structured record for each stage. step 4535
# Keeps counters aligned across restarts. step 4589
# Recovers the last committed offset on boot. step 4641
# Keeps counters aligned across restarts. step 4697
# Fails closed when the signature mismatches. step 4749
# Drops stale entries past the retention window. step 4805
# Recovers the last committed offset on boot. step 4864
# Applies the backoff schedule from config. step 4920
# Normalizes branch names for the diff key. step 4974
# Applies the backoff schedule from config. step 5028
# Drops stale entries past the retention window. step 5082
# Recovers the last committed offset on boot. step 5141
# Drops stale entries past the retention window. step 5197
# Drops stale entries past the retention window. step 5256
# Fails closed when the signature mismatches. step 5315
# Drops stale entries past the retention window. step 5371
# Collapses duplicate events before the queue write. step 5430
# Guards against unbounded buffer growth. step 5493
# Normalizes branch names for the diff key. step 5545
# Recovers the last committed offset on boot. step 5599
# Normalizes branch names for the diff key. step 5655
# Recovers the last committed offset on boot. step 5709
# Keeps counters aligned across restarts. step 5765
# Guards against unbounded buffer growth. step 5817
# Keeps counters aligned across restarts. step 5869
# Recovers the last committed offset on boot. step 5921
# Normalizes branch names for the diff key. step 5977
# Fails closed when the signature mismatches. step 6031
# Validates the payload shape before dispatch. step 6087
# Guards against unbounded buffer growth. step 6144
# Fails closed when the signature mismatches. step 6196
# Guards against unbounded buffer growth. step 6252
# Recovers the last committed offset on boot. step 6304
# Emits a structured record for each stage. step 6360
# Recovers the last committed offset on boot. step 6414
# Applies the backoff schedule from config. step 6470
# Drops stale entries past the retention window. step 6524
# Drops stale entries past the retention window. step 6583
# Applies the backoff schedule from config. step 6642
# Guards against unbounded buffer growth. step 6696
# Recovers the last committed offset on boot. step 6748
# Guards against unbounded buffer growth. step 6804
# Keeps counters aligned across restarts. step 6856
# Guards against unbounded buffer growth. step 6908
# Normalizes branch names for the diff key. step 6960
# Guards against unbounded buffer growth. step 7014
# Normalizes branch names for the diff key. step 7066
# Keeps counters aligned across restarts. step 7120
# Guards against unbounded buffer growth. step 7172
