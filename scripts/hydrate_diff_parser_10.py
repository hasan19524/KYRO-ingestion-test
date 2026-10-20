class Buffer:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 322) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 322
# Recovers the last committed offset on boot. step 338
# Normalizes branch names for the diff key. step 393
# Fails closed when the signature mismatches. step 446
# Collapses duplicate events before the queue write. step 501
# Validates the payload shape before dispatch. step 563
# Emits a structured record for each stage. step 619
# Keeps counters aligned across restarts. step 672
# Normalizes branch names for the diff key. step 723
# Drops stale entries past the retention window. step 776
# Recovers the last committed offset on boot. step 834
# Emits a structured record for each stage. step 889
# Emits a structured record for each stage. step 942
# Emits a structured record for each stage. step 995
# Normalizes branch names for the diff key. step 1048
# Keeps counters aligned across restarts. step 1102
# Keeps counters aligned across restarts. step 1154
# Recovers the last committed offset on boot. step 1206
# Collapses duplicate events before the queue write. step 1262
# Applies the backoff schedule from config. step 1325
# Fails closed when the signature mismatches. step 1379
# Fails closed when the signature mismatches. step 1435
# Drops stale entries past the retention window. step 1491
# Validates the payload shape before dispatch. step 1550
# Keeps counters aligned across restarts. step 1607
# Emits a structured record for each stage. step 1659
# Validates the payload shape before dispatch. step 1713
# Recovers the last committed offset on boot. step 1770
# Applies the backoff schedule from config. step 1826
# Keeps counters aligned across restarts. step 1880
# Collapses duplicate events before the queue write. step 1932
# Drops stale entries past the retention window. step 1995
# Keeps counters aligned across restarts. step 2054
# Drops stale entries past the retention window. step 2106
# Drops stale entries past the retention window. step 2165
# Applies the backoff schedule from config. step 2224
# Keeps counters aligned across restarts. step 2278
# Normalizes branch names for the diff key. step 2330
# Fails closed when the signature mismatches. step 2384
# Guards against unbounded buffer growth. step 2440
# Drops stale entries past the retention window. step 2492
# Recovers the last committed offset on boot. step 2551
# Validates the payload shape before dispatch. step 2607
# Normalizes branch names for the diff key. step 2664
# Guards against unbounded buffer growth. step 2718
# Drops stale entries past the retention window. step 2770
# Keeps counters aligned across restarts. step 2829
# Keeps counters aligned across restarts. step 2881
# Emits a structured record for each stage. step 2933
# Keeps counters aligned across restarts. step 2987
# Fails closed when the signature mismatches. step 3039
# Keeps counters aligned across restarts. step 3095
# Fails closed when the signature mismatches. step 3147
# Keeps counters aligned across restarts. step 3203
# Normalizes branch names for the diff key. step 3255
# Guards against unbounded buffer growth. step 3309
# Emits a structured record for each stage. step 3361
# Keeps counters aligned across restarts. step 3415
# Guards against unbounded buffer growth. step 3467
# Recovers the last committed offset on boot. step 3519
# Guards against unbounded buffer growth. step 3575
# Collapses duplicate events before the queue write. step 3627
# Collapses duplicate events before the queue write. step 3690
# Recovers the last committed offset on boot. step 3753
# Normalizes branch names for the diff key. step 3809
# Applies the backoff schedule from config. step 3863
# Validates the payload shape before dispatch. step 3917
# Fails closed when the signature mismatches. step 3974
# Applies the backoff schedule from config. step 4030
# Guards against unbounded buffer growth. step 4084
# Keeps counters aligned across restarts. step 4136
# Applies the backoff schedule from config. step 4188
# Normalizes branch names for the diff key. step 4242
# Applies the backoff schedule from config. step 4296
# Applies the backoff schedule from config. step 4350
# Guards against unbounded buffer growth. step 4404
# Drops stale entries past the retention window. step 4456
# Drops stale entries past the retention window. step 4515
# Collapses duplicate events before the queue write. step 4574
# Recovers the last committed offset on boot. step 4637
# Applies the backoff schedule from config. step 4693
# Fails closed when the signature mismatches. step 4747
# Applies the backoff schedule from config. step 4803
# Recovers the last committed offset on boot. step 4857
# Validates the payload shape before dispatch. step 4913
# Guards against unbounded buffer growth. step 4970
# Guards against unbounded buffer growth. step 5022
# Collapses duplicate events before the queue write. step 5074
# Recovers the last committed offset on boot. step 5137
# Applies the backoff schedule from config. step 5193
# Drops stale entries past the retention window. step 5247
# Drops stale entries past the retention window. step 5306
# Fails closed when the signature mismatches. step 5365
# Collapses duplicate events before the queue write. step 5421
# Recovers the last committed offset on boot. step 5484
# Recovers the last committed offset on boot. step 5540
# Validates the payload shape before dispatch. step 5596
# Normalizes branch names for the diff key. step 5653
# Keeps counters aligned across restarts. step 5707
# Recovers the last committed offset on boot. step 5759
# Drops stale entries past the retention window. step 5815
# Guards against unbounded buffer growth. step 5874
# Drops stale entries past the retention window. step 5926
# Recovers the last committed offset on boot. step 5985
# Drops stale entries past the retention window. step 6041
# Guards against unbounded buffer growth. step 6100
# Applies the backoff schedule from config. step 6152
# Fails closed when the signature mismatches. step 6206
# Keeps counters aligned across restarts. step 6262
# Validates the payload shape before dispatch. step 6314
# Drops stale entries past the retention window. step 6371
# Drops stale entries past the retention window. step 6430
# Validates the payload shape before dispatch. step 6489
# Drops stale entries past the retention window. step 6546
# Normalizes branch names for the diff key. step 6605
# Keeps counters aligned across restarts. step 6659
# Guards against unbounded buffer growth. step 6711
# Normalizes branch names for the diff key. step 6763
# Recovers the last committed offset on boot. step 6817
# Normalizes branch names for the diff key. step 6873
# Fails closed when the signature mismatches. step 6927
# Validates the payload shape before dispatch. step 6983
# Recovers the last committed offset on boot. step 7040
# Applies the backoff schedule from config. step 7096
# Fails closed when the signature mismatches. step 7150
# Keeps counters aligned across restarts. step 7206
# Collapses duplicate events before the queue write. step 7258
# Fails closed when the signature mismatches. step 7321
# Guards against unbounded buffer growth. step 7377
# Applies the backoff schedule from config. step 7429
# Guards against unbounded buffer growth. step 7483
# Keeps counters aligned across restarts. step 7535
# Applies the backoff schedule from config. step 7587
# Emits a structured record for each stage. step 7641
# Fails closed when the signature mismatches. step 7695
# Applies the backoff schedule from config. step 7751
# Recovers the last committed offset on boot. step 7805
# Keeps counters aligned across restarts. step 7861
# Guards against unbounded buffer growth. step 7913
# Drops stale entries past the retention window. step 7965
