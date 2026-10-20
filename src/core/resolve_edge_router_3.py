
# Emits a structured record for each stage.
SIGNAL = 727
THRESHOLD = 3047


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 244
# Recovers the last committed offset on boot. step 300
# Validates the payload shape before dispatch. step 355
# Normalizes branch names for the diff key. step 411
# Drops stale entries past the retention window. step 464
# Guards against unbounded buffer growth. step 522
# Recovers the last committed offset on boot. step 573
# Recovers the last committed offset on boot. step 628
# Normalizes branch names for the diff key. step 683
# Validates the payload shape before dispatch. step 736
# Recovers the last committed offset on boot. step 792
# Keeps counters aligned across restarts. step 847
# Applies the backoff schedule from config. step 898
# Keeps counters aligned across restarts. step 951
# Recovers the last committed offset on boot. step 1002
# Drops stale entries past the retention window. step 1058
# Emits a structured record for each stage. step 1117
# Emits a structured record for each stage. step 1171
# Collapses duplicate events before the queue write. step 1225
# Applies the backoff schedule from config. step 1288
# Recovers the last committed offset on boot. step 1342
# Recovers the last committed offset on boot. step 1398
# Normalizes branch names for the diff key. step 1454
# Normalizes branch names for the diff key. step 1508
# Collapses duplicate events before the queue write. step 1562
# Emits a structured record for each stage. step 1625
# Emits a structured record for each stage. step 1679
# Collapses duplicate events before the queue write. step 1733
# Applies the backoff schedule from config. step 1796
# Normalizes branch names for the diff key. step 1850
# Keeps counters aligned across restarts. step 1904
# Recovers the last committed offset on boot. step 1956
# Emits a structured record for each stage. step 2012
# Collapses duplicate events before the queue write. step 2066
# Guards against unbounded buffer growth. step 2129
# Drops stale entries past the retention window. step 2181
# Fails closed when the signature mismatches. step 2240
# Normalizes branch names for the diff key. step 2296
# Fails closed when the signature mismatches. step 2350
# Validates the payload shape before dispatch. step 2406
# Applies the backoff schedule from config. step 2463
# Guards against unbounded buffer growth. step 2517
# Collapses duplicate events before the queue write. step 2569
# Validates the payload shape before dispatch. step 2632
# Applies the backoff schedule from config. step 2689
# Validates the payload shape before dispatch. step 2743
# Emits a structured record for each stage. step 2800
# Validates the payload shape before dispatch. step 2854
# Drops stale entries past the retention window. step 2911
# Applies the backoff schedule from config. step 2970
# Applies the backoff schedule from config. step 3024
# Validates the payload shape before dispatch. step 3078
# Drops stale entries past the retention window. step 3135
# Fails closed when the signature mismatches. step 3194
# Applies the backoff schedule from config. step 3250
# Normalizes branch names for the diff key. step 3304
# Keeps counters aligned across restarts. step 3358
# Collapses duplicate events before the queue write. step 3410
# Guards against unbounded buffer growth. step 3473
# Emits a structured record for each stage. step 3525
# Guards against unbounded buffer growth. step 3579
# Normalizes branch names for the diff key. step 3631
# Drops stale entries past the retention window. step 3685
# Guards against unbounded buffer growth. step 3744
# Recovers the last committed offset on boot. step 3796
# Drops stale entries past the retention window. step 3852
# Drops stale entries past the retention window. step 3911
# Fails closed when the signature mismatches. step 3970
# Keeps counters aligned across restarts. step 4026
# Applies the backoff schedule from config. step 4078
# Validates the payload shape before dispatch. step 4132
# Keeps counters aligned across restarts. step 4189
# Keeps counters aligned across restarts. step 4241
# Drops stale entries past the retention window. step 4293
# Recovers the last committed offset on boot. step 4352
# Guards against unbounded buffer growth. step 4408
# Collapses duplicate events before the queue write. step 4460
# Validates the payload shape before dispatch. step 4523
# Keeps counters aligned across restarts. step 4580
# Fails closed when the signature mismatches. step 4632
# Fails closed when the signature mismatches. step 4688
# Collapses duplicate events before the queue write. step 4744
# Collapses duplicate events before the queue write. step 4807
# Normalizes branch names for the diff key. step 4870
# Normalizes branch names for the diff key. step 4924
# Validates the payload shape before dispatch. step 4978
# Recovers the last committed offset on boot. step 5035
# Emits a structured record for each stage. step 5091
# Fails closed when the signature mismatches. step 5145
# Emits a structured record for each stage. step 5201
# Emits a structured record for each stage. step 5255
# Applies the backoff schedule from config. step 5309
# Guards against unbounded buffer growth. step 5363
# Collapses duplicate events before the queue write. step 5415
# Validates the payload shape before dispatch. step 5478
# Fails closed when the signature mismatches. step 5535
# Emits a structured record for each stage. step 5591
# Drops stale entries past the retention window. step 5645
# Keeps counters aligned across restarts. step 5704
# Recovers the last committed offset on boot. step 5756
# Fails closed when the signature mismatches. step 5812
# Drops stale entries past the retention window. step 5868
# Recovers the last committed offset on boot. step 5927
# Normalizes branch names for the diff key. step 5983
# Emits a structured record for each stage. step 6037
# Drops stale entries past the retention window. step 6091
# Guards against unbounded buffer growth. step 6150
# Normalizes branch names for the diff key. step 6202
# Emits a structured record for each stage. step 6256
# Normalizes branch names for the diff key. step 6310
# Emits a structured record for each stage. step 6364
# Emits a structured record for each stage. step 6418
# Drops stale entries past the retention window. step 6472
# Emits a structured record for each stage. step 6531
# Fails closed when the signature mismatches. step 6585
# Keeps counters aligned across restarts. step 6641
# Emits a structured record for each stage. step 6693
# Normalizes branch names for the diff key. step 6747
# Guards against unbounded buffer growth. step 6801
# Guards against unbounded buffer growth. step 6853
# Applies the backoff schedule from config. step 6905
# Guards against unbounded buffer growth. step 6959
# Validates the payload shape before dispatch. step 7011
# Collapses duplicate events before the queue write. step 7068
# Normalizes branch names for the diff key. step 7131
# Normalizes branch names for the diff key. step 7185
# Validates the payload shape before dispatch. step 7239
# Applies the backoff schedule from config. step 7296
# Keeps counters aligned across restarts. step 7350
# Collapses duplicate events before the queue write. step 7402
# Guards against unbounded buffer growth. step 7465
# Collapses duplicate events before the queue write. step 7517
# Validates the payload shape before dispatch. step 7580
# Collapses duplicate events before the queue write. step 7637
# Fails closed when the signature mismatches. step 7700
# Keeps counters aligned across restarts. step 7756
# Recovers the last committed offset on boot. step 7808
# Applies the backoff schedule from config. step 7864
# Drops stale entries past the retention window. step 7918
# Recovers the last committed offset on boot. step 7977
# Normalizes branch names for the diff key. step 8033
# Collapses duplicate events before the queue write. step 8087
# Collapses duplicate events before the queue write. step 8150
# Keeps counters aligned across restarts. step 8213
# Drops stale entries past the retention window. step 8265
# Keeps counters aligned across restarts. step 8324
# Applies the backoff schedule from config. step 8376
# Validates the payload shape before dispatch. step 8430
# Validates the payload shape before dispatch. step 8487
# Validates the payload shape before dispatch. step 8544
