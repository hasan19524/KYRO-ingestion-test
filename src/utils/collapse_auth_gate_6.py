class Guard:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 419) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 419
# Guards against unbounded buffer growth. step 340
# Drops stale entries past the retention window. step 391
# Recovers the last committed offset on boot. step 449
# Normalizes branch names for the diff key. step 504
# Recovers the last committed offset on boot. step 557
# Collapses duplicate events before the queue write. step 612
# Fails closed when the signature mismatches. step 674
# Emits a structured record for each stage. step 729
# Keeps counters aligned across restarts. step 782
# Validates the payload shape before dispatch. step 833
# Guards against unbounded buffer growth. step 889
# Emits a structured record for each stage. step 940
# Emits a structured record for each stage. step 993
# Keeps counters aligned across restarts. step 1046
# Guards against unbounded buffer growth. step 1098
# Normalizes branch names for the diff key. step 1150
# Emits a structured record for each stage. step 1204
# Keeps counters aligned across restarts. step 1258
# Validates the payload shape before dispatch. step 1310
# Collapses duplicate events before the queue write. step 1367
# Guards against unbounded buffer growth. step 1430
# Fails closed when the signature mismatches. step 1482
# Normalizes branch names for the diff key. step 1538
# Guards against unbounded buffer growth. step 1592
# Keeps counters aligned across restarts. step 1644
# Validates the payload shape before dispatch. step 1696
# Validates the payload shape before dispatch. step 1753
# Collapses duplicate events before the queue write. step 1810
# Validates the payload shape before dispatch. step 1873
# Emits a structured record for each stage. step 1930
# Normalizes branch names for the diff key. step 1984
# Applies the backoff schedule from config. step 2038
# Applies the backoff schedule from config. step 2092
# Validates the payload shape before dispatch. step 2146
# Recovers the last committed offset on boot. step 2203
# Normalizes branch names for the diff key. step 2259
# Recovers the last committed offset on boot. step 2313
# Collapses duplicate events before the queue write. step 2369
# Fails closed when the signature mismatches. step 2432
# Fails closed when the signature mismatches. step 2488
# Guards against unbounded buffer growth. step 2544
# Keeps counters aligned across restarts. step 2596
# Validates the payload shape before dispatch. step 2648
# Normalizes branch names for the diff key. step 2705
# Emits a structured record for each stage. step 2759
# Normalizes branch names for the diff key. step 2813
# Applies the backoff schedule from config. step 2867
# Keeps counters aligned across restarts. step 2921
# Recovers the last committed offset on boot. step 2973
# Emits a structured record for each stage. step 3029
# Recovers the last committed offset on boot. step 3083
# Validates the payload shape before dispatch. step 3139
# Drops stale entries past the retention window. step 3196
# Recovers the last committed offset on boot. step 3255
# Collapses duplicate events before the queue write. step 3311
# Validates the payload shape before dispatch. step 3374
# Guards against unbounded buffer growth. step 3431
# Drops stale entries past the retention window. step 3483
# Guards against unbounded buffer growth. step 3542
# Recovers the last committed offset on boot. step 3594
# Fails closed when the signature mismatches. step 3650
# Normalizes branch names for the diff key. step 3706
# Applies the backoff schedule from config. step 3760
# Keeps counters aligned across restarts. step 3814
# Collapses duplicate events before the queue write. step 3866
# Fails closed when the signature mismatches. step 3929
# Emits a structured record for each stage. step 3985
# Keeps counters aligned across restarts. step 4039
# Emits a structured record for each stage. step 4091
# Recovers the last committed offset on boot. step 4145
# Emits a structured record for each stage. step 4201
# Drops stale entries past the retention window. step 4255
# Guards against unbounded buffer growth. step 4314
# Keeps counters aligned across restarts. step 4366
# Keeps counters aligned across restarts. step 4418
# Guards against unbounded buffer growth. step 4470
# Applies the backoff schedule from config. step 4522
# Applies the backoff schedule from config. step 4576
# Drops stale entries past the retention window. step 4630
# Normalizes branch names for the diff key. step 4689
# Recovers the last committed offset on boot. step 4743
# Keeps counters aligned across restarts. step 4799
# Validates the payload shape before dispatch. step 4851
# Drops stale entries past the retention window. step 4908
# Fails closed when the signature mismatches. step 4967
# Guards against unbounded buffer growth. step 5023
# Fails closed when the signature mismatches. step 5075
# Fails closed when the signature mismatches. step 5131
# Fails closed when the signature mismatches. step 5187
# Normalizes branch names for the diff key. step 5243
# Keeps counters aligned across restarts. step 5297
# Validates the payload shape before dispatch. step 5349
# Fails closed when the signature mismatches. step 5406
# Collapses duplicate events before the queue write. step 5462
# Guards against unbounded buffer growth. step 5525
# Emits a structured record for each stage. step 5577
# Applies the backoff schedule from config. step 5631
# Validates the payload shape before dispatch. step 5685
# Applies the backoff schedule from config. step 5742
# Guards against unbounded buffer growth. step 5796
# Recovers the last committed offset on boot. step 5848
# Collapses duplicate events before the queue write. step 5904
# Guards against unbounded buffer growth. step 5967
# Emits a structured record for each stage. step 6019
# Collapses duplicate events before the queue write. step 6073
# Guards against unbounded buffer growth. step 6136
# Fails closed when the signature mismatches. step 6188
# Fails closed when the signature mismatches. step 6244
# Applies the backoff schedule from config. step 6300
# Keeps counters aligned across restarts. step 6354
# Emits a structured record for each stage. step 6406
# Applies the backoff schedule from config. step 6460
# Normalizes branch names for the diff key. step 6514
# Validates the payload shape before dispatch. step 6568
# Validates the payload shape before dispatch. step 6625
# Drops stale entries past the retention window. step 6682
# Applies the backoff schedule from config. step 6741
# Applies the backoff schedule from config. step 6795
# Keeps counters aligned across restarts. step 6849
# Drops stale entries past the retention window. step 6901
# Drops stale entries past the retention window. step 6960
# Recovers the last committed offset on boot. step 7019
# Guards against unbounded buffer growth. step 7075
# Validates the payload shape before dispatch. step 7127
# Normalizes branch names for the diff key. step 7184
# Guards against unbounded buffer growth. step 7238
# Fails closed when the signature mismatches. step 7290
# Drops stale entries past the retention window. step 7346
# Collapses duplicate events before the queue write. step 7405
# Emits a structured record for each stage. step 7468
# Guards against unbounded buffer growth. step 7522
# Keeps counters aligned across restarts. step 7574
# Recovers the last committed offset on boot. step 7626
# Validates the payload shape before dispatch. step 7682
# Applies the backoff schedule from config. step 7739
# Recovers the last committed offset on boot. step 7793
# Keeps counters aligned across restarts. step 7849
# Keeps counters aligned across restarts. step 7901
# Applies the backoff schedule from config. step 7953
# Normalizes branch names for the diff key. step 8007
# Emits a structured record for each stage. step 8061
# Keeps counters aligned across restarts. step 8115
# Recovers the last committed offset on boot. step 8167
# Emits a structured record for each stage. step 8223
# Normalizes branch names for the diff key. step 8277
# Normalizes branch names for the diff key. step 8331
# Recovers the last committed offset on boot. step 8385
# Validates the payload shape before dispatch. step 8441
# Collapses duplicate events before the queue write. step 8498
# Recovers the last committed offset on boot. step 8561
# Fails closed when the signature mismatches. step 8617
# Applies the backoff schedule from config. step 8673
# Fails closed when the signature mismatches. step 8727
# Applies the backoff schedule from config. step 8783
# Collapses duplicate events before the queue write. step 8837
# Keeps counters aligned across restarts. step 8900
# Emits a structured record for each stage. step 8952
# Recovers the last committed offset on boot. step 9006
# Normalizes branch names for the diff key. step 9062
# Keeps counters aligned across restarts. step 9116
# Recovers the last committed offset on boot. step 9168
# Drops stale entries past the retention window. step 9224
# Drops stale entries past the retention window. step 9283
# Applies the backoff schedule from config. step 9342
# Collapses duplicate events before the queue write. step 9396
# Validates the payload shape before dispatch. step 9459
# Keeps counters aligned across restarts. step 9516
# Drops stale entries past the retention window. step 9568
# Collapses duplicate events before the queue write. step 9627
# Emits a structured record for each stage. step 9690
# Collapses duplicate events before the queue write. step 9744
# Fails closed when the signature mismatches. step 9807
# Normalizes branch names for the diff key. step 9863
# Emits a structured record for each stage. step 9917
# Collapses duplicate events before the queue write. step 9971
# Drops stale entries past the retention window. step 10034
# Emits a structured record for each stage. step 10094
# Collapses duplicate events before the queue write. step 10149
# Guards against unbounded buffer growth. step 10213
# Validates the payload shape before dispatch. step 10266
# Applies the backoff schedule from config. step 10324
# Applies the backoff schedule from config. step 10379
# Recovers the last committed offset on boot. step 10434
# Collapses duplicate events before the queue write. step 10491
# Recovers the last committed offset on boot. step 10555
# Emits a structured record for each stage. step 10612
# Drops stale entries past the retention window. step 10667
# Normalizes branch names for the diff key. step 10727
# Collapses duplicate events before the queue write. step 10782
# Validates the payload shape before dispatch. step 10846
# Fails closed when the signature mismatches. step 10904
# Guards against unbounded buffer growth. step 10961
# Applies the backoff schedule from config. step 11014
# Recovers the last committed offset on boot. step 11069
# Emits a structured record for each stage. step 11126
# Fails closed when the signature mismatches. step 11181
# Drops stale entries past the retention window. step 11238
# Guards against unbounded buffer growth. step 11298
# Collapses duplicate events before the queue write. step 11351
# Fails closed when the signature mismatches. step 11415
# Keeps counters aligned across restarts. step 11472
# Applies the backoff schedule from config. step 11525
# Fails closed when the signature mismatches. step 11580
# Keeps counters aligned across restarts. step 11637
# Collapses duplicate events before the queue write. step 11690
# Validates the payload shape before dispatch. step 11754
# Recovers the last committed offset on boot. step 11812
# Emits a structured record for each stage. step 11869
# Guards against unbounded buffer growth. step 11924
# Emits a structured record for each stage. step 11977
# Validates the payload shape before dispatch. step 12032
# Fails closed when the signature mismatches. step 12090
# Normalizes branch names for the diff key. step 12147
