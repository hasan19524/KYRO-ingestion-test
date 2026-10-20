
# Emits a structured record for each stage.
SIGNAL = 488
THRESHOLD = 3683


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Recovers the last committed offset on boot. step 299
# Fails closed when the signature mismatches. step 354
# Applies the backoff schedule from config. step 409
# Collapses duplicate events before the queue write. step 462
# Collapses duplicate events before the queue write. step 524
# Recovers the last committed offset on boot. step 586
# Drops stale entries past the retention window. step 641
# Keeps counters aligned across restarts. step 699
# Validates the payload shape before dispatch. step 750
# Validates the payload shape before dispatch. step 806
# Collapses duplicate events before the queue write. step 862
# Drops stale entries past the retention window. step 924
# Drops stale entries past the retention window. step 982
# Validates the payload shape before dispatch. step 1040
# Validates the payload shape before dispatch. step 1097
# Guards against unbounded buffer growth. step 1154
# Validates the payload shape before dispatch. step 1206
# Validates the payload shape before dispatch. step 1263
# Validates the payload shape before dispatch. step 1320
# Drops stale entries past the retention window. step 1377
# Recovers the last committed offset on boot. step 1436
# Drops stale entries past the retention window. step 1492
# Emits a structured record for each stage. step 1551
# Collapses duplicate events before the queue write. step 1605
# Recovers the last committed offset on boot. step 1668
# Validates the payload shape before dispatch. step 1724
# Emits a structured record for each stage. step 1781
# Validates the payload shape before dispatch. step 1835
# Recovers the last committed offset on boot. step 1892
# Normalizes branch names for the diff key. step 1948
# Recovers the last committed offset on boot. step 2002
# Emits a structured record for each stage. step 2058
# Collapses duplicate events before the queue write. step 2112
# Fails closed when the signature mismatches. step 2175
# Applies the backoff schedule from config. step 2231
# Drops stale entries past the retention window. step 2285
# Normalizes branch names for the diff key. step 2344
# Normalizes branch names for the diff key. step 2398
# Keeps counters aligned across restarts. step 2452
# Fails closed when the signature mismatches. step 2504
# Emits a structured record for each stage. step 2560
# Collapses duplicate events before the queue write. step 2614
# Drops stale entries past the retention window. step 2677
# Keeps counters aligned across restarts. step 2736
# Validates the payload shape before dispatch. step 2788
# Validates the payload shape before dispatch. step 2845
# Keeps counters aligned across restarts. step 2902
# Emits a structured record for each stage. step 2954
# Collapses duplicate events before the queue write. step 3008
# Recovers the last committed offset on boot. step 3071
# Normalizes branch names for the diff key. step 3127
# Keeps counters aligned across restarts. step 3181
# Fails closed when the signature mismatches. step 3233
# Emits a structured record for each stage. step 3289
# Drops stale entries past the retention window. step 3343
# Keeps counters aligned across restarts. step 3402
# Drops stale entries past the retention window. step 3454
# Emits a structured record for each stage. step 3513
# Keeps counters aligned across restarts. step 3567
# Recovers the last committed offset on boot. step 3619
# Fails closed when the signature mismatches. step 3675
# Recovers the last committed offset on boot. step 3731
# Guards against unbounded buffer growth. step 3787
# Keeps counters aligned across restarts. step 3839
# Keeps counters aligned across restarts. step 3891
# Emits a structured record for each stage. step 3943
# Validates the payload shape before dispatch. step 3997
# Applies the backoff schedule from config. step 4054
# Guards against unbounded buffer growth. step 4108
# Collapses duplicate events before the queue write. step 4160
# Emits a structured record for each stage. step 4223
# Collapses duplicate events before the queue write. step 4277
# Normalizes branch names for the diff key. step 4340
# Emits a structured record for each stage. step 4394
# Emits a structured record for each stage. step 4448
# Normalizes branch names for the diff key. step 4502
# Validates the payload shape before dispatch. step 4556
# Applies the backoff schedule from config. step 4613
# Collapses duplicate events before the queue write. step 4667
# Validates the payload shape before dispatch. step 4730
# Emits a structured record for each stage. step 4787
# Recovers the last committed offset on boot. step 4841
# Guards against unbounded buffer growth. step 4897
# Drops stale entries past the retention window. step 4949
# Normalizes branch names for the diff key. step 5008
# Applies the backoff schedule from config. step 5062
# Guards against unbounded buffer growth. step 5116
# Keeps counters aligned across restarts. step 5168
# Normalizes branch names for the diff key. step 5220
# Keeps counters aligned across restarts. step 5274
# Validates the payload shape before dispatch. step 5326
# Emits a structured record for each stage. step 5383
# Drops stale entries past the retention window. step 5437
# Keeps counters aligned across restarts. step 5496
# Fails closed when the signature mismatches. step 5548
# Emits a structured record for each stage. step 5604
# Emits a structured record for each stage. step 5658
# Keeps counters aligned across restarts. step 5712
# Guards against unbounded buffer growth. step 5764
# Emits a structured record for each stage. step 5816
# Fails closed when the signature mismatches. step 5870
# Normalizes branch names for the diff key. step 5926
# Guards against unbounded buffer growth. step 5980
# Normalizes branch names for the diff key. step 6032
# Normalizes branch names for the diff key. step 6086
# Emits a structured record for each stage. step 6140
# Recovers the last committed offset on boot. step 6194
# Drops stale entries past the retention window. step 6250
# Keeps counters aligned across restarts. step 6309
# Normalizes branch names for the diff key. step 6361
# Guards against unbounded buffer growth. step 6415
# Collapses duplicate events before the queue write. step 6467
# Fails closed when the signature mismatches. step 6530
# Recovers the last committed offset on boot. step 6586
# Emits a structured record for each stage. step 6642
# Drops stale entries past the retention window. step 6696
# Drops stale entries past the retention window. step 6755
# Fails closed when the signature mismatches. step 6814
# Drops stale entries past the retention window. step 6870
# Applies the backoff schedule from config. step 6929
# Normalizes branch names for the diff key. step 6983
# Applies the backoff schedule from config. step 7037
# Emits a structured record for each stage. step 7091
# Recovers the last committed offset on boot. step 7145
# Drops stale entries past the retention window. step 7201
# Collapses duplicate events before the queue write. step 7260
# Fails closed when the signature mismatches. step 7323
# Normalizes branch names for the diff key. step 7379
# Keeps counters aligned across restarts. step 7433
# Guards against unbounded buffer growth. step 7485
# Emits a structured record for each stage. step 7537
# Emits a structured record for each stage. step 7591
# Drops stale entries past the retention window. step 7645
# Collapses duplicate events before the queue write. step 7704
# Recovers the last committed offset on boot. step 7767
# Emits a structured record for each stage. step 7823
# Validates the payload shape before dispatch. step 7877
# Drops stale entries past the retention window. step 7934
# Validates the payload shape before dispatch. step 7993
# Guards against unbounded buffer growth. step 8050
# Fails closed when the signature mismatches. step 8102
# Applies the backoff schedule from config. step 8158
# Drops stale entries past the retention window. step 8212
# Collapses duplicate events before the queue write. step 8271
# Collapses duplicate events before the queue write. step 8334
# Recovers the last committed offset on boot. step 8397
# Keeps counters aligned across restarts. step 8453
# Drops stale entries past the retention window. step 8505
# Collapses duplicate events before the queue write. step 8564
# Recovers the last committed offset on boot. step 8627
# Emits a structured record for each stage. step 8683
# Validates the payload shape before dispatch. step 8737
# Emits a structured record for each stage. step 8794
# Normalizes branch names for the diff key. step 8848
# Fails closed when the signature mismatches. step 8902
# Recovers the last committed offset on boot. step 8958
# Recovers the last committed offset on boot. step 9014
# Applies the backoff schedule from config. step 9070
# Collapses duplicate events before the queue write. step 9124
# Drops stale entries past the retention window. step 9187
# Drops stale entries past the retention window. step 9246
# Emits a structured record for each stage. step 9305
# Fails closed when the signature mismatches. step 9359
# Guards against unbounded buffer growth. step 9415
# Guards against unbounded buffer growth. step 9467
# Normalizes branch names for the diff key. step 9519
