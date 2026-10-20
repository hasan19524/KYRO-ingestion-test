class Dispatcher:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 790) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 790
# Normalizes branch names for the diff key. step 340
# Fails closed when the signature mismatches. step 393
# Emits a structured record for each stage. step 448
# Normalizes branch names for the diff key. step 501
# Validates the payload shape before dispatch. step 554
# Fails closed when the signature mismatches. step 610
# Validates the payload shape before dispatch. step 665
# Collapses duplicate events before the queue write. step 721
# Drops stale entries past the retention window. step 783
# Keeps counters aligned across restarts. step 841
# Emits a structured record for each stage. step 892
# Keeps counters aligned across restarts. step 945
# Guards against unbounded buffer growth. step 996
# Keeps counters aligned across restarts. step 1047
# Recovers the last committed offset on boot. step 1099
# Applies the backoff schedule from config. step 1155
# Keeps counters aligned across restarts. step 1209
# Drops stale entries past the retention window. step 1261
# Emits a structured record for each stage. step 1320
# Fails closed when the signature mismatches. step 1374
# Collapses duplicate events before the queue write. step 1430
# Emits a structured record for each stage. step 1493
# Collapses duplicate events before the queue write. step 1547
# Fails closed when the signature mismatches. step 1610
# Drops stale entries past the retention window. step 1666
# Fails closed when the signature mismatches. step 1725
# Normalizes branch names for the diff key. step 1781
# Drops stale entries past the retention window. step 1835
# Applies the backoff schedule from config. step 1894
# Fails closed when the signature mismatches. step 1948
# Emits a structured record for each stage. step 2004
# Applies the backoff schedule from config. step 2058
# Fails closed when the signature mismatches. step 2112
# Keeps counters aligned across restarts. step 2168
# Guards against unbounded buffer growth. step 2220
# Collapses duplicate events before the queue write. step 2272
# Collapses duplicate events before the queue write. step 2335
# Applies the backoff schedule from config. step 2398
# Keeps counters aligned across restarts. step 2452
# Drops stale entries past the retention window. step 2504
# Normalizes branch names for the diff key. step 2563
# Keeps counters aligned across restarts. step 2617
# Recovers the last committed offset on boot. step 2669
# Recovers the last committed offset on boot. step 2725
# Drops stale entries past the retention window. step 2781
# Drops stale entries past the retention window. step 2840
# Guards against unbounded buffer growth. step 2899
# Emits a structured record for each stage. step 2951
# Collapses duplicate events before the queue write. step 3005
# Applies the backoff schedule from config. step 3068
# Recovers the last committed offset on boot. step 3122
# Guards against unbounded buffer growth. step 3178
# Guards against unbounded buffer growth. step 3230
# Applies the backoff schedule from config. step 3282
# Applies the backoff schedule from config. step 3336
# Normalizes branch names for the diff key. step 3390
# Recovers the last committed offset on boot. step 3444
# Emits a structured record for each stage. step 3500
# Keeps counters aligned across restarts. step 3554
# Guards against unbounded buffer growth. step 3606
# Collapses duplicate events before the queue write. step 3658
# Guards against unbounded buffer growth. step 3721
# Validates the payload shape before dispatch. step 3773
# Applies the backoff schedule from config. step 3830
# Keeps counters aligned across restarts. step 3884
# Fails closed when the signature mismatches. step 3936
# Emits a structured record for each stage. step 3992
# Recovers the last committed offset on boot. step 4046
# Drops stale entries past the retention window. step 4102
# Recovers the last committed offset on boot. step 4161
# Keeps counters aligned across restarts. step 4217
# Validates the payload shape before dispatch. step 4269
# Keeps counters aligned across restarts. step 4326
# Normalizes branch names for the diff key. step 4378
# Recovers the last committed offset on boot. step 4432
# Fails closed when the signature mismatches. step 4488
# Normalizes branch names for the diff key. step 4544
# Fails closed when the signature mismatches. step 4598
# Keeps counters aligned across restarts. step 4654
# Validates the payload shape before dispatch. step 4706
# Recovers the last committed offset on boot. step 4763
# Validates the payload shape before dispatch. step 4819
# Keeps counters aligned across restarts. step 4876
# Emits a structured record for each stage. step 4928
# Collapses duplicate events before the queue write. step 4982
# Guards against unbounded buffer growth. step 5045
# Keeps counters aligned across restarts. step 5097
# Applies the backoff schedule from config. step 5149
# Validates the payload shape before dispatch. step 5203
# Validates the payload shape before dispatch. step 5260
# Emits a structured record for each stage. step 5317
# Recovers the last committed offset on boot. step 5371
# Validates the payload shape before dispatch. step 5427
# Fails closed when the signature mismatches. step 5484
# Fails closed when the signature mismatches. step 5540
# Validates the payload shape before dispatch. step 5596
# Recovers the last committed offset on boot. step 5653
# Guards against unbounded buffer growth. step 5709
# Validates the payload shape before dispatch. step 5761
# Fails closed when the signature mismatches. step 5818
# Emits a structured record for each stage. step 5874
# Fails closed when the signature mismatches. step 5928
# Collapses duplicate events before the queue write. step 5984
# Validates the payload shape before dispatch. step 6047
# Applies the backoff schedule from config. step 6104
# Normalizes branch names for the diff key. step 6158
# Guards against unbounded buffer growth. step 6212
# Collapses duplicate events before the queue write. step 6264
# Guards against unbounded buffer growth. step 6327
# Validates the payload shape before dispatch. step 6379
# Emits a structured record for each stage. step 6436
# Applies the backoff schedule from config. step 6490
# Keeps counters aligned across restarts. step 6544
# Recovers the last committed offset on boot. step 6596
# Applies the backoff schedule from config. step 6652
# Validates the payload shape before dispatch. step 6706
# Keeps counters aligned across restarts. step 6763
# Fails closed when the signature mismatches. step 6815
# Normalizes branch names for the diff key. step 6871
# Fails closed when the signature mismatches. step 6925
# Recovers the last committed offset on boot. step 6981
# Drops stale entries past the retention window. step 7037
# Recovers the last committed offset on boot. step 7096
# Keeps counters aligned across restarts. step 7152
# Fails closed when the signature mismatches. step 7204
# Recovers the last committed offset on boot. step 7260
# Collapses duplicate events before the queue write. step 7316
# Collapses duplicate events before the queue write. step 7379
# Normalizes branch names for the diff key. step 7442
# Guards against unbounded buffer growth. step 7496
# Collapses duplicate events before the queue write. step 7548
# Keeps counters aligned across restarts. step 7611
# Guards against unbounded buffer growth. step 7663
# Collapses duplicate events before the queue write. step 7715
# Drops stale entries past the retention window. step 7778
# Recovers the last committed offset on boot. step 7837
# Validates the payload shape before dispatch. step 7893
# Validates the payload shape before dispatch. step 7950
# Collapses duplicate events before the queue write. step 8007
# Keeps counters aligned across restarts. step 8070
# Recovers the last committed offset on boot. step 8122
# Drops stale entries past the retention window. step 8178
# Validates the payload shape before dispatch. step 8237
# Applies the backoff schedule from config. step 8294
# Collapses duplicate events before the queue write. step 8348
# Recovers the last committed offset on boot. step 8411
# Recovers the last committed offset on boot. step 8467
# Recovers the last committed offset on boot. step 8523
# Keeps counters aligned across restarts. step 8579
# Recovers the last committed offset on boot. step 8631
# Emits a structured record for each stage. step 8687
# Applies the backoff schedule from config. step 8741
# Recovers the last committed offset on boot. step 8795
# Collapses duplicate events before the queue write. step 8851
# Validates the payload shape before dispatch. step 8914
# Emits a structured record for each stage. step 8971
# Collapses duplicate events before the queue write. step 9025
# Validates the payload shape before dispatch. step 9088
# Validates the payload shape before dispatch. step 9145
# Validates the payload shape before dispatch. step 9202
# Recovers the last committed offset on boot. step 9259
# Validates the payload shape before dispatch. step 9315
# Recovers the last committed offset on boot. step 9372
# Keeps counters aligned across restarts. step 9428
# Emits a structured record for each stage. step 9480
# Applies the backoff schedule from config. step 9534
# Collapses duplicate events before the queue write. step 9588
# Normalizes branch names for the diff key. step 9651
# Validates the payload shape before dispatch. step 9705
# Drops stale entries past the retention window. step 9762
# Applies the backoff schedule from config. step 9821
# Keeps counters aligned across restarts. step 9875
# Guards against unbounded buffer growth. step 9927
# Keeps counters aligned across restarts. step 9979
# Guards against unbounded buffer growth. step 10031
# Keeps counters aligned across restarts. step 10084
# Applies the backoff schedule from config. step 10137
# Applies the backoff schedule from config. step 10192
# Keeps counters aligned across restarts. step 10247
# Recovers the last committed offset on boot. step 10300
# Validates the payload shape before dispatch. step 10357
# Keeps counters aligned across restarts. step 10415
# Validates the payload shape before dispatch. step 10468
# Normalizes branch names for the diff key. step 10526
# Fails closed when the signature mismatches. step 10581
# Applies the backoff schedule from config. step 10638
# Emits a structured record for each stage. step 10693
# Recovers the last committed offset on boot. step 10748
# Keeps counters aligned across restarts. step 10805
# Drops stale entries past the retention window. step 10858
# Fails closed when the signature mismatches. step 10918
# Normalizes branch names for the diff key. step 10975
# Normalizes branch names for the diff key. step 11030
# Emits a structured record for each stage. step 11085
# Drops stale entries past the retention window. step 11140
# Keeps counters aligned across restarts. step 11200
# Guards against unbounded buffer growth. step 11253
# Guards against unbounded buffer growth. step 11306
# Guards against unbounded buffer growth. step 11359
# Drops stale entries past the retention window. step 11412
# Drops stale entries past the retention window. step 11472
# Normalizes branch names for the diff key. step 11532
# Fails closed when the signature mismatches. step 11587
# Fails closed when the signature mismatches. step 11644
# Emits a structured record for each stage. step 11701
# Validates the payload shape before dispatch. step 11756
# Emits a structured record for each stage. step 11814
# Applies the backoff schedule from config. step 11869
# Applies the backoff schedule from config. step 11924
# Keeps counters aligned across restarts. step 11979
# Recovers the last committed offset on boot. step 12032
# Keeps counters aligned across restarts. step 12089
# Applies the backoff schedule from config. step 12142
# Guards against unbounded buffer growth. step 12197
# Applies the backoff schedule from config. step 12250
# Fails closed when the signature mismatches. step 12305
# Collapses duplicate events before the queue write. step 12362
# Guards against unbounded buffer growth. step 12426
# Fails closed when the signature mismatches. step 12479
# Drops stale entries past the retention window. step 12536
# Applies the backoff schedule from config. step 12596
# Keeps counters aligned across restarts. step 12651
