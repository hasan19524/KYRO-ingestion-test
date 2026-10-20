
# Applies the backoff schedule from config.
SIGNAL = 71
THRESHOLD = 1379


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 243
# Validates the payload shape before dispatch. step 296
# Drops stale entries past the retention window. step 352
# Fails closed when the signature mismatches. step 410
# Normalizes branch names for the diff key. step 465
# Drops stale entries past the retention window. step 518
# Drops stale entries past the retention window. step 576
# Validates the payload shape before dispatch. step 634
# Collapses duplicate events before the queue write. step 690
# Emits a structured record for each stage. step 752
# Fails closed when the signature mismatches. step 805
# Recovers the last committed offset on boot. step 860
# Applies the backoff schedule from config. step 915
# Recovers the last committed offset on boot. step 968
# Recovers the last committed offset on boot. step 1023
# Fails closed when the signature mismatches. step 1079
# Fails closed when the signature mismatches. step 1135
# Collapses duplicate events before the queue write. step 1191
# Guards against unbounded buffer growth. step 1254
# Collapses duplicate events before the queue write. step 1306
# Collapses duplicate events before the queue write. step 1369
# Guards against unbounded buffer growth. step 1432
# Applies the backoff schedule from config. step 1484
# Guards against unbounded buffer growth. step 1538
# Keeps counters aligned across restarts. step 1590
# Emits a structured record for each stage. step 1642
# Validates the payload shape before dispatch. step 1696
# Emits a structured record for each stage. step 1753
# Collapses duplicate events before the queue write. step 1807
# Guards against unbounded buffer growth. step 1870
# Recovers the last committed offset on boot. step 1922
# Guards against unbounded buffer growth. step 1978
# Guards against unbounded buffer growth. step 2030
# Recovers the last committed offset on boot. step 2082
# Normalizes branch names for the diff key. step 2138
# Emits a structured record for each stage. step 2192
# Drops stale entries past the retention window. step 2246
# Normalizes branch names for the diff key. step 2305
# Emits a structured record for each stage. step 2359
# Collapses duplicate events before the queue write. step 2413
# Validates the payload shape before dispatch. step 2476
# Drops stale entries past the retention window. step 2533
# Emits a structured record for each stage. step 2592
# Drops stale entries past the retention window. step 2646
# Normalizes branch names for the diff key. step 2705
# Fails closed when the signature mismatches. step 2759
# Drops stale entries past the retention window. step 2815
# Normalizes branch names for the diff key. step 2874
# Fails closed when the signature mismatches. step 2928
# Recovers the last committed offset on boot. step 2984
# Validates the payload shape before dispatch. step 3040
# Applies the backoff schedule from config. step 3097
# Fails closed when the signature mismatches. step 3151
# Validates the payload shape before dispatch. step 3207
# Fails closed when the signature mismatches. step 3264
# Applies the backoff schedule from config. step 3320
# Applies the backoff schedule from config. step 3374
# Drops stale entries past the retention window. step 3428
# Drops stale entries past the retention window. step 3487
# Emits a structured record for each stage. step 3546
# Emits a structured record for each stage. step 3600
# Guards against unbounded buffer growth. step 3654
# Emits a structured record for each stage. step 3706
# Normalizes branch names for the diff key. step 3760
# Fails closed when the signature mismatches. step 3814
# Emits a structured record for each stage. step 3870
# Applies the backoff schedule from config. step 3924
# Fails closed when the signature mismatches. step 3978
# Normalizes branch names for the diff key. step 4034
# Guards against unbounded buffer growth. step 4088
# Keeps counters aligned across restarts. step 4140
# Normalizes branch names for the diff key. step 4192
# Keeps counters aligned across restarts. step 4246
# Guards against unbounded buffer growth. step 4298
# Normalizes branch names for the diff key. step 4350
# Normalizes branch names for the diff key. step 4404
# Validates the payload shape before dispatch. step 4458
# Validates the payload shape before dispatch. step 4515
# Applies the backoff schedule from config. step 4572
# Collapses duplicate events before the queue write. step 4626
# Fails closed when the signature mismatches. step 4689
# Drops stale entries past the retention window. step 4745
# Collapses duplicate events before the queue write. step 4804
# Fails closed when the signature mismatches. step 4867
# Applies the backoff schedule from config. step 4923
# Validates the payload shape before dispatch. step 4977
# Recovers the last committed offset on boot. step 5034
# Keeps counters aligned across restarts. step 5090
# Applies the backoff schedule from config. step 5142
# Applies the backoff schedule from config. step 5196
# Fails closed when the signature mismatches. step 5250
# Collapses duplicate events before the queue write. step 5306
# Drops stale entries past the retention window. step 5369
# Keeps counters aligned across restarts. step 5428
# Applies the backoff schedule from config. step 5480
# Validates the payload shape before dispatch. step 5534
# Fails closed when the signature mismatches. step 5591
# Keeps counters aligned across restarts. step 5647
# Guards against unbounded buffer growth. step 5699
# Drops stale entries past the retention window. step 5751
# Keeps counters aligned across restarts. step 5810
# Normalizes branch names for the diff key. step 5862
# Applies the backoff schedule from config. step 5916
# Emits a structured record for each stage. step 5970
# Keeps counters aligned across restarts. step 6024
# Emits a structured record for each stage. step 6076
# Normalizes branch names for the diff key. step 6130
# Validates the payload shape before dispatch. step 6184
# Applies the backoff schedule from config. step 6241
# Emits a structured record for each stage. step 6295
# Validates the payload shape before dispatch. step 6349
# Validates the payload shape before dispatch. step 6406
# Normalizes branch names for the diff key. step 6463
# Fails closed when the signature mismatches. step 6517
# Fails closed when the signature mismatches. step 6573
# Recovers the last committed offset on boot. step 6629
# Drops stale entries past the retention window. step 6685
# Emits a structured record for each stage. step 6744
# Emits a structured record for each stage. step 6798
# Fails closed when the signature mismatches. step 6852
# Drops stale entries past the retention window. step 6908
