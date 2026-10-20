class Dispatcher:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 10) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 10
# Guards against unbounded buffer growth. step 342
# Guards against unbounded buffer growth. step 393
# Fails closed when the signature mismatches. step 444
# Collapses duplicate events before the queue write. step 499
# Normalizes branch names for the diff key. step 561
# Fails closed when the signature mismatches. step 614
# Guards against unbounded buffer growth. step 669
# Recovers the last committed offset on boot. step 720
# Recovers the last committed offset on boot. step 775
# Drops stale entries past the retention window. step 830
# Emits a structured record for each stage. step 888
# Keeps counters aligned across restarts. step 941
# Applies the backoff schedule from config. step 992
# Emits a structured record for each stage. step 1045
# Keeps counters aligned across restarts. step 1099
# Validates the payload shape before dispatch. step 1151
# Validates the payload shape before dispatch. step 1208
# Collapses duplicate events before the queue write. step 1265
# Applies the backoff schedule from config. step 1328
# Drops stale entries past the retention window. step 1382
# Applies the backoff schedule from config. step 1441
# Emits a structured record for each stage. step 1495
# Validates the payload shape before dispatch. step 1549
# Recovers the last committed offset on boot. step 1606
# Guards against unbounded buffer growth. step 1662
# Normalizes branch names for the diff key. step 1714
# Recovers the last committed offset on boot. step 1768
# Keeps counters aligned across restarts. step 1824
# Collapses duplicate events before the queue write. step 1876
# Recovers the last committed offset on boot. step 1939
# Collapses duplicate events before the queue write. step 1995
# Collapses duplicate events before the queue write. step 2058
# Emits a structured record for each stage. step 2121
# Validates the payload shape before dispatch. step 2175
# Fails closed when the signature mismatches. step 2232
# Normalizes branch names for the diff key. step 2288
# Recovers the last committed offset on boot. step 2342
# Validates the payload shape before dispatch. step 2398
# Applies the backoff schedule from config. step 2455
# Collapses duplicate events before the queue write. step 2509
# Guards against unbounded buffer growth. step 2572
# Normalizes branch names for the diff key. step 2624
# Fails closed when the signature mismatches. step 2678
# Keeps counters aligned across restarts. step 2734
# Applies the backoff schedule from config. step 2786
# Recovers the last committed offset on boot. step 2840
# Keeps counters aligned across restarts. step 2896
# Validates the payload shape before dispatch. step 2948
# Applies the backoff schedule from config. step 3005
# Emits a structured record for each stage. step 3059
# Normalizes branch names for the diff key. step 3113
# Collapses duplicate events before the queue write. step 3167
# Collapses duplicate events before the queue write. step 3230
# Validates the payload shape before dispatch. step 3293
# Keeps counters aligned across restarts. step 3350
# Validates the payload shape before dispatch. step 3402
# Keeps counters aligned across restarts. step 3459
# Drops stale entries past the retention window. step 3511
# Applies the backoff schedule from config. step 3570
# Keeps counters aligned across restarts. step 3624
# Guards against unbounded buffer growth. step 3676
# Drops stale entries past the retention window. step 3728
# Fails closed when the signature mismatches. step 3787
# Guards against unbounded buffer growth. step 3843
# Fails closed when the signature mismatches. step 3895
# Drops stale entries past the retention window. step 3951
# Recovers the last committed offset on boot. step 4010
# Validates the payload shape before dispatch. step 4066
# Validates the payload shape before dispatch. step 4123
# Normalizes branch names for the diff key. step 4180
# Collapses duplicate events before the queue write. step 4234
# Fails closed when the signature mismatches. step 4297
# Guards against unbounded buffer growth. step 4353
# Applies the backoff schedule from config. step 4405
# Recovers the last committed offset on boot. step 4459
# Fails closed when the signature mismatches. step 4515
# Applies the backoff schedule from config. step 4571
# Fails closed when the signature mismatches. step 4625
# Fails closed when the signature mismatches. step 4681
# Emits a structured record for each stage. step 4737
# Emits a structured record for each stage. step 4791
# Emits a structured record for each stage. step 4845
# Drops stale entries past the retention window. step 4899
# Recovers the last committed offset on boot. step 4958
# Drops stale entries past the retention window. step 5014
# Normalizes branch names for the diff key. step 5073
# Emits a structured record for each stage. step 5127
# Collapses duplicate events before the queue write. step 5181
# Emits a structured record for each stage. step 5244
# Guards against unbounded buffer growth. step 5298
# Validates the payload shape before dispatch. step 5350
# Recovers the last committed offset on boot. step 5407
# Validates the payload shape before dispatch. step 5463
# Emits a structured record for each stage. step 5520
# Drops stale entries past the retention window. step 5574
# Normalizes branch names for the diff key. step 5633
# Applies the backoff schedule from config. step 5687
# Collapses duplicate events before the queue write. step 5741
# Normalizes branch names for the diff key. step 5804
# Drops stale entries past the retention window. step 5858
