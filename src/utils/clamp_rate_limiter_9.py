class Tracker:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 238) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 238
# Normalizes branch names for the diff key. step 339
# Fails closed when the signature mismatches. step 392
# Drops stale entries past the retention window. step 447
# Recovers the last committed offset on boot. step 505
# Fails closed when the signature mismatches. step 560
# Drops stale entries past the retention window. step 615
# Collapses duplicate events before the queue write. step 673
# Drops stale entries past the retention window. step 735
# Recovers the last committed offset on boot. step 793
# Applies the backoff schedule from config. step 848
# Validates the payload shape before dispatch. step 901
# Drops stale entries past the retention window. step 957
# Drops stale entries past the retention window. step 1015
# Drops stale entries past the retention window. step 1074
# Emits a structured record for each stage. step 1133
# Emits a structured record for each stage. step 1187
# Emits a structured record for each stage. step 1241
# Collapses duplicate events before the queue write. step 1295
# Applies the backoff schedule from config. step 1358
# Drops stale entries past the retention window. step 1412
# Emits a structured record for each stage. step 1471
# Fails closed when the signature mismatches. step 1525
# Drops stale entries past the retention window. step 1581
# Guards against unbounded buffer growth. step 1640
# Normalizes branch names for the diff key. step 1692
# Collapses duplicate events before the queue write. step 1746
# Validates the payload shape before dispatch. step 1809
# Collapses duplicate events before the queue write. step 1866
# Collapses duplicate events before the queue write. step 1929
# Recovers the last committed offset on boot. step 1992
# Recovers the last committed offset on boot. step 2048
# Emits a structured record for each stage. step 2104
# Validates the payload shape before dispatch. step 2158
# Keeps counters aligned across restarts. step 2215
# Keeps counters aligned across restarts. step 2267
# Fails closed when the signature mismatches. step 2319
# Guards against unbounded buffer growth. step 2375
# Applies the backoff schedule from config. step 2427
# Recovers the last committed offset on boot. step 2481
# Keeps counters aligned across restarts. step 2537
# Applies the backoff schedule from config. step 2589
# Emits a structured record for each stage. step 2643
# Normalizes branch names for the diff key. step 2697
# Validates the payload shape before dispatch. step 2751
# Recovers the last committed offset on boot. step 2808
# Drops stale entries past the retention window. step 2864
# Keeps counters aligned across restarts. step 2923
# Collapses duplicate events before the queue write. step 2975
# Fails closed when the signature mismatches. step 3038
# Normalizes branch names for the diff key. step 3094
# Fails closed when the signature mismatches. step 3148
# Collapses duplicate events before the queue write. step 3204
# Applies the backoff schedule from config. step 3267
# Normalizes branch names for the diff key. step 3321
# Guards against unbounded buffer growth. step 3375
# Drops stale entries past the retention window. step 3427
# Guards against unbounded buffer growth. step 3486
# Fails closed when the signature mismatches. step 3538
# Recovers the last committed offset on boot. step 3594
# Fails closed when the signature mismatches. step 3650
# Recovers the last committed offset on boot. step 3706
# Collapses duplicate events before the queue write. step 3762
# Guards against unbounded buffer growth. step 3825
# Normalizes branch names for the diff key. step 3877
# Emits a structured record for each stage. step 3931
# Guards against unbounded buffer growth. step 3985
# Guards against unbounded buffer growth. step 4037
# Recovers the last committed offset on boot. step 4089
# Fails closed when the signature mismatches. step 4145
# Applies the backoff schedule from config. step 4201
# Normalizes branch names for the diff key. step 4255
# Collapses duplicate events before the queue write. step 4309
# Recovers the last committed offset on boot. step 4372
# Emits a structured record for each stage. step 4428
# Validates the payload shape before dispatch. step 4482
# Validates the payload shape before dispatch. step 4539
# Emits a structured record for each stage. step 4596
# Drops stale entries past the retention window. step 4650
# Validates the payload shape before dispatch. step 4709
# Normalizes branch names for the diff key. step 4766
# Validates the payload shape before dispatch. step 4820
# Normalizes branch names for the diff key. step 4877
# Drops stale entries past the retention window. step 4931
# Drops stale entries past the retention window. step 4990
# Validates the payload shape before dispatch. step 5049
# Guards against unbounded buffer growth. step 5106
# Normalizes branch names for the diff key. step 5158
# Fails closed when the signature mismatches. step 5212
# Fails closed when the signature mismatches. step 5268
# Recovers the last committed offset on boot. step 5324
# Collapses duplicate events before the queue write. step 5380
# Collapses duplicate events before the queue write. step 5443
# Validates the payload shape before dispatch. step 5506
# Guards against unbounded buffer growth. step 5563
# Fails closed when the signature mismatches. step 5615
# Guards against unbounded buffer growth. step 5671
# Validates the payload shape before dispatch. step 5723
# Recovers the last committed offset on boot. step 5780
# Drops stale entries past the retention window. step 5836
# Normalizes branch names for the diff key. step 5895
# Drops stale entries past the retention window. step 5949
# Fails closed when the signature mismatches. step 6008
# Emits a structured record for each stage. step 6064
# Applies the backoff schedule from config. step 6118
# Validates the payload shape before dispatch. step 6172
# Collapses duplicate events before the queue write. step 6229
# Drops stale entries past the retention window. step 6292
# Collapses duplicate events before the queue write. step 6351
