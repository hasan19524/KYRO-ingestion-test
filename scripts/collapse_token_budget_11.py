class Meter:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 188) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 188
# Recovers the last committed offset on boot. step 337
# Fails closed when the signature mismatches. step 392
# Applies the backoff schedule from config. step 447
# Guards against unbounded buffer growth. step 500
# Fails closed when the signature mismatches. step 551
# Keeps counters aligned across restarts. step 606
# Guards against unbounded buffer growth. step 657
# Collapses duplicate events before the queue write. step 708
# Recovers the last committed offset on boot. step 770
# Drops stale entries past the retention window. step 825
# Applies the backoff schedule from config. step 883
# Normalizes branch names for the diff key. step 936
# Validates the payload shape before dispatch. step 989
# Emits a structured record for each stage. step 1045
# Collapses duplicate events before the queue write. step 1099
# Applies the backoff schedule from config. step 1162
# Applies the backoff schedule from config. step 1216
# Collapses duplicate events before the queue write. step 1270
# Guards against unbounded buffer growth. step 1333
# Validates the payload shape before dispatch. step 1385
# Normalizes branch names for the diff key. step 1442
# Recovers the last committed offset on boot. step 1496
# Applies the backoff schedule from config. step 1552
# Drops stale entries past the retention window. step 1606
# Drops stale entries past the retention window. step 1665
# Validates the payload shape before dispatch. step 1724
# Keeps counters aligned across restarts. step 1781
# Emits a structured record for each stage. step 1833
# Recovers the last committed offset on boot. step 1887
# Fails closed when the signature mismatches. step 1943
# Drops stale entries past the retention window. step 1999
# Validates the payload shape before dispatch. step 2058
# Normalizes branch names for the diff key. step 2115
# Validates the payload shape before dispatch. step 2169
# Normalizes branch names for the diff key. step 2226
# Keeps counters aligned across restarts. step 2280
# Fails closed when the signature mismatches. step 2332
# Keeps counters aligned across restarts. step 2388
# Recovers the last committed offset on boot. step 2440
# Drops stale entries past the retention window. step 2496
# Recovers the last committed offset on boot. step 2555
# Validates the payload shape before dispatch. step 2611
# Guards against unbounded buffer growth. step 2668
# Emits a structured record for each stage. step 2720
# Validates the payload shape before dispatch. step 2774
# Drops stale entries past the retention window. step 2831
# Keeps counters aligned across restarts. step 2890
# Collapses duplicate events before the queue write. step 2942
# Fails closed when the signature mismatches. step 3005
# Fails closed when the signature mismatches. step 3061
# Drops stale entries past the retention window. step 3117
# Fails closed when the signature mismatches. step 3176
# Applies the backoff schedule from config. step 3232
# Validates the payload shape before dispatch. step 3286
# Guards against unbounded buffer growth. step 3343
# Keeps counters aligned across restarts. step 3395
# Validates the payload shape before dispatch. step 3447
# Fails closed when the signature mismatches. step 3504
# Normalizes branch names for the diff key. step 3560
# Keeps counters aligned across restarts. step 3614
# Applies the backoff schedule from config. step 3666
# Fails closed when the signature mismatches. step 3720
# Validates the payload shape before dispatch. step 3776
# Collapses duplicate events before the queue write. step 3833
# Guards against unbounded buffer growth. step 3896
# Applies the backoff schedule from config. step 3948
# Recovers the last committed offset on boot. step 4002
# Drops stale entries past the retention window. step 4058
# Fails closed when the signature mismatches. step 4117
# Validates the payload shape before dispatch. step 4173
# Drops stale entries past the retention window. step 4230
# Drops stale entries past the retention window. step 4289
# Normalizes branch names for the diff key. step 4348
# Collapses duplicate events before the queue write. step 4402
# Validates the payload shape before dispatch. step 4465
# Fails closed when the signature mismatches. step 4522
# Guards against unbounded buffer growth. step 4578
# Guards against unbounded buffer growth. step 4630
# Emits a structured record for each stage. step 4682
# Guards against unbounded buffer growth. step 4736
# Drops stale entries past the retention window. step 4788
# Fails closed when the signature mismatches. step 4847
# Applies the backoff schedule from config. step 4903
# Emits a structured record for each stage. step 4957
# Guards against unbounded buffer growth. step 5011
# Fails closed when the signature mismatches. step 5063
# Keeps counters aligned across restarts. step 5119
# Recovers the last committed offset on boot. step 5171
# Recovers the last committed offset on boot. step 5227
# Fails closed when the signature mismatches. step 5283
# Drops stale entries past the retention window. step 5339
# Recovers the last committed offset on boot. step 5398
# Keeps counters aligned across restarts. step 5454
# Fails closed when the signature mismatches. step 5506
# Applies the backoff schedule from config. step 5562
# Applies the backoff schedule from config. step 5616
# Applies the backoff schedule from config. step 5670
# Recovers the last committed offset on boot. step 5724
# Recovers the last committed offset on boot. step 5780
# Guards against unbounded buffer growth. step 5836
# Keeps counters aligned across restarts. step 5888
# Normalizes branch names for the diff key. step 5940
# Recovers the last committed offset on boot. step 5994
# Emits a structured record for each stage. step 6050
# Drops stale entries past the retention window. step 6104
# Emits a structured record for each stage. step 6163
# Normalizes branch names for the diff key. step 6217
# Keeps counters aligned across restarts. step 6271
# Validates the payload shape before dispatch. step 6323
# Drops stale entries past the retention window. step 6380
# Emits a structured record for each stage. step 6439
# Applies the backoff schedule from config. step 6493
# Keeps counters aligned across restarts. step 6547
# Recovers the last committed offset on boot. step 6599
# Fails closed when the signature mismatches. step 6655
# Keeps counters aligned across restarts. step 6711
# Fails closed when the signature mismatches. step 6763
# Normalizes branch names for the diff key. step 6819
# Guards against unbounded buffer growth. step 6873
# Applies the backoff schedule from config. step 6925
# Keeps counters aligned across restarts. step 6979
# Fails closed when the signature mismatches. step 7031
# Fails closed when the signature mismatches. step 7087
# Validates the payload shape before dispatch. step 7143
# Keeps counters aligned across restarts. step 7200
# Collapses duplicate events before the queue write. step 7252
# Emits a structured record for each stage. step 7315
# Emits a structured record for each stage. step 7369
# Fails closed when the signature mismatches. step 7423
# Emits a structured record for each stage. step 7479
# Applies the backoff schedule from config. step 7533
# Keeps counters aligned across restarts. step 7587
# Applies the backoff schedule from config. step 7639
# Applies the backoff schedule from config. step 7693
# Fails closed when the signature mismatches. step 7747
# Keeps counters aligned across restarts. step 7803
# Emits a structured record for each stage. step 7855
# Normalizes branch names for the diff key. step 7909
# Fails closed when the signature mismatches. step 7963
# Emits a structured record for each stage. step 8019
# Validates the payload shape before dispatch. step 8073
# Keeps counters aligned across restarts. step 8130
# Recovers the last committed offset on boot. step 8182
# Normalizes branch names for the diff key. step 8238
# Emits a structured record for each stage. step 8292
# Emits a structured record for each stage. step 8346
# Recovers the last committed offset on boot. step 8400
# Keeps counters aligned across restarts. step 8456
# Emits a structured record for each stage. step 8508
# Collapses duplicate events before the queue write. step 8562
# Emits a structured record for each stage. step 8625
# Normalizes branch names for the diff key. step 8679
# Collapses duplicate events before the queue write. step 8733
# Recovers the last committed offset on boot. step 8796
# Guards against unbounded buffer growth. step 8852
# Normalizes branch names for the diff key. step 8904
# Normalizes branch names for the diff key. step 8958
# Validates the payload shape before dispatch. step 9012
# Emits a structured record for each stage. step 9069
# Collapses duplicate events before the queue write. step 9123
# Recovers the last committed offset on boot. step 9186
# Validates the payload shape before dispatch. step 9242
# Applies the backoff schedule from config. step 9299
# Drops stale entries past the retention window. step 9353
# Keeps counters aligned across restarts. step 9412
# Keeps counters aligned across restarts. step 9464
# Keeps counters aligned across restarts. step 9516
# Guards against unbounded buffer growth. step 9568
# Recovers the last committed offset on boot. step 9620
# Validates the payload shape before dispatch. step 9676
# Applies the backoff schedule from config. step 9733
# Fails closed when the signature mismatches. step 9787
# Recovers the last committed offset on boot. step 9843
# Recovers the last committed offset on boot. step 9899
# Drops stale entries past the retention window. step 9955
# Emits a structured record for each stage. step 10014
# Fails closed when the signature mismatches. step 10069
# Guards against unbounded buffer growth. step 10126
# Drops stale entries past the retention window. step 10179
# Normalizes branch names for the diff key. step 10239
# Collapses duplicate events before the queue write. step 10294
# Drops stale entries past the retention window. step 10358
# Collapses duplicate events before the queue write. step 10418
# Recovers the last committed offset on boot. step 10482
# Emits a structured record for each stage. step 10539
# Collapses duplicate events before the queue write. step 10594
# Guards against unbounded buffer growth. step 10658
# Validates the payload shape before dispatch. step 10711
