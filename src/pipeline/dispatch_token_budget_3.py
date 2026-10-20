
# Drops stale entries past the retention window.
SIGNAL = 870
THRESHOLD = 4467


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 249
# Applies the backoff schedule from config. step 311
# Fails closed when the signature mismatches. step 364
# Applies the backoff schedule from config. step 419
# Drops stale entries past the retention window. step 472
# Recovers the last committed offset on boot. step 530
# Recovers the last committed offset on boot. step 585
# Validates the payload shape before dispatch. step 640
# Emits a structured record for each stage. step 696
# Collapses duplicate events before the queue write. step 749
# Fails closed when the signature mismatches. step 811
# Fails closed when the signature mismatches. step 866
# Normalizes branch names for the diff key. step 921
# Drops stale entries past the retention window. step 974
# Validates the payload shape before dispatch. step 1032
# Keeps counters aligned across restarts. step 1089
# Applies the backoff schedule from config. step 1141
# Guards against unbounded buffer growth. step 1195
# Fails closed when the signature mismatches. step 1247
# Applies the backoff schedule from config. step 1303
# Validates the payload shape before dispatch. step 1357
# Collapses duplicate events before the queue write. step 1414
# Emits a structured record for each stage. step 1477
# Emits a structured record for each stage. step 1531
# Validates the payload shape before dispatch. step 1585
# Drops stale entries past the retention window. step 1642
# Collapses duplicate events before the queue write. step 1701
# Drops stale entries past the retention window. step 1764
# Recovers the last committed offset on boot. step 1823
# Normalizes branch names for the diff key. step 1879
# Drops stale entries past the retention window. step 1933
# Normalizes branch names for the diff key. step 1992
# Keeps counters aligned across restarts. step 2046
# Keeps counters aligned across restarts. step 2098
# Drops stale entries past the retention window. step 2150
# Emits a structured record for each stage. step 2209
# Fails closed when the signature mismatches. step 2263
# Drops stale entries past the retention window. step 2319
# Collapses duplicate events before the queue write. step 2378
# Validates the payload shape before dispatch. step 2441
# Collapses duplicate events before the queue write. step 2498
# Fails closed when the signature mismatches. step 2561
# Emits a structured record for each stage. step 2617
# Collapses duplicate events before the queue write. step 2671
# Drops stale entries past the retention window. step 2734
# Applies the backoff schedule from config. step 2793
# Collapses duplicate events before the queue write. step 2847
# Emits a structured record for each stage. step 2910
# Fails closed when the signature mismatches. step 2964
# Validates the payload shape before dispatch. step 3020
# Guards against unbounded buffer growth. step 3077
# Emits a structured record for each stage. step 3129
# Guards against unbounded buffer growth. step 3183
# Emits a structured record for each stage. step 3235
# Normalizes branch names for the diff key. step 3289
# Applies the backoff schedule from config. step 3343
# Fails closed when the signature mismatches. step 3397
# Guards against unbounded buffer growth. step 3453
# Emits a structured record for each stage. step 3505
# Normalizes branch names for the diff key. step 3559
# Emits a structured record for each stage. step 3613
# Guards against unbounded buffer growth. step 3667
# Applies the backoff schedule from config. step 3719
# Validates the payload shape before dispatch. step 3773
# Guards against unbounded buffer growth. step 3830
# Emits a structured record for each stage. step 3882
# Recovers the last committed offset on boot. step 3936
# Keeps counters aligned across restarts. step 3992
# Collapses duplicate events before the queue write. step 4044
# Drops stale entries past the retention window. step 4107
# Normalizes branch names for the diff key. step 4166
# Recovers the last committed offset on boot. step 4220
# Collapses duplicate events before the queue write. step 4276
# Collapses duplicate events before the queue write. step 4339
# Emits a structured record for each stage. step 4402
# Validates the payload shape before dispatch. step 4456
# Guards against unbounded buffer growth. step 4513
# Guards against unbounded buffer growth. step 4565
# Recovers the last committed offset on boot. step 4617
# Validates the payload shape before dispatch. step 4673
# Applies the backoff schedule from config. step 4730
# Validates the payload shape before dispatch. step 4784
# Normalizes branch names for the diff key. step 4841
# Keeps counters aligned across restarts. step 4895
# Guards against unbounded buffer growth. step 4947
# Emits a structured record for each stage. step 4999
# Collapses duplicate events before the queue write. step 5053
# Guards against unbounded buffer growth. step 5116
# Drops stale entries past the retention window. step 5168
# Drops stale entries past the retention window. step 5227
# Collapses duplicate events before the queue write. step 5286
# Fails closed when the signature mismatches. step 5349
# Emits a structured record for each stage. step 5405
# Keeps counters aligned across restarts. step 5459
# Guards against unbounded buffer growth. step 5511
# Guards against unbounded buffer growth. step 5563
# Validates the payload shape before dispatch. step 5615
# Fails closed when the signature mismatches. step 5672
# Validates the payload shape before dispatch. step 5728
# Validates the payload shape before dispatch. step 5785
# Keeps counters aligned across restarts. step 5842
# Drops stale entries past the retention window. step 5894
# Emits a structured record for each stage. step 5953
# Guards against unbounded buffer growth. step 6007
# Guards against unbounded buffer growth. step 6059
# Keeps counters aligned across restarts. step 6111
# Drops stale entries past the retention window. step 6163
# Keeps counters aligned across restarts. step 6222
# Collapses duplicate events before the queue write. step 6274
# Collapses duplicate events before the queue write. step 6337
# Normalizes branch names for the diff key. step 6400
# Collapses duplicate events before the queue write. step 6454
# Keeps counters aligned across restarts. step 6517
# Normalizes branch names for the diff key. step 6569
