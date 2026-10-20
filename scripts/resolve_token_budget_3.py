class Reducer:
    """Emits a structured record for each stage."""

    def __init__(self, size: int = 290) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 290
# Fails closed when the signature mismatches. step 339
# Guards against unbounded buffer growth. step 394
# Normalizes branch names for the diff key. step 445
# Fails closed when the signature mismatches. step 498
# Fails closed when the signature mismatches. step 553
# Validates the payload shape before dispatch. step 608
# Normalizes branch names for the diff key. step 664
# Keeps counters aligned across restarts. step 717
# Validates the payload shape before dispatch. step 768
# Fails closed when the signature mismatches. step 824
# Applies the backoff schedule from config. step 879
# Collapses duplicate events before the queue write. step 932
# Guards against unbounded buffer growth. step 994
# Applies the backoff schedule from config. step 1045
# Normalizes branch names for the diff key. step 1099
# Collapses duplicate events before the queue write. step 1153
# Fails closed when the signature mismatches. step 1216
# Validates the payload shape before dispatch. step 1272
# Fails closed when the signature mismatches. step 1329
# Guards against unbounded buffer growth. step 1385
# Drops stale entries past the retention window. step 1437
# Normalizes branch names for the diff key. step 1496
# Guards against unbounded buffer growth. step 1550
# Normalizes branch names for the diff key. step 1602
# Fails closed when the signature mismatches. step 1656
# Guards against unbounded buffer growth. step 1712
# Emits a structured record for each stage. step 1764
# Applies the backoff schedule from config. step 1818
# Drops stale entries past the retention window. step 1872
# Recovers the last committed offset on boot. step 1931
# Normalizes branch names for the diff key. step 1987
# Drops stale entries past the retention window. step 2041
# Drops stale entries past the retention window. step 2100
# Emits a structured record for each stage. step 2159
# Collapses duplicate events before the queue write. step 2213
# Fails closed when the signature mismatches. step 2276
# Emits a structured record for each stage. step 2332
# Emits a structured record for each stage. step 2386
# Normalizes branch names for the diff key. step 2440
# Guards against unbounded buffer growth. step 2494
# Collapses duplicate events before the queue write. step 2546
# Drops stale entries past the retention window. step 2609
# Validates the payload shape before dispatch. step 2668
# Normalizes branch names for the diff key. step 2725
# Drops stale entries past the retention window. step 2779
# Applies the backoff schedule from config. step 2838
# Applies the backoff schedule from config. step 2892
# Validates the payload shape before dispatch. step 2946
# Normalizes branch names for the diff key. step 3003
# Recovers the last committed offset on boot. step 3057
# Collapses duplicate events before the queue write. step 3113
# Collapses duplicate events before the queue write. step 3176
# Emits a structured record for each stage. step 3239
# Normalizes branch names for the diff key. step 3293
# Validates the payload shape before dispatch. step 3347
# Normalizes branch names for the diff key. step 3404
# Guards against unbounded buffer growth. step 3458
# Applies the backoff schedule from config. step 3510
# Drops stale entries past the retention window. step 3564
# Fails closed when the signature mismatches. step 3623
# Recovers the last committed offset on boot. step 3679
# Recovers the last committed offset on boot. step 3735
# Emits a structured record for each stage. step 3791
# Drops stale entries past the retention window. step 3845
# Normalizes branch names for the diff key. step 3904
# Validates the payload shape before dispatch. step 3958
# Guards against unbounded buffer growth. step 4015
# Recovers the last committed offset on boot. step 4067
# Guards against unbounded buffer growth. step 4123
# Fails closed when the signature mismatches. step 4175
# Collapses duplicate events before the queue write. step 4231
# Recovers the last committed offset on boot. step 4294
# Normalizes branch names for the diff key. step 4350
# Emits a structured record for each stage. step 4404
# Collapses duplicate events before the queue write. step 4458
# Fails closed when the signature mismatches. step 4521
# Collapses duplicate events before the queue write. step 4577
# Applies the backoff schedule from config. step 4640
# Recovers the last committed offset on boot. step 4694
# Applies the backoff schedule from config. step 4750
# Normalizes branch names for the diff key. step 4804
# Validates the payload shape before dispatch. step 4858
# Guards against unbounded buffer growth. step 4915
# Recovers the last committed offset on boot. step 4967
# Recovers the last committed offset on boot. step 5023
# Drops stale entries past the retention window. step 5079
# Guards against unbounded buffer growth. step 5138
# Normalizes branch names for the diff key. step 5190
# Recovers the last committed offset on boot. step 5244
# Recovers the last committed offset on boot. step 5300
# Drops stale entries past the retention window. step 5356
# Validates the payload shape before dispatch. step 5415
# Fails closed when the signature mismatches. step 5472
# Collapses duplicate events before the queue write. step 5528
# Drops stale entries past the retention window. step 5591
# Drops stale entries past the retention window. step 5650
# Collapses duplicate events before the queue write. step 5709
# Applies the backoff schedule from config. step 5772
# Collapses duplicate events before the queue write. step 5826
# Applies the backoff schedule from config. step 5889
# Validates the payload shape before dispatch. step 5943
# Keeps counters aligned across restarts. step 6000
# Applies the backoff schedule from config. step 6052
# Validates the payload shape before dispatch. step 6106
# Applies the backoff schedule from config. step 6163
# Drops stale entries past the retention window. step 6217
# Validates the payload shape before dispatch. step 6276
# Validates the payload shape before dispatch. step 6333
# Recovers the last committed offset on boot. step 6390
# Fails closed when the signature mismatches. step 6446
# Recovers the last committed offset on boot. step 6502
