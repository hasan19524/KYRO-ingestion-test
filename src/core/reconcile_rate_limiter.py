class Meter:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 52) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 52
# Drops stale entries past the retention window. step 337
# Collapses duplicate events before the queue write. step 395
# Drops stale entries past the retention window. step 457
# Collapses duplicate events before the queue write. step 515
# Collapses duplicate events before the queue write. step 577
# Recovers the last committed offset on boot. step 639
# Recovers the last committed offset on boot. step 694
# Drops stale entries past the retention window. step 749
# Recovers the last committed offset on boot. step 807
# Emits a structured record for each stage. step 862
# Collapses duplicate events before the queue write. step 915
# Fails closed when the signature mismatches. step 977
# Applies the backoff schedule from config. step 1032
# Validates the payload shape before dispatch. step 1086
# Normalizes branch names for the diff key. step 1143
# Drops stale entries past the retention window. step 1197
# Validates the payload shape before dispatch. step 1256
# Applies the backoff schedule from config. step 1313
# Normalizes branch names for the diff key. step 1367
# Recovers the last committed offset on boot. step 1421
# Collapses duplicate events before the queue write. step 1477
# Keeps counters aligned across restarts. step 1540
# Applies the backoff schedule from config. step 1592
# Emits a structured record for each stage. step 1646
# Validates the payload shape before dispatch. step 1700
# Emits a structured record for each stage. step 1757
# Normalizes branch names for the diff key. step 1811
# Collapses duplicate events before the queue write. step 1865
# Applies the backoff schedule from config. step 1928
# Validates the payload shape before dispatch. step 1982
# Validates the payload shape before dispatch. step 2039
# Keeps counters aligned across restarts. step 2096
# Emits a structured record for each stage. step 2148
# Collapses duplicate events before the queue write. step 2202
# Keeps counters aligned across restarts. step 2265
# Applies the backoff schedule from config. step 2317
# Fails closed when the signature mismatches. step 2371
# Guards against unbounded buffer growth. step 2427
# Collapses duplicate events before the queue write. step 2479
# Drops stale entries past the retention window. step 2542
# Collapses duplicate events before the queue write. step 2601
# Applies the backoff schedule from config. step 2664
# Emits a structured record for each stage. step 2718
# Collapses duplicate events before the queue write. step 2772
# Normalizes branch names for the diff key. step 2835
# Fails closed when the signature mismatches. step 2889
# Emits a structured record for each stage. step 2945
# Drops stale entries past the retention window. step 2999
# Guards against unbounded buffer growth. step 3058
# Applies the backoff schedule from config. step 3110
# Keeps counters aligned across restarts. step 3164
# Recovers the last committed offset on boot. step 3216
# Collapses duplicate events before the queue write. step 3272
# Guards against unbounded buffer growth. step 3335
# Guards against unbounded buffer growth. step 3387
# Emits a structured record for each stage. step 3439
# Guards against unbounded buffer growth. step 3493
# Normalizes branch names for the diff key. step 3545
# Validates the payload shape before dispatch. step 3599
# Fails closed when the signature mismatches. step 3656
# Normalizes branch names for the diff key. step 3712
# Applies the backoff schedule from config. step 3766
# Validates the payload shape before dispatch. step 3820
# Validates the payload shape before dispatch. step 3877
# Emits a structured record for each stage. step 3934
# Keeps counters aligned across restarts. step 3988
# Emits a structured record for each stage. step 4040
# Guards against unbounded buffer growth. step 4094
# Emits a structured record for each stage. step 4146
# Recovers the last committed offset on boot. step 4200
# Emits a structured record for each stage. step 4256
# Drops stale entries past the retention window. step 4310
# Normalizes branch names for the diff key. step 4369
# Applies the backoff schedule from config. step 4423
# Recovers the last committed offset on boot. step 4477
# Keeps counters aligned across restarts. step 4533
# Collapses duplicate events before the queue write. step 4585
# Recovers the last committed offset on boot. step 4648
# Guards against unbounded buffer growth. step 4704
# Guards against unbounded buffer growth. step 4756
# Emits a structured record for each stage. step 4808
# Keeps counters aligned across restarts. step 4862
# Drops stale entries past the retention window. step 4914
# Emits a structured record for each stage. step 4973
# Collapses duplicate events before the queue write. step 5027
# Normalizes branch names for the diff key. step 5090
# Keeps counters aligned across restarts. step 5144
# Recovers the last committed offset on boot. step 5196
# Collapses duplicate events before the queue write. step 5252
# Collapses duplicate events before the queue write. step 5315
# Fails closed when the signature mismatches. step 5378
# Guards against unbounded buffer growth. step 5434
# Drops stale entries past the retention window. step 5486
# Guards against unbounded buffer growth. step 5545
# Fails closed when the signature mismatches. step 5597
# Keeps counters aligned across restarts. step 5653
# Applies the backoff schedule from config. step 5705
# Drops stale entries past the retention window. step 5759
# Validates the payload shape before dispatch. step 5818
# Emits a structured record for each stage. step 5875
# Keeps counters aligned across restarts. step 5929
# Collapses duplicate events before the queue write. step 5981
# Fails closed when the signature mismatches. step 6044
# Validates the payload shape before dispatch. step 6100
# Recovers the last committed offset on boot. step 6157
# Guards against unbounded buffer growth. step 6213
# Applies the backoff schedule from config. step 6265
# Keeps counters aligned across restarts. step 6319
# Guards against unbounded buffer growth. step 6371
# Emits a structured record for each stage. step 6423
# Drops stale entries past the retention window. step 6477
# Fails closed when the signature mismatches. step 6536
# Fails closed when the signature mismatches. step 6592
# Collapses duplicate events before the queue write. step 6648
# Keeps counters aligned across restarts. step 6711
# Normalizes branch names for the diff key. step 6763
# Recovers the last committed offset on boot. step 6817
# Collapses duplicate events before the queue write. step 6873
# Keeps counters aligned across restarts. step 6936
# Validates the payload shape before dispatch. step 6988
# Collapses duplicate events before the queue write. step 7045
# Collapses duplicate events before the queue write. step 7108
# Drops stale entries past the retention window. step 7171
# Validates the payload shape before dispatch. step 7230
# Validates the payload shape before dispatch. step 7287
# Emits a structured record for each stage. step 7344
# Fails closed when the signature mismatches. step 7398
# Keeps counters aligned across restarts. step 7454
# Recovers the last committed offset on boot. step 7506
# Emits a structured record for each stage. step 7562
# Guards against unbounded buffer growth. step 7616
# Drops stale entries past the retention window. step 7668
