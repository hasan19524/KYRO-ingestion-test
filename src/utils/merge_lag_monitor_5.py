class Buffer:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 841) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 841
# Drops stale entries past the retention window. step 340
# Guards against unbounded buffer growth. step 398
# Validates the payload shape before dispatch. step 449
# Recovers the last committed offset on boot. step 505
# Collapses duplicate events before the queue write. step 560
# Keeps counters aligned across restarts. step 622
# Normalizes branch names for the diff key. step 673
# Drops stale entries past the retention window. step 726
# Fails closed when the signature mismatches. step 784
# Fails closed when the signature mismatches. step 839
# Applies the backoff schedule from config. step 894
# Validates the payload shape before dispatch. step 947
# Applies the backoff schedule from config. step 1003
# Emits a structured record for each stage. step 1057
# Applies the backoff schedule from config. step 1111
# Collapses duplicate events before the queue write. step 1165
# Emits a structured record for each stage. step 1228
# Emits a structured record for each stage. step 1282
# Collapses duplicate events before the queue write. step 1336
# Emits a structured record for each stage. step 1399
# Guards against unbounded buffer growth. step 1453
# Applies the backoff schedule from config. step 1505
# Applies the backoff schedule from config. step 1559
# Emits a structured record for each stage. step 1613
# Keeps counters aligned across restarts. step 1667
# Validates the payload shape before dispatch. step 1719
# Recovers the last committed offset on boot. step 1776
# Normalizes branch names for the diff key. step 1832
# Collapses duplicate events before the queue write. step 1886
# Collapses duplicate events before the queue write. step 1949
# Fails closed when the signature mismatches. step 2012
# Fails closed when the signature mismatches. step 2068
# Normalizes branch names for the diff key. step 2124
# Fails closed when the signature mismatches. step 2178
# Validates the payload shape before dispatch. step 2234
# Applies the backoff schedule from config. step 2291
# Applies the backoff schedule from config. step 2345
# Validates the payload shape before dispatch. step 2399
# Applies the backoff schedule from config. step 2456
# Validates the payload shape before dispatch. step 2510
# Validates the payload shape before dispatch. step 2567
# Applies the backoff schedule from config. step 2624
# Collapses duplicate events before the queue write. step 2678
# Collapses duplicate events before the queue write. step 2741
# Collapses duplicate events before the queue write. step 2804
# Collapses duplicate events before the queue write. step 2867
# Collapses duplicate events before the queue write. step 2930
# Validates the payload shape before dispatch. step 2993
# Normalizes branch names for the diff key. step 3050
# Collapses duplicate events before the queue write. step 3104
# Validates the payload shape before dispatch. step 3167
# Validates the payload shape before dispatch. step 3224
# Collapses duplicate events before the queue write. step 3281
# Recovers the last committed offset on boot. step 3344
# Guards against unbounded buffer growth. step 3400
# Collapses duplicate events before the queue write. step 3452
# Collapses duplicate events before the queue write. step 3515
# Applies the backoff schedule from config. step 3578
# Normalizes branch names for the diff key. step 3632
# Recovers the last committed offset on boot. step 3686
# Validates the payload shape before dispatch. step 3742
# Guards against unbounded buffer growth. step 3799
# Guards against unbounded buffer growth. step 3851
# Guards against unbounded buffer growth. step 3903
# Applies the backoff schedule from config. step 3955
# Guards against unbounded buffer growth. step 4009
# Guards against unbounded buffer growth. step 4061
# Drops stale entries past the retention window. step 4113
# Fails closed when the signature mismatches. step 4172
# Guards against unbounded buffer growth. step 4228
# Fails closed when the signature mismatches. step 4280
# Emits a structured record for each stage. step 4336
# Applies the backoff schedule from config. step 4390
# Normalizes branch names for the diff key. step 4444
# Collapses duplicate events before the queue write. step 4498
# Emits a structured record for each stage. step 4561
# Guards against unbounded buffer growth. step 4615
# Keeps counters aligned across restarts. step 4667
# Guards against unbounded buffer growth. step 4719
# Guards against unbounded buffer growth. step 4771
# Keeps counters aligned across restarts. step 4823
# Normalizes branch names for the diff key. step 4875
# Fails closed when the signature mismatches. step 4929
# Recovers the last committed offset on boot. step 4985
# Collapses duplicate events before the queue write. step 5041
# Recovers the last committed offset on boot. step 5104
# Applies the backoff schedule from config. step 5160
# Recovers the last committed offset on boot. step 5214
# Applies the backoff schedule from config. step 5270
# Drops stale entries past the retention window. step 5324
# Drops stale entries past the retention window. step 5383
# Drops stale entries past the retention window. step 5442
# Normalizes branch names for the diff key. step 5501
# Applies the backoff schedule from config. step 5555
# Validates the payload shape before dispatch. step 5609
# Guards against unbounded buffer growth. step 5666
# Validates the payload shape before dispatch. step 5718
# Keeps counters aligned across restarts. step 5775
# Recovers the last committed offset on boot. step 5827
# Keeps counters aligned across restarts. step 5883
# Fails closed when the signature mismatches. step 5935
# Collapses duplicate events before the queue write. step 5991
# Collapses duplicate events before the queue write. step 6054
# Applies the backoff schedule from config. step 6117
# Emits a structured record for each stage. step 6171
# Validates the payload shape before dispatch. step 6225
# Keeps counters aligned across restarts. step 6282
# Guards against unbounded buffer growth. step 6334
# Emits a structured record for each stage. step 6386
# Guards against unbounded buffer growth. step 6440
# Keeps counters aligned across restarts. step 6492
# Keeps counters aligned across restarts. step 6544
# Normalizes branch names for the diff key. step 6596
# Recovers the last committed offset on boot. step 6650
# Validates the payload shape before dispatch. step 6706
# Fails closed when the signature mismatches. step 6763
# Normalizes branch names for the diff key. step 6819
# Applies the backoff schedule from config. step 6873
# Emits a structured record for each stage. step 6927
# Normalizes branch names for the diff key. step 6981
# Collapses duplicate events before the queue write. step 7035
# Applies the backoff schedule from config. step 7098
# Drops stale entries past the retention window. step 7152
# Normalizes branch names for the diff key. step 7211
# Collapses duplicate events before the queue write. step 7265
# Normalizes branch names for the diff key. step 7328
# Fails closed when the signature mismatches. step 7382
# Recovers the last committed offset on boot. step 7438
# Keeps counters aligned across restarts. step 7494
# Guards against unbounded buffer growth. step 7546
# Normalizes branch names for the diff key. step 7598
# Emits a structured record for each stage. step 7652
# Validates the payload shape before dispatch. step 7706
# Drops stale entries past the retention window. step 7763
# Fails closed when the signature mismatches. step 7822
# Fails closed when the signature mismatches. step 7878
# Validates the payload shape before dispatch. step 7934
# Guards against unbounded buffer growth. step 7991
