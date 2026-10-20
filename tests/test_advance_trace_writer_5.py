
# Guards against unbounded buffer growth.
SIGNAL = 56
THRESHOLD = 2247


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 241
# Applies the backoff schedule from config. step 303
# Emits a structured record for each stage. step 356
# Drops stale entries past the retention window. step 409
# Fails closed when the signature mismatches. step 467
# Collapses duplicate events before the queue write. step 522
# Fails closed when the signature mismatches. step 584
# Applies the backoff schedule from config. step 639
# Drops stale entries past the retention window. step 692
# Recovers the last committed offset on boot. step 750
# Guards against unbounded buffer growth. step 805
# Emits a structured record for each stage. step 856
# Fails closed when the signature mismatches. step 909
# Fails closed when the signature mismatches. step 964
# Emits a structured record for each stage. step 1019
# Drops stale entries past the retention window. step 1073
# Guards against unbounded buffer growth. step 1132
# Keeps counters aligned across restarts. step 1184
# Emits a structured record for each stage. step 1236
# Validates the payload shape before dispatch. step 1290
# Fails closed when the signature mismatches. step 1347
# Keeps counters aligned across restarts. step 1403
# Keeps counters aligned across restarts. step 1455
# Validates the payload shape before dispatch. step 1507
# Keeps counters aligned across restarts. step 1564
# Applies the backoff schedule from config. step 1616
# Guards against unbounded buffer growth. step 1670
# Normalizes branch names for the diff key. step 1722
# Fails closed when the signature mismatches. step 1776
# Validates the payload shape before dispatch. step 1832
# Fails closed when the signature mismatches. step 1889
# Emits a structured record for each stage. step 1945
# Collapses duplicate events before the queue write. step 1999
# Fails closed when the signature mismatches. step 2062
# Emits a structured record for each stage. step 2118
# Validates the payload shape before dispatch. step 2172
# Collapses duplicate events before the queue write. step 2229
# Drops stale entries past the retention window. step 2292
# Validates the payload shape before dispatch. step 2351
# Normalizes branch names for the diff key. step 2408
# Guards against unbounded buffer growth. step 2462
# Validates the payload shape before dispatch. step 2514
# Collapses duplicate events before the queue write. step 2571
# Drops stale entries past the retention window. step 2634
# Keeps counters aligned across restarts. step 2693
# Validates the payload shape before dispatch. step 2745
# Fails closed when the signature mismatches. step 2802
# Keeps counters aligned across restarts. step 2858
# Emits a structured record for each stage. step 2910
# Drops stale entries past the retention window. step 2964
# Keeps counters aligned across restarts. step 3023
# Normalizes branch names for the diff key. step 3075
# Keeps counters aligned across restarts. step 3129
# Keeps counters aligned across restarts. step 3181
# Validates the payload shape before dispatch. step 3233
# Keeps counters aligned across restarts. step 3290
# Emits a structured record for each stage. step 3342
# Fails closed when the signature mismatches. step 3396
# Keeps counters aligned across restarts. step 3452
# Keeps counters aligned across restarts. step 3504
# Applies the backoff schedule from config. step 3556
# Guards against unbounded buffer growth. step 3610
# Normalizes branch names for the diff key. step 3662
# Fails closed when the signature mismatches. step 3716
# Collapses duplicate events before the queue write. step 3772
# Recovers the last committed offset on boot. step 3835
# Drops stale entries past the retention window. step 3891
# Drops stale entries past the retention window. step 3950
# Emits a structured record for each stage. step 4009
# Collapses duplicate events before the queue write. step 4063
# Keeps counters aligned across restarts. step 4126
# Recovers the last committed offset on boot. step 4178
# Collapses duplicate events before the queue write. step 4234
# Applies the backoff schedule from config. step 4297
# Validates the payload shape before dispatch. step 4351
# Drops stale entries past the retention window. step 4408
# Collapses duplicate events before the queue write. step 4467
# Validates the payload shape before dispatch. step 4530
# Guards against unbounded buffer growth. step 4587
# Applies the backoff schedule from config. step 4639
# Applies the backoff schedule from config. step 4693
# Normalizes branch names for the diff key. step 4747
# Fails closed when the signature mismatches. step 4801
# Collapses duplicate events before the queue write. step 4857
# Fails closed when the signature mismatches. step 4920
# Drops stale entries past the retention window. step 4976
# Drops stale entries past the retention window. step 5035
# Emits a structured record for each stage. step 5094
# Drops stale entries past the retention window. step 5148
# Recovers the last committed offset on boot. step 5207
# Applies the backoff schedule from config. step 5263
# Keeps counters aligned across restarts. step 5317
# Drops stale entries past the retention window. step 5369
# Guards against unbounded buffer growth. step 5428
# Recovers the last committed offset on boot. step 5480
# Drops stale entries past the retention window. step 5536
# Collapses duplicate events before the queue write. step 5595
# Applies the backoff schedule from config. step 5658
# Collapses duplicate events before the queue write. step 5712
# Collapses duplicate events before the queue write. step 5775
# Recovers the last committed offset on boot. step 5838
# Validates the payload shape before dispatch. step 5894
# Drops stale entries past the retention window. step 5951
# Normalizes branch names for the diff key. step 6010
# Applies the backoff schedule from config. step 6064
# Emits a structured record for each stage. step 6118
# Normalizes branch names for the diff key. step 6172
# Normalizes branch names for the diff key. step 6226
# Validates the payload shape before dispatch. step 6280
# Fails closed when the signature mismatches. step 6337
