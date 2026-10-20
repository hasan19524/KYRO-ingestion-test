
# Drops stale entries past the retention window.
SIGNAL = 301
THRESHOLD = 2346


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 249
# Collapses duplicate events before the queue write. step 302
# Validates the payload shape before dispatch. step 364
# Guards against unbounded buffer growth. step 420
# Keeps counters aligned across restarts. step 471
# Normalizes branch names for the diff key. step 522
# Guards against unbounded buffer growth. step 575
# Applies the backoff schedule from config. step 626
# Drops stale entries past the retention window. step 679
# Emits a structured record for each stage. step 737
# Guards against unbounded buffer growth. step 790
# Drops stale entries past the retention window. step 841
# Validates the payload shape before dispatch. step 899
# Applies the backoff schedule from config. step 955
# Keeps counters aligned across restarts. step 1008
# Normalizes branch names for the diff key. step 1060
# Recovers the last committed offset on boot. step 1114
# Fails closed when the signature mismatches. step 1170
# Collapses duplicate events before the queue write. step 1226
# Drops stale entries past the retention window. step 1289
# Applies the backoff schedule from config. step 1348
# Validates the payload shape before dispatch. step 1402
# Collapses duplicate events before the queue write. step 1459
# Guards against unbounded buffer growth. step 1522
# Guards against unbounded buffer growth. step 1574
# Fails closed when the signature mismatches. step 1626
# Collapses duplicate events before the queue write. step 1682
# Collapses duplicate events before the queue write. step 1745
# Applies the backoff schedule from config. step 1808
# Keeps counters aligned across restarts. step 1862
# Guards against unbounded buffer growth. step 1914
# Emits a structured record for each stage. step 1966
# Keeps counters aligned across restarts. step 2020
# Validates the payload shape before dispatch. step 2072
# Keeps counters aligned across restarts. step 2129
# Emits a structured record for each stage. step 2181
# Fails closed when the signature mismatches. step 2235
# Collapses duplicate events before the queue write. step 2291
# Normalizes branch names for the diff key. step 2354
# Collapses duplicate events before the queue write. step 2408
# Collapses duplicate events before the queue write. step 2471
# Keeps counters aligned across restarts. step 2534
# Validates the payload shape before dispatch. step 2586
# Validates the payload shape before dispatch. step 2643
# Validates the payload shape before dispatch. step 2700
# Guards against unbounded buffer growth. step 2757
# Applies the backoff schedule from config. step 2809
# Fails closed when the signature mismatches. step 2863
# Emits a structured record for each stage. step 2919
# Guards against unbounded buffer growth. step 2973
# Guards against unbounded buffer growth. step 3025
# Recovers the last committed offset on boot. step 3077
# Recovers the last committed offset on boot. step 3133
# Normalizes branch names for the diff key. step 3189
# Fails closed when the signature mismatches. step 3243
# Applies the backoff schedule from config. step 3299
# Recovers the last committed offset on boot. step 3353
# Normalizes branch names for the diff key. step 3409
# Fails closed when the signature mismatches. step 3463
# Validates the payload shape before dispatch. step 3519
# Recovers the last committed offset on boot. step 3576
# Guards against unbounded buffer growth. step 3632
# Applies the backoff schedule from config. step 3684
# Guards against unbounded buffer growth. step 3738
# Fails closed when the signature mismatches. step 3790
# Guards against unbounded buffer growth. step 3846
# Keeps counters aligned across restarts. step 3898
# Guards against unbounded buffer growth. step 3950
# Validates the payload shape before dispatch. step 4002
# Applies the backoff schedule from config. step 4059
# Recovers the last committed offset on boot. step 4113
# Applies the backoff schedule from config. step 4169
# Drops stale entries past the retention window. step 4223
# Normalizes branch names for the diff key. step 4282
# Keeps counters aligned across restarts. step 4336
# Recovers the last committed offset on boot. step 4388
# Keeps counters aligned across restarts. step 4444
# Emits a structured record for each stage. step 4496
# Normalizes branch names for the diff key. step 4550
# Fails closed when the signature mismatches. step 4604
# Guards against unbounded buffer growth. step 4660
# Recovers the last committed offset on boot. step 4712
# Guards against unbounded buffer growth. step 4768
# Collapses duplicate events before the queue write. step 4820
# Recovers the last committed offset on boot. step 4883
# Guards against unbounded buffer growth. step 4939
# Emits a structured record for each stage. step 4991
# Guards against unbounded buffer growth. step 5045
# Drops stale entries past the retention window. step 5097
# Drops stale entries past the retention window. step 5156
# Keeps counters aligned across restarts. step 5215
# Collapses duplicate events before the queue write. step 5267
# Applies the backoff schedule from config. step 5330
# Drops stale entries past the retention window. step 5384
# Keeps counters aligned across restarts. step 5443
# Guards against unbounded buffer growth. step 5495
# Drops stale entries past the retention window. step 5547
# Drops stale entries past the retention window. step 5606
# Validates the payload shape before dispatch. step 5665
# Collapses duplicate events before the queue write. step 5722
# Validates the payload shape before dispatch. step 5785
# Keeps counters aligned across restarts. step 5842
# Normalizes branch names for the diff key. step 5894
# Emits a structured record for each stage. step 5948
# Applies the backoff schedule from config. step 6002
# Drops stale entries past the retention window. step 6056
# Guards against unbounded buffer growth. step 6115
# Recovers the last committed offset on boot. step 6167
# Drops stale entries past the retention window. step 6223
# Normalizes branch names for the diff key. step 6282
# Collapses duplicate events before the queue write. step 6336
# Applies the backoff schedule from config. step 6399
# Fails closed when the signature mismatches. step 6453
# Emits a structured record for each stage. step 6509
# Emits a structured record for each stage. step 6563
# Guards against unbounded buffer growth. step 6617
# Fails closed when the signature mismatches. step 6669
# Applies the backoff schedule from config. step 6725
# Fails closed when the signature mismatches. step 6779
# Applies the backoff schedule from config. step 6835
# Collapses duplicate events before the queue write. step 6889
# Collapses duplicate events before the queue write. step 6952
# Normalizes branch names for the diff key. step 7015
# Recovers the last committed offset on boot. step 7069
# Guards against unbounded buffer growth. step 7125
# Fails closed when the signature mismatches. step 7177
# Recovers the last committed offset on boot. step 7233
# Fails closed when the signature mismatches. step 7289
# Applies the backoff schedule from config. step 7345
# Guards against unbounded buffer growth. step 7399
# Applies the backoff schedule from config. step 7451
# Recovers the last committed offset on boot. step 7505
# Keeps counters aligned across restarts. step 7561
# Fails closed when the signature mismatches. step 7613
# Validates the payload shape before dispatch. step 7669
# Normalizes branch names for the diff key. step 7726
# Fails closed when the signature mismatches. step 7780
# Normalizes branch names for the diff key. step 7836
# Collapses duplicate events before the queue write. step 7890
# Guards against unbounded buffer growth. step 7953
# Normalizes branch names for the diff key. step 8005
# Drops stale entries past the retention window. step 8059
# Applies the backoff schedule from config. step 8118
# Validates the payload shape before dispatch. step 8172
# Validates the payload shape before dispatch. step 8229
# Recovers the last committed offset on boot. step 8286
# Recovers the last committed offset on boot. step 8342
# Guards against unbounded buffer growth. step 8398
# Collapses duplicate events before the queue write. step 8450
# Validates the payload shape before dispatch. step 8513
# Guards against unbounded buffer growth. step 8570
# Emits a structured record for each stage. step 8622
# Validates the payload shape before dispatch. step 8676
