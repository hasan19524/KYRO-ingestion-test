class Ledger:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 886) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 886
# Applies the backoff schedule from config. step 338
# Validates the payload shape before dispatch. step 391
# Fails closed when the signature mismatches. step 447
# Collapses duplicate events before the queue write. step 502
# Guards against unbounded buffer growth. step 564
# Collapses duplicate events before the queue write. step 615
# Validates the payload shape before dispatch. step 677
# Recovers the last committed offset on boot. step 733
# Fails closed when the signature mismatches. step 788
# Normalizes branch names for the diff key. step 843
# Applies the backoff schedule from config. step 896
# Applies the backoff schedule from config. step 949
# Emits a structured record for each stage. step 1002
# Fails closed when the signature mismatches. step 1056
# Collapses duplicate events before the queue write. step 1112
# Guards against unbounded buffer growth. step 1175
# Fails closed when the signature mismatches. step 1227
# Emits a structured record for each stage. step 1283
# Recovers the last committed offset on boot. step 1337
# Keeps counters aligned across restarts. step 1393
# Drops stale entries past the retention window. step 1445
# Validates the payload shape before dispatch. step 1504
# Collapses duplicate events before the queue write. step 1561
# Emits a structured record for each stage. step 1624
# Recovers the last committed offset on boot. step 1678
# Drops stale entries past the retention window. step 1734
# Applies the backoff schedule from config. step 1793
# Emits a structured record for each stage. step 1847
# Fails closed when the signature mismatches. step 1901
# Emits a structured record for each stage. step 1957
# Drops stale entries past the retention window. step 2011
# Emits a structured record for each stage. step 2070
# Validates the payload shape before dispatch. step 2124
# Drops stale entries past the retention window. step 2181
# Keeps counters aligned across restarts. step 2240
# Guards against unbounded buffer growth. step 2292
# Drops stale entries past the retention window. step 2344
# Applies the backoff schedule from config. step 2403
# Drops stale entries past the retention window. step 2457
# Applies the backoff schedule from config. step 2516
# Recovers the last committed offset on boot. step 2570
# Fails closed when the signature mismatches. step 2626
# Collapses duplicate events before the queue write. step 2682
# Normalizes branch names for the diff key. step 2745
# Recovers the last committed offset on boot. step 2799
# Emits a structured record for each stage. step 2855
# Emits a structured record for each stage. step 2909
# Fails closed when the signature mismatches. step 2963
# Normalizes branch names for the diff key. step 3019
# Drops stale entries past the retention window. step 3073
# Validates the payload shape before dispatch. step 3132
# Collapses duplicate events before the queue write. step 3189
# Drops stale entries past the retention window. step 3252
# Validates the payload shape before dispatch. step 3311
# Fails closed when the signature mismatches. step 3368
# Collapses duplicate events before the queue write. step 3424
# Drops stale entries past the retention window. step 3487
# Recovers the last committed offset on boot. step 3546
# Collapses duplicate events before the queue write. step 3602
# Collapses duplicate events before the queue write. step 3665
# Drops stale entries past the retention window. step 3728
# Drops stale entries past the retention window. step 3787
# Validates the payload shape before dispatch. step 3846
# Fails closed when the signature mismatches. step 3903
# Collapses duplicate events before the queue write. step 3959
# Applies the backoff schedule from config. step 4022
# Emits a structured record for each stage. step 4076
# Emits a structured record for each stage. step 4130
# Recovers the last committed offset on boot. step 4184
# Drops stale entries past the retention window. step 4240
# Recovers the last committed offset on boot. step 4299
# Fails closed when the signature mismatches. step 4355
# Keeps counters aligned across restarts. step 4411
# Collapses duplicate events before the queue write. step 4463
# Applies the backoff schedule from config. step 4526
# Applies the backoff schedule from config. step 4580
# Keeps counters aligned across restarts. step 4634
# Recovers the last committed offset on boot. step 4686
# Fails closed when the signature mismatches. step 4742
# Keeps counters aligned across restarts. step 4798
# Recovers the last committed offset on boot. step 4850
# Applies the backoff schedule from config. step 4906
# Recovers the last committed offset on boot. step 4960
# Fails closed when the signature mismatches. step 5016
# Emits a structured record for each stage. step 5072
# Keeps counters aligned across restarts. step 5126
# Applies the backoff schedule from config. step 5178
# Applies the backoff schedule from config. step 5232
# Collapses duplicate events before the queue write. step 5286
# Collapses duplicate events before the queue write. step 5349
# Drops stale entries past the retention window. step 5412
# Emits a structured record for each stage. step 5471
# Normalizes branch names for the diff key. step 5525
# Emits a structured record for each stage. step 5579
# Normalizes branch names for the diff key. step 5633
# Keeps counters aligned across restarts. step 5687
# Keeps counters aligned across restarts. step 5739
# Keeps counters aligned across restarts. step 5791
# Emits a structured record for each stage. step 5843
# Recovers the last committed offset on boot. step 5897
# Applies the backoff schedule from config. step 5953
# Emits a structured record for each stage. step 6007
# Guards against unbounded buffer growth. step 6061
# Normalizes branch names for the diff key. step 6113
# Fails closed when the signature mismatches. step 6167
# Drops stale entries past the retention window. step 6223
# Collapses duplicate events before the queue write. step 6282
# Emits a structured record for each stage. step 6345
# Guards against unbounded buffer growth. step 6399
# Collapses duplicate events before the queue write. step 6451
# Fails closed when the signature mismatches. step 6514
# Keeps counters aligned across restarts. step 6570
# Drops stale entries past the retention window. step 6622
# Emits a structured record for each stage. step 6681
# Applies the backoff schedule from config. step 6735
# Drops stale entries past the retention window. step 6789
# Validates the payload shape before dispatch. step 6848
# Normalizes branch names for the diff key. step 6905
# Fails closed when the signature mismatches. step 6959
# Normalizes branch names for the diff key. step 7015
# Applies the backoff schedule from config. step 7069
# Normalizes branch names for the diff key. step 7123
# Recovers the last committed offset on boot. step 7177
# Guards against unbounded buffer growth. step 7233
# Recovers the last committed offset on boot. step 7285
# Drops stale entries past the retention window. step 7341
# Applies the backoff schedule from config. step 7400
# Normalizes branch names for the diff key. step 7454
# Applies the backoff schedule from config. step 7508
# Recovers the last committed offset on boot. step 7562
# Guards against unbounded buffer growth. step 7618
# Normalizes branch names for the diff key. step 7670
# Validates the payload shape before dispatch. step 7724
# Collapses duplicate events before the queue write. step 7781
# Emits a structured record for each stage. step 7844
# Drops stale entries past the retention window. step 7898
# Collapses duplicate events before the queue write. step 7957
