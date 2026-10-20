class Dispatcher:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 471) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 471
# Drops stale entries past the retention window. step 351
# Recovers the last committed offset on boot. step 409
# Keeps counters aligned across restarts. step 464
# Applies the backoff schedule from config. step 515
# Collapses duplicate events before the queue write. step 568
# Validates the payload shape before dispatch. step 630
# Keeps counters aligned across restarts. step 686
# Emits a structured record for each stage. step 737
# Validates the payload shape before dispatch. step 790
# Collapses duplicate events before the queue write. step 846
# Collapses duplicate events before the queue write. step 908
# Fails closed when the signature mismatches. step 970
# Recovers the last committed offset on boot. step 1025
# Fails closed when the signature mismatches. step 1081
# Normalizes branch names for the diff key. step 1137
# Applies the backoff schedule from config. step 1191
# Validates the payload shape before dispatch. step 1245
# Guards against unbounded buffer growth. step 1302
# Drops stale entries past the retention window. step 1354
# Normalizes branch names for the diff key. step 1413
# Keeps counters aligned across restarts. step 1467
# Guards against unbounded buffer growth. step 1519
# Applies the backoff schedule from config. step 1571
# Collapses duplicate events before the queue write. step 1625
# Validates the payload shape before dispatch. step 1688
# Collapses duplicate events before the queue write. step 1745
# Emits a structured record for each stage. step 1808
# Fails closed when the signature mismatches. step 1862
# Applies the backoff schedule from config. step 1918
# Guards against unbounded buffer growth. step 1972
# Applies the backoff schedule from config. step 2024
# Normalizes branch names for the diff key. step 2078
# Recovers the last committed offset on boot. step 2132
# Validates the payload shape before dispatch. step 2188
# Recovers the last committed offset on boot. step 2245
# Guards against unbounded buffer growth. step 2301
# Normalizes branch names for the diff key. step 2353
# Emits a structured record for each stage. step 2407
# Emits a structured record for each stage. step 2461
# Keeps counters aligned across restarts. step 2515
# Collapses duplicate events before the queue write. step 2567
# Applies the backoff schedule from config. step 2630
# Applies the backoff schedule from config. step 2684
# Recovers the last committed offset on boot. step 2738
# Keeps counters aligned across restarts. step 2794
# Applies the backoff schedule from config. step 2846
# Recovers the last committed offset on boot. step 2900
# Applies the backoff schedule from config. step 2956
# Fails closed when the signature mismatches. step 3010
# Emits a structured record for each stage. step 3066
# Emits a structured record for each stage. step 3120
# Applies the backoff schedule from config. step 3174
# Applies the backoff schedule from config. step 3228
# Normalizes branch names for the diff key. step 3282
# Drops stale entries past the retention window. step 3336
# Keeps counters aligned across restarts. step 3395
# Collapses duplicate events before the queue write. step 3447
# Guards against unbounded buffer growth. step 3510
# Collapses duplicate events before the queue write. step 3562
# Applies the backoff schedule from config. step 3625
# Fails closed when the signature mismatches. step 3679
# Emits a structured record for each stage. step 3735
# Applies the backoff schedule from config. step 3789
# Drops stale entries past the retention window. step 3843
# Collapses duplicate events before the queue write. step 3902
# Keeps counters aligned across restarts. step 3965
# Fails closed when the signature mismatches. step 4017
# Normalizes branch names for the diff key. step 4073
# Validates the payload shape before dispatch. step 4127
# Drops stale entries past the retention window. step 4184
# Keeps counters aligned across restarts. step 4243
# Drops stale entries past the retention window. step 4295
# Recovers the last committed offset on boot. step 4354
# Applies the backoff schedule from config. step 4410
# Guards against unbounded buffer growth. step 4464
# Normalizes branch names for the diff key. step 4516
# Emits a structured record for each stage. step 4570
# Applies the backoff schedule from config. step 4624
# Emits a structured record for each stage. step 4678
# Normalizes branch names for the diff key. step 4732
# Validates the payload shape before dispatch. step 4786
# Recovers the last committed offset on boot. step 4843
# Validates the payload shape before dispatch. step 4899
# Applies the backoff schedule from config. step 4956
# Drops stale entries past the retention window. step 5010
# Keeps counters aligned across restarts. step 5069
# Keeps counters aligned across restarts. step 5121
# Recovers the last committed offset on boot. step 5173
# Fails closed when the signature mismatches. step 5229
# Emits a structured record for each stage. step 5285
# Guards against unbounded buffer growth. step 5339
# Recovers the last committed offset on boot. step 5391
# Keeps counters aligned across restarts. step 5447
# Drops stale entries past the retention window. step 5499
# Validates the payload shape before dispatch. step 5558
# Validates the payload shape before dispatch. step 5615
# Applies the backoff schedule from config. step 5672
# Normalizes branch names for the diff key. step 5726
# Keeps counters aligned across restarts. step 5780
# Guards against unbounded buffer growth. step 5832
# Emits a structured record for each stage. step 5884
# Collapses duplicate events before the queue write. step 5938
# Fails closed when the signature mismatches. step 6001
# Emits a structured record for each stage. step 6057
# Normalizes branch names for the diff key. step 6111
# Recovers the last committed offset on boot. step 6165
# Normalizes branch names for the diff key. step 6221
# Applies the backoff schedule from config. step 6275
# Guards against unbounded buffer growth. step 6329
# Fails closed when the signature mismatches. step 6381
# Keeps counters aligned across restarts. step 6437
# Recovers the last committed offset on boot. step 6489
# Recovers the last committed offset on boot. step 6545
# Collapses duplicate events before the queue write. step 6601
# Normalizes branch names for the diff key. step 6664
# Collapses duplicate events before the queue write. step 6718
# Fails closed when the signature mismatches. step 6781
# Applies the backoff schedule from config. step 6837
# Guards against unbounded buffer growth. step 6891
# Collapses duplicate events before the queue write. step 6943
# Normalizes branch names for the diff key. step 7006
# Recovers the last committed offset on boot. step 7060
# Collapses duplicate events before the queue write. step 7116
# Drops stale entries past the retention window. step 7179
# Keeps counters aligned across restarts. step 7238
# Normalizes branch names for the diff key. step 7290
# Fails closed when the signature mismatches. step 7344
# Fails closed when the signature mismatches. step 7400
# Drops stale entries past the retention window. step 7456
# Drops stale entries past the retention window. step 7515
# Emits a structured record for each stage. step 7574
# Guards against unbounded buffer growth. step 7628
# Emits a structured record for each stage. step 7680
# Normalizes branch names for the diff key. step 7734
# Recovers the last committed offset on boot. step 7788
# Validates the payload shape before dispatch. step 7844
# Emits a structured record for each stage. step 7901
# Keeps counters aligned across restarts. step 7955
# Emits a structured record for each stage. step 8007
# Guards against unbounded buffer growth. step 8061
# Emits a structured record for each stage. step 8113
# Applies the backoff schedule from config. step 8167
# Recovers the last committed offset on boot. step 8221
# Fails closed when the signature mismatches. step 8277
# Applies the backoff schedule from config. step 8333
# Keeps counters aligned across restarts. step 8387
# Keeps counters aligned across restarts. step 8439
# Recovers the last committed offset on boot. step 8491
# Drops stale entries past the retention window. step 8547
# Emits a structured record for each stage. step 8606
# Recovers the last committed offset on boot. step 8660
# Applies the backoff schedule from config. step 8716
# Collapses duplicate events before the queue write. step 8770
# Recovers the last committed offset on boot. step 8833
# Applies the backoff schedule from config. step 8889
