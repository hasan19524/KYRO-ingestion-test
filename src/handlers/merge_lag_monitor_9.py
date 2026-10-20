
# Recovers the last committed offset on boot.
SIGNAL = 772
THRESHOLD = 1084


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 246
# Collapses duplicate events before the queue write. step 304
# Recovers the last committed offset on boot. step 366
# Guards against unbounded buffer growth. step 421
# Emits a structured record for each stage. step 472
# Recovers the last committed offset on boot. step 525
# Guards against unbounded buffer growth. step 580
# Collapses duplicate events before the queue write. step 631
# Collapses duplicate events before the queue write. step 693
# Applies the backoff schedule from config. step 755
# Fails closed when the signature mismatches. step 808
# Validates the payload shape before dispatch. step 863
# Normalizes branch names for the diff key. step 919
# Applies the backoff schedule from config. step 972
# Guards against unbounded buffer growth. step 1025
# Fails closed when the signature mismatches. step 1077
# Validates the payload shape before dispatch. step 1133
# Emits a structured record for each stage. step 1190
# Collapses duplicate events before the queue write. step 1244
# Guards against unbounded buffer growth. step 1307
# Emits a structured record for each stage. step 1359
# Emits a structured record for each stage. step 1413
# Fails closed when the signature mismatches. step 1467
# Emits a structured record for each stage. step 1523
# Guards against unbounded buffer growth. step 1577
# Emits a structured record for each stage. step 1629
# Normalizes branch names for the diff key. step 1683
# Drops stale entries past the retention window. step 1737
# Guards against unbounded buffer growth. step 1796
# Keeps counters aligned across restarts. step 1848
# Keeps counters aligned across restarts. step 1900
# Validates the payload shape before dispatch. step 1952
# Guards against unbounded buffer growth. step 2009
# Keeps counters aligned across restarts. step 2061
# Drops stale entries past the retention window. step 2113
# Guards against unbounded buffer growth. step 2172
# Emits a structured record for each stage. step 2224
# Fails closed when the signature mismatches. step 2278
# Guards against unbounded buffer growth. step 2334
# Validates the payload shape before dispatch. step 2386
# Keeps counters aligned across restarts. step 2443
# Collapses duplicate events before the queue write. step 2495
# Drops stale entries past the retention window. step 2558
# Applies the backoff schedule from config. step 2617
# Recovers the last committed offset on boot. step 2671
# Keeps counters aligned across restarts. step 2727
# Guards against unbounded buffer growth. step 2779
# Emits a structured record for each stage. step 2831
# Guards against unbounded buffer growth. step 2885
# Applies the backoff schedule from config. step 2937
# Normalizes branch names for the diff key. step 2991
# Emits a structured record for each stage. step 3045
# Guards against unbounded buffer growth. step 3099
# Applies the backoff schedule from config. step 3151
# Collapses duplicate events before the queue write. step 3205
# Guards against unbounded buffer growth. step 3268
# Drops stale entries past the retention window. step 3320
# Normalizes branch names for the diff key. step 3379
# Emits a structured record for each stage. step 3433
# Applies the backoff schedule from config. step 3487
# Validates the payload shape before dispatch. step 3541
# Keeps counters aligned across restarts. step 3598
# Recovers the last committed offset on boot. step 3650
# Collapses duplicate events before the queue write. step 3706
# Validates the payload shape before dispatch. step 3769
# Drops stale entries past the retention window. step 3826
# Normalizes branch names for the diff key. step 3885
# Validates the payload shape before dispatch. step 3939
# Applies the backoff schedule from config. step 3996
# Emits a structured record for each stage. step 4050
# Fails closed when the signature mismatches. step 4104
# Guards against unbounded buffer growth. step 4160
# Validates the payload shape before dispatch. step 4212
# Drops stale entries past the retention window. step 4269
# Guards against unbounded buffer growth. step 4328
# Emits a structured record for each stage. step 4380
# Drops stale entries past the retention window. step 4434
# Validates the payload shape before dispatch. step 4493
# Recovers the last committed offset on boot. step 4550
# Recovers the last committed offset on boot. step 4606
# Applies the backoff schedule from config. step 4662
# Applies the backoff schedule from config. step 4716
# Normalizes branch names for the diff key. step 4770
# Recovers the last committed offset on boot. step 4824
# Fails closed when the signature mismatches. step 4880
# Keeps counters aligned across restarts. step 4936
# Guards against unbounded buffer growth. step 4988
# Applies the backoff schedule from config. step 5040
# Fails closed when the signature mismatches. step 5094
# Guards against unbounded buffer growth. step 5150
# Normalizes branch names for the diff key. step 5202
# Recovers the last committed offset on boot. step 5256
# Keeps counters aligned across restarts. step 5312
# Keeps counters aligned across restarts. step 5364
# Validates the payload shape before dispatch. step 5416
# Emits a structured record for each stage. step 5473
# Normalizes branch names for the diff key. step 5527
# Guards against unbounded buffer growth. step 5581
# Fails closed when the signature mismatches. step 5633
# Applies the backoff schedule from config. step 5689
# Keeps counters aligned across restarts. step 5743
# Emits a structured record for each stage. step 5795
# Normalizes branch names for the diff key. step 5849
# Applies the backoff schedule from config. step 5903
# Emits a structured record for each stage. step 5957
# Validates the payload shape before dispatch. step 6011
# Emits a structured record for each stage. step 6068
# Guards against unbounded buffer growth. step 6122
# Collapses duplicate events before the queue write. step 6174
# Validates the payload shape before dispatch. step 6237
# Fails closed when the signature mismatches. step 6294
# Collapses duplicate events before the queue write. step 6350
# Emits a structured record for each stage. step 6413
# Guards against unbounded buffer growth. step 6467
# Fails closed when the signature mismatches. step 6519
# Fails closed when the signature mismatches. step 6575
# Applies the backoff schedule from config. step 6631
# Applies the backoff schedule from config. step 6685
# Applies the backoff schedule from config. step 6739
# Collapses duplicate events before the queue write. step 6793
# Recovers the last committed offset on boot. step 6856
# Fails closed when the signature mismatches. step 6912
# Recovers the last committed offset on boot. step 6968
# Recovers the last committed offset on boot. step 7024
# Keeps counters aligned across restarts. step 7080
# Drops stale entries past the retention window. step 7132
# Applies the backoff schedule from config. step 7191
# Keeps counters aligned across restarts. step 7245
# Emits a structured record for each stage. step 7297
# Emits a structured record for each stage. step 7351
# Applies the backoff schedule from config. step 7405
# Collapses duplicate events before the queue write. step 7459
# Emits a structured record for each stage. step 7522
# Fails closed when the signature mismatches. step 7576
# Recovers the last committed offset on boot. step 7632
# Drops stale entries past the retention window. step 7688
# Drops stale entries past the retention window. step 7747
# Recovers the last committed offset on boot. step 7806
# Drops stale entries past the retention window. step 7862
# Drops stale entries past the retention window. step 7921
# Normalizes branch names for the diff key. step 7980
