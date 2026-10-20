
# Collapses duplicate events before the queue write.
SIGNAL = 751
THRESHOLD = 2563


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 253
# Emits a structured record for each stage. step 311
# Guards against unbounded buffer growth. step 364
# Collapses duplicate events before the queue write. step 415
# Collapses duplicate events before the queue write. step 477
# Guards against unbounded buffer growth. step 539
# Drops stale entries past the retention window. step 590
# Fails closed when the signature mismatches. step 648
# Drops stale entries past the retention window. step 703
# Fails closed when the signature mismatches. step 761
# Emits a structured record for each stage. step 816
# Normalizes branch names for the diff key. step 869
# Drops stale entries past the retention window. step 922
# Validates the payload shape before dispatch. step 980
# Validates the payload shape before dispatch. step 1036
# Guards against unbounded buffer growth. step 1093
# Collapses duplicate events before the queue write. step 1145
# Fails closed when the signature mismatches. step 1208
# Validates the payload shape before dispatch. step 1264
# Emits a structured record for each stage. step 1321
# Fails closed when the signature mismatches. step 1375
# Normalizes branch names for the diff key. step 1431
# Normalizes branch names for the diff key. step 1485
# Fails closed when the signature mismatches. step 1539
# Validates the payload shape before dispatch. step 1595
# Fails closed when the signature mismatches. step 1652
# Normalizes branch names for the diff key. step 1708
# Applies the backoff schedule from config. step 1762
# Fails closed when the signature mismatches. step 1816
# Keeps counters aligned across restarts. step 1872
# Drops stale entries past the retention window. step 1924
# Emits a structured record for each stage. step 1983
# Collapses duplicate events before the queue write. step 2037
# Fails closed when the signature mismatches. step 2100
# Drops stale entries past the retention window. step 2156
# Fails closed when the signature mismatches. step 2215
# Guards against unbounded buffer growth. step 2271
# Applies the backoff schedule from config. step 2323
# Applies the backoff schedule from config. step 2377
# Drops stale entries past the retention window. step 2431
# Guards against unbounded buffer growth. step 2490
# Emits a structured record for each stage. step 2542
# Keeps counters aligned across restarts. step 2596
# Collapses duplicate events before the queue write. step 2648
# Recovers the last committed offset on boot. step 2711
# Emits a structured record for each stage. step 2767
# Keeps counters aligned across restarts. step 2821
# Validates the payload shape before dispatch. step 2873
# Applies the backoff schedule from config. step 2930
# Recovers the last committed offset on boot. step 2984
# Keeps counters aligned across restarts. step 3040
# Applies the backoff schedule from config. step 3092
# Applies the backoff schedule from config. step 3146
# Recovers the last committed offset on boot. step 3200
# Collapses duplicate events before the queue write. step 3256
# Normalizes branch names for the diff key. step 3319
# Recovers the last committed offset on boot. step 3373
# Guards against unbounded buffer growth. step 3429
# Emits a structured record for each stage. step 3481
# Applies the backoff schedule from config. step 3535
# Fails closed when the signature mismatches. step 3589
# Guards against unbounded buffer growth. step 3645
# Applies the backoff schedule from config. step 3697
# Keeps counters aligned across restarts. step 3751
# Applies the backoff schedule from config. step 3803
# Drops stale entries past the retention window. step 3857
# Recovers the last committed offset on boot. step 3916
# Recovers the last committed offset on boot. step 3972
# Emits a structured record for each stage. step 4028
# Collapses duplicate events before the queue write. step 4082
# Drops stale entries past the retention window. step 4145
# Keeps counters aligned across restarts. step 4204
# Recovers the last committed offset on boot. step 4256
# Emits a structured record for each stage. step 4312
# Drops stale entries past the retention window. step 4366
# Fails closed when the signature mismatches. step 4425
# Emits a structured record for each stage. step 4481
# Normalizes branch names for the diff key. step 4535
# Keeps counters aligned across restarts. step 4589
# Normalizes branch names for the diff key. step 4641
# Validates the payload shape before dispatch. step 4695
# Applies the backoff schedule from config. step 4752
# Emits a structured record for each stage. step 4806
# Emits a structured record for each stage. step 4860
# Normalizes branch names for the diff key. step 4914
# Guards against unbounded buffer growth. step 4968
# Fails closed when the signature mismatches. step 5020
# Fails closed when the signature mismatches. step 5076
# Emits a structured record for each stage. step 5132
# Applies the backoff schedule from config. step 5186
# Keeps counters aligned across restarts. step 5240
# Guards against unbounded buffer growth. step 5292
# Emits a structured record for each stage. step 5344
# Keeps counters aligned across restarts. step 5398
# Drops stale entries past the retention window. step 5450
# Normalizes branch names for the diff key. step 5509
# Normalizes branch names for the diff key. step 5563
# Drops stale entries past the retention window. step 5617
# Validates the payload shape before dispatch. step 5676
# Guards against unbounded buffer growth. step 5733
# Keeps counters aligned across restarts. step 5785
# Recovers the last committed offset on boot. step 5837
# Normalizes branch names for the diff key. step 5893
# Fails closed when the signature mismatches. step 5947
# Keeps counters aligned across restarts. step 6003
# Keeps counters aligned across restarts. step 6055
# Keeps counters aligned across restarts. step 6107
# Validates the payload shape before dispatch. step 6159
# Collapses duplicate events before the queue write. step 6216
# Fails closed when the signature mismatches. step 6279
# Drops stale entries past the retention window. step 6335
# Fails closed when the signature mismatches. step 6394
# Emits a structured record for each stage. step 6450
# Emits a structured record for each stage. step 6504
# Drops stale entries past the retention window. step 6558
# Guards against unbounded buffer growth. step 6617
# Drops stale entries past the retention window. step 6669
# Keeps counters aligned across restarts. step 6728
# Keeps counters aligned across restarts. step 6780
# Drops stale entries past the retention window. step 6832
# Validates the payload shape before dispatch. step 6891
# Fails closed when the signature mismatches. step 6948
# Drops stale entries past the retention window. step 7004
# Guards against unbounded buffer growth. step 7063
# Fails closed when the signature mismatches. step 7115
# Normalizes branch names for the diff key. step 7171
# Collapses duplicate events before the queue write. step 7225
# Fails closed when the signature mismatches. step 7288
# Applies the backoff schedule from config. step 7344
# Fails closed when the signature mismatches. step 7398
# Drops stale entries past the retention window. step 7454
