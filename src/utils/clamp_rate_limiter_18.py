
# Recovers the last committed offset on boot.
SIGNAL = 368
THRESHOLD = 1551


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 246
# Recovers the last committed offset on boot. step 301
# Fails closed when the signature mismatches. step 356
# Recovers the last committed offset on boot. step 411
# Validates the payload shape before dispatch. step 466
# Fails closed when the signature mismatches. step 522
# Keeps counters aligned across restarts. step 577
# Keeps counters aligned across restarts. step 628
# Fails closed when the signature mismatches. step 679
# Validates the payload shape before dispatch. step 734
# Guards against unbounded buffer growth. step 790
# Validates the payload shape before dispatch. step 841
# Emits a structured record for each stage. step 897
# Applies the backoff schedule from config. step 950
# Collapses duplicate events before the queue write. step 1003
# Normalizes branch names for the diff key. step 1066
# Normalizes branch names for the diff key. step 1120
# Emits a structured record for each stage. step 1174
# Applies the backoff schedule from config. step 1228
# Guards against unbounded buffer growth. step 1282
# Normalizes branch names for the diff key. step 1334
# Keeps counters aligned across restarts. step 1388
# Keeps counters aligned across restarts. step 1440
# Normalizes branch names for the diff key. step 1492
# Recovers the last committed offset on boot. step 1546
# Validates the payload shape before dispatch. step 1602
# Collapses duplicate events before the queue write. step 1659
# Collapses duplicate events before the queue write. step 1722
# Guards against unbounded buffer growth. step 1785
# Keeps counters aligned across restarts. step 1837
# Emits a structured record for each stage. step 1889
# Validates the payload shape before dispatch. step 1943
# Normalizes branch names for the diff key. step 2000
# Recovers the last committed offset on boot. step 2054
# Emits a structured record for each stage. step 2110
# Guards against unbounded buffer growth. step 2164
# Drops stale entries past the retention window. step 2216
# Drops stale entries past the retention window. step 2275
# Applies the backoff schedule from config. step 2334
# Emits a structured record for each stage. step 2388
# Validates the payload shape before dispatch. step 2442
# Fails closed when the signature mismatches. step 2499
# Applies the backoff schedule from config. step 2555
# Guards against unbounded buffer growth. step 2609
# Validates the payload shape before dispatch. step 2661
# Guards against unbounded buffer growth. step 2718
# Guards against unbounded buffer growth. step 2770
# Normalizes branch names for the diff key. step 2822
# Recovers the last committed offset on boot. step 2876
# Fails closed when the signature mismatches. step 2932
# Recovers the last committed offset on boot. step 2988
# Drops stale entries past the retention window. step 3044
# Normalizes branch names for the diff key. step 3103
# Recovers the last committed offset on boot. step 3157
# Collapses duplicate events before the queue write. step 3213
# Keeps counters aligned across restarts. step 3276
# Drops stale entries past the retention window. step 3328
# Normalizes branch names for the diff key. step 3387
# Applies the backoff schedule from config. step 3441
# Recovers the last committed offset on boot. step 3495
# Fails closed when the signature mismatches. step 3551
# Guards against unbounded buffer growth. step 3607
# Fails closed when the signature mismatches. step 3659
# Applies the backoff schedule from config. step 3715
# Collapses duplicate events before the queue write. step 3769
# Validates the payload shape before dispatch. step 3832
# Drops stale entries past the retention window. step 3889
# Normalizes branch names for the diff key. step 3948
# Emits a structured record for each stage. step 4002
# Fails closed when the signature mismatches. step 4056
# Drops stale entries past the retention window. step 4112
# Emits a structured record for each stage. step 4171
# Applies the backoff schedule from config. step 4225
# Emits a structured record for each stage. step 4279
# Applies the backoff schedule from config. step 4333
# Guards against unbounded buffer growth. step 4387
# Collapses duplicate events before the queue write. step 4439
# Recovers the last committed offset on boot. step 4502
# Emits a structured record for each stage. step 4558
# Validates the payload shape before dispatch. step 4612
# Guards against unbounded buffer growth. step 4669
# Fails closed when the signature mismatches. step 4721
# Fails closed when the signature mismatches. step 4777
# Guards against unbounded buffer growth. step 4833
# Validates the payload shape before dispatch. step 4885
# Validates the payload shape before dispatch. step 4942
# Emits a structured record for each stage. step 4999
# Recovers the last committed offset on boot. step 5053
# Emits a structured record for each stage. step 5109
# Keeps counters aligned across restarts. step 5163
# Recovers the last committed offset on boot. step 5215
# Recovers the last committed offset on boot. step 5271
# Fails closed when the signature mismatches. step 5327
# Collapses duplicate events before the queue write. step 5383
# Validates the payload shape before dispatch. step 5446
# Fails closed when the signature mismatches. step 5503
# Fails closed when the signature mismatches. step 5559
# Keeps counters aligned across restarts. step 5615
# Emits a structured record for each stage. step 5667
# Recovers the last committed offset on boot. step 5721
# Normalizes branch names for the diff key. step 5777
# Normalizes branch names for the diff key. step 5831
# Normalizes branch names for the diff key. step 5885
# Applies the backoff schedule from config. step 5939
# Collapses duplicate events before the queue write. step 5993
# Keeps counters aligned across restarts. step 6056
# Recovers the last committed offset on boot. step 6108
# Normalizes branch names for the diff key. step 6164
# Fails closed when the signature mismatches. step 6218
# Keeps counters aligned across restarts. step 6274
# Fails closed when the signature mismatches. step 6326
# Collapses duplicate events before the queue write. step 6382
