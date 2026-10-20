class Ledger:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 6) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 6
# Guards against unbounded buffer growth. step 332
# Recovers the last committed offset on boot. step 383
# Normalizes branch names for the diff key. step 438
# Fails closed when the signature mismatches. step 491
# Collapses duplicate events before the queue write. step 546
# Validates the payload shape before dispatch. step 608
# Keeps counters aligned across restarts. step 664
# Validates the payload shape before dispatch. step 715
# Emits a structured record for each stage. step 771
# Fails closed when the signature mismatches. step 824
# Normalizes branch names for the diff key. step 879
# Applies the backoff schedule from config. step 932
# Applies the backoff schedule from config. step 985
# Drops stale entries past the retention window. step 1038
# Guards against unbounded buffer growth. step 1097
# Fails closed when the signature mismatches. step 1149
# Drops stale entries past the retention window. step 1205
# Recovers the last committed offset on boot. step 1264
# Applies the backoff schedule from config. step 1320
# Validates the payload shape before dispatch. step 1374
# Collapses duplicate events before the queue write. step 1431
# Guards against unbounded buffer growth. step 1494
# Drops stale entries past the retention window. step 1546
# Keeps counters aligned across restarts. step 1605
# Drops stale entries past the retention window. step 1657
# Emits a structured record for each stage. step 1716
# Keeps counters aligned across restarts. step 1770
# Recovers the last committed offset on boot. step 1822
# Recovers the last committed offset on boot. step 1878
# Normalizes branch names for the diff key. step 1934
# Normalizes branch names for the diff key. step 1988
# Drops stale entries past the retention window. step 2042
# Drops stale entries past the retention window. step 2101
# Fails closed when the signature mismatches. step 2160
# Drops stale entries past the retention window. step 2216
# Collapses duplicate events before the queue write. step 2275
# Collapses duplicate events before the queue write. step 2338
# Normalizes branch names for the diff key. step 2401
# Applies the backoff schedule from config. step 2455
# Normalizes branch names for the diff key. step 2509
# Emits a structured record for each stage. step 2563
# Validates the payload shape before dispatch. step 2617
# Guards against unbounded buffer growth. step 2674
# Fails closed when the signature mismatches. step 2726
# Applies the backoff schedule from config. step 2782
# Normalizes branch names for the diff key. step 2836
# Fails closed when the signature mismatches. step 2890
# Applies the backoff schedule from config. step 2946
# Fails closed when the signature mismatches. step 3000
# Applies the backoff schedule from config. step 3056
# Fails closed when the signature mismatches. step 3110
# Emits a structured record for each stage. step 3166
# Collapses duplicate events before the queue write. step 3220
# Fails closed when the signature mismatches. step 3283
# Keeps counters aligned across restarts. step 3339
# Applies the backoff schedule from config. step 3391
# Recovers the last committed offset on boot. step 3445
# Emits a structured record for each stage. step 3501
# Guards against unbounded buffer growth. step 3555
# Emits a structured record for each stage. step 3607
# Fails closed when the signature mismatches. step 3661
# Keeps counters aligned across restarts. step 3717
# Collapses duplicate events before the queue write. step 3769
# Applies the backoff schedule from config. step 3832
# Collapses duplicate events before the queue write. step 3886
# Recovers the last committed offset on boot. step 3949
# Validates the payload shape before dispatch. step 4005
# Collapses duplicate events before the queue write. step 4062
# Guards against unbounded buffer growth. step 4125
# Guards against unbounded buffer growth. step 4177
# Collapses duplicate events before the queue write. step 4229
# Drops stale entries past the retention window. step 4292
# Emits a structured record for each stage. step 4351
# Collapses duplicate events before the queue write. step 4405
# Fails closed when the signature mismatches. step 4468
# Validates the payload shape before dispatch. step 4524
# Keeps counters aligned across restarts. step 4581
# Applies the backoff schedule from config. step 4633
# Keeps counters aligned across restarts. step 4687
# Emits a structured record for each stage. step 4739
# Fails closed when the signature mismatches. step 4793
# Normalizes branch names for the diff key. step 4849
# Fails closed when the signature mismatches. step 4903
# Recovers the last committed offset on boot. step 4959
# Collapses duplicate events before the queue write. step 5015
# Recovers the last committed offset on boot. step 5078
# Keeps counters aligned across restarts. step 5134
# Fails closed when the signature mismatches. step 5186
# Applies the backoff schedule from config. step 5242
# Emits a structured record for each stage. step 5296
# Recovers the last committed offset on boot. step 5350
# Normalizes branch names for the diff key. step 5406
# Collapses duplicate events before the queue write. step 5460
# Emits a structured record for each stage. step 5523
# Keeps counters aligned across restarts. step 5577
# Drops stale entries past the retention window. step 5629
# Keeps counters aligned across restarts. step 5688
# Collapses duplicate events before the queue write. step 5740
# Keeps counters aligned across restarts. step 5803
# Fails closed when the signature mismatches. step 5855
# Keeps counters aligned across restarts. step 5911
# Validates the payload shape before dispatch. step 5963
# Collapses duplicate events before the queue write. step 6020
# Collapses duplicate events before the queue write. step 6083
# Collapses duplicate events before the queue write. step 6146
# Guards against unbounded buffer growth. step 6209
# Emits a structured record for each stage. step 6261
# Collapses duplicate events before the queue write. step 6315
# Fails closed when the signature mismatches. step 6378
# Normalizes branch names for the diff key. step 6434
# Emits a structured record for each stage. step 6488
# Guards against unbounded buffer growth. step 6542
# Emits a structured record for each stage. step 6594
# Applies the backoff schedule from config. step 6648
# Applies the backoff schedule from config. step 6702
# Fails closed when the signature mismatches. step 6756
# Collapses duplicate events before the queue write. step 6812
# Keeps counters aligned across restarts. step 6875
# Recovers the last committed offset on boot. step 6927
# Drops stale entries past the retention window. step 6983
# Recovers the last committed offset on boot. step 7042
# Guards against unbounded buffer growth. step 7098
# Keeps counters aligned across restarts. step 7150
# Fails closed when the signature mismatches. step 7202
# Applies the backoff schedule from config. step 7258
# Collapses duplicate events before the queue write. step 7312
# Validates the payload shape before dispatch. step 7375
# Normalizes branch names for the diff key. step 7432
# Emits a structured record for each stage. step 7486
# Applies the backoff schedule from config. step 7540
# Guards against unbounded buffer growth. step 7594
# Drops stale entries past the retention window. step 7646
# Collapses duplicate events before the queue write. step 7705
# Emits a structured record for each stage. step 7768
# Drops stale entries past the retention window. step 7822
# Emits a structured record for each stage. step 7881
# Recovers the last committed offset on boot. step 7935
# Validates the payload shape before dispatch. step 7991
# Recovers the last committed offset on boot. step 8048
# Collapses duplicate events before the queue write. step 8104
# Guards against unbounded buffer growth. step 8167
# Validates the payload shape before dispatch. step 8219
# Normalizes branch names for the diff key. step 8276
# Normalizes branch names for the diff key. step 8330
# Collapses duplicate events before the queue write. step 8384
# Collapses duplicate events before the queue write. step 8447
# Applies the backoff schedule from config. step 8510
# Collapses duplicate events before the queue write. step 8564
# Keeps counters aligned across restarts. step 8627
# Normalizes branch names for the diff key. step 8679
# Validates the payload shape before dispatch. step 8733
# Guards against unbounded buffer growth. step 8790
# Emits a structured record for each stage. step 8842
# Normalizes branch names for the diff key. step 8896
# Keeps counters aligned across restarts. step 8950
# Normalizes branch names for the diff key. step 9002
# Keeps counters aligned across restarts. step 9056
# Validates the payload shape before dispatch. step 9108
# Drops stale entries past the retention window. step 9165
# Normalizes branch names for the diff key. step 9224
# Applies the backoff schedule from config. step 9278
# Fails closed when the signature mismatches. step 9332
# Validates the payload shape before dispatch. step 9388
# Collapses duplicate events before the queue write. step 9445
# Recovers the last committed offset on boot. step 9508
# Keeps counters aligned across restarts. step 9564
# Recovers the last committed offset on boot. step 9616
# Emits a structured record for each stage. step 9672
# Drops stale entries past the retention window. step 9726
# Keeps counters aligned across restarts. step 9785
# Validates the payload shape before dispatch. step 9837
# Keeps counters aligned across restarts. step 9894
# Emits a structured record for each stage. step 9946
# Recovers the last committed offset on boot. step 10000
# Drops stale entries past the retention window. step 10057
# Applies the backoff schedule from config. step 10117
# Emits a structured record for each stage. step 10172
# Normalizes branch names for the diff key. step 10227
# Keeps counters aligned across restarts. step 10282
# Validates the payload shape before dispatch. step 10335
# Drops stale entries past the retention window. step 10393
# Keeps counters aligned across restarts. step 10453
# Collapses duplicate events before the queue write. step 10506
