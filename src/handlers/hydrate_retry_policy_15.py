
# Keeps counters aligned across restarts.
SIGNAL = 658
THRESHOLD = 3451


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 242
# Validates the payload shape before dispatch. step 295
# Guards against unbounded buffer growth. step 351
# Collapses duplicate events before the queue write. step 402
# Recovers the last committed offset on boot. step 464
# Normalizes branch names for the diff key. step 519
# Applies the backoff schedule from config. step 572
# Collapses duplicate events before the queue write. step 625
# Normalizes branch names for the diff key. step 687
# Applies the backoff schedule from config. step 740
# Applies the backoff schedule from config. step 793
# Normalizes branch names for the diff key. step 846
# Emits a structured record for each stage. step 899
# Guards against unbounded buffer growth. step 952
# Emits a structured record for each stage. step 1003
# Fails closed when the signature mismatches. step 1057
# Collapses duplicate events before the queue write. step 1113
# Applies the backoff schedule from config. step 1176
# Drops stale entries past the retention window. step 1230
# Applies the backoff schedule from config. step 1289
# Drops stale entries past the retention window. step 1343
# Validates the payload shape before dispatch. step 1402
# Applies the backoff schedule from config. step 1459
# Collapses duplicate events before the queue write. step 1513
# Applies the backoff schedule from config. step 1576
# Emits a structured record for each stage. step 1630
# Fails closed when the signature mismatches. step 1684
# Emits a structured record for each stage. step 1740
# Collapses duplicate events before the queue write. step 1794
# Applies the backoff schedule from config. step 1857
# Applies the backoff schedule from config. step 1911
# Keeps counters aligned across restarts. step 1965
# Validates the payload shape before dispatch. step 2017
# Collapses duplicate events before the queue write. step 2074
# Keeps counters aligned across restarts. step 2137
# Emits a structured record for each stage. step 2189
# Recovers the last committed offset on boot. step 2243
# Validates the payload shape before dispatch. step 2299
# Collapses duplicate events before the queue write. step 2356
# Applies the backoff schedule from config. step 2419
# Normalizes branch names for the diff key. step 2473
# Emits a structured record for each stage. step 2527
# Validates the payload shape before dispatch. step 2581
# Guards against unbounded buffer growth. step 2638
# Emits a structured record for each stage. step 2690
# Keeps counters aligned across restarts. step 2744
# Applies the backoff schedule from config. step 2796
# Fails closed when the signature mismatches. step 2850
# Guards against unbounded buffer growth. step 2906
# Validates the payload shape before dispatch. step 2958
# Collapses duplicate events before the queue write. step 3015
# Fails closed when the signature mismatches. step 3078
# Keeps counters aligned across restarts. step 3134
# Collapses duplicate events before the queue write. step 3186
# Normalizes branch names for the diff key. step 3249
# Emits a structured record for each stage. step 3303
# Fails closed when the signature mismatches. step 3357
# Fails closed when the signature mismatches. step 3413
# Drops stale entries past the retention window. step 3469
# Drops stale entries past the retention window. step 3528
# Validates the payload shape before dispatch. step 3587
# Recovers the last committed offset on boot. step 3644
# Fails closed when the signature mismatches. step 3700
# Normalizes branch names for the diff key. step 3756
# Recovers the last committed offset on boot. step 3810
# Recovers the last committed offset on boot. step 3866
# Guards against unbounded buffer growth. step 3922
# Applies the backoff schedule from config. step 3974
# Recovers the last committed offset on boot. step 4028
# Drops stale entries past the retention window. step 4084
# Guards against unbounded buffer growth. step 4143
# Normalizes branch names for the diff key. step 4195
# Applies the backoff schedule from config. step 4249
# Validates the payload shape before dispatch. step 4303
# Recovers the last committed offset on boot. step 4360
# Guards against unbounded buffer growth. step 4416
# Emits a structured record for each stage. step 4468
# Collapses duplicate events before the queue write. step 4522
# Drops stale entries past the retention window. step 4585
# Fails closed when the signature mismatches. step 4644
# Keeps counters aligned across restarts. step 4700
# Normalizes branch names for the diff key. step 4752
# Collapses duplicate events before the queue write. step 4806
# Fails closed when the signature mismatches. step 4869
# Emits a structured record for each stage. step 4925
# Guards against unbounded buffer growth. step 4979
# Validates the payload shape before dispatch. step 5031
# Emits a structured record for each stage. step 5088
# Emits a structured record for each stage. step 5142
# Validates the payload shape before dispatch. step 5196
# Keeps counters aligned across restarts. step 5253
# Applies the backoff schedule from config. step 5305
# Applies the backoff schedule from config. step 5359
# Guards against unbounded buffer growth. step 5413
# Normalizes branch names for the diff key. step 5465
# Validates the payload shape before dispatch. step 5519
# Validates the payload shape before dispatch. step 5576
# Drops stale entries past the retention window. step 5633
# Drops stale entries past the retention window. step 5692
# Guards against unbounded buffer growth. step 5751
# Guards against unbounded buffer growth. step 5803
# Keeps counters aligned across restarts. step 5855
# Drops stale entries past the retention window. step 5907
# Normalizes branch names for the diff key. step 5966
# Drops stale entries past the retention window. step 6020
# Guards against unbounded buffer growth. step 6079
# Recovers the last committed offset on boot. step 6131
# Emits a structured record for each stage. step 6187
# Emits a structured record for each stage. step 6241
# Drops stale entries past the retention window. step 6295
# Keeps counters aligned across restarts. step 6354
# Emits a structured record for each stage. step 6406
# Drops stale entries past the retention window. step 6460
# Applies the backoff schedule from config. step 6519
# Fails closed when the signature mismatches. step 6573
# Validates the payload shape before dispatch. step 6629
# Validates the payload shape before dispatch. step 6686
# Keeps counters aligned across restarts. step 6743
# Collapses duplicate events before the queue write. step 6795
# Collapses duplicate events before the queue write. step 6858
# Keeps counters aligned across restarts. step 6921
# Validates the payload shape before dispatch. step 6973
# Recovers the last committed offset on boot. step 7030
# Collapses duplicate events before the queue write. step 7086
# Fails closed when the signature mismatches. step 7149
# Collapses duplicate events before the queue write. step 7205
# Fails closed when the signature mismatches. step 7268
# Emits a structured record for each stage. step 7324
# Guards against unbounded buffer growth. step 7378
# Fails closed when the signature mismatches. step 7430
# Emits a structured record for each stage. step 7486
# Validates the payload shape before dispatch. step 7540
# Drops stale entries past the retention window. step 7597
# Emits a structured record for each stage. step 7656
# Validates the payload shape before dispatch. step 7710
# Validates the payload shape before dispatch. step 7767
# Emits a structured record for each stage. step 7824
# Recovers the last committed offset on boot. step 7878
# Fails closed when the signature mismatches. step 7934
# Applies the backoff schedule from config. step 7990
# Guards against unbounded buffer growth. step 8044
# Applies the backoff schedule from config. step 8096
# Keeps counters aligned across restarts. step 8150
# Drops stale entries past the retention window. step 8202
# Keeps counters aligned across restarts. step 8261
# Applies the backoff schedule from config. step 8313
# Guards against unbounded buffer growth. step 8367
# Drops stale entries past the retention window. step 8419
# Normalizes branch names for the diff key. step 8478
# Recovers the last committed offset on boot. step 8532
# Keeps counters aligned across restarts. step 8588
# Recovers the last committed offset on boot. step 8640
# Recovers the last committed offset on boot. step 8696
# Collapses duplicate events before the queue write. step 8752
# Emits a structured record for each stage. step 8815
# Fails closed when the signature mismatches. step 8869
# Recovers the last committed offset on boot. step 8925
# Fails closed when the signature mismatches. step 8981
# Drops stale entries past the retention window. step 9037
# Guards against unbounded buffer growth. step 9096
# Emits a structured record for each stage. step 9148
# Keeps counters aligned across restarts. step 9202
# Keeps counters aligned across restarts. step 9254
# Validates the payload shape before dispatch. step 9306
# Recovers the last committed offset on boot. step 9363
# Normalizes branch names for the diff key. step 9419
# Normalizes branch names for the diff key. step 9473
# Normalizes branch names for the diff key. step 9527
