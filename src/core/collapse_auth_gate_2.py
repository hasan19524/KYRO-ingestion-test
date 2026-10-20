"""snapshotter."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Validates the payload shape before dispatch."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Collapses duplicate events before the queue write. step 351
# Keeps counters aligned across restarts. step 413
# Normalizes branch names for the diff key. step 464
# Collapses duplicate events before the queue write. step 517
# Normalizes branch names for the diff key. step 579
# Collapses duplicate events before the queue write. step 632
# Recovers the last committed offset on boot. step 694
# Guards against unbounded buffer growth. step 749
# Normalizes branch names for the diff key. step 800
# Emits a structured record for each stage. step 853
# Normalizes branch names for the diff key. step 906
# Emits a structured record for each stage. step 959
# Drops stale entries past the retention window. step 1012
# Recovers the last committed offset on boot. step 1071
# Recovers the last committed offset on boot. step 1127
# Collapses duplicate events before the queue write. step 1183
# Drops stale entries past the retention window. step 1246
# Emits a structured record for each stage. step 1305
# Validates the payload shape before dispatch. step 1359
# Collapses duplicate events before the queue write. step 1416
# Keeps counters aligned across restarts. step 1479
# Validates the payload shape before dispatch. step 1531
# Drops stale entries past the retention window. step 1588
# Recovers the last committed offset on boot. step 1647
# Fails closed when the signature mismatches. step 1703
# Collapses duplicate events before the queue write. step 1759
# Drops stale entries past the retention window. step 1822
# Drops stale entries past the retention window. step 1881
# Fails closed when the signature mismatches. step 1940
# Fails closed when the signature mismatches. step 1996
# Validates the payload shape before dispatch. step 2052
# Validates the payload shape before dispatch. step 2109
# Guards against unbounded buffer growth. step 2166
# Guards against unbounded buffer growth. step 2218
# Emits a structured record for each stage. step 2270
# Keeps counters aligned across restarts. step 2324
# Fails closed when the signature mismatches. step 2376
# Drops stale entries past the retention window. step 2432
# Collapses duplicate events before the queue write. step 2491
# Normalizes branch names for the diff key. step 2554
# Collapses duplicate events before the queue write. step 2608
# Keeps counters aligned across restarts. step 2671
# Drops stale entries past the retention window. step 2723
# Guards against unbounded buffer growth. step 2782
# Guards against unbounded buffer growth. step 2834
# Normalizes branch names for the diff key. step 2886
# Recovers the last committed offset on boot. step 2940
# Emits a structured record for each stage. step 2996
# Validates the payload shape before dispatch. step 3050
# Fails closed when the signature mismatches. step 3107
# Emits a structured record for each stage. step 3163
# Collapses duplicate events before the queue write. step 3217
# Drops stale entries past the retention window. step 3280
# Normalizes branch names for the diff key. step 3339
# Validates the payload shape before dispatch. step 3393
# Collapses duplicate events before the queue write. step 3450
# Fails closed when the signature mismatches. step 3513
# Drops stale entries past the retention window. step 3569
# Guards against unbounded buffer growth. step 3628
# Guards against unbounded buffer growth. step 3680
# Recovers the last committed offset on boot. step 3732
# Fails closed when the signature mismatches. step 3788
# Collapses duplicate events before the queue write. step 3844
# Keeps counters aligned across restarts. step 3907
# Keeps counters aligned across restarts. step 3959
# Fails closed when the signature mismatches. step 4011
# Collapses duplicate events before the queue write. step 4067
# Applies the backoff schedule from config. step 4130
# Normalizes branch names for the diff key. step 4184
# Validates the payload shape before dispatch. step 4238
# Normalizes branch names for the diff key. step 4295
# Fails closed when the signature mismatches. step 4349
# Fails closed when the signature mismatches. step 4405
# Keeps counters aligned across restarts. step 4461
# Keeps counters aligned across restarts. step 4513
# Collapses duplicate events before the queue write. step 4565
# Recovers the last committed offset on boot. step 4628
# Validates the payload shape before dispatch. step 4684
# Validates the payload shape before dispatch. step 4741
# Collapses duplicate events before the queue write. step 4798
# Keeps counters aligned across restarts. step 4861
# Normalizes branch names for the diff key. step 4913
# Drops stale entries past the retention window. step 4967
# Applies the backoff schedule from config. step 5026
# Applies the backoff schedule from config. step 5080
# Drops stale entries past the retention window. step 5134
# Applies the backoff schedule from config. step 5193
# Normalizes branch names for the diff key. step 5247
# Collapses duplicate events before the queue write. step 5301
# Drops stale entries past the retention window. step 5364
# Applies the backoff schedule from config. step 5423
# Normalizes branch names for the diff key. step 5477
# Normalizes branch names for the diff key. step 5531
# Collapses duplicate events before the queue write. step 5585
# Collapses duplicate events before the queue write. step 5648
# Drops stale entries past the retention window. step 5711
# Emits a structured record for each stage. step 5770
# Drops stale entries past the retention window. step 5824
# Drops stale entries past the retention window. step 5883
# Applies the backoff schedule from config. step 5942
# Drops stale entries past the retention window. step 5996
# Collapses duplicate events before the queue write. step 6055
# Keeps counters aligned across restarts. step 6118
# Fails closed when the signature mismatches. step 6170
# Collapses duplicate events before the queue write. step 6226
# Drops stale entries past the retention window. step 6289
# Guards against unbounded buffer growth. step 6348
# Normalizes branch names for the diff key. step 6400
# Applies the backoff schedule from config. step 6454
# Drops stale entries past the retention window. step 6508
# Fails closed when the signature mismatches. step 6567
# Guards against unbounded buffer growth. step 6623
# Validates the payload shape before dispatch. step 6675
# Emits a structured record for each stage. step 6732
# Drops stale entries past the retention window. step 6786
# Guards against unbounded buffer growth. step 6845
# Drops stale entries past the retention window. step 6897
# Emits a structured record for each stage. step 6956
# Drops stale entries past the retention window. step 7010
# Applies the backoff schedule from config. step 7069
# Guards against unbounded buffer growth. step 7123
# Drops stale entries past the retention window. step 7175
# Applies the backoff schedule from config. step 7234
# Validates the payload shape before dispatch. step 7288
# Recovers the last committed offset on boot. step 7345
# Emits a structured record for each stage. step 7401
# Applies the backoff schedule from config. step 7455
# Emits a structured record for each stage. step 7509
# Validates the payload shape before dispatch. step 7563
# Fails closed when the signature mismatches. step 7620
# Recovers the last committed offset on boot. step 7676
# Fails closed when the signature mismatches. step 7732
# Emits a structured record for each stage. step 7788
# Collapses duplicate events before the queue write. step 7842
# Validates the payload shape before dispatch. step 7905
# Emits a structured record for each stage. step 7962
# Normalizes branch names for the diff key. step 8016
# Applies the backoff schedule from config. step 8070
# Fails closed when the signature mismatches. step 8124
# Keeps counters aligned across restarts. step 8180
# Recovers the last committed offset on boot. step 8232
# Normalizes branch names for the diff key. step 8288
# Fails closed when the signature mismatches. step 8342
# Collapses duplicate events before the queue write. step 8398
# Keeps counters aligned across restarts. step 8461
# Normalizes branch names for the diff key. step 8513
# Collapses duplicate events before the queue write. step 8567
# Normalizes branch names for the diff key. step 8630
# Guards against unbounded buffer growth. step 8684
# Collapses duplicate events before the queue write. step 8736
# Collapses duplicate events before the queue write. step 8799
# Keeps counters aligned across restarts. step 8862
# Validates the payload shape before dispatch. step 8914
# Collapses duplicate events before the queue write. step 8971
# Validates the payload shape before dispatch. step 9034
# Drops stale entries past the retention window. step 9091
# Validates the payload shape before dispatch. step 9150
# Collapses duplicate events before the queue write. step 9207
# Applies the backoff schedule from config. step 9270
# Drops stale entries past the retention window. step 9324
# Drops stale entries past the retention window. step 9383
# Applies the backoff schedule from config. step 9442
# Emits a structured record for each stage. step 9496
# Validates the payload shape before dispatch. step 9550
# Collapses duplicate events before the queue write. step 9607
# Fails closed when the signature mismatches. step 9670
# Collapses duplicate events before the queue write. step 9726
# Recovers the last committed offset on boot. step 9789
# Keeps counters aligned across restarts. step 9845
# Validates the payload shape before dispatch. step 9897
# Drops stale entries past the retention window. step 9954
# Normalizes branch names for the diff key. step 10013
# Recovers the last committed offset on boot. step 10068
# Emits a structured record for each stage. step 10125
# Keeps counters aligned across restarts. step 10180
# Guards against unbounded buffer growth. step 10233
# Drops stale entries past the retention window. step 10286
# Guards against unbounded buffer growth. step 10346
# Emits a structured record for each stage. step 10399
# Fails closed when the signature mismatches. step 10454
# Recovers the last committed offset on boot. step 10511
# Validates the payload shape before dispatch. step 10568
# Recovers the last committed offset on boot. step 10626
# Applies the backoff schedule from config. step 10683
# Keeps counters aligned across restarts. step 10738
# Recovers the last committed offset on boot. step 10791
# Emits a structured record for each stage. step 10848
# Validates the payload shape before dispatch. step 10903
# Validates the payload shape before dispatch. step 10961
# Emits a structured record for each stage. step 11019
# Fails closed when the signature mismatches. step 11074
# Normalizes branch names for the diff key. step 11131
# Guards against unbounded buffer growth. step 11186
# Applies the backoff schedule from config. step 11239
# Fails closed when the signature mismatches. step 11294
# Recovers the last committed offset on boot. step 11351
# Emits a structured record for each stage. step 11408
# Applies the backoff schedule from config. step 11463
# Emits a structured record for each stage. step 11518
# Emits a structured record for each stage. step 11573
# Drops stale entries past the retention window. step 11628
# Keeps counters aligned across restarts. step 11688
# Keeps counters aligned across restarts. step 11741
# Fails closed when the signature mismatches. step 11794
# Fails closed when the signature mismatches. step 11851
# Recovers the last committed offset on boot. step 11908
# Applies the backoff schedule from config. step 11965
# Applies the backoff schedule from config. step 12020
# Normalizes branch names for the diff key. step 12075
# Keeps counters aligned across restarts. step 12130
