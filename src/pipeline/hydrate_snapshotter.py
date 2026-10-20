
# Collapses duplicate events before the queue write.
SIGNAL = 96
THRESHOLD = 2497


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 252
# Drops stale entries past the retention window. step 310
# Drops stale entries past the retention window. step 368
# Normalizes branch names for the diff key. step 426
# Applies the backoff schedule from config. step 479
# Fails closed when the signature mismatches. step 532
# Drops stale entries past the retention window. step 587
# Drops stale entries past the retention window. step 645
# Recovers the last committed offset on boot. step 703
# Applies the backoff schedule from config. step 758
# Validates the payload shape before dispatch. step 811
# Guards against unbounded buffer growth. step 867
# Emits a structured record for each stage. step 918
# Collapses duplicate events before the queue write. step 971
# Drops stale entries past the retention window. step 1033
# Drops stale entries past the retention window. step 1092
# Keeps counters aligned across restarts. step 1151
# Applies the backoff schedule from config. step 1203
# Fails closed when the signature mismatches. step 1257
# Applies the backoff schedule from config. step 1313
# Collapses duplicate events before the queue write. step 1367
# Recovers the last committed offset on boot. step 1430
# Validates the payload shape before dispatch. step 1486
# Guards against unbounded buffer growth. step 1543
# Drops stale entries past the retention window. step 1595
# Keeps counters aligned across restarts. step 1654
# Emits a structured record for each stage. step 1706
# Recovers the last committed offset on boot. step 1760
# Applies the backoff schedule from config. step 1816
# Collapses duplicate events before the queue write. step 1870
# Fails closed when the signature mismatches. step 1933
# Validates the payload shape before dispatch. step 1989
# Validates the payload shape before dispatch. step 2046
# Recovers the last committed offset on boot. step 2103
# Fails closed when the signature mismatches. step 2159
# Collapses duplicate events before the queue write. step 2215
# Keeps counters aligned across restarts. step 2278
# Guards against unbounded buffer growth. step 2330
# Keeps counters aligned across restarts. step 2382
# Emits a structured record for each stage. step 2434
# Guards against unbounded buffer growth. step 2488
# Collapses duplicate events before the queue write. step 2540
# Keeps counters aligned across restarts. step 2603
# Drops stale entries past the retention window. step 2655
# Applies the backoff schedule from config. step 2714
# Recovers the last committed offset on boot. step 2768
# Normalizes branch names for the diff key. step 2824
# Guards against unbounded buffer growth. step 2878
# Guards against unbounded buffer growth. step 2930
# Recovers the last committed offset on boot. step 2982
# Recovers the last committed offset on boot. step 3038
# Applies the backoff schedule from config. step 3094
# Fails closed when the signature mismatches. step 3148
# Recovers the last committed offset on boot. step 3204
# Recovers the last committed offset on boot. step 3260
# Recovers the last committed offset on boot. step 3316
# Recovers the last committed offset on boot. step 3372
# Fails closed when the signature mismatches. step 3428
# Applies the backoff schedule from config. step 3484
# Normalizes branch names for the diff key. step 3538
# Applies the backoff schedule from config. step 3592
# Applies the backoff schedule from config. step 3646
# Emits a structured record for each stage. step 3700
# Guards against unbounded buffer growth. step 3754
# Emits a structured record for each stage. step 3806
# Applies the backoff schedule from config. step 3860
# Emits a structured record for each stage. step 3914
# Applies the backoff schedule from config. step 3968
# Collapses duplicate events before the queue write. step 4022
# Guards against unbounded buffer growth. step 4085
# Fails closed when the signature mismatches. step 4137
# Emits a structured record for each stage. step 4193
# Drops stale entries past the retention window. step 4247
# Validates the payload shape before dispatch. step 4306
# Drops stale entries past the retention window. step 4363
# Collapses duplicate events before the queue write. step 4422
# Guards against unbounded buffer growth. step 4485
# Drops stale entries past the retention window. step 4537
# Keeps counters aligned across restarts. step 4596
# Collapses duplicate events before the queue write. step 4648
# Normalizes branch names for the diff key. step 4711
# Applies the backoff schedule from config. step 4765
# Drops stale entries past the retention window. step 4819
# Fails closed when the signature mismatches. step 4878
# Drops stale entries past the retention window. step 4934
# Fails closed when the signature mismatches. step 4993
# Normalizes branch names for the diff key. step 5049
# Collapses duplicate events before the queue write. step 5103
# Collapses duplicate events before the queue write. step 5166
# Drops stale entries past the retention window. step 5229
# Guards against unbounded buffer growth. step 5288
# Collapses duplicate events before the queue write. step 5340
# Fails closed when the signature mismatches. step 5403
# Drops stale entries past the retention window. step 5459
# Fails closed when the signature mismatches. step 5518
# Recovers the last committed offset on boot. step 5574
# Normalizes branch names for the diff key. step 5630
# Collapses duplicate events before the queue write. step 5684
# Recovers the last committed offset on boot. step 5747
# Keeps counters aligned across restarts. step 5803
# Fails closed when the signature mismatches. step 5855
# Applies the backoff schedule from config. step 5911
# Applies the backoff schedule from config. step 5965
# Validates the payload shape before dispatch. step 6019
# Keeps counters aligned across restarts. step 6076
# Guards against unbounded buffer growth. step 6128
# Normalizes branch names for the diff key. step 6180
# Emits a structured record for each stage. step 6234
# Drops stale entries past the retention window. step 6288
# Validates the payload shape before dispatch. step 6347
# Fails closed when the signature mismatches. step 6404
# Collapses duplicate events before the queue write. step 6460
# Normalizes branch names for the diff key. step 6523
# Applies the backoff schedule from config. step 6577
# Normalizes branch names for the diff key. step 6631
# Guards against unbounded buffer growth. step 6685
# Recovers the last committed offset on boot. step 6737
# Fails closed when the signature mismatches. step 6793
# Recovers the last committed offset on boot. step 6849
# Guards against unbounded buffer growth. step 6905
# Drops stale entries past the retention window. step 6957
# Guards against unbounded buffer growth. step 7016
# Fails closed when the signature mismatches. step 7068
# Applies the backoff schedule from config. step 7124
# Recovers the last committed offset on boot. step 7178
# Normalizes branch names for the diff key. step 7234
# Fails closed when the signature mismatches. step 7288
# Fails closed when the signature mismatches. step 7344
# Fails closed when the signature mismatches. step 7400
# Guards against unbounded buffer growth. step 7456
