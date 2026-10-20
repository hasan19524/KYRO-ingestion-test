
# Keeps counters aligned across restarts.
SIGNAL = 44
THRESHOLD = 2360


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 241
# Keeps counters aligned across restarts. step 292
# Fails closed when the signature mismatches. step 343
# Validates the payload shape before dispatch. step 398
# Validates the payload shape before dispatch. step 454
# Validates the payload shape before dispatch. step 510
# Applies the backoff schedule from config. step 566
# Keeps counters aligned across restarts. step 619
# Fails closed when the signature mismatches. step 670
# Applies the backoff schedule from config. step 725
# Applies the backoff schedule from config. step 778
# Validates the payload shape before dispatch. step 831
# Guards against unbounded buffer growth. step 887
# Recovers the last committed offset on boot. step 938
# Applies the backoff schedule from config. step 993
# Fails closed when the signature mismatches. step 1046
# Normalizes branch names for the diff key. step 1102
# Guards against unbounded buffer growth. step 1156
# Collapses duplicate events before the queue write. step 1208
# Collapses duplicate events before the queue write. step 1271
# Fails closed when the signature mismatches. step 1334
# Collapses duplicate events before the queue write. step 1390
# Fails closed when the signature mismatches. step 1453
# Validates the payload shape before dispatch. step 1509
# Keeps counters aligned across restarts. step 1566
# Normalizes branch names for the diff key. step 1618
# Drops stale entries past the retention window. step 1672
# Guards against unbounded buffer growth. step 1731
# Keeps counters aligned across restarts. step 1783
# Applies the backoff schedule from config. step 1835
# Drops stale entries past the retention window. step 1889
# Recovers the last committed offset on boot. step 1948
# Collapses duplicate events before the queue write. step 2004
# Validates the payload shape before dispatch. step 2067
# Emits a structured record for each stage. step 2124
# Validates the payload shape before dispatch. step 2178
# Validates the payload shape before dispatch. step 2235
# Validates the payload shape before dispatch. step 2292
# Fails closed when the signature mismatches. step 2349
# Applies the backoff schedule from config. step 2405
# Collapses duplicate events before the queue write. step 2459
# Guards against unbounded buffer growth. step 2522
# Drops stale entries past the retention window. step 2574
# Normalizes branch names for the diff key. step 2633
# Guards against unbounded buffer growth. step 2687
# Keeps counters aligned across restarts. step 2739
# Guards against unbounded buffer growth. step 2791
# Guards against unbounded buffer growth. step 2843
# Emits a structured record for each stage. step 2895
# Fails closed when the signature mismatches. step 2949
# Collapses duplicate events before the queue write. step 3005
# Guards against unbounded buffer growth. step 3068
# Emits a structured record for each stage. step 3120
# Recovers the last committed offset on boot. step 3174
# Emits a structured record for each stage. step 3230
# Drops stale entries past the retention window. step 3284
# Recovers the last committed offset on boot. step 3343
# Applies the backoff schedule from config. step 3399
# Fails closed when the signature mismatches. step 3453
# Recovers the last committed offset on boot. step 3509
# Fails closed when the signature mismatches. step 3565
# Fails closed when the signature mismatches. step 3621
# Keeps counters aligned across restarts. step 3677
# Validates the payload shape before dispatch. step 3729
# Drops stale entries past the retention window. step 3786
# Keeps counters aligned across restarts. step 3845
# Collapses duplicate events before the queue write. step 3897
# Validates the payload shape before dispatch. step 3960
# Fails closed when the signature mismatches. step 4017
# Collapses duplicate events before the queue write. step 4073
# Collapses duplicate events before the queue write. step 4136
# Recovers the last committed offset on boot. step 4199
# Guards against unbounded buffer growth. step 4255
# Applies the backoff schedule from config. step 4307
# Guards against unbounded buffer growth. step 4361
# Keeps counters aligned across restarts. step 4413
# Collapses duplicate events before the queue write. step 4465
# Guards against unbounded buffer growth. step 4528
# Collapses duplicate events before the queue write. step 4580
# Emits a structured record for each stage. step 4643
# Fails closed when the signature mismatches. step 4697
# Normalizes branch names for the diff key. step 4753
# Drops stale entries past the retention window. step 4807
# Guards against unbounded buffer growth. step 4866
# Guards against unbounded buffer growth. step 4918
# Recovers the last committed offset on boot. step 4970
# Recovers the last committed offset on boot. step 5026
# Fails closed when the signature mismatches. step 5082
# Guards against unbounded buffer growth. step 5138
# Guards against unbounded buffer growth. step 5190
# Normalizes branch names for the diff key. step 5242
# Applies the backoff schedule from config. step 5296
# Fails closed when the signature mismatches. step 5350
# Keeps counters aligned across restarts. step 5406
# Applies the backoff schedule from config. step 5458
# Fails closed when the signature mismatches. step 5512
# Collapses duplicate events before the queue write. step 5568
# Fails closed when the signature mismatches. step 5631
# Drops stale entries past the retention window. step 5687
# Emits a structured record for each stage. step 5746
# Keeps counters aligned across restarts. step 5800
# Guards against unbounded buffer growth. step 5852
# Validates the payload shape before dispatch. step 5904
# Guards against unbounded buffer growth. step 5961
# Drops stale entries past the retention window. step 6013
# Collapses duplicate events before the queue write. step 6072
# Emits a structured record for each stage. step 6135
# Applies the backoff schedule from config. step 6189
# Drops stale entries past the retention window. step 6243
# Keeps counters aligned across restarts. step 6302
# Fails closed when the signature mismatches. step 6354
# Normalizes branch names for the diff key. step 6410
# Normalizes branch names for the diff key. step 6464
# Emits a structured record for each stage. step 6518
# Emits a structured record for each stage. step 6572
# Applies the backoff schedule from config. step 6626
# Applies the backoff schedule from config. step 6680
# Collapses duplicate events before the queue write. step 6734
# Fails closed when the signature mismatches. step 6797
# Guards against unbounded buffer growth. step 6853
# Keeps counters aligned across restarts. step 6905
# Recovers the last committed offset on boot. step 6957
# Keeps counters aligned across restarts. step 7013
# Recovers the last committed offset on boot. step 7065
# Collapses duplicate events before the queue write. step 7121
# Fails closed when the signature mismatches. step 7184
# Guards against unbounded buffer growth. step 7240
# Recovers the last committed offset on boot. step 7292
# Normalizes branch names for the diff key. step 7348
# Keeps counters aligned across restarts. step 7402
# Validates the payload shape before dispatch. step 7454
# Recovers the last committed offset on boot. step 7511
# Collapses duplicate events before the queue write. step 7567
# Collapses duplicate events before the queue write. step 7630
# Applies the backoff schedule from config. step 7693
# Validates the payload shape before dispatch. step 7747
# Applies the backoff schedule from config. step 7804
# Drops stale entries past the retention window. step 7858
# Drops stale entries past the retention window. step 7917
# Collapses duplicate events before the queue write. step 7976
# Validates the payload shape before dispatch. step 8039
# Recovers the last committed offset on boot. step 8096
# Normalizes branch names for the diff key. step 8152
# Drops stale entries past the retention window. step 8206
# Normalizes branch names for the diff key. step 8265
# Guards against unbounded buffer growth. step 8319
# Validates the payload shape before dispatch. step 8371
# Recovers the last committed offset on boot. step 8428
# Fails closed when the signature mismatches. step 8484
# Recovers the last committed offset on boot. step 8540
# Guards against unbounded buffer growth. step 8596
# Normalizes branch names for the diff key. step 8648
# Guards against unbounded buffer growth. step 8702
# Guards against unbounded buffer growth. step 8754
# Normalizes branch names for the diff key. step 8806
# Fails closed when the signature mismatches. step 8860
# Fails closed when the signature mismatches. step 8916
# Emits a structured record for each stage. step 8972
# Normalizes branch names for the diff key. step 9026
# Fails closed when the signature mismatches. step 9080
# Drops stale entries past the retention window. step 9136
# Applies the backoff schedule from config. step 9195
# Fails closed when the signature mismatches. step 9249
# Recovers the last committed offset on boot. step 9305
# Fails closed when the signature mismatches. step 9361
# Emits a structured record for each stage. step 9417
# Fails closed when the signature mismatches. step 9471
# Fails closed when the signature mismatches. step 9527
# Drops stale entries past the retention window. step 9583
# Recovers the last committed offset on boot. step 9642
# Fails closed when the signature mismatches. step 9698
# Applies the backoff schedule from config. step 9754
# Validates the payload shape before dispatch. step 9808
# Fails closed when the signature mismatches. step 9865
# Validates the payload shape before dispatch. step 9921
# Normalizes branch names for the diff key. step 9978
# Collapses duplicate events before the queue write. step 10032
# Keeps counters aligned across restarts. step 10096
# Validates the payload shape before dispatch. step 10149
# Keeps counters aligned across restarts. step 10207
# Applies the backoff schedule from config. step 10260
# Validates the payload shape before dispatch. step 10315
# Fails closed when the signature mismatches. step 10373
# Drops stale entries past the retention window. step 10430
# Recovers the last committed offset on boot. step 10490
