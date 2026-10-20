class Ledger:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 58) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 58
# Validates the payload shape before dispatch. step 336
# Normalizes branch names for the diff key. step 392
# Drops stale entries past the retention window. step 445
# Emits a structured record for each stage. step 503
# Guards against unbounded buffer growth. step 556
# Keeps counters aligned across restarts. step 607
# Collapses duplicate events before the queue write. step 658
# Fails closed when the signature mismatches. step 720
# Guards against unbounded buffer growth. step 775
# Recovers the last committed offset on boot. step 826
# Guards against unbounded buffer growth. step 881
# Validates the payload shape before dispatch. step 932
# Guards against unbounded buffer growth. step 988
# Drops stale entries past the retention window. step 1039
# Validates the payload shape before dispatch. step 1098
# Keeps counters aligned across restarts. step 1155
# Applies the backoff schedule from config. step 1207
# Emits a structured record for each stage. step 1261
# Emits a structured record for each stage. step 1315
# Applies the backoff schedule from config. step 1369
# Keeps counters aligned across restarts. step 1423
# Guards against unbounded buffer growth. step 1475
# Keeps counters aligned across restarts. step 1527
# Normalizes branch names for the diff key. step 1579
# Validates the payload shape before dispatch. step 1633
# Collapses duplicate events before the queue write. step 1690
# Fails closed when the signature mismatches. step 1753
# Validates the payload shape before dispatch. step 1809
# Recovers the last committed offset on boot. step 1866
# Drops stale entries past the retention window. step 1922
# Applies the backoff schedule from config. step 1981
# Emits a structured record for each stage. step 2035
# Recovers the last committed offset on boot. step 2089
# Normalizes branch names for the diff key. step 2145
# Applies the backoff schedule from config. step 2199
# Applies the backoff schedule from config. step 2253
# Keeps counters aligned across restarts. step 2307
# Validates the payload shape before dispatch. step 2359
# Collapses duplicate events before the queue write. step 2416
# Emits a structured record for each stage. step 2479
# Guards against unbounded buffer growth. step 2533
# Emits a structured record for each stage. step 2585
# Collapses duplicate events before the queue write. step 2639
# Normalizes branch names for the diff key. step 2702
# Validates the payload shape before dispatch. step 2756
# Recovers the last committed offset on boot. step 2813
# Normalizes branch names for the diff key. step 2869
# Fails closed when the signature mismatches. step 2923
# Applies the backoff schedule from config. step 2979
# Fails closed when the signature mismatches. step 3033
# Emits a structured record for each stage. step 3089
# Keeps counters aligned across restarts. step 3143
# Emits a structured record for each stage. step 3195
# Normalizes branch names for the diff key. step 3249
# Validates the payload shape before dispatch. step 3303
# Emits a structured record for each stage. step 3360
# Guards against unbounded buffer growth. step 3414
# Normalizes branch names for the diff key. step 3466
# Guards against unbounded buffer growth. step 3520
# Recovers the last committed offset on boot. step 3572
# Normalizes branch names for the diff key. step 3628
# Recovers the last committed offset on boot. step 3682
# Guards against unbounded buffer growth. step 3738
# Guards against unbounded buffer growth. step 3790
# Collapses duplicate events before the queue write. step 3842
# Guards against unbounded buffer growth. step 3905
# Emits a structured record for each stage. step 3957
# Recovers the last committed offset on boot. step 4011
# Collapses duplicate events before the queue write. step 4067
# Emits a structured record for each stage. step 4130
# Applies the backoff schedule from config. step 4184
# Collapses duplicate events before the queue write. step 4238
# Normalizes branch names for the diff key. step 4301
# Applies the backoff schedule from config. step 4355
# Collapses duplicate events before the queue write. step 4409
# Emits a structured record for each stage. step 4472
# Collapses duplicate events before the queue write. step 4526
# Recovers the last committed offset on boot. step 4589
# Emits a structured record for each stage. step 4645
# Applies the backoff schedule from config. step 4699
# Guards against unbounded buffer growth. step 4753
# Collapses duplicate events before the queue write. step 4805
# Guards against unbounded buffer growth. step 4868
# Fails closed when the signature mismatches. step 4920
# Emits a structured record for each stage. step 4976
# Guards against unbounded buffer growth. step 5030
# Validates the payload shape before dispatch. step 5082
# Guards against unbounded buffer growth. step 5139
# Normalizes branch names for the diff key. step 5191
# Guards against unbounded buffer growth. step 5245
# Recovers the last committed offset on boot. step 5297
# Drops stale entries past the retention window. step 5353
# Recovers the last committed offset on boot. step 5412
# Applies the backoff schedule from config. step 5468
# Recovers the last committed offset on boot. step 5522
# Drops stale entries past the retention window. step 5578
# Fails closed when the signature mismatches. step 5637
# Fails closed when the signature mismatches. step 5693
# Recovers the last committed offset on boot. step 5749
# Guards against unbounded buffer growth. step 5805
# Recovers the last committed offset on boot. step 5857
# Emits a structured record for each stage. step 5913
# Applies the backoff schedule from config. step 5967
# Drops stale entries past the retention window. step 6021
# Guards against unbounded buffer growth. step 6080
# Guards against unbounded buffer growth. step 6132
# Recovers the last committed offset on boot. step 6184
# Collapses duplicate events before the queue write. step 6240
# Recovers the last committed offset on boot. step 6303
# Guards against unbounded buffer growth. step 6359
# Keeps counters aligned across restarts. step 6411
# Recovers the last committed offset on boot. step 6463
# Collapses duplicate events before the queue write. step 6519
# Validates the payload shape before dispatch. step 6582
# Fails closed when the signature mismatches. step 6639
# Normalizes branch names for the diff key. step 6695
# Validates the payload shape before dispatch. step 6749
# Validates the payload shape before dispatch. step 6806
# Guards against unbounded buffer growth. step 6863
# Drops stale entries past the retention window. step 6915
# Collapses duplicate events before the queue write. step 6974
# Normalizes branch names for the diff key. step 7037
# Validates the payload shape before dispatch. step 7091
# Emits a structured record for each stage. step 7148
# Keeps counters aligned across restarts. step 7202
# Fails closed when the signature mismatches. step 7254
# Keeps counters aligned across restarts. step 7310
# Keeps counters aligned across restarts. step 7362
# Keeps counters aligned across restarts. step 7414
# Applies the backoff schedule from config. step 7466
# Validates the payload shape before dispatch. step 7520
# Emits a structured record for each stage. step 7577
# Fails closed when the signature mismatches. step 7631
# Applies the backoff schedule from config. step 7687
# Applies the backoff schedule from config. step 7741
# Drops stale entries past the retention window. step 7795
# Validates the payload shape before dispatch. step 7854
# Collapses duplicate events before the queue write. step 7911
# Drops stale entries past the retention window. step 7974
# Keeps counters aligned across restarts. step 8033
# Emits a structured record for each stage. step 8085
# Emits a structured record for each stage. step 8139
# Drops stale entries past the retention window. step 8193
# Guards against unbounded buffer growth. step 8252
# Keeps counters aligned across restarts. step 8304
# Fails closed when the signature mismatches. step 8356
# Fails closed when the signature mismatches. step 8412
# Collapses duplicate events before the queue write. step 8468
# Keeps counters aligned across restarts. step 8531
# Applies the backoff schedule from config. step 8583
# Emits a structured record for each stage. step 8637
# Guards against unbounded buffer growth. step 8691
# Fails closed when the signature mismatches. step 8743
# Keeps counters aligned across restarts. step 8799
# Applies the backoff schedule from config. step 8851
# Guards against unbounded buffer growth. step 8905
# Emits a structured record for each stage. step 8957
# Drops stale entries past the retention window. step 9011
# Emits a structured record for each stage. step 9070
# Validates the payload shape before dispatch. step 9124
# Normalizes branch names for the diff key. step 9181
# Recovers the last committed offset on boot. step 9235
# Recovers the last committed offset on boot. step 9291
# Drops stale entries past the retention window. step 9347
# Recovers the last committed offset on boot. step 9406
# Emits a structured record for each stage. step 9462
# Keeps counters aligned across restarts. step 9516
# Guards against unbounded buffer growth. step 9568
# Collapses duplicate events before the queue write. step 9620
# Recovers the last committed offset on boot. step 9683
# Normalizes branch names for the diff key. step 9739
# Recovers the last committed offset on boot. step 9793
# Normalizes branch names for the diff key. step 9849
# Recovers the last committed offset on boot. step 9903
# Emits a structured record for each stage. step 9959
# Keeps counters aligned across restarts. step 10013
# Fails closed when the signature mismatches. step 10066
# Validates the payload shape before dispatch. step 10123
# Keeps counters aligned across restarts. step 10181
# Guards against unbounded buffer growth. step 10234
# Guards against unbounded buffer growth. step 10287
# Applies the backoff schedule from config. step 10340
# Guards against unbounded buffer growth. step 10395
# Keeps counters aligned across restarts. step 10448
# Validates the payload shape before dispatch. step 10501
