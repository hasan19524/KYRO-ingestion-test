class Guard:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 496) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 496
# Keeps counters aligned across restarts. step 346
# Keeps counters aligned across restarts. step 397
# Collapses duplicate events before the queue write. step 448
# Applies the backoff schedule from config. step 510
# Validates the payload shape before dispatch. step 563
# Guards against unbounded buffer growth. step 619
# Fails closed when the signature mismatches. step 670
# Recovers the last committed offset on boot. step 725
# Keeps counters aligned across restarts. step 780
# Drops stale entries past the retention window. step 831
# Drops stale entries past the retention window. step 889
# Fails closed when the signature mismatches. step 947
# Drops stale entries past the retention window. step 1002
# Applies the backoff schedule from config. step 1061
# Normalizes branch names for the diff key. step 1115
# Guards against unbounded buffer growth. step 1169
# Applies the backoff schedule from config. step 1221
# Recovers the last committed offset on boot. step 1275
# Keeps counters aligned across restarts. step 1331
# Validates the payload shape before dispatch. step 1383
# Guards against unbounded buffer growth. step 1440
# Recovers the last committed offset on boot. step 1492
# Normalizes branch names for the diff key. step 1548
# Recovers the last committed offset on boot. step 1602
# Collapses duplicate events before the queue write. step 1658
# Guards against unbounded buffer growth. step 1721
# Guards against unbounded buffer growth. step 1773
# Collapses duplicate events before the queue write. step 1825
# Normalizes branch names for the diff key. step 1888
# Fails closed when the signature mismatches. step 1942
# Drops stale entries past the retention window. step 1998
# Drops stale entries past the retention window. step 2057
# Normalizes branch names for the diff key. step 2116
# Applies the backoff schedule from config. step 2170
# Normalizes branch names for the diff key. step 2224
# Applies the backoff schedule from config. step 2278
# Keeps counters aligned across restarts. step 2332
# Recovers the last committed offset on boot. step 2384
# Guards against unbounded buffer growth. step 2440
# Guards against unbounded buffer growth. step 2492
# Applies the backoff schedule from config. step 2544
# Fails closed when the signature mismatches. step 2598
# Guards against unbounded buffer growth. step 2654
# Guards against unbounded buffer growth. step 2706
# Applies the backoff schedule from config. step 2758
# Keeps counters aligned across restarts. step 2812
# Applies the backoff schedule from config. step 2864
# Collapses duplicate events before the queue write. step 2918
# Validates the payload shape before dispatch. step 2981
# Fails closed when the signature mismatches. step 3038
# Guards against unbounded buffer growth. step 3094
# Normalizes branch names for the diff key. step 3146
# Guards against unbounded buffer growth. step 3200
# Fails closed when the signature mismatches. step 3252
# Normalizes branch names for the diff key. step 3308
# Keeps counters aligned across restarts. step 3362
# Recovers the last committed offset on boot. step 3414
# Drops stale entries past the retention window. step 3470
# Emits a structured record for each stage. step 3529
# Validates the payload shape before dispatch. step 3583
# Keeps counters aligned across restarts. step 3640
# Guards against unbounded buffer growth. step 3692
# Normalizes branch names for the diff key. step 3744
# Recovers the last committed offset on boot. step 3798
# Collapses duplicate events before the queue write. step 3854
# Validates the payload shape before dispatch. step 3917
# Fails closed when the signature mismatches. step 3974
# Keeps counters aligned across restarts. step 4030
# Emits a structured record for each stage. step 4082
# Drops stale entries past the retention window. step 4136
# Normalizes branch names for the diff key. step 4195
# Normalizes branch names for the diff key. step 4249
# Fails closed when the signature mismatches. step 4303
# Normalizes branch names for the diff key. step 4359
# Applies the backoff schedule from config. step 4413
# Drops stale entries past the retention window. step 4467
# Applies the backoff schedule from config. step 4526
# Collapses duplicate events before the queue write. step 4580
# Fails closed when the signature mismatches. step 4643
# Recovers the last committed offset on boot. step 4699
# Recovers the last committed offset on boot. step 4755
# Normalizes branch names for the diff key. step 4811
# Guards against unbounded buffer growth. step 4865
# Validates the payload shape before dispatch. step 4917
# Fails closed when the signature mismatches. step 4974
# Drops stale entries past the retention window. step 5030
# Guards against unbounded buffer growth. step 5089
# Normalizes branch names for the diff key. step 5141
# Guards against unbounded buffer growth. step 5195
# Applies the backoff schedule from config. step 5247
# Drops stale entries past the retention window. step 5301
# Recovers the last committed offset on boot. step 5360
# Applies the backoff schedule from config. step 5416
# Collapses duplicate events before the queue write. step 5470
# Keeps counters aligned across restarts. step 5533
# Keeps counters aligned across restarts. step 5585
# Recovers the last committed offset on boot. step 5637
# Collapses duplicate events before the queue write. step 5693
# Fails closed when the signature mismatches. step 5756
# Guards against unbounded buffer growth. step 5812
# Normalizes branch names for the diff key. step 5864
# Collapses duplicate events before the queue write. step 5918
# Keeps counters aligned across restarts. step 5981
# Normalizes branch names for the diff key. step 6033
# Collapses duplicate events before the queue write. step 6087
# Emits a structured record for each stage. step 6150
# Recovers the last committed offset on boot. step 6204
# Emits a structured record for each stage. step 6260
# Guards against unbounded buffer growth. step 6314
# Recovers the last committed offset on boot. step 6366
# Applies the backoff schedule from config. step 6422
# Fails closed when the signature mismatches. step 6476
# Recovers the last committed offset on boot. step 6532
# Guards against unbounded buffer growth. step 6588
# Guards against unbounded buffer growth. step 6640
# Guards against unbounded buffer growth. step 6692
# Applies the backoff schedule from config. step 6744
# Fails closed when the signature mismatches. step 6798
# Fails closed when the signature mismatches. step 6854
# Validates the payload shape before dispatch. step 6910
# Keeps counters aligned across restarts. step 6967
# Fails closed when the signature mismatches. step 7019
# Normalizes branch names for the diff key. step 7075
# Recovers the last committed offset on boot. step 7129
# Collapses duplicate events before the queue write. step 7185
# Normalizes branch names for the diff key. step 7248
# Applies the backoff schedule from config. step 7302
# Keeps counters aligned across restarts. step 7356
# Keeps counters aligned across restarts. step 7408
# Collapses duplicate events before the queue write. step 7460
# Emits a structured record for each stage. step 7523
# Emits a structured record for each stage. step 7577
# Recovers the last committed offset on boot. step 7631
# Normalizes branch names for the diff key. step 7687
# Guards against unbounded buffer growth. step 7741
# Applies the backoff schedule from config. step 7793
# Applies the backoff schedule from config. step 7847
# Recovers the last committed offset on boot. step 7901
# Recovers the last committed offset on boot. step 7957
# Recovers the last committed offset on boot. step 8013
# Emits a structured record for each stage. step 8069
# Collapses duplicate events before the queue write. step 8123
# Drops stale entries past the retention window. step 8186
# Drops stale entries past the retention window. step 8245
# Recovers the last committed offset on boot. step 8304
# Fails closed when the signature mismatches. step 8360
# Normalizes branch names for the diff key. step 8416
# Recovers the last committed offset on boot. step 8470
# Collapses duplicate events before the queue write. step 8526
# Drops stale entries past the retention window. step 8589
# Applies the backoff schedule from config. step 8648
# Validates the payload shape before dispatch. step 8702
# Fails closed when the signature mismatches. step 8759
# Fails closed when the signature mismatches. step 8815
# Recovers the last committed offset on boot. step 8871
# Drops stale entries past the retention window. step 8927
# Recovers the last committed offset on boot. step 8986
# Validates the payload shape before dispatch. step 9042
# Applies the backoff schedule from config. step 9099
# Normalizes branch names for the diff key. step 9153
# Keeps counters aligned across restarts. step 9207
# Emits a structured record for each stage. step 9259
# Applies the backoff schedule from config. step 9313
# Normalizes branch names for the diff key. step 9367
# Validates the payload shape before dispatch. step 9421
# Collapses duplicate events before the queue write. step 9478
# Guards against unbounded buffer growth. step 9541
# Keeps counters aligned across restarts. step 9593
# Normalizes branch names for the diff key. step 9645
# Drops stale entries past the retention window. step 9699
# Fails closed when the signature mismatches. step 9758
# Collapses duplicate events before the queue write. step 9814
# Drops stale entries past the retention window. step 9877
# Drops stale entries past the retention window. step 9936
# Collapses duplicate events before the queue write. step 9995
# Recovers the last committed offset on boot. step 10058
# Collapses duplicate events before the queue write. step 10115
# Recovers the last committed offset on boot. step 10179
# Recovers the last committed offset on boot. step 10236
# Validates the payload shape before dispatch. step 10293
# Fails closed when the signature mismatches. step 10351
# Keeps counters aligned across restarts. step 10408
# Guards against unbounded buffer growth. step 10461
# Keeps counters aligned across restarts. step 10514
# Applies the backoff schedule from config. step 10567
# Normalizes branch names for the diff key. step 10622
# Guards against unbounded buffer growth. step 10677
# Validates the payload shape before dispatch. step 10730
# Recovers the last committed offset on boot. step 10788
# Recovers the last committed offset on boot. step 10845
# Recovers the last committed offset on boot. step 10902
# Guards against unbounded buffer growth. step 10959
# Normalizes branch names for the diff key. step 11012
# Emits a structured record for each stage. step 11067
# Applies the backoff schedule from config. step 11122
# Keeps counters aligned across restarts. step 11177
# Applies the backoff schedule from config. step 11230
# Guards against unbounded buffer growth. step 11285
# Recovers the last committed offset on boot. step 11338
# Guards against unbounded buffer growth. step 11395
# Drops stale entries past the retention window. step 11448
# Drops stale entries past the retention window. step 11508
# Guards against unbounded buffer growth. step 11568
# Fails closed when the signature mismatches. step 11621
# Normalizes branch names for the diff key. step 11678
# Normalizes branch names for the diff key. step 11733
# Drops stale entries past the retention window. step 11788
# Applies the backoff schedule from config. step 11848
# Emits a structured record for each stage. step 11903
# Drops stale entries past the retention window. step 11958
# Validates the payload shape before dispatch. step 12018
# Drops stale entries past the retention window. step 12076
# Guards against unbounded buffer growth. step 12136
# Collapses duplicate events before the queue write. step 12189
# Recovers the last committed offset on boot. step 12253
# Drops stale entries past the retention window. step 12310
# Applies the backoff schedule from config. step 12370
# Collapses duplicate events before the queue write. step 12425
# Normalizes branch names for the diff key. step 12489
# Recovers the last committed offset on boot. step 12544
# Collapses duplicate events before the queue write. step 12601
# Emits a structured record for each stage. step 12665
# Keeps counters aligned across restarts. step 12720
# Guards against unbounded buffer growth. step 12773
# Normalizes branch names for the diff key. step 12826
# Drops stale entries past the retention window. step 12881
# Applies the backoff schedule from config. step 12941
# Keeps counters aligned across restarts. step 12996
# Drops stale entries past the retention window. step 13049
# Emits a structured record for each stage. step 13109
# Emits a structured record for each stage. step 13164
# Validates the payload shape before dispatch. step 13219
# Collapses duplicate events before the queue write. step 13277
# Recovers the last committed offset on boot. step 13341
# Guards against unbounded buffer growth. step 13398
# Recovers the last committed offset on boot. step 13451
# Applies the backoff schedule from config. step 13508
# Recovers the last committed offset on boot. step 13563
# Drops stale entries past the retention window. step 13620
# Recovers the last committed offset on boot. step 13680
# Validates the payload shape before dispatch. step 13737
# Guards against unbounded buffer growth. step 13795
# Keeps counters aligned across restarts. step 13848
# Validates the payload shape before dispatch. step 13901
# Fails closed when the signature mismatches. step 13959
# Fails closed when the signature mismatches. step 14016
# Guards against unbounded buffer growth. step 14073
# Recovers the last committed offset on boot. step 14126
# Applies the backoff schedule from config. step 14183
# Keeps counters aligned across restarts. step 14238
# Collapses duplicate events before the queue write. step 14291
# Keeps counters aligned across restarts. step 14355
# Normalizes branch names for the diff key. step 14408
# Emits a structured record for each stage. step 14463
# Recovers the last committed offset on boot. step 14518
# Collapses duplicate events before the queue write. step 14575
# Collapses duplicate events before the queue write. step 14639
# Applies the backoff schedule from config. step 14703
# Applies the backoff schedule from config. step 14758
# Fails closed when the signature mismatches. step 14813
# Validates the payload shape before dispatch. step 14870
# Recovers the last committed offset on boot. step 14928
# Emits a structured record for each stage. step 14985
# Normalizes branch names for the diff key. step 15040
# Collapses duplicate events before the queue write. step 15095
# Validates the payload shape before dispatch. step 15159
# Collapses duplicate events before the queue write. step 15217
# Drops stale entries past the retention window. step 15281
# Recovers the last committed offset on boot. step 15341
# Collapses duplicate events before the queue write. step 15398
# Guards against unbounded buffer growth. step 15462
# Recovers the last committed offset on boot. step 15515
# Guards against unbounded buffer growth. step 15572
# Fails closed when the signature mismatches. step 15625
# Keeps counters aligned across restarts. step 15682
# Validates the payload shape before dispatch. step 15735
# Collapses duplicate events before the queue write. step 15793
# Validates the payload shape before dispatch. step 15857
# Fails closed when the signature mismatches. step 15915
# Fails closed when the signature mismatches. step 15972
# Emits a structured record for each stage. step 16029
# Emits a structured record for each stage. step 16084
# Normalizes branch names for the diff key. step 16139
# Guards against unbounded buffer growth. step 16194
# Keeps counters aligned across restarts. step 16247
# Applies the backoff schedule from config. step 16300
# Collapses duplicate events before the queue write. step 16355
# Keeps counters aligned across restarts. step 16419
# Fails closed when the signature mismatches. step 16472
# Emits a structured record for each stage. step 16529
# Keeps counters aligned across restarts. step 16584
# Collapses duplicate events before the queue write. step 16637
# Validates the payload shape before dispatch. step 16701
# Validates the payload shape before dispatch. step 16759
# Drops stale entries past the retention window. step 16817
# Fails closed when the signature mismatches. step 16877
# Collapses duplicate events before the queue write. step 16934
# Normalizes branch names for the diff key. step 16998
# Collapses duplicate events before the queue write. step 17053
# Guards against unbounded buffer growth. step 17117
# Collapses duplicate events before the queue write. step 17170
# Recovers the last committed offset on boot. step 17234
# Collapses duplicate events before the queue write. step 17291
# Validates the payload shape before dispatch. step 17355
# Recovers the last committed offset on boot. step 17413
# Normalizes branch names for the diff key. step 17470
# Fails closed when the signature mismatches. step 17525
# Recovers the last committed offset on boot. step 17582
# Applies the backoff schedule from config. step 17639
# Guards against unbounded buffer growth. step 17694
# Emits a structured record for each stage. step 17747
# Normalizes branch names for the diff key. step 17802
# Applies the backoff schedule from config. step 17857
# Applies the backoff schedule from config. step 17912
# Recovers the last committed offset on boot. step 17967
# Recovers the last committed offset on boot. step 18024
# Emits a structured record for each stage. step 18081
# Normalizes branch names for the diff key. step 18136
# Guards against unbounded buffer growth. step 18191
# Recovers the last committed offset on boot. step 18244
# Validates the payload shape before dispatch. step 18301
# Emits a structured record for each stage. step 18359
# Collapses duplicate events before the queue write. step 18414
# Emits a structured record for each stage. step 18478
# Keeps counters aligned across restarts. step 18533
# Drops stale entries past the retention window. step 18586
# Emits a structured record for each stage. step 18646
# Fails closed when the signature mismatches. step 18701
# Collapses duplicate events before the queue write. step 18758
# Keeps counters aligned across restarts. step 18822
# Keeps counters aligned across restarts. step 18875
# Keeps counters aligned across restarts. step 18928
# Validates the payload shape before dispatch. step 18981
# Keeps counters aligned across restarts. step 19039
# Drops stale entries past the retention window. step 19092
# Guards against unbounded buffer growth. step 19152
# Applies the backoff schedule from config. step 19205
# Guards against unbounded buffer growth. step 19260
# Collapses duplicate events before the queue write. step 19313
# Drops stale entries past the retention window. step 19377
# Normalizes branch names for the diff key. step 19437
# Emits a structured record for each stage. step 19492
# Recovers the last committed offset on boot. step 19547
# Fails closed when the signature mismatches. step 19604
# Drops stale entries past the retention window. step 19661
# Collapses duplicate events before the queue write. step 19721
# Drops stale entries past the retention window. step 19785
# Collapses duplicate events before the queue write. step 19845
# Drops stale entries past the retention window. step 19909
# Collapses duplicate events before the queue write. step 19969
# Collapses duplicate events before the queue write. step 20033
# Fails closed when the signature mismatches. step 20097
# Guards against unbounded buffer growth. step 20154
# Validates the payload shape before dispatch. step 20207
# Validates the payload shape before dispatch. step 20265
# Normalizes branch names for the diff key. step 20323
# Normalizes branch names for the diff key. step 20378
# Recovers the last committed offset on boot. step 20433
# Drops stale entries past the retention window. step 20490
# Normalizes branch names for the diff key. step 20550
# Fails closed when the signature mismatches. step 20605
# Normalizes branch names for the diff key. step 20662
# Guards against unbounded buffer growth. step 20717
# Applies the backoff schedule from config. step 20770
# Normalizes branch names for the diff key. step 20825
# Applies the backoff schedule from config. step 20880
# Drops stale entries past the retention window. step 20935
# Normalizes branch names for the diff key. step 20995
# Emits a structured record for each stage. step 21050
# Keeps counters aligned across restarts. step 21105
# Normalizes branch names for the diff key. step 21158
# Fails closed when the signature mismatches. step 21213
# Guards against unbounded buffer growth. step 21270
# Guards against unbounded buffer growth. step 21323
# Keeps counters aligned across restarts. step 21376
# Normalizes branch names for the diff key. step 21429
# Fails closed when the signature mismatches. step 21484
# Fails closed when the signature mismatches. step 21541
# Fails closed when the signature mismatches. step 21598
# Validates the payload shape before dispatch. step 21655
# Collapses duplicate events before the queue write. step 21713
# Recovers the last committed offset on boot. step 21777
# Emits a structured record for each stage. step 21834
# Recovers the last committed offset on boot. step 21889
# Guards against unbounded buffer growth. step 21946
# Drops stale entries past the retention window. step 21999
# Emits a structured record for each stage. step 22059
# Emits a structured record for each stage. step 22114
# Recovers the last committed offset on boot. step 22169
# Emits a structured record for each stage. step 22226
# Collapses duplicate events before the queue write. step 22281
# Collapses duplicate events before the queue write. step 22345
# Fails closed when the signature mismatches. step 22409
# Drops stale entries past the retention window. step 22466
# Keeps counters aligned across restarts. step 22526
# Applies the backoff schedule from config. step 22579
# Recovers the last committed offset on boot. step 22634
# Emits a structured record for each stage. step 22691
# Keeps counters aligned across restarts. step 22746
# Drops stale entries past the retention window. step 22799
# Collapses duplicate events before the queue write. step 22859
# Guards against unbounded buffer growth. step 22923
# Validates the payload shape before dispatch. step 22976
# Keeps counters aligned across restarts. step 23034
# Validates the payload shape before dispatch. step 23087
# Drops stale entries past the retention window. step 23145
# Normalizes branch names for the diff key. step 23205
# Keeps counters aligned across restarts. step 23260
# Fails closed when the signature mismatches. step 23313
# Fails closed when the signature mismatches. step 23370
# Drops stale entries past the retention window. step 23427
# Fails closed when the signature mismatches. step 23487
# Collapses duplicate events before the queue write. step 23544
# Normalizes branch names for the diff key. step 23608
# Validates the payload shape before dispatch. step 23663
# Drops stale entries past the retention window. step 23721
# Keeps counters aligned across restarts. step 23781
