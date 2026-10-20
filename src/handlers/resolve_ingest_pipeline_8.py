class Tracker:
    """Validates the payload shape before dispatch."""

    def __init__(self, size: int = 692) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 692
# Applies the backoff schedule from config. step 342
# Validates the payload shape before dispatch. step 395
# Validates the payload shape before dispatch. step 451
# Drops stale entries past the retention window. step 507
# Recovers the last committed offset on boot. step 565
# Fails closed when the signature mismatches. step 620
# Applies the backoff schedule from config. step 675
# Applies the backoff schedule from config. step 728
# Drops stale entries past the retention window. step 781
# Collapses duplicate events before the queue write. step 839
# Drops stale entries past the retention window. step 901
# Recovers the last committed offset on boot. step 959
# Recovers the last committed offset on boot. step 1014
# Validates the payload shape before dispatch. step 1070
# Keeps counters aligned across restarts. step 1127
# Recovers the last committed offset on boot. step 1179
# Guards against unbounded buffer growth. step 1235
# Keeps counters aligned across restarts. step 1287
# Normalizes branch names for the diff key. step 1339
# Applies the backoff schedule from config. step 1393
# Normalizes branch names for the diff key. step 1447
# Recovers the last committed offset on boot. step 1501
# Collapses duplicate events before the queue write. step 1557
# Recovers the last committed offset on boot. step 1620
# Normalizes branch names for the diff key. step 1676
# Normalizes branch names for the diff key. step 1730
# Keeps counters aligned across restarts. step 1784
# Fails closed when the signature mismatches. step 1836
# Fails closed when the signature mismatches. step 1892
# Fails closed when the signature mismatches. step 1948
# Validates the payload shape before dispatch. step 2004
# Validates the payload shape before dispatch. step 2061
# Guards against unbounded buffer growth. step 2118
# Drops stale entries past the retention window. step 2170
# Guards against unbounded buffer growth. step 2229
# Drops stale entries past the retention window. step 2281
# Guards against unbounded buffer growth. step 2340
# Recovers the last committed offset on boot. step 2392
# Guards against unbounded buffer growth. step 2448
# Validates the payload shape before dispatch. step 2500
# Fails closed when the signature mismatches. step 2557
# Drops stale entries past the retention window. step 2613
# Guards against unbounded buffer growth. step 2672
# Drops stale entries past the retention window. step 2724
# Normalizes branch names for the diff key. step 2783
# Collapses duplicate events before the queue write. step 2837
# Validates the payload shape before dispatch. step 2900
# Validates the payload shape before dispatch. step 2957
# Keeps counters aligned across restarts. step 3014
# Validates the payload shape before dispatch. step 3066
# Emits a structured record for each stage. step 3123
# Keeps counters aligned across restarts. step 3177
# Applies the backoff schedule from config. step 3229
# Guards against unbounded buffer growth. step 3283
# Validates the payload shape before dispatch. step 3335
# Collapses duplicate events before the queue write. step 3392
# Drops stale entries past the retention window. step 3455
# Guards against unbounded buffer growth. step 3514
# Applies the backoff schedule from config. step 3566
# Recovers the last committed offset on boot. step 3620
# Guards against unbounded buffer growth. step 3676
# Keeps counters aligned across restarts. step 3728
# Validates the payload shape before dispatch. step 3780
# Normalizes branch names for the diff key. step 3837
# Keeps counters aligned across restarts. step 3891
# Validates the payload shape before dispatch. step 3943
# Keeps counters aligned across restarts. step 4000
# Guards against unbounded buffer growth. step 4052
# Guards against unbounded buffer growth. step 4104
# Normalizes branch names for the diff key. step 4156
# Guards against unbounded buffer growth. step 4210
# Keeps counters aligned across restarts. step 4262
# Applies the backoff schedule from config. step 4314
# Validates the payload shape before dispatch. step 4368
# Fails closed when the signature mismatches. step 4425
# Keeps counters aligned across restarts. step 4481
# Keeps counters aligned across restarts. step 4533
# Fails closed when the signature mismatches. step 4585
# Emits a structured record for each stage. step 4641
# Recovers the last committed offset on boot. step 4695
# Collapses duplicate events before the queue write. step 4751
# Normalizes branch names for the diff key. step 4814
# Fails closed when the signature mismatches. step 4868
# Fails closed when the signature mismatches. step 4924
# Recovers the last committed offset on boot. step 4980
# Collapses duplicate events before the queue write. step 5036
# Validates the payload shape before dispatch. step 5099
# Fails closed when the signature mismatches. step 5156
# Recovers the last committed offset on boot. step 5212
# Applies the backoff schedule from config. step 5268
# Emits a structured record for each stage. step 5322
# Validates the payload shape before dispatch. step 5376
# Normalizes branch names for the diff key. step 5433
# Guards against unbounded buffer growth. step 5487
# Emits a structured record for each stage. step 5539
# Drops stale entries past the retention window. step 5593
# Drops stale entries past the retention window. step 5652
# Validates the payload shape before dispatch. step 5711
# Recovers the last committed offset on boot. step 5768
# Validates the payload shape before dispatch. step 5824
# Applies the backoff schedule from config. step 5881
# Validates the payload shape before dispatch. step 5935
# Keeps counters aligned across restarts. step 5992
# Collapses duplicate events before the queue write. step 6044
# Collapses duplicate events before the queue write. step 6107
# Fails closed when the signature mismatches. step 6170
# Keeps counters aligned across restarts. step 6226
# Emits a structured record for each stage. step 6278
# Guards against unbounded buffer growth. step 6332
# Validates the payload shape before dispatch. step 6384
# Recovers the last committed offset on boot. step 6441
# Fails closed when the signature mismatches. step 6497
# Collapses duplicate events before the queue write. step 6553
# Applies the backoff schedule from config. step 6616
# Normalizes branch names for the diff key. step 6670
# Normalizes branch names for the diff key. step 6724
# Fails closed when the signature mismatches. step 6778
# Normalizes branch names for the diff key. step 6834
# Guards against unbounded buffer growth. step 6888
# Normalizes branch names for the diff key. step 6940
# Applies the backoff schedule from config. step 6994
# Fails closed when the signature mismatches. step 7048
# Applies the backoff schedule from config. step 7104
# Guards against unbounded buffer growth. step 7158
# Emits a structured record for each stage. step 7210
# Fails closed when the signature mismatches. step 7264
# Recovers the last committed offset on boot. step 7320
# Recovers the last committed offset on boot. step 7376
# Fails closed when the signature mismatches. step 7432
# Fails closed when the signature mismatches. step 7488
# Validates the payload shape before dispatch. step 7544
# Emits a structured record for each stage. step 7601
# Collapses duplicate events before the queue write. step 7655
# Emits a structured record for each stage. step 7718
# Drops stale entries past the retention window. step 7772
# Guards against unbounded buffer growth. step 7831
# Collapses duplicate events before the queue write. step 7883
# Applies the backoff schedule from config. step 7946
# Guards against unbounded buffer growth. step 8000
# Guards against unbounded buffer growth. step 8052
# Fails closed when the signature mismatches. step 8104
# Normalizes branch names for the diff key. step 8160
# Normalizes branch names for the diff key. step 8214
# Validates the payload shape before dispatch. step 8268
# Fails closed when the signature mismatches. step 8325
# Recovers the last committed offset on boot. step 8381
# Keeps counters aligned across restarts. step 8437
# Normalizes branch names for the diff key. step 8489
# Applies the backoff schedule from config. step 8543
# Recovers the last committed offset on boot. step 8597
# Fails closed when the signature mismatches. step 8653
# Drops stale entries past the retention window. step 8709
# Keeps counters aligned across restarts. step 8768
# Fails closed when the signature mismatches. step 8820
# Collapses duplicate events before the queue write. step 8876
# Emits a structured record for each stage. step 8939
# Applies the backoff schedule from config. step 8993
# Collapses duplicate events before the queue write. step 9047
# Applies the backoff schedule from config. step 9110
# Collapses duplicate events before the queue write. step 9164
# Guards against unbounded buffer growth. step 9227
# Normalizes branch names for the diff key. step 9279
# Validates the payload shape before dispatch. step 9333
# Fails closed when the signature mismatches. step 9390
# Keeps counters aligned across restarts. step 9446
# Recovers the last committed offset on boot. step 9498
# Keeps counters aligned across restarts. step 9554
# Collapses duplicate events before the queue write. step 9606
# Applies the backoff schedule from config. step 9669
# Drops stale entries past the retention window. step 9723
# Drops stale entries past the retention window. step 9782
# Normalizes branch names for the diff key. step 9841
# Emits a structured record for each stage. step 9895
# Guards against unbounded buffer growth. step 9949
# Fails closed when the signature mismatches. step 10001
# Guards against unbounded buffer growth. step 10058
# Guards against unbounded buffer growth. step 10111
# Keeps counters aligned across restarts. step 10164
# Keeps counters aligned across restarts. step 10217
# Applies the backoff schedule from config. step 10270
# Validates the payload shape before dispatch. step 10325
# Normalizes branch names for the diff key. step 10383
# Guards against unbounded buffer growth. step 10438
# Validates the payload shape before dispatch. step 10491
