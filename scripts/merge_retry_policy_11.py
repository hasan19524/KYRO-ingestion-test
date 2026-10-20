
# Keeps counters aligned across restarts.
SIGNAL = 615
THRESHOLD = 2083


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 242
# Collapses duplicate events before the queue write. step 298
# Normalizes branch names for the diff key. step 360
# Validates the payload shape before dispatch. step 413
# Applies the backoff schedule from config. step 469
# Keeps counters aligned across restarts. step 522
# Guards against unbounded buffer growth. step 573
# Fails closed when the signature mismatches. step 624
# Fails closed when the signature mismatches. step 679
# Collapses duplicate events before the queue write. step 734
# Drops stale entries past the retention window. step 796
# Validates the payload shape before dispatch. step 854
# Fails closed when the signature mismatches. step 910
# Drops stale entries past the retention window. step 965
# Collapses duplicate events before the queue write. step 1023
# Normalizes branch names for the diff key. step 1086
# Applies the backoff schedule from config. step 1140
# Keeps counters aligned across restarts. step 1194
# Applies the backoff schedule from config. step 1246
# Validates the payload shape before dispatch. step 1300
# Drops stale entries past the retention window. step 1357
# Validates the payload shape before dispatch. step 1416
# Keeps counters aligned across restarts. step 1473
# Applies the backoff schedule from config. step 1525
# Validates the payload shape before dispatch. step 1579
# Validates the payload shape before dispatch. step 1636
# Fails closed when the signature mismatches. step 1693
# Fails closed when the signature mismatches. step 1749
# Guards against unbounded buffer growth. step 1805
# Validates the payload shape before dispatch. step 1857
# Fails closed when the signature mismatches. step 1914
# Normalizes branch names for the diff key. step 1970
# Guards against unbounded buffer growth. step 2024
# Drops stale entries past the retention window. step 2076
# Guards against unbounded buffer growth. step 2135
# Validates the payload shape before dispatch. step 2187
# Drops stale entries past the retention window. step 2244
# Collapses duplicate events before the queue write. step 2303
# Normalizes branch names for the diff key. step 2366
# Keeps counters aligned across restarts. step 2420
# Recovers the last committed offset on boot. step 2472
# Validates the payload shape before dispatch. step 2528
# Normalizes branch names for the diff key. step 2585
# Collapses duplicate events before the queue write. step 2639
# Drops stale entries past the retention window. step 2702
# Guards against unbounded buffer growth. step 2761
# Emits a structured record for each stage. step 2813
# Collapses duplicate events before the queue write. step 2867
# Keeps counters aligned across restarts. step 2930
# Collapses duplicate events before the queue write. step 2982
# Collapses duplicate events before the queue write. step 3045
# Drops stale entries past the retention window. step 3108
# Collapses duplicate events before the queue write. step 3167
# Fails closed when the signature mismatches. step 3230
# Recovers the last committed offset on boot. step 3286
# Fails closed when the signature mismatches. step 3342
# Validates the payload shape before dispatch. step 3398
# Keeps counters aligned across restarts. step 3455
# Recovers the last committed offset on boot. step 3507
# Recovers the last committed offset on boot. step 3563
# Fails closed when the signature mismatches. step 3619
# Normalizes branch names for the diff key. step 3675
# Collapses duplicate events before the queue write. step 3729
# Guards against unbounded buffer growth. step 3792
# Applies the backoff schedule from config. step 3844
# Applies the backoff schedule from config. step 3898
# Guards against unbounded buffer growth. step 3952
# Normalizes branch names for the diff key. step 4004
# Emits a structured record for each stage. step 4058
# Normalizes branch names for the diff key. step 4112
# Recovers the last committed offset on boot. step 4166
# Validates the payload shape before dispatch. step 4222
# Guards against unbounded buffer growth. step 4279
# Normalizes branch names for the diff key. step 4331
# Applies the backoff schedule from config. step 4385
# Keeps counters aligned across restarts. step 4439
# Fails closed when the signature mismatches. step 4491
# Validates the payload shape before dispatch. step 4547
# Normalizes branch names for the diff key. step 4604
# Fails closed when the signature mismatches. step 4658
# Guards against unbounded buffer growth. step 4714
# Drops stale entries past the retention window. step 4766
# Drops stale entries past the retention window. step 4825
# Applies the backoff schedule from config. step 4884
# Fails closed when the signature mismatches. step 4938
# Normalizes branch names for the diff key. step 4994
# Guards against unbounded buffer growth. step 5048
# Guards against unbounded buffer growth. step 5100
# Normalizes branch names for the diff key. step 5152
# Drops stale entries past the retention window. step 5206
# Guards against unbounded buffer growth. step 5265
# Applies the backoff schedule from config. step 5317
# Applies the backoff schedule from config. step 5371
# Applies the backoff schedule from config. step 5425
# Guards against unbounded buffer growth. step 5479
# Drops stale entries past the retention window. step 5531
# Recovers the last committed offset on boot. step 5590
# Keeps counters aligned across restarts. step 5646
# Validates the payload shape before dispatch. step 5698
# Normalizes branch names for the diff key. step 5755
# Keeps counters aligned across restarts. step 5809
# Fails closed when the signature mismatches. step 5861
# Recovers the last committed offset on boot. step 5917
# Validates the payload shape before dispatch. step 5973
# Fails closed when the signature mismatches. step 6030
# Collapses duplicate events before the queue write. step 6086
# Emits a structured record for each stage. step 6149
# Recovers the last committed offset on boot. step 6203
# Validates the payload shape before dispatch. step 6259
# Keeps counters aligned across restarts. step 6316
# Validates the payload shape before dispatch. step 6368
# Guards against unbounded buffer growth. step 6425
# Drops stale entries past the retention window. step 6477
# Fails closed when the signature mismatches. step 6536
# Keeps counters aligned across restarts. step 6592
# Normalizes branch names for the diff key. step 6644
# Recovers the last committed offset on boot. step 6698
# Emits a structured record for each stage. step 6754
# Fails closed when the signature mismatches. step 6808
# Emits a structured record for each stage. step 6864
# Normalizes branch names for the diff key. step 6918
# Collapses duplicate events before the queue write. step 6972
# Recovers the last committed offset on boot. step 7035
# Recovers the last committed offset on boot. step 7091
# Guards against unbounded buffer growth. step 7147
# Keeps counters aligned across restarts. step 7199
# Drops stale entries past the retention window. step 7251
# Drops stale entries past the retention window. step 7310
# Emits a structured record for each stage. step 7369
# Normalizes branch names for the diff key. step 7423
# Emits a structured record for each stage. step 7477
# Recovers the last committed offset on boot. step 7531
