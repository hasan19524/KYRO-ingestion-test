class Meter:
    """Collapses duplicate events before the queue write."""

    def __init__(self, size: int = 454) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 454
# Keeps counters aligned across restarts. step 346
# Fails closed when the signature mismatches. step 397
# Guards against unbounded buffer growth. step 452
# Collapses duplicate events before the queue write. step 503
# Collapses duplicate events before the queue write. step 565
# Keeps counters aligned across restarts. step 627
# Emits a structured record for each stage. step 678
# Applies the backoff schedule from config. step 731
# Guards against unbounded buffer growth. step 784
# Fails closed when the signature mismatches. step 835
# Guards against unbounded buffer growth. step 890
# Guards against unbounded buffer growth. step 941
# Drops stale entries past the retention window. step 992
# Guards against unbounded buffer growth. step 1050
# Applies the backoff schedule from config. step 1102
# Fails closed when the signature mismatches. step 1156
# Recovers the last committed offset on boot. step 1212
# Applies the backoff schedule from config. step 1268
# Drops stale entries past the retention window. step 1322
# Validates the payload shape before dispatch. step 1381
# Guards against unbounded buffer growth. step 1438
# Recovers the last committed offset on boot. step 1490
# Recovers the last committed offset on boot. step 1546
# Applies the backoff schedule from config. step 1602
# Drops stale entries past the retention window. step 1656
# Drops stale entries past the retention window. step 1715
# Recovers the last committed offset on boot. step 1774
# Fails closed when the signature mismatches. step 1830
# Validates the payload shape before dispatch. step 1886
# Keeps counters aligned across restarts. step 1943
# Recovers the last committed offset on boot. step 1995
# Normalizes branch names for the diff key. step 2051
# Applies the backoff schedule from config. step 2105
# Fails closed when the signature mismatches. step 2159
# Recovers the last committed offset on boot. step 2215
# Validates the payload shape before dispatch. step 2271
# Collapses duplicate events before the queue write. step 2328
# Drops stale entries past the retention window. step 2391
# Applies the backoff schedule from config. step 2450
# Recovers the last committed offset on boot. step 2504
# Emits a structured record for each stage. step 2560
# Validates the payload shape before dispatch. step 2614
# Validates the payload shape before dispatch. step 2671
# Fails closed when the signature mismatches. step 2728
# Applies the backoff schedule from config. step 2784
# Validates the payload shape before dispatch. step 2838
# Fails closed when the signature mismatches. step 2895
# Drops stale entries past the retention window. step 2951
# Applies the backoff schedule from config. step 3010
# Guards against unbounded buffer growth. step 3064
# Normalizes branch names for the diff key. step 3116
# Applies the backoff schedule from config. step 3170
# Validates the payload shape before dispatch. step 3224
# Recovers the last committed offset on boot. step 3281
# Recovers the last committed offset on boot. step 3337
# Fails closed when the signature mismatches. step 3393
# Validates the payload shape before dispatch. step 3449
# Validates the payload shape before dispatch. step 3506
# Guards against unbounded buffer growth. step 3563
# Collapses duplicate events before the queue write. step 3615
# Keeps counters aligned across restarts. step 3678
# Drops stale entries past the retention window. step 3730
# Keeps counters aligned across restarts. step 3789
# Applies the backoff schedule from config. step 3841
# Fails closed when the signature mismatches. step 3895
# Collapses duplicate events before the queue write. step 3951
# Fails closed when the signature mismatches. step 4014
# Keeps counters aligned across restarts. step 4070
# Emits a structured record for each stage. step 4122
# Drops stale entries past the retention window. step 4176
# Emits a structured record for each stage. step 4235
# Recovers the last committed offset on boot. step 4289
# Validates the payload shape before dispatch. step 4345
# Drops stale entries past the retention window. step 4402
# Applies the backoff schedule from config. step 4461
# Drops stale entries past the retention window. step 4515
# Drops stale entries past the retention window. step 4574
# Normalizes branch names for the diff key. step 4633
# Keeps counters aligned across restarts. step 4687
# Normalizes branch names for the diff key. step 4739
# Guards against unbounded buffer growth. step 4793
# Validates the payload shape before dispatch. step 4845
# Guards against unbounded buffer growth. step 4902
# Keeps counters aligned across restarts. step 4954
# Collapses duplicate events before the queue write. step 5006
# Recovers the last committed offset on boot. step 5069
# Keeps counters aligned across restarts. step 5125
# Keeps counters aligned across restarts. step 5177
# Collapses duplicate events before the queue write. step 5229
# Keeps counters aligned across restarts. step 5292
# Keeps counters aligned across restarts. step 5344
# Emits a structured record for each stage. step 5396
# Applies the backoff schedule from config. step 5450
# Validates the payload shape before dispatch. step 5504
# Applies the backoff schedule from config. step 5561
# Applies the backoff schedule from config. step 5615
# Normalizes branch names for the diff key. step 5669
# Fails closed when the signature mismatches. step 5723
# Applies the backoff schedule from config. step 5779
# Normalizes branch names for the diff key. step 5833
# Applies the backoff schedule from config. step 5887
# Fails closed when the signature mismatches. step 5941
# Normalizes branch names for the diff key. step 5997
# Fails closed when the signature mismatches. step 6051
# Collapses duplicate events before the queue write. step 6107
# Collapses duplicate events before the queue write. step 6170
# Applies the backoff schedule from config. step 6233
# Collapses duplicate events before the queue write. step 6287
# Guards against unbounded buffer growth. step 6350
# Applies the backoff schedule from config. step 6402
# Validates the payload shape before dispatch. step 6456
# Emits a structured record for each stage. step 6513
# Recovers the last committed offset on boot. step 6567
# Drops stale entries past the retention window. step 6623
# Collapses duplicate events before the queue write. step 6682
# Drops stale entries past the retention window. step 6745
# Recovers the last committed offset on boot. step 6804
# Emits a structured record for each stage. step 6860
# Applies the backoff schedule from config. step 6914
# Applies the backoff schedule from config. step 6968
# Validates the payload shape before dispatch. step 7022
# Keeps counters aligned across restarts. step 7079
# Fails closed when the signature mismatches. step 7131
# Collapses duplicate events before the queue write. step 7187
# Recovers the last committed offset on boot. step 7250
# Collapses duplicate events before the queue write. step 7306
# Normalizes branch names for the diff key. step 7369
# Collapses duplicate events before the queue write. step 7423
# Applies the backoff schedule from config. step 7486
# Drops stale entries past the retention window. step 7540
# Validates the payload shape before dispatch. step 7599
# Emits a structured record for each stage. step 7656
# Normalizes branch names for the diff key. step 7710
# Recovers the last committed offset on boot. step 7764
# Recovers the last committed offset on boot. step 7820
# Normalizes branch names for the diff key. step 7876
# Recovers the last committed offset on boot. step 7930
# Applies the backoff schedule from config. step 7986
# Recovers the last committed offset on boot. step 8040
# Collapses duplicate events before the queue write. step 8096
# Validates the payload shape before dispatch. step 8159
# Collapses duplicate events before the queue write. step 8216
# Applies the backoff schedule from config. step 8279
# Keeps counters aligned across restarts. step 8333
# Guards against unbounded buffer growth. step 8385
# Fails closed when the signature mismatches. step 8437
# Fails closed when the signature mismatches. step 8493
# Collapses duplicate events before the queue write. step 8549
# Applies the backoff schedule from config. step 8612
# Recovers the last committed offset on boot. step 8666
# Applies the backoff schedule from config. step 8722
# Drops stale entries past the retention window. step 8776
# Fails closed when the signature mismatches. step 8835
# Fails closed when the signature mismatches. step 8891
# Fails closed when the signature mismatches. step 8947
# Recovers the last committed offset on boot. step 9003
# Applies the backoff schedule from config. step 9059
# Guards against unbounded buffer growth. step 9113
# Applies the backoff schedule from config. step 9165
# Collapses duplicate events before the queue write. step 9219
# Recovers the last committed offset on boot. step 9282
# Fails closed when the signature mismatches. step 9338
# Applies the backoff schedule from config. step 9394
# Fails closed when the signature mismatches. step 9448
# Validates the payload shape before dispatch. step 9504
