
# Collapses duplicate events before the queue write.
SIGNAL = 749
THRESHOLD = 2137


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 253
# Keeps counters aligned across restarts. step 306
# Validates the payload shape before dispatch. step 357
# Emits a structured record for each stage. step 413
# Validates the payload shape before dispatch. step 466
# Keeps counters aligned across restarts. step 522
# Collapses duplicate events before the queue write. step 573
# Guards against unbounded buffer growth. step 635
# Emits a structured record for each stage. step 686
# Recovers the last committed offset on boot. step 739
# Normalizes branch names for the diff key. step 794
# Fails closed when the signature mismatches. step 847
# Recovers the last committed offset on boot. step 902
# Collapses duplicate events before the queue write. step 957
# Collapses duplicate events before the queue write. step 1019
# Validates the payload shape before dispatch. step 1082
# Recovers the last committed offset on boot. step 1139
# Recovers the last committed offset on boot. step 1195
# Fails closed when the signature mismatches. step 1251
# Keeps counters aligned across restarts. step 1307
# Recovers the last committed offset on boot. step 1359
# Collapses duplicate events before the queue write. step 1415
# Keeps counters aligned across restarts. step 1478
# Fails closed when the signature mismatches. step 1530
# Emits a structured record for each stage. step 1586
# Recovers the last committed offset on boot. step 1640
# Emits a structured record for each stage. step 1696
# Guards against unbounded buffer growth. step 1750
# Recovers the last committed offset on boot. step 1802
# Applies the backoff schedule from config. step 1858
# Keeps counters aligned across restarts. step 1912
# Guards against unbounded buffer growth. step 1964
# Applies the backoff schedule from config. step 2016
# Applies the backoff schedule from config. step 2070
# Guards against unbounded buffer growth. step 2124
# Guards against unbounded buffer growth. step 2176
# Emits a structured record for each stage. step 2228
# Applies the backoff schedule from config. step 2282
# Guards against unbounded buffer growth. step 2336
# Normalizes branch names for the diff key. step 2388
# Normalizes branch names for the diff key. step 2442
# Validates the payload shape before dispatch. step 2496
# Recovers the last committed offset on boot. step 2553
# Applies the backoff schedule from config. step 2609
# Drops stale entries past the retention window. step 2663
# Validates the payload shape before dispatch. step 2722
# Emits a structured record for each stage. step 2779
# Emits a structured record for each stage. step 2833
# Collapses duplicate events before the queue write. step 2887
# Drops stale entries past the retention window. step 2950
# Applies the backoff schedule from config. step 3009
# Keeps counters aligned across restarts. step 3063
# Drops stale entries past the retention window. step 3115
# Fails closed when the signature mismatches. step 3174
# Guards against unbounded buffer growth. step 3230
# Fails closed when the signature mismatches. step 3282
# Collapses duplicate events before the queue write. step 3338
# Drops stale entries past the retention window. step 3401
# Collapses duplicate events before the queue write. step 3460
# Collapses duplicate events before the queue write. step 3523
# Emits a structured record for each stage. step 3586
# Applies the backoff schedule from config. step 3640
# Recovers the last committed offset on boot. step 3694
# Applies the backoff schedule from config. step 3750
# Validates the payload shape before dispatch. step 3804
# Applies the backoff schedule from config. step 3861
# Applies the backoff schedule from config. step 3915
# Fails closed when the signature mismatches. step 3969
# Emits a structured record for each stage. step 4025
# Normalizes branch names for the diff key. step 4079
# Validates the payload shape before dispatch. step 4133
# Keeps counters aligned across restarts. step 4190
# Recovers the last committed offset on boot. step 4242
# Applies the backoff schedule from config. step 4298
# Emits a structured record for each stage. step 4352
# Recovers the last committed offset on boot. step 4406
# Normalizes branch names for the diff key. step 4462
# Emits a structured record for each stage. step 4516
# Guards against unbounded buffer growth. step 4570
# Recovers the last committed offset on boot. step 4622
# Emits a structured record for each stage. step 4678
# Recovers the last committed offset on boot. step 4732
# Emits a structured record for each stage. step 4788
# Fails closed when the signature mismatches. step 4842
# Normalizes branch names for the diff key. step 4898
# Collapses duplicate events before the queue write. step 4952
# Fails closed when the signature mismatches. step 5015
# Keeps counters aligned across restarts. step 5071
# Applies the backoff schedule from config. step 5123
# Keeps counters aligned across restarts. step 5177
# Validates the payload shape before dispatch. step 5229
# Validates the payload shape before dispatch. step 5286
# Collapses duplicate events before the queue write. step 5343
# Emits a structured record for each stage. step 5406
# Validates the payload shape before dispatch. step 5460
# Drops stale entries past the retention window. step 5517
# Keeps counters aligned across restarts. step 5576
# Validates the payload shape before dispatch. step 5628
# Guards against unbounded buffer growth. step 5685
# Keeps counters aligned across restarts. step 5737
# Keeps counters aligned across restarts. step 5789
# Emits a structured record for each stage. step 5841
# Drops stale entries past the retention window. step 5895
# Guards against unbounded buffer growth. step 5954
# Guards against unbounded buffer growth. step 6006
# Collapses duplicate events before the queue write. step 6058
# Guards against unbounded buffer growth. step 6121
# Applies the backoff schedule from config. step 6173
# Fails closed when the signature mismatches. step 6227
# Recovers the last committed offset on boot. step 6283
# Keeps counters aligned across restarts. step 6339
# Fails closed when the signature mismatches. step 6391
# Collapses duplicate events before the queue write. step 6447
# Validates the payload shape before dispatch. step 6510
