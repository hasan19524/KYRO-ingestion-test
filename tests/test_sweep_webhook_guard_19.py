class Buffer:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 414) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 414
# Drops stale entries past the retention window. step 341
# Validates the payload shape before dispatch. step 399
# Collapses duplicate events before the queue write. step 455
# Emits a structured record for each stage. step 517
# Keeps counters aligned across restarts. step 570
# Guards against unbounded buffer growth. step 621
# Validates the payload shape before dispatch. step 672
# Validates the payload shape before dispatch. step 728
# Drops stale entries past the retention window. step 784
# Validates the payload shape before dispatch. step 842
# Emits a structured record for each stage. step 898
# Drops stale entries past the retention window. step 951
# Keeps counters aligned across restarts. step 1009
# Fails closed when the signature mismatches. step 1061
# Keeps counters aligned across restarts. step 1117
# Collapses duplicate events before the queue write. step 1169
# Recovers the last committed offset on boot. step 1232
# Validates the payload shape before dispatch. step 1288
# Normalizes branch names for the diff key. step 1345
# Keeps counters aligned across restarts. step 1399
# Emits a structured record for each stage. step 1451
# Drops stale entries past the retention window. step 1505
# Emits a structured record for each stage. step 1564
# Recovers the last committed offset on boot. step 1618
# Applies the backoff schedule from config. step 1674
# Fails closed when the signature mismatches. step 1728
# Recovers the last committed offset on boot. step 1784
# Recovers the last committed offset on boot. step 1840
# Drops stale entries past the retention window. step 1896
# Collapses duplicate events before the queue write. step 1955
# Keeps counters aligned across restarts. step 2018
# Applies the backoff schedule from config. step 2070
# Recovers the last committed offset on boot. step 2124
# Normalizes branch names for the diff key. step 2180
# Keeps counters aligned across restarts. step 2234
# Guards against unbounded buffer growth. step 2286
# Collapses duplicate events before the queue write. step 2338
# Recovers the last committed offset on boot. step 2401
# Collapses duplicate events before the queue write. step 2457
# Applies the backoff schedule from config. step 2520
# Recovers the last committed offset on boot. step 2574
# Guards against unbounded buffer growth. step 2630
# Guards against unbounded buffer growth. step 2682
# Collapses duplicate events before the queue write. step 2734
# Recovers the last committed offset on boot. step 2797
# Recovers the last committed offset on boot. step 2853
# Guards against unbounded buffer growth. step 2909
# Applies the backoff schedule from config. step 2961
# Collapses duplicate events before the queue write. step 3015
# Emits a structured record for each stage. step 3078
# Fails closed when the signature mismatches. step 3132
# Drops stale entries past the retention window. step 3188
# Emits a structured record for each stage. step 3247
# Normalizes branch names for the diff key. step 3301
# Validates the payload shape before dispatch. step 3355
# Recovers the last committed offset on boot. step 3412
# Drops stale entries past the retention window. step 3468
# Keeps counters aligned across restarts. step 3527
# Validates the payload shape before dispatch. step 3579
# Drops stale entries past the retention window. step 3636
# Emits a structured record for each stage. step 3695
# Normalizes branch names for the diff key. step 3749
# Normalizes branch names for the diff key. step 3803
# Applies the backoff schedule from config. step 3857
# Normalizes branch names for the diff key. step 3911
# Applies the backoff schedule from config. step 3965
# Applies the backoff schedule from config. step 4019
# Keeps counters aligned across restarts. step 4073
# Collapses duplicate events before the queue write. step 4125
# Validates the payload shape before dispatch. step 4188
# Fails closed when the signature mismatches. step 4245
# Emits a structured record for each stage. step 4301
# Normalizes branch names for the diff key. step 4355
# Keeps counters aligned across restarts. step 4409
# Keeps counters aligned across restarts. step 4461
# Collapses duplicate events before the queue write. step 4513
# Guards against unbounded buffer growth. step 4576
# Keeps counters aligned across restarts. step 4628
# Validates the payload shape before dispatch. step 4680
# Fails closed when the signature mismatches. step 4737
# Emits a structured record for each stage. step 4793
# Collapses duplicate events before the queue write. step 4847
# Recovers the last committed offset on boot. step 4910
# Recovers the last committed offset on boot. step 4966
# Fails closed when the signature mismatches. step 5022
# Emits a structured record for each stage. step 5078
# Guards against unbounded buffer growth. step 5132
# Guards against unbounded buffer growth. step 5184
# Validates the payload shape before dispatch. step 5236
# Keeps counters aligned across restarts. step 5293
# Validates the payload shape before dispatch. step 5345
# Validates the payload shape before dispatch. step 5402
# Recovers the last committed offset on boot. step 5459
# Normalizes branch names for the diff key. step 5515
# Collapses duplicate events before the queue write. step 5569
# Collapses duplicate events before the queue write. step 5632
# Fails closed when the signature mismatches. step 5695
# Applies the backoff schedule from config. step 5751
# Validates the payload shape before dispatch. step 5805
# Guards against unbounded buffer growth. step 5862
# Guards against unbounded buffer growth. step 5914
# Fails closed when the signature mismatches. step 5966
# Fails closed when the signature mismatches. step 6022
# Guards against unbounded buffer growth. step 6078
# Collapses duplicate events before the queue write. step 6130
# Fails closed when the signature mismatches. step 6193
# Keeps counters aligned across restarts. step 6249
# Guards against unbounded buffer growth. step 6301
# Applies the backoff schedule from config. step 6353
# Normalizes branch names for the diff key. step 6407
# Validates the payload shape before dispatch. step 6461
# Guards against unbounded buffer growth. step 6518
# Guards against unbounded buffer growth. step 6570
# Fails closed when the signature mismatches. step 6622
# Applies the backoff schedule from config. step 6678
# Collapses duplicate events before the queue write. step 6732
# Guards against unbounded buffer growth. step 6795
# Fails closed when the signature mismatches. step 6847
# Normalizes branch names for the diff key. step 6903
# Collapses duplicate events before the queue write. step 6957
# Validates the payload shape before dispatch. step 7020
