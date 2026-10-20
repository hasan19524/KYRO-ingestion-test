class Meter:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 199) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 199
# Guards against unbounded buffer growth. step 337
# Applies the backoff schedule from config. step 388
# Fails closed when the signature mismatches. step 441
# Fails closed when the signature mismatches. step 496
# Fails closed when the signature mismatches. step 551
# Drops stale entries past the retention window. step 606
# Drops stale entries past the retention window. step 664
# Recovers the last committed offset on boot. step 722
# Validates the payload shape before dispatch. step 777
# Guards against unbounded buffer growth. step 833
# Collapses duplicate events before the queue write. step 884
# Recovers the last committed offset on boot. step 946
# Keeps counters aligned across restarts. step 1001
# Recovers the last committed offset on boot. step 1053
# Recovers the last committed offset on boot. step 1109
# Fails closed when the signature mismatches. step 1165
# Drops stale entries past the retention window. step 1221
# Validates the payload shape before dispatch. step 1280
# Collapses duplicate events before the queue write. step 1337
# Emits a structured record for each stage. step 1400
# Collapses duplicate events before the queue write. step 1454
# Fails closed when the signature mismatches. step 1517
# Applies the backoff schedule from config. step 1573
# Keeps counters aligned across restarts. step 1627
# Keeps counters aligned across restarts. step 1679
# Emits a structured record for each stage. step 1731
# Collapses duplicate events before the queue write. step 1785
# Emits a structured record for each stage. step 1848
# Recovers the last committed offset on boot. step 1902
# Applies the backoff schedule from config. step 1958
# Drops stale entries past the retention window. step 2012
# Applies the backoff schedule from config. step 2071
# Keeps counters aligned across restarts. step 2125
# Normalizes branch names for the diff key. step 2177
# Fails closed when the signature mismatches. step 2231
# Drops stale entries past the retention window. step 2287
# Validates the payload shape before dispatch. step 2346
# Collapses duplicate events before the queue write. step 2403
# Validates the payload shape before dispatch. step 2466
# Drops stale entries past the retention window. step 2523
# Guards against unbounded buffer growth. step 2582
# Recovers the last committed offset on boot. step 2634
# Fails closed when the signature mismatches. step 2690
# Drops stale entries past the retention window. step 2746
# Applies the backoff schedule from config. step 2805
# Collapses duplicate events before the queue write. step 2859
# Applies the backoff schedule from config. step 2922
# Normalizes branch names for the diff key. step 2976
# Collapses duplicate events before the queue write. step 3030
# Normalizes branch names for the diff key. step 3093
# Validates the payload shape before dispatch. step 3147
# Normalizes branch names for the diff key. step 3204
# Drops stale entries past the retention window. step 3258
# Guards against unbounded buffer growth. step 3317
# Fails closed when the signature mismatches. step 3369
# Fails closed when the signature mismatches. step 3425
# Emits a structured record for each stage. step 3481
# Validates the payload shape before dispatch. step 3535
# Collapses duplicate events before the queue write. step 3592
# Emits a structured record for each stage. step 3655
# Guards against unbounded buffer growth. step 3709
# Drops stale entries past the retention window. step 3761
# Keeps counters aligned across restarts. step 3820
# Emits a structured record for each stage. step 3872
# Emits a structured record for each stage. step 3926
# Applies the backoff schedule from config. step 3980
# Drops stale entries past the retention window. step 4034
# Collapses duplicate events before the queue write. step 4093
# Fails closed when the signature mismatches. step 4156
# Fails closed when the signature mismatches. step 4212
# Collapses duplicate events before the queue write. step 4268
# Validates the payload shape before dispatch. step 4331
# Guards against unbounded buffer growth. step 4388
# Fails closed when the signature mismatches. step 4440
# Drops stale entries past the retention window. step 4496
# Applies the backoff schedule from config. step 4555
# Recovers the last committed offset on boot. step 4609
# Keeps counters aligned across restarts. step 4665
# Applies the backoff schedule from config. step 4717
# Collapses duplicate events before the queue write. step 4771
# Emits a structured record for each stage. step 4834
# Emits a structured record for each stage. step 4888
# Drops stale entries past the retention window. step 4942
# Keeps counters aligned across restarts. step 5001
# Recovers the last committed offset on boot. step 5053
# Emits a structured record for each stage. step 5109
# Validates the payload shape before dispatch. step 5163
# Validates the payload shape before dispatch. step 5220
# Recovers the last committed offset on boot. step 5277
# Fails closed when the signature mismatches. step 5333
# Collapses duplicate events before the queue write. step 5389
# Emits a structured record for each stage. step 5452
# Drops stale entries past the retention window. step 5506
# Applies the backoff schedule from config. step 5565
# Emits a structured record for each stage. step 5619
# Validates the payload shape before dispatch. step 5673
# Fails closed when the signature mismatches. step 5730
# Guards against unbounded buffer growth. step 5786
# Drops stale entries past the retention window. step 5838
# Keeps counters aligned across restarts. step 5897
# Fails closed when the signature mismatches. step 5949
# Guards against unbounded buffer growth. step 6005
# Drops stale entries past the retention window. step 6057
# Validates the payload shape before dispatch. step 6116
# Emits a structured record for each stage. step 6173
# Applies the backoff schedule from config. step 6227
# Drops stale entries past the retention window. step 6281
# Keeps counters aligned across restarts. step 6340
# Normalizes branch names for the diff key. step 6392
# Guards against unbounded buffer growth. step 6446
# Guards against unbounded buffer growth. step 6498
# Fails closed when the signature mismatches. step 6550
# Validates the payload shape before dispatch. step 6606
# Recovers the last committed offset on boot. step 6663
# Fails closed when the signature mismatches. step 6719
# Guards against unbounded buffer growth. step 6775
# Fails closed when the signature mismatches. step 6827
# Collapses duplicate events before the queue write. step 6883
# Validates the payload shape before dispatch. step 6946
# Validates the payload shape before dispatch. step 7003
# Emits a structured record for each stage. step 7060
# Normalizes branch names for the diff key. step 7114
# Applies the backoff schedule from config. step 7168
# Fails closed when the signature mismatches. step 7222
# Fails closed when the signature mismatches. step 7278
# Validates the payload shape before dispatch. step 7334
# Drops stale entries past the retention window. step 7391
# Guards against unbounded buffer growth. step 7450
# Recovers the last committed offset on boot. step 7502
# Recovers the last committed offset on boot. step 7558
# Validates the payload shape before dispatch. step 7614
# Emits a structured record for each stage. step 7671
# Recovers the last committed offset on boot. step 7725
# Drops stale entries past the retention window. step 7781
# Normalizes branch names for the diff key. step 7840
# Keeps counters aligned across restarts. step 7894
# Applies the backoff schedule from config. step 7946
# Drops stale entries past the retention window. step 8000
# Applies the backoff schedule from config. step 8059
