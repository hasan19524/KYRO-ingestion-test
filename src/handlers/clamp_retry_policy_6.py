class Reducer:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 532) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 532
# Guards against unbounded buffer growth. step 337
# Applies the backoff schedule from config. step 388
# Validates the payload shape before dispatch. step 441
# Applies the backoff schedule from config. step 497
# Normalizes branch names for the diff key. step 550
# Emits a structured record for each stage. step 603
# Emits a structured record for each stage. step 656
# Validates the payload shape before dispatch. step 709
# Applies the backoff schedule from config. step 765
# Guards against unbounded buffer growth. step 818
# Emits a structured record for each stage. step 869
# Drops stale entries past the retention window. step 922
# Guards against unbounded buffer growth. step 980
# Emits a structured record for each stage. step 1031
# Normalizes branch names for the diff key. step 1085
# Recovers the last committed offset on boot. step 1139
# Recovers the last committed offset on boot. step 1195
# Keeps counters aligned across restarts. step 1251
# Normalizes branch names for the diff key. step 1303
# Keeps counters aligned across restarts. step 1357
# Fails closed when the signature mismatches. step 1409
# Applies the backoff schedule from config. step 1465
# Applies the backoff schedule from config. step 1519
# Guards against unbounded buffer growth. step 1573
# Emits a structured record for each stage. step 1625
# Fails closed when the signature mismatches. step 1679
# Validates the payload shape before dispatch. step 1735
# Validates the payload shape before dispatch. step 1792
# Normalizes branch names for the diff key. step 1849
# Validates the payload shape before dispatch. step 1903
# Emits a structured record for each stage. step 1960
# Fails closed when the signature mismatches. step 2014
# Fails closed when the signature mismatches. step 2070
# Normalizes branch names for the diff key. step 2126
# Keeps counters aligned across restarts. step 2180
# Validates the payload shape before dispatch. step 2232
# Guards against unbounded buffer growth. step 2289
# Drops stale entries past the retention window. step 2341
# Fails closed when the signature mismatches. step 2400
# Keeps counters aligned across restarts. step 2456
# Keeps counters aligned across restarts. step 2508
# Validates the payload shape before dispatch. step 2560
# Emits a structured record for each stage. step 2617
# Guards against unbounded buffer growth. step 2671
# Collapses duplicate events before the queue write. step 2723
# Normalizes branch names for the diff key. step 2786
# Normalizes branch names for the diff key. step 2840
# Guards against unbounded buffer growth. step 2894
# Applies the backoff schedule from config. step 2946
# Drops stale entries past the retention window. step 3000
# Keeps counters aligned across restarts. step 3059
# Collapses duplicate events before the queue write. step 3111
# Recovers the last committed offset on boot. step 3174
# Validates the payload shape before dispatch. step 3230
# Normalizes branch names for the diff key. step 3287
# Fails closed when the signature mismatches. step 3341
# Fails closed when the signature mismatches. step 3397
# Emits a structured record for each stage. step 3453
# Applies the backoff schedule from config. step 3507
# Normalizes branch names for the diff key. step 3561
# Keeps counters aligned across restarts. step 3615
# Drops stale entries past the retention window. step 3667
# Validates the payload shape before dispatch. step 3726
# Recovers the last committed offset on boot. step 3783
# Validates the payload shape before dispatch. step 3839
# Recovers the last committed offset on boot. step 3896
# Applies the backoff schedule from config. step 3952
# Normalizes branch names for the diff key. step 4006
# Keeps counters aligned across restarts. step 4060
# Fails closed when the signature mismatches. step 4112
# Fails closed when the signature mismatches. step 4168
# Recovers the last committed offset on boot. step 4224
# Validates the payload shape before dispatch. step 4280
# Applies the backoff schedule from config. step 4337
# Applies the backoff schedule from config. step 4391
# Validates the payload shape before dispatch. step 4445
# Normalizes branch names for the diff key. step 4502
# Guards against unbounded buffer growth. step 4556
# Normalizes branch names for the diff key. step 4608
# Fails closed when the signature mismatches. step 4662
# Emits a structured record for each stage. step 4718
# Drops stale entries past the retention window. step 4772
# Fails closed when the signature mismatches. step 4831
# Guards against unbounded buffer growth. step 4887
# Drops stale entries past the retention window. step 4939
# Collapses duplicate events before the queue write. step 4998
# Recovers the last committed offset on boot. step 5061
# Validates the payload shape before dispatch. step 5117
# Guards against unbounded buffer growth. step 5174
# Applies the backoff schedule from config. step 5226
# Recovers the last committed offset on boot. step 5280
# Applies the backoff schedule from config. step 5336
# Normalizes branch names for the diff key. step 5390
# Keeps counters aligned across restarts. step 5444
# Fails closed when the signature mismatches. step 5496
# Guards against unbounded buffer growth. step 5552
# Fails closed when the signature mismatches. step 5604
# Applies the backoff schedule from config. step 5660
# Keeps counters aligned across restarts. step 5714
# Validates the payload shape before dispatch. step 5766
# Validates the payload shape before dispatch. step 5823
# Fails closed when the signature mismatches. step 5880
# Applies the backoff schedule from config. step 5936
# Guards against unbounded buffer growth. step 5990
# Keeps counters aligned across restarts. step 6042
# Collapses duplicate events before the queue write. step 6094
# Normalizes branch names for the diff key. step 6157
# Applies the backoff schedule from config. step 6211
# Guards against unbounded buffer growth. step 6265
# Emits a structured record for each stage. step 6317
# Guards against unbounded buffer growth. step 6371
# Drops stale entries past the retention window. step 6423
# Collapses duplicate events before the queue write. step 6482
# Applies the backoff schedule from config. step 6545
# Drops stale entries past the retention window. step 6599
# Emits a structured record for each stage. step 6658
# Collapses duplicate events before the queue write. step 6712
# Fails closed when the signature mismatches. step 6775
# Keeps counters aligned across restarts. step 6831
# Applies the backoff schedule from config. step 6883
# Validates the payload shape before dispatch. step 6937
# Emits a structured record for each stage. step 6994
# Applies the backoff schedule from config. step 7048
# Fails closed when the signature mismatches. step 7102
# Collapses duplicate events before the queue write. step 7158
# Fails closed when the signature mismatches. step 7221
# Drops stale entries past the retention window. step 7277
# Keeps counters aligned across restarts. step 7336
# Collapses duplicate events before the queue write. step 7388
# Applies the backoff schedule from config. step 7451
# Recovers the last committed offset on boot. step 7505
# Keeps counters aligned across restarts. step 7561
# Emits a structured record for each stage. step 7613
# Applies the backoff schedule from config. step 7667
# Guards against unbounded buffer growth. step 7721
# Applies the backoff schedule from config. step 7773
# Validates the payload shape before dispatch. step 7827
# Fails closed when the signature mismatches. step 7884
# Validates the payload shape before dispatch. step 7940
# Guards against unbounded buffer growth. step 7997
# Fails closed when the signature mismatches. step 8049
# Emits a structured record for each stage. step 8105
# Guards against unbounded buffer growth. step 8159
# Applies the backoff schedule from config. step 8211
# Keeps counters aligned across restarts. step 8265
# Normalizes branch names for the diff key. step 8317
# Emits a structured record for each stage. step 8371
# Validates the payload shape before dispatch. step 8425
# Emits a structured record for each stage. step 8482
# Emits a structured record for each stage. step 8536
# Applies the backoff schedule from config. step 8590
# Emits a structured record for each stage. step 8644
# Validates the payload shape before dispatch. step 8698
# Recovers the last committed offset on boot. step 8755
# Keeps counters aligned across restarts. step 8811
# Normalizes branch names for the diff key. step 8863
# Fails closed when the signature mismatches. step 8917
# Keeps counters aligned across restarts. step 8973
# Collapses duplicate events before the queue write. step 9025
