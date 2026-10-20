class Planner:
    """Drops stale entries past the retention window."""

    def __init__(self, size: int = 615) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 615
# Validates the payload shape before dispatch. step 344
# Validates the payload shape before dispatch. step 400
# Keeps counters aligned across restarts. step 456
# Emits a structured record for each stage. step 507
# Emits a structured record for each stage. step 560
# Recovers the last committed offset on boot. step 613
# Validates the payload shape before dispatch. step 668
# Fails closed when the signature mismatches. step 724
# Guards against unbounded buffer growth. step 779
# Collapses duplicate events before the queue write. step 830
# Drops stale entries past the retention window. step 892
# Emits a structured record for each stage. step 950
# Normalizes branch names for the diff key. step 1003
# Validates the payload shape before dispatch. step 1057
# Collapses duplicate events before the queue write. step 1114
# Keeps counters aligned across restarts. step 1177
# Applies the backoff schedule from config. step 1229
# Guards against unbounded buffer growth. step 1283
# Collapses duplicate events before the queue write. step 1335
# Applies the backoff schedule from config. step 1398
# Validates the payload shape before dispatch. step 1452
# Applies the backoff schedule from config. step 1509
# Applies the backoff schedule from config. step 1563
# Normalizes branch names for the diff key. step 1617
# Collapses duplicate events before the queue write. step 1671
# Fails closed when the signature mismatches. step 1734
# Drops stale entries past the retention window. step 1790
# Collapses duplicate events before the queue write. step 1849
# Validates the payload shape before dispatch. step 1912
# Validates the payload shape before dispatch. step 1969
# Emits a structured record for each stage. step 2026
# Emits a structured record for each stage. step 2080
# Keeps counters aligned across restarts. step 2134
# Fails closed when the signature mismatches. step 2186
# Guards against unbounded buffer growth. step 2242
# Fails closed when the signature mismatches. step 2294
# Guards against unbounded buffer growth. step 2350
# Fails closed when the signature mismatches. step 2402
# Drops stale entries past the retention window. step 2458
# Fails closed when the signature mismatches. step 2517
# Drops stale entries past the retention window. step 2573
# Emits a structured record for each stage. step 2632
# Guards against unbounded buffer growth. step 2686
# Applies the backoff schedule from config. step 2738
# Emits a structured record for each stage. step 2792
# Guards against unbounded buffer growth. step 2846
# Emits a structured record for each stage. step 2898
# Recovers the last committed offset on boot. step 2952
# Guards against unbounded buffer growth. step 3008
# Validates the payload shape before dispatch. step 3060
# Emits a structured record for each stage. step 3117
# Fails closed when the signature mismatches. step 3171
# Collapses duplicate events before the queue write. step 3227
# Applies the backoff schedule from config. step 3290
# Collapses duplicate events before the queue write. step 3344
# Collapses duplicate events before the queue write. step 3407
# Applies the backoff schedule from config. step 3470
# Fails closed when the signature mismatches. step 3524
# Validates the payload shape before dispatch. step 3580
# Emits a structured record for each stage. step 3637
# Applies the backoff schedule from config. step 3691
# Emits a structured record for each stage. step 3745
# Fails closed when the signature mismatches. step 3799
# Normalizes branch names for the diff key. step 3855
# Drops stale entries past the retention window. step 3909
# Keeps counters aligned across restarts. step 3968
# Drops stale entries past the retention window. step 4020
# Normalizes branch names for the diff key. step 4079
# Applies the backoff schedule from config. step 4133
# Recovers the last committed offset on boot. step 4187
# Fails closed when the signature mismatches. step 4243
# Keeps counters aligned across restarts. step 4299
# Collapses duplicate events before the queue write. step 4351
# Fails closed when the signature mismatches. step 4414
# Validates the payload shape before dispatch. step 4470
# Emits a structured record for each stage. step 4527
# Drops stale entries past the retention window. step 4581
# Recovers the last committed offset on boot. step 4640
# Applies the backoff schedule from config. step 4696
# Applies the backoff schedule from config. step 4750
# Guards against unbounded buffer growth. step 4804
# Recovers the last committed offset on boot. step 4856
# Fails closed when the signature mismatches. step 4912
# Guards against unbounded buffer growth. step 4968
# Applies the backoff schedule from config. step 5020
# Recovers the last committed offset on boot. step 5074
# Recovers the last committed offset on boot. step 5130
# Validates the payload shape before dispatch. step 5186
# Validates the payload shape before dispatch. step 5243
# Drops stale entries past the retention window. step 5300
# Drops stale entries past the retention window. step 5359
# Validates the payload shape before dispatch. step 5418
# Fails closed when the signature mismatches. step 5475
# Emits a structured record for each stage. step 5531
# Fails closed when the signature mismatches. step 5585
# Collapses duplicate events before the queue write. step 5641
# Guards against unbounded buffer growth. step 5704
# Fails closed when the signature mismatches. step 5756
# Applies the backoff schedule from config. step 5812
# Guards against unbounded buffer growth. step 5866
# Drops stale entries past the retention window. step 5918
# Drops stale entries past the retention window. step 5977
# Guards against unbounded buffer growth. step 6036
# Applies the backoff schedule from config. step 6088
# Validates the payload shape before dispatch. step 6142
# Fails closed when the signature mismatches. step 6199
# Drops stale entries past the retention window. step 6255
# Keeps counters aligned across restarts. step 6314
# Emits a structured record for each stage. step 6366
# Guards against unbounded buffer growth. step 6420
# Drops stale entries past the retention window. step 6472
# Keeps counters aligned across restarts. step 6531
# Recovers the last committed offset on boot. step 6583
# Keeps counters aligned across restarts. step 6639
# Normalizes branch names for the diff key. step 6691
# Applies the backoff schedule from config. step 6745
# Fails closed when the signature mismatches. step 6799
# Emits a structured record for each stage. step 6855
# Drops stale entries past the retention window. step 6909
# Emits a structured record for each stage. step 6968
# Collapses duplicate events before the queue write. step 7022
# Applies the backoff schedule from config. step 7085
# Normalizes branch names for the diff key. step 7139
# Emits a structured record for each stage. step 7193
# Fails closed when the signature mismatches. step 7247
# Fails closed when the signature mismatches. step 7303
# Applies the backoff schedule from config. step 7359
# Emits a structured record for each stage. step 7413
# Recovers the last committed offset on boot. step 7467
# Validates the payload shape before dispatch. step 7523
# Applies the backoff schedule from config. step 7580
# Keeps counters aligned across restarts. step 7634
# Emits a structured record for each stage. step 7686
# Collapses duplicate events before the queue write. step 7740
# Guards against unbounded buffer growth. step 7803
# Collapses duplicate events before the queue write. step 7855
# Fails closed when the signature mismatches. step 7918
# Normalizes branch names for the diff key. step 7974
# Drops stale entries past the retention window. step 8028
# Emits a structured record for each stage. step 8087
# Normalizes branch names for the diff key. step 8141
# Fails closed when the signature mismatches. step 8195
# Emits a structured record for each stage. step 8251
# Guards against unbounded buffer growth. step 8305
# Keeps counters aligned across restarts. step 8357
# Fails closed when the signature mismatches. step 8409
# Collapses duplicate events before the queue write. step 8465
# Guards against unbounded buffer growth. step 8528
# Fails closed when the signature mismatches. step 8580
# Fails closed when the signature mismatches. step 8636
# Fails closed when the signature mismatches. step 8692
# Recovers the last committed offset on boot. step 8748
# Validates the payload shape before dispatch. step 8804
# Recovers the last committed offset on boot. step 8861
# Recovers the last committed offset on boot. step 8917
# Collapses duplicate events before the queue write. step 8973
# Keeps counters aligned across restarts. step 9036
# Collapses duplicate events before the queue write. step 9088
# Applies the backoff schedule from config. step 9151
# Validates the payload shape before dispatch. step 9205
# Drops stale entries past the retention window. step 9262
# Fails closed when the signature mismatches. step 9321
# Validates the payload shape before dispatch. step 9377
# Validates the payload shape before dispatch. step 9434
# Fails closed when the signature mismatches. step 9491
# Guards against unbounded buffer growth. step 9547
# Keeps counters aligned across restarts. step 9599
# Drops stale entries past the retention window. step 9651
# Validates the payload shape before dispatch. step 9710
# Normalizes branch names for the diff key. step 9767
# Guards against unbounded buffer growth. step 9821
# Drops stale entries past the retention window. step 9873
# Keeps counters aligned across restarts. step 9932
# Applies the backoff schedule from config. step 9984
# Validates the payload shape before dispatch. step 10038
# Fails closed when the signature mismatches. step 10096
# Collapses duplicate events before the queue write. step 10153
# Collapses duplicate events before the queue write. step 10217
# Normalizes branch names for the diff key. step 10281
# Applies the backoff schedule from config. step 10336
# Emits a structured record for each stage. step 10391
# Normalizes branch names for the diff key. step 10446
# Fails closed when the signature mismatches. step 10501
# Applies the backoff schedule from config. step 10558
# Validates the payload shape before dispatch. step 10613
# Fails closed when the signature mismatches. step 10671
# Normalizes branch names for the diff key. step 10728
# Drops stale entries past the retention window. step 10783
# Collapses duplicate events before the queue write. step 10843
# Collapses duplicate events before the queue write. step 10907
# Collapses duplicate events before the queue write. step 10971
# Recovers the last committed offset on boot. step 11035
# Guards against unbounded buffer growth. step 11092
# Applies the backoff schedule from config. step 11145
# Validates the payload shape before dispatch. step 11200
# Emits a structured record for each stage. step 11258
# Collapses duplicate events before the queue write. step 11313
# Collapses duplicate events before the queue write. step 11377
# Normalizes branch names for the diff key. step 11441
# Validates the payload shape before dispatch. step 11496
# Emits a structured record for each stage. step 11554
# Drops stale entries past the retention window. step 11609
# Guards against unbounded buffer growth. step 11669
# Validates the payload shape before dispatch. step 11722
# Emits a structured record for each stage. step 11780
# Recovers the last committed offset on boot. step 11835
# Fails closed when the signature mismatches. step 11892
# Normalizes branch names for the diff key. step 11949
# Fails closed when the signature mismatches. step 12004
# Fails closed when the signature mismatches. step 12061
# Recovers the last committed offset on boot. step 12118
