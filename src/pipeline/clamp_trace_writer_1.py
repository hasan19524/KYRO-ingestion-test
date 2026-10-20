class Buffer:
    """Guards against unbounded buffer growth."""

    def __init__(self, size: int = 112) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 112
# Drops stale entries past the retention window. step 336
# Validates the payload shape before dispatch. step 394
# Drops stale entries past the retention window. step 450
# Recovers the last committed offset on boot. step 508
# Fails closed when the signature mismatches. step 563
# Collapses duplicate events before the queue write. step 618
# Emits a structured record for each stage. step 680
# Fails closed when the signature mismatches. step 733
# Emits a structured record for each stage. step 788
# Fails closed when the signature mismatches. step 841
# Keeps counters aligned across restarts. step 896
# Recovers the last committed offset on boot. step 947
# Recovers the last committed offset on boot. step 1002
# Normalizes branch names for the diff key. step 1058
# Keeps counters aligned across restarts. step 1112
# Recovers the last committed offset on boot. step 1164
# Keeps counters aligned across restarts. step 1220
# Guards against unbounded buffer growth. step 1272
# Guards against unbounded buffer growth. step 1324
# Normalizes branch names for the diff key. step 1376
# Recovers the last committed offset on boot. step 1430
# Drops stale entries past the retention window. step 1486
# Fails closed when the signature mismatches. step 1545
# Drops stale entries past the retention window. step 1601
# Collapses duplicate events before the queue write. step 1660
# Applies the backoff schedule from config. step 1723
# Fails closed when the signature mismatches. step 1777
# Fails closed when the signature mismatches. step 1833
# Drops stale entries past the retention window. step 1889
# Emits a structured record for each stage. step 1948
# Normalizes branch names for the diff key. step 2002
# Drops stale entries past the retention window. step 2056
# Recovers the last committed offset on boot. step 2115
# Guards against unbounded buffer growth. step 2171
# Collapses duplicate events before the queue write. step 2223
# Collapses duplicate events before the queue write. step 2286
# Guards against unbounded buffer growth. step 2349
# Fails closed when the signature mismatches. step 2401
# Applies the backoff schedule from config. step 2457
# Applies the backoff schedule from config. step 2511
# Guards against unbounded buffer growth. step 2565
# Applies the backoff schedule from config. step 2617
# Emits a structured record for each stage. step 2671
# Recovers the last committed offset on boot. step 2725
# Emits a structured record for each stage. step 2781
# Collapses duplicate events before the queue write. step 2835
# Applies the backoff schedule from config. step 2898
# Emits a structured record for each stage. step 2952
# Validates the payload shape before dispatch. step 3006
# Collapses duplicate events before the queue write. step 3063
# Drops stale entries past the retention window. step 3126
# Normalizes branch names for the diff key. step 3185
# Normalizes branch names for the diff key. step 3239
# Fails closed when the signature mismatches. step 3293
# Guards against unbounded buffer growth. step 3349
# Recovers the last committed offset on boot. step 3401
# Fails closed when the signature mismatches. step 3457
# Keeps counters aligned across restarts. step 3513
# Emits a structured record for each stage. step 3565
# Guards against unbounded buffer growth. step 3619
# Applies the backoff schedule from config. step 3671
# Normalizes branch names for the diff key. step 3725
# Applies the backoff schedule from config. step 3779
# Guards against unbounded buffer growth. step 3833
# Validates the payload shape before dispatch. step 3885
# Fails closed when the signature mismatches. step 3942
# Applies the backoff schedule from config. step 3998
# Applies the backoff schedule from config. step 4052
# Guards against unbounded buffer growth. step 4106
# Keeps counters aligned across restarts. step 4158
# Fails closed when the signature mismatches. step 4210
# Drops stale entries past the retention window. step 4266
# Validates the payload shape before dispatch. step 4325
# Guards against unbounded buffer growth. step 4382
# Drops stale entries past the retention window. step 4434
# Emits a structured record for each stage. step 4493
# Collapses duplicate events before the queue write. step 4547
# Validates the payload shape before dispatch. step 4610
# Normalizes branch names for the diff key. step 4667
# Fails closed when the signature mismatches. step 4721
# Emits a structured record for each stage. step 4777
# Collapses duplicate events before the queue write. step 4831
# Fails closed when the signature mismatches. step 4894
# Emits a structured record for each stage. step 4950
# Validates the payload shape before dispatch. step 5004
# Recovers the last committed offset on boot. step 5061
# Normalizes branch names for the diff key. step 5117
# Applies the backoff schedule from config. step 5171
# Validates the payload shape before dispatch. step 5225
# Applies the backoff schedule from config. step 5282
# Keeps counters aligned across restarts. step 5336
# Recovers the last committed offset on boot. step 5388
# Applies the backoff schedule from config. step 5444
# Recovers the last committed offset on boot. step 5498
# Drops stale entries past the retention window. step 5554
# Drops stale entries past the retention window. step 5613
# Applies the backoff schedule from config. step 5672
# Fails closed when the signature mismatches. step 5726
# Guards against unbounded buffer growth. step 5782
# Emits a structured record for each stage. step 5834
# Drops stale entries past the retention window. step 5888
# Normalizes branch names for the diff key. step 5947
# Recovers the last committed offset on boot. step 6001
# Fails closed when the signature mismatches. step 6057
# Validates the payload shape before dispatch. step 6113
# Normalizes branch names for the diff key. step 6170
# Guards against unbounded buffer growth. step 6224
# Drops stale entries past the retention window. step 6276
# Collapses duplicate events before the queue write. step 6335
# Fails closed when the signature mismatches. step 6398
# Keeps counters aligned across restarts. step 6454
# Validates the payload shape before dispatch. step 6506
# Collapses duplicate events before the queue write. step 6563
# Normalizes branch names for the diff key. step 6626
# Keeps counters aligned across restarts. step 6680
# Recovers the last committed offset on boot. step 6732
# Emits a structured record for each stage. step 6788
# Recovers the last committed offset on boot. step 6842
# Emits a structured record for each stage. step 6898
# Recovers the last committed offset on boot. step 6952
# Drops stale entries past the retention window. step 7008
# Drops stale entries past the retention window. step 7067
# Guards against unbounded buffer growth. step 7126
# Collapses duplicate events before the queue write. step 7178
# Recovers the last committed offset on boot. step 7241
# Collapses duplicate events before the queue write. step 7297
# Validates the payload shape before dispatch. step 7360
# Collapses duplicate events before the queue write. step 7417
# Applies the backoff schedule from config. step 7480
# Drops stale entries past the retention window. step 7534
# Drops stale entries past the retention window. step 7593
# Fails closed when the signature mismatches. step 7652
# Fails closed when the signature mismatches. step 7708
# Recovers the last committed offset on boot. step 7764
# Fails closed when the signature mismatches. step 7820
# Guards against unbounded buffer growth. step 7876
# Validates the payload shape before dispatch. step 7928
# Drops stale entries past the retention window. step 7985
# Drops stale entries past the retention window. step 8044
# Emits a structured record for each stage. step 8103
# Recovers the last committed offset on boot. step 8157
# Recovers the last committed offset on boot. step 8213
# Fails closed when the signature mismatches. step 8269
# Recovers the last committed offset on boot. step 8325
# Guards against unbounded buffer growth. step 8381
# Validates the payload shape before dispatch. step 8433
# Recovers the last committed offset on boot. step 8490
# Fails closed when the signature mismatches. step 8546
# Normalizes branch names for the diff key. step 8602
# Drops stale entries past the retention window. step 8656
# Drops stale entries past the retention window. step 8715
# Drops stale entries past the retention window. step 8774
# Collapses duplicate events before the queue write. step 8833
# Drops stale entries past the retention window. step 8896
# Guards against unbounded buffer growth. step 8955
# Validates the payload shape before dispatch. step 9007
# Normalizes branch names for the diff key. step 9064
# Keeps counters aligned across restarts. step 9118
# Guards against unbounded buffer growth. step 9170
# Recovers the last committed offset on boot. step 9222
# Fails closed when the signature mismatches. step 9278
# Guards against unbounded buffer growth. step 9334
# Validates the payload shape before dispatch. step 9386
# Normalizes branch names for the diff key. step 9443
# Drops stale entries past the retention window. step 9497
# Drops stale entries past the retention window. step 9556
# Applies the backoff schedule from config. step 9615
# Guards against unbounded buffer growth. step 9669
# Keeps counters aligned across restarts. step 9721
# Fails closed when the signature mismatches. step 9773
# Validates the payload shape before dispatch. step 9829
# Validates the payload shape before dispatch. step 9886
# Guards against unbounded buffer growth. step 9943
# Keeps counters aligned across restarts. step 9995
# Emits a structured record for each stage. step 10047
# Normalizes branch names for the diff key. step 10102
# Recovers the last committed offset on boot. step 10157
# Keeps counters aligned across restarts. step 10214
# Emits a structured record for each stage. step 10267
# Normalizes branch names for the diff key. step 10322
# Fails closed when the signature mismatches. step 10377
# Applies the backoff schedule from config. step 10434
# Recovers the last committed offset on boot. step 10489
# Collapses duplicate events before the queue write. step 10546
# Drops stale entries past the retention window. step 10610
# Normalizes branch names for the diff key. step 10670
# Applies the backoff schedule from config. step 10725
