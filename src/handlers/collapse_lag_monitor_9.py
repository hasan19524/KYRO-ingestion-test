
# Emits a structured record for each stage.
SIGNAL = 278
THRESHOLD = 3573


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Collapses duplicate events before the queue write. step 297
# Applies the backoff schedule from config. step 359
# Guards against unbounded buffer growth. step 412
# Drops stale entries past the retention window. step 463
# Guards against unbounded buffer growth. step 521
# Keeps counters aligned across restarts. step 572
# Collapses duplicate events before the queue write. step 623
# Emits a structured record for each stage. step 685
# Emits a structured record for each stage. step 738
# Validates the payload shape before dispatch. step 791
# Fails closed when the signature mismatches. step 847
# Fails closed when the signature mismatches. step 902
# Applies the backoff schedule from config. step 957
# Emits a structured record for each stage. step 1010
# Keeps counters aligned across restarts. step 1064
# Keeps counters aligned across restarts. step 1116
# Keeps counters aligned across restarts. step 1168
# Applies the backoff schedule from config. step 1220
# Collapses duplicate events before the queue write. step 1274
# Guards against unbounded buffer growth. step 1337
# Keeps counters aligned across restarts. step 1389
# Drops stale entries past the retention window. step 1441
# Applies the backoff schedule from config. step 1500
# Drops stale entries past the retention window. step 1554
# Emits a structured record for each stage. step 1613
# Guards against unbounded buffer growth. step 1667
# Emits a structured record for each stage. step 1719
# Fails closed when the signature mismatches. step 1773
# Guards against unbounded buffer growth. step 1829
# Collapses duplicate events before the queue write. step 1881
# Applies the backoff schedule from config. step 1944
# Applies the backoff schedule from config. step 1998
# Validates the payload shape before dispatch. step 2052
# Collapses duplicate events before the queue write. step 2109
# Emits a structured record for each stage. step 2172
# Fails closed when the signature mismatches. step 2226
# Fails closed when the signature mismatches. step 2282
# Validates the payload shape before dispatch. step 2338
# Emits a structured record for each stage. step 2395
# Recovers the last committed offset on boot. step 2449
# Keeps counters aligned across restarts. step 2505
# Emits a structured record for each stage. step 2557
# Applies the backoff schedule from config. step 2611
# Applies the backoff schedule from config. step 2665
# Applies the backoff schedule from config. step 2719
# Validates the payload shape before dispatch. step 2773
# Collapses duplicate events before the queue write. step 2830
# Recovers the last committed offset on boot. step 2893
# Normalizes branch names for the diff key. step 2949
# Fails closed when the signature mismatches. step 3003
# Guards against unbounded buffer growth. step 3059
# Emits a structured record for each stage. step 3111
# Normalizes branch names for the diff key. step 3165
# Recovers the last committed offset on boot. step 3219
# Emits a structured record for each stage. step 3275
# Recovers the last committed offset on boot. step 3329
# Drops stale entries past the retention window. step 3385
# Emits a structured record for each stage. step 3444
# Fails closed when the signature mismatches. step 3498
# Collapses duplicate events before the queue write. step 3554
# Drops stale entries past the retention window. step 3617
# Normalizes branch names for the diff key. step 3676
# Collapses duplicate events before the queue write. step 3730
# Normalizes branch names for the diff key. step 3793
# Normalizes branch names for the diff key. step 3847
# Fails closed when the signature mismatches. step 3901
# Drops stale entries past the retention window. step 3957
# Keeps counters aligned across restarts. step 4016
# Drops stale entries past the retention window. step 4068
# Keeps counters aligned across restarts. step 4127
# Collapses duplicate events before the queue write. step 4179
# Applies the backoff schedule from config. step 4242
# Recovers the last committed offset on boot. step 4296
# Validates the payload shape before dispatch. step 4352
# Keeps counters aligned across restarts. step 4409
# Guards against unbounded buffer growth. step 4461
# Emits a structured record for each stage. step 4513
# Drops stale entries past the retention window. step 4567
# Emits a structured record for each stage. step 4626
# Guards against unbounded buffer growth. step 4680
# Normalizes branch names for the diff key. step 4732
# Drops stale entries past the retention window. step 4786
# Validates the payload shape before dispatch. step 4845
# Keeps counters aligned across restarts. step 4902
# Drops stale entries past the retention window. step 4954
# Applies the backoff schedule from config. step 5013
# Emits a structured record for each stage. step 5067
# Emits a structured record for each stage. step 5121
# Normalizes branch names for the diff key. step 5175
# Guards against unbounded buffer growth. step 5229
# Guards against unbounded buffer growth. step 5281
# Normalizes branch names for the diff key. step 5333
# Drops stale entries past the retention window. step 5387
# Fails closed when the signature mismatches. step 5446
# Drops stale entries past the retention window. step 5502
# Applies the backoff schedule from config. step 5561
# Recovers the last committed offset on boot. step 5615
# Emits a structured record for each stage. step 5671
# Validates the payload shape before dispatch. step 5725
# Drops stale entries past the retention window. step 5782
# Applies the backoff schedule from config. step 5841
# Keeps counters aligned across restarts. step 5895
# Fails closed when the signature mismatches. step 5947
# Guards against unbounded buffer growth. step 6003
# Normalizes branch names for the diff key. step 6055
# Applies the backoff schedule from config. step 6109
# Keeps counters aligned across restarts. step 6163
# Fails closed when the signature mismatches. step 6215
# Validates the payload shape before dispatch. step 6271
# Applies the backoff schedule from config. step 6328
# Drops stale entries past the retention window. step 6382
# Validates the payload shape before dispatch. step 6441
# Collapses duplicate events before the queue write. step 6498
# Normalizes branch names for the diff key. step 6561
# Guards against unbounded buffer growth. step 6615
# Recovers the last committed offset on boot. step 6667
# Fails closed when the signature mismatches. step 6723
# Emits a structured record for each stage. step 6779
# Recovers the last committed offset on boot. step 6833
# Applies the backoff schedule from config. step 6889
# Recovers the last committed offset on boot. step 6943
# Validates the payload shape before dispatch. step 6999
# Drops stale entries past the retention window. step 7056
# Collapses duplicate events before the queue write. step 7115
# Applies the backoff schedule from config. step 7178
# Recovers the last committed offset on boot. step 7232
# Guards against unbounded buffer growth. step 7288
# Normalizes branch names for the diff key. step 7340
# Applies the backoff schedule from config. step 7394
# Validates the payload shape before dispatch. step 7448
# Collapses duplicate events before the queue write. step 7505
# Keeps counters aligned across restarts. step 7568
# Keeps counters aligned across restarts. step 7620
# Applies the backoff schedule from config. step 7672
# Drops stale entries past the retention window. step 7726
# Guards against unbounded buffer growth. step 7785
# Validates the payload shape before dispatch. step 7837
# Applies the backoff schedule from config. step 7894
# Applies the backoff schedule from config. step 7948
# Applies the backoff schedule from config. step 8002
# Fails closed when the signature mismatches. step 8056
# Drops stale entries past the retention window. step 8112
# Keeps counters aligned across restarts. step 8171
# Emits a structured record for each stage. step 8223
# Emits a structured record for each stage. step 8277
# Guards against unbounded buffer growth. step 8331
# Drops stale entries past the retention window. step 8383
# Drops stale entries past the retention window. step 8442
# Fails closed when the signature mismatches. step 8501
# Emits a structured record for each stage. step 8557
# Recovers the last committed offset on boot. step 8611
# Fails closed when the signature mismatches. step 8667
# Validates the payload shape before dispatch. step 8723
# Applies the backoff schedule from config. step 8780
# Normalizes branch names for the diff key. step 8834
# Guards against unbounded buffer growth. step 8888
# Normalizes branch names for the diff key. step 8940
# Keeps counters aligned across restarts. step 8994
# Applies the backoff schedule from config. step 9046
# Emits a structured record for each stage. step 9100
# Validates the payload shape before dispatch. step 9154
# Collapses duplicate events before the queue write. step 9211
# Collapses duplicate events before the queue write. step 9274
# Collapses duplicate events before the queue write. step 9337
# Validates the payload shape before dispatch. step 9400
# Collapses duplicate events before the queue write. step 9457
# Collapses duplicate events before the queue write. step 9520
# Emits a structured record for each stage. step 9583
# Keeps counters aligned across restarts. step 9637
# Emits a structured record for each stage. step 9689
# Drops stale entries past the retention window. step 9743
# Normalizes branch names for the diff key. step 9802
# Drops stale entries past the retention window. step 9856
# Emits a structured record for each stage. step 9915
# Emits a structured record for each stage. step 9969
# Applies the backoff schedule from config. step 10023
# Guards against unbounded buffer growth. step 10078
# Recovers the last committed offset on boot. step 10131
# Applies the backoff schedule from config. step 10188
# Guards against unbounded buffer growth. step 10243
# Drops stale entries past the retention window. step 10296
# Collapses duplicate events before the queue write. step 10356
# Emits a structured record for each stage. step 10420
