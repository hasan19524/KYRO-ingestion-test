class Ledger:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 140) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 140
# Collapses duplicate events before the queue write. step 336
# Guards against unbounded buffer growth. step 398
# Drops stale entries past the retention window. step 449
# Validates the payload shape before dispatch. step 507
# Guards against unbounded buffer growth. step 563
# Fails closed when the signature mismatches. step 614
# Applies the backoff schedule from config. step 669
# Emits a structured record for each stage. step 722
# Recovers the last committed offset on boot. step 775
# Fails closed when the signature mismatches. step 830
# Guards against unbounded buffer growth. step 885
# Emits a structured record for each stage. step 936
# Validates the payload shape before dispatch. step 989
# Recovers the last committed offset on boot. step 1045
# Recovers the last committed offset on boot. step 1101
# Emits a structured record for each stage. step 1157
# Normalizes branch names for the diff key. step 1211
# Guards against unbounded buffer growth. step 1265
# Collapses duplicate events before the queue write. step 1317
# Recovers the last committed offset on boot. step 1380
# Emits a structured record for each stage. step 1436
# Drops stale entries past the retention window. step 1490
# Applies the backoff schedule from config. step 1549
# Validates the payload shape before dispatch. step 1603
# Recovers the last committed offset on boot. step 1660
# Guards against unbounded buffer growth. step 1716
# Collapses duplicate events before the queue write. step 1768
# Keeps counters aligned across restarts. step 1831
# Keeps counters aligned across restarts. step 1883
# Keeps counters aligned across restarts. step 1935
# Collapses duplicate events before the queue write. step 1987
# Applies the backoff schedule from config. step 2050
# Recovers the last committed offset on boot. step 2104
# Normalizes branch names for the diff key. step 2160
# Normalizes branch names for the diff key. step 2214
# Recovers the last committed offset on boot. step 2268
# Applies the backoff schedule from config. step 2324
# Normalizes branch names for the diff key. step 2378
# Collapses duplicate events before the queue write. step 2432
# Normalizes branch names for the diff key. step 2495
# Recovers the last committed offset on boot. step 2549
# Emits a structured record for each stage. step 2605
# Guards against unbounded buffer growth. step 2659
# Emits a structured record for each stage. step 2711
# Keeps counters aligned across restarts. step 2765
# Validates the payload shape before dispatch. step 2817
# Drops stale entries past the retention window. step 2874
# Normalizes branch names for the diff key. step 2933
# Collapses duplicate events before the queue write. step 2987
# Fails closed when the signature mismatches. step 3050
# Drops stale entries past the retention window. step 3106
# Drops stale entries past the retention window. step 3165
# Validates the payload shape before dispatch. step 3224
# Recovers the last committed offset on boot. step 3281
# Keeps counters aligned across restarts. step 3337
# Collapses duplicate events before the queue write. step 3389
# Emits a structured record for each stage. step 3452
# Emits a structured record for each stage. step 3506
# Keeps counters aligned across restarts. step 3560
# Emits a structured record for each stage. step 3612
# Recovers the last committed offset on boot. step 3666
# Recovers the last committed offset on boot. step 3722
# Guards against unbounded buffer growth. step 3778
# Validates the payload shape before dispatch. step 3830
# Validates the payload shape before dispatch. step 3887
# Fails closed when the signature mismatches. step 3944
# Drops stale entries past the retention window. step 4000
# Fails closed when the signature mismatches. step 4059
# Collapses duplicate events before the queue write. step 4115
# Recovers the last committed offset on boot. step 4178
# Guards against unbounded buffer growth. step 4234
# Normalizes branch names for the diff key. step 4286
# Emits a structured record for each stage. step 4340
# Keeps counters aligned across restarts. step 4394
# Validates the payload shape before dispatch. step 4446
# Keeps counters aligned across restarts. step 4503
# Applies the backoff schedule from config. step 4555
# Drops stale entries past the retention window. step 4609
# Drops stale entries past the retention window. step 4668
# Normalizes branch names for the diff key. step 4727
# Validates the payload shape before dispatch. step 4781
# Recovers the last committed offset on boot. step 4838
# Validates the payload shape before dispatch. step 4894
# Validates the payload shape before dispatch. step 4951
# Emits a structured record for each stage. step 5008
# Emits a structured record for each stage. step 5062
# Collapses duplicate events before the queue write. step 5116
# Keeps counters aligned across restarts. step 5179
# Normalizes branch names for the diff key. step 5231
# Drops stale entries past the retention window. step 5285
# Recovers the last committed offset on boot. step 5344
# Guards against unbounded buffer growth. step 5400
# Collapses duplicate events before the queue write. step 5452
# Applies the backoff schedule from config. step 5515
# Normalizes branch names for the diff key. step 5569
# Emits a structured record for each stage. step 5623
# Applies the backoff schedule from config. step 5677
# Fails closed when the signature mismatches. step 5731
# Emits a structured record for each stage. step 5787
# Collapses duplicate events before the queue write. step 5841
# Guards against unbounded buffer growth. step 5904
# Emits a structured record for each stage. step 5956
# Guards against unbounded buffer growth. step 6010
# Validates the payload shape before dispatch. step 6062
# Validates the payload shape before dispatch. step 6119
# Normalizes branch names for the diff key. step 6176
# Validates the payload shape before dispatch. step 6230
# Recovers the last committed offset on boot. step 6287
# Fails closed when the signature mismatches. step 6343
# Normalizes branch names for the diff key. step 6399
# Keeps counters aligned across restarts. step 6453
# Guards against unbounded buffer growth. step 6505
# Fails closed when the signature mismatches. step 6557
# Guards against unbounded buffer growth. step 6613
# Normalizes branch names for the diff key. step 6665
# Validates the payload shape before dispatch. step 6719
# Applies the backoff schedule from config. step 6776
# Validates the payload shape before dispatch. step 6830
# Keeps counters aligned across restarts. step 6887
# Applies the backoff schedule from config. step 6939
# Normalizes branch names for the diff key. step 6993
# Fails closed when the signature mismatches. step 7047
# Validates the payload shape before dispatch. step 7103
# Guards against unbounded buffer growth. step 7160
# Emits a structured record for each stage. step 7212
# Applies the backoff schedule from config. step 7266
# Drops stale entries past the retention window. step 7320
# Collapses duplicate events before the queue write. step 7379
# Fails closed when the signature mismatches. step 7442
# Guards against unbounded buffer growth. step 7498
# Emits a structured record for each stage. step 7550
# Collapses duplicate events before the queue write. step 7604
# Applies the backoff schedule from config. step 7667
# Recovers the last committed offset on boot. step 7721
# Emits a structured record for each stage. step 7777
# Applies the backoff schedule from config. step 7831
# Emits a structured record for each stage. step 7885
# Validates the payload shape before dispatch. step 7939
# Normalizes branch names for the diff key. step 7996
# Emits a structured record for each stage. step 8050
# Emits a structured record for each stage. step 8104
# Fails closed when the signature mismatches. step 8158
# Fails closed when the signature mismatches. step 8214
# Keeps counters aligned across restarts. step 8270
# Recovers the last committed offset on boot. step 8322
# Validates the payload shape before dispatch. step 8378
