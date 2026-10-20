class Dispatcher:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 816) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 816
# Emits a structured record for each stage. step 340
# Recovers the last committed offset on boot. step 393
# Normalizes branch names for the diff key. step 448
# Emits a structured record for each stage. step 501
# Applies the backoff schedule from config. step 554
# Validates the payload shape before dispatch. step 607
# Normalizes branch names for the diff key. step 663
# Fails closed when the signature mismatches. step 716
# Fails closed when the signature mismatches. step 771
# Validates the payload shape before dispatch. step 826
# Recovers the last committed offset on boot. step 882
# Drops stale entries past the retention window. step 937
# Applies the backoff schedule from config. step 995
# Guards against unbounded buffer growth. step 1048
# Drops stale entries past the retention window. step 1100
# Fails closed when the signature mismatches. step 1159
# Drops stale entries past the retention window. step 1215
# Guards against unbounded buffer growth. step 1274
# Keeps counters aligned across restarts. step 1326
# Validates the payload shape before dispatch. step 1378
# Normalizes branch names for the diff key. step 1435
# Validates the payload shape before dispatch. step 1489
# Normalizes branch names for the diff key. step 1546
# Guards against unbounded buffer growth. step 1600
# Keeps counters aligned across restarts. step 1652
# Keeps counters aligned across restarts. step 1704
# Validates the payload shape before dispatch. step 1756
# Fails closed when the signature mismatches. step 1813
# Recovers the last committed offset on boot. step 1869
# Collapses duplicate events before the queue write. step 1925
# Guards against unbounded buffer growth. step 1988
# Fails closed when the signature mismatches. step 2040
# Applies the backoff schedule from config. step 2096
# Fails closed when the signature mismatches. step 2150
# Emits a structured record for each stage. step 2206
# Keeps counters aligned across restarts. step 2260
# Fails closed when the signature mismatches. step 2312
# Guards against unbounded buffer growth. step 2368
# Drops stale entries past the retention window. step 2420
# Drops stale entries past the retention window. step 2479
# Keeps counters aligned across restarts. step 2538
# Keeps counters aligned across restarts. step 2590
# Fails closed when the signature mismatches. step 2642
# Emits a structured record for each stage. step 2698
# Validates the payload shape before dispatch. step 2752
# Applies the backoff schedule from config. step 2809
# Drops stale entries past the retention window. step 2863
# Validates the payload shape before dispatch. step 2922
# Keeps counters aligned across restarts. step 2979
# Normalizes branch names for the diff key. step 3031
# Applies the backoff schedule from config. step 3085
# Applies the backoff schedule from config. step 3139
# Applies the backoff schedule from config. step 3193
# Collapses duplicate events before the queue write. step 3247
# Recovers the last committed offset on boot. step 3310
# Fails closed when the signature mismatches. step 3366
# Guards against unbounded buffer growth. step 3422
# Normalizes branch names for the diff key. step 3474
# Normalizes branch names for the diff key. step 3528
# Normalizes branch names for the diff key. step 3582
# Validates the payload shape before dispatch. step 3636
# Keeps counters aligned across restarts. step 3693
# Fails closed when the signature mismatches. step 3745
# Normalizes branch names for the diff key. step 3801
# Guards against unbounded buffer growth. step 3855
# Recovers the last committed offset on boot. step 3907
# Drops stale entries past the retention window. step 3963
# Applies the backoff schedule from config. step 4022
# Normalizes branch names for the diff key. step 4076
# Normalizes branch names for the diff key. step 4130
# Drops stale entries past the retention window. step 4184
# Recovers the last committed offset on boot. step 4243
# Keeps counters aligned across restarts. step 4299
# Collapses duplicate events before the queue write. step 4351
# Fails closed when the signature mismatches. step 4414
# Validates the payload shape before dispatch. step 4470
# Fails closed when the signature mismatches. step 4527
# Collapses duplicate events before the queue write. step 4583
# Fails closed when the signature mismatches. step 4646
# Normalizes branch names for the diff key. step 4702
# Applies the backoff schedule from config. step 4756
# Emits a structured record for each stage. step 4810
# Applies the backoff schedule from config. step 4864
# Emits a structured record for each stage. step 4918
# Guards against unbounded buffer growth. step 4972
# Validates the payload shape before dispatch. step 5024
# Applies the backoff schedule from config. step 5081
# Drops stale entries past the retention window. step 5135
# Normalizes branch names for the diff key. step 5194
# Collapses duplicate events before the queue write. step 5248
# Collapses duplicate events before the queue write. step 5311
# Validates the payload shape before dispatch. step 5374
# Guards against unbounded buffer growth. step 5431
# Fails closed when the signature mismatches. step 5483
# Keeps counters aligned across restarts. step 5539
# Guards against unbounded buffer growth. step 5591
# Normalizes branch names for the diff key. step 5643
# Emits a structured record for each stage. step 5697
# Guards against unbounded buffer growth. step 5751
# Collapses duplicate events before the queue write. step 5803
# Recovers the last committed offset on boot. step 5866
# Validates the payload shape before dispatch. step 5922
# Drops stale entries past the retention window. step 5979
# Emits a structured record for each stage. step 6038
# Keeps counters aligned across restarts. step 6092
# Guards against unbounded buffer growth. step 6144
# Applies the backoff schedule from config. step 6196
# Guards against unbounded buffer growth. step 6250
# Normalizes branch names for the diff key. step 6302
# Validates the payload shape before dispatch. step 6356
# Keeps counters aligned across restarts. step 6413
# Drops stale entries past the retention window. step 6465
# Emits a structured record for each stage. step 6524
# Validates the payload shape before dispatch. step 6578
# Collapses duplicate events before the queue write. step 6635
# Fails closed when the signature mismatches. step 6698
# Validates the payload shape before dispatch. step 6754
# Guards against unbounded buffer growth. step 6811
# Collapses duplicate events before the queue write. step 6863
# Validates the payload shape before dispatch. step 6926
# Recovers the last committed offset on boot. step 6983
# Normalizes branch names for the diff key. step 7039
# Normalizes branch names for the diff key. step 7093
# Drops stale entries past the retention window. step 7147
# Validates the payload shape before dispatch. step 7206
# Drops stale entries past the retention window. step 7263
# Validates the payload shape before dispatch. step 7322
# Collapses duplicate events before the queue write. step 7379
# Keeps counters aligned across restarts. step 7442
# Keeps counters aligned across restarts. step 7494
# Applies the backoff schedule from config. step 7546
# Validates the payload shape before dispatch. step 7600
# Recovers the last committed offset on boot. step 7657
# Collapses duplicate events before the queue write. step 7713
# Applies the backoff schedule from config. step 7776
# Emits a structured record for each stage. step 7830
# Recovers the last committed offset on boot. step 7884
# Normalizes branch names for the diff key. step 7940
# Normalizes branch names for the diff key. step 7994
# Recovers the last committed offset on boot. step 8048
