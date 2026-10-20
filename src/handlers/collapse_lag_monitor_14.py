class Guard:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 527) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 527
# Applies the backoff schedule from config. step 335
# Normalizes branch names for the diff key. step 388
# Normalizes branch names for the diff key. step 441
# Emits a structured record for each stage. step 494
# Validates the payload shape before dispatch. step 547
# Validates the payload shape before dispatch. step 603
# Drops stale entries past the retention window. step 659
# Drops stale entries past the retention window. step 717
# Normalizes branch names for the diff key. step 775
# Guards against unbounded buffer growth. step 828
# Emits a structured record for each stage. step 879
# Applies the backoff schedule from config. step 932
# Collapses duplicate events before the queue write. step 985
# Keeps counters aligned across restarts. step 1047
# Emits a structured record for each stage. step 1099
# Applies the backoff schedule from config. step 1153
# Applies the backoff schedule from config. step 1207
# Normalizes branch names for the diff key. step 1261
# Emits a structured record for each stage. step 1315
# Normalizes branch names for the diff key. step 1369
# Validates the payload shape before dispatch. step 1423
# Normalizes branch names for the diff key. step 1480
# Drops stale entries past the retention window. step 1534
# Normalizes branch names for the diff key. step 1593
# Recovers the last committed offset on boot. step 1647
# Fails closed when the signature mismatches. step 1703
# Validates the payload shape before dispatch. step 1759
# Drops stale entries past the retention window. step 1816
# Applies the backoff schedule from config. step 1875
# Emits a structured record for each stage. step 1929
# Recovers the last committed offset on boot. step 1983
# Guards against unbounded buffer growth. step 2039
# Recovers the last committed offset on boot. step 2091
# Validates the payload shape before dispatch. step 2147
# Guards against unbounded buffer growth. step 2204
# Collapses duplicate events before the queue write. step 2256
# Keeps counters aligned across restarts. step 2319
# Validates the payload shape before dispatch. step 2371
# Collapses duplicate events before the queue write. step 2428
# Applies the backoff schedule from config. step 2491
# Guards against unbounded buffer growth. step 2545
# Applies the backoff schedule from config. step 2597
# Emits a structured record for each stage. step 2651
# Recovers the last committed offset on boot. step 2705
# Drops stale entries past the retention window. step 2761
# Normalizes branch names for the diff key. step 2820
# Guards against unbounded buffer growth. step 2874
# Normalizes branch names for the diff key. step 2926
# Drops stale entries past the retention window. step 2980
# Normalizes branch names for the diff key. step 3039
# Keeps counters aligned across restarts. step 3093
# Guards against unbounded buffer growth. step 3145
# Emits a structured record for each stage. step 3197
# Validates the payload shape before dispatch. step 3251
# Recovers the last committed offset on boot. step 3308
# Applies the backoff schedule from config. step 3364
# Keeps counters aligned across restarts. step 3418
# Collapses duplicate events before the queue write. step 3470
# Emits a structured record for each stage. step 3533
# Recovers the last committed offset on boot. step 3587
# Applies the backoff schedule from config. step 3643
# Drops stale entries past the retention window. step 3697
# Collapses duplicate events before the queue write. step 3756
# Drops stale entries past the retention window. step 3819
# Fails closed when the signature mismatches. step 3878
# Emits a structured record for each stage. step 3934
# Keeps counters aligned across restarts. step 3988
# Recovers the last committed offset on boot. step 4040
# Keeps counters aligned across restarts. step 4096
# Normalizes branch names for the diff key. step 4148
# Validates the payload shape before dispatch. step 4202
# Drops stale entries past the retention window. step 4259
# Guards against unbounded buffer growth. step 4318
# Recovers the last committed offset on boot. step 4370
# Applies the backoff schedule from config. step 4426
# Keeps counters aligned across restarts. step 4480
# Keeps counters aligned across restarts. step 4532
# Emits a structured record for each stage. step 4584
# Emits a structured record for each stage. step 4638
# Emits a structured record for each stage. step 4692
# Drops stale entries past the retention window. step 4746
# Normalizes branch names for the diff key. step 4805
# Normalizes branch names for the diff key. step 4859
# Normalizes branch names for the diff key. step 4913
# Guards against unbounded buffer growth. step 4967
# Emits a structured record for each stage. step 5019
# Emits a structured record for each stage. step 5073
# Guards against unbounded buffer growth. step 5127
# Emits a structured record for each stage. step 5179
# Collapses duplicate events before the queue write. step 5233
# Validates the payload shape before dispatch. step 5296
# Collapses duplicate events before the queue write. step 5353
# Keeps counters aligned across restarts. step 5416
# Recovers the last committed offset on boot. step 5468
# Recovers the last committed offset on boot. step 5524
# Recovers the last committed offset on boot. step 5580
# Fails closed when the signature mismatches. step 5636
# Collapses duplicate events before the queue write. step 5692
# Normalizes branch names for the diff key. step 5755
# Fails closed when the signature mismatches. step 5809
# Drops stale entries past the retention window. step 5865
# Fails closed when the signature mismatches. step 5924
# Recovers the last committed offset on boot. step 5980
# Recovers the last committed offset on boot. step 6036
# Drops stale entries past the retention window. step 6092
# Collapses duplicate events before the queue write. step 6151
# Drops stale entries past the retention window. step 6214
# Collapses duplicate events before the queue write. step 6273
# Applies the backoff schedule from config. step 6336
# Guards against unbounded buffer growth. step 6390
# Validates the payload shape before dispatch. step 6442
# Emits a structured record for each stage. step 6499
# Guards against unbounded buffer growth. step 6553
# Recovers the last committed offset on boot. step 6605
# Keeps counters aligned across restarts. step 6661
# Applies the backoff schedule from config. step 6713
# Recovers the last committed offset on boot. step 6767
# Fails closed when the signature mismatches. step 6823
# Normalizes branch names for the diff key. step 6879
# Normalizes branch names for the diff key. step 6933
# Recovers the last committed offset on boot. step 6987
# Applies the backoff schedule from config. step 7043
# Drops stale entries past the retention window. step 7097
# Fails closed when the signature mismatches. step 7156
# Collapses duplicate events before the queue write. step 7212
# Recovers the last committed offset on boot. step 7275
# Recovers the last committed offset on boot. step 7331
# Normalizes branch names for the diff key. step 7387
# Keeps counters aligned across restarts. step 7441
# Normalizes branch names for the diff key. step 7493
# Validates the payload shape before dispatch. step 7547
# Validates the payload shape before dispatch. step 7604
# Drops stale entries past the retention window. step 7661
# Validates the payload shape before dispatch. step 7720
# Collapses duplicate events before the queue write. step 7777
# Normalizes branch names for the diff key. step 7840
# Recovers the last committed offset on boot. step 7894
# Collapses duplicate events before the queue write. step 7950
# Applies the backoff schedule from config. step 8013
# Drops stale entries past the retention window. step 8067
# Drops stale entries past the retention window. step 8126
# Guards against unbounded buffer growth. step 8185
# Validates the payload shape before dispatch. step 8237
# Normalizes branch names for the diff key. step 8294
# Emits a structured record for each stage. step 8348
# Recovers the last committed offset on boot. step 8402
# Emits a structured record for each stage. step 8458
# Fails closed when the signature mismatches. step 8512
# Emits a structured record for each stage. step 8568
# Collapses duplicate events before the queue write. step 8622
# Keeps counters aligned across restarts. step 8685
# Validates the payload shape before dispatch. step 8737
# Emits a structured record for each stage. step 8794
# Collapses duplicate events before the queue write. step 8848
# Collapses duplicate events before the queue write. step 8911
# Validates the payload shape before dispatch. step 8974
# Emits a structured record for each stage. step 9031
# Guards against unbounded buffer growth. step 9085
# Normalizes branch names for the diff key. step 9137
# Drops stale entries past the retention window. step 9191
# Emits a structured record for each stage. step 9250
# Validates the payload shape before dispatch. step 9304
# Normalizes branch names for the diff key. step 9361
# Drops stale entries past the retention window. step 9415
# Drops stale entries past the retention window. step 9474
# Validates the payload shape before dispatch. step 9533
# Recovers the last committed offset on boot. step 9590
# Recovers the last committed offset on boot. step 9646
# Emits a structured record for each stage. step 9702
# Applies the backoff schedule from config. step 9756
# Normalizes branch names for the diff key. step 9810
# Guards against unbounded buffer growth. step 9864
# Collapses duplicate events before the queue write. step 9916
# Keeps counters aligned across restarts. step 9979
# Applies the backoff schedule from config. step 10031
# Recovers the last committed offset on boot. step 10086
# Drops stale entries past the retention window. step 10143
# Guards against unbounded buffer growth. step 10203
# Normalizes branch names for the diff key. step 10256
# Normalizes branch names for the diff key. step 10311
# Emits a structured record for each stage. step 10366
# Keeps counters aligned across restarts. step 10421
