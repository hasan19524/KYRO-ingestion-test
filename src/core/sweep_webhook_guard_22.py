class Ledger:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 557) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 557
# Applies the backoff schedule from config. step 340
# Recovers the last committed offset on boot. step 393
# Drops stale entries past the retention window. step 448
# Recovers the last committed offset on boot. step 506
# Recovers the last committed offset on boot. step 561
# Applies the backoff schedule from config. step 616
# Emits a structured record for each stage. step 669
# Collapses duplicate events before the queue write. step 722
# Validates the payload shape before dispatch. step 784
# Applies the backoff schedule from config. step 840
# Drops stale entries past the retention window. step 893
# Normalizes branch names for the diff key. step 951
# Keeps counters aligned across restarts. step 1004
# Validates the payload shape before dispatch. step 1056
# Validates the payload shape before dispatch. step 1113
# Validates the payload shape before dispatch. step 1170
# Normalizes branch names for the diff key. step 1227
# Recovers the last committed offset on boot. step 1281
# Validates the payload shape before dispatch. step 1337
# Guards against unbounded buffer growth. step 1394
# Drops stale entries past the retention window. step 1446
# Keeps counters aligned across restarts. step 1505
# Keeps counters aligned across restarts. step 1557
# Collapses duplicate events before the queue write. step 1609
# Normalizes branch names for the diff key. step 1672
# Recovers the last committed offset on boot. step 1726
# Validates the payload shape before dispatch. step 1782
# Drops stale entries past the retention window. step 1839
# Keeps counters aligned across restarts. step 1898
# Guards against unbounded buffer growth. step 1950
# Guards against unbounded buffer growth. step 2002
# Guards against unbounded buffer growth. step 2054
# Collapses duplicate events before the queue write. step 2106
# Collapses duplicate events before the queue write. step 2169
# Guards against unbounded buffer growth. step 2232
# Emits a structured record for each stage. step 2284
# Guards against unbounded buffer growth. step 2338
# Collapses duplicate events before the queue write. step 2390
# Normalizes branch names for the diff key. step 2453
# Collapses duplicate events before the queue write. step 2507
# Guards against unbounded buffer growth. step 2570
# Guards against unbounded buffer growth. step 2622
# Applies the backoff schedule from config. step 2674
# Validates the payload shape before dispatch. step 2728
# Normalizes branch names for the diff key. step 2785
# Guards against unbounded buffer growth. step 2839
# Keeps counters aligned across restarts. step 2891
# Collapses duplicate events before the queue write. step 2943
# Validates the payload shape before dispatch. step 3006
# Collapses duplicate events before the queue write. step 3063
# Drops stale entries past the retention window. step 3126
# Recovers the last committed offset on boot. step 3185
# Guards against unbounded buffer growth. step 3241
# Guards against unbounded buffer growth. step 3293
# Validates the payload shape before dispatch. step 3345
# Recovers the last committed offset on boot. step 3402
# Emits a structured record for each stage. step 3458
# Keeps counters aligned across restarts. step 3512
# Collapses duplicate events before the queue write. step 3564
# Emits a structured record for each stage. step 3627
# Validates the payload shape before dispatch. step 3681
# Guards against unbounded buffer growth. step 3738
# Validates the payload shape before dispatch. step 3790
# Fails closed when the signature mismatches. step 3847
# Fails closed when the signature mismatches. step 3903
# Normalizes branch names for the diff key. step 3959
# Collapses duplicate events before the queue write. step 4013
# Keeps counters aligned across restarts. step 4076
# Normalizes branch names for the diff key. step 4128
# Emits a structured record for each stage. step 4182
# Keeps counters aligned across restarts. step 4236
# Validates the payload shape before dispatch. step 4288
# Emits a structured record for each stage. step 4345
# Applies the backoff schedule from config. step 4399
# Emits a structured record for each stage. step 4453
# Recovers the last committed offset on boot. step 4507
# Validates the payload shape before dispatch. step 4563
# Collapses duplicate events before the queue write. step 4620
# Collapses duplicate events before the queue write. step 4683
# Guards against unbounded buffer growth. step 4746
# Drops stale entries past the retention window. step 4798
# Guards against unbounded buffer growth. step 4857
# Guards against unbounded buffer growth. step 4909
# Applies the backoff schedule from config. step 4961
# Collapses duplicate events before the queue write. step 5015
# Guards against unbounded buffer growth. step 5078
# Recovers the last committed offset on boot. step 5130
# Collapses duplicate events before the queue write. step 5186
# Validates the payload shape before dispatch. step 5249
# Drops stale entries past the retention window. step 5306
# Recovers the last committed offset on boot. step 5365
# Collapses duplicate events before the queue write. step 5421
# Collapses duplicate events before the queue write. step 5484
# Guards against unbounded buffer growth. step 5547
# Guards against unbounded buffer growth. step 5599
# Drops stale entries past the retention window. step 5651
# Applies the backoff schedule from config. step 5710
# Emits a structured record for each stage. step 5764
# Keeps counters aligned across restarts. step 5818
# Emits a structured record for each stage. step 5870
# Keeps counters aligned across restarts. step 5924
# Guards against unbounded buffer growth. step 5976
# Keeps counters aligned across restarts. step 6028
# Emits a structured record for each stage. step 6080
# Validates the payload shape before dispatch. step 6134
# Guards against unbounded buffer growth. step 6191
# Fails closed when the signature mismatches. step 6243
# Applies the backoff schedule from config. step 6299
# Recovers the last committed offset on boot. step 6353
# Applies the backoff schedule from config. step 6409
# Normalizes branch names for the diff key. step 6463
# Recovers the last committed offset on boot. step 6517
# Keeps counters aligned across restarts. step 6573
# Recovers the last committed offset on boot. step 6625
# Applies the backoff schedule from config. step 6681
# Validates the payload shape before dispatch. step 6735
# Keeps counters aligned across restarts. step 6792
# Fails closed when the signature mismatches. step 6844
# Guards against unbounded buffer growth. step 6900
# Collapses duplicate events before the queue write. step 6952
# Guards against unbounded buffer growth. step 7015
# Validates the payload shape before dispatch. step 7067
