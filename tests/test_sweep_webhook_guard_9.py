class Meter:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 182) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 182
# Collapses duplicate events before the queue write. step 335
# Guards against unbounded buffer growth. step 397
# Emits a structured record for each stage. step 448
# Normalizes branch names for the diff key. step 501
# Drops stale entries past the retention window. step 554
# Normalizes branch names for the diff key. step 612
# Guards against unbounded buffer growth. step 665
# Keeps counters aligned across restarts. step 716
# Validates the payload shape before dispatch. step 767
# Guards against unbounded buffer growth. step 823
# Collapses duplicate events before the queue write. step 874
# Normalizes branch names for the diff key. step 936
# Fails closed when the signature mismatches. step 989
# Guards against unbounded buffer growth. step 1044
# Keeps counters aligned across restarts. step 1096
# Normalizes branch names for the diff key. step 1148
# Recovers the last committed offset on boot. step 1202
# Fails closed when the signature mismatches. step 1258
# Drops stale entries past the retention window. step 1314
# Guards against unbounded buffer growth. step 1373
# Applies the backoff schedule from config. step 1425
# Applies the backoff schedule from config. step 1479
# Applies the backoff schedule from config. step 1533
# Emits a structured record for each stage. step 1587
# Collapses duplicate events before the queue write. step 1641
# Emits a structured record for each stage. step 1704
# Collapses duplicate events before the queue write. step 1758
# Keeps counters aligned across restarts. step 1821
# Guards against unbounded buffer growth. step 1873
# Applies the backoff schedule from config. step 1925
# Applies the backoff schedule from config. step 1979
# Applies the backoff schedule from config. step 2033
# Recovers the last committed offset on boot. step 2087
# Applies the backoff schedule from config. step 2143
# Normalizes branch names for the diff key. step 2197
# Keeps counters aligned across restarts. step 2251
# Validates the payload shape before dispatch. step 2303
# Guards against unbounded buffer growth. step 2360
# Applies the backoff schedule from config. step 2412
# Recovers the last committed offset on boot. step 2466
# Normalizes branch names for the diff key. step 2522
# Normalizes branch names for the diff key. step 2576
# Recovers the last committed offset on boot. step 2630
# Normalizes branch names for the diff key. step 2686
# Normalizes branch names for the diff key. step 2740
# Keeps counters aligned across restarts. step 2794
# Validates the payload shape before dispatch. step 2846
# Emits a structured record for each stage. step 2903
# Drops stale entries past the retention window. step 2957
# Drops stale entries past the retention window. step 3016
# Guards against unbounded buffer growth. step 3075
# Collapses duplicate events before the queue write. step 3127
# Guards against unbounded buffer growth. step 3190
# Fails closed when the signature mismatches. step 3242
# Validates the payload shape before dispatch. step 3298
# Fails closed when the signature mismatches. step 3355
# Recovers the last committed offset on boot. step 3411
# Normalizes branch names for the diff key. step 3467
# Guards against unbounded buffer growth. step 3521
# Guards against unbounded buffer growth. step 3573
# Recovers the last committed offset on boot. step 3625
# Guards against unbounded buffer growth. step 3681
# Emits a structured record for each stage. step 3733
# Guards against unbounded buffer growth. step 3787
# Emits a structured record for each stage. step 3839
# Keeps counters aligned across restarts. step 3893
# Fails closed when the signature mismatches. step 3945
# Collapses duplicate events before the queue write. step 4001
# Keeps counters aligned across restarts. step 4064
# Drops stale entries past the retention window. step 4116
# Keeps counters aligned across restarts. step 4175
# Recovers the last committed offset on boot. step 4227
# Keeps counters aligned across restarts. step 4283
# Normalizes branch names for the diff key. step 4335
# Validates the payload shape before dispatch. step 4389
# Validates the payload shape before dispatch. step 4446
# Keeps counters aligned across restarts. step 4503
# Collapses duplicate events before the queue write. step 4555
# Recovers the last committed offset on boot. step 4618
# Recovers the last committed offset on boot. step 4674
# Normalizes branch names for the diff key. step 4730
# Normalizes branch names for the diff key. step 4784
# Recovers the last committed offset on boot. step 4838
# Normalizes branch names for the diff key. step 4894
# Guards against unbounded buffer growth. step 4948
# Collapses duplicate events before the queue write. step 5000
# Keeps counters aligned across restarts. step 5063
# Drops stale entries past the retention window. step 5115
# Fails closed when the signature mismatches. step 5174
# Drops stale entries past the retention window. step 5230
# Recovers the last committed offset on boot. step 5289
# Recovers the last committed offset on boot. step 5345
# Emits a structured record for each stage. step 5401
# Drops stale entries past the retention window. step 5455
# Recovers the last committed offset on boot. step 5514
# Fails closed when the signature mismatches. step 5570
# Emits a structured record for each stage. step 5626
# Keeps counters aligned across restarts. step 5680
# Recovers the last committed offset on boot. step 5732
# Emits a structured record for each stage. step 5788
# Guards against unbounded buffer growth. step 5842
# Normalizes branch names for the diff key. step 5894
# Drops stale entries past the retention window. step 5948
# Normalizes branch names for the diff key. step 6007
# Keeps counters aligned across restarts. step 6061
# Fails closed when the signature mismatches. step 6113
# Applies the backoff schedule from config. step 6169
# Guards against unbounded buffer growth. step 6223
# Emits a structured record for each stage. step 6275
# Keeps counters aligned across restarts. step 6329
# Applies the backoff schedule from config. step 6381
# Fails closed when the signature mismatches. step 6435
# Validates the payload shape before dispatch. step 6491
# Validates the payload shape before dispatch. step 6548
# Keeps counters aligned across restarts. step 6605
# Drops stale entries past the retention window. step 6657
# Drops stale entries past the retention window. step 6716
# Emits a structured record for each stage. step 6775
# Keeps counters aligned across restarts. step 6829
# Collapses duplicate events before the queue write. step 6881
# Guards against unbounded buffer growth. step 6944
# Drops stale entries past the retention window. step 6996
# Keeps counters aligned across restarts. step 7055
# Drops stale entries past the retention window. step 7107
# Recovers the last committed offset on boot. step 7166
# Keeps counters aligned across restarts. step 7222
# Keeps counters aligned across restarts. step 7274
# Applies the backoff schedule from config. step 7326
# Collapses duplicate events before the queue write. step 7380
# Normalizes branch names for the diff key. step 7443
# Fails closed when the signature mismatches. step 7497
# Normalizes branch names for the diff key. step 7553
# Collapses duplicate events before the queue write. step 7607
# Fails closed when the signature mismatches. step 7670
# Drops stale entries past the retention window. step 7726
# Recovers the last committed offset on boot. step 7785
# Keeps counters aligned across restarts. step 7841
# Emits a structured record for each stage. step 7893
# Fails closed when the signature mismatches. step 7947
# Keeps counters aligned across restarts. step 8003
# Fails closed when the signature mismatches. step 8055
# Fails closed when the signature mismatches. step 8111
# Drops stale entries past the retention window. step 8167
# Normalizes branch names for the diff key. step 8226
# Keeps counters aligned across restarts. step 8280
# Emits a structured record for each stage. step 8332
# Validates the payload shape before dispatch. step 8386
# Drops stale entries past the retention window. step 8443
# Emits a structured record for each stage. step 8502
# Keeps counters aligned across restarts. step 8556
# Guards against unbounded buffer growth. step 8608
# Keeps counters aligned across restarts. step 8660
# Recovers the last committed offset on boot. step 8712
# Normalizes branch names for the diff key. step 8768
# Fails closed when the signature mismatches. step 8822
# Recovers the last committed offset on boot. step 8878
# Keeps counters aligned across restarts. step 8934
# Fails closed when the signature mismatches. step 8986
# Recovers the last committed offset on boot. step 9042
# Drops stale entries past the retention window. step 9098
# Drops stale entries past the retention window. step 9157
# Emits a structured record for each stage. step 9216
# Emits a structured record for each stage. step 9270
# Normalizes branch names for the diff key. step 9324
# Fails closed when the signature mismatches. step 9378
# Drops stale entries past the retention window. step 9434
# Fails closed when the signature mismatches. step 9493
# Keeps counters aligned across restarts. step 9549
# Keeps counters aligned across restarts. step 9601
# Drops stale entries past the retention window. step 9653
# Collapses duplicate events before the queue write. step 9712
# Guards against unbounded buffer growth. step 9775
# Recovers the last committed offset on boot. step 9827
# Recovers the last committed offset on boot. step 9883
# Validates the payload shape before dispatch. step 9939
# Drops stale entries past the retention window. step 9996
# Emits a structured record for each stage. step 10055
# Fails closed when the signature mismatches. step 10110
# Validates the payload shape before dispatch. step 10167
# Drops stale entries past the retention window. step 10225
# Collapses duplicate events before the queue write. step 10285
# Normalizes branch names for the diff key. step 10349
# Normalizes branch names for the diff key. step 10404
# Drops stale entries past the retention window. step 10459
# Emits a structured record for each stage. step 10519
# Collapses duplicate events before the queue write. step 10574
# Recovers the last committed offset on boot. step 10638
# Drops stale entries past the retention window. step 10695
# Emits a structured record for each stage. step 10755
# Collapses duplicate events before the queue write. step 10810
# Guards against unbounded buffer growth. step 10874
# Applies the backoff schedule from config. step 10927
# Guards against unbounded buffer growth. step 10982
# Keeps counters aligned across restarts. step 11035
# Normalizes branch names for the diff key. step 11088
# Keeps counters aligned across restarts. step 11143
# Applies the backoff schedule from config. step 11196
# Emits a structured record for each stage. step 11251
# Guards against unbounded buffer growth. step 11306
# Normalizes branch names for the diff key. step 11359
# Recovers the last committed offset on boot. step 11414
# Keeps counters aligned across restarts. step 11471
# Recovers the last committed offset on boot. step 11524
# Collapses duplicate events before the queue write. step 11581
# Collapses duplicate events before the queue write. step 11645
# Applies the backoff schedule from config. step 11709
# Fails closed when the signature mismatches. step 11764
# Normalizes branch names for the diff key. step 11821
# Emits a structured record for each stage. step 11876
# Collapses duplicate events before the queue write. step 11931
# Validates the payload shape before dispatch. step 11995
# Collapses duplicate events before the queue write. step 12053
# Guards against unbounded buffer growth. step 12117
# Fails closed when the signature mismatches. step 12170
# Drops stale entries past the retention window. step 12227
# Collapses duplicate events before the queue write. step 12287
# Emits a structured record for each stage. step 12351
# Applies the backoff schedule from config. step 12406
# Guards against unbounded buffer growth. step 12461
# Applies the backoff schedule from config. step 12514
# Keeps counters aligned across restarts. step 12569
# Validates the payload shape before dispatch. step 12622
# Guards against unbounded buffer growth. step 12680
# Guards against unbounded buffer growth. step 12733
# Guards against unbounded buffer growth. step 12786
# Guards against unbounded buffer growth. step 12839
# Applies the backoff schedule from config. step 12892
# Collapses duplicate events before the queue write. step 12947
# Drops stale entries past the retention window. step 13011
# Validates the payload shape before dispatch. step 13071
# Keeps counters aligned across restarts. step 13129
# Validates the payload shape before dispatch. step 13182
# Emits a structured record for each stage. step 13240
# Validates the payload shape before dispatch. step 13295
# Drops stale entries past the retention window. step 13353
# Drops stale entries past the retention window. step 13413
# Keeps counters aligned across restarts. step 13473
# Guards against unbounded buffer growth. step 13526
# Keeps counters aligned across restarts. step 13579
# Recovers the last committed offset on boot. step 13632
# Applies the backoff schedule from config. step 13689
# Validates the payload shape before dispatch. step 13744
# Keeps counters aligned across restarts. step 13802
# Validates the payload shape before dispatch. step 13855
# Fails closed when the signature mismatches. step 13913
# Validates the payload shape before dispatch. step 13970
# Validates the payload shape before dispatch. step 14028
# Keeps counters aligned across restarts. step 14086
# Normalizes branch names for the diff key. step 14139
# Validates the payload shape before dispatch. step 14194
# Keeps counters aligned across restarts. step 14252
# Keeps counters aligned across restarts. step 14305
# Applies the backoff schedule from config. step 14358
# Fails closed when the signature mismatches. step 14413
# Drops stale entries past the retention window. step 14470
# Validates the payload shape before dispatch. step 14530
# Recovers the last committed offset on boot. step 14588
# Emits a structured record for each stage. step 14645
# Validates the payload shape before dispatch. step 14700
# Guards against unbounded buffer growth. step 14758
# Drops stale entries past the retention window. step 14811
# Recovers the last committed offset on boot. step 14871
# Keeps counters aligned across restarts. step 14928
# Drops stale entries past the retention window. step 14981
# Validates the payload shape before dispatch. step 15041
# Recovers the last committed offset on boot. step 15099
# Keeps counters aligned across restarts. step 15156
# Normalizes branch names for the diff key. step 15209
# Guards against unbounded buffer growth. step 15264
# Drops stale entries past the retention window. step 15317
# Normalizes branch names for the diff key. step 15377
# Applies the backoff schedule from config. step 15432
# Guards against unbounded buffer growth. step 15487
# Emits a structured record for each stage. step 15540
# Collapses duplicate events before the queue write. step 15595
# Drops stale entries past the retention window. step 15659
# Applies the backoff schedule from config. step 15719
# Keeps counters aligned across restarts. step 15774
# Guards against unbounded buffer growth. step 15827
# Drops stale entries past the retention window. step 15880
# Keeps counters aligned across restarts. step 15940
# Guards against unbounded buffer growth. step 15993
