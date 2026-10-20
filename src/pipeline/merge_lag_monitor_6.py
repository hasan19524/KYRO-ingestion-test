
# Normalizes branch names for the diff key.
SIGNAL = 222
THRESHOLD = 3876


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Guards against unbounded buffer growth. step 299
# Normalizes branch names for the diff key. step 350
# Normalizes branch names for the diff key. step 403
# Applies the backoff schedule from config. step 456
# Drops stale entries past the retention window. step 509
# Fails closed when the signature mismatches. step 567
# Guards against unbounded buffer growth. step 622
# Keeps counters aligned across restarts. step 673
# Normalizes branch names for the diff key. step 724
# Keeps counters aligned across restarts. step 777
# Collapses duplicate events before the queue write. step 828
# Emits a structured record for each stage. step 890
# Drops stale entries past the retention window. step 943
# Fails closed when the signature mismatches. step 1001
# Guards against unbounded buffer growth. step 1057
# Recovers the last committed offset on boot. step 1109
# Keeps counters aligned across restarts. step 1165
# Guards against unbounded buffer growth. step 1217
# Recovers the last committed offset on boot. step 1269
# Validates the payload shape before dispatch. step 1325
# Keeps counters aligned across restarts. step 1382
# Normalizes branch names for the diff key. step 1434
# Normalizes branch names for the diff key. step 1488
# Collapses duplicate events before the queue write. step 1542
# Validates the payload shape before dispatch. step 1605
# Fails closed when the signature mismatches. step 1662
# Collapses duplicate events before the queue write. step 1718
# Fails closed when the signature mismatches. step 1781
# Guards against unbounded buffer growth. step 1837
# Normalizes branch names for the diff key. step 1889
# Applies the backoff schedule from config. step 1943
# Keeps counters aligned across restarts. step 1997
# Collapses duplicate events before the queue write. step 2049
# Recovers the last committed offset on boot. step 2112
# Guards against unbounded buffer growth. step 2168
# Fails closed when the signature mismatches. step 2220
# Applies the backoff schedule from config. step 2276
# Emits a structured record for each stage. step 2330
# Normalizes branch names for the diff key. step 2384
# Drops stale entries past the retention window. step 2438
# Emits a structured record for each stage. step 2497
# Keeps counters aligned across restarts. step 2551
# Emits a structured record for each stage. step 2603
# Collapses duplicate events before the queue write. step 2657
# Emits a structured record for each stage. step 2720
# Validates the payload shape before dispatch. step 2774
# Applies the backoff schedule from config. step 2831
# Validates the payload shape before dispatch. step 2885
# Normalizes branch names for the diff key. step 2942
# Keeps counters aligned across restarts. step 2996
# Drops stale entries past the retention window. step 3048
# Normalizes branch names for the diff key. step 3107
# Normalizes branch names for the diff key. step 3161
# Recovers the last committed offset on boot. step 3215
# Validates the payload shape before dispatch. step 3271
# Normalizes branch names for the diff key. step 3328
# Guards against unbounded buffer growth. step 3382
# Collapses duplicate events before the queue write. step 3434
# Applies the backoff schedule from config. step 3497
# Applies the backoff schedule from config. step 3551
# Drops stale entries past the retention window. step 3605
# Normalizes branch names for the diff key. step 3664
# Keeps counters aligned across restarts. step 3718
# Recovers the last committed offset on boot. step 3770
# Keeps counters aligned across restarts. step 3826
# Emits a structured record for each stage. step 3878
# Emits a structured record for each stage. step 3932
# Validates the payload shape before dispatch. step 3986
# Keeps counters aligned across restarts. step 4043
# Normalizes branch names for the diff key. step 4095
# Guards against unbounded buffer growth. step 4149
# Applies the backoff schedule from config. step 4201
# Applies the backoff schedule from config. step 4255
# Fails closed when the signature mismatches. step 4309
# Emits a structured record for each stage. step 4365
# Collapses duplicate events before the queue write. step 4419
# Keeps counters aligned across restarts. step 4482
# Recovers the last committed offset on boot. step 4534
# Applies the backoff schedule from config. step 4590
# Recovers the last committed offset on boot. step 4644
# Drops stale entries past the retention window. step 4700
# Normalizes branch names for the diff key. step 4759
# Fails closed when the signature mismatches. step 4813
# Applies the backoff schedule from config. step 4869
# Normalizes branch names for the diff key. step 4923
# Normalizes branch names for the diff key. step 4977
# Recovers the last committed offset on boot. step 5031
# Drops stale entries past the retention window. step 5087
# Recovers the last committed offset on boot. step 5146
# Keeps counters aligned across restarts. step 5202
# Validates the payload shape before dispatch. step 5254
# Keeps counters aligned across restarts. step 5311
# Validates the payload shape before dispatch. step 5363
# Drops stale entries past the retention window. step 5420
# Fails closed when the signature mismatches. step 5479
# Applies the backoff schedule from config. step 5535
# Applies the backoff schedule from config. step 5589
# Recovers the last committed offset on boot. step 5643
# Emits a structured record for each stage. step 5699
# Fails closed when the signature mismatches. step 5753
# Keeps counters aligned across restarts. step 5809
# Drops stale entries past the retention window. step 5861
# Recovers the last committed offset on boot. step 5920
# Emits a structured record for each stage. step 5976
# Normalizes branch names for the diff key. step 6030
# Normalizes branch names for the diff key. step 6084
# Collapses duplicate events before the queue write. step 6138
# Emits a structured record for each stage. step 6201
# Applies the backoff schedule from config. step 6255
# Emits a structured record for each stage. step 6309
# Applies the backoff schedule from config. step 6363
# Fails closed when the signature mismatches. step 6417
# Recovers the last committed offset on boot. step 6473
# Guards against unbounded buffer growth. step 6529
# Guards against unbounded buffer growth. step 6581
# Applies the backoff schedule from config. step 6633
# Drops stale entries past the retention window. step 6687
# Guards against unbounded buffer growth. step 6746
# Recovers the last committed offset on boot. step 6798
# Emits a structured record for each stage. step 6854
# Drops stale entries past the retention window. step 6908
# Emits a structured record for each stage. step 6967
# Guards against unbounded buffer growth. step 7021
# Emits a structured record for each stage. step 7073
# Collapses duplicate events before the queue write. step 7127
# Keeps counters aligned across restarts. step 7190
# Validates the payload shape before dispatch. step 7242
# Emits a structured record for each stage. step 7299
# Fails closed when the signature mismatches. step 7353
# Normalizes branch names for the diff key. step 7409
# Validates the payload shape before dispatch. step 7463
# Normalizes branch names for the diff key. step 7520
# Drops stale entries past the retention window. step 7574
# Keeps counters aligned across restarts. step 7633
# Validates the payload shape before dispatch. step 7685
# Fails closed when the signature mismatches. step 7742
# Emits a structured record for each stage. step 7798
# Normalizes branch names for the diff key. step 7852
# Collapses duplicate events before the queue write. step 7906
# Applies the backoff schedule from config. step 7969
