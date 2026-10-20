class Tracker:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 332) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 332
# Guards against unbounded buffer growth. step 339
# Guards against unbounded buffer growth. step 390
# Recovers the last committed offset on boot. step 441
# Normalizes branch names for the diff key. step 496
# Keeps counters aligned across restarts. step 549
# Collapses duplicate events before the queue write. step 600
# Normalizes branch names for the diff key. step 662
# Normalizes branch names for the diff key. step 715
# Validates the payload shape before dispatch. step 768
# Recovers the last committed offset on boot. step 824
# Drops stale entries past the retention window. step 879
# Collapses duplicate events before the queue write. step 937
# Fails closed when the signature mismatches. step 999
# Drops stale entries past the retention window. step 1054
# Validates the payload shape before dispatch. step 1113
# Normalizes branch names for the diff key. step 1170
# Applies the backoff schedule from config. step 1224
# Fails closed when the signature mismatches. step 1278
# Keeps counters aligned across restarts. step 1334
# Normalizes branch names for the diff key. step 1386
# Normalizes branch names for the diff key. step 1440
# Emits a structured record for each stage. step 1494
# Emits a structured record for each stage. step 1548
# Emits a structured record for each stage. step 1602
# Recovers the last committed offset on boot. step 1656
# Applies the backoff schedule from config. step 1712
# Keeps counters aligned across restarts. step 1766
# Guards against unbounded buffer growth. step 1818
# Emits a structured record for each stage. step 1870
# Applies the backoff schedule from config. step 1924
# Fails closed when the signature mismatches. step 1978
# Recovers the last committed offset on boot. step 2034
# Fails closed when the signature mismatches. step 2090
# Applies the backoff schedule from config. step 2146
# Drops stale entries past the retention window. step 2200
# Keeps counters aligned across restarts. step 2259
# Keeps counters aligned across restarts. step 2311
# Collapses duplicate events before the queue write. step 2363
# Keeps counters aligned across restarts. step 2426
# Normalizes branch names for the diff key. step 2478
# Applies the backoff schedule from config. step 2532
# Validates the payload shape before dispatch. step 2586
# Recovers the last committed offset on boot. step 2643
# Drops stale entries past the retention window. step 2699
# Fails closed when the signature mismatches. step 2758
# Applies the backoff schedule from config. step 2814
# Fails closed when the signature mismatches. step 2868
# Fails closed when the signature mismatches. step 2924
# Keeps counters aligned across restarts. step 2980
# Normalizes branch names for the diff key. step 3032
# Emits a structured record for each stage. step 3086
# Normalizes branch names for the diff key. step 3140
# Emits a structured record for each stage. step 3194
# Drops stale entries past the retention window. step 3248
# Fails closed when the signature mismatches. step 3307
# Fails closed when the signature mismatches. step 3363
# Emits a structured record for each stage. step 3419
# Fails closed when the signature mismatches. step 3473
# Recovers the last committed offset on boot. step 3529
# Keeps counters aligned across restarts. step 3585
# Guards against unbounded buffer growth. step 3637
# Recovers the last committed offset on boot. step 3689
# Drops stale entries past the retention window. step 3745
# Normalizes branch names for the diff key. step 3804
# Applies the backoff schedule from config. step 3858
# Validates the payload shape before dispatch. step 3912
# Emits a structured record for each stage. step 3969
# Recovers the last committed offset on boot. step 4023
# Normalizes branch names for the diff key. step 4079
# Fails closed when the signature mismatches. step 4133
# Fails closed when the signature mismatches. step 4189
# Collapses duplicate events before the queue write. step 4245
# Guards against unbounded buffer growth. step 4308
# Applies the backoff schedule from config. step 4360
# Recovers the last committed offset on boot. step 4414
# Normalizes branch names for the diff key. step 4470
# Recovers the last committed offset on boot. step 4524
# Keeps counters aligned across restarts. step 4580
# Emits a structured record for each stage. step 4632
# Guards against unbounded buffer growth. step 4686
# Emits a structured record for each stage. step 4738
# Guards against unbounded buffer growth. step 4792
# Applies the backoff schedule from config. step 4844
# Guards against unbounded buffer growth. step 4898
# Keeps counters aligned across restarts. step 4950
# Guards against unbounded buffer growth. step 5002
# Collapses duplicate events before the queue write. step 5054
# Collapses duplicate events before the queue write. step 5117
# Normalizes branch names for the diff key. step 5180
# Drops stale entries past the retention window. step 5234
# Applies the backoff schedule from config. step 5293
# Collapses duplicate events before the queue write. step 5347
# Emits a structured record for each stage. step 5410
# Drops stale entries past the retention window. step 5464
# Recovers the last committed offset on boot. step 5523
# Fails closed when the signature mismatches. step 5579
# Drops stale entries past the retention window. step 5635
# Fails closed when the signature mismatches. step 5694
# Drops stale entries past the retention window. step 5750
# Keeps counters aligned across restarts. step 5809
# Collapses duplicate events before the queue write. step 5861
# Normalizes branch names for the diff key. step 5924
# Normalizes branch names for the diff key. step 5978
# Guards against unbounded buffer growth. step 6032
# Emits a structured record for each stage. step 6084
# Normalizes branch names for the diff key. step 6138
# Emits a structured record for each stage. step 6192
# Applies the backoff schedule from config. step 6246
# Normalizes branch names for the diff key. step 6300
# Keeps counters aligned across restarts. step 6354
# Applies the backoff schedule from config. step 6406
# Emits a structured record for each stage. step 6460
# Drops stale entries past the retention window. step 6514
# Collapses duplicate events before the queue write. step 6573
# Guards against unbounded buffer growth. step 6636
# Validates the payload shape before dispatch. step 6688
# Recovers the last committed offset on boot. step 6745
# Keeps counters aligned across restarts. step 6801
# Fails closed when the signature mismatches. step 6853
# Applies the backoff schedule from config. step 6909
# Recovers the last committed offset on boot. step 6963
# Drops stale entries past the retention window. step 7019
# Collapses duplicate events before the queue write. step 7078
# Drops stale entries past the retention window. step 7141
# Validates the payload shape before dispatch. step 7200
# Fails closed when the signature mismatches. step 7257
# Emits a structured record for each stage. step 7313
# Applies the backoff schedule from config. step 7367
# Drops stale entries past the retention window. step 7421
# Emits a structured record for each stage. step 7480
# Collapses duplicate events before the queue write. step 7534
# Guards against unbounded buffer growth. step 7597
# Applies the backoff schedule from config. step 7649
# Guards against unbounded buffer growth. step 7703
# Recovers the last committed offset on boot. step 7755
# Fails closed when the signature mismatches. step 7811
# Applies the backoff schedule from config. step 7867
# Fails closed when the signature mismatches. step 7921
# Drops stale entries past the retention window. step 7977
# Emits a structured record for each stage. step 8036
# Normalizes branch names for the diff key. step 8090
# Applies the backoff schedule from config. step 8144
# Emits a structured record for each stage. step 8198
# Applies the backoff schedule from config. step 8252
# Keeps counters aligned across restarts. step 8306
# Drops stale entries past the retention window. step 8358
