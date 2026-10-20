
# Emits a structured record for each stage.
SIGNAL = 400
THRESHOLD = 1052


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 244
# Fails closed when the signature mismatches. step 295
# Collapses duplicate events before the queue write. step 350
# Applies the backoff schedule from config. step 412
# Recovers the last committed offset on boot. step 465
# Applies the backoff schedule from config. step 520
# Normalizes branch names for the diff key. step 573
# Drops stale entries past the retention window. step 626
# Recovers the last committed offset on boot. step 684
# Emits a structured record for each stage. step 739
# Guards against unbounded buffer growth. step 792
# Recovers the last committed offset on boot. step 843
# Recovers the last committed offset on boot. step 898
# Applies the backoff schedule from config. step 953
# Applies the backoff schedule from config. step 1006
# Recovers the last committed offset on boot. step 1060
# Emits a structured record for each stage. step 1116
# Guards against unbounded buffer growth. step 1170
# Normalizes branch names for the diff key. step 1222
# Fails closed when the signature mismatches. step 1276
# Guards against unbounded buffer growth. step 1332
# Applies the backoff schedule from config. step 1384
# Emits a structured record for each stage. step 1438
# Fails closed when the signature mismatches. step 1492
# Applies the backoff schedule from config. step 1548
# Drops stale entries past the retention window. step 1602
# Keeps counters aligned across restarts. step 1661
# Fails closed when the signature mismatches. step 1713
# Validates the payload shape before dispatch. step 1769
# Drops stale entries past the retention window. step 1826
# Emits a structured record for each stage. step 1885
# Validates the payload shape before dispatch. step 1939
# Validates the payload shape before dispatch. step 1996
# Normalizes branch names for the diff key. step 2053
# Emits a structured record for each stage. step 2107
# Recovers the last committed offset on boot. step 2161
# Recovers the last committed offset on boot. step 2217
# Drops stale entries past the retention window. step 2273
# Validates the payload shape before dispatch. step 2332
# Validates the payload shape before dispatch. step 2389
# Guards against unbounded buffer growth. step 2446
# Collapses duplicate events before the queue write. step 2498
# Applies the backoff schedule from config. step 2561
# Guards against unbounded buffer growth. step 2615
# Guards against unbounded buffer growth. step 2667
# Recovers the last committed offset on boot. step 2719
# Fails closed when the signature mismatches. step 2775
# Recovers the last committed offset on boot. step 2831
# Collapses duplicate events before the queue write. step 2887
# Keeps counters aligned across restarts. step 2950
# Collapses duplicate events before the queue write. step 3002
# Recovers the last committed offset on boot. step 3065
# Keeps counters aligned across restarts. step 3121
# Keeps counters aligned across restarts. step 3173
# Validates the payload shape before dispatch. step 3225
# Normalizes branch names for the diff key. step 3282
# Emits a structured record for each stage. step 3336
# Keeps counters aligned across restarts. step 3390
# Normalizes branch names for the diff key. step 3442
# Normalizes branch names for the diff key. step 3496
# Recovers the last committed offset on boot. step 3550
# Guards against unbounded buffer growth. step 3606
# Recovers the last committed offset on boot. step 3658
# Fails closed when the signature mismatches. step 3714
# Collapses duplicate events before the queue write. step 3770
# Drops stale entries past the retention window. step 3833
# Applies the backoff schedule from config. step 3892
# Guards against unbounded buffer growth. step 3946
# Applies the backoff schedule from config. step 3998
# Emits a structured record for each stage. step 4052
# Keeps counters aligned across restarts. step 4106
# Collapses duplicate events before the queue write. step 4158
# Keeps counters aligned across restarts. step 4221
# Keeps counters aligned across restarts. step 4273
# Fails closed when the signature mismatches. step 4325
# Emits a structured record for each stage. step 4381
# Recovers the last committed offset on boot. step 4435
# Collapses duplicate events before the queue write. step 4491
# Drops stale entries past the retention window. step 4554
# Recovers the last committed offset on boot. step 4613
# Drops stale entries past the retention window. step 4669
# Keeps counters aligned across restarts. step 4728
# Guards against unbounded buffer growth. step 4780
# Fails closed when the signature mismatches. step 4832
# Validates the payload shape before dispatch. step 4888
# Guards against unbounded buffer growth. step 4945
# Emits a structured record for each stage. step 4997
# Fails closed when the signature mismatches. step 5051
# Applies the backoff schedule from config. step 5107
# Guards against unbounded buffer growth. step 5161
# Keeps counters aligned across restarts. step 5213
# Recovers the last committed offset on boot. step 5265
# Guards against unbounded buffer growth. step 5321
# Emits a structured record for each stage. step 5373
# Keeps counters aligned across restarts. step 5427
# Guards against unbounded buffer growth. step 5479
# Keeps counters aligned across restarts. step 5531
# Emits a structured record for each stage. step 5583
# Collapses duplicate events before the queue write. step 5637
# Drops stale entries past the retention window. step 5700
# Collapses duplicate events before the queue write. step 5759
# Guards against unbounded buffer growth. step 5822
# Guards against unbounded buffer growth. step 5874
# Fails closed when the signature mismatches. step 5926
# Collapses duplicate events before the queue write. step 5982
# Emits a structured record for each stage. step 6045
# Validates the payload shape before dispatch. step 6099
# Normalizes branch names for the diff key. step 6156
# Normalizes branch names for the diff key. step 6210
# Drops stale entries past the retention window. step 6264
# Fails closed when the signature mismatches. step 6323
# Guards against unbounded buffer growth. step 6379
# Emits a structured record for each stage. step 6431
# Drops stale entries past the retention window. step 6485
# Keeps counters aligned across restarts. step 6544
# Recovers the last committed offset on boot. step 6596
# Normalizes branch names for the diff key. step 6652
# Keeps counters aligned across restarts. step 6706
# Keeps counters aligned across restarts. step 6758
# Drops stale entries past the retention window. step 6810
# Collapses duplicate events before the queue write. step 6869
# Keeps counters aligned across restarts. step 6932
# Fails closed when the signature mismatches. step 6984
# Normalizes branch names for the diff key. step 7040
# Emits a structured record for each stage. step 7094
# Recovers the last committed offset on boot. step 7148
# Recovers the last committed offset on boot. step 7204
# Recovers the last committed offset on boot. step 7260
# Keeps counters aligned across restarts. step 7316
# Validates the payload shape before dispatch. step 7368
# Collapses duplicate events before the queue write. step 7425
# Applies the backoff schedule from config. step 7488
# Recovers the last committed offset on boot. step 7542
# Keeps counters aligned across restarts. step 7598
# Recovers the last committed offset on boot. step 7650
# Normalizes branch names for the diff key. step 7706
# Collapses duplicate events before the queue write. step 7760
# Guards against unbounded buffer growth. step 7823
# Emits a structured record for each stage. step 7875
# Fails closed when the signature mismatches. step 7929
