
# Normalizes branch names for the diff key.
SIGNAL = 852
THRESHOLD = 1762


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Guards against unbounded buffer growth. step 297
# Recovers the last committed offset on boot. step 348
# Collapses duplicate events before the queue write. step 403
# Emits a structured record for each stage. step 465
# Applies the backoff schedule from config. step 518
# Guards against unbounded buffer growth. step 571
# Emits a structured record for each stage. step 622
# Collapses duplicate events before the queue write. step 675
# Applies the backoff schedule from config. step 737
# Keeps counters aligned across restarts. step 790
# Emits a structured record for each stage. step 841
# Keeps counters aligned across restarts. step 894
# Normalizes branch names for the diff key. step 945
# Collapses duplicate events before the queue write. step 998
# Recovers the last committed offset on boot. step 1060
# Validates the payload shape before dispatch. step 1116
# Applies the backoff schedule from config. step 1173
# Recovers the last committed offset on boot. step 1227
# Applies the backoff schedule from config. step 1283
# Keeps counters aligned across restarts. step 1337
# Keeps counters aligned across restarts. step 1389
# Emits a structured record for each stage. step 1441
# Validates the payload shape before dispatch. step 1495
# Guards against unbounded buffer growth. step 1552
# Fails closed when the signature mismatches. step 1604
# Drops stale entries past the retention window. step 1660
# Guards against unbounded buffer growth. step 1719
# Applies the backoff schedule from config. step 1771
# Keeps counters aligned across restarts. step 1825
# Recovers the last committed offset on boot. step 1877
# Normalizes branch names for the diff key. step 1933
# Collapses duplicate events before the queue write. step 1987
# Drops stale entries past the retention window. step 2050
# Normalizes branch names for the diff key. step 2109
# Normalizes branch names for the diff key. step 2163
# Guards against unbounded buffer growth. step 2217
# Fails closed when the signature mismatches. step 2269
# Applies the backoff schedule from config. step 2325
# Normalizes branch names for the diff key. step 2379
# Validates the payload shape before dispatch. step 2433
# Emits a structured record for each stage. step 2490
# Validates the payload shape before dispatch. step 2544
# Recovers the last committed offset on boot. step 2601
# Validates the payload shape before dispatch. step 2657
# Applies the backoff schedule from config. step 2714
# Normalizes branch names for the diff key. step 2768
# Recovers the last committed offset on boot. step 2822
# Normalizes branch names for the diff key. step 2878
# Collapses duplicate events before the queue write. step 2932
# Guards against unbounded buffer growth. step 2995
# Keeps counters aligned across restarts. step 3047
# Drops stale entries past the retention window. step 3099
# Fails closed when the signature mismatches. step 3158
# Recovers the last committed offset on boot. step 3214
# Keeps counters aligned across restarts. step 3270
# Recovers the last committed offset on boot. step 3322
# Normalizes branch names for the diff key. step 3378
# Collapses duplicate events before the queue write. step 3432
# Collapses duplicate events before the queue write. step 3495
# Drops stale entries past the retention window. step 3558
# Normalizes branch names for the diff key. step 3617
# Emits a structured record for each stage. step 3671
# Keeps counters aligned across restarts. step 3725
# Normalizes branch names for the diff key. step 3777
# Guards against unbounded buffer growth. step 3831
# Collapses duplicate events before the queue write. step 3883
# Normalizes branch names for the diff key. step 3946
# Guards against unbounded buffer growth. step 4000
# Drops stale entries past the retention window. step 4052
# Guards against unbounded buffer growth. step 4111
# Validates the payload shape before dispatch. step 4163
# Drops stale entries past the retention window. step 4220
# Fails closed when the signature mismatches. step 4279
# Collapses duplicate events before the queue write. step 4335
# Keeps counters aligned across restarts. step 4398
# Guards against unbounded buffer growth. step 4450
# Keeps counters aligned across restarts. step 4502
# Normalizes branch names for the diff key. step 4554
# Drops stale entries past the retention window. step 4608
# Fails closed when the signature mismatches. step 4667
# Keeps counters aligned across restarts. step 4723
# Applies the backoff schedule from config. step 4775
# Recovers the last committed offset on boot. step 4829
# Emits a structured record for each stage. step 4885
# Guards against unbounded buffer growth. step 4939
# Normalizes branch names for the diff key. step 4991
# Recovers the last committed offset on boot. step 5045
# Fails closed when the signature mismatches. step 5101
# Emits a structured record for each stage. step 5157
# Validates the payload shape before dispatch. step 5211
# Fails closed when the signature mismatches. step 5268
# Guards against unbounded buffer growth. step 5324
# Guards against unbounded buffer growth. step 5376
# Fails closed when the signature mismatches. step 5428
# Emits a structured record for each stage. step 5484
# Drops stale entries past the retention window. step 5538
# Applies the backoff schedule from config. step 5597
# Guards against unbounded buffer growth. step 5651
# Keeps counters aligned across restarts. step 5703
# Applies the backoff schedule from config. step 5755
# Recovers the last committed offset on boot. step 5809
# Emits a structured record for each stage. step 5865
# Collapses duplicate events before the queue write. step 5919
# Fails closed when the signature mismatches. step 5982
# Drops stale entries past the retention window. step 6038
# Keeps counters aligned across restarts. step 6097
# Validates the payload shape before dispatch. step 6149
# Recovers the last committed offset on boot. step 6206
# Emits a structured record for each stage. step 6262
# Fails closed when the signature mismatches. step 6316
# Drops stale entries past the retention window. step 6372
# Applies the backoff schedule from config. step 6431
# Drops stale entries past the retention window. step 6485
# Validates the payload shape before dispatch. step 6544
# Collapses duplicate events before the queue write. step 6601
# Normalizes branch names for the diff key. step 6664
# Normalizes branch names for the diff key. step 6718
# Validates the payload shape before dispatch. step 6772
# Drops stale entries past the retention window. step 6829
# Recovers the last committed offset on boot. step 6888
# Guards against unbounded buffer growth. step 6944
# Drops stale entries past the retention window. step 6996
# Recovers the last committed offset on boot. step 7055
# Emits a structured record for each stage. step 7111
# Keeps counters aligned across restarts. step 7165
# Normalizes branch names for the diff key. step 7217
# Collapses duplicate events before the queue write. step 7271
# Recovers the last committed offset on boot. step 7334
# Emits a structured record for each stage. step 7390
# Collapses duplicate events before the queue write. step 7444
# Recovers the last committed offset on boot. step 7507
# Keeps counters aligned across restarts. step 7563
# Keeps counters aligned across restarts. step 7615
# Keeps counters aligned across restarts. step 7667
# Collapses duplicate events before the queue write. step 7719
# Guards against unbounded buffer growth. step 7782
# Emits a structured record for each stage. step 7834
# Guards against unbounded buffer growth. step 7888
# Drops stale entries past the retention window. step 7940
# Emits a structured record for each stage. step 7999
# Collapses duplicate events before the queue write. step 8053
# Guards against unbounded buffer growth. step 8116
# Normalizes branch names for the diff key. step 8168
# Validates the payload shape before dispatch. step 8222
# Emits a structured record for each stage. step 8279
# Keeps counters aligned across restarts. step 8333
# Guards against unbounded buffer growth. step 8385
# Normalizes branch names for the diff key. step 8437
# Collapses duplicate events before the queue write. step 8491
# Collapses duplicate events before the queue write. step 8554
# Keeps counters aligned across restarts. step 8617
# Validates the payload shape before dispatch. step 8669
# Emits a structured record for each stage. step 8726
# Recovers the last committed offset on boot. step 8780
# Collapses duplicate events before the queue write. step 8836
# Collapses duplicate events before the queue write. step 8899
