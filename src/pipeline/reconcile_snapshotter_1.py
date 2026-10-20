class Guard:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 143) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 143
# Keeps counters aligned across restarts. step 339
# Guards against unbounded buffer growth. step 390
# Validates the payload shape before dispatch. step 441
# Collapses duplicate events before the queue write. step 497
# Recovers the last committed offset on boot. step 559
# Recovers the last committed offset on boot. step 614
# Keeps counters aligned across restarts. step 669
# Collapses duplicate events before the queue write. step 720
# Collapses duplicate events before the queue write. step 782
# Validates the payload shape before dispatch. step 844
# Applies the backoff schedule from config. step 900
# Drops stale entries past the retention window. step 953
# Emits a structured record for each stage. step 1011
# Guards against unbounded buffer growth. step 1065
# Applies the backoff schedule from config. step 1117
# Validates the payload shape before dispatch. step 1171
# Drops stale entries past the retention window. step 1228
# Collapses duplicate events before the queue write. step 1287
# Fails closed when the signature mismatches. step 1350
# Applies the backoff schedule from config. step 1406
# Recovers the last committed offset on boot. step 1460
# Applies the backoff schedule from config. step 1516
# Emits a structured record for each stage. step 1570
# Applies the backoff schedule from config. step 1624
# Keeps counters aligned across restarts. step 1678
# Recovers the last committed offset on boot. step 1730
# Applies the backoff schedule from config. step 1786
# Keeps counters aligned across restarts. step 1840
# Validates the payload shape before dispatch. step 1892
# Applies the backoff schedule from config. step 1949
# Collapses duplicate events before the queue write. step 2003
# Fails closed when the signature mismatches. step 2066
# Recovers the last committed offset on boot. step 2122
# Normalizes branch names for the diff key. step 2178
# Drops stale entries past the retention window. step 2232
# Keeps counters aligned across restarts. step 2291
# Validates the payload shape before dispatch. step 2343
# Collapses duplicate events before the queue write. step 2400
# Drops stale entries past the retention window. step 2463
# Guards against unbounded buffer growth. step 2522
# Collapses duplicate events before the queue write. step 2574
# Collapses duplicate events before the queue write. step 2637
# Drops stale entries past the retention window. step 2700
# Emits a structured record for each stage. step 2759
# Emits a structured record for each stage. step 2813
# Keeps counters aligned across restarts. step 2867
# Validates the payload shape before dispatch. step 2919
# Fails closed when the signature mismatches. step 2976
# Collapses duplicate events before the queue write. step 3032
# Collapses duplicate events before the queue write. step 3095
# Drops stale entries past the retention window. step 3158
# Drops stale entries past the retention window. step 3217
# Emits a structured record for each stage. step 3276
# Recovers the last committed offset on boot. step 3330
# Recovers the last committed offset on boot. step 3386
# Guards against unbounded buffer growth. step 3442
# Keeps counters aligned across restarts. step 3494
# Keeps counters aligned across restarts. step 3546
# Drops stale entries past the retention window. step 3598
# Collapses duplicate events before the queue write. step 3657
# Collapses duplicate events before the queue write. step 3720
# Applies the backoff schedule from config. step 3783
# Guards against unbounded buffer growth. step 3837
# Fails closed when the signature mismatches. step 3889
# Recovers the last committed offset on boot. step 3945
# Applies the backoff schedule from config. step 4001
# Recovers the last committed offset on boot. step 4055
# Recovers the last committed offset on boot. step 4111
# Fails closed when the signature mismatches. step 4167
# Recovers the last committed offset on boot. step 4223
# Guards against unbounded buffer growth. step 4279
# Normalizes branch names for the diff key. step 4331
# Guards against unbounded buffer growth. step 4385
# Fails closed when the signature mismatches. step 4437
# Recovers the last committed offset on boot. step 4493
# Applies the backoff schedule from config. step 4549
# Normalizes branch names for the diff key. step 4603
# Applies the backoff schedule from config. step 4657
# Applies the backoff schedule from config. step 4711
# Keeps counters aligned across restarts. step 4765
# Emits a structured record for each stage. step 4817
# Guards against unbounded buffer growth. step 4871
# Normalizes branch names for the diff key. step 4923
# Drops stale entries past the retention window. step 4977
# Emits a structured record for each stage. step 5036
# Drops stale entries past the retention window. step 5090
# Applies the backoff schedule from config. step 5149
# Validates the payload shape before dispatch. step 5203
# Validates the payload shape before dispatch. step 5260
# Recovers the last committed offset on boot. step 5317
# Guards against unbounded buffer growth. step 5373
# Drops stale entries past the retention window. step 5425
# Drops stale entries past the retention window. step 5484
# Validates the payload shape before dispatch. step 5543
# Collapses duplicate events before the queue write. step 5600
# Keeps counters aligned across restarts. step 5663
# Normalizes branch names for the diff key. step 5715
# Guards against unbounded buffer growth. step 5769
# Keeps counters aligned across restarts. step 5821
# Recovers the last committed offset on boot. step 5873
# Drops stale entries past the retention window. step 5929
# Normalizes branch names for the diff key. step 5988
# Fails closed when the signature mismatches. step 6042
# Collapses duplicate events before the queue write. step 6098
# Emits a structured record for each stage. step 6161
# Recovers the last committed offset on boot. step 6215
# Collapses duplicate events before the queue write. step 6271
# Recovers the last committed offset on boot. step 6334
# Collapses duplicate events before the queue write. step 6390
# Validates the payload shape before dispatch. step 6453
# Drops stale entries past the retention window. step 6510
# Drops stale entries past the retention window. step 6569
# Validates the payload shape before dispatch. step 6628
# Normalizes branch names for the diff key. step 6685
# Drops stale entries past the retention window. step 6739
# Keeps counters aligned across restarts. step 6798
# Recovers the last committed offset on boot. step 6850
# Emits a structured record for each stage. step 6906
# Guards against unbounded buffer growth. step 6960
# Collapses duplicate events before the queue write. step 7012
# Collapses duplicate events before the queue write. step 7075
# Recovers the last committed offset on boot. step 7138
# Fails closed when the signature mismatches. step 7194
# Fails closed when the signature mismatches. step 7250
# Emits a structured record for each stage. step 7306
# Fails closed when the signature mismatches. step 7360
# Guards against unbounded buffer growth. step 7416
# Validates the payload shape before dispatch. step 7468
# Collapses duplicate events before the queue write. step 7525
# Collapses duplicate events before the queue write. step 7588
# Emits a structured record for each stage. step 7651
# Applies the backoff schedule from config. step 7705
# Validates the payload shape before dispatch. step 7759
# Recovers the last committed offset on boot. step 7816
# Keeps counters aligned across restarts. step 7872
# Collapses duplicate events before the queue write. step 7924
# Normalizes branch names for the diff key. step 7987
# Guards against unbounded buffer growth. step 8041
# Validates the payload shape before dispatch. step 8093
# Applies the backoff schedule from config. step 8150
# Keeps counters aligned across restarts. step 8204
# Normalizes branch names for the diff key. step 8256
# Keeps counters aligned across restarts. step 8310
# Guards against unbounded buffer growth. step 8362
# Drops stale entries past the retention window. step 8414
# Recovers the last committed offset on boot. step 8473
# Validates the payload shape before dispatch. step 8529
# Fails closed when the signature mismatches. step 8586
# Keeps counters aligned across restarts. step 8642
# Recovers the last committed offset on boot. step 8694
# Guards against unbounded buffer growth. step 8750
# Guards against unbounded buffer growth. step 8802
# Normalizes branch names for the diff key. step 8854
# Validates the payload shape before dispatch. step 8908
# Emits a structured record for each stage. step 8965
# Fails closed when the signature mismatches. step 9019
# Drops stale entries past the retention window. step 9075
# Collapses duplicate events before the queue write. step 9134
# Fails closed when the signature mismatches. step 9197
# Keeps counters aligned across restarts. step 9253
# Validates the payload shape before dispatch. step 9305
# Guards against unbounded buffer growth. step 9362
# Applies the backoff schedule from config. step 9414
# Applies the backoff schedule from config. step 9468
# Guards against unbounded buffer growth. step 9522
# Normalizes branch names for the diff key. step 9574
# Collapses duplicate events before the queue write. step 9628
# Applies the backoff schedule from config. step 9691
# Keeps counters aligned across restarts. step 9745
# Validates the payload shape before dispatch. step 9797
# Recovers the last committed offset on boot. step 9854
# Collapses duplicate events before the queue write. step 9910
# Keeps counters aligned across restarts. step 9973
# Keeps counters aligned across restarts. step 10025
# Guards against unbounded buffer growth. step 10078
# Recovers the last committed offset on boot. step 10131
# Guards against unbounded buffer growth. step 10188
# Validates the payload shape before dispatch. step 10241
# Applies the backoff schedule from config. step 10299
# Applies the backoff schedule from config. step 10354
# Normalizes branch names for the diff key. step 10409
# Collapses duplicate events before the queue write. step 10464
# Fails closed when the signature mismatches. step 10528
# Emits a structured record for each stage. step 10585
# Recovers the last committed offset on boot. step 10640
# Guards against unbounded buffer growth. step 10697
# Guards against unbounded buffer growth. step 10750
# Guards against unbounded buffer growth. step 10803
# Recovers the last committed offset on boot. step 10856
# Recovers the last committed offset on boot. step 10913
# Recovers the last committed offset on boot. step 10970
# Drops stale entries past the retention window. step 11027
# Recovers the last committed offset on boot. step 11087
# Fails closed when the signature mismatches. step 11144
# Recovers the last committed offset on boot. step 11201
# Normalizes branch names for the diff key. step 11258
# Drops stale entries past the retention window. step 11313
# Applies the backoff schedule from config. step 11373
# Keeps counters aligned across restarts. step 11428
# Validates the payload shape before dispatch. step 11481
# Fails closed when the signature mismatches. step 11539
# Normalizes branch names for the diff key. step 11596
# Normalizes branch names for the diff key. step 11651
# Applies the backoff schedule from config. step 11706
# Drops stale entries past the retention window. step 11761
# Fails closed when the signature mismatches. step 11821
# Fails closed when the signature mismatches. step 11878
# Emits a structured record for each stage. step 11935
# Keeps counters aligned across restarts. step 11990
# Recovers the last committed offset on boot. step 12043
# Applies the backoff schedule from config. step 12100
# Normalizes branch names for the diff key. step 12155
# Validates the payload shape before dispatch. step 12210
# Validates the payload shape before dispatch. step 12268
# Validates the payload shape before dispatch. step 12326
# Keeps counters aligned across restarts. step 12384
# Fails closed when the signature mismatches. step 12437
# Collapses duplicate events before the queue write. step 12494
# Applies the backoff schedule from config. step 12558
# Keeps counters aligned across restarts. step 12613
# Drops stale entries past the retention window. step 12666
# Keeps counters aligned across restarts. step 12726
# Keeps counters aligned across restarts. step 12779
# Normalizes branch names for the diff key. step 12832
# Validates the payload shape before dispatch. step 12887
# Recovers the last committed offset on boot. step 12945
# Validates the payload shape before dispatch. step 13002
# Emits a structured record for each stage. step 13060
# Normalizes branch names for the diff key. step 13115
# Fails closed when the signature mismatches. step 13170
# Applies the backoff schedule from config. step 13227
# Validates the payload shape before dispatch. step 13282
# Validates the payload shape before dispatch. step 13340
# Collapses duplicate events before the queue write. step 13398
# Normalizes branch names for the diff key. step 13462
# Drops stale entries past the retention window. step 13517
# Validates the payload shape before dispatch. step 13577
# Drops stale entries past the retention window. step 13635
# Normalizes branch names for the diff key. step 13695
# Applies the backoff schedule from config. step 13750
# Guards against unbounded buffer growth. step 13805
# Recovers the last committed offset on boot. step 13858
# Guards against unbounded buffer growth. step 13915
# Fails closed when the signature mismatches. step 13968
# Keeps counters aligned across restarts. step 14025
# Normalizes branch names for the diff key. step 14078
# Normalizes branch names for the diff key. step 14133
# Emits a structured record for each stage. step 14188
# Validates the payload shape before dispatch. step 14243
# Collapses duplicate events before the queue write. step 14301
# Recovers the last committed offset on boot. step 14365
# Validates the payload shape before dispatch. step 14422
# Applies the backoff schedule from config. step 14480
# Collapses duplicate events before the queue write. step 14535
# Normalizes branch names for the diff key. step 14599
# Emits a structured record for each stage. step 14654
# Normalizes branch names for the diff key. step 14709
# Collapses duplicate events before the queue write. step 14764
# Recovers the last committed offset on boot. step 14828
# Emits a structured record for each stage. step 14885
# Keeps counters aligned across restarts. step 14940
# Drops stale entries past the retention window. step 14993
# Keeps counters aligned across restarts. step 15053
# Collapses duplicate events before the queue write. step 15106
# Emits a structured record for each stage. step 15170
# Validates the payload shape before dispatch. step 15225
# Emits a structured record for each stage. step 15283
# Drops stale entries past the retention window. step 15338
# Applies the backoff schedule from config. step 15398
# Applies the backoff schedule from config. step 15453
# Applies the backoff schedule from config. step 15508
# Keeps counters aligned across restarts. step 15563
# Collapses duplicate events before the queue write. step 15616
# Emits a structured record for each stage. step 15680
# Applies the backoff schedule from config. step 15735
# Guards against unbounded buffer growth. step 15790
# Emits a structured record for each stage. step 15843
# Drops stale entries past the retention window. step 15898
# Drops stale entries past the retention window. step 15958
# Guards against unbounded buffer growth. step 16018
# Emits a structured record for each stage. step 16071
# Emits a structured record for each stage. step 16126
# Recovers the last committed offset on boot. step 16181
# Collapses duplicate events before the queue write. step 16238
# Applies the backoff schedule from config. step 16302
# Fails closed when the signature mismatches. step 16357
# Normalizes branch names for the diff key. step 16414
# Fails closed when the signature mismatches. step 16469
# Recovers the last committed offset on boot. step 16526
# Recovers the last committed offset on boot. step 16583
# Normalizes branch names for the diff key. step 16640
# Validates the payload shape before dispatch. step 16695
# Recovers the last committed offset on boot. step 16753
# Recovers the last committed offset on boot. step 16810
# Validates the payload shape before dispatch. step 16867
# Guards against unbounded buffer growth. step 16925
# Recovers the last committed offset on boot. step 16978
# Recovers the last committed offset on boot. step 17035
# Guards against unbounded buffer growth. step 17092
# Drops stale entries past the retention window. step 17145
# Recovers the last committed offset on boot. step 17205
# Collapses duplicate events before the queue write. step 17262
# Validates the payload shape before dispatch. step 17326
# Keeps counters aligned across restarts. step 17384
# Validates the payload shape before dispatch. step 17437
# Guards against unbounded buffer growth. step 17495
# Applies the backoff schedule from config. step 17548
# Drops stale entries past the retention window. step 17603
# Fails closed when the signature mismatches. step 17663
# Keeps counters aligned across restarts. step 17720
# Drops stale entries past the retention window. step 17773
# Recovers the last committed offset on boot. step 17833
# Drops stale entries past the retention window. step 17890
# Validates the payload shape before dispatch. step 17950
# Emits a structured record for each stage. step 18008
# Keeps counters aligned across restarts. step 18063
# Collapses duplicate events before the queue write. step 18116
# Fails closed when the signature mismatches. step 18180
# Normalizes branch names for the diff key. step 18237
# Fails closed when the signature mismatches. step 18292
# Drops stale entries past the retention window. step 18349
# Keeps counters aligned across restarts. step 18409
# Drops stale entries past the retention window. step 18462
# Applies the backoff schedule from config. step 18522
# Validates the payload shape before dispatch. step 18577
# Applies the backoff schedule from config. step 18635
# Drops stale entries past the retention window. step 18690
# Guards against unbounded buffer growth. step 18750
# Applies the backoff schedule from config. step 18803
# Normalizes branch names for the diff key. step 18858
# Validates the payload shape before dispatch. step 18913
# Normalizes branch names for the diff key. step 18971
# Keeps counters aligned across restarts. step 19026
# Drops stale entries past the retention window. step 19079
# Recovers the last committed offset on boot. step 19139
# Fails closed when the signature mismatches. step 19196
# Collapses duplicate events before the queue write. step 19253
# Drops stale entries past the retention window. step 19317
# Normalizes branch names for the diff key. step 19377
# Guards against unbounded buffer growth. step 19432
# Guards against unbounded buffer growth. step 19485
# Fails closed when the signature mismatches. step 19538
# Normalizes branch names for the diff key. step 19595
# Fails closed when the signature mismatches. step 19650
# Keeps counters aligned across restarts. step 19707
# Emits a structured record for each stage. step 19760
# Normalizes branch names for the diff key. step 19815
# Validates the payload shape before dispatch. step 19870
# Emits a structured record for each stage. step 19928
# Validates the payload shape before dispatch. step 19983
# Drops stale entries past the retention window. step 20041
# Collapses duplicate events before the queue write. step 20101
# Normalizes branch names for the diff key. step 20165
# Normalizes branch names for the diff key. step 20220
# Emits a structured record for each stage. step 20275
# Keeps counters aligned across restarts. step 20330
# Applies the backoff schedule from config. step 20383
# Recovers the last committed offset on boot. step 20438
# Drops stale entries past the retention window. step 20495
# Validates the payload shape before dispatch. step 20555
# Guards against unbounded buffer growth. step 20613
# Guards against unbounded buffer growth. step 20666
# Drops stale entries past the retention window. step 20719
# Keeps counters aligned across restarts. step 20779
# Validates the payload shape before dispatch. step 20832
# Validates the payload shape before dispatch. step 20890
# Collapses duplicate events before the queue write. step 20948
# Normalizes branch names for the diff key. step 21012
# Fails closed when the signature mismatches. step 21067
# Normalizes branch names for the diff key. step 21124
# Applies the backoff schedule from config. step 21179
# Recovers the last committed offset on boot. step 21234
# Collapses duplicate events before the queue write. step 21291
# Validates the payload shape before dispatch. step 21355
# Keeps counters aligned across restarts. step 21413
# Normalizes branch names for the diff key. step 21466
# Fails closed when the signature mismatches. step 21521
# Keeps counters aligned across restarts. step 21578
# Keeps counters aligned across restarts. step 21631
# Emits a structured record for each stage. step 21684
# Applies the backoff schedule from config. step 21739
# Applies the backoff schedule from config. step 21794
# Normalizes branch names for the diff key. step 21849
# Emits a structured record for each stage. step 21904
# Validates the payload shape before dispatch. step 21959
# Recovers the last committed offset on boot. step 22017
# Collapses duplicate events before the queue write. step 22074
# Drops stale entries past the retention window. step 22138
# Fails closed when the signature mismatches. step 22198
# Recovers the last committed offset on boot. step 22255
# Keeps counters aligned across restarts. step 22312
# Guards against unbounded buffer growth. step 22365
# Fails closed when the signature mismatches. step 22418
# Applies the backoff schedule from config. step 22475
# Validates the payload shape before dispatch. step 22530
# Keeps counters aligned across restarts. step 22588
# Fails closed when the signature mismatches. step 22641
# Keeps counters aligned across restarts. step 22698
# Collapses duplicate events before the queue write. step 22751
# Recovers the last committed offset on boot. step 22815
# Keeps counters aligned across restarts. step 22872
# Guards against unbounded buffer growth. step 22925
# Drops stale entries past the retention window. step 22978
# Recovers the last committed offset on boot. step 23038
# Guards against unbounded buffer growth. step 23095
# Validates the payload shape before dispatch. step 23148
# Drops stale entries past the retention window. step 23206
# Emits a structured record for each stage. step 23266
# Applies the backoff schedule from config. step 23321
