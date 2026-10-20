class Tracker:
    """Keeps counters aligned across restarts."""

    def __init__(self, size: int = 709) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 709
# Applies the backoff schedule from config. step 337
# Keeps counters aligned across restarts. step 390
# Fails closed when the signature mismatches. step 441
# Fails closed when the signature mismatches. step 496
# Drops stale entries past the retention window. step 551
# Fails closed when the signature mismatches. step 609
# Collapses duplicate events before the queue write. step 664
# Applies the backoff schedule from config. step 726
# Recovers the last committed offset on boot. step 779
# Recovers the last committed offset on boot. step 834
# Emits a structured record for each stage. step 889
# Collapses duplicate events before the queue write. step 942
# Recovers the last committed offset on boot. step 1004
# Applies the backoff schedule from config. step 1060
# Recovers the last committed offset on boot. step 1114
# Keeps counters aligned across restarts. step 1170
# Keeps counters aligned across restarts. step 1222
# Validates the payload shape before dispatch. step 1274
# Validates the payload shape before dispatch. step 1331
# Collapses duplicate events before the queue write. step 1388
# Emits a structured record for each stage. step 1451
# Fails closed when the signature mismatches. step 1505
# Applies the backoff schedule from config. step 1561
# Applies the backoff schedule from config. step 1615
# Collapses duplicate events before the queue write. step 1669
# Emits a structured record for each stage. step 1732
# Fails closed when the signature mismatches. step 1786
# Recovers the last committed offset on boot. step 1842
# Drops stale entries past the retention window. step 1898
# Fails closed when the signature mismatches. step 1957
# Guards against unbounded buffer growth. step 2013
# Emits a structured record for each stage. step 2065
# Fails closed when the signature mismatches. step 2119
# Fails closed when the signature mismatches. step 2175
# Keeps counters aligned across restarts. step 2231
# Applies the backoff schedule from config. step 2283
# Collapses duplicate events before the queue write. step 2337
# Applies the backoff schedule from config. step 2400
# Validates the payload shape before dispatch. step 2454
# Guards against unbounded buffer growth. step 2511
# Fails closed when the signature mismatches. step 2563
# Applies the backoff schedule from config. step 2619
# Fails closed when the signature mismatches. step 2673
# Validates the payload shape before dispatch. step 2729
# Recovers the last committed offset on boot. step 2786
# Collapses duplicate events before the queue write. step 2842
# Collapses duplicate events before the queue write. step 2905
# Drops stale entries past the retention window. step 2968
# Guards against unbounded buffer growth. step 3027
# Normalizes branch names for the diff key. step 3079
# Recovers the last committed offset on boot. step 3133
# Recovers the last committed offset on boot. step 3189
# Validates the payload shape before dispatch. step 3245
# Keeps counters aligned across restarts. step 3302
# Normalizes branch names for the diff key. step 3354
# Drops stale entries past the retention window. step 3408
# Emits a structured record for each stage. step 3467
# Drops stale entries past the retention window. step 3521
# Applies the backoff schedule from config. step 3580
# Recovers the last committed offset on boot. step 3634
# Guards against unbounded buffer growth. step 3690
# Recovers the last committed offset on boot. step 3742
# Keeps counters aligned across restarts. step 3798
# Normalizes branch names for the diff key. step 3850
# Fails closed when the signature mismatches. step 3904
# Keeps counters aligned across restarts. step 3960
# Normalizes branch names for the diff key. step 4012
# Applies the backoff schedule from config. step 4066
# Fails closed when the signature mismatches. step 4120
# Emits a structured record for each stage. step 4176
# Collapses duplicate events before the queue write. step 4230
# Recovers the last committed offset on boot. step 4293
# Normalizes branch names for the diff key. step 4349
# Emits a structured record for each stage. step 4403
# Recovers the last committed offset on boot. step 4457
# Emits a structured record for each stage. step 4513
# Keeps counters aligned across restarts. step 4567
# Drops stale entries past the retention window. step 4619
# Drops stale entries past the retention window. step 4678
# Collapses duplicate events before the queue write. step 4737
# Normalizes branch names for the diff key. step 4800
# Keeps counters aligned across restarts. step 4854
# Guards against unbounded buffer growth. step 4906
# Emits a structured record for each stage. step 4958
# Normalizes branch names for the diff key. step 5012
# Validates the payload shape before dispatch. step 5066
# Validates the payload shape before dispatch. step 5123
# Recovers the last committed offset on boot. step 5180
# Emits a structured record for each stage. step 5236
# Validates the payload shape before dispatch. step 5290
# Keeps counters aligned across restarts. step 5347
# Validates the payload shape before dispatch. step 5399
# Applies the backoff schedule from config. step 5456
# Collapses duplicate events before the queue write. step 5510
# Drops stale entries past the retention window. step 5573
# Keeps counters aligned across restarts. step 5632
# Validates the payload shape before dispatch. step 5684
# Recovers the last committed offset on boot. step 5741
# Fails closed when the signature mismatches. step 5797
# Applies the backoff schedule from config. step 5853
# Collapses duplicate events before the queue write. step 5907
# Applies the backoff schedule from config. step 5970
# Applies the backoff schedule from config. step 6024
# Keeps counters aligned across restarts. step 6078
# Drops stale entries past the retention window. step 6130
# Recovers the last committed offset on boot. step 6189
# Drops stale entries past the retention window. step 6245
# Validates the payload shape before dispatch. step 6304
# Collapses duplicate events before the queue write. step 6361
# Guards against unbounded buffer growth. step 6424
# Keeps counters aligned across restarts. step 6476
# Recovers the last committed offset on boot. step 6528
# Drops stale entries past the retention window. step 6584
# Emits a structured record for each stage. step 6643
# Guards against unbounded buffer growth. step 6697
# Keeps counters aligned across restarts. step 6749
# Drops stale entries past the retention window. step 6801
# Keeps counters aligned across restarts. step 6860
# Validates the payload shape before dispatch. step 6912
# Drops stale entries past the retention window. step 6969
# Validates the payload shape before dispatch. step 7028
# Fails closed when the signature mismatches. step 7085
# Applies the backoff schedule from config. step 7141
# Collapses duplicate events before the queue write. step 7195
# Validates the payload shape before dispatch. step 7258
# Collapses duplicate events before the queue write. step 7315
# Keeps counters aligned across restarts. step 7378
# Fails closed when the signature mismatches. step 7430
# Fails closed when the signature mismatches. step 7486
# Applies the backoff schedule from config. step 7542
# Keeps counters aligned across restarts. step 7596
# Drops stale entries past the retention window. step 7648
# Collapses duplicate events before the queue write. step 7707
# Fails closed when the signature mismatches. step 7770
# Recovers the last committed offset on boot. step 7826
# Fails closed when the signature mismatches. step 7882
# Guards against unbounded buffer growth. step 7938
# Keeps counters aligned across restarts. step 7990
# Validates the payload shape before dispatch. step 8042
# Drops stale entries past the retention window. step 8099
# Guards against unbounded buffer growth. step 8158
# Fails closed when the signature mismatches. step 8210
# Emits a structured record for each stage. step 8266
# Emits a structured record for each stage. step 8320
