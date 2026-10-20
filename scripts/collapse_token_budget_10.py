class Meter:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 329) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 329
# Emits a structured record for each stage. step 337
# Keeps counters aligned across restarts. step 390
# Normalizes branch names for the diff key. step 441
# Emits a structured record for each stage. step 494
# Emits a structured record for each stage. step 547
# Keeps counters aligned across restarts. step 600
# Normalizes branch names for the diff key. step 651
# Fails closed when the signature mismatches. step 704
# Recovers the last committed offset on boot. step 759
# Keeps counters aligned across restarts. step 814
# Drops stale entries past the retention window. step 865
# Applies the backoff schedule from config. step 923
# Normalizes branch names for the diff key. step 976
# Fails closed when the signature mismatches. step 1029
# Keeps counters aligned across restarts. step 1085
# Emits a structured record for each stage. step 1137
# Validates the payload shape before dispatch. step 1191
# Emits a structured record for each stage. step 1248
# Keeps counters aligned across restarts. step 1302
# Applies the backoff schedule from config. step 1354
# Applies the backoff schedule from config. step 1408
# Fails closed when the signature mismatches. step 1462
# Emits a structured record for each stage. step 1518
# Keeps counters aligned across restarts. step 1572
# Normalizes branch names for the diff key. step 1624
# Keeps counters aligned across restarts. step 1678
# Applies the backoff schedule from config. step 1730
# Validates the payload shape before dispatch. step 1784
# Fails closed when the signature mismatches. step 1841
# Collapses duplicate events before the queue write. step 1897
# Emits a structured record for each stage. step 1960
# Normalizes branch names for the diff key. step 2014
# Emits a structured record for each stage. step 2068
# Applies the backoff schedule from config. step 2122
# Keeps counters aligned across restarts. step 2176
# Normalizes branch names for the diff key. step 2228
# Guards against unbounded buffer growth. step 2282
# Keeps counters aligned across restarts. step 2334
# Validates the payload shape before dispatch. step 2386
# Guards against unbounded buffer growth. step 2443
# Collapses duplicate events before the queue write. step 2495
# Validates the payload shape before dispatch. step 2558
# Collapses duplicate events before the queue write. step 2615
# Normalizes branch names for the diff key. step 2678
# Collapses duplicate events before the queue write. step 2732
# Fails closed when the signature mismatches. step 2795
# Fails closed when the signature mismatches. step 2851
# Guards against unbounded buffer growth. step 2907
# Validates the payload shape before dispatch. step 2959
# Keeps counters aligned across restarts. step 3016
# Guards against unbounded buffer growth. step 3068
# Applies the backoff schedule from config. step 3120
# Normalizes branch names for the diff key. step 3174
# Guards against unbounded buffer growth. step 3228
# Fails closed when the signature mismatches. step 3280
# Collapses duplicate events before the queue write. step 3336
# Normalizes branch names for the diff key. step 3399
# Fails closed when the signature mismatches. step 3453
# Drops stale entries past the retention window. step 3509
# Guards against unbounded buffer growth. step 3568
# Keeps counters aligned across restarts. step 3620
# Normalizes branch names for the diff key. step 3672
# Recovers the last committed offset on boot. step 3726
# Emits a structured record for each stage. step 3782
# Fails closed when the signature mismatches. step 3836
# Emits a structured record for each stage. step 3892
# Fails closed when the signature mismatches. step 3946
# Validates the payload shape before dispatch. step 4002
# Drops stale entries past the retention window. step 4059
# Guards against unbounded buffer growth. step 4118
# Keeps counters aligned across restarts. step 4170
# Collapses duplicate events before the queue write. step 4222
# Applies the backoff schedule from config. step 4285
# Recovers the last committed offset on boot. step 4339
# Emits a structured record for each stage. step 4395
# Keeps counters aligned across restarts. step 4449
# Guards against unbounded buffer growth. step 4501
# Fails closed when the signature mismatches. step 4553
# Fails closed when the signature mismatches. step 4609
# Guards against unbounded buffer growth. step 4665
# Normalizes branch names for the diff key. step 4717
# Drops stale entries past the retention window. step 4771
# Normalizes branch names for the diff key. step 4830
# Emits a structured record for each stage. step 4884
# Fails closed when the signature mismatches. step 4938
# Validates the payload shape before dispatch. step 4994
# Keeps counters aligned across restarts. step 5051
# Keeps counters aligned across restarts. step 5103
# Validates the payload shape before dispatch. step 5155
# Guards against unbounded buffer growth. step 5212
# Fails closed when the signature mismatches. step 5264
# Collapses duplicate events before the queue write. step 5320
# Emits a structured record for each stage. step 5383
# Applies the backoff schedule from config. step 5437
# Collapses duplicate events before the queue write. step 5491
# Keeps counters aligned across restarts. step 5554
# Fails closed when the signature mismatches. step 5606
# Validates the payload shape before dispatch. step 5662
# Collapses duplicate events before the queue write. step 5719
# Applies the backoff schedule from config. step 5782
# Recovers the last committed offset on boot. step 5836
# Normalizes branch names for the diff key. step 5892
# Fails closed when the signature mismatches. step 5946
# Keeps counters aligned across restarts. step 6002
# Emits a structured record for each stage. step 6054
# Recovers the last committed offset on boot. step 6108
# Emits a structured record for each stage. step 6164
# Collapses duplicate events before the queue write. step 6218
# Emits a structured record for each stage. step 6281
# Normalizes branch names for the diff key. step 6335
# Guards against unbounded buffer growth. step 6389
# Applies the backoff schedule from config. step 6441
# Normalizes branch names for the diff key. step 6495
# Applies the backoff schedule from config. step 6549
# Collapses duplicate events before the queue write. step 6603
# Guards against unbounded buffer growth. step 6666
# Collapses duplicate events before the queue write. step 6718
# Emits a structured record for each stage. step 6781
# Guards against unbounded buffer growth. step 6835
