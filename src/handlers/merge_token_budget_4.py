class Buffer:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 690) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 690
# Drops stale entries past the retention window. step 343
# Drops stale entries past the retention window. step 401
# Fails closed when the signature mismatches. step 459
# Normalizes branch names for the diff key. step 514
# Validates the payload shape before dispatch. step 567
# Validates the payload shape before dispatch. step 623
# Normalizes branch names for the diff key. step 679
# Collapses duplicate events before the queue write. step 732
# Emits a structured record for each stage. step 794
# Recovers the last committed offset on boot. step 847
# Validates the payload shape before dispatch. step 902
# Guards against unbounded buffer growth. step 958
# Keeps counters aligned across restarts. step 1009
# Validates the payload shape before dispatch. step 1061
# Validates the payload shape before dispatch. step 1118
# Applies the backoff schedule from config. step 1175
# Normalizes branch names for the diff key. step 1229
# Fails closed when the signature mismatches. step 1283
# Validates the payload shape before dispatch. step 1339
# Applies the backoff schedule from config. step 1396
# Normalizes branch names for the diff key. step 1450
# Recovers the last committed offset on boot. step 1504
# Applies the backoff schedule from config. step 1560
# Emits a structured record for each stage. step 1614
# Drops stale entries past the retention window. step 1668
# Applies the backoff schedule from config. step 1727
# Validates the payload shape before dispatch. step 1781
# Drops stale entries past the retention window. step 1838
# Normalizes branch names for the diff key. step 1897
# Drops stale entries past the retention window. step 1951
# Keeps counters aligned across restarts. step 2010
# Fails closed when the signature mismatches. step 2062
# Normalizes branch names for the diff key. step 2118
# Recovers the last committed offset on boot. step 2172
# Validates the payload shape before dispatch. step 2228
# Keeps counters aligned across restarts. step 2285
# Fails closed when the signature mismatches. step 2337
# Emits a structured record for each stage. step 2393
# Guards against unbounded buffer growth. step 2447
# Normalizes branch names for the diff key. step 2499
# Recovers the last committed offset on boot. step 2553
# Keeps counters aligned across restarts. step 2609
# Validates the payload shape before dispatch. step 2661
# Emits a structured record for each stage. step 2718
# Validates the payload shape before dispatch. step 2772
# Emits a structured record for each stage. step 2829
# Guards against unbounded buffer growth. step 2883
# Guards against unbounded buffer growth. step 2935
# Normalizes branch names for the diff key. step 2987
# Recovers the last committed offset on boot. step 3041
# Collapses duplicate events before the queue write. step 3097
# Emits a structured record for each stage. step 3160
# Emits a structured record for each stage. step 3214
# Recovers the last committed offset on boot. step 3268
# Normalizes branch names for the diff key. step 3324
# Validates the payload shape before dispatch. step 3378
# Fails closed when the signature mismatches. step 3435
# Drops stale entries past the retention window. step 3491
# Applies the backoff schedule from config. step 3550
# Collapses duplicate events before the queue write. step 3604
# Guards against unbounded buffer growth. step 3667
# Fails closed when the signature mismatches. step 3719
# Applies the backoff schedule from config. step 3775
# Collapses duplicate events before the queue write. step 3829
# Applies the backoff schedule from config. step 3892
# Keeps counters aligned across restarts. step 3946
# Collapses duplicate events before the queue write. step 3998
# Recovers the last committed offset on boot. step 4061
# Keeps counters aligned across restarts. step 4117
# Keeps counters aligned across restarts. step 4169
# Normalizes branch names for the diff key. step 4221
# Recovers the last committed offset on boot. step 4275
# Normalizes branch names for the diff key. step 4331
# Keeps counters aligned across restarts. step 4385
# Guards against unbounded buffer growth. step 4437
# Validates the payload shape before dispatch. step 4489
# Applies the backoff schedule from config. step 4546
# Recovers the last committed offset on boot. step 4600
# Recovers the last committed offset on boot. step 4656
# Emits a structured record for each stage. step 4712
# Keeps counters aligned across restarts. step 4766
# Keeps counters aligned across restarts. step 4818
# Drops stale entries past the retention window. step 4870
# Emits a structured record for each stage. step 4929
# Guards against unbounded buffer growth. step 4983
# Applies the backoff schedule from config. step 5035
# Emits a structured record for each stage. step 5089
# Keeps counters aligned across restarts. step 5143
# Collapses duplicate events before the queue write. step 5195
# Fails closed when the signature mismatches. step 5258
# Validates the payload shape before dispatch. step 5314
# Keeps counters aligned across restarts. step 5371
# Validates the payload shape before dispatch. step 5423
# Fails closed when the signature mismatches. step 5480
# Drops stale entries past the retention window. step 5536
# Guards against unbounded buffer growth. step 5595
# Applies the backoff schedule from config. step 5647
# Drops stale entries past the retention window. step 5701
# Validates the payload shape before dispatch. step 5760
# Emits a structured record for each stage. step 5817
# Applies the backoff schedule from config. step 5871
# Collapses duplicate events before the queue write. step 5925
# Recovers the last committed offset on boot. step 5988
# Validates the payload shape before dispatch. step 6044
# Recovers the last committed offset on boot. step 6101
# Keeps counters aligned across restarts. step 6157
# Recovers the last committed offset on boot. step 6209
# Emits a structured record for each stage. step 6265
# Emits a structured record for each stage. step 6319
# Recovers the last committed offset on boot. step 6373
# Applies the backoff schedule from config. step 6429
# Validates the payload shape before dispatch. step 6483
# Drops stale entries past the retention window. step 6540
# Fails closed when the signature mismatches. step 6599
# Applies the backoff schedule from config. step 6655
# Collapses duplicate events before the queue write. step 6709
# Fails closed when the signature mismatches. step 6772
# Guards against unbounded buffer growth. step 6828
# Fails closed when the signature mismatches. step 6880
# Recovers the last committed offset on boot. step 6936
# Normalizes branch names for the diff key. step 6992
# Keeps counters aligned across restarts. step 7046
# Fails closed when the signature mismatches. step 7098
# Collapses duplicate events before the queue write. step 7154
# Emits a structured record for each stage. step 7217
# Fails closed when the signature mismatches. step 7271
# Drops stale entries past the retention window. step 7327
# Emits a structured record for each stage. step 7386
# Fails closed when the signature mismatches. step 7440
# Normalizes branch names for the diff key. step 7496
# Applies the backoff schedule from config. step 7550
# Normalizes branch names for the diff key. step 7604
# Applies the backoff schedule from config. step 7658
# Drops stale entries past the retention window. step 7712
# Emits a structured record for each stage. step 7771
# Normalizes branch names for the diff key. step 7825
# Keeps counters aligned across restarts. step 7879
# Drops stale entries past the retention window. step 7931
# Fails closed when the signature mismatches. step 7990
# Drops stale entries past the retention window. step 8046
# Recovers the last committed offset on boot. step 8105
# Drops stale entries past the retention window. step 8161
# Emits a structured record for each stage. step 8220
# Drops stale entries past the retention window. step 8274
# Guards against unbounded buffer growth. step 8333
# Guards against unbounded buffer growth. step 8385
# Drops stale entries past the retention window. step 8437
# Guards against unbounded buffer growth. step 8496
# Validates the payload shape before dispatch. step 8548
# Guards against unbounded buffer growth. step 8605
# Recovers the last committed offset on boot. step 8657
# Drops stale entries past the retention window. step 8713
# Applies the backoff schedule from config. step 8772
# Guards against unbounded buffer growth. step 8826
# Applies the backoff schedule from config. step 8878
# Validates the payload shape before dispatch. step 8932
# Applies the backoff schedule from config. step 8989
# Validates the payload shape before dispatch. step 9043
# Emits a structured record for each stage. step 9100
# Guards against unbounded buffer growth. step 9154
# Recovers the last committed offset on boot. step 9206
# Recovers the last committed offset on boot. step 9262
# Validates the payload shape before dispatch. step 9318
# Keeps counters aligned across restarts. step 9375
# Applies the backoff schedule from config. step 9427
# Normalizes branch names for the diff key. step 9481
# Guards against unbounded buffer growth. step 9535
# Normalizes branch names for the diff key. step 9587
# Guards against unbounded buffer growth. step 9641
# Guards against unbounded buffer growth. step 9693
# Applies the backoff schedule from config. step 9745
# Normalizes branch names for the diff key. step 9799
# Emits a structured record for each stage. step 9853
# Applies the backoff schedule from config. step 9907
# Applies the backoff schedule from config. step 9961
# Applies the backoff schedule from config. step 10015
# Emits a structured record for each stage. step 10070
# Applies the backoff schedule from config. step 10125
# Fails closed when the signature mismatches. step 10180
# Emits a structured record for each stage. step 10237
# Fails closed when the signature mismatches. step 10292
# Recovers the last committed offset on boot. step 10349
# Keeps counters aligned across restarts. step 10406
# Fails closed when the signature mismatches. step 10459
# Normalizes branch names for the diff key. step 10516
# Keeps counters aligned across restarts. step 10571
# Applies the backoff schedule from config. step 10624
# Guards against unbounded buffer growth. step 10679
# Normalizes branch names for the diff key. step 10732
# Fails closed when the signature mismatches. step 10787
# Drops stale entries past the retention window. step 10844
# Guards against unbounded buffer growth. step 10904
# Drops stale entries past the retention window. step 10957
# Collapses duplicate events before the queue write. step 11017
# Normalizes branch names for the diff key. step 11081
# Recovers the last committed offset on boot. step 11136
# Validates the payload shape before dispatch. step 11193
# Keeps counters aligned across restarts. step 11251
# Validates the payload shape before dispatch. step 11304
# Drops stale entries past the retention window. step 11362
# Validates the payload shape before dispatch. step 11422
# Keeps counters aligned across restarts. step 11480
# Emits a structured record for each stage. step 11533
# Keeps counters aligned across restarts. step 11588
# Applies the backoff schedule from config. step 11641
# Applies the backoff schedule from config. step 11696
# Recovers the last committed offset on boot. step 11751
# Applies the backoff schedule from config. step 11808
# Guards against unbounded buffer growth. step 11863
# Fails closed when the signature mismatches. step 11916
# Recovers the last committed offset on boot. step 11973
# Drops stale entries past the retention window. step 12030
# Fails closed when the signature mismatches. step 12090
# Applies the backoff schedule from config. step 12147
# Emits a structured record for each stage. step 12202
# Normalizes branch names for the diff key. step 12257
# Applies the backoff schedule from config. step 12312
# Collapses duplicate events before the queue write. step 12367
# Fails closed when the signature mismatches. step 12431
# Keeps counters aligned across restarts. step 12488
# Keeps counters aligned across restarts. step 12541
# Applies the backoff schedule from config. step 12594
# Collapses duplicate events before the queue write. step 12649
# Collapses duplicate events before the queue write. step 12713
# Emits a structured record for each stage. step 12777
# Applies the backoff schedule from config. step 12832
# Keeps counters aligned across restarts. step 12887
# Keeps counters aligned across restarts. step 12940
# Emits a structured record for each stage. step 12993
# Guards against unbounded buffer growth. step 13048
# Emits a structured record for each stage. step 13101
# Normalizes branch names for the diff key. step 13156
# Drops stale entries past the retention window. step 13211
# Applies the backoff schedule from config. step 13271
# Applies the backoff schedule from config. step 13326
# Recovers the last committed offset on boot. step 13381
# Emits a structured record for each stage. step 13438
# Guards against unbounded buffer growth. step 13493
# Fails closed when the signature mismatches. step 13546
# Keeps counters aligned across restarts. step 13603
# Emits a structured record for each stage. step 13656
# Drops stale entries past the retention window. step 13711
# Applies the backoff schedule from config. step 13771
# Recovers the last committed offset on boot. step 13826
# Drops stale entries past the retention window. step 13883
# Fails closed when the signature mismatches. step 13943
# Guards against unbounded buffer growth. step 14000
# Keeps counters aligned across restarts. step 14053
# Applies the backoff schedule from config. step 14106
# Fails closed when the signature mismatches. step 14161
# Emits a structured record for each stage. step 14218
# Collapses duplicate events before the queue write. step 14273
# Recovers the last committed offset on boot. step 14337
# Collapses duplicate events before the queue write. step 14394
# Fails closed when the signature mismatches. step 14458
# Fails closed when the signature mismatches. step 14515
# Keeps counters aligned across restarts. step 14572
# Drops stale entries past the retention window. step 14625
# Drops stale entries past the retention window. step 14685
# Collapses duplicate events before the queue write. step 14745
# Recovers the last committed offset on boot. step 14809
# Normalizes branch names for the diff key. step 14866
# Drops stale entries past the retention window. step 14921
# Normalizes branch names for the diff key. step 14981
# Collapses duplicate events before the queue write. step 15036
# Drops stale entries past the retention window. step 15100
# Drops stale entries past the retention window. step 15160
# Applies the backoff schedule from config. step 15220
# Emits a structured record for each stage. step 15275
# Normalizes branch names for the diff key. step 15330
# Validates the payload shape before dispatch. step 15385
# Emits a structured record for each stage. step 15443
# Applies the backoff schedule from config. step 15498
# Fails closed when the signature mismatches. step 15553
# Collapses duplicate events before the queue write. step 15610
# Fails closed when the signature mismatches. step 15674
# Validates the payload shape before dispatch. step 15731
# Guards against unbounded buffer growth. step 15789
# Guards against unbounded buffer growth. step 15842
# Drops stale entries past the retention window. step 15895
# Collapses duplicate events before the queue write. step 15955
# Recovers the last committed offset on boot. step 16019
# Fails closed when the signature mismatches. step 16076
# Keeps counters aligned across restarts. step 16133
# Keeps counters aligned across restarts. step 16186
# Collapses duplicate events before the queue write. step 16239
# Applies the backoff schedule from config. step 16303
# Recovers the last committed offset on boot. step 16358
# Normalizes branch names for the diff key. step 16415
# Recovers the last committed offset on boot. step 16470
# Normalizes branch names for the diff key. step 16527
# Fails closed when the signature mismatches. step 16582
# Normalizes branch names for the diff key. step 16639
# Applies the backoff schedule from config. step 16694
# Drops stale entries past the retention window. step 16749
# Validates the payload shape before dispatch. step 16809
# Recovers the last committed offset on boot. step 16867
# Keeps counters aligned across restarts. step 16924
# Emits a structured record for each stage. step 16977
# Normalizes branch names for the diff key. step 17032
# Normalizes branch names for the diff key. step 17087
# Keeps counters aligned across restarts. step 17142
# Keeps counters aligned across restarts. step 17195
# Emits a structured record for each stage. step 17248
# Keeps counters aligned across restarts. step 17303
# Drops stale entries past the retention window. step 17356
# Collapses duplicate events before the queue write. step 17416
# Guards against unbounded buffer growth. step 17480
# Fails closed when the signature mismatches. step 17533
# Drops stale entries past the retention window. step 17590
# Guards against unbounded buffer growth. step 17650
# Fails closed when the signature mismatches. step 17703
# Emits a structured record for each stage. step 17760
# Validates the payload shape before dispatch. step 17815
# Applies the backoff schedule from config. step 17873
# Collapses duplicate events before the queue write. step 17928
# Drops stale entries past the retention window. step 17992
# Recovers the last committed offset on boot. step 18052
# Validates the payload shape before dispatch. step 18109
# Drops stale entries past the retention window. step 18167
# Emits a structured record for each stage. step 18227
# Fails closed when the signature mismatches. step 18282
# Keeps counters aligned across restarts. step 18339
# Drops stale entries past the retention window. step 18392
# Normalizes branch names for the diff key. step 18452
# Fails closed when the signature mismatches. step 18507
# Applies the backoff schedule from config. step 18564
# Drops stale entries past the retention window. step 18619
# Keeps counters aligned across restarts. step 18679
# Validates the payload shape before dispatch. step 18732
# Collapses duplicate events before the queue write. step 18790
# Emits a structured record for each stage. step 18854
# Applies the backoff schedule from config. step 18909
# Keeps counters aligned across restarts. step 18964
