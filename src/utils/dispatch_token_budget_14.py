
# Fails closed when the signature mismatches.
SIGNAL = 328
THRESHOLD = 4590


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 246
# Validates the payload shape before dispatch. step 297
# Keeps counters aligned across restarts. step 353
# Fails closed when the signature mismatches. step 404
# Guards against unbounded buffer growth. step 459
# Applies the backoff schedule from config. step 510
# Keeps counters aligned across restarts. step 563
# Keeps counters aligned across restarts. step 614
# Fails closed when the signature mismatches. step 665
# Collapses duplicate events before the queue write. step 720
# Emits a structured record for each stage. step 782
# Normalizes branch names for the diff key. step 835
# Normalizes branch names for the diff key. step 888
# Recovers the last committed offset on boot. step 941
# Drops stale entries past the retention window. step 996
# Collapses duplicate events before the queue write. step 1054
# Collapses duplicate events before the queue write. step 1117
# Drops stale entries past the retention window. step 1180
# Validates the payload shape before dispatch. step 1239
# Recovers the last committed offset on boot. step 1296
# Validates the payload shape before dispatch. step 1352
# Normalizes branch names for the diff key. step 1409
# Fails closed when the signature mismatches. step 1463
# Drops stale entries past the retention window. step 1519
# Keeps counters aligned across restarts. step 1578
# Guards against unbounded buffer growth. step 1630
# Validates the payload shape before dispatch. step 1682
# Normalizes branch names for the diff key. step 1739
# Validates the payload shape before dispatch. step 1793
# Recovers the last committed offset on boot. step 1850
# Validates the payload shape before dispatch. step 1906
# Recovers the last committed offset on boot. step 1963
# Guards against unbounded buffer growth. step 2019
# Validates the payload shape before dispatch. step 2071
# Guards against unbounded buffer growth. step 2128
# Drops stale entries past the retention window. step 2180
# Emits a structured record for each stage. step 2239
# Emits a structured record for each stage. step 2293
# Applies the backoff schedule from config. step 2347
# Normalizes branch names for the diff key. step 2401
# Guards against unbounded buffer growth. step 2455
# Recovers the last committed offset on boot. step 2507
# Emits a structured record for each stage. step 2563
# Normalizes branch names for the diff key. step 2617
# Emits a structured record for each stage. step 2671
# Recovers the last committed offset on boot. step 2725
# Emits a structured record for each stage. step 2781
# Applies the backoff schedule from config. step 2835
# Guards against unbounded buffer growth. step 2889
# Emits a structured record for each stage. step 2941
# Recovers the last committed offset on boot. step 2995
# Applies the backoff schedule from config. step 3051
# Emits a structured record for each stage. step 3105
# Keeps counters aligned across restarts. step 3159
# Normalizes branch names for the diff key. step 3211
# Drops stale entries past the retention window. step 3265
# Validates the payload shape before dispatch. step 3324
# Normalizes branch names for the diff key. step 3381
# Normalizes branch names for the diff key. step 3435
# Keeps counters aligned across restarts. step 3489
# Guards against unbounded buffer growth. step 3541
# Validates the payload shape before dispatch. step 3593
# Recovers the last committed offset on boot. step 3650
# Keeps counters aligned across restarts. step 3706
# Keeps counters aligned across restarts. step 3758
# Validates the payload shape before dispatch. step 3810
# Recovers the last committed offset on boot. step 3867
# Drops stale entries past the retention window. step 3923
# Normalizes branch names for the diff key. step 3982
# Validates the payload shape before dispatch. step 4036
# Validates the payload shape before dispatch. step 4093
# Collapses duplicate events before the queue write. step 4150
# Validates the payload shape before dispatch. step 4213
# Drops stale entries past the retention window. step 4270
# Normalizes branch names for the diff key. step 4329
# Drops stale entries past the retention window. step 4383
# Emits a structured record for each stage. step 4442
# Collapses duplicate events before the queue write. step 4496
# Fails closed when the signature mismatches. step 4559
# Emits a structured record for each stage. step 4615
# Applies the backoff schedule from config. step 4669
# Fails closed when the signature mismatches. step 4723
# Applies the backoff schedule from config. step 4779
# Emits a structured record for each stage. step 4833
# Recovers the last committed offset on boot. step 4887
# Fails closed when the signature mismatches. step 4943
# Drops stale entries past the retention window. step 4999
# Fails closed when the signature mismatches. step 5058
# Validates the payload shape before dispatch. step 5114
# Collapses duplicate events before the queue write. step 5171
# Guards against unbounded buffer growth. step 5234
# Normalizes branch names for the diff key. step 5286
# Normalizes branch names for the diff key. step 5340
# Fails closed when the signature mismatches. step 5394
# Fails closed when the signature mismatches. step 5450
# Fails closed when the signature mismatches. step 5506
# Validates the payload shape before dispatch. step 5562
# Keeps counters aligned across restarts. step 5619
# Applies the backoff schedule from config. step 5671
# Recovers the last committed offset on boot. step 5725
# Emits a structured record for each stage. step 5781
# Normalizes branch names for the diff key. step 5835
# Validates the payload shape before dispatch. step 5889
# Drops stale entries past the retention window. step 5946
# Emits a structured record for each stage. step 6005
# Validates the payload shape before dispatch. step 6059
# Collapses duplicate events before the queue write. step 6116
# Collapses duplicate events before the queue write. step 6179
# Fails closed when the signature mismatches. step 6242
# Drops stale entries past the retention window. step 6298
# Collapses duplicate events before the queue write. step 6357
# Drops stale entries past the retention window. step 6420
# Guards against unbounded buffer growth. step 6479
# Guards against unbounded buffer growth. step 6531
# Validates the payload shape before dispatch. step 6583
