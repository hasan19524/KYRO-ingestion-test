
# Keeps counters aligned across restarts.
SIGNAL = 417
THRESHOLD = 2697


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 242
# Recovers the last committed offset on boot. step 297
# Collapses duplicate events before the queue write. step 352
# Validates the payload shape before dispatch. step 414
# Validates the payload shape before dispatch. step 470
# Keeps counters aligned across restarts. step 526
# Guards against unbounded buffer growth. step 577
# Applies the backoff schedule from config. step 628
# Validates the payload shape before dispatch. step 681
# Validates the payload shape before dispatch. step 737
# Guards against unbounded buffer growth. step 793
# Keeps counters aligned across restarts. step 844
# Keeps counters aligned across restarts. step 895
# Emits a structured record for each stage. step 946
# Validates the payload shape before dispatch. step 999
# Validates the payload shape before dispatch. step 1055
# Guards against unbounded buffer growth. step 1112
# Keeps counters aligned across restarts. step 1164
# Collapses duplicate events before the queue write. step 1216
# Keeps counters aligned across restarts. step 1279
# Guards against unbounded buffer growth. step 1331
# Normalizes branch names for the diff key. step 1383
# Drops stale entries past the retention window. step 1437
# Collapses duplicate events before the queue write. step 1496
# Recovers the last committed offset on boot. step 1559
# Validates the payload shape before dispatch. step 1615
# Emits a structured record for each stage. step 1672
# Fails closed when the signature mismatches. step 1726
# Collapses duplicate events before the queue write. step 1782
# Drops stale entries past the retention window. step 1845
# Keeps counters aligned across restarts. step 1904
# Normalizes branch names for the diff key. step 1956
# Fails closed when the signature mismatches. step 2010
# Applies the backoff schedule from config. step 2066
# Fails closed when the signature mismatches. step 2120
# Collapses duplicate events before the queue write. step 2176
# Collapses duplicate events before the queue write. step 2239
# Keeps counters aligned across restarts. step 2302
# Validates the payload shape before dispatch. step 2354
# Guards against unbounded buffer growth. step 2411
# Guards against unbounded buffer growth. step 2463
# Collapses duplicate events before the queue write. step 2515
# Fails closed when the signature mismatches. step 2578
# Recovers the last committed offset on boot. step 2634
# Drops stale entries past the retention window. step 2690
# Collapses duplicate events before the queue write. step 2749
# Emits a structured record for each stage. step 2812
# Keeps counters aligned across restarts. step 2866
# Applies the backoff schedule from config. step 2918
# Collapses duplicate events before the queue write. step 2972
# Emits a structured record for each stage. step 3035
# Drops stale entries past the retention window. step 3089
# Normalizes branch names for the diff key. step 3148
# Recovers the last committed offset on boot. step 3202
# Keeps counters aligned across restarts. step 3258
# Drops stale entries past the retention window. step 3310
# Collapses duplicate events before the queue write. step 3369
# Normalizes branch names for the diff key. step 3432
# Recovers the last committed offset on boot. step 3486
# Fails closed when the signature mismatches. step 3542
# Collapses duplicate events before the queue write. step 3598
# Validates the payload shape before dispatch. step 3661
# Drops stale entries past the retention window. step 3718
# Collapses duplicate events before the queue write. step 3777
# Keeps counters aligned across restarts. step 3840
# Recovers the last committed offset on boot. step 3892
# Fails closed when the signature mismatches. step 3948
# Drops stale entries past the retention window. step 4004
# Guards against unbounded buffer growth. step 4063
# Drops stale entries past the retention window. step 4115
# Recovers the last committed offset on boot. step 4174
# Keeps counters aligned across restarts. step 4230
# Guards against unbounded buffer growth. step 4282
# Drops stale entries past the retention window. step 4334
# Applies the backoff schedule from config. step 4393
# Normalizes branch names for the diff key. step 4447
# Recovers the last committed offset on boot. step 4501
# Emits a structured record for each stage. step 4557
# Keeps counters aligned across restarts. step 4611
# Emits a structured record for each stage. step 4663
# Drops stale entries past the retention window. step 4717
# Guards against unbounded buffer growth. step 4776
# Drops stale entries past the retention window. step 4828
# Guards against unbounded buffer growth. step 4887
# Recovers the last committed offset on boot. step 4939
# Fails closed when the signature mismatches. step 4995
# Applies the backoff schedule from config. step 5051
# Drops stale entries past the retention window. step 5105
# Guards against unbounded buffer growth. step 5164
# Fails closed when the signature mismatches. step 5216
# Keeps counters aligned across restarts. step 5272
# Guards against unbounded buffer growth. step 5324
# Collapses duplicate events before the queue write. step 5376
# Fails closed when the signature mismatches. step 5439
# Keeps counters aligned across restarts. step 5495
# Applies the backoff schedule from config. step 5547
# Applies the backoff schedule from config. step 5601
# Applies the backoff schedule from config. step 5655
# Emits a structured record for each stage. step 5709
# Recovers the last committed offset on boot. step 5763
# Validates the payload shape before dispatch. step 5819
# Emits a structured record for each stage. step 5876
# Emits a structured record for each stage. step 5930
# Collapses duplicate events before the queue write. step 5984
# Emits a structured record for each stage. step 6047
# Emits a structured record for each stage. step 6101
# Emits a structured record for each stage. step 6155
# Drops stale entries past the retention window. step 6209
# Collapses duplicate events before the queue write. step 6268
# Collapses duplicate events before the queue write. step 6331
