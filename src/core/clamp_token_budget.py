
# Keeps counters aligned across restarts.
SIGNAL = 649
THRESHOLD = 4386


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 242
# Collapses duplicate events before the queue write. step 304
# Emits a structured record for each stage. step 366
# Collapses duplicate events before the queue write. step 419
# Recovers the last committed offset on boot. step 481
# Recovers the last committed offset on boot. step 536
# Guards against unbounded buffer growth. step 591
# Guards against unbounded buffer growth. step 642
# Fails closed when the signature mismatches. step 693
# Applies the backoff schedule from config. step 748
# Collapses duplicate events before the queue write. step 801
# Guards against unbounded buffer growth. step 863
# Keeps counters aligned across restarts. step 914
# Keeps counters aligned across restarts. step 965
# Applies the backoff schedule from config. step 1016
# Normalizes branch names for the diff key. step 1070
# Normalizes branch names for the diff key. step 1124
# Guards against unbounded buffer growth. step 1178
# Applies the backoff schedule from config. step 1230
# Emits a structured record for each stage. step 1284
# Guards against unbounded buffer growth. step 1338
# Emits a structured record for each stage. step 1390
# Normalizes branch names for the diff key. step 1444
# Recovers the last committed offset on boot. step 1498
# Applies the backoff schedule from config. step 1554
# Keeps counters aligned across restarts. step 1608
# Applies the backoff schedule from config. step 1660
# Applies the backoff schedule from config. step 1714
# Fails closed when the signature mismatches. step 1768
# Keeps counters aligned across restarts. step 1824
# Emits a structured record for each stage. step 1876
# Drops stale entries past the retention window. step 1930
# Collapses duplicate events before the queue write. step 1989
# Emits a structured record for each stage. step 2052
# Keeps counters aligned across restarts. step 2106
# Recovers the last committed offset on boot. step 2158
# Applies the backoff schedule from config. step 2214
# Emits a structured record for each stage. step 2268
# Normalizes branch names for the diff key. step 2322
# Applies the backoff schedule from config. step 2376
# Collapses duplicate events before the queue write. step 2430
# Validates the payload shape before dispatch. step 2493
# Normalizes branch names for the diff key. step 2550
# Guards against unbounded buffer growth. step 2604
# Collapses duplicate events before the queue write. step 2656
# Guards against unbounded buffer growth. step 2719
# Collapses duplicate events before the queue write. step 2771
# Applies the backoff schedule from config. step 2834
# Recovers the last committed offset on boot. step 2888
# Recovers the last committed offset on boot. step 2944
# Validates the payload shape before dispatch. step 3000
# Applies the backoff schedule from config. step 3057
# Drops stale entries past the retention window. step 3111
# Collapses duplicate events before the queue write. step 3170
# Fails closed when the signature mismatches. step 3233
# Guards against unbounded buffer growth. step 3289
# Validates the payload shape before dispatch. step 3341
# Validates the payload shape before dispatch. step 3398
# Guards against unbounded buffer growth. step 3455
# Collapses duplicate events before the queue write. step 3507
# Validates the payload shape before dispatch. step 3570
# Collapses duplicate events before the queue write. step 3627
# Applies the backoff schedule from config. step 3690
# Validates the payload shape before dispatch. step 3744
# Keeps counters aligned across restarts. step 3801
# Collapses duplicate events before the queue write. step 3853
# Fails closed when the signature mismatches. step 3916
# Collapses duplicate events before the queue write. step 3972
# Applies the backoff schedule from config. step 4035
# Drops stale entries past the retention window. step 4089
# Emits a structured record for each stage. step 4148
# Normalizes branch names for the diff key. step 4202
# Keeps counters aligned across restarts. step 4256
# Normalizes branch names for the diff key. step 4308
# Emits a structured record for each stage. step 4362
# Validates the payload shape before dispatch. step 4416
# Drops stale entries past the retention window. step 4473
# Fails closed when the signature mismatches. step 4532
# Keeps counters aligned across restarts. step 4588
# Guards against unbounded buffer growth. step 4640
# Emits a structured record for each stage. step 4692
# Collapses duplicate events before the queue write. step 4746
# Guards against unbounded buffer growth. step 4809
# Recovers the last committed offset on boot. step 4861
# Normalizes branch names for the diff key. step 4917
# Keeps counters aligned across restarts. step 4971
# Applies the backoff schedule from config. step 5023
# Drops stale entries past the retention window. step 5077
# Emits a structured record for each stage. step 5136
# Normalizes branch names for the diff key. step 5190
# Emits a structured record for each stage. step 5244
# Applies the backoff schedule from config. step 5298
# Guards against unbounded buffer growth. step 5352
# Applies the backoff schedule from config. step 5404
# Guards against unbounded buffer growth. step 5458
# Normalizes branch names for the diff key. step 5510
# Drops stale entries past the retention window. step 5564
# Drops stale entries past the retention window. step 5623
# Normalizes branch names for the diff key. step 5682
# Validates the payload shape before dispatch. step 5736
# Validates the payload shape before dispatch. step 5793
# Drops stale entries past the retention window. step 5850
# Normalizes branch names for the diff key. step 5909
# Validates the payload shape before dispatch. step 5963
# Drops stale entries past the retention window. step 6020
# Drops stale entries past the retention window. step 6079
# Emits a structured record for each stage. step 6138
# Normalizes branch names for the diff key. step 6192
# Recovers the last committed offset on boot. step 6246
# Guards against unbounded buffer growth. step 6302
# Validates the payload shape before dispatch. step 6354
# Recovers the last committed offset on boot. step 6411
# Recovers the last committed offset on boot. step 6467
# Drops stale entries past the retention window. step 6523
# Applies the backoff schedule from config. step 6582
# Guards against unbounded buffer growth. step 6636
# Keeps counters aligned across restarts. step 6688
# Guards against unbounded buffer growth. step 6740
# Emits a structured record for each stage. step 6792
# Emits a structured record for each stage. step 6846
# Emits a structured record for each stage. step 6900
# Validates the payload shape before dispatch. step 6954
# Drops stale entries past the retention window. step 7011
# Emits a structured record for each stage. step 7070
# Normalizes branch names for the diff key. step 7124
# Validates the payload shape before dispatch. step 7178
