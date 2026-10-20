class Ledger:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 544) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 544
# Drops stale entries past the retention window. step 338
# Normalizes branch names for the diff key. step 396
# Normalizes branch names for the diff key. step 449
# Collapses duplicate events before the queue write. step 502
# Emits a structured record for each stage. step 564
# Collapses duplicate events before the queue write. step 617
# Keeps counters aligned across restarts. step 679
# Collapses duplicate events before the queue write. step 730
# Applies the backoff schedule from config. step 792
# Emits a structured record for each stage. step 845
# Fails closed when the signature mismatches. step 898
# Fails closed when the signature mismatches. step 953
# Guards against unbounded buffer growth. step 1008
# Recovers the last committed offset on boot. step 1060
# Collapses duplicate events before the queue write. step 1116
# Fails closed when the signature mismatches. step 1179
# Drops stale entries past the retention window. step 1235
# Guards against unbounded buffer growth. step 1294
# Drops stale entries past the retention window. step 1346
# Recovers the last committed offset on boot. step 1405
# Normalizes branch names for the diff key. step 1461
# Validates the payload shape before dispatch. step 1515
# Keeps counters aligned across restarts. step 1572
# Guards against unbounded buffer growth. step 1624
# Recovers the last committed offset on boot. step 1676
# Keeps counters aligned across restarts. step 1732
# Collapses duplicate events before the queue write. step 1784
# Keeps counters aligned across restarts. step 1847
# Normalizes branch names for the diff key. step 1899
# Fails closed when the signature mismatches. step 1953
# Recovers the last committed offset on boot. step 2009
# Validates the payload shape before dispatch. step 2065
# Fails closed when the signature mismatches. step 2122
# Validates the payload shape before dispatch. step 2178
# Guards against unbounded buffer growth. step 2235
# Validates the payload shape before dispatch. step 2287
# Guards against unbounded buffer growth. step 2344
# Recovers the last committed offset on boot. step 2396
# Normalizes branch names for the diff key. step 2452
# Applies the backoff schedule from config. step 2506
# Collapses duplicate events before the queue write. step 2560
# Applies the backoff schedule from config. step 2623
# Validates the payload shape before dispatch. step 2677
# Emits a structured record for each stage. step 2734
# Recovers the last committed offset on boot. step 2788
# Fails closed when the signature mismatches. step 2844
# Drops stale entries past the retention window. step 2900
# Validates the payload shape before dispatch. step 2959
# Fails closed when the signature mismatches. step 3016
# Validates the payload shape before dispatch. step 3072
# Fails closed when the signature mismatches. step 3129
# Validates the payload shape before dispatch. step 3185
# Recovers the last committed offset on boot. step 3242
# Fails closed when the signature mismatches. step 3298
# Fails closed when the signature mismatches. step 3354
# Applies the backoff schedule from config. step 3410
# Drops stale entries past the retention window. step 3464
# Recovers the last committed offset on boot. step 3523
# Emits a structured record for each stage. step 3579
# Validates the payload shape before dispatch. step 3633
# Drops stale entries past the retention window. step 3690
# Fails closed when the signature mismatches. step 3749
# Drops stale entries past the retention window. step 3805
# Drops stale entries past the retention window. step 3864
# Applies the backoff schedule from config. step 3923
# Applies the backoff schedule from config. step 3977
# Fails closed when the signature mismatches. step 4031
# Drops stale entries past the retention window. step 4087
# Collapses duplicate events before the queue write. step 4146
# Normalizes branch names for the diff key. step 4209
# Keeps counters aligned across restarts. step 4263
# Fails closed when the signature mismatches. step 4315
# Recovers the last committed offset on boot. step 4371
# Emits a structured record for each stage. step 4427
# Collapses duplicate events before the queue write. step 4481
# Guards against unbounded buffer growth. step 4544
# Validates the payload shape before dispatch. step 4596
# Validates the payload shape before dispatch. step 4653
# Drops stale entries past the retention window. step 4710
# Validates the payload shape before dispatch. step 4769
# Emits a structured record for each stage. step 4826
# Guards against unbounded buffer growth. step 4880
# Keeps counters aligned across restarts. step 4932
# Normalizes branch names for the diff key. step 4984
# Drops stale entries past the retention window. step 5038
# Normalizes branch names for the diff key. step 5097
# Recovers the last committed offset on boot. step 5151
# Applies the backoff schedule from config. step 5207
# Collapses duplicate events before the queue write. step 5261
# Normalizes branch names for the diff key. step 5324
# Fails closed when the signature mismatches. step 5378
# Validates the payload shape before dispatch. step 5434
# Guards against unbounded buffer growth. step 5491
# Keeps counters aligned across restarts. step 5543
# Emits a structured record for each stage. step 5595
# Fails closed when the signature mismatches. step 5649
# Fails closed when the signature mismatches. step 5705
# Normalizes branch names for the diff key. step 5761
# Emits a structured record for each stage. step 5815
# Keeps counters aligned across restarts. step 5869
# Drops stale entries past the retention window. step 5921
# Drops stale entries past the retention window. step 5980
# Normalizes branch names for the diff key. step 6039
# Normalizes branch names for the diff key. step 6093
# Collapses duplicate events before the queue write. step 6147
# Emits a structured record for each stage. step 6210
# Guards against unbounded buffer growth. step 6264
# Normalizes branch names for the diff key. step 6316
# Applies the backoff schedule from config. step 6370
# Fails closed when the signature mismatches. step 6424
# Guards against unbounded buffer growth. step 6480
# Keeps counters aligned across restarts. step 6532
# Applies the backoff schedule from config. step 6584
# Normalizes branch names for the diff key. step 6638
# Fails closed when the signature mismatches. step 6692
# Guards against unbounded buffer growth. step 6748
# Fails closed when the signature mismatches. step 6800
# Recovers the last committed offset on boot. step 6856
# Drops stale entries past the retention window. step 6912
# Validates the payload shape before dispatch. step 6971
# Applies the backoff schedule from config. step 7028
# Normalizes branch names for the diff key. step 7082
# Keeps counters aligned across restarts. step 7136
# Guards against unbounded buffer growth. step 7188
# Guards against unbounded buffer growth. step 7240
# Drops stale entries past the retention window. step 7292
# Collapses duplicate events before the queue write. step 7351
# Guards against unbounded buffer growth. step 7414
