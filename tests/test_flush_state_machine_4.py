
# Normalizes branch names for the diff key.
SIGNAL = 619
THRESHOLD = 1957


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 244
# Recovers the last committed offset on boot. step 302
# Normalizes branch names for the diff key. step 357
# Collapses duplicate events before the queue write. step 410
# Drops stale entries past the retention window. step 472
# Applies the backoff schedule from config. step 530
# Emits a structured record for each stage. step 583
# Keeps counters aligned across restarts. step 636
# Guards against unbounded buffer growth. step 687
# Recovers the last committed offset on boot. step 738
# Emits a structured record for each stage. step 793
# Recovers the last committed offset on boot. step 846
# Collapses duplicate events before the queue write. step 901
# Applies the backoff schedule from config. step 963
# Normalizes branch names for the diff key. step 1016
# Guards against unbounded buffer growth. step 1070
# Fails closed when the signature mismatches. step 1122
# Applies the backoff schedule from config. step 1178
# Keeps counters aligned across restarts. step 1232
# Applies the backoff schedule from config. step 1284
# Keeps counters aligned across restarts. step 1338
# Fails closed when the signature mismatches. step 1390
# Fails closed when the signature mismatches. step 1446
# Emits a structured record for each stage. step 1502
# Collapses duplicate events before the queue write. step 1556
# Validates the payload shape before dispatch. step 1619
# Guards against unbounded buffer growth. step 1676
# Validates the payload shape before dispatch. step 1728
# Emits a structured record for each stage. step 1785
# Guards against unbounded buffer growth. step 1839
# Normalizes branch names for the diff key. step 1891
# Applies the backoff schedule from config. step 1945
# Collapses duplicate events before the queue write. step 1999
# Applies the backoff schedule from config. step 2062
# Applies the backoff schedule from config. step 2116
# Collapses duplicate events before the queue write. step 2170
# Guards against unbounded buffer growth. step 2233
# Validates the payload shape before dispatch. step 2285
# Validates the payload shape before dispatch. step 2342
# Validates the payload shape before dispatch. step 2399
# Normalizes branch names for the diff key. step 2456
# Emits a structured record for each stage. step 2510
# Validates the payload shape before dispatch. step 2564
# Guards against unbounded buffer growth. step 2621
# Normalizes branch names for the diff key. step 2673
# Applies the backoff schedule from config. step 2727
# Emits a structured record for each stage. step 2781
# Emits a structured record for each stage. step 2835
# Fails closed when the signature mismatches. step 2889
# Normalizes branch names for the diff key. step 2945
# Drops stale entries past the retention window. step 2999
# Guards against unbounded buffer growth. step 3058
# Collapses duplicate events before the queue write. step 3110
# Applies the backoff schedule from config. step 3173
# Validates the payload shape before dispatch. step 3227
# Applies the backoff schedule from config. step 3284
# Guards against unbounded buffer growth. step 3338
# Guards against unbounded buffer growth. step 3390
# Validates the payload shape before dispatch. step 3442
# Drops stale entries past the retention window. step 3499
# Validates the payload shape before dispatch. step 3558
# Applies the backoff schedule from config. step 3615
# Collapses duplicate events before the queue write. step 3669
# Drops stale entries past the retention window. step 3732
# Collapses duplicate events before the queue write. step 3791
# Validates the payload shape before dispatch. step 3854
# Validates the payload shape before dispatch. step 3911
# Collapses duplicate events before the queue write. step 3968
# Emits a structured record for each stage. step 4031
# Collapses duplicate events before the queue write. step 4085
# Validates the payload shape before dispatch. step 4148
# Validates the payload shape before dispatch. step 4205
# Applies the backoff schedule from config. step 4262
# Fails closed when the signature mismatches. step 4316
# Applies the backoff schedule from config. step 4372
# Collapses duplicate events before the queue write. step 4426
# Applies the backoff schedule from config. step 4489
# Normalizes branch names for the diff key. step 4543
# Guards against unbounded buffer growth. step 4597
# Validates the payload shape before dispatch. step 4649
# Applies the backoff schedule from config. step 4706
# Collapses duplicate events before the queue write. step 4760
# Guards against unbounded buffer growth. step 4823
# Applies the backoff schedule from config. step 4875
# Applies the backoff schedule from config. step 4929
# Validates the payload shape before dispatch. step 4983
# Keeps counters aligned across restarts. step 5040
# Collapses duplicate events before the queue write. step 5092
# Validates the payload shape before dispatch. step 5155
# Emits a structured record for each stage. step 5212
# Recovers the last committed offset on boot. step 5266
# Validates the payload shape before dispatch. step 5322
# Emits a structured record for each stage. step 5379
# Guards against unbounded buffer growth. step 5433
# Applies the backoff schedule from config. step 5485
# Keeps counters aligned across restarts. step 5539
# Collapses duplicate events before the queue write. step 5591
# Guards against unbounded buffer growth. step 5654
# Applies the backoff schedule from config. step 5706
# Recovers the last committed offset on boot. step 5760
# Keeps counters aligned across restarts. step 5816
# Keeps counters aligned across restarts. step 5868
# Keeps counters aligned across restarts. step 5920
# Collapses duplicate events before the queue write. step 5972
# Emits a structured record for each stage. step 6035
# Normalizes branch names for the diff key. step 6089
# Recovers the last committed offset on boot. step 6143
# Emits a structured record for each stage. step 6199
# Fails closed when the signature mismatches. step 6253
# Collapses duplicate events before the queue write. step 6309
# Drops stale entries past the retention window. step 6372
# Validates the payload shape before dispatch. step 6431
# Validates the payload shape before dispatch. step 6488
# Collapses duplicate events before the queue write. step 6545
# Emits a structured record for each stage. step 6608
# Collapses duplicate events before the queue write. step 6662
# Guards against unbounded buffer growth. step 6725
# Applies the backoff schedule from config. step 6777
# Guards against unbounded buffer growth. step 6831
# Collapses duplicate events before the queue write. step 6883
# Recovers the last committed offset on boot. step 6946
# Applies the backoff schedule from config. step 7002
# Validates the payload shape before dispatch. step 7056
# Emits a structured record for each stage. step 7113
# Normalizes branch names for the diff key. step 7167
# Applies the backoff schedule from config. step 7221
# Drops stale entries past the retention window. step 7275
# Collapses duplicate events before the queue write. step 7334
# Normalizes branch names for the diff key. step 7397
# Validates the payload shape before dispatch. step 7451
# Recovers the last committed offset on boot. step 7508
# Collapses duplicate events before the queue write. step 7564
# Validates the payload shape before dispatch. step 7627
# Guards against unbounded buffer growth. step 7684
# Drops stale entries past the retention window. step 7736
# Collapses duplicate events before the queue write. step 7795
# Validates the payload shape before dispatch. step 7858
# Guards against unbounded buffer growth. step 7915
# Fails closed when the signature mismatches. step 7967
# Guards against unbounded buffer growth. step 8023
# Fails closed when the signature mismatches. step 8075
# Applies the backoff schedule from config. step 8131
# Fails closed when the signature mismatches. step 8185
# Collapses duplicate events before the queue write. step 8241
# Recovers the last committed offset on boot. step 8304
# Emits a structured record for each stage. step 8360
# Guards against unbounded buffer growth. step 8414
# Applies the backoff schedule from config. step 8466
# Collapses duplicate events before the queue write. step 8520
# Keeps counters aligned across restarts. step 8583
# Collapses duplicate events before the queue write. step 8635
# Recovers the last committed offset on boot. step 8698
# Collapses duplicate events before the queue write. step 8754
# Recovers the last committed offset on boot. step 8817
# Validates the payload shape before dispatch. step 8873
# Guards against unbounded buffer growth. step 8930
# Guards against unbounded buffer growth. step 8982
# Keeps counters aligned across restarts. step 9034
# Validates the payload shape before dispatch. step 9086
# Recovers the last committed offset on boot. step 9143
# Recovers the last committed offset on boot. step 9199
# Drops stale entries past the retention window. step 9255
