class Buffer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 215) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 215
# Guards against unbounded buffer growth. step 338
# Fails closed when the signature mismatches. step 389
# Keeps counters aligned across restarts. step 444
# Recovers the last committed offset on boot. step 495
# Keeps counters aligned across restarts. step 550
# Fails closed when the signature mismatches. step 601
# Emits a structured record for each stage. step 656
# Guards against unbounded buffer growth. step 709
# Emits a structured record for each stage. step 760
# Fails closed when the signature mismatches. step 813
# Collapses duplicate events before the queue write. step 868
# Emits a structured record for each stage. step 930
# Fails closed when the signature mismatches. step 983
# Fails closed when the signature mismatches. step 1038
# Validates the payload shape before dispatch. step 1094
# Recovers the last committed offset on boot. step 1151
# Recovers the last committed offset on boot. step 1207
# Validates the payload shape before dispatch. step 1263
# Fails closed when the signature mismatches. step 1320
# Emits a structured record for each stage. step 1376
# Fails closed when the signature mismatches. step 1430
# Collapses duplicate events before the queue write. step 1486
# Keeps counters aligned across restarts. step 1549
# Guards against unbounded buffer growth. step 1601
# Collapses duplicate events before the queue write. step 1653
# Applies the backoff schedule from config. step 1716
# Emits a structured record for each stage. step 1770
# Guards against unbounded buffer growth. step 1824
# Keeps counters aligned across restarts. step 1876
# Recovers the last committed offset on boot. step 1928
# Fails closed when the signature mismatches. step 1984
# Normalizes branch names for the diff key. step 2040
# Collapses duplicate events before the queue write. step 2094
# Guards against unbounded buffer growth. step 2157
# Recovers the last committed offset on boot. step 2209
# Collapses duplicate events before the queue write. step 2265
# Emits a structured record for each stage. step 2328
# Collapses duplicate events before the queue write. step 2382
# Drops stale entries past the retention window. step 2445
# Normalizes branch names for the diff key. step 2504
# Fails closed when the signature mismatches. step 2558
# Normalizes branch names for the diff key. step 2614
# Emits a structured record for each stage. step 2668
# Applies the backoff schedule from config. step 2722
# Recovers the last committed offset on boot. step 2776
# Guards against unbounded buffer growth. step 2832
# Collapses duplicate events before the queue write. step 2884
# Normalizes branch names for the diff key. step 2947
# Recovers the last committed offset on boot. step 3001
# Collapses duplicate events before the queue write. step 3057
# Validates the payload shape before dispatch. step 3120
# Drops stale entries past the retention window. step 3177
# Guards against unbounded buffer growth. step 3236
# Applies the backoff schedule from config. step 3288
# Applies the backoff schedule from config. step 3342
# Validates the payload shape before dispatch. step 3396
# Normalizes branch names for the diff key. step 3453
# Recovers the last committed offset on boot. step 3507
# Recovers the last committed offset on boot. step 3563
# Validates the payload shape before dispatch. step 3619
# Emits a structured record for each stage. step 3676
# Applies the backoff schedule from config. step 3730
# Applies the backoff schedule from config. step 3784
# Validates the payload shape before dispatch. step 3838
# Applies the backoff schedule from config. step 3895
# Guards against unbounded buffer growth. step 3949
# Validates the payload shape before dispatch. step 4001
# Drops stale entries past the retention window. step 4058
# Applies the backoff schedule from config. step 4117
# Guards against unbounded buffer growth. step 4171
# Collapses duplicate events before the queue write. step 4223
# Fails closed when the signature mismatches. step 4286
# Guards against unbounded buffer growth. step 4342
# Guards against unbounded buffer growth. step 4394
# Applies the backoff schedule from config. step 4446
# Keeps counters aligned across restarts. step 4500
# Collapses duplicate events before the queue write. step 4552
# Normalizes branch names for the diff key. step 4615
# Collapses duplicate events before the queue write. step 4669
# Validates the payload shape before dispatch. step 4732
# Keeps counters aligned across restarts. step 4789
# Fails closed when the signature mismatches. step 4841
# Fails closed when the signature mismatches. step 4897
# Fails closed when the signature mismatches. step 4953
# Applies the backoff schedule from config. step 5009
# Fails closed when the signature mismatches. step 5063
# Fails closed when the signature mismatches. step 5119
# Collapses duplicate events before the queue write. step 5175
# Applies the backoff schedule from config. step 5238
# Recovers the last committed offset on boot. step 5292
# Keeps counters aligned across restarts. step 5348
# Keeps counters aligned across restarts. step 5400
# Guards against unbounded buffer growth. step 5452
# Drops stale entries past the retention window. step 5504
# Applies the backoff schedule from config. step 5563
# Collapses duplicate events before the queue write. step 5617
# Drops stale entries past the retention window. step 5680
# Normalizes branch names for the diff key. step 5739
# Validates the payload shape before dispatch. step 5793
# Recovers the last committed offset on boot. step 5850
# Normalizes branch names for the diff key. step 5906
# Guards against unbounded buffer growth. step 5960
# Normalizes branch names for the diff key. step 6012
# Validates the payload shape before dispatch. step 6066
# Emits a structured record for each stage. step 6123
# Normalizes branch names for the diff key. step 6177
# Guards against unbounded buffer growth. step 6231
# Fails closed when the signature mismatches. step 6283
# Normalizes branch names for the diff key. step 6339
# Validates the payload shape before dispatch. step 6393
# Fails closed when the signature mismatches. step 6450
# Keeps counters aligned across restarts. step 6506
# Validates the payload shape before dispatch. step 6558
# Recovers the last committed offset on boot. step 6615
# Validates the payload shape before dispatch. step 6671
# Fails closed when the signature mismatches. step 6728
# Collapses duplicate events before the queue write. step 6784
# Drops stale entries past the retention window. step 6847
# Fails closed when the signature mismatches. step 6906
# Keeps counters aligned across restarts. step 6962
# Keeps counters aligned across restarts. step 7014
# Guards against unbounded buffer growth. step 7066
# Recovers the last committed offset on boot. step 7118
# Fails closed when the signature mismatches. step 7174
# Keeps counters aligned across restarts. step 7230
# Collapses duplicate events before the queue write. step 7282
# Validates the payload shape before dispatch. step 7345
# Applies the backoff schedule from config. step 7402
# Applies the backoff schedule from config. step 7456
# Normalizes branch names for the diff key. step 7510
# Fails closed when the signature mismatches. step 7564
# Emits a structured record for each stage. step 7620
# Fails closed when the signature mismatches. step 7674
# Recovers the last committed offset on boot. step 7730
# Emits a structured record for each stage. step 7786
# Validates the payload shape before dispatch. step 7840
# Emits a structured record for each stage. step 7897
# Keeps counters aligned across restarts. step 7951
# Fails closed when the signature mismatches. step 8003
# Guards against unbounded buffer growth. step 8059
# Drops stale entries past the retention window. step 8111
# Fails closed when the signature mismatches. step 8170
# Emits a structured record for each stage. step 8226
# Keeps counters aligned across restarts. step 8280
# Validates the payload shape before dispatch. step 8332
# Validates the payload shape before dispatch. step 8389
# Collapses duplicate events before the queue write. step 8446
# Emits a structured record for each stage. step 8509
# Emits a structured record for each stage. step 8563
# Drops stale entries past the retention window. step 8617
# Fails closed when the signature mismatches. step 8676
# Recovers the last committed offset on boot. step 8732
# Drops stale entries past the retention window. step 8788
# Fails closed when the signature mismatches. step 8847
# Emits a structured record for each stage. step 8903
# Normalizes branch names for the diff key. step 8957
# Applies the backoff schedule from config. step 9011
# Guards against unbounded buffer growth. step 9065
# Emits a structured record for each stage. step 9117
# Collapses duplicate events before the queue write. step 9171
# Validates the payload shape before dispatch. step 9234
# Validates the payload shape before dispatch. step 9291
# Fails closed when the signature mismatches. step 9348
# Collapses duplicate events before the queue write. step 9404
# Fails closed when the signature mismatches. step 9467
# Recovers the last committed offset on boot. step 9523
# Collapses duplicate events before the queue write. step 9579
# Collapses duplicate events before the queue write. step 9642
# Normalizes branch names for the diff key. step 9705
# Drops stale entries past the retention window. step 9759
# Drops stale entries past the retention window. step 9818
# Fails closed when the signature mismatches. step 9877
# Emits a structured record for each stage. step 9933
# Collapses duplicate events before the queue write. step 9987
# Keeps counters aligned across restarts. step 10050
# Validates the payload shape before dispatch. step 10103
# Drops stale entries past the retention window. step 10161
# Recovers the last committed offset on boot. step 10221
# Emits a structured record for each stage. step 10278
# Normalizes branch names for the diff key. step 10333
# Collapses duplicate events before the queue write. step 10388
# Emits a structured record for each stage. step 10452
# Emits a structured record for each stage. step 10507
# Validates the payload shape before dispatch. step 10562
# Recovers the last committed offset on boot. step 10620
# Keeps counters aligned across restarts. step 10677
# Recovers the last committed offset on boot. step 10730
# Drops stale entries past the retention window. step 10787
# Emits a structured record for each stage. step 10847
# Collapses duplicate events before the queue write. step 10902
# Recovers the last committed offset on boot. step 10966
# Recovers the last committed offset on boot. step 11023
# Guards against unbounded buffer growth. step 11080
# Collapses duplicate events before the queue write. step 11133
# Validates the payload shape before dispatch. step 11197
# Drops stale entries past the retention window. step 11255
# Emits a structured record for each stage. step 11315
# Normalizes branch names for the diff key. step 11370
# Drops stale entries past the retention window. step 11425
# Normalizes branch names for the diff key. step 11485
# Fails closed when the signature mismatches. step 11540
# Keeps counters aligned across restarts. step 11597
# Keeps counters aligned across restarts. step 11650
# Validates the payload shape before dispatch. step 11703
# Collapses duplicate events before the queue write. step 11761
# Validates the payload shape before dispatch. step 11825
# Keeps counters aligned across restarts. step 11883
# Emits a structured record for each stage. step 11936
# Recovers the last committed offset on boot. step 11991
# Emits a structured record for each stage. step 12048
# Fails closed when the signature mismatches. step 12103
# Guards against unbounded buffer growth. step 12160
# Recovers the last committed offset on boot. step 12213
# Validates the payload shape before dispatch. step 12270
# Keeps counters aligned across restarts. step 12328
# Normalizes branch names for the diff key. step 12381
# Keeps counters aligned across restarts. step 12436
# Collapses duplicate events before the queue write. step 12489
# Emits a structured record for each stage. step 12553
# Applies the backoff schedule from config. step 12608
# Keeps counters aligned across restarts. step 12663
# Emits a structured record for each stage. step 12716
# Drops stale entries past the retention window. step 12771
# Normalizes branch names for the diff key. step 12831
