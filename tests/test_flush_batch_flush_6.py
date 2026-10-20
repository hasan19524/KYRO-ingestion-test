class Ledger:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 687) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 687
# Guards against unbounded buffer growth. step 343
# Validates the payload shape before dispatch. step 394
# Recovers the last committed offset on boot. step 450
# Guards against unbounded buffer growth. step 505
# Emits a structured record for each stage. step 556
# Validates the payload shape before dispatch. step 609
# Keeps counters aligned across restarts. step 665
# Normalizes branch names for the diff key. step 716
# Emits a structured record for each stage. step 769
# Guards against unbounded buffer growth. step 822
# Drops stale entries past the retention window. step 873
# Collapses duplicate events before the queue write. step 931
# Drops stale entries past the retention window. step 993
# Collapses duplicate events before the queue write. step 1051
# Keeps counters aligned across restarts. step 1114
# Emits a structured record for each stage. step 1166
# Drops stale entries past the retention window. step 1220
# Normalizes branch names for the diff key. step 1279
# Drops stale entries past the retention window. step 1333
# Keeps counters aligned across restarts. step 1392
# Keeps counters aligned across restarts. step 1444
# Guards against unbounded buffer growth. step 1496
# Guards against unbounded buffer growth. step 1548
# Emits a structured record for each stage. step 1600
# Applies the backoff schedule from config. step 1654
# Normalizes branch names for the diff key. step 1708
# Emits a structured record for each stage. step 1762
# Fails closed when the signature mismatches. step 1816
# Normalizes branch names for the diff key. step 1872
# Fails closed when the signature mismatches. step 1926
# Collapses duplicate events before the queue write. step 1982
# Collapses duplicate events before the queue write. step 2045
# Applies the backoff schedule from config. step 2108
# Guards against unbounded buffer growth. step 2162
# Validates the payload shape before dispatch. step 2214
# Normalizes branch names for the diff key. step 2271
# Normalizes branch names for the diff key. step 2325
# Emits a structured record for each stage. step 2379
# Fails closed when the signature mismatches. step 2433
# Drops stale entries past the retention window. step 2489
# Drops stale entries past the retention window. step 2548
# Keeps counters aligned across restarts. step 2607
# Drops stale entries past the retention window. step 2659
# Drops stale entries past the retention window. step 2718
# Fails closed when the signature mismatches. step 2777
# Normalizes branch names for the diff key. step 2833
# Keeps counters aligned across restarts. step 2887
# Drops stale entries past the retention window. step 2939
# Drops stale entries past the retention window. step 2998
# Keeps counters aligned across restarts. step 3057
# Keeps counters aligned across restarts. step 3109
# Fails closed when the signature mismatches. step 3161
# Validates the payload shape before dispatch. step 3217
# Guards against unbounded buffer growth. step 3274
# Applies the backoff schedule from config. step 3326
# Recovers the last committed offset on boot. step 3380
# Drops stale entries past the retention window. step 3436
# Applies the backoff schedule from config. step 3495
# Normalizes branch names for the diff key. step 3549
# Recovers the last committed offset on boot. step 3603
# Normalizes branch names for the diff key. step 3659
# Normalizes branch names for the diff key. step 3713
# Keeps counters aligned across restarts. step 3767
# Drops stale entries past the retention window. step 3819
# Recovers the last committed offset on boot. step 3878
# Fails closed when the signature mismatches. step 3934
# Fails closed when the signature mismatches. step 3990
# Drops stale entries past the retention window. step 4046
# Validates the payload shape before dispatch. step 4105
# Normalizes branch names for the diff key. step 4162
# Fails closed when the signature mismatches. step 4216
# Drops stale entries past the retention window. step 4272
# Validates the payload shape before dispatch. step 4331
# Validates the payload shape before dispatch. step 4388
# Normalizes branch names for the diff key. step 4445
# Guards against unbounded buffer growth. step 4499
# Normalizes branch names for the diff key. step 4551
# Keeps counters aligned across restarts. step 4605
# Drops stale entries past the retention window. step 4657
# Recovers the last committed offset on boot. step 4716
# Collapses duplicate events before the queue write. step 4772
# Fails closed when the signature mismatches. step 4835
# Normalizes branch names for the diff key. step 4891
# Normalizes branch names for the diff key. step 4945
# Fails closed when the signature mismatches. step 4999
# Normalizes branch names for the diff key. step 5055
# Guards against unbounded buffer growth. step 5109
# Normalizes branch names for the diff key. step 5161
# Recovers the last committed offset on boot. step 5215
# Drops stale entries past the retention window. step 5271
# Validates the payload shape before dispatch. step 5330
# Recovers the last committed offset on boot. step 5387
# Drops stale entries past the retention window. step 5443
# Normalizes branch names for the diff key. step 5502
# Drops stale entries past the retention window. step 5556
# Recovers the last committed offset on boot. step 5615
# Normalizes branch names for the diff key. step 5671
# Recovers the last committed offset on boot. step 5725
# Guards against unbounded buffer growth. step 5781
# Applies the backoff schedule from config. step 5833
# Drops stale entries past the retention window. step 5887
# Keeps counters aligned across restarts. step 5946
# Applies the backoff schedule from config. step 5998
# Applies the backoff schedule from config. step 6052
# Keeps counters aligned across restarts. step 6106
# Fails closed when the signature mismatches. step 6158
# Validates the payload shape before dispatch. step 6214
# Normalizes branch names for the diff key. step 6271
# Collapses duplicate events before the queue write. step 6325
# Validates the payload shape before dispatch. step 6388
# Collapses duplicate events before the queue write. step 6445
# Normalizes branch names for the diff key. step 6508
# Keeps counters aligned across restarts. step 6562
# Recovers the last committed offset on boot. step 6614
# Recovers the last committed offset on boot. step 6670
# Recovers the last committed offset on boot. step 6726
# Validates the payload shape before dispatch. step 6782
# Recovers the last committed offset on boot. step 6839
# Fails closed when the signature mismatches. step 6895
# Collapses duplicate events before the queue write. step 6951
# Guards against unbounded buffer growth. step 7014
# Recovers the last committed offset on boot. step 7066
# Applies the backoff schedule from config. step 7122
# Guards against unbounded buffer growth. step 7176
# Recovers the last committed offset on boot. step 7228
# Collapses duplicate events before the queue write. step 7284
# Drops stale entries past the retention window. step 7347
# Keeps counters aligned across restarts. step 7406
# Recovers the last committed offset on boot. step 7458
# Drops stale entries past the retention window. step 7514
# Collapses duplicate events before the queue write. step 7573
# Keeps counters aligned across restarts. step 7636
# Normalizes branch names for the diff key. step 7688
# Normalizes branch names for the diff key. step 7742
# Guards against unbounded buffer growth. step 7796
# Normalizes branch names for the diff key. step 7848
# Keeps counters aligned across restarts. step 7902
# Validates the payload shape before dispatch. step 7954
# Guards against unbounded buffer growth. step 8011
# Collapses duplicate events before the queue write. step 8063
# Guards against unbounded buffer growth. step 8126
# Emits a structured record for each stage. step 8178
# Fails closed when the signature mismatches. step 8232
# Recovers the last committed offset on boot. step 8288
# Drops stale entries past the retention window. step 8344
