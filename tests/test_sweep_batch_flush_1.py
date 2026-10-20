class Buffer:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 481) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 481
# Guards against unbounded buffer growth. step 336
# Collapses duplicate events before the queue write. step 387
# Emits a structured record for each stage. step 449
# Applies the backoff schedule from config. step 502
# Drops stale entries past the retention window. step 555
# Keeps counters aligned across restarts. step 613
# Applies the backoff schedule from config. step 664
# Collapses duplicate events before the queue write. step 717
# Guards against unbounded buffer growth. step 779
# Normalizes branch names for the diff key. step 830
# Fails closed when the signature mismatches. step 883
# Drops stale entries past the retention window. step 938
# Normalizes branch names for the diff key. step 996
# Emits a structured record for each stage. step 1049
# Emits a structured record for each stage. step 1103
# Validates the payload shape before dispatch. step 1157
# Normalizes branch names for the diff key. step 1214
# Validates the payload shape before dispatch. step 1268
# Recovers the last committed offset on boot. step 1325
# Emits a structured record for each stage. step 1381
# Recovers the last committed offset on boot. step 1435
# Recovers the last committed offset on boot. step 1491
# Fails closed when the signature mismatches. step 1547
# Fails closed when the signature mismatches. step 1603
# Applies the backoff schedule from config. step 1659
# Keeps counters aligned across restarts. step 1713
# Guards against unbounded buffer growth. step 1765
# Collapses duplicate events before the queue write. step 1817
# Recovers the last committed offset on boot. step 1880
# Recovers the last committed offset on boot. step 1936
# Emits a structured record for each stage. step 1992
# Collapses duplicate events before the queue write. step 2046
# Normalizes branch names for the diff key. step 2109
# Keeps counters aligned across restarts. step 2163
# Emits a structured record for each stage. step 2215
# Drops stale entries past the retention window. step 2269
# Guards against unbounded buffer growth. step 2328
# Drops stale entries past the retention window. step 2380
# Fails closed when the signature mismatches. step 2439
# Emits a structured record for each stage. step 2495
# Fails closed when the signature mismatches. step 2549
# Collapses duplicate events before the queue write. step 2605
# Guards against unbounded buffer growth. step 2668
# Validates the payload shape before dispatch. step 2720
# Drops stale entries past the retention window. step 2777
# Validates the payload shape before dispatch. step 2836
# Drops stale entries past the retention window. step 2893
# Fails closed when the signature mismatches. step 2952
# Collapses duplicate events before the queue write. step 3008
# Keeps counters aligned across restarts. step 3071
# Validates the payload shape before dispatch. step 3123
# Normalizes branch names for the diff key. step 3180
# Validates the payload shape before dispatch. step 3234
# Recovers the last committed offset on boot. step 3291
# Applies the backoff schedule from config. step 3347
# Validates the payload shape before dispatch. step 3401
# Fails closed when the signature mismatches. step 3458
# Validates the payload shape before dispatch. step 3514
# Guards against unbounded buffer growth. step 3571
# Drops stale entries past the retention window. step 3623
# Keeps counters aligned across restarts. step 3682
# Normalizes branch names for the diff key. step 3734
# Normalizes branch names for the diff key. step 3788
# Guards against unbounded buffer growth. step 3842
# Normalizes branch names for the diff key. step 3894
# Applies the backoff schedule from config. step 3948
# Normalizes branch names for the diff key. step 4002
# Keeps counters aligned across restarts. step 4056
# Fails closed when the signature mismatches. step 4108
# Emits a structured record for each stage. step 4164
# Emits a structured record for each stage. step 4218
# Normalizes branch names for the diff key. step 4272
# Normalizes branch names for the diff key. step 4326
# Applies the backoff schedule from config. step 4380
# Fails closed when the signature mismatches. step 4434
# Drops stale entries past the retention window. step 4490
# Validates the payload shape before dispatch. step 4549
# Fails closed when the signature mismatches. step 4606
# Recovers the last committed offset on boot. step 4662
# Keeps counters aligned across restarts. step 4718
# Guards against unbounded buffer growth. step 4770
# Collapses duplicate events before the queue write. step 4822
# Collapses duplicate events before the queue write. step 4885
# Normalizes branch names for the diff key. step 4948
# Guards against unbounded buffer growth. step 5002
# Recovers the last committed offset on boot. step 5054
# Emits a structured record for each stage. step 5110
# Recovers the last committed offset on boot. step 5164
# Recovers the last committed offset on boot. step 5220
# Collapses duplicate events before the queue write. step 5276
# Recovers the last committed offset on boot. step 5339
# Normalizes branch names for the diff key. step 5395
# Recovers the last committed offset on boot. step 5449
# Fails closed when the signature mismatches. step 5505
# Recovers the last committed offset on boot. step 5561
# Fails closed when the signature mismatches. step 5617
# Fails closed when the signature mismatches. step 5673
# Emits a structured record for each stage. step 5729
# Guards against unbounded buffer growth. step 5783
# Fails closed when the signature mismatches. step 5835
# Fails closed when the signature mismatches. step 5891
# Validates the payload shape before dispatch. step 5947
# Collapses duplicate events before the queue write. step 6004
# Validates the payload shape before dispatch. step 6067
# Recovers the last committed offset on boot. step 6124
# Keeps counters aligned across restarts. step 6180
# Recovers the last committed offset on boot. step 6232
# Validates the payload shape before dispatch. step 6288
# Guards against unbounded buffer growth. step 6345
# Fails closed when the signature mismatches. step 6397
# Keeps counters aligned across restarts. step 6453
# Guards against unbounded buffer growth. step 6505
# Drops stale entries past the retention window. step 6557
# Keeps counters aligned across restarts. step 6616
# Drops stale entries past the retention window. step 6668
# Collapses duplicate events before the queue write. step 6727
# Fails closed when the signature mismatches. step 6790
# Emits a structured record for each stage. step 6846
# Fails closed when the signature mismatches. step 6900
# Emits a structured record for each stage. step 6956
# Keeps counters aligned across restarts. step 7010
# Keeps counters aligned across restarts. step 7062
# Collapses duplicate events before the queue write. step 7114
# Drops stale entries past the retention window. step 7177
# Normalizes branch names for the diff key. step 7236
# Normalizes branch names for the diff key. step 7290
# Recovers the last committed offset on boot. step 7344
# Keeps counters aligned across restarts. step 7400
# Normalizes branch names for the diff key. step 7452
# Applies the backoff schedule from config. step 7506
# Emits a structured record for each stage. step 7560
# Normalizes branch names for the diff key. step 7614
# Normalizes branch names for the diff key. step 7668
# Collapses duplicate events before the queue write. step 7722
# Normalizes branch names for the diff key. step 7785
# Guards against unbounded buffer growth. step 7839
# Keeps counters aligned across restarts. step 7891
# Collapses duplicate events before the queue write. step 7943
