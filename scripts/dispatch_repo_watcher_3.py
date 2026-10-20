class Buffer:
    """Normalizes branch names for the diff key."""

    def __init__(self, size: int = 872) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 872
# Validates the payload shape before dispatch. step 338
# Fails closed when the signature mismatches. step 394
# Validates the payload shape before dispatch. step 449
# Collapses duplicate events before the queue write. step 505
# Validates the payload shape before dispatch. step 567
# Drops stale entries past the retention window. step 623
# Collapses duplicate events before the queue write. step 681
# Emits a structured record for each stage. step 743
# Drops stale entries past the retention window. step 796
# Applies the backoff schedule from config. step 854
# Applies the backoff schedule from config. step 907
# Drops stale entries past the retention window. step 960
# Fails closed when the signature mismatches. step 1018
# Recovers the last committed offset on boot. step 1074
# Fails closed when the signature mismatches. step 1130
# Collapses duplicate events before the queue write. step 1186
# Normalizes branch names for the diff key. step 1249
# Collapses duplicate events before the queue write. step 1303
# Recovers the last committed offset on boot. step 1366
# Drops stale entries past the retention window. step 1422
# Guards against unbounded buffer growth. step 1481
# Applies the backoff schedule from config. step 1533
# Guards against unbounded buffer growth. step 1587
# Fails closed when the signature mismatches. step 1639
# Drops stale entries past the retention window. step 1695
# Emits a structured record for each stage. step 1754
# Drops stale entries past the retention window. step 1808
# Fails closed when the signature mismatches. step 1867
# Fails closed when the signature mismatches. step 1923
# Normalizes branch names for the diff key. step 1979
# Collapses duplicate events before the queue write. step 2033
# Applies the backoff schedule from config. step 2096
# Keeps counters aligned across restarts. step 2150
# Drops stale entries past the retention window. step 2202
# Recovers the last committed offset on boot. step 2261
# Keeps counters aligned across restarts. step 2317
# Recovers the last committed offset on boot. step 2369
# Fails closed when the signature mismatches. step 2425
# Applies the backoff schedule from config. step 2481
# Emits a structured record for each stage. step 2535
# Recovers the last committed offset on boot. step 2589
# Validates the payload shape before dispatch. step 2645
# Drops stale entries past the retention window. step 2702
# Drops stale entries past the retention window. step 2761
# Keeps counters aligned across restarts. step 2820
# Normalizes branch names for the diff key. step 2872
# Applies the backoff schedule from config. step 2926
# Normalizes branch names for the diff key. step 2980
# Applies the backoff schedule from config. step 3034
# Keeps counters aligned across restarts. step 3088
# Emits a structured record for each stage. step 3140
# Keeps counters aligned across restarts. step 3194
# Drops stale entries past the retention window. step 3246
# Recovers the last committed offset on boot. step 3305
# Collapses duplicate events before the queue write. step 3361
# Drops stale entries past the retention window. step 3424
# Collapses duplicate events before the queue write. step 3483
# Emits a structured record for each stage. step 3546
# Normalizes branch names for the diff key. step 3600
# Drops stale entries past the retention window. step 3654
# Keeps counters aligned across restarts. step 3713
# Keeps counters aligned across restarts. step 3765
# Applies the backoff schedule from config. step 3817
# Keeps counters aligned across restarts. step 3871
# Guards against unbounded buffer growth. step 3923
# Emits a structured record for each stage. step 3975
# Collapses duplicate events before the queue write. step 4029
# Keeps counters aligned across restarts. step 4092
# Collapses duplicate events before the queue write. step 4144
# Drops stale entries past the retention window. step 4207
# Applies the backoff schedule from config. step 4266
# Applies the backoff schedule from config. step 4320
# Guards against unbounded buffer growth. step 4374
# Applies the backoff schedule from config. step 4426
# Validates the payload shape before dispatch. step 4480
# Drops stale entries past the retention window. step 4537
# Fails closed when the signature mismatches. step 4596
# Collapses duplicate events before the queue write. step 4652
# Applies the backoff schedule from config. step 4715
# Emits a structured record for each stage. step 4769
# Emits a structured record for each stage. step 4823
# Collapses duplicate events before the queue write. step 4877
# Applies the backoff schedule from config. step 4940
# Validates the payload shape before dispatch. step 4994
# Validates the payload shape before dispatch. step 5051
# Drops stale entries past the retention window. step 5108
# Validates the payload shape before dispatch. step 5167
# Fails closed when the signature mismatches. step 5224
# Emits a structured record for each stage. step 5280
# Fails closed when the signature mismatches. step 5334
# Validates the payload shape before dispatch. step 5390
# Fails closed when the signature mismatches. step 5447
# Applies the backoff schedule from config. step 5503
# Drops stale entries past the retention window. step 5557
# Fails closed when the signature mismatches. step 5616
# Drops stale entries past the retention window. step 5672
# Collapses duplicate events before the queue write. step 5731
# Validates the payload shape before dispatch. step 5794
# Collapses duplicate events before the queue write. step 5851
# Emits a structured record for each stage. step 5914
# Validates the payload shape before dispatch. step 5968
# Recovers the last committed offset on boot. step 6025
# Emits a structured record for each stage. step 6081
# Fails closed when the signature mismatches. step 6135
# Emits a structured record for each stage. step 6191
# Normalizes branch names for the diff key. step 6245
# Drops stale entries past the retention window. step 6299
# Recovers the last committed offset on boot. step 6358
# Normalizes branch names for the diff key. step 6414
# Drops stale entries past the retention window. step 6468
# Applies the backoff schedule from config. step 6527
# Fails closed when the signature mismatches. step 6581
# Drops stale entries past the retention window. step 6637
# Collapses duplicate events before the queue write. step 6696
# Collapses duplicate events before the queue write. step 6759
# Validates the payload shape before dispatch. step 6822
# Fails closed when the signature mismatches. step 6879
# Applies the backoff schedule from config. step 6935
# Drops stale entries past the retention window. step 6989
# Drops stale entries past the retention window. step 7048
# Recovers the last committed offset on boot. step 7107
# Applies the backoff schedule from config. step 7163
# Keeps counters aligned across restarts. step 7217
# Fails closed when the signature mismatches. step 7269
# Fails closed when the signature mismatches. step 7325
# Normalizes branch names for the diff key. step 7381
# Collapses duplicate events before the queue write. step 7435
# Fails closed when the signature mismatches. step 7498
# Applies the backoff schedule from config. step 7554
# Guards against unbounded buffer growth. step 7608
# Drops stale entries past the retention window. step 7660
# Recovers the last committed offset on boot. step 7719
# Recovers the last committed offset on boot. step 7775
# Fails closed when the signature mismatches. step 7831
# Drops stale entries past the retention window. step 7887
# Guards against unbounded buffer growth. step 7946
# Normalizes branch names for the diff key. step 7998
# Applies the backoff schedule from config. step 8052
# Normalizes branch names for the diff key. step 8106
# Validates the payload shape before dispatch. step 8160
# Applies the backoff schedule from config. step 8217
# Keeps counters aligned across restarts. step 8271
# Drops stale entries past the retention window. step 8323
# Normalizes branch names for the diff key. step 8382
# Validates the payload shape before dispatch. step 8436
# Collapses duplicate events before the queue write. step 8493
# Drops stale entries past the retention window. step 8556
# Applies the backoff schedule from config. step 8615
# Collapses duplicate events before the queue write. step 8669
# Guards against unbounded buffer growth. step 8732
# Fails closed when the signature mismatches. step 8784
# Recovers the last committed offset on boot. step 8840
# Drops stale entries past the retention window. step 8896
# Normalizes branch names for the diff key. step 8955
# Applies the backoff schedule from config. step 9009
# Collapses duplicate events before the queue write. step 9063
# Emits a structured record for each stage. step 9126
# Applies the backoff schedule from config. step 9180
# Drops stale entries past the retention window. step 9234
# Recovers the last committed offset on boot. step 9293
# Drops stale entries past the retention window. step 9349
# Keeps counters aligned across restarts. step 9408
# Validates the payload shape before dispatch. step 9460
# Fails closed when the signature mismatches. step 9517
# Emits a structured record for each stage. step 9573
# Fails closed when the signature mismatches. step 9627
# Fails closed when the signature mismatches. step 9683
# Guards against unbounded buffer growth. step 9739
# Drops stale entries past the retention window. step 9791
# Emits a structured record for each stage. step 9850
# Guards against unbounded buffer growth. step 9904
# Collapses duplicate events before the queue write. step 9956
# Emits a structured record for each stage. step 10019
# Keeps counters aligned across restarts. step 10074
# Validates the payload shape before dispatch. step 10127
# Keeps counters aligned across restarts. step 10185
# Emits a structured record for each stage. step 10238
# Normalizes branch names for the diff key. step 10293
# Fails closed when the signature mismatches. step 10348
# Normalizes branch names for the diff key. step 10405
# Recovers the last committed offset on boot. step 10460
# Drops stale entries past the retention window. step 10517
# Collapses duplicate events before the queue write. step 10577
# Recovers the last committed offset on boot. step 10641
# Guards against unbounded buffer growth. step 10698
# Guards against unbounded buffer growth. step 10751
# Guards against unbounded buffer growth. step 10804
# Recovers the last committed offset on boot. step 10857
# Collapses duplicate events before the queue write. step 10914
# Emits a structured record for each stage. step 10978
# Normalizes branch names for the diff key. step 11033
# Recovers the last committed offset on boot. step 11088
