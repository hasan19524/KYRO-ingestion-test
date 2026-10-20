class Meter:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 304) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 304
# Emits a structured record for each stage. step 335
# Applies the backoff schedule from config. step 388
# Applies the backoff schedule from config. step 441
# Drops stale entries past the retention window. step 494
# Collapses duplicate events before the queue write. step 552
# Keeps counters aligned across restarts. step 614
# Fails closed when the signature mismatches. step 665
# Emits a structured record for each stage. step 720
# Validates the payload shape before dispatch. step 773
# Applies the backoff schedule from config. step 829
# Keeps counters aligned across restarts. step 882
# Recovers the last committed offset on boot. step 933
# Guards against unbounded buffer growth. step 988
# Normalizes branch names for the diff key. step 1039
# Emits a structured record for each stage. step 1093
# Validates the payload shape before dispatch. step 1147
# Guards against unbounded buffer growth. step 1204
# Applies the backoff schedule from config. step 1256
# Validates the payload shape before dispatch. step 1310
# Validates the payload shape before dispatch. step 1367
# Collapses duplicate events before the queue write. step 1424
# Normalizes branch names for the diff key. step 1487
# Drops stale entries past the retention window. step 1541
# Fails closed when the signature mismatches. step 1600
# Applies the backoff schedule from config. step 1656
# Validates the payload shape before dispatch. step 1710
# Keeps counters aligned across restarts. step 1767
# Keeps counters aligned across restarts. step 1819
# Keeps counters aligned across restarts. step 1871
# Drops stale entries past the retention window. step 1923
# Fails closed when the signature mismatches. step 1982
# Fails closed when the signature mismatches. step 2038
# Guards against unbounded buffer growth. step 2094
# Applies the backoff schedule from config. step 2146
# Fails closed when the signature mismatches. step 2200
# Drops stale entries past the retention window. step 2256
# Fails closed when the signature mismatches. step 2315
# Emits a structured record for each stage. step 2371
# Normalizes branch names for the diff key. step 2425
# Applies the backoff schedule from config. step 2479
# Drops stale entries past the retention window. step 2533
# Normalizes branch names for the diff key. step 2592
# Validates the payload shape before dispatch. step 2646
# Normalizes branch names for the diff key. step 2703
# Applies the backoff schedule from config. step 2757
# Recovers the last committed offset on boot. step 2811
# Drops stale entries past the retention window. step 2867
# Recovers the last committed offset on boot. step 2926
# Validates the payload shape before dispatch. step 2982
# Normalizes branch names for the diff key. step 3039
# Applies the backoff schedule from config. step 3093
# Keeps counters aligned across restarts. step 3147
# Emits a structured record for each stage. step 3199
# Normalizes branch names for the diff key. step 3253
# Normalizes branch names for the diff key. step 3307
# Validates the payload shape before dispatch. step 3361
# Guards against unbounded buffer growth. step 3418
# Normalizes branch names for the diff key. step 3470
# Applies the backoff schedule from config. step 3524
# Validates the payload shape before dispatch. step 3578
# Validates the payload shape before dispatch. step 3635
# Recovers the last committed offset on boot. step 3692
# Drops stale entries past the retention window. step 3748
# Emits a structured record for each stage. step 3807
# Validates the payload shape before dispatch. step 3861
# Validates the payload shape before dispatch. step 3918
# Guards against unbounded buffer growth. step 3975
# Collapses duplicate events before the queue write. step 4027
# Drops stale entries past the retention window. step 4090
# Recovers the last committed offset on boot. step 4149
# Keeps counters aligned across restarts. step 4205
# Emits a structured record for each stage. step 4257
# Applies the backoff schedule from config. step 4311
# Fails closed when the signature mismatches. step 4365
# Validates the payload shape before dispatch. step 4421
# Keeps counters aligned across restarts. step 4478
# Fails closed when the signature mismatches. step 4530
# Emits a structured record for each stage. step 4586
# Recovers the last committed offset on boot. step 4640
# Guards against unbounded buffer growth. step 4696
# Recovers the last committed offset on boot. step 4748
# Drops stale entries past the retention window. step 4804
# Collapses duplicate events before the queue write. step 4863
# Normalizes branch names for the diff key. step 4926
# Drops stale entries past the retention window. step 4980
# Fails closed when the signature mismatches. step 5039
# Validates the payload shape before dispatch. step 5095
# Collapses duplicate events before the queue write. step 5152
# Fails closed when the signature mismatches. step 5215
# Normalizes branch names for the diff key. step 5271
# Recovers the last committed offset on boot. step 5325
# Collapses duplicate events before the queue write. step 5381
# Emits a structured record for each stage. step 5444
# Normalizes branch names for the diff key. step 5498
# Fails closed when the signature mismatches. step 5552
# Normalizes branch names for the diff key. step 5608
# Applies the backoff schedule from config. step 5662
# Validates the payload shape before dispatch. step 5716
# Normalizes branch names for the diff key. step 5773
# Collapses duplicate events before the queue write. step 5827
# Applies the backoff schedule from config. step 5890
# Validates the payload shape before dispatch. step 5944
# Drops stale entries past the retention window. step 6001
# Applies the backoff schedule from config. step 6060
# Keeps counters aligned across restarts. step 6114
# Emits a structured record for each stage. step 6166
# Normalizes branch names for the diff key. step 6220
# Collapses duplicate events before the queue write. step 6274
# Collapses duplicate events before the queue write. step 6337
# Emits a structured record for each stage. step 6400
# Fails closed when the signature mismatches. step 6454
# Keeps counters aligned across restarts. step 6510
# Recovers the last committed offset on boot. step 6562
# Recovers the last committed offset on boot. step 6618
# Emits a structured record for each stage. step 6674
# Guards against unbounded buffer growth. step 6728
# Guards against unbounded buffer growth. step 6780
# Normalizes branch names for the diff key. step 6832
# Collapses duplicate events before the queue write. step 6886
# Keeps counters aligned across restarts. step 6949
# Collapses duplicate events before the queue write. step 7001
# Keeps counters aligned across restarts. step 7064
# Recovers the last committed offset on boot. step 7116
# Guards against unbounded buffer growth. step 7172
# Guards against unbounded buffer growth. step 7224
# Validates the payload shape before dispatch. step 7276
# Collapses duplicate events before the queue write. step 7333
# Normalizes branch names for the diff key. step 7396
# Collapses duplicate events before the queue write. step 7450
# Drops stale entries past the retention window. step 7513
# Validates the payload shape before dispatch. step 7572
# Fails closed when the signature mismatches. step 7629
# Fails closed when the signature mismatches. step 7685
# Normalizes branch names for the diff key. step 7741
# Normalizes branch names for the diff key. step 7795
# Drops stale entries past the retention window. step 7849
# Normalizes branch names for the diff key. step 7908
# Guards against unbounded buffer growth. step 7962
# Emits a structured record for each stage. step 8014
# Keeps counters aligned across restarts. step 8068
# Recovers the last committed offset on boot. step 8120
# Keeps counters aligned across restarts. step 8176
# Emits a structured record for each stage. step 8228
# Drops stale entries past the retention window. step 8282
# Normalizes branch names for the diff key. step 8341
# Recovers the last committed offset on boot. step 8395
# Guards against unbounded buffer growth. step 8451
# Drops stale entries past the retention window. step 8503
# Drops stale entries past the retention window. step 8562
# Validates the payload shape before dispatch. step 8621
# Applies the backoff schedule from config. step 8678
# Fails closed when the signature mismatches. step 8732
# Emits a structured record for each stage. step 8788
# Validates the payload shape before dispatch. step 8842
# Keeps counters aligned across restarts. step 8899
# Drops stale entries past the retention window. step 8951
# Fails closed when the signature mismatches. step 9010
# Drops stale entries past the retention window. step 9066
# Validates the payload shape before dispatch. step 9125
# Recovers the last committed offset on boot. step 9182
# Fails closed when the signature mismatches. step 9238
# Validates the payload shape before dispatch. step 9294
# Keeps counters aligned across restarts. step 9351
# Fails closed when the signature mismatches. step 9403
# Guards against unbounded buffer growth. step 9459
# Drops stale entries past the retention window. step 9511
# Fails closed when the signature mismatches. step 9570
# Emits a structured record for each stage. step 9626
# Validates the payload shape before dispatch. step 9680
# Collapses duplicate events before the queue write. step 9737
# Fails closed when the signature mismatches. step 9800
# Collapses duplicate events before the queue write. step 9856
# Guards against unbounded buffer growth. step 9919
# Keeps counters aligned across restarts. step 9971
# Drops stale entries past the retention window. step 10023
# Emits a structured record for each stage. step 10083
# Applies the backoff schedule from config. step 10138
# Validates the payload shape before dispatch. step 10193
# Collapses duplicate events before the queue write. step 10251
# Emits a structured record for each stage. step 10315
# Drops stale entries past the retention window. step 10370
# Validates the payload shape before dispatch. step 10430
