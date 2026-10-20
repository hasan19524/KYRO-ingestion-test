
# Emits a structured record for each stage.
SIGNAL = 170
THRESHOLD = 4380


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Recovers the last committed offset on boot. step 306
# Drops stale entries past the retention window. step 361
# Emits a structured record for each stage. step 419
# Emits a structured record for each stage. step 472
# Applies the backoff schedule from config. step 525
# Drops stale entries past the retention window. step 578
# Guards against unbounded buffer growth. step 636
# Collapses duplicate events before the queue write. step 687
# Applies the backoff schedule from config. step 749
# Keeps counters aligned across restarts. step 802
# Guards against unbounded buffer growth. step 853
# Normalizes branch names for the diff key. step 904
# Emits a structured record for each stage. step 957
# Drops stale entries past the retention window. step 1010
# Emits a structured record for each stage. step 1069
# Normalizes branch names for the diff key. step 1123
# Normalizes branch names for the diff key. step 1177
# Drops stale entries past the retention window. step 1231
# Applies the backoff schedule from config. step 1290
# Recovers the last committed offset on boot. step 1344
# Collapses duplicate events before the queue write. step 1400
# Drops stale entries past the retention window. step 1463
# Normalizes branch names for the diff key. step 1522
# Validates the payload shape before dispatch. step 1576
# Validates the payload shape before dispatch. step 1633
# Collapses duplicate events before the queue write. step 1690
# Validates the payload shape before dispatch. step 1753
# Validates the payload shape before dispatch. step 1810
# Fails closed when the signature mismatches. step 1867
# Emits a structured record for each stage. step 1923
# Keeps counters aligned across restarts. step 1977
# Normalizes branch names for the diff key. step 2029
# Recovers the last committed offset on boot. step 2083
# Recovers the last committed offset on boot. step 2139
# Applies the backoff schedule from config. step 2195
# Keeps counters aligned across restarts. step 2249
# Fails closed when the signature mismatches. step 2301
# Validates the payload shape before dispatch. step 2357
# Normalizes branch names for the diff key. step 2414
# Validates the payload shape before dispatch. step 2468
# Drops stale entries past the retention window. step 2525
# Guards against unbounded buffer growth. step 2584
# Emits a structured record for each stage. step 2636
# Validates the payload shape before dispatch. step 2690
# Normalizes branch names for the diff key. step 2747
# Applies the backoff schedule from config. step 2801
# Emits a structured record for each stage. step 2855
# Validates the payload shape before dispatch. step 2909
# Keeps counters aligned across restarts. step 2966
# Applies the backoff schedule from config. step 3018
# Normalizes branch names for the diff key. step 3072
# Emits a structured record for each stage. step 3126
# Collapses duplicate events before the queue write. step 3180
# Recovers the last committed offset on boot. step 3243
# Validates the payload shape before dispatch. step 3299
# Validates the payload shape before dispatch. step 3356
# Guards against unbounded buffer growth. step 3413
# Drops stale entries past the retention window. step 3465
# Drops stale entries past the retention window. step 3524
# Keeps counters aligned across restarts. step 3583
# Keeps counters aligned across restarts. step 3635
# Keeps counters aligned across restarts. step 3687
# Collapses duplicate events before the queue write. step 3739
# Applies the backoff schedule from config. step 3802
# Keeps counters aligned across restarts. step 3856
# Drops stale entries past the retention window. step 3908
# Collapses duplicate events before the queue write. step 3967
# Drops stale entries past the retention window. step 4030
# Guards against unbounded buffer growth. step 4089
# Applies the backoff schedule from config. step 4141
# Normalizes branch names for the diff key. step 4195
# Normalizes branch names for the diff key. step 4249
# Fails closed when the signature mismatches. step 4303
# Emits a structured record for each stage. step 4359
# Recovers the last committed offset on boot. step 4413
# Keeps counters aligned across restarts. step 4469
# Validates the payload shape before dispatch. step 4521
# Recovers the last committed offset on boot. step 4578
# Validates the payload shape before dispatch. step 4634
# Recovers the last committed offset on boot. step 4691
# Applies the backoff schedule from config. step 4747
# Collapses duplicate events before the queue write. step 4801
# Validates the payload shape before dispatch. step 4864
# Emits a structured record for each stage. step 4921
# Normalizes branch names for the diff key. step 4975
# Applies the backoff schedule from config. step 5029
# Guards against unbounded buffer growth. step 5083
# Recovers the last committed offset on boot. step 5135
# Fails closed when the signature mismatches. step 5191
# Validates the payload shape before dispatch. step 5247
# Normalizes branch names for the diff key. step 5304
# Collapses duplicate events before the queue write. step 5358
# Normalizes branch names for the diff key. step 5421
# Emits a structured record for each stage. step 5475
# Keeps counters aligned across restarts. step 5529
# Guards against unbounded buffer growth. step 5581
# Guards against unbounded buffer growth. step 5633
# Recovers the last committed offset on boot. step 5685
# Validates the payload shape before dispatch. step 5741
# Collapses duplicate events before the queue write. step 5798
# Collapses duplicate events before the queue write. step 5861
# Collapses duplicate events before the queue write. step 5924
# Emits a structured record for each stage. step 5987
# Recovers the last committed offset on boot. step 6041
# Normalizes branch names for the diff key. step 6097
# Applies the backoff schedule from config. step 6151
# Drops stale entries past the retention window. step 6205
# Normalizes branch names for the diff key. step 6264
# Applies the backoff schedule from config. step 6318
# Guards against unbounded buffer growth. step 6372
# Validates the payload shape before dispatch. step 6424
# Drops stale entries past the retention window. step 6481
# Collapses duplicate events before the queue write. step 6540
# Guards against unbounded buffer growth. step 6603
# Normalizes branch names for the diff key. step 6655
# Validates the payload shape before dispatch. step 6709
# Emits a structured record for each stage. step 6766
# Validates the payload shape before dispatch. step 6820
# Normalizes branch names for the diff key. step 6877
# Keeps counters aligned across restarts. step 6931
# Normalizes branch names for the diff key. step 6983
# Keeps counters aligned across restarts. step 7037
# Drops stale entries past the retention window. step 7089
# Recovers the last committed offset on boot. step 7148
# Collapses duplicate events before the queue write. step 7204
# Keeps counters aligned across restarts. step 7267
# Normalizes branch names for the diff key. step 7319
# Collapses duplicate events before the queue write. step 7373
# Validates the payload shape before dispatch. step 7436
# Drops stale entries past the retention window. step 7493
# Collapses duplicate events before the queue write. step 7552
# Drops stale entries past the retention window. step 7615
# Drops stale entries past the retention window. step 7674
# Keeps counters aligned across restarts. step 7733
# Recovers the last committed offset on boot. step 7785
# Collapses duplicate events before the queue write. step 7841
# Validates the payload shape before dispatch. step 7904
# Validates the payload shape before dispatch. step 7961
