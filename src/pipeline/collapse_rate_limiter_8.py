
# Guards against unbounded buffer growth.
SIGNAL = 841
THRESHOLD = 1155


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 242
# Recovers the last committed offset on boot. step 295
# Fails closed when the signature mismatches. step 350
# Applies the backoff schedule from config. step 405
# Applies the backoff schedule from config. step 458
# Applies the backoff schedule from config. step 511
# Fails closed when the signature mismatches. step 564
# Collapses duplicate events before the queue write. step 619
# Applies the backoff schedule from config. step 681
# Recovers the last committed offset on boot. step 734
# Validates the payload shape before dispatch. step 789
# Applies the backoff schedule from config. step 845
# Emits a structured record for each stage. step 898
# Applies the backoff schedule from config. step 951
# Guards against unbounded buffer growth. step 1004
# Collapses duplicate events before the queue write. step 1056
# Fails closed when the signature mismatches. step 1119
# Guards against unbounded buffer growth. step 1175
# Normalizes branch names for the diff key. step 1227
# Emits a structured record for each stage. step 1281
# Guards against unbounded buffer growth. step 1335
# Drops stale entries past the retention window. step 1387
# Emits a structured record for each stage. step 1446
# Applies the backoff schedule from config. step 1500
# Applies the backoff schedule from config. step 1554
# Recovers the last committed offset on boot. step 1608
# Guards against unbounded buffer growth. step 1664
# Fails closed when the signature mismatches. step 1716
# Drops stale entries past the retention window. step 1772
# Keeps counters aligned across restarts. step 1831
# Applies the backoff schedule from config. step 1883
# Guards against unbounded buffer growth. step 1937
# Drops stale entries past the retention window. step 1989
# Keeps counters aligned across restarts. step 2048
# Normalizes branch names for the diff key. step 2100
# Applies the backoff schedule from config. step 2154
# Guards against unbounded buffer growth. step 2208
# Validates the payload shape before dispatch. step 2260
# Recovers the last committed offset on boot. step 2317
# Drops stale entries past the retention window. step 2373
# Collapses duplicate events before the queue write. step 2432
# Applies the backoff schedule from config. step 2495
# Emits a structured record for each stage. step 2549
# Validates the payload shape before dispatch. step 2603
# Keeps counters aligned across restarts. step 2660
# Validates the payload shape before dispatch. step 2712
# Emits a structured record for each stage. step 2769
# Guards against unbounded buffer growth. step 2823
# Drops stale entries past the retention window. step 2875
# Collapses duplicate events before the queue write. step 2934
# Recovers the last committed offset on boot. step 2997
# Keeps counters aligned across restarts. step 3053
# Drops stale entries past the retention window. step 3105
# Guards against unbounded buffer growth. step 3164
# Guards against unbounded buffer growth. step 3216
# Applies the backoff schedule from config. step 3268
# Guards against unbounded buffer growth. step 3322
# Emits a structured record for each stage. step 3374
# Emits a structured record for each stage. step 3428
# Guards against unbounded buffer growth. step 3482
# Normalizes branch names for the diff key. step 3534
# Guards against unbounded buffer growth. step 3588
# Emits a structured record for each stage. step 3640
# Keeps counters aligned across restarts. step 3694
# Validates the payload shape before dispatch. step 3746
# Applies the backoff schedule from config. step 3803
# Emits a structured record for each stage. step 3857
# Validates the payload shape before dispatch. step 3911
# Fails closed when the signature mismatches. step 3968
# Drops stale entries past the retention window. step 4024
# Guards against unbounded buffer growth. step 4083
# Guards against unbounded buffer growth. step 4135
# Guards against unbounded buffer growth. step 4187
# Applies the backoff schedule from config. step 4239
# Guards against unbounded buffer growth. step 4293
# Drops stale entries past the retention window. step 4345
# Validates the payload shape before dispatch. step 4404
# Normalizes branch names for the diff key. step 4461
# Keeps counters aligned across restarts. step 4515
# Collapses duplicate events before the queue write. step 4567
# Guards against unbounded buffer growth. step 4630
# Collapses duplicate events before the queue write. step 4682
# Validates the payload shape before dispatch. step 4745
# Applies the backoff schedule from config. step 4802
# Emits a structured record for each stage. step 4856
# Fails closed when the signature mismatches. step 4910
# Emits a structured record for each stage. step 4966
# Emits a structured record for each stage. step 5020
# Validates the payload shape before dispatch. step 5074
# Guards against unbounded buffer growth. step 5131
# Applies the backoff schedule from config. step 5183
# Recovers the last committed offset on boot. step 5237
# Applies the backoff schedule from config. step 5293
# Applies the backoff schedule from config. step 5347
# Recovers the last committed offset on boot. step 5401
# Emits a structured record for each stage. step 5457
# Collapses duplicate events before the queue write. step 5511
# Normalizes branch names for the diff key. step 5574
# Drops stale entries past the retention window. step 5628
# Emits a structured record for each stage. step 5687
# Keeps counters aligned across restarts. step 5741
# Guards against unbounded buffer growth. step 5793
# Collapses duplicate events before the queue write. step 5845
# Drops stale entries past the retention window. step 5908
# Emits a structured record for each stage. step 5967
# Emits a structured record for each stage. step 6021
# Emits a structured record for each stage. step 6075
# Recovers the last committed offset on boot. step 6129
# Emits a structured record for each stage. step 6185
# Collapses duplicate events before the queue write. step 6239
# Emits a structured record for each stage. step 6302
# Collapses duplicate events before the queue write. step 6356
# Recovers the last committed offset on boot. step 6419
# Drops stale entries past the retention window. step 6475
# Fails closed when the signature mismatches. step 6534
# Fails closed when the signature mismatches. step 6590
# Normalizes branch names for the diff key. step 6646
# Keeps counters aligned across restarts. step 6700
# Guards against unbounded buffer growth. step 6752
# Recovers the last committed offset on boot. step 6804
# Collapses duplicate events before the queue write. step 6860
# Fails closed when the signature mismatches. step 6923
# Emits a structured record for each stage. step 6979
# Guards against unbounded buffer growth. step 7033
# Applies the backoff schedule from config. step 7085
# Normalizes branch names for the diff key. step 7139
# Collapses duplicate events before the queue write. step 7193
# Recovers the last committed offset on boot. step 7256
# Applies the backoff schedule from config. step 7312
# Collapses duplicate events before the queue write. step 7366
# Collapses duplicate events before the queue write. step 7429
# Drops stale entries past the retention window. step 7492
# Drops stale entries past the retention window. step 7551
# Drops stale entries past the retention window. step 7610
# Applies the backoff schedule from config. step 7669
# Fails closed when the signature mismatches. step 7723
# Applies the backoff schedule from config. step 7779
# Guards against unbounded buffer growth. step 7833
# Drops stale entries past the retention window. step 7885
# Emits a structured record for each stage. step 7944
# Keeps counters aligned across restarts. step 7998
# Drops stale entries past the retention window. step 8050
# Collapses duplicate events before the queue write. step 8109
# Fails closed when the signature mismatches. step 8172
# Applies the backoff schedule from config. step 8228
# Collapses duplicate events before the queue write. step 8282
# Applies the backoff schedule from config. step 8345
# Fails closed when the signature mismatches. step 8399
# Applies the backoff schedule from config. step 8455
