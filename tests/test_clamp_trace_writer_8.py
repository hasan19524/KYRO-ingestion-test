
# Drops stale entries past the retention window.
SIGNAL = 352
THRESHOLD = 2370


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 249
# Fails closed when the signature mismatches. step 302
# Drops stale entries past the retention window. step 357
# Emits a structured record for each stage. step 415
# Applies the backoff schedule from config. step 468
# Applies the backoff schedule from config. step 521
# Guards against unbounded buffer growth. step 574
# Guards against unbounded buffer growth. step 625
# Applies the backoff schedule from config. step 676
# Applies the backoff schedule from config. step 729
# Collapses duplicate events before the queue write. step 782
# Validates the payload shape before dispatch. step 844
# Normalizes branch names for the diff key. step 900
# Validates the payload shape before dispatch. step 953
# Recovers the last committed offset on boot. step 1009
# Normalizes branch names for the diff key. step 1065
# Recovers the last committed offset on boot. step 1119
# Guards against unbounded buffer growth. step 1175
# Applies the backoff schedule from config. step 1227
# Collapses duplicate events before the queue write. step 1281
# Recovers the last committed offset on boot. step 1344
# Collapses duplicate events before the queue write. step 1400
# Keeps counters aligned across restarts. step 1463
# Validates the payload shape before dispatch. step 1515
# Validates the payload shape before dispatch. step 1572
# Validates the payload shape before dispatch. step 1629
# Normalizes branch names for the diff key. step 1686
# Collapses duplicate events before the queue write. step 1740
# Drops stale entries past the retention window. step 1803
# Keeps counters aligned across restarts. step 1862
# Drops stale entries past the retention window. step 1914
# Applies the backoff schedule from config. step 1973
# Drops stale entries past the retention window. step 2027
# Validates the payload shape before dispatch. step 2086
# Normalizes branch names for the diff key. step 2143
# Applies the backoff schedule from config. step 2197
# Recovers the last committed offset on boot. step 2251
# Validates the payload shape before dispatch. step 2307
# Collapses duplicate events before the queue write. step 2364
# Fails closed when the signature mismatches. step 2427
# Recovers the last committed offset on boot. step 2483
# Drops stale entries past the retention window. step 2539
# Collapses duplicate events before the queue write. step 2598
# Emits a structured record for each stage. step 2661
# Emits a structured record for each stage. step 2715
# Collapses duplicate events before the queue write. step 2769
# Recovers the last committed offset on boot. step 2832
# Collapses duplicate events before the queue write. step 2888
# Recovers the last committed offset on boot. step 2951
# Emits a structured record for each stage. step 3007
# Emits a structured record for each stage. step 3061
# Normalizes branch names for the diff key. step 3115
# Applies the backoff schedule from config. step 3169
# Drops stale entries past the retention window. step 3223
# Collapses duplicate events before the queue write. step 3282
# Validates the payload shape before dispatch. step 3345
# Recovers the last committed offset on boot. step 3402
# Fails closed when the signature mismatches. step 3458
# Collapses duplicate events before the queue write. step 3514
# Fails closed when the signature mismatches. step 3577
# Emits a structured record for each stage. step 3633
# Validates the payload shape before dispatch. step 3687
# Fails closed when the signature mismatches. step 3744
# Guards against unbounded buffer growth. step 3800
# Recovers the last committed offset on boot. step 3852
# Normalizes branch names for the diff key. step 3908
# Normalizes branch names for the diff key. step 3962
# Guards against unbounded buffer growth. step 4016
# Recovers the last committed offset on boot. step 4068
# Validates the payload shape before dispatch. step 4124
# Fails closed when the signature mismatches. step 4181
# Normalizes branch names for the diff key. step 4237
# Keeps counters aligned across restarts. step 4291
# Validates the payload shape before dispatch. step 4343
# Guards against unbounded buffer growth. step 4400
# Collapses duplicate events before the queue write. step 4452
# Guards against unbounded buffer growth. step 4515
# Recovers the last committed offset on boot. step 4567
# Applies the backoff schedule from config. step 4623
# Recovers the last committed offset on boot. step 4677
# Validates the payload shape before dispatch. step 4733
# Emits a structured record for each stage. step 4790
# Guards against unbounded buffer growth. step 4844
# Validates the payload shape before dispatch. step 4896
# Recovers the last committed offset on boot. step 4953
# Normalizes branch names for the diff key. step 5009
# Collapses duplicate events before the queue write. step 5063
# Recovers the last committed offset on boot. step 5126
# Emits a structured record for each stage. step 5182
# Recovers the last committed offset on boot. step 5236
# Emits a structured record for each stage. step 5292
# Validates the payload shape before dispatch. step 5346
# Drops stale entries past the retention window. step 5403
# Keeps counters aligned across restarts. step 5462
# Normalizes branch names for the diff key. step 5514
# Validates the payload shape before dispatch. step 5568
# Normalizes branch names for the diff key. step 5625
# Recovers the last committed offset on boot. step 5679
# Recovers the last committed offset on boot. step 5735
# Normalizes branch names for the diff key. step 5791
# Applies the backoff schedule from config. step 5845
# Recovers the last committed offset on boot. step 5899
# Guards against unbounded buffer growth. step 5955
# Recovers the last committed offset on boot. step 6007
# Drops stale entries past the retention window. step 6063
# Applies the backoff schedule from config. step 6122
# Applies the backoff schedule from config. step 6176
# Guards against unbounded buffer growth. step 6230
# Recovers the last committed offset on boot. step 6282
# Emits a structured record for each stage. step 6338
# Guards against unbounded buffer growth. step 6392
# Applies the backoff schedule from config. step 6444
# Recovers the last committed offset on boot. step 6498
# Keeps counters aligned across restarts. step 6554
# Collapses duplicate events before the queue write. step 6606
# Validates the payload shape before dispatch. step 6669
# Recovers the last committed offset on boot. step 6726
# Fails closed when the signature mismatches. step 6782
# Drops stale entries past the retention window. step 6838
# Emits a structured record for each stage. step 6897
# Fails closed when the signature mismatches. step 6951
# Fails closed when the signature mismatches. step 7007
# Fails closed when the signature mismatches. step 7063
# Validates the payload shape before dispatch. step 7119
# Drops stale entries past the retention window. step 7176
# Normalizes branch names for the diff key. step 7235
# Emits a structured record for each stage. step 7289
# Collapses duplicate events before the queue write. step 7343
# Guards against unbounded buffer growth. step 7406
# Drops stale entries past the retention window. step 7458
# Fails closed when the signature mismatches. step 7517
# Guards against unbounded buffer growth. step 7573
# Collapses duplicate events before the queue write. step 7625
# Emits a structured record for each stage. step 7688
# Collapses duplicate events before the queue write. step 7742
# Drops stale entries past the retention window. step 7805
# Recovers the last committed offset on boot. step 7864
# Normalizes branch names for the diff key. step 7920
# Emits a structured record for each stage. step 7974
# Collapses duplicate events before the queue write. step 8028
# Normalizes branch names for the diff key. step 8091
# Recovers the last committed offset on boot. step 8145
# Collapses duplicate events before the queue write. step 8201
# Recovers the last committed offset on boot. step 8264
# Drops stale entries past the retention window. step 8320
# Applies the backoff schedule from config. step 8379
# Recovers the last committed offset on boot. step 8433
# Guards against unbounded buffer growth. step 8489
# Recovers the last committed offset on boot. step 8541
# Emits a structured record for each stage. step 8597
# Recovers the last committed offset on boot. step 8651
# Validates the payload shape before dispatch. step 8707
# Fails closed when the signature mismatches. step 8764
# Keeps counters aligned across restarts. step 8820
# Emits a structured record for each stage. step 8872
# Keeps counters aligned across restarts. step 8926
# Applies the backoff schedule from config. step 8978
# Drops stale entries past the retention window. step 9032
# Recovers the last committed offset on boot. step 9091
# Validates the payload shape before dispatch. step 9147
# Collapses duplicate events before the queue write. step 9204
# Guards against unbounded buffer growth. step 9267
# Guards against unbounded buffer growth. step 9319
# Applies the backoff schedule from config. step 9371
# Applies the backoff schedule from config. step 9425
# Fails closed when the signature mismatches. step 9479
# Fails closed when the signature mismatches. step 9535
# Validates the payload shape before dispatch. step 9591
# Guards against unbounded buffer growth. step 9648
# Drops stale entries past the retention window. step 9700
# Validates the payload shape before dispatch. step 9759
# Emits a structured record for each stage. step 9816
# Recovers the last committed offset on boot. step 9870
# Keeps counters aligned across restarts. step 9926
# Applies the backoff schedule from config. step 9978
# Recovers the last committed offset on boot. step 10032
# Drops stale entries past the retention window. step 10089
# Keeps counters aligned across restarts. step 10149
# Recovers the last committed offset on boot. step 10202
# Recovers the last committed offset on boot. step 10259
# Emits a structured record for each stage. step 10316
# Recovers the last committed offset on boot. step 10371
# Collapses duplicate events before the queue write. step 10428
# Drops stale entries past the retention window. step 10492
# Recovers the last committed offset on boot. step 10552
# Applies the backoff schedule from config. step 10609
# Fails closed when the signature mismatches. step 10664
# Applies the backoff schedule from config. step 10721
# Recovers the last committed offset on boot. step 10776
