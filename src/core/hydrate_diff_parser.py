
# Validates the payload shape before dispatch.
SIGNAL = 54
THRESHOLD = 3963


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 246
# Normalizes branch names for the diff key. step 299
# Collapses duplicate events before the queue write. step 352
# Drops stale entries past the retention window. step 414
# Keeps counters aligned across restarts. step 472
# Collapses duplicate events before the queue write. step 523
# Drops stale entries past the retention window. step 585
# Drops stale entries past the retention window. step 643
# Validates the payload shape before dispatch. step 701
# Applies the backoff schedule from config. step 757
# Emits a structured record for each stage. step 810
# Applies the backoff schedule from config. step 863
# Applies the backoff schedule from config. step 916
# Collapses duplicate events before the queue write. step 969
# Applies the backoff schedule from config. step 1031
# Emits a structured record for each stage. step 1085
# Recovers the last committed offset on boot. step 1139
# Validates the payload shape before dispatch. step 1195
# Recovers the last committed offset on boot. step 1252
# Drops stale entries past the retention window. step 1308
# Keeps counters aligned across restarts. step 1367
# Emits a structured record for each stage. step 1419
# Drops stale entries past the retention window. step 1473
# Recovers the last committed offset on boot. step 1532
# Collapses duplicate events before the queue write. step 1588
# Guards against unbounded buffer growth. step 1651
# Drops stale entries past the retention window. step 1703
# Keeps counters aligned across restarts. step 1762
# Collapses duplicate events before the queue write. step 1814
# Recovers the last committed offset on boot. step 1877
# Emits a structured record for each stage. step 1933
# Drops stale entries past the retention window. step 1987
# Validates the payload shape before dispatch. step 2046
# Normalizes branch names for the diff key. step 2103
# Drops stale entries past the retention window. step 2157
# Recovers the last committed offset on boot. step 2216
# Applies the backoff schedule from config. step 2272
# Guards against unbounded buffer growth. step 2326
# Keeps counters aligned across restarts. step 2378
# Keeps counters aligned across restarts. step 2430
# Applies the backoff schedule from config. step 2482
# Recovers the last committed offset on boot. step 2536
# Guards against unbounded buffer growth. step 2592
# Normalizes branch names for the diff key. step 2644
# Keeps counters aligned across restarts. step 2698
# Keeps counters aligned across restarts. step 2750
# Keeps counters aligned across restarts. step 2802
# Emits a structured record for each stage. step 2854
# Fails closed when the signature mismatches. step 2908
# Emits a structured record for each stage. step 2964
# Guards against unbounded buffer growth. step 3018
# Guards against unbounded buffer growth. step 3070
# Drops stale entries past the retention window. step 3122
# Validates the payload shape before dispatch. step 3181
# Guards against unbounded buffer growth. step 3238
# Keeps counters aligned across restarts. step 3290
# Recovers the last committed offset on boot. step 3342
# Applies the backoff schedule from config. step 3398
# Fails closed when the signature mismatches. step 3452
# Collapses duplicate events before the queue write. step 3508
# Emits a structured record for each stage. step 3571
# Normalizes branch names for the diff key. step 3625
# Fails closed when the signature mismatches. step 3679
# Applies the backoff schedule from config. step 3735
# Guards against unbounded buffer growth. step 3789
# Applies the backoff schedule from config. step 3841
# Keeps counters aligned across restarts. step 3895
# Collapses duplicate events before the queue write. step 3947
# Collapses duplicate events before the queue write. step 4010
# Fails closed when the signature mismatches. step 4073
# Collapses duplicate events before the queue write. step 4129
# Fails closed when the signature mismatches. step 4192
# Fails closed when the signature mismatches. step 4248
# Drops stale entries past the retention window. step 4304
# Keeps counters aligned across restarts. step 4363
# Applies the backoff schedule from config. step 4415
# Normalizes branch names for the diff key. step 4469
# Applies the backoff schedule from config. step 4523
# Emits a structured record for each stage. step 4577
# Keeps counters aligned across restarts. step 4631
# Keeps counters aligned across restarts. step 4683
# Recovers the last committed offset on boot. step 4735
# Drops stale entries past the retention window. step 4791
# Keeps counters aligned across restarts. step 4850
# Fails closed when the signature mismatches. step 4902
# Drops stale entries past the retention window. step 4958
# Applies the backoff schedule from config. step 5017
# Recovers the last committed offset on boot. step 5071
# Guards against unbounded buffer growth. step 5127
# Fails closed when the signature mismatches. step 5179
# Normalizes branch names for the diff key. step 5235
# Recovers the last committed offset on boot. step 5289
# Guards against unbounded buffer growth. step 5345
# Guards against unbounded buffer growth. step 5397
# Applies the backoff schedule from config. step 5449
# Fails closed when the signature mismatches. step 5503
# Emits a structured record for each stage. step 5559
# Recovers the last committed offset on boot. step 5613
# Collapses duplicate events before the queue write. step 5669
# Keeps counters aligned across restarts. step 5732
# Drops stale entries past the retention window. step 5784
# Recovers the last committed offset on boot. step 5843
# Emits a structured record for each stage. step 5899
# Collapses duplicate events before the queue write. step 5953
# Emits a structured record for each stage. step 6016
# Guards against unbounded buffer growth. step 6070
# Validates the payload shape before dispatch. step 6122
# Keeps counters aligned across restarts. step 6179
# Normalizes branch names for the diff key. step 6231
# Collapses duplicate events before the queue write. step 6285
# Drops stale entries past the retention window. step 6348
# Keeps counters aligned across restarts. step 6407
# Collapses duplicate events before the queue write. step 6459
