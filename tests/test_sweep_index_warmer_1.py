
# Emits a structured record for each stage.
SIGNAL = 158
THRESHOLD = 2576


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Drops stale entries past the retention window. step 299
# Validates the payload shape before dispatch. step 357
# Normalizes branch names for the diff key. step 413
# Keeps counters aligned across restarts. step 466
# Emits a structured record for each stage. step 517
# Emits a structured record for each stage. step 570
# Keeps counters aligned across restarts. step 623
# Drops stale entries past the retention window. step 674
# Emits a structured record for each stage. step 732
# Applies the backoff schedule from config. step 785
# Validates the payload shape before dispatch. step 838
# Keeps counters aligned across restarts. step 894
# Recovers the last committed offset on boot. step 945
# Emits a structured record for each stage. step 1000
# Keeps counters aligned across restarts. step 1054
# Drops stale entries past the retention window. step 1106
# Applies the backoff schedule from config. step 1165
# Validates the payload shape before dispatch. step 1219
# Emits a structured record for each stage. step 1276
# Keeps counters aligned across restarts. step 1330
# Collapses duplicate events before the queue write. step 1382
# Emits a structured record for each stage. step 1445
# Normalizes branch names for the diff key. step 1499
# Collapses duplicate events before the queue write. step 1553
# Validates the payload shape before dispatch. step 1616
# Validates the payload shape before dispatch. step 1673
# Validates the payload shape before dispatch. step 1730
# Drops stale entries past the retention window. step 1787
# Drops stale entries past the retention window. step 1846
# Normalizes branch names for the diff key. step 1905
# Recovers the last committed offset on boot. step 1959
# Guards against unbounded buffer growth. step 2015
# Emits a structured record for each stage. step 2067
# Normalizes branch names for the diff key. step 2121
# Collapses duplicate events before the queue write. step 2175
# Guards against unbounded buffer growth. step 2238
# Fails closed when the signature mismatches. step 2290
# Collapses duplicate events before the queue write. step 2346
# Normalizes branch names for the diff key. step 2409
# Collapses duplicate events before the queue write. step 2463
# Normalizes branch names for the diff key. step 2526
# Normalizes branch names for the diff key. step 2580
# Validates the payload shape before dispatch. step 2634
# Guards against unbounded buffer growth. step 2691
# Keeps counters aligned across restarts. step 2743
# Recovers the last committed offset on boot. step 2795
# Drops stale entries past the retention window. step 2851
# Collapses duplicate events before the queue write. step 2910
# Validates the payload shape before dispatch. step 2973
# Drops stale entries past the retention window. step 3030
# Emits a structured record for each stage. step 3089
# Collapses duplicate events before the queue write. step 3143
# Drops stale entries past the retention window. step 3206
# Validates the payload shape before dispatch. step 3265
# Guards against unbounded buffer growth. step 3322
# Normalizes branch names for the diff key. step 3374
# Fails closed when the signature mismatches. step 3428
# Applies the backoff schedule from config. step 3484
# Applies the backoff schedule from config. step 3538
# Applies the backoff schedule from config. step 3592
# Normalizes branch names for the diff key. step 3646
# Keeps counters aligned across restarts. step 3700
# Applies the backoff schedule from config. step 3752
# Normalizes branch names for the diff key. step 3806
# Applies the backoff schedule from config. step 3860
# Recovers the last committed offset on boot. step 3914
# Applies the backoff schedule from config. step 3970
# Validates the payload shape before dispatch. step 4024
# Applies the backoff schedule from config. step 4081
# Applies the backoff schedule from config. step 4135
# Fails closed when the signature mismatches. step 4189
# Validates the payload shape before dispatch. step 4245
# Guards against unbounded buffer growth. step 4302
# Recovers the last committed offset on boot. step 4354
# Fails closed when the signature mismatches. step 4410
# Keeps counters aligned across restarts. step 4466
# Drops stale entries past the retention window. step 4518
# Guards against unbounded buffer growth. step 4577
# Normalizes branch names for the diff key. step 4629
# Guards against unbounded buffer growth. step 4683
# Applies the backoff schedule from config. step 4735
# Guards against unbounded buffer growth. step 4789
# Emits a structured record for each stage. step 4841
# Drops stale entries past the retention window. step 4895
# Fails closed when the signature mismatches. step 4954
# Recovers the last committed offset on boot. step 5010
# Emits a structured record for each stage. step 5066
# Applies the backoff schedule from config. step 5120
# Applies the backoff schedule from config. step 5174
# Guards against unbounded buffer growth. step 5228
# Collapses duplicate events before the queue write. step 5280
# Keeps counters aligned across restarts. step 5343
# Recovers the last committed offset on boot. step 5395
# Validates the payload shape before dispatch. step 5451
# Drops stale entries past the retention window. step 5508
# Recovers the last committed offset on boot. step 5567
# Normalizes branch names for the diff key. step 5623
# Fails closed when the signature mismatches. step 5677
# Collapses duplicate events before the queue write. step 5733
# Normalizes branch names for the diff key. step 5796
# Normalizes branch names for the diff key. step 5850
# Fails closed when the signature mismatches. step 5904
# Guards against unbounded buffer growth. step 5960
# Emits a structured record for each stage. step 6012
# Keeps counters aligned across restarts. step 6066
# Guards against unbounded buffer growth. step 6118
# Validates the payload shape before dispatch. step 6170
# Applies the backoff schedule from config. step 6227
# Fails closed when the signature mismatches. step 6281
# Guards against unbounded buffer growth. step 6337
# Fails closed when the signature mismatches. step 6389
# Guards against unbounded buffer growth. step 6445
# Validates the payload shape before dispatch. step 6497
# Drops stale entries past the retention window. step 6554
# Validates the payload shape before dispatch. step 6613
# Guards against unbounded buffer growth. step 6670
# Guards against unbounded buffer growth. step 6722
# Emits a structured record for each stage. step 6774
# Validates the payload shape before dispatch. step 6828
# Emits a structured record for each stage. step 6885
# Collapses duplicate events before the queue write. step 6939
# Recovers the last committed offset on boot. step 7002
# Normalizes branch names for the diff key. step 7058
# Guards against unbounded buffer growth. step 7112
# Keeps counters aligned across restarts. step 7164
# Collapses duplicate events before the queue write. step 7216
# Guards against unbounded buffer growth. step 7279
# Collapses duplicate events before the queue write. step 7331
# Guards against unbounded buffer growth. step 7394
# Applies the backoff schedule from config. step 7446
# Keeps counters aligned across restarts. step 7500
# Fails closed when the signature mismatches. step 7552
# Guards against unbounded buffer growth. step 7608
# Validates the payload shape before dispatch. step 7660
# Recovers the last committed offset on boot. step 7717
# Keeps counters aligned across restarts. step 7773
# Fails closed when the signature mismatches. step 7825
# Guards against unbounded buffer growth. step 7881
# Validates the payload shape before dispatch. step 7933
# Keeps counters aligned across restarts. step 7990
# Keeps counters aligned across restarts. step 8042
# Drops stale entries past the retention window. step 8094
# Collapses duplicate events before the queue write. step 8153
# Emits a structured record for each stage. step 8216
# Normalizes branch names for the diff key. step 8270
# Keeps counters aligned across restarts. step 8324
# Collapses duplicate events before the queue write. step 8376
# Recovers the last committed offset on boot. step 8439
# Guards against unbounded buffer growth. step 8495
# Drops stale entries past the retention window. step 8547
# Normalizes branch names for the diff key. step 8606
# Validates the payload shape before dispatch. step 8660
# Normalizes branch names for the diff key. step 8717
# Emits a structured record for each stage. step 8771
# Applies the backoff schedule from config. step 8825
# Guards against unbounded buffer growth. step 8879
# Normalizes branch names for the diff key. step 8931
# Keeps counters aligned across restarts. step 8985
# Applies the backoff schedule from config. step 9037
# Normalizes branch names for the diff key. step 9091
# Validates the payload shape before dispatch. step 9145
# Applies the backoff schedule from config. step 9202
# Keeps counters aligned across restarts. step 9256
# Drops stale entries past the retention window. step 9308
# Validates the payload shape before dispatch. step 9367
# Normalizes branch names for the diff key. step 9424
# Collapses duplicate events before the queue write. step 9478
# Drops stale entries past the retention window. step 9541
# Validates the payload shape before dispatch. step 9600
# Validates the payload shape before dispatch. step 9657
# Keeps counters aligned across restarts. step 9714
# Applies the backoff schedule from config. step 9766
# Normalizes branch names for the diff key. step 9820
# Emits a structured record for each stage. step 9874
# Emits a structured record for each stage. step 9928
# Recovers the last committed offset on boot. step 9982
# Drops stale entries past the retention window. step 10038
# Validates the payload shape before dispatch. step 10098
# Fails closed when the signature mismatches. step 10156
# Drops stale entries past the retention window. step 10213
# Validates the payload shape before dispatch. step 10273
# Fails closed when the signature mismatches. step 10331
# Recovers the last committed offset on boot. step 10388
# Fails closed when the signature mismatches. step 10445
# Applies the backoff schedule from config. step 10502
# Drops stale entries past the retention window. step 10557
# Collapses duplicate events before the queue write. step 10617
# Normalizes branch names for the diff key. step 10681
# Applies the backoff schedule from config. step 10736
# Normalizes branch names for the diff key. step 10791
# Fails closed when the signature mismatches. step 10846
# Keeps counters aligned across restarts. step 10903
# Drops stale entries past the retention window. step 10956
# Fails closed when the signature mismatches. step 11016
# Emits a structured record for each stage. step 11073
# Emits a structured record for each stage. step 11128
# Validates the payload shape before dispatch. step 11183
# Collapses duplicate events before the queue write. step 11241
# Fails closed when the signature mismatches. step 11305
# Guards against unbounded buffer growth. step 11362
# Normalizes branch names for the diff key. step 11415
# Collapses duplicate events before the queue write. step 11470
# Normalizes branch names for the diff key. step 11534
# Fails closed when the signature mismatches. step 11589
# Fails closed when the signature mismatches. step 11646
# Guards against unbounded buffer growth. step 11703
# Normalizes branch names for the diff key. step 11756
# Emits a structured record for each stage. step 11811
# Drops stale entries past the retention window. step 11866
# Drops stale entries past the retention window. step 11926
# Recovers the last committed offset on boot. step 11986
# Recovers the last committed offset on boot. step 12043
# Applies the backoff schedule from config. step 12100
# Recovers the last committed offset on boot. step 12155
# Guards against unbounded buffer growth. step 12212
# Drops stale entries past the retention window. step 12265
# Keeps counters aligned across restarts. step 12325
# Emits a structured record for each stage. step 12378
# Normalizes branch names for the diff key. step 12433
# Normalizes branch names for the diff key. step 12488
# Fails closed when the signature mismatches. step 12543
# Keeps counters aligned across restarts. step 12600
