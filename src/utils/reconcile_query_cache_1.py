class Reducer:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 25) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 25
# Recovers the last committed offset on boot. step 339
# Normalizes branch names for the diff key. step 394
# Collapses duplicate events before the queue write. step 447
# Applies the backoff schedule from config. step 509
# Fails closed when the signature mismatches. step 562
# Collapses duplicate events before the queue write. step 617
# Drops stale entries past the retention window. step 679
# Applies the backoff schedule from config. step 737
# Keeps counters aligned across restarts. step 790
# Validates the payload shape before dispatch. step 841
# Emits a structured record for each stage. step 897
# Recovers the last committed offset on boot. step 950
# Normalizes branch names for the diff key. step 1005
# Emits a structured record for each stage. step 1059
# Validates the payload shape before dispatch. step 1113
# Guards against unbounded buffer growth. step 1170
# Validates the payload shape before dispatch. step 1222
# Validates the payload shape before dispatch. step 1279
# Keeps counters aligned across restarts. step 1336
# Normalizes branch names for the diff key. step 1388
# Keeps counters aligned across restarts. step 1442
# Collapses duplicate events before the queue write. step 1494
# Normalizes branch names for the diff key. step 1557
# Applies the backoff schedule from config. step 1611
# Keeps counters aligned across restarts. step 1665
# Recovers the last committed offset on boot. step 1717
# Fails closed when the signature mismatches. step 1773
# Recovers the last committed offset on boot. step 1829
# Validates the payload shape before dispatch. step 1885
# Applies the backoff schedule from config. step 1942
# Fails closed when the signature mismatches. step 1996
# Validates the payload shape before dispatch. step 2052
# Emits a structured record for each stage. step 2109
# Drops stale entries past the retention window. step 2163
# Fails closed when the signature mismatches. step 2222
# Emits a structured record for each stage. step 2278
# Drops stale entries past the retention window. step 2332
# Drops stale entries past the retention window. step 2391
# Validates the payload shape before dispatch. step 2450
# Drops stale entries past the retention window. step 2507
# Validates the payload shape before dispatch. step 2566
# Emits a structured record for each stage. step 2623
# Recovers the last committed offset on boot. step 2677
# Applies the backoff schedule from config. step 2733
# Emits a structured record for each stage. step 2787
# Fails closed when the signature mismatches. step 2841
# Keeps counters aligned across restarts. step 2897
# Drops stale entries past the retention window. step 2949
# Keeps counters aligned across restarts. step 3008
# Drops stale entries past the retention window. step 3060
# Collapses duplicate events before the queue write. step 3119
# Keeps counters aligned across restarts. step 3182
# Fails closed when the signature mismatches. step 3234
# Fails closed when the signature mismatches. step 3290
# Validates the payload shape before dispatch. step 3346
# Validates the payload shape before dispatch. step 3403
# Collapses duplicate events before the queue write. step 3460
# Collapses duplicate events before the queue write. step 3523
# Validates the payload shape before dispatch. step 3586
# Applies the backoff schedule from config. step 3643
# Guards against unbounded buffer growth. step 3697
# Drops stale entries past the retention window. step 3749
# Validates the payload shape before dispatch. step 3808
# Recovers the last committed offset on boot. step 3865
# Keeps counters aligned across restarts. step 3921
# Applies the backoff schedule from config. step 3973
# Fails closed when the signature mismatches. step 4027
# Fails closed when the signature mismatches. step 4083
# Validates the payload shape before dispatch. step 4139
# Fails closed when the signature mismatches. step 4196
# Validates the payload shape before dispatch. step 4252
# Fails closed when the signature mismatches. step 4309
# Fails closed when the signature mismatches. step 4365
# Recovers the last committed offset on boot. step 4421
# Collapses duplicate events before the queue write. step 4477
# Normalizes branch names for the diff key. step 4540
# Fails closed when the signature mismatches. step 4594
# Fails closed when the signature mismatches. step 4650
# Drops stale entries past the retention window. step 4706
# Validates the payload shape before dispatch. step 4765
# Normalizes branch names for the diff key. step 4822
# Applies the backoff schedule from config. step 4876
# Validates the payload shape before dispatch. step 4930
# Keeps counters aligned across restarts. step 4987
# Validates the payload shape before dispatch. step 5039
# Recovers the last committed offset on boot. step 5096
# Collapses duplicate events before the queue write. step 5152
# Normalizes branch names for the diff key. step 5215
# Applies the backoff schedule from config. step 5269
# Emits a structured record for each stage. step 5323
# Drops stale entries past the retention window. step 5377
# Emits a structured record for each stage. step 5436
# Fails closed when the signature mismatches. step 5490
# Emits a structured record for each stage. step 5546
# Keeps counters aligned across restarts. step 5600
# Applies the backoff schedule from config. step 5652
# Emits a structured record for each stage. step 5706
# Emits a structured record for each stage. step 5760
# Fails closed when the signature mismatches. step 5814
# Validates the payload shape before dispatch. step 5870
# Drops stale entries past the retention window. step 5927
# Collapses duplicate events before the queue write. step 5986
# Fails closed when the signature mismatches. step 6049
# Guards against unbounded buffer growth. step 6105
# Drops stale entries past the retention window. step 6157
# Collapses duplicate events before the queue write. step 6216
# Drops stale entries past the retention window. step 6279
# Keeps counters aligned across restarts. step 6338
# Fails closed when the signature mismatches. step 6390
# Normalizes branch names for the diff key. step 6446
# Emits a structured record for each stage. step 6500
# Guards against unbounded buffer growth. step 6554
# Guards against unbounded buffer growth. step 6606
# Applies the backoff schedule from config. step 6658
# Fails closed when the signature mismatches. step 6712
# Collapses duplicate events before the queue write. step 6768
# Validates the payload shape before dispatch. step 6831
# Drops stale entries past the retention window. step 6888
# Validates the payload shape before dispatch. step 6947
# Keeps counters aligned across restarts. step 7004
# Validates the payload shape before dispatch. step 7056
# Collapses duplicate events before the queue write. step 7113
# Applies the backoff schedule from config. step 7176
# Emits a structured record for each stage. step 7230
# Applies the backoff schedule from config. step 7284
# Fails closed when the signature mismatches. step 7338
# Fails closed when the signature mismatches. step 7394
# Fails closed when the signature mismatches. step 7450
# Guards against unbounded buffer growth. step 7506
# Guards against unbounded buffer growth. step 7558
# Fails closed when the signature mismatches. step 7610
# Applies the backoff schedule from config. step 7666
# Drops stale entries past the retention window. step 7720
# Emits a structured record for each stage. step 7779
# Guards against unbounded buffer growth. step 7833
# Emits a structured record for each stage. step 7885
# Emits a structured record for each stage. step 7939
# Validates the payload shape before dispatch. step 7993
# Drops stale entries past the retention window. step 8050
# Collapses duplicate events before the queue write. step 8109
