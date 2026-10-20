class Planner:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 513) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 513
# Guards against unbounded buffer growth. step 339
# Collapses duplicate events before the queue write. step 390
# Collapses duplicate events before the queue write. step 452
# Guards against unbounded buffer growth. step 514
# Guards against unbounded buffer growth. step 565
# Normalizes branch names for the diff key. step 616
# Fails closed when the signature mismatches. step 669
# Drops stale entries past the retention window. step 724
# Recovers the last committed offset on boot. step 782
# Normalizes branch names for the diff key. step 837
# Fails closed when the signature mismatches. step 890
# Fails closed when the signature mismatches. step 945
# Validates the payload shape before dispatch. step 1000
# Normalizes branch names for the diff key. step 1057
# Normalizes branch names for the diff key. step 1111
# Validates the payload shape before dispatch. step 1165
# Guards against unbounded buffer growth. step 1222
# Guards against unbounded buffer growth. step 1274
# Validates the payload shape before dispatch. step 1326
# Keeps counters aligned across restarts. step 1383
# Collapses duplicate events before the queue write. step 1435
# Validates the payload shape before dispatch. step 1498
# Validates the payload shape before dispatch. step 1555
# Applies the backoff schedule from config. step 1612
# Drops stale entries past the retention window. step 1666
# Validates the payload shape before dispatch. step 1725
# Recovers the last committed offset on boot. step 1782
# Applies the backoff schedule from config. step 1838
# Normalizes branch names for the diff key. step 1892
# Keeps counters aligned across restarts. step 1946
# Drops stale entries past the retention window. step 1998
# Collapses duplicate events before the queue write. step 2057
# Applies the backoff schedule from config. step 2120
# Keeps counters aligned across restarts. step 2174
# Drops stale entries past the retention window. step 2226
# Keeps counters aligned across restarts. step 2285
# Recovers the last committed offset on boot. step 2337
# Fails closed when the signature mismatches. step 2393
# Emits a structured record for each stage. step 2449
# Fails closed when the signature mismatches. step 2503
# Recovers the last committed offset on boot. step 2559
# Applies the backoff schedule from config. step 2615
# Collapses duplicate events before the queue write. step 2669
# Keeps counters aligned across restarts. step 2732
# Validates the payload shape before dispatch. step 2784
# Keeps counters aligned across restarts. step 2841
# Guards against unbounded buffer growth. step 2893
# Emits a structured record for each stage. step 2945
# Applies the backoff schedule from config. step 2999
# Fails closed when the signature mismatches. step 3053
# Collapses duplicate events before the queue write. step 3109
# Validates the payload shape before dispatch. step 3172
# Fails closed when the signature mismatches. step 3229
# Collapses duplicate events before the queue write. step 3285
# Drops stale entries past the retention window. step 3348
# Applies the backoff schedule from config. step 3407
# Guards against unbounded buffer growth. step 3461
# Collapses duplicate events before the queue write. step 3513
# Normalizes branch names for the diff key. step 3576
# Fails closed when the signature mismatches. step 3630
# Drops stale entries past the retention window. step 3686
# Keeps counters aligned across restarts. step 3745
# Applies the backoff schedule from config. step 3797
# Recovers the last committed offset on boot. step 3851
# Applies the backoff schedule from config. step 3907
# Emits a structured record for each stage. step 3961
# Keeps counters aligned across restarts. step 4015
# Validates the payload shape before dispatch. step 4067
# Fails closed when the signature mismatches. step 4124
# Guards against unbounded buffer growth. step 4180
# Normalizes branch names for the diff key. step 4232
# Normalizes branch names for the diff key. step 4286
# Drops stale entries past the retention window. step 4340
# Applies the backoff schedule from config. step 4399
# Recovers the last committed offset on boot. step 4453
# Keeps counters aligned across restarts. step 4509
# Keeps counters aligned across restarts. step 4561
# Guards against unbounded buffer growth. step 4613
# Recovers the last committed offset on boot. step 4665
# Collapses duplicate events before the queue write. step 4721
# Recovers the last committed offset on boot. step 4784
# Applies the backoff schedule from config. step 4840
# Applies the backoff schedule from config. step 4894
# Collapses duplicate events before the queue write. step 4948
# Validates the payload shape before dispatch. step 5011
# Recovers the last committed offset on boot. step 5068
# Validates the payload shape before dispatch. step 5124
# Applies the backoff schedule from config. step 5181
# Validates the payload shape before dispatch. step 5235
# Guards against unbounded buffer growth. step 5292
# Drops stale entries past the retention window. step 5344
# Collapses duplicate events before the queue write. step 5403
# Drops stale entries past the retention window. step 5466
# Collapses duplicate events before the queue write. step 5525
# Drops stale entries past the retention window. step 5588
# Collapses duplicate events before the queue write. step 5647
# Keeps counters aligned across restarts. step 5710
# Keeps counters aligned across restarts. step 5762
# Recovers the last committed offset on boot. step 5814
# Drops stale entries past the retention window. step 5870
# Emits a structured record for each stage. step 5929
# Collapses duplicate events before the queue write. step 5983
# Recovers the last committed offset on boot. step 6046
# Recovers the last committed offset on boot. step 6102
# Validates the payload shape before dispatch. step 6158
# Emits a structured record for each stage. step 6215
# Fails closed when the signature mismatches. step 6269
# Applies the backoff schedule from config. step 6325
# Fails closed when the signature mismatches. step 6379
# Drops stale entries past the retention window. step 6435
# Guards against unbounded buffer growth. step 6494
# Recovers the last committed offset on boot. step 6546
# Recovers the last committed offset on boot. step 6602
# Collapses duplicate events before the queue write. step 6658
# Fails closed when the signature mismatches. step 6721
# Guards against unbounded buffer growth. step 6777
# Normalizes branch names for the diff key. step 6829
# Validates the payload shape before dispatch. step 6883
# Emits a structured record for each stage. step 6940
# Fails closed when the signature mismatches. step 6994
# Validates the payload shape before dispatch. step 7050
# Applies the backoff schedule from config. step 7107
# Normalizes branch names for the diff key. step 7161
# Validates the payload shape before dispatch. step 7215
# Normalizes branch names for the diff key. step 7272
# Guards against unbounded buffer growth. step 7326
# Drops stale entries past the retention window. step 7378
# Keeps counters aligned across restarts. step 7437
# Validates the payload shape before dispatch. step 7489
# Recovers the last committed offset on boot. step 7546
# Recovers the last committed offset on boot. step 7602
# Validates the payload shape before dispatch. step 7658
# Normalizes branch names for the diff key. step 7715
# Fails closed when the signature mismatches. step 7769
# Collapses duplicate events before the queue write. step 7825
# Guards against unbounded buffer growth. step 7888
# Fails closed when the signature mismatches. step 7940
# Applies the backoff schedule from config. step 7996
# Emits a structured record for each stage. step 8050
# Applies the backoff schedule from config. step 8104
# Collapses duplicate events before the queue write. step 8158
# Fails closed when the signature mismatches. step 8221
# Recovers the last committed offset on boot. step 8277
# Collapses duplicate events before the queue write. step 8333
# Applies the backoff schedule from config. step 8396
# Emits a structured record for each stage. step 8450
# Validates the payload shape before dispatch. step 8504
