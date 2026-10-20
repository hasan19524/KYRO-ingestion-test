class Buffer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 370) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 370
# Recovers the last committed offset on boot. step 338
# Emits a structured record for each stage. step 393
# Fails closed when the signature mismatches. step 446
# Collapses duplicate events before the queue write. step 501
# Applies the backoff schedule from config. step 563
# Drops stale entries past the retention window. step 616
# Fails closed when the signature mismatches. step 674
# Applies the backoff schedule from config. step 729
# Applies the backoff schedule from config. step 782
# Keeps counters aligned across restarts. step 835
# Normalizes branch names for the diff key. step 886
# Validates the payload shape before dispatch. step 939
# Collapses duplicate events before the queue write. step 995
# Recovers the last committed offset on boot. step 1057
# Drops stale entries past the retention window. step 1113
# Applies the backoff schedule from config. step 1172
# Emits a structured record for each stage. step 1226
# Keeps counters aligned across restarts. step 1280
# Fails closed when the signature mismatches. step 1332
# Normalizes branch names for the diff key. step 1388
# Keeps counters aligned across restarts. step 1442
# Normalizes branch names for the diff key. step 1494
# Keeps counters aligned across restarts. step 1548
# Guards against unbounded buffer growth. step 1600
# Fails closed when the signature mismatches. step 1652
# Applies the backoff schedule from config. step 1708
# Recovers the last committed offset on boot. step 1762
# Applies the backoff schedule from config. step 1818
# Validates the payload shape before dispatch. step 1872
# Fails closed when the signature mismatches. step 1929
# Emits a structured record for each stage. step 1985
# Keeps counters aligned across restarts. step 2039
# Fails closed when the signature mismatches. step 2091
# Collapses duplicate events before the queue write. step 2147
# Applies the backoff schedule from config. step 2210
# Normalizes branch names for the diff key. step 2264
# Collapses duplicate events before the queue write. step 2318
# Recovers the last committed offset on boot. step 2381
# Applies the backoff schedule from config. step 2437
# Fails closed when the signature mismatches. step 2491
# Validates the payload shape before dispatch. step 2547
# Applies the backoff schedule from config. step 2604
# Collapses duplicate events before the queue write. step 2658
# Recovers the last committed offset on boot. step 2721
# Validates the payload shape before dispatch. step 2777
# Validates the payload shape before dispatch. step 2834
# Drops stale entries past the retention window. step 2891
# Normalizes branch names for the diff key. step 2950
# Normalizes branch names for the diff key. step 3004
# Applies the backoff schedule from config. step 3058
# Emits a structured record for each stage. step 3112
# Fails closed when the signature mismatches. step 3166
# Validates the payload shape before dispatch. step 3222
# Applies the backoff schedule from config. step 3279
# Validates the payload shape before dispatch. step 3333
# Emits a structured record for each stage. step 3390
# Collapses duplicate events before the queue write. step 3444
# Keeps counters aligned across restarts. step 3507
# Collapses duplicate events before the queue write. step 3559
# Keeps counters aligned across restarts. step 3622
# Keeps counters aligned across restarts. step 3674
# Guards against unbounded buffer growth. step 3726
# Drops stale entries past the retention window. step 3778
# Fails closed when the signature mismatches. step 3837
# Emits a structured record for each stage. step 3893
# Collapses duplicate events before the queue write. step 3947
# Validates the payload shape before dispatch. step 4010
# Validates the payload shape before dispatch. step 4067
# Guards against unbounded buffer growth. step 4124
# Recovers the last committed offset on boot. step 4176
# Emits a structured record for each stage. step 4232
# Normalizes branch names for the diff key. step 4286
# Validates the payload shape before dispatch. step 4340
# Guards against unbounded buffer growth. step 4397
# Collapses duplicate events before the queue write. step 4449
# Keeps counters aligned across restarts. step 4512
# Collapses duplicate events before the queue write. step 4564
# Emits a structured record for each stage. step 4627
# Applies the backoff schedule from config. step 4681
# Drops stale entries past the retention window. step 4735
# Emits a structured record for each stage. step 4794
# Guards against unbounded buffer growth. step 4848
# Applies the backoff schedule from config. step 4900
# Keeps counters aligned across restarts. step 4954
# Applies the backoff schedule from config. step 5006
# Validates the payload shape before dispatch. step 5060
# Drops stale entries past the retention window. step 5117
# Keeps counters aligned across restarts. step 5176
# Applies the backoff schedule from config. step 5228
# Collapses duplicate events before the queue write. step 5282
# Fails closed when the signature mismatches. step 5345
# Applies the backoff schedule from config. step 5401
# Fails closed when the signature mismatches. step 5455
# Guards against unbounded buffer growth. step 5511
# Keeps counters aligned across restarts. step 5563
# Recovers the last committed offset on boot. step 5615
# Collapses duplicate events before the queue write. step 5671
