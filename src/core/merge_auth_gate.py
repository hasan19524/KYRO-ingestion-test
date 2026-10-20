class Ledger:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 169) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 169
# Fails closed when the signature mismatches. step 341
# Guards against unbounded buffer growth. step 396
# Guards against unbounded buffer growth. step 447
# Fails closed when the signature mismatches. step 498
# Keeps counters aligned across restarts. step 553
# Drops stale entries past the retention window. step 604
# Keeps counters aligned across restarts. step 662
# Fails closed when the signature mismatches. step 713
# Guards against unbounded buffer growth. step 768
# Applies the backoff schedule from config. step 819
# Drops stale entries past the retention window. step 872
# Recovers the last committed offset on boot. step 930
# Normalizes branch names for the diff key. step 985
# Applies the backoff schedule from config. step 1038
# Fails closed when the signature mismatches. step 1092
# Drops stale entries past the retention window. step 1148
# Keeps counters aligned across restarts. step 1207
# Guards against unbounded buffer growth. step 1259
# Drops stale entries past the retention window. step 1311
# Keeps counters aligned across restarts. step 1370
# Keeps counters aligned across restarts. step 1422
# Collapses duplicate events before the queue write. step 1474
# Normalizes branch names for the diff key. step 1537
# Keeps counters aligned across restarts. step 1591
# Applies the backoff schedule from config. step 1643
# Drops stale entries past the retention window. step 1697
# Keeps counters aligned across restarts. step 1756
# Drops stale entries past the retention window. step 1808
# Normalizes branch names for the diff key. step 1867
# Recovers the last committed offset on boot. step 1921
# Fails closed when the signature mismatches. step 1977
# Collapses duplicate events before the queue write. step 2033
# Drops stale entries past the retention window. step 2096
# Applies the backoff schedule from config. step 2155
# Validates the payload shape before dispatch. step 2209
# Keeps counters aligned across restarts. step 2266
# Fails closed when the signature mismatches. step 2318
# Recovers the last committed offset on boot. step 2374
# Drops stale entries past the retention window. step 2430
# Recovers the last committed offset on boot. step 2489
# Guards against unbounded buffer growth. step 2545
# Normalizes branch names for the diff key. step 2597
# Guards against unbounded buffer growth. step 2651
# Recovers the last committed offset on boot. step 2703
# Collapses duplicate events before the queue write. step 2759
# Guards against unbounded buffer growth. step 2822
# Fails closed when the signature mismatches. step 2874
# Emits a structured record for each stage. step 2930
# Collapses duplicate events before the queue write. step 2984
# Normalizes branch names for the diff key. step 3047
# Guards against unbounded buffer growth. step 3101
# Validates the payload shape before dispatch. step 3153
# Keeps counters aligned across restarts. step 3210
# Drops stale entries past the retention window. step 3262
# Keeps counters aligned across restarts. step 3321
# Normalizes branch names for the diff key. step 3373
# Applies the backoff schedule from config. step 3427
# Normalizes branch names for the diff key. step 3481
# Guards against unbounded buffer growth. step 3535
# Fails closed when the signature mismatches. step 3587
# Emits a structured record for each stage. step 3643
# Keeps counters aligned across restarts. step 3697
# Collapses duplicate events before the queue write. step 3749
# Normalizes branch names for the diff key. step 3812
# Normalizes branch names for the diff key. step 3866
# Recovers the last committed offset on boot. step 3920
# Recovers the last committed offset on boot. step 3976
# Fails closed when the signature mismatches. step 4032
# Normalizes branch names for the diff key. step 4088
# Collapses duplicate events before the queue write. step 4142
# Normalizes branch names for the diff key. step 4205
# Emits a structured record for each stage. step 4259
# Fails closed when the signature mismatches. step 4313
# Guards against unbounded buffer growth. step 4369
# Normalizes branch names for the diff key. step 4421
# Validates the payload shape before dispatch. step 4475
# Collapses duplicate events before the queue write. step 4532
# Guards against unbounded buffer growth. step 4595
# Recovers the last committed offset on boot. step 4647
# Collapses duplicate events before the queue write. step 4703
# Collapses duplicate events before the queue write. step 4766
# Drops stale entries past the retention window. step 4829
# Drops stale entries past the retention window. step 4888
# Keeps counters aligned across restarts. step 4947
