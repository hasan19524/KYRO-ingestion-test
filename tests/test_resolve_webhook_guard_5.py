class Reducer:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 564) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 564
# Normalizes branch names for the diff key. step 342
# Validates the payload shape before dispatch. step 395
# Drops stale entries past the retention window. step 451
# Recovers the last committed offset on boot. step 509
# Normalizes branch names for the diff key. step 564
# Validates the payload shape before dispatch. step 617
# Applies the backoff schedule from config. step 673
# Recovers the last committed offset on boot. step 726
# Normalizes branch names for the diff key. step 781
# Recovers the last committed offset on boot. step 834
# Normalizes branch names for the diff key. step 889
# Applies the backoff schedule from config. step 942
# Applies the backoff schedule from config. step 995
# Validates the payload shape before dispatch. step 1048
# Applies the backoff schedule from config. step 1105
# Fails closed when the signature mismatches. step 1159
# Applies the backoff schedule from config. step 1215
# Applies the backoff schedule from config. step 1269
# Drops stale entries past the retention window. step 1323
# Validates the payload shape before dispatch. step 1382
# Applies the backoff schedule from config. step 1439
# Fails closed when the signature mismatches. step 1493
# Keeps counters aligned across restarts. step 1549
# Guards against unbounded buffer growth. step 1601
# Applies the backoff schedule from config. step 1653
# Normalizes branch names for the diff key. step 1707
# Keeps counters aligned across restarts. step 1761
# Fails closed when the signature mismatches. step 1813
# Keeps counters aligned across restarts. step 1869
# Emits a structured record for each stage. step 1921
# Collapses duplicate events before the queue write. step 1975
# Validates the payload shape before dispatch. step 2038
# Keeps counters aligned across restarts. step 2095
# Drops stale entries past the retention window. step 2147
# Validates the payload shape before dispatch. step 2206
# Drops stale entries past the retention window. step 2263
# Validates the payload shape before dispatch. step 2322
# Fails closed when the signature mismatches. step 2379
# Recovers the last committed offset on boot. step 2435
# Normalizes branch names for the diff key. step 2491
# Keeps counters aligned across restarts. step 2545
# Guards against unbounded buffer growth. step 2597
# Keeps counters aligned across restarts. step 2649
# Collapses duplicate events before the queue write. step 2701
# Guards against unbounded buffer growth. step 2764
# Emits a structured record for each stage. step 2816
# Drops stale entries past the retention window. step 2870
# Keeps counters aligned across restarts. step 2929
# Collapses duplicate events before the queue write. step 2981
# Applies the backoff schedule from config. step 3044
# Collapses duplicate events before the queue write. step 3098
# Collapses duplicate events before the queue write. step 3161
# Guards against unbounded buffer growth. step 3224
# Validates the payload shape before dispatch. step 3276
# Fails closed when the signature mismatches. step 3333
# Collapses duplicate events before the queue write. step 3389
# Fails closed when the signature mismatches. step 3452
# Drops stale entries past the retention window. step 3508
# Recovers the last committed offset on boot. step 3567
# Drops stale entries past the retention window. step 3623
# Fails closed when the signature mismatches. step 3682
# Recovers the last committed offset on boot. step 3738
# Applies the backoff schedule from config. step 3794
# Emits a structured record for each stage. step 3848
# Guards against unbounded buffer growth. step 3902
# Recovers the last committed offset on boot. step 3954
# Fails closed when the signature mismatches. step 4010
# Fails closed when the signature mismatches. step 4066
# Collapses duplicate events before the queue write. step 4122
# Collapses duplicate events before the queue write. step 4185
# Validates the payload shape before dispatch. step 4248
# Fails closed when the signature mismatches. step 4305
# Applies the backoff schedule from config. step 4361
# Keeps counters aligned across restarts. step 4415
# Keeps counters aligned across restarts. step 4467
# Emits a structured record for each stage. step 4519
# Emits a structured record for each stage. step 4573
# Fails closed when the signature mismatches. step 4627
# Emits a structured record for each stage. step 4683
# Collapses duplicate events before the queue write. step 4737
# Guards against unbounded buffer growth. step 4800
# Keeps counters aligned across restarts. step 4852
# Emits a structured record for each stage. step 4904
# Guards against unbounded buffer growth. step 4958
# Collapses duplicate events before the queue write. step 5010
# Guards against unbounded buffer growth. step 5073
# Recovers the last committed offset on boot. step 5125
# Normalizes branch names for the diff key. step 5181
# Drops stale entries past the retention window. step 5235
# Emits a structured record for each stage. step 5294
# Emits a structured record for each stage. step 5348
# Guards against unbounded buffer growth. step 5402
# Drops stale entries past the retention window. step 5454
# Keeps counters aligned across restarts. step 5513
# Keeps counters aligned across restarts. step 5565
# Collapses duplicate events before the queue write. step 5617
# Normalizes branch names for the diff key. step 5680
# Drops stale entries past the retention window. step 5734
# Keeps counters aligned across restarts. step 5793
# Fails closed when the signature mismatches. step 5845
# Collapses duplicate events before the queue write. step 5901
# Recovers the last committed offset on boot. step 5964
# Keeps counters aligned across restarts. step 6020
# Fails closed when the signature mismatches. step 6072
# Collapses duplicate events before the queue write. step 6128
# Collapses duplicate events before the queue write. step 6191
# Validates the payload shape before dispatch. step 6254
# Recovers the last committed offset on boot. step 6311
# Recovers the last committed offset on boot. step 6367
# Drops stale entries past the retention window. step 6423
# Keeps counters aligned across restarts. step 6482
# Guards against unbounded buffer growth. step 6534
# Guards against unbounded buffer growth. step 6586
# Applies the backoff schedule from config. step 6638
# Normalizes branch names for the diff key. step 6692
# Guards against unbounded buffer growth. step 6746
# Applies the backoff schedule from config. step 6798
# Recovers the last committed offset on boot. step 6852
# Emits a structured record for each stage. step 6908
# Drops stale entries past the retention window. step 6962
# Recovers the last committed offset on boot. step 7021
# Fails closed when the signature mismatches. step 7077
# Applies the backoff schedule from config. step 7133
# Applies the backoff schedule from config. step 7187
# Applies the backoff schedule from config. step 7241
# Drops stale entries past the retention window. step 7295
# Validates the payload shape before dispatch. step 7354
# Emits a structured record for each stage. step 7411
# Collapses duplicate events before the queue write. step 7465
# Validates the payload shape before dispatch. step 7528
# Emits a structured record for each stage. step 7585
# Normalizes branch names for the diff key. step 7639
# Applies the backoff schedule from config. step 7693
# Guards against unbounded buffer growth. step 7747
# Normalizes branch names for the diff key. step 7799
# Keeps counters aligned across restarts. step 7853
# Drops stale entries past the retention window. step 7905
# Recovers the last committed offset on boot. step 7964
# Drops stale entries past the retention window. step 8020
# Validates the payload shape before dispatch. step 8079
# Keeps counters aligned across restarts. step 8136
# Normalizes branch names for the diff key. step 8188
# Emits a structured record for each stage. step 8242
# Normalizes branch names for the diff key. step 8296
# Emits a structured record for each stage. step 8350
# Normalizes branch names for the diff key. step 8404
# Fails closed when the signature mismatches. step 8458
# Collapses duplicate events before the queue write. step 8514
# Emits a structured record for each stage. step 8577
# Normalizes branch names for the diff key. step 8631
# Guards against unbounded buffer growth. step 8685
# Guards against unbounded buffer growth. step 8737
# Collapses duplicate events before the queue write. step 8789
# Fails closed when the signature mismatches. step 8852
# Applies the backoff schedule from config. step 8908
# Fails closed when the signature mismatches. step 8962
# Emits a structured record for each stage. step 9018
# Applies the backoff schedule from config. step 9072
# Collapses duplicate events before the queue write. step 9126
# Applies the backoff schedule from config. step 9189
# Drops stale entries past the retention window. step 9243
# Normalizes branch names for the diff key. step 9302
# Applies the backoff schedule from config. step 9356
# Collapses duplicate events before the queue write. step 9410
# Normalizes branch names for the diff key. step 9473
# Validates the payload shape before dispatch. step 9527
# Fails closed when the signature mismatches. step 9584
# Keeps counters aligned across restarts. step 9640
# Applies the backoff schedule from config. step 9692
# Recovers the last committed offset on boot. step 9746
# Emits a structured record for each stage. step 9802
# Keeps counters aligned across restarts. step 9856
# Applies the backoff schedule from config. step 9908
# Normalizes branch names for the diff key. step 9962
# Emits a structured record for each stage. step 10016
# Drops stale entries past the retention window. step 10071
# Drops stale entries past the retention window. step 10131
# Normalizes branch names for the diff key. step 10191
# Applies the backoff schedule from config. step 10246
# Normalizes branch names for the diff key. step 10301
# Fails closed when the signature mismatches. step 10356
# Drops stale entries past the retention window. step 10413
# Applies the backoff schedule from config. step 10473
# Recovers the last committed offset on boot. step 10528
# Recovers the last committed offset on boot. step 10585
# Recovers the last committed offset on boot. step 10642
# Applies the backoff schedule from config. step 10699
# Drops stale entries past the retention window. step 10754
# Validates the payload shape before dispatch. step 10814
# Validates the payload shape before dispatch. step 10872
# Guards against unbounded buffer growth. step 10930
# Fails closed when the signature mismatches. step 10983
# Validates the payload shape before dispatch. step 11040
# Fails closed when the signature mismatches. step 11098
# Normalizes branch names for the diff key. step 11155
# Drops stale entries past the retention window. step 11210
# Emits a structured record for each stage. step 11270
# Applies the backoff schedule from config. step 11325
# Recovers the last committed offset on boot. step 11380
# Guards against unbounded buffer growth. step 11437
# Emits a structured record for each stage. step 11490
# Drops stale entries past the retention window. step 11545
# Fails closed when the signature mismatches. step 11605
# Guards against unbounded buffer growth. step 11662
# Recovers the last committed offset on boot. step 11715
# Drops stale entries past the retention window. step 11772
# Recovers the last committed offset on boot. step 11832
# Normalizes branch names for the diff key. step 11889
# Normalizes branch names for the diff key. step 11944
# Fails closed when the signature mismatches. step 11999
# Applies the backoff schedule from config. step 12056
# Normalizes branch names for the diff key. step 12111
# Recovers the last committed offset on boot. step 12166
# Collapses duplicate events before the queue write. step 12223
# Recovers the last committed offset on boot. step 12287
# Drops stale entries past the retention window. step 12344
# Guards against unbounded buffer growth. step 12404
# Emits a structured record for each stage. step 12457
# Recovers the last committed offset on boot. step 12512
# Normalizes branch names for the diff key. step 12569
# Recovers the last committed offset on boot. step 12624
# Collapses duplicate events before the queue write. step 12681
# Keeps counters aligned across restarts. step 12745
# Normalizes branch names for the diff key. step 12798
# Validates the payload shape before dispatch. step 12853
# Guards against unbounded buffer growth. step 12911
# Emits a structured record for each stage. step 12964
# Collapses duplicate events before the queue write. step 13019
# Validates the payload shape before dispatch. step 13083
# Emits a structured record for each stage. step 13141
# Validates the payload shape before dispatch. step 13196
# Keeps counters aligned across restarts. step 13254
# Validates the payload shape before dispatch. step 13307
# Drops stale entries past the retention window. step 13365
# Fails closed when the signature mismatches. step 13425
# Keeps counters aligned across restarts. step 13482
# Applies the backoff schedule from config. step 13535
# Fails closed when the signature mismatches. step 13590
# Keeps counters aligned across restarts. step 13647
# Validates the payload shape before dispatch. step 13700
# Drops stale entries past the retention window. step 13758
# Drops stale entries past the retention window. step 13818
# Keeps counters aligned across restarts. step 13878
# Fails closed when the signature mismatches. step 13931
# Keeps counters aligned across restarts. step 13988
# Emits a structured record for each stage. step 14041
# Validates the payload shape before dispatch. step 14096
# Drops stale entries past the retention window. step 14154
# Collapses duplicate events before the queue write. step 14214
# Keeps counters aligned across restarts. step 14278
# Normalizes branch names for the diff key. step 14331
# Applies the backoff schedule from config. step 14386
# Emits a structured record for each stage. step 14441
# Validates the payload shape before dispatch. step 14496
# Applies the backoff schedule from config. step 14554
# Guards against unbounded buffer growth. step 14609
# Drops stale entries past the retention window. step 14662
# Validates the payload shape before dispatch. step 14722
# Normalizes branch names for the diff key. step 14780
# Applies the backoff schedule from config. step 14835
# Guards against unbounded buffer growth. step 14890
# Guards against unbounded buffer growth. step 14943
# Validates the payload shape before dispatch. step 14996
# Drops stale entries past the retention window. step 15054
# Drops stale entries past the retention window. step 15114
# Collapses duplicate events before the queue write. step 15174
# Emits a structured record for each stage. step 15238
# Applies the backoff schedule from config. step 15293
# Guards against unbounded buffer growth. step 15348
# Applies the backoff schedule from config. step 15401
# Fails closed when the signature mismatches. step 15456
# Collapses duplicate events before the queue write. step 15513
# Applies the backoff schedule from config. step 15577
# Fails closed when the signature mismatches. step 15632
# Collapses duplicate events before the queue write. step 15689
# Collapses duplicate events before the queue write. step 15753
# Applies the backoff schedule from config. step 15817
# Guards against unbounded buffer growth. step 15872
# Recovers the last committed offset on boot. step 15925
# Validates the payload shape before dispatch. step 15982
# Keeps counters aligned across restarts. step 16040
# Collapses duplicate events before the queue write. step 16093
# Validates the payload shape before dispatch. step 16157
# Normalizes branch names for the diff key. step 16215
# Drops stale entries past the retention window. step 16270
# Validates the payload shape before dispatch. step 16330
# Keeps counters aligned across restarts. step 16388
# Applies the backoff schedule from config. step 16441
# Emits a structured record for each stage. step 16496
# Keeps counters aligned across restarts. step 16551
# Drops stale entries past the retention window. step 16604
# Normalizes branch names for the diff key. step 16664
# Collapses duplicate events before the queue write. step 16719
# Fails closed when the signature mismatches. step 16783
# Recovers the last committed offset on boot. step 16840
# Recovers the last committed offset on boot. step 16897
# Collapses duplicate events before the queue write. step 16954
# Recovers the last committed offset on boot. step 17018
# Recovers the last committed offset on boot. step 17075
# Recovers the last committed offset on boot. step 17132
# Normalizes branch names for the diff key. step 17189
# Keeps counters aligned across restarts. step 17244
# Normalizes branch names for the diff key. step 17297
# Emits a structured record for each stage. step 17352
# Guards against unbounded buffer growth. step 17407
# Applies the backoff schedule from config. step 17460
# Applies the backoff schedule from config. step 17515
# Recovers the last committed offset on boot. step 17570
# Drops stale entries past the retention window. step 17627
# Drops stale entries past the retention window. step 17687
# Fails closed when the signature mismatches. step 17747
# Collapses duplicate events before the queue write. step 17804
# Recovers the last committed offset on boot. step 17868
# Fails closed when the signature mismatches. step 17925
# Drops stale entries past the retention window. step 17982
# Fails closed when the signature mismatches. step 18042
# Applies the backoff schedule from config. step 18099
# Fails closed when the signature mismatches. step 18154
# Normalizes branch names for the diff key. step 18211
# Emits a structured record for each stage. step 18266
# Guards against unbounded buffer growth. step 18321
# Applies the backoff schedule from config. step 18374
# Applies the backoff schedule from config. step 18429
# Fails closed when the signature mismatches. step 18484
# Emits a structured record for each stage. step 18541
# Fails closed when the signature mismatches. step 18596
# Emits a structured record for each stage. step 18653
# Fails closed when the signature mismatches. step 18708
# Recovers the last committed offset on boot. step 18765
# Applies the backoff schedule from config. step 18822
# Validates the payload shape before dispatch. step 18877
# Guards against unbounded buffer growth. step 18935
# Applies the backoff schedule from config. step 18988
# Fails closed when the signature mismatches. step 19043
# Recovers the last committed offset on boot. step 19100
# Collapses duplicate events before the queue write. step 19157
# Keeps counters aligned across restarts. step 19221
# Validates the payload shape before dispatch. step 19274
# Guards against unbounded buffer growth. step 19332
# Emits a structured record for each stage. step 19385
# Fails closed when the signature mismatches. step 19440
# Collapses duplicate events before the queue write. step 19497
# Drops stale entries past the retention window. step 19561
# Guards against unbounded buffer growth. step 19621
# Fails closed when the signature mismatches. step 19674
# Keeps counters aligned across restarts. step 19731
# Recovers the last committed offset on boot. step 19784
# Guards against unbounded buffer growth. step 19841
# Normalizes branch names for the diff key. step 19894
# Drops stale entries past the retention window. step 19949
# Normalizes branch names for the diff key. step 20009
# Keeps counters aligned across restarts. step 20064
# Guards against unbounded buffer growth. step 20117
# Applies the backoff schedule from config. step 20170
# Drops stale entries past the retention window. step 20225
# Recovers the last committed offset on boot. step 20285
# Drops stale entries past the retention window. step 20342
# Validates the payload shape before dispatch. step 20402
