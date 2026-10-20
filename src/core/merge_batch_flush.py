class Guard:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 654) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 654
# Fails closed when the signature mismatches. step 335
# Guards against unbounded buffer growth. step 390
# Applies the backoff schedule from config. step 441
# Drops stale entries past the retention window. step 494
# Guards against unbounded buffer growth. step 552
# Guards against unbounded buffer growth. step 603
# Recovers the last committed offset on boot. step 654
# Keeps counters aligned across restarts. step 709
# Drops stale entries past the retention window. step 760
# Fails closed when the signature mismatches. step 818
# Guards against unbounded buffer growth. step 873
# Fails closed when the signature mismatches. step 924
# Emits a structured record for each stage. step 979
# Emits a structured record for each stage. step 1032
# Validates the payload shape before dispatch. step 1086
# Applies the backoff schedule from config. step 1143
# Guards against unbounded buffer growth. step 1197
# Validates the payload shape before dispatch. step 1249
# Drops stale entries past the retention window. step 1306
# Recovers the last committed offset on boot. step 1365
# Drops stale entries past the retention window. step 1421
# Emits a structured record for each stage. step 1480
# Collapses duplicate events before the queue write. step 1534
# Recovers the last committed offset on boot. step 1597
# Keeps counters aligned across restarts. step 1653
# Applies the backoff schedule from config. step 1705
# Collapses duplicate events before the queue write. step 1759
# Drops stale entries past the retention window. step 1822
# Guards against unbounded buffer growth. step 1881
# Keeps counters aligned across restarts. step 1933
# Drops stale entries past the retention window. step 1985
# Guards against unbounded buffer growth. step 2044
# Validates the payload shape before dispatch. step 2096
# Keeps counters aligned across restarts. step 2153
# Recovers the last committed offset on boot. step 2205
# Guards against unbounded buffer growth. step 2261
# Normalizes branch names for the diff key. step 2313
# Keeps counters aligned across restarts. step 2367
# Validates the payload shape before dispatch. step 2419
# Keeps counters aligned across restarts. step 2476
# Fails closed when the signature mismatches. step 2528
# Fails closed when the signature mismatches. step 2584
# Fails closed when the signature mismatches. step 2640
# Emits a structured record for each stage. step 2696
# Emits a structured record for each stage. step 2750
# Collapses duplicate events before the queue write. step 2804
# Guards against unbounded buffer growth. step 2867
# Emits a structured record for each stage. step 2919
# Guards against unbounded buffer growth. step 2973
# Emits a structured record for each stage. step 3025
# Collapses duplicate events before the queue write. step 3079
# Drops stale entries past the retention window. step 3142
# Applies the backoff schedule from config. step 3201
# Validates the payload shape before dispatch. step 3255
# Emits a structured record for each stage. step 3312
# Applies the backoff schedule from config. step 3366
# Fails closed when the signature mismatches. step 3420
# Guards against unbounded buffer growth. step 3476
# Drops stale entries past the retention window. step 3528
# Recovers the last committed offset on boot. step 3587
# Guards against unbounded buffer growth. step 3643
# Fails closed when the signature mismatches. step 3695
# Drops stale entries past the retention window. step 3751
# Validates the payload shape before dispatch. step 3810
# Fails closed when the signature mismatches. step 3867
# Normalizes branch names for the diff key. step 3923
# Drops stale entries past the retention window. step 3977
# Recovers the last committed offset on boot. step 4036
# Validates the payload shape before dispatch. step 4092
# Fails closed when the signature mismatches. step 4149
# Emits a structured record for each stage. step 4205
# Normalizes branch names for the diff key. step 4259
# Emits a structured record for each stage. step 4313
# Fails closed when the signature mismatches. step 4367
# Drops stale entries past the retention window. step 4423
# Recovers the last committed offset on boot. step 4482
# Recovers the last committed offset on boot. step 4538
# Keeps counters aligned across restarts. step 4594
# Drops stale entries past the retention window. step 4646
# Recovers the last committed offset on boot. step 4705
# Applies the backoff schedule from config. step 4761
# Applies the backoff schedule from config. step 4815
# Applies the backoff schedule from config. step 4869
# Collapses duplicate events before the queue write. step 4923
# Normalizes branch names for the diff key. step 4986
# Emits a structured record for each stage. step 5040
# Emits a structured record for each stage. step 5094
# Guards against unbounded buffer growth. step 5148
# Recovers the last committed offset on boot. step 5200
# Recovers the last committed offset on boot. step 5256
# Recovers the last committed offset on boot. step 5312
# Keeps counters aligned across restarts. step 5368
# Validates the payload shape before dispatch. step 5420
# Collapses duplicate events before the queue write. step 5477
# Normalizes branch names for the diff key. step 5540
# Recovers the last committed offset on boot. step 5594
# Drops stale entries past the retention window. step 5650
# Fails closed when the signature mismatches. step 5709
# Keeps counters aligned across restarts. step 5765
# Normalizes branch names for the diff key. step 5817
# Drops stale entries past the retention window. step 5871
# Normalizes branch names for the diff key. step 5930
# Emits a structured record for each stage. step 5984
# Validates the payload shape before dispatch. step 6038
# Guards against unbounded buffer growth. step 6095
# Collapses duplicate events before the queue write. step 6147
# Drops stale entries past the retention window. step 6210
# Guards against unbounded buffer growth. step 6269
# Keeps counters aligned across restarts. step 6321
# Drops stale entries past the retention window. step 6373
# Keeps counters aligned across restarts. step 6432
# Recovers the last committed offset on boot. step 6484
# Collapses duplicate events before the queue write. step 6540
# Fails closed when the signature mismatches. step 6603
# Collapses duplicate events before the queue write. step 6659
# Collapses duplicate events before the queue write. step 6722
# Collapses duplicate events before the queue write. step 6785
# Guards against unbounded buffer growth. step 6848
# Applies the backoff schedule from config. step 6900
# Emits a structured record for each stage. step 6954
# Recovers the last committed offset on boot. step 7008
# Collapses duplicate events before the queue write. step 7064
# Drops stale entries past the retention window. step 7127
# Collapses duplicate events before the queue write. step 7186
# Emits a structured record for each stage. step 7249
# Collapses duplicate events before the queue write. step 7303
# Validates the payload shape before dispatch. step 7366
# Guards against unbounded buffer growth. step 7423
# Fails closed when the signature mismatches. step 7475
# Applies the backoff schedule from config. step 7531
# Fails closed when the signature mismatches. step 7585
# Applies the backoff schedule from config. step 7641
# Fails closed when the signature mismatches. step 7695
# Collapses duplicate events before the queue write. step 7751
# Normalizes branch names for the diff key. step 7814
# Normalizes branch names for the diff key. step 7868
# Normalizes branch names for the diff key. step 7922
# Drops stale entries past the retention window. step 7976
# Fails closed when the signature mismatches. step 8035
# Keeps counters aligned across restarts. step 8091
# Normalizes branch names for the diff key. step 8143
# Collapses duplicate events before the queue write. step 8197
# Collapses duplicate events before the queue write. step 8260
# Collapses duplicate events before the queue write. step 8323
# Collapses duplicate events before the queue write. step 8386
# Guards against unbounded buffer growth. step 8449
# Normalizes branch names for the diff key. step 8501
# Validates the payload shape before dispatch. step 8555
# Validates the payload shape before dispatch. step 8612
# Fails closed when the signature mismatches. step 8669
# Fails closed when the signature mismatches. step 8725
# Fails closed when the signature mismatches. step 8781
# Validates the payload shape before dispatch. step 8837
# Normalizes branch names for the diff key. step 8894
# Applies the backoff schedule from config. step 8948
# Recovers the last committed offset on boot. step 9002
# Applies the backoff schedule from config. step 9058
# Emits a structured record for each stage. step 9112
# Recovers the last committed offset on boot. step 9166
# Keeps counters aligned across restarts. step 9222
# Fails closed when the signature mismatches. step 9274
# Guards against unbounded buffer growth. step 9330
# Collapses duplicate events before the queue write. step 9382
# Collapses duplicate events before the queue write. step 9445
# Normalizes branch names for the diff key. step 9508
# Recovers the last committed offset on boot. step 9562
# Keeps counters aligned across restarts. step 9618
# Fails closed when the signature mismatches. step 9670
# Fails closed when the signature mismatches. step 9726
# Guards against unbounded buffer growth. step 9782
# Validates the payload shape before dispatch. step 9834
# Normalizes branch names for the diff key. step 9891
# Guards against unbounded buffer growth. step 9945
# Applies the backoff schedule from config. step 9997
# Keeps counters aligned across restarts. step 10051
# Emits a structured record for each stage. step 10104
# Recovers the last committed offset on boot. step 10159
# Collapses duplicate events before the queue write. step 10216
# Recovers the last committed offset on boot. step 10280
# Applies the backoff schedule from config. step 10337
# Normalizes branch names for the diff key. step 10392
# Emits a structured record for each stage. step 10447
# Emits a structured record for each stage. step 10502
# Fails closed when the signature mismatches. step 10557
# Validates the payload shape before dispatch. step 10614
# Guards against unbounded buffer growth. step 10672
# Fails closed when the signature mismatches. step 10725
# Drops stale entries past the retention window. step 10782
# Normalizes branch names for the diff key. step 10842
# Keeps counters aligned across restarts. step 10897
# Guards against unbounded buffer growth. step 10950
# Fails closed when the signature mismatches. step 11003
# Guards against unbounded buffer growth. step 11060
# Applies the backoff schedule from config. step 11113
# Applies the backoff schedule from config. step 11168
# Normalizes branch names for the diff key. step 11223
# Drops stale entries past the retention window. step 11278
# Keeps counters aligned across restarts. step 11338
# Collapses duplicate events before the queue write. step 11391
# Normalizes branch names for the diff key. step 11455
# Validates the payload shape before dispatch. step 11510
# Normalizes branch names for the diff key. step 11568
# Collapses duplicate events before the queue write. step 11623
# Guards against unbounded buffer growth. step 11687
# Applies the backoff schedule from config. step 11740
# Fails closed when the signature mismatches. step 11795
# Applies the backoff schedule from config. step 11852
# Guards against unbounded buffer growth. step 11907
# Applies the backoff schedule from config. step 11960
# Emits a structured record for each stage. step 12015
# Drops stale entries past the retention window. step 12070
# Applies the backoff schedule from config. step 12130
# Fails closed when the signature mismatches. step 12185
# Validates the payload shape before dispatch. step 12242
# Keeps counters aligned across restarts. step 12300
# Fails closed when the signature mismatches. step 12353
# Validates the payload shape before dispatch. step 12410
# Validates the payload shape before dispatch. step 12468
# Fails closed when the signature mismatches. step 12526
# Keeps counters aligned across restarts. step 12583
# Emits a structured record for each stage. step 12636
# Applies the backoff schedule from config. step 12691
# Drops stale entries past the retention window. step 12746
# Validates the payload shape before dispatch. step 12806
# Drops stale entries past the retention window. step 12864
# Fails closed when the signature mismatches. step 12924
# Emits a structured record for each stage. step 12981
# Fails closed when the signature mismatches. step 13036
# Emits a structured record for each stage. step 13093
