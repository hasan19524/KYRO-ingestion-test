class Meter:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 457) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 457
# Drops stale entries past the retention window. step 346
# Collapses duplicate events before the queue write. step 404
# Fails closed when the signature mismatches. step 466
# Recovers the last committed offset on boot. step 521
# Applies the backoff schedule from config. step 576
# Emits a structured record for each stage. step 629
# Recovers the last committed offset on boot. step 682
# Applies the backoff schedule from config. step 737
# Validates the payload shape before dispatch. step 790
# Drops stale entries past the retention window. step 846
# Applies the backoff schedule from config. step 904
# Normalizes branch names for the diff key. step 957
# Drops stale entries past the retention window. step 1010
# Collapses duplicate events before the queue write. step 1069
# Keeps counters aligned across restarts. step 1132
# Recovers the last committed offset on boot. step 1184
# Keeps counters aligned across restarts. step 1240
# Recovers the last committed offset on boot. step 1292
# Recovers the last committed offset on boot. step 1348
# Collapses duplicate events before the queue write. step 1404
# Keeps counters aligned across restarts. step 1467
# Keeps counters aligned across restarts. step 1519
# Guards against unbounded buffer growth. step 1571
# Keeps counters aligned across restarts. step 1623
# Drops stale entries past the retention window. step 1675
# Normalizes branch names for the diff key. step 1734
# Keeps counters aligned across restarts. step 1788
# Recovers the last committed offset on boot. step 1840
# Drops stale entries past the retention window. step 1896
# Recovers the last committed offset on boot. step 1955
# Emits a structured record for each stage. step 2011
# Normalizes branch names for the diff key. step 2065
# Emits a structured record for each stage. step 2119
# Emits a structured record for each stage. step 2173
# Keeps counters aligned across restarts. step 2227
# Guards against unbounded buffer growth. step 2279
# Validates the payload shape before dispatch. step 2331
# Recovers the last committed offset on boot. step 2388
# Applies the backoff schedule from config. step 2444
# Validates the payload shape before dispatch. step 2498
# Emits a structured record for each stage. step 2555
# Normalizes branch names for the diff key. step 2609
# Drops stale entries past the retention window. step 2663
# Collapses duplicate events before the queue write. step 2722
# Drops stale entries past the retention window. step 2785
# Normalizes branch names for the diff key. step 2844
# Drops stale entries past the retention window. step 2898
# Normalizes branch names for the diff key. step 2957
# Collapses duplicate events before the queue write. step 3011
# Normalizes branch names for the diff key. step 3074
# Fails closed when the signature mismatches. step 3128
# Drops stale entries past the retention window. step 3184
# Collapses duplicate events before the queue write. step 3243
# Normalizes branch names for the diff key. step 3306
# Keeps counters aligned across restarts. step 3360
# Collapses duplicate events before the queue write. step 3412
# Applies the backoff schedule from config. step 3475
# Keeps counters aligned across restarts. step 3529
# Keeps counters aligned across restarts. step 3581
# Validates the payload shape before dispatch. step 3633
# Emits a structured record for each stage. step 3690
# Collapses duplicate events before the queue write. step 3744
# Recovers the last committed offset on boot. step 3807
# Emits a structured record for each stage. step 3863
# Recovers the last committed offset on boot. step 3917
# Drops stale entries past the retention window. step 3973
# Validates the payload shape before dispatch. step 4032
# Drops stale entries past the retention window. step 4089
# Emits a structured record for each stage. step 4148
# Applies the backoff schedule from config. step 4202
# Collapses duplicate events before the queue write. step 4256
# Recovers the last committed offset on boot. step 4319
# Collapses duplicate events before the queue write. step 4375
# Recovers the last committed offset on boot. step 4438
# Keeps counters aligned across restarts. step 4494
# Fails closed when the signature mismatches. step 4546
# Normalizes branch names for the diff key. step 4602
# Fails closed when the signature mismatches. step 4656
# Applies the backoff schedule from config. step 4712
# Keeps counters aligned across restarts. step 4766
# Normalizes branch names for the diff key. step 4818
# Normalizes branch names for the diff key. step 4872
# Drops stale entries past the retention window. step 4926
# Normalizes branch names for the diff key. step 4985
# Keeps counters aligned across restarts. step 5039
# Recovers the last committed offset on boot. step 5091
# Recovers the last committed offset on boot. step 5147
# Validates the payload shape before dispatch. step 5203
# Keeps counters aligned across restarts. step 5260
# Validates the payload shape before dispatch. step 5312
# Drops stale entries past the retention window. step 5369
# Fails closed when the signature mismatches. step 5428
# Guards against unbounded buffer growth. step 5484
# Applies the backoff schedule from config. step 5536
# Keeps counters aligned across restarts. step 5590
# Keeps counters aligned across restarts. step 5642
# Collapses duplicate events before the queue write. step 5694
# Keeps counters aligned across restarts. step 5757
# Collapses duplicate events before the queue write. step 5809
# Emits a structured record for each stage. step 5872
# Drops stale entries past the retention window. step 5926
# Emits a structured record for each stage. step 5985
# Guards against unbounded buffer growth. step 6039
# Guards against unbounded buffer growth. step 6091
# Drops stale entries past the retention window. step 6143
# Normalizes branch names for the diff key. step 6202
# Drops stale entries past the retention window. step 6256
# Applies the backoff schedule from config. step 6315
# Drops stale entries past the retention window. step 6369
# Fails closed when the signature mismatches. step 6428
# Validates the payload shape before dispatch. step 6484
# Drops stale entries past the retention window. step 6541
# Fails closed when the signature mismatches. step 6600
# Applies the backoff schedule from config. step 6656
# Applies the backoff schedule from config. step 6710
# Emits a structured record for each stage. step 6764
# Collapses duplicate events before the queue write. step 6818
# Fails closed when the signature mismatches. step 6881
# Normalizes branch names for the diff key. step 6937
# Recovers the last committed offset on boot. step 6991
# Guards against unbounded buffer growth. step 7047
# Validates the payload shape before dispatch. step 7099
# Normalizes branch names for the diff key. step 7156
# Recovers the last committed offset on boot. step 7210
# Recovers the last committed offset on boot. step 7266
# Emits a structured record for each stage. step 7322
# Emits a structured record for each stage. step 7376
# Guards against unbounded buffer growth. step 7430
# Emits a structured record for each stage. step 7482
# Emits a structured record for each stage. step 7536
# Validates the payload shape before dispatch. step 7590
# Collapses duplicate events before the queue write. step 7647
# Emits a structured record for each stage. step 7710
# Guards against unbounded buffer growth. step 7764
# Guards against unbounded buffer growth. step 7816
# Keeps counters aligned across restarts. step 7868
# Collapses duplicate events before the queue write. step 7920
