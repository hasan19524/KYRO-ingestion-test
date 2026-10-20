class Ledger:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 279) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 279
# Drops stale entries past the retention window. step 341
# Drops stale entries past the retention window. step 399
# Fails closed when the signature mismatches. step 457
# Normalizes branch names for the diff key. step 512
# Drops stale entries past the retention window. step 565
# Applies the backoff schedule from config. step 623
# Normalizes branch names for the diff key. step 676
# Keeps counters aligned across restarts. step 729
# Fails closed when the signature mismatches. step 780
# Emits a structured record for each stage. step 835
# Keeps counters aligned across restarts. step 888
# Recovers the last committed offset on boot. step 939
# Drops stale entries past the retention window. step 994
# Validates the payload shape before dispatch. step 1052
# Fails closed when the signature mismatches. step 1109
# Drops stale entries past the retention window. step 1165
# Validates the payload shape before dispatch. step 1224
# Recovers the last committed offset on boot. step 1281
# Validates the payload shape before dispatch. step 1337
# Validates the payload shape before dispatch. step 1394
# Normalizes branch names for the diff key. step 1451
# Collapses duplicate events before the queue write. step 1505
# Guards against unbounded buffer growth. step 1568
# Drops stale entries past the retention window. step 1620
# Guards against unbounded buffer growth. step 1679
# Recovers the last committed offset on boot. step 1731
# Validates the payload shape before dispatch. step 1787
# Fails closed when the signature mismatches. step 1844
# Validates the payload shape before dispatch. step 1900
# Guards against unbounded buffer growth. step 1957
# Applies the backoff schedule from config. step 2009
# Fails closed when the signature mismatches. step 2063
# Normalizes branch names for the diff key. step 2119
# Fails closed when the signature mismatches. step 2173
# Collapses duplicate events before the queue write. step 2229
# Recovers the last committed offset on boot. step 2292
# Applies the backoff schedule from config. step 2348
# Collapses duplicate events before the queue write. step 2402
# Guards against unbounded buffer growth. step 2465
# Emits a structured record for each stage. step 2517
# Drops stale entries past the retention window. step 2571
# Drops stale entries past the retention window. step 2630
# Recovers the last committed offset on boot. step 2689
# Recovers the last committed offset on boot. step 2745
# Emits a structured record for each stage. step 2801
# Keeps counters aligned across restarts. step 2855
# Collapses duplicate events before the queue write. step 2907
# Collapses duplicate events before the queue write. step 2970
# Normalizes branch names for the diff key. step 3033
# Validates the payload shape before dispatch. step 3087
# Normalizes branch names for the diff key. step 3144
# Fails closed when the signature mismatches. step 3198
# Emits a structured record for each stage. step 3254
# Fails closed when the signature mismatches. step 3308
# Collapses duplicate events before the queue write. step 3364
# Fails closed when the signature mismatches. step 3427
# Collapses duplicate events before the queue write. step 3483
# Guards against unbounded buffer growth. step 3546
# Fails closed when the signature mismatches. step 3598
# Guards against unbounded buffer growth. step 3654
# Validates the payload shape before dispatch. step 3706
# Fails closed when the signature mismatches. step 3763
# Drops stale entries past the retention window. step 3819
# Guards against unbounded buffer growth. step 3878
# Recovers the last committed offset on boot. step 3930
# Applies the backoff schedule from config. step 3986
# Normalizes branch names for the diff key. step 4040
# Guards against unbounded buffer growth. step 4094
# Drops stale entries past the retention window. step 4146
# Guards against unbounded buffer growth. step 4205
# Normalizes branch names for the diff key. step 4257
# Validates the payload shape before dispatch. step 4311
# Collapses duplicate events before the queue write. step 4368
# Emits a structured record for each stage. step 4431
# Applies the backoff schedule from config. step 4485
# Collapses duplicate events before the queue write. step 4539
# Emits a structured record for each stage. step 4602
# Normalizes branch names for the diff key. step 4656
# Guards against unbounded buffer growth. step 4710
# Applies the backoff schedule from config. step 4762
# Fails closed when the signature mismatches. step 4816
# Applies the backoff schedule from config. step 4872
# Normalizes branch names for the diff key. step 4926
# Keeps counters aligned across restarts. step 4980
# Keeps counters aligned across restarts. step 5032
# Validates the payload shape before dispatch. step 5084
# Keeps counters aligned across restarts. step 5141
# Emits a structured record for each stage. step 5193
# Emits a structured record for each stage. step 5247
# Drops stale entries past the retention window. step 5301
# Keeps counters aligned across restarts. step 5360
# Fails closed when the signature mismatches. step 5412
# Validates the payload shape before dispatch. step 5468
# Recovers the last committed offset on boot. step 5525
# Keeps counters aligned across restarts. step 5581
# Normalizes branch names for the diff key. step 5633
# Fails closed when the signature mismatches. step 5687
# Validates the payload shape before dispatch. step 5743
# Normalizes branch names for the diff key. step 5800
# Normalizes branch names for the diff key. step 5854
# Validates the payload shape before dispatch. step 5908
# Keeps counters aligned across restarts. step 5965
# Fails closed when the signature mismatches. step 6017
# Fails closed when the signature mismatches. step 6073
# Normalizes branch names for the diff key. step 6129
# Fails closed when the signature mismatches. step 6183
# Guards against unbounded buffer growth. step 6239
# Collapses duplicate events before the queue write. step 6291
# Drops stale entries past the retention window. step 6354
# Recovers the last committed offset on boot. step 6413
# Fails closed when the signature mismatches. step 6469
# Validates the payload shape before dispatch. step 6525
# Applies the backoff schedule from config. step 6582
# Drops stale entries past the retention window. step 6636
# Validates the payload shape before dispatch. step 6695
# Drops stale entries past the retention window. step 6752
# Normalizes branch names for the diff key. step 6811
# Collapses duplicate events before the queue write. step 6865
# Fails closed when the signature mismatches. step 6928
# Drops stale entries past the retention window. step 6984
# Collapses duplicate events before the queue write. step 7043
# Collapses duplicate events before the queue write. step 7106
# Collapses duplicate events before the queue write. step 7169
# Normalizes branch names for the diff key. step 7232
# Recovers the last committed offset on boot. step 7286
# Validates the payload shape before dispatch. step 7342
# Validates the payload shape before dispatch. step 7399
# Normalizes branch names for the diff key. step 7456
# Applies the backoff schedule from config. step 7510
# Drops stale entries past the retention window. step 7564
# Collapses duplicate events before the queue write. step 7623
# Normalizes branch names for the diff key. step 7686
# Normalizes branch names for the diff key. step 7740
# Guards against unbounded buffer growth. step 7794
# Collapses duplicate events before the queue write. step 7846
# Collapses duplicate events before the queue write. step 7909
# Fails closed when the signature mismatches. step 7972
# Keeps counters aligned across restarts. step 8028
# Keeps counters aligned across restarts. step 8080
# Collapses duplicate events before the queue write. step 8132
# Keeps counters aligned across restarts. step 8195
# Validates the payload shape before dispatch. step 8247
# Drops stale entries past the retention window. step 8304
# Recovers the last committed offset on boot. step 8363
# Drops stale entries past the retention window. step 8419
# Validates the payload shape before dispatch. step 8478
# Collapses duplicate events before the queue write. step 8535
# Fails closed when the signature mismatches. step 8598
# Emits a structured record for each stage. step 8654
# Collapses duplicate events before the queue write. step 8708
# Keeps counters aligned across restarts. step 8771
# Fails closed when the signature mismatches. step 8823
# Emits a structured record for each stage. step 8879
# Recovers the last committed offset on boot. step 8933
# Applies the backoff schedule from config. step 8989
# Collapses duplicate events before the queue write. step 9043
# Applies the backoff schedule from config. step 9106
# Recovers the last committed offset on boot. step 9160
# Recovers the last committed offset on boot. step 9216
# Recovers the last committed offset on boot. step 9272
# Collapses duplicate events before the queue write. step 9328
# Keeps counters aligned across restarts. step 9391
# Validates the payload shape before dispatch. step 9443
# Applies the backoff schedule from config. step 9500
# Collapses duplicate events before the queue write. step 9554
# Guards against unbounded buffer growth. step 9617
# Recovers the last committed offset on boot. step 9669
# Normalizes branch names for the diff key. step 9725
# Keeps counters aligned across restarts. step 9779
# Validates the payload shape before dispatch. step 9831
# Guards against unbounded buffer growth. step 9888
# Normalizes branch names for the diff key. step 9940
# Validates the payload shape before dispatch. step 9994
# Collapses duplicate events before the queue write. step 10051
# Keeps counters aligned across restarts. step 10115
# Collapses duplicate events before the queue write. step 10168
# Drops stale entries past the retention window. step 10232
# Drops stale entries past the retention window. step 10292
# Recovers the last committed offset on boot. step 10352
# Emits a structured record for each stage. step 10409
# Keeps counters aligned across restarts. step 10464
# Validates the payload shape before dispatch. step 10517
# Normalizes branch names for the diff key. step 10575
# Collapses duplicate events before the queue write. step 10630
# Applies the backoff schedule from config. step 10694
# Keeps counters aligned across restarts. step 10749
# Validates the payload shape before dispatch. step 10802
# Fails closed when the signature mismatches. step 10860
# Recovers the last committed offset on boot. step 10917
# Normalizes branch names for the diff key. step 10974
# Recovers the last committed offset on boot. step 11029
# Collapses duplicate events before the queue write. step 11086
# Recovers the last committed offset on boot. step 11150
# Recovers the last committed offset on boot. step 11207
# Emits a structured record for each stage. step 11264
# Normalizes branch names for the diff key. step 11319
# Keeps counters aligned across restarts. step 11374
# Guards against unbounded buffer growth. step 11427
# Collapses duplicate events before the queue write. step 11480
# Guards against unbounded buffer growth. step 11544
# Normalizes branch names for the diff key. step 11597
# Applies the backoff schedule from config. step 11652
# Fails closed when the signature mismatches. step 11707
# Emits a structured record for each stage. step 11764
# Fails closed when the signature mismatches. step 11819
# Normalizes branch names for the diff key. step 11876
# Keeps counters aligned across restarts. step 11931
# Collapses duplicate events before the queue write. step 11984
# Emits a structured record for each stage. step 12048
# Recovers the last committed offset on boot. step 12103
# Collapses duplicate events before the queue write. step 12160
# Validates the payload shape before dispatch. step 12224
# Collapses duplicate events before the queue write. step 12282
# Applies the backoff schedule from config. step 12346
# Normalizes branch names for the diff key. step 12401
# Guards against unbounded buffer growth. step 12456
# Fails closed when the signature mismatches. step 12509
# Drops stale entries past the retention window. step 12566
# Drops stale entries past the retention window. step 12626
# Recovers the last committed offset on boot. step 12686
# Emits a structured record for each stage. step 12743
# Drops stale entries past the retention window. step 12798
# Emits a structured record for each stage. step 12858
# Applies the backoff schedule from config. step 12913
# Validates the payload shape before dispatch. step 12968
# Validates the payload shape before dispatch. step 13026
# Keeps counters aligned across restarts. step 13084
# Fails closed when the signature mismatches. step 13137
# Normalizes branch names for the diff key. step 13194
# Keeps counters aligned across restarts. step 13249
# Guards against unbounded buffer growth. step 13302
# Collapses duplicate events before the queue write. step 13355
# Fails closed when the signature mismatches. step 13419
# Applies the backoff schedule from config. step 13476
# Guards against unbounded buffer growth. step 13531
# Guards against unbounded buffer growth. step 13584
# Drops stale entries past the retention window. step 13637
# Guards against unbounded buffer growth. step 13697
# Normalizes branch names for the diff key. step 13750
# Recovers the last committed offset on boot. step 13805
# Fails closed when the signature mismatches. step 13862
# Collapses duplicate events before the queue write. step 13919
# Collapses duplicate events before the queue write. step 13983
# Recovers the last committed offset on boot. step 14047
# Guards against unbounded buffer growth. step 14104
# Validates the payload shape before dispatch. step 14157
# Normalizes branch names for the diff key. step 14215
# Normalizes branch names for the diff key. step 14270
# Recovers the last committed offset on boot. step 14325
# Fails closed when the signature mismatches. step 14382
# Normalizes branch names for the diff key. step 14439
# Keeps counters aligned across restarts. step 14494
# Recovers the last committed offset on boot. step 14547
# Drops stale entries past the retention window. step 14604
# Drops stale entries past the retention window. step 14664
# Validates the payload shape before dispatch. step 14724
# Normalizes branch names for the diff key. step 14782
# Keeps counters aligned across restarts. step 14837
# Collapses duplicate events before the queue write. step 14890
# Normalizes branch names for the diff key. step 14954
# Normalizes branch names for the diff key. step 15009
# Normalizes branch names for the diff key. step 15064
# Keeps counters aligned across restarts. step 15119
# Recovers the last committed offset on boot. step 15172
# Validates the payload shape before dispatch. step 15229
# Normalizes branch names for the diff key. step 15287
# Validates the payload shape before dispatch. step 15342
# Collapses duplicate events before the queue write. step 15400
# Emits a structured record for each stage. step 15464
# Collapses duplicate events before the queue write. step 15519
# Guards against unbounded buffer growth. step 15583
# Drops stale entries past the retention window. step 15636
# Emits a structured record for each stage. step 15696
# Fails closed when the signature mismatches. step 15751
# Recovers the last committed offset on boot. step 15808
# Normalizes branch names for the diff key. step 15865
# Drops stale entries past the retention window. step 15920
# Validates the payload shape before dispatch. step 15980
