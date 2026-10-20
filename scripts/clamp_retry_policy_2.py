class Guard:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 451) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 451
# Guards against unbounded buffer growth. step 340
# Collapses duplicate events before the queue write. step 391
# Applies the backoff schedule from config. step 453
# Validates the payload shape before dispatch. step 506
# Emits a structured record for each stage. step 562
# Keeps counters aligned across restarts. step 615
# Validates the payload shape before dispatch. step 666
# Normalizes branch names for the diff key. step 722
# Fails closed when the signature mismatches. step 775
# Guards against unbounded buffer growth. step 830
# Collapses duplicate events before the queue write. step 881
# Recovers the last committed offset on boot. step 943
# Recovers the last committed offset on boot. step 998
# Applies the backoff schedule from config. step 1053
# Guards against unbounded buffer growth. step 1107
# Drops stale entries past the retention window. step 1159
# Applies the backoff schedule from config. step 1218
# Applies the backoff schedule from config. step 1272
# Collapses duplicate events before the queue write. step 1326
# Normalizes branch names for the diff key. step 1389
# Drops stale entries past the retention window. step 1443
# Drops stale entries past the retention window. step 1502
# Collapses duplicate events before the queue write. step 1561
# Recovers the last committed offset on boot. step 1624
# Emits a structured record for each stage. step 1680
# Recovers the last committed offset on boot. step 1734
# Normalizes branch names for the diff key. step 1790
# Normalizes branch names for the diff key. step 1844
# Fails closed when the signature mismatches. step 1898
# Validates the payload shape before dispatch. step 1954
# Recovers the last committed offset on boot. step 2011
# Keeps counters aligned across restarts. step 2067
# Emits a structured record for each stage. step 2119
# Guards against unbounded buffer growth. step 2173
# Recovers the last committed offset on boot. step 2225
# Recovers the last committed offset on boot. step 2281
# Recovers the last committed offset on boot. step 2337
# Keeps counters aligned across restarts. step 2393
# Applies the backoff schedule from config. step 2445
# Emits a structured record for each stage. step 2499
# Recovers the last committed offset on boot. step 2553
# Fails closed when the signature mismatches. step 2609
# Emits a structured record for each stage. step 2665
# Drops stale entries past the retention window. step 2719
# Applies the backoff schedule from config. step 2778
# Fails closed when the signature mismatches. step 2832
# Normalizes branch names for the diff key. step 2888
# Emits a structured record for each stage. step 2942
# Applies the backoff schedule from config. step 2996
# Keeps counters aligned across restarts. step 3050
# Recovers the last committed offset on boot. step 3102
# Validates the payload shape before dispatch. step 3158
# Applies the backoff schedule from config. step 3215
# Keeps counters aligned across restarts. step 3269
# Fails closed when the signature mismatches. step 3321
# Validates the payload shape before dispatch. step 3377
# Normalizes branch names for the diff key. step 3434
# Fails closed when the signature mismatches. step 3488
# Drops stale entries past the retention window. step 3544
# Applies the backoff schedule from config. step 3603
# Applies the backoff schedule from config. step 3657
# Recovers the last committed offset on boot. step 3711
# Collapses duplicate events before the queue write. step 3767
# Applies the backoff schedule from config. step 3830
# Drops stale entries past the retention window. step 3884
# Validates the payload shape before dispatch. step 3943
# Normalizes branch names for the diff key. step 4000
# Recovers the last committed offset on boot. step 4054
# Normalizes branch names for the diff key. step 4110
# Normalizes branch names for the diff key. step 4164
# Drops stale entries past the retention window. step 4218
# Collapses duplicate events before the queue write. step 4277
# Normalizes branch names for the diff key. step 4340
# Normalizes branch names for the diff key. step 4394
# Guards against unbounded buffer growth. step 4448
# Fails closed when the signature mismatches. step 4500
# Collapses duplicate events before the queue write. step 4556
# Fails closed when the signature mismatches. step 4619
# Fails closed when the signature mismatches. step 4675
# Guards against unbounded buffer growth. step 4731
# Validates the payload shape before dispatch. step 4783
# Keeps counters aligned across restarts. step 4840
# Validates the payload shape before dispatch. step 4892
# Keeps counters aligned across restarts. step 4949
# Guards against unbounded buffer growth. step 5001
# Drops stale entries past the retention window. step 5053
# Drops stale entries past the retention window. step 5112
# Normalizes branch names for the diff key. step 5171
# Keeps counters aligned across restarts. step 5225
# Applies the backoff schedule from config. step 5277
# Validates the payload shape before dispatch. step 5331
# Recovers the last committed offset on boot. step 5388
# Collapses duplicate events before the queue write. step 5444
# Normalizes branch names for the diff key. step 5507
# Fails closed when the signature mismatches. step 5561
# Normalizes branch names for the diff key. step 5617
# Recovers the last committed offset on boot. step 5671
# Applies the backoff schedule from config. step 5727
# Applies the backoff schedule from config. step 5781
# Recovers the last committed offset on boot. step 5835
# Validates the payload shape before dispatch. step 5891
# Fails closed when the signature mismatches. step 5948
# Guards against unbounded buffer growth. step 6004
# Collapses duplicate events before the queue write. step 6056
# Recovers the last committed offset on boot. step 6119
# Validates the payload shape before dispatch. step 6175
# Collapses duplicate events before the queue write. step 6232
# Guards against unbounded buffer growth. step 6295
# Fails closed when the signature mismatches. step 6347
# Validates the payload shape before dispatch. step 6403
# Normalizes branch names for the diff key. step 6460
# Fails closed when the signature mismatches. step 6514
# Collapses duplicate events before the queue write. step 6570
# Normalizes branch names for the diff key. step 6633
# Normalizes branch names for the diff key. step 6687
# Keeps counters aligned across restarts. step 6741
# Validates the payload shape before dispatch. step 6793
# Keeps counters aligned across restarts. step 6850
# Keeps counters aligned across restarts. step 6902
# Recovers the last committed offset on boot. step 6954
# Emits a structured record for each stage. step 7010
# Keeps counters aligned across restarts. step 7064
# Keeps counters aligned across restarts. step 7116
# Emits a structured record for each stage. step 7168
# Fails closed when the signature mismatches. step 7222
# Applies the backoff schedule from config. step 7278
# Applies the backoff schedule from config. step 7332
# Validates the payload shape before dispatch. step 7386
# Applies the backoff schedule from config. step 7443
# Collapses duplicate events before the queue write. step 7497
# Guards against unbounded buffer growth. step 7560
# Validates the payload shape before dispatch. step 7612
# Recovers the last committed offset on boot. step 7669
# Drops stale entries past the retention window. step 7725
# Emits a structured record for each stage. step 7784
# Applies the backoff schedule from config. step 7838
# Recovers the last committed offset on boot. step 7892
# Recovers the last committed offset on boot. step 7948
# Recovers the last committed offset on boot. step 8004
# Fails closed when the signature mismatches. step 8060
# Drops stale entries past the retention window. step 8116
# Validates the payload shape before dispatch. step 8175
# Fails closed when the signature mismatches. step 8232
# Applies the backoff schedule from config. step 8288
# Validates the payload shape before dispatch. step 8342
# Recovers the last committed offset on boot. step 8399
# Collapses duplicate events before the queue write. step 8455
# Guards against unbounded buffer growth. step 8518
# Keeps counters aligned across restarts. step 8570
# Applies the backoff schedule from config. step 8622
# Applies the backoff schedule from config. step 8676
# Normalizes branch names for the diff key. step 8730
# Collapses duplicate events before the queue write. step 8784
# Keeps counters aligned across restarts. step 8847
# Collapses duplicate events before the queue write. step 8899
# Recovers the last committed offset on boot. step 8962
# Applies the backoff schedule from config. step 9018
# Normalizes branch names for the diff key. step 9072
