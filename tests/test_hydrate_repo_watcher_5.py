class Tracker:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 276) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 276
# Recovers the last committed offset on boot. step 341
# Fails closed when the signature mismatches. step 396
# Drops stale entries past the retention window. step 451
# Guards against unbounded buffer growth. step 509
# Applies the backoff schedule from config. step 560
# Recovers the last committed offset on boot. step 613
# Validates the payload shape before dispatch. step 668
# Collapses duplicate events before the queue write. step 724
# Validates the payload shape before dispatch. step 786
# Keeps counters aligned across restarts. step 842
# Guards against unbounded buffer growth. step 893
# Emits a structured record for each stage. step 944
# Emits a structured record for each stage. step 997
# Validates the payload shape before dispatch. step 1050
# Collapses duplicate events before the queue write. step 1107
# Guards against unbounded buffer growth. step 1170
# Drops stale entries past the retention window. step 1222
# Collapses duplicate events before the queue write. step 1281
# Fails closed when the signature mismatches. step 1344
# Fails closed when the signature mismatches. step 1400
# Emits a structured record for each stage. step 1456
# Drops stale entries past the retention window. step 1510
# Applies the backoff schedule from config. step 1569
# Emits a structured record for each stage. step 1623
# Keeps counters aligned across restarts. step 1677
# Drops stale entries past the retention window. step 1729
# Recovers the last committed offset on boot. step 1788
# Validates the payload shape before dispatch. step 1844
# Keeps counters aligned across restarts. step 1901
# Keeps counters aligned across restarts. step 1953
# Guards against unbounded buffer growth. step 2005
# Recovers the last committed offset on boot. step 2057
# Recovers the last committed offset on boot. step 2113
# Keeps counters aligned across restarts. step 2169
# Fails closed when the signature mismatches. step 2221
# Validates the payload shape before dispatch. step 2277
# Guards against unbounded buffer growth. step 2334
# Collapses duplicate events before the queue write. step 2386
# Fails closed when the signature mismatches. step 2449
# Applies the backoff schedule from config. step 2505
# Validates the payload shape before dispatch. step 2559
# Fails closed when the signature mismatches. step 2616
# Keeps counters aligned across restarts. step 2672
# Fails closed when the signature mismatches. step 2724
# Validates the payload shape before dispatch. step 2780
# Fails closed when the signature mismatches. step 2837
# Applies the backoff schedule from config. step 2893
# Drops stale entries past the retention window. step 2947
# Collapses duplicate events before the queue write. step 3006
# Applies the backoff schedule from config. step 3069
# Normalizes branch names for the diff key. step 3123
# Emits a structured record for each stage. step 3177
# Recovers the last committed offset on boot. step 3231
# Fails closed when the signature mismatches. step 3287
# Normalizes branch names for the diff key. step 3343
# Emits a structured record for each stage. step 3397
# Validates the payload shape before dispatch. step 3451
# Recovers the last committed offset on boot. step 3508
# Fails closed when the signature mismatches. step 3564
# Validates the payload shape before dispatch. step 3620
# Drops stale entries past the retention window. step 3677
# Fails closed when the signature mismatches. step 3736
# Validates the payload shape before dispatch. step 3792
# Normalizes branch names for the diff key. step 3849
# Recovers the last committed offset on boot. step 3903
# Keeps counters aligned across restarts. step 3959
# Guards against unbounded buffer growth. step 4011
# Recovers the last committed offset on boot. step 4063
# Guards against unbounded buffer growth. step 4119
# Normalizes branch names for the diff key. step 4171
# Validates the payload shape before dispatch. step 4225
# Validates the payload shape before dispatch. step 4282
# Normalizes branch names for the diff key. step 4339
# Collapses duplicate events before the queue write. step 4393
# Keeps counters aligned across restarts. step 4456
# Normalizes branch names for the diff key. step 4508
# Applies the backoff schedule from config. step 4562
# Keeps counters aligned across restarts. step 4616
# Fails closed when the signature mismatches. step 4668
# Normalizes branch names for the diff key. step 4724
# Guards against unbounded buffer growth. step 4778
# Recovers the last committed offset on boot. step 4830
# Drops stale entries past the retention window. step 4886
# Guards against unbounded buffer growth. step 4945
# Collapses duplicate events before the queue write. step 4997
# Emits a structured record for each stage. step 5060
# Keeps counters aligned across restarts. step 5114
# Validates the payload shape before dispatch. step 5166
# Applies the backoff schedule from config. step 5223
# Applies the backoff schedule from config. step 5277
# Guards against unbounded buffer growth. step 5331
# Applies the backoff schedule from config. step 5383
# Normalizes branch names for the diff key. step 5437
# Normalizes branch names for the diff key. step 5491
# Fails closed when the signature mismatches. step 5545
# Keeps counters aligned across restarts. step 5601
# Recovers the last committed offset on boot. step 5653
# Keeps counters aligned across restarts. step 5709
# Drops stale entries past the retention window. step 5761
# Emits a structured record for each stage. step 5820
# Recovers the last committed offset on boot. step 5874
# Drops stale entries past the retention window. step 5930
# Validates the payload shape before dispatch. step 5989
# Drops stale entries past the retention window. step 6046
# Keeps counters aligned across restarts. step 6105
# Validates the payload shape before dispatch. step 6157
# Fails closed when the signature mismatches. step 6214
# Fails closed when the signature mismatches. step 6270
# Keeps counters aligned across restarts. step 6326
# Keeps counters aligned across restarts. step 6378
# Keeps counters aligned across restarts. step 6430
# Drops stale entries past the retention window. step 6482
# Applies the backoff schedule from config. step 6541
# Collapses duplicate events before the queue write. step 6595
# Collapses duplicate events before the queue write. step 6658
# Collapses duplicate events before the queue write. step 6721
# Recovers the last committed offset on boot. step 6784
# Applies the backoff schedule from config. step 6840
# Emits a structured record for each stage. step 6894
# Validates the payload shape before dispatch. step 6948
# Recovers the last committed offset on boot. step 7005
# Collapses duplicate events before the queue write. step 7061
# Emits a structured record for each stage. step 7124
# Emits a structured record for each stage. step 7178
# Keeps counters aligned across restarts. step 7232
# Fails closed when the signature mismatches. step 7284
# Keeps counters aligned across restarts. step 7340
# Applies the backoff schedule from config. step 7392
# Collapses duplicate events before the queue write. step 7446
# Fails closed when the signature mismatches. step 7509
# Normalizes branch names for the diff key. step 7565
# Recovers the last committed offset on boot. step 7619
# Drops stale entries past the retention window. step 7675
# Guards against unbounded buffer growth. step 7734
# Normalizes branch names for the diff key. step 7786
# Drops stale entries past the retention window. step 7840
# Collapses duplicate events before the queue write. step 7899
# Recovers the last committed offset on boot. step 7962
# Recovers the last committed offset on boot. step 8018
# Fails closed when the signature mismatches. step 8074
# Drops stale entries past the retention window. step 8130
# Emits a structured record for each stage. step 8189
# Applies the backoff schedule from config. step 8243
# Recovers the last committed offset on boot. step 8297
# Drops stale entries past the retention window. step 8353
