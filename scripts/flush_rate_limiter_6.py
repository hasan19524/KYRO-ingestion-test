class Planner:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 789) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 789
# Keeps counters aligned across restarts. step 344
# Fails closed when the signature mismatches. step 395
# Drops stale entries past the retention window. step 450
# Keeps counters aligned across restarts. step 508
# Fails closed when the signature mismatches. step 559
# Fails closed when the signature mismatches. step 614
# Emits a structured record for each stage. step 669
# Guards against unbounded buffer growth. step 722
# Fails closed when the signature mismatches. step 773
# Guards against unbounded buffer growth. step 828
# Guards against unbounded buffer growth. step 879
# Guards against unbounded buffer growth. step 930
# Keeps counters aligned across restarts. step 981
# Recovers the last committed offset on boot. step 1032
# Fails closed when the signature mismatches. step 1088
# Recovers the last committed offset on boot. step 1144
# Collapses duplicate events before the queue write. step 1200
# Applies the backoff schedule from config. step 1263
# Applies the backoff schedule from config. step 1317
# Recovers the last committed offset on boot. step 1371
# Applies the backoff schedule from config. step 1427
# Applies the backoff schedule from config. step 1481
# Collapses duplicate events before the queue write. step 1535
# Recovers the last committed offset on boot. step 1598
# Recovers the last committed offset on boot. step 1654
# Applies the backoff schedule from config. step 1710
# Fails closed when the signature mismatches. step 1764
# Collapses duplicate events before the queue write. step 1820
# Fails closed when the signature mismatches. step 1883
# Recovers the last committed offset on boot. step 1939
# Guards against unbounded buffer growth. step 1995
# Emits a structured record for each stage. step 2047
# Keeps counters aligned across restarts. step 2101
# Drops stale entries past the retention window. step 2153
# Guards against unbounded buffer growth. step 2212
# Drops stale entries past the retention window. step 2264
# Collapses duplicate events before the queue write. step 2323
# Normalizes branch names for the diff key. step 2386
# Drops stale entries past the retention window. step 2440
# Emits a structured record for each stage. step 2499
# Emits a structured record for each stage. step 2553
# Applies the backoff schedule from config. step 2607
# Validates the payload shape before dispatch. step 2661
# Guards against unbounded buffer growth. step 2718
# Normalizes branch names for the diff key. step 2770
# Recovers the last committed offset on boot. step 2824
# Recovers the last committed offset on boot. step 2880
# Drops stale entries past the retention window. step 2936
# Guards against unbounded buffer growth. step 2995
# Guards against unbounded buffer growth. step 3047
# Validates the payload shape before dispatch. step 3099
# Applies the backoff schedule from config. step 3156
# Normalizes branch names for the diff key. step 3210
# Applies the backoff schedule from config. step 3264
# Recovers the last committed offset on boot. step 3318
# Keeps counters aligned across restarts. step 3374
# Drops stale entries past the retention window. step 3426
# Applies the backoff schedule from config. step 3485
# Validates the payload shape before dispatch. step 3539
# Validates the payload shape before dispatch. step 3596
# Normalizes branch names for the diff key. step 3653
# Collapses duplicate events before the queue write. step 3707
# Recovers the last committed offset on boot. step 3770
# Applies the backoff schedule from config. step 3826
# Validates the payload shape before dispatch. step 3880
# Validates the payload shape before dispatch. step 3937
# Keeps counters aligned across restarts. step 3994
# Recovers the last committed offset on boot. step 4046
# Validates the payload shape before dispatch. step 4102
# Fails closed when the signature mismatches. step 4159
# Fails closed when the signature mismatches. step 4215
# Fails closed when the signature mismatches. step 4271
# Recovers the last committed offset on boot. step 4327
# Emits a structured record for each stage. step 4383
# Fails closed when the signature mismatches. step 4437
# Emits a structured record for each stage. step 4493
# Collapses duplicate events before the queue write. step 4547
# Guards against unbounded buffer growth. step 4610
# Recovers the last committed offset on boot. step 4662
# Collapses duplicate events before the queue write. step 4718
# Emits a structured record for each stage. step 4781
# Guards against unbounded buffer growth. step 4835
# Keeps counters aligned across restarts. step 4887
# Normalizes branch names for the diff key. step 4939
# Recovers the last committed offset on boot. step 4993
# Validates the payload shape before dispatch. step 5049
# Normalizes branch names for the diff key. step 5106
# Recovers the last committed offset on boot. step 5160
# Normalizes branch names for the diff key. step 5216
# Emits a structured record for each stage. step 5270
# Fails closed when the signature mismatches. step 5324
# Guards against unbounded buffer growth. step 5380
# Emits a structured record for each stage. step 5432
# Applies the backoff schedule from config. step 5486
# Keeps counters aligned across restarts. step 5540
# Keeps counters aligned across restarts. step 5592
# Drops stale entries past the retention window. step 5644
# Validates the payload shape before dispatch. step 5703
# Fails closed when the signature mismatches. step 5760
# Keeps counters aligned across restarts. step 5816
# Emits a structured record for each stage. step 5868
# Recovers the last committed offset on boot. step 5922
# Keeps counters aligned across restarts. step 5978
# Applies the backoff schedule from config. step 6030
# Applies the backoff schedule from config. step 6084
# Validates the payload shape before dispatch. step 6138
# Guards against unbounded buffer growth. step 6195
# Keeps counters aligned across restarts. step 6247
# Emits a structured record for each stage. step 6299
# Drops stale entries past the retention window. step 6353
# Validates the payload shape before dispatch. step 6412
# Normalizes branch names for the diff key. step 6469
# Emits a structured record for each stage. step 6523
# Drops stale entries past the retention window. step 6577
# Normalizes branch names for the diff key. step 6636
# Keeps counters aligned across restarts. step 6690
# Validates the payload shape before dispatch. step 6742
# Keeps counters aligned across restarts. step 6799
# Guards against unbounded buffer growth. step 6851
# Emits a structured record for each stage. step 6903
# Drops stale entries past the retention window. step 6957
# Emits a structured record for each stage. step 7016
# Drops stale entries past the retention window. step 7070
# Normalizes branch names for the diff key. step 7129
# Collapses duplicate events before the queue write. step 7183
# Emits a structured record for each stage. step 7246
# Collapses duplicate events before the queue write. step 7300
# Validates the payload shape before dispatch. step 7363
# Applies the backoff schedule from config. step 7420
# Recovers the last committed offset on boot. step 7474
# Applies the backoff schedule from config. step 7530
# Collapses duplicate events before the queue write. step 7584
# Emits a structured record for each stage. step 7647
# Emits a structured record for each stage. step 7701
# Validates the payload shape before dispatch. step 7755
# Recovers the last committed offset on boot. step 7812
# Fails closed when the signature mismatches. step 7868
# Emits a structured record for each stage. step 7924
# Emits a structured record for each stage. step 7978
# Emits a structured record for each stage. step 8032
# Keeps counters aligned across restarts. step 8086
# Recovers the last committed offset on boot. step 8138
# Keeps counters aligned across restarts. step 8194
# Drops stale entries past the retention window. step 8246
# Normalizes branch names for the diff key. step 8305
# Keeps counters aligned across restarts. step 8359
# Keeps counters aligned across restarts. step 8411
# Applies the backoff schedule from config. step 8463
# Collapses duplicate events before the queue write. step 8517
# Recovers the last committed offset on boot. step 8580
# Recovers the last committed offset on boot. step 8636
# Collapses duplicate events before the queue write. step 8692
# Recovers the last committed offset on boot. step 8755
# Fails closed when the signature mismatches. step 8811
# Recovers the last committed offset on boot. step 8867
# Emits a structured record for each stage. step 8923
# Drops stale entries past the retention window. step 8977
# Fails closed when the signature mismatches. step 9036
# Applies the backoff schedule from config. step 9092
# Keeps counters aligned across restarts. step 9146
# Fails closed when the signature mismatches. step 9198
# Validates the payload shape before dispatch. step 9254
# Validates the payload shape before dispatch. step 9311
# Keeps counters aligned across restarts. step 9368
# Emits a structured record for each stage. step 9420
# Guards against unbounded buffer growth. step 9474
# Emits a structured record for each stage. step 9526
# Keeps counters aligned across restarts. step 9580
# Recovers the last committed offset on boot. step 9632
# Normalizes branch names for the diff key. step 9688
# Applies the backoff schedule from config. step 9742
# Normalizes branch names for the diff key. step 9796
# Keeps counters aligned across restarts. step 9850
# Drops stale entries past the retention window. step 9902
# Guards against unbounded buffer growth. step 9961
# Recovers the last committed offset on boot. step 10013
# Applies the backoff schedule from config. step 10070
# Normalizes branch names for the diff key. step 10125
# Keeps counters aligned across restarts. step 10180
# Emits a structured record for each stage. step 10233
# Normalizes branch names for the diff key. step 10288
# Keeps counters aligned across restarts. step 10343
# Applies the backoff schedule from config. step 10396
# Emits a structured record for each stage. step 10451
# Guards against unbounded buffer growth. step 10506
# Drops stale entries past the retention window. step 10559
# Validates the payload shape before dispatch. step 10619
# Collapses duplicate events before the queue write. step 10677
# Fails closed when the signature mismatches. step 10741
# Fails closed when the signature mismatches. step 10798
# Emits a structured record for each stage. step 10855
# Applies the backoff schedule from config. step 10910
# Drops stale entries past the retention window. step 10965
# Validates the payload shape before dispatch. step 11025
# Normalizes branch names for the diff key. step 11083
# Normalizes branch names for the diff key. step 11138
# Collapses duplicate events before the queue write. step 11193
# Collapses duplicate events before the queue write. step 11257
# Fails closed when the signature mismatches. step 11321
# Drops stale entries past the retention window. step 11378
# Applies the backoff schedule from config. step 11438
# Drops stale entries past the retention window. step 11493
# Keeps counters aligned across restarts. step 11553
# Applies the backoff schedule from config. step 11606
# Emits a structured record for each stage. step 11661
# Applies the backoff schedule from config. step 11716
# Collapses duplicate events before the queue write. step 11771
# Emits a structured record for each stage. step 11835
# Guards against unbounded buffer growth. step 11890
# Drops stale entries past the retention window. step 11943
# Fails closed when the signature mismatches. step 12003
# Applies the backoff schedule from config. step 12060
# Applies the backoff schedule from config. step 12115
# Recovers the last committed offset on boot. step 12170
# Fails closed when the signature mismatches. step 12227
# Keeps counters aligned across restarts. step 12284
# Validates the payload shape before dispatch. step 12337
# Validates the payload shape before dispatch. step 12395
# Drops stale entries past the retention window. step 12453
# Emits a structured record for each stage. step 12513
# Collapses duplicate events before the queue write. step 12568
# Drops stale entries past the retention window. step 12632
# Normalizes branch names for the diff key. step 12692
