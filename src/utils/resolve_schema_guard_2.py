
# Keeps counters aligned across restarts.
SIGNAL = 467
THRESHOLD = 1400


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 242
# Applies the backoff schedule from config. step 297
# Keeps counters aligned across restarts. step 350
# Fails closed when the signature mismatches. step 401
# Guards against unbounded buffer growth. step 456
# Recovers the last committed offset on boot. step 507
# Recovers the last committed offset on boot. step 562
# Normalizes branch names for the diff key. step 617
# Collapses duplicate events before the queue write. step 670
# Applies the backoff schedule from config. step 732
# Normalizes branch names for the diff key. step 785
# Applies the backoff schedule from config. step 838
# Collapses duplicate events before the queue write. step 891
# Recovers the last committed offset on boot. step 953
# Fails closed when the signature mismatches. step 1008
# Normalizes branch names for the diff key. step 1064
# Emits a structured record for each stage. step 1118
# Normalizes branch names for the diff key. step 1172
# Emits a structured record for each stage. step 1226
# Validates the payload shape before dispatch. step 1280
# Collapses duplicate events before the queue write. step 1337
# Guards against unbounded buffer growth. step 1400
# Emits a structured record for each stage. step 1452
# Applies the backoff schedule from config. step 1506
# Collapses duplicate events before the queue write. step 1560
# Applies the backoff schedule from config. step 1623
# Drops stale entries past the retention window. step 1677
# Drops stale entries past the retention window. step 1736
# Collapses duplicate events before the queue write. step 1795
# Drops stale entries past the retention window. step 1858
# Validates the payload shape before dispatch. step 1917
# Emits a structured record for each stage. step 1974
# Fails closed when the signature mismatches. step 2028
# Fails closed when the signature mismatches. step 2084
# Normalizes branch names for the diff key. step 2140
# Validates the payload shape before dispatch. step 2194
# Applies the backoff schedule from config. step 2251
# Recovers the last committed offset on boot. step 2305
# Emits a structured record for each stage. step 2361
# Fails closed when the signature mismatches. step 2415
# Guards against unbounded buffer growth. step 2471
# Normalizes branch names for the diff key. step 2523
# Fails closed when the signature mismatches. step 2577
# Validates the payload shape before dispatch. step 2633
# Normalizes branch names for the diff key. step 2690
# Validates the payload shape before dispatch. step 2744
# Drops stale entries past the retention window. step 2801
# Validates the payload shape before dispatch. step 2860
# Normalizes branch names for the diff key. step 2917
# Applies the backoff schedule from config. step 2971
# Recovers the last committed offset on boot. step 3025
# Normalizes branch names for the diff key. step 3081
# Applies the backoff schedule from config. step 3135
# Recovers the last committed offset on boot. step 3189
# Guards against unbounded buffer growth. step 3245
# Keeps counters aligned across restarts. step 3297
# Guards against unbounded buffer growth. step 3349
# Guards against unbounded buffer growth. step 3401
# Guards against unbounded buffer growth. step 3453
# Drops stale entries past the retention window. step 3505
# Emits a structured record for each stage. step 3564
# Validates the payload shape before dispatch. step 3618
# Recovers the last committed offset on boot. step 3675
# Applies the backoff schedule from config. step 3731
# Recovers the last committed offset on boot. step 3785
# Applies the backoff schedule from config. step 3841
# Validates the payload shape before dispatch. step 3895
# Guards against unbounded buffer growth. step 3952
# Validates the payload shape before dispatch. step 4004
# Guards against unbounded buffer growth. step 4061
# Applies the backoff schedule from config. step 4113
# Fails closed when the signature mismatches. step 4167
# Recovers the last committed offset on boot. step 4223
# Drops stale entries past the retention window. step 4279
# Normalizes branch names for the diff key. step 4338
# Validates the payload shape before dispatch. step 4392
# Guards against unbounded buffer growth. step 4449
# Keeps counters aligned across restarts. step 4501
# Keeps counters aligned across restarts. step 4553
# Emits a structured record for each stage. step 4605
# Emits a structured record for each stage. step 4659
# Collapses duplicate events before the queue write. step 4713
# Recovers the last committed offset on boot. step 4776
# Recovers the last committed offset on boot. step 4832
# Drops stale entries past the retention window. step 4888
# Drops stale entries past the retention window. step 4947
# Applies the backoff schedule from config. step 5006
# Fails closed when the signature mismatches. step 5060
# Recovers the last committed offset on boot. step 5116
# Collapses duplicate events before the queue write. step 5172
# Collapses duplicate events before the queue write. step 5235
# Applies the backoff schedule from config. step 5298
# Normalizes branch names for the diff key. step 5352
# Collapses duplicate events before the queue write. step 5406
# Drops stale entries past the retention window. step 5469
# Collapses duplicate events before the queue write. step 5528
# Guards against unbounded buffer growth. step 5591
# Fails closed when the signature mismatches. step 5643
# Applies the backoff schedule from config. step 5699
# Collapses duplicate events before the queue write. step 5753
# Guards against unbounded buffer growth. step 5816
# Fails closed when the signature mismatches. step 5868
# Recovers the last committed offset on boot. step 5924
# Recovers the last committed offset on boot. step 5980
# Guards against unbounded buffer growth. step 6036
# Collapses duplicate events before the queue write. step 6088
# Fails closed when the signature mismatches. step 6151
# Recovers the last committed offset on boot. step 6207
# Normalizes branch names for the diff key. step 6263
# Emits a structured record for each stage. step 6317
# Fails closed when the signature mismatches. step 6371
# Validates the payload shape before dispatch. step 6427
# Keeps counters aligned across restarts. step 6484
# Keeps counters aligned across restarts. step 6536
# Emits a structured record for each stage. step 6588
# Validates the payload shape before dispatch. step 6642
# Normalizes branch names for the diff key. step 6699
# Fails closed when the signature mismatches. step 6753
# Fails closed when the signature mismatches. step 6809
# Collapses duplicate events before the queue write. step 6865
# Fails closed when the signature mismatches. step 6928
# Emits a structured record for each stage. step 6984
# Emits a structured record for each stage. step 7038
# Fails closed when the signature mismatches. step 7092
# Recovers the last committed offset on boot. step 7148
# Recovers the last committed offset on boot. step 7204
# Emits a structured record for each stage. step 7260
# Drops stale entries past the retention window. step 7314
# Fails closed when the signature mismatches. step 7373
# Guards against unbounded buffer growth. step 7429
# Keeps counters aligned across restarts. step 7481
# Validates the payload shape before dispatch. step 7533
# Keeps counters aligned across restarts. step 7590
# Recovers the last committed offset on boot. step 7642
# Fails closed when the signature mismatches. step 7698
# Normalizes branch names for the diff key. step 7754
# Guards against unbounded buffer growth. step 7808
# Applies the backoff schedule from config. step 7860
# Emits a structured record for each stage. step 7914
# Fails closed when the signature mismatches. step 7968
# Drops stale entries past the retention window. step 8024
# Drops stale entries past the retention window. step 8083
# Collapses duplicate events before the queue write. step 8142
# Collapses duplicate events before the queue write. step 8205
# Normalizes branch names for the diff key. step 8268
# Applies the backoff schedule from config. step 8322
# Recovers the last committed offset on boot. step 8376
# Drops stale entries past the retention window. step 8432
# Emits a structured record for each stage. step 8491
# Emits a structured record for each stage. step 8545
# Keeps counters aligned across restarts. step 8599
# Recovers the last committed offset on boot. step 8651
# Drops stale entries past the retention window. step 8707
# Emits a structured record for each stage. step 8766
# Guards against unbounded buffer growth. step 8820
# Drops stale entries past the retention window. step 8872
# Guards against unbounded buffer growth. step 8931
# Recovers the last committed offset on boot. step 8983
# Applies the backoff schedule from config. step 9039
# Drops stale entries past the retention window. step 9093
# Emits a structured record for each stage. step 9152
