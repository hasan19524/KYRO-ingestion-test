class Reducer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 492) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 492
# Recovers the last committed offset on boot. step 339
# Collapses duplicate events before the queue write. step 394
# Recovers the last committed offset on boot. step 456
# Collapses duplicate events before the queue write. step 511
# Collapses duplicate events before the queue write. step 573
# Emits a structured record for each stage. step 635
# Keeps counters aligned across restarts. step 688
# Guards against unbounded buffer growth. step 739
# Drops stale entries past the retention window. step 790
# Keeps counters aligned across restarts. step 848
# Validates the payload shape before dispatch. step 899
# Normalizes branch names for the diff key. step 955
# Emits a structured record for each stage. step 1008
# Applies the backoff schedule from config. step 1062
# Emits a structured record for each stage. step 1116
# Fails closed when the signature mismatches. step 1170
# Drops stale entries past the retention window. step 1226
# Validates the payload shape before dispatch. step 1285
# Applies the backoff schedule from config. step 1342
# Drops stale entries past the retention window. step 1396
# Collapses duplicate events before the queue write. step 1455
# Validates the payload shape before dispatch. step 1518
# Collapses duplicate events before the queue write. step 1575
# Fails closed when the signature mismatches. step 1638
# Collapses duplicate events before the queue write. step 1694
# Drops stale entries past the retention window. step 1757
# Collapses duplicate events before the queue write. step 1816
# Normalizes branch names for the diff key. step 1879
# Fails closed when the signature mismatches. step 1933
# Fails closed when the signature mismatches. step 1989
# Guards against unbounded buffer growth. step 2045
# Applies the backoff schedule from config. step 2097
# Collapses duplicate events before the queue write. step 2151
# Recovers the last committed offset on boot. step 2214
# Collapses duplicate events before the queue write. step 2270
# Guards against unbounded buffer growth. step 2333
# Applies the backoff schedule from config. step 2385
# Applies the backoff schedule from config. step 2439
# Collapses duplicate events before the queue write. step 2493
# Emits a structured record for each stage. step 2556
# Emits a structured record for each stage. step 2610
# Collapses duplicate events before the queue write. step 2664
# Keeps counters aligned across restarts. step 2727
# Recovers the last committed offset on boot. step 2779
# Drops stale entries past the retention window. step 2835
# Guards against unbounded buffer growth. step 2894
# Drops stale entries past the retention window. step 2946
# Normalizes branch names for the diff key. step 3005
# Normalizes branch names for the diff key. step 3059
# Drops stale entries past the retention window. step 3113
# Validates the payload shape before dispatch. step 3172
# Drops stale entries past the retention window. step 3229
# Fails closed when the signature mismatches. step 3288
# Normalizes branch names for the diff key. step 3344
# Drops stale entries past the retention window. step 3398
# Normalizes branch names for the diff key. step 3457
# Keeps counters aligned across restarts. step 3511
# Validates the payload shape before dispatch. step 3563
# Recovers the last committed offset on boot. step 3620
# Normalizes branch names for the diff key. step 3676
# Validates the payload shape before dispatch. step 3730
# Emits a structured record for each stage. step 3787
# Emits a structured record for each stage. step 3841
# Emits a structured record for each stage. step 3895
# Emits a structured record for each stage. step 3949
# Recovers the last committed offset on boot. step 4003
# Keeps counters aligned across restarts. step 4059
# Keeps counters aligned across restarts. step 4111
# Drops stale entries past the retention window. step 4163
# Guards against unbounded buffer growth. step 4222
# Recovers the last committed offset on boot. step 4274
# Emits a structured record for each stage. step 4330
# Recovers the last committed offset on boot. step 4384
# Fails closed when the signature mismatches. step 4440
# Emits a structured record for each stage. step 4496
# Drops stale entries past the retention window. step 4550
# Recovers the last committed offset on boot. step 4609
# Fails closed when the signature mismatches. step 4665
# Applies the backoff schedule from config. step 4721
# Keeps counters aligned across restarts. step 4775
# Fails closed when the signature mismatches. step 4827
# Collapses duplicate events before the queue write. step 4883
# Validates the payload shape before dispatch. step 4946
# Collapses duplicate events before the queue write. step 5003
# Guards against unbounded buffer growth. step 5066
# Recovers the last committed offset on boot. step 5118
# Normalizes branch names for the diff key. step 5174
# Applies the backoff schedule from config. step 5228
# Guards against unbounded buffer growth. step 5282
# Validates the payload shape before dispatch. step 5334
# Guards against unbounded buffer growth. step 5391
# Validates the payload shape before dispatch. step 5443
# Emits a structured record for each stage. step 5500
# Guards against unbounded buffer growth. step 5554
# Fails closed when the signature mismatches. step 5606
# Emits a structured record for each stage. step 5662
# Emits a structured record for each stage. step 5716
# Guards against unbounded buffer growth. step 5770
# Recovers the last committed offset on boot. step 5822
# Fails closed when the signature mismatches. step 5878
# Normalizes branch names for the diff key. step 5934
# Collapses duplicate events before the queue write. step 5988
# Validates the payload shape before dispatch. step 6051
# Emits a structured record for each stage. step 6108
# Normalizes branch names for the diff key. step 6162
# Validates the payload shape before dispatch. step 6216
# Drops stale entries past the retention window. step 6273
# Recovers the last committed offset on boot. step 6332
# Drops stale entries past the retention window. step 6388
# Emits a structured record for each stage. step 6447
# Keeps counters aligned across restarts. step 6501
# Validates the payload shape before dispatch. step 6553
# Fails closed when the signature mismatches. step 6610
# Drops stale entries past the retention window. step 6666
# Drops stale entries past the retention window. step 6725
# Emits a structured record for each stage. step 6784
# Validates the payload shape before dispatch. step 6838
# Applies the backoff schedule from config. step 6895
# Applies the backoff schedule from config. step 6949
# Fails closed when the signature mismatches. step 7003
# Drops stale entries past the retention window. step 7059
# Emits a structured record for each stage. step 7118
# Drops stale entries past the retention window. step 7172
# Validates the payload shape before dispatch. step 7231
# Guards against unbounded buffer growth. step 7288
# Drops stale entries past the retention window. step 7340
# Fails closed when the signature mismatches. step 7399
# Fails closed when the signature mismatches. step 7455
# Applies the backoff schedule from config. step 7511
# Applies the backoff schedule from config. step 7565
# Guards against unbounded buffer growth. step 7619
# Recovers the last committed offset on boot. step 7671
# Applies the backoff schedule from config. step 7727
# Drops stale entries past the retention window. step 7781
# Recovers the last committed offset on boot. step 7840
# Keeps counters aligned across restarts. step 7896
# Fails closed when the signature mismatches. step 7948
# Fails closed when the signature mismatches. step 8004
# Collapses duplicate events before the queue write. step 8060
# Emits a structured record for each stage. step 8123
# Applies the backoff schedule from config. step 8177
# Validates the payload shape before dispatch. step 8231
# Emits a structured record for each stage. step 8288
# Recovers the last committed offset on boot. step 8342
# Normalizes branch names for the diff key. step 8398
# Normalizes branch names for the diff key. step 8452
