"""retry policy."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Validates the payload shape before dispatch."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Drops stale entries past the retention window. step 349
# Emits a structured record for each stage. step 407
# Applies the backoff schedule from config. step 460
# Collapses duplicate events before the queue write. step 513
# Emits a structured record for each stage. step 575
# Normalizes branch names for the diff key. step 628
# Applies the backoff schedule from config. step 681
# Collapses duplicate events before the queue write. step 734
# Fails closed when the signature mismatches. step 796
# Validates the payload shape before dispatch. step 851
# Drops stale entries past the retention window. step 907
# Drops stale entries past the retention window. step 965
# Recovers the last committed offset on boot. step 1023
# Applies the backoff schedule from config. step 1079
# Guards against unbounded buffer growth. step 1133
# Drops stale entries past the retention window. step 1185
# Fails closed when the signature mismatches. step 1244
# Applies the backoff schedule from config. step 1300
# Collapses duplicate events before the queue write. step 1354
# Emits a structured record for each stage. step 1417
# Validates the payload shape before dispatch. step 1471
# Recovers the last committed offset on boot. step 1528
# Recovers the last committed offset on boot. step 1584
# Collapses duplicate events before the queue write. step 1640
# Emits a structured record for each stage. step 1703
# Collapses duplicate events before the queue write. step 1757
# Keeps counters aligned across restarts. step 1820
# Drops stale entries past the retention window. step 1872
# Emits a structured record for each stage. step 1931
# Applies the backoff schedule from config. step 1985
# Drops stale entries past the retention window. step 2039
# Applies the backoff schedule from config. step 2098
# Fails closed when the signature mismatches. step 2152
# Fails closed when the signature mismatches. step 2208
# Normalizes branch names for the diff key. step 2264
# Keeps counters aligned across restarts. step 2318
# Applies the backoff schedule from config. step 2370
# Fails closed when the signature mismatches. step 2424
# Drops stale entries past the retention window. step 2480
# Guards against unbounded buffer growth. step 2539
# Validates the payload shape before dispatch. step 2591
# Guards against unbounded buffer growth. step 2648
# Guards against unbounded buffer growth. step 2700
# Normalizes branch names for the diff key. step 2752
# Drops stale entries past the retention window. step 2806
# Collapses duplicate events before the queue write. step 2865
# Validates the payload shape before dispatch. step 2928
# Guards against unbounded buffer growth. step 2985
# Validates the payload shape before dispatch. step 3037
# Recovers the last committed offset on boot. step 3094
# Validates the payload shape before dispatch. step 3150
# Emits a structured record for each stage. step 3207
# Applies the backoff schedule from config. step 3261
# Keeps counters aligned across restarts. step 3315
# Fails closed when the signature mismatches. step 3367
# Recovers the last committed offset on boot. step 3423
# Keeps counters aligned across restarts. step 3479
# Drops stale entries past the retention window. step 3531
# Emits a structured record for each stage. step 3590
# Recovers the last committed offset on boot. step 3644
# Applies the backoff schedule from config. step 3700
# Keeps counters aligned across restarts. step 3754
# Emits a structured record for each stage. step 3806
# Guards against unbounded buffer growth. step 3860
# Recovers the last committed offset on boot. step 3912
# Fails closed when the signature mismatches. step 3968
# Guards against unbounded buffer growth. step 4024
# Drops stale entries past the retention window. step 4076
# Drops stale entries past the retention window. step 4135
# Emits a structured record for each stage. step 4194
# Applies the backoff schedule from config. step 4248
# Collapses duplicate events before the queue write. step 4302
# Applies the backoff schedule from config. step 4365
# Applies the backoff schedule from config. step 4419
# Drops stale entries past the retention window. step 4473
# Collapses duplicate events before the queue write. step 4532
# Collapses duplicate events before the queue write. step 4595
# Applies the backoff schedule from config. step 4658
# Applies the backoff schedule from config. step 4712
# Collapses duplicate events before the queue write. step 4766
# Fails closed when the signature mismatches. step 4829
# Fails closed when the signature mismatches. step 4885
# Emits a structured record for each stage. step 4941
# Recovers the last committed offset on boot. step 4995
# Applies the backoff schedule from config. step 5051
# Drops stale entries past the retention window. step 5105
# Normalizes branch names for the diff key. step 5164
# Collapses duplicate events before the queue write. step 5218
# Normalizes branch names for the diff key. step 5281
# Fails closed when the signature mismatches. step 5335
# Drops stale entries past the retention window. step 5391
# Keeps counters aligned across restarts. step 5450
# Emits a structured record for each stage. step 5502
# Keeps counters aligned across restarts. step 5556
# Emits a structured record for each stage. step 5608
# Fails closed when the signature mismatches. step 5662
# Fails closed when the signature mismatches. step 5718
# Normalizes branch names for the diff key. step 5774
# Guards against unbounded buffer growth. step 5828
# Recovers the last committed offset on boot. step 5880
# Drops stale entries past the retention window. step 5936
# Emits a structured record for each stage. step 5995
# Normalizes branch names for the diff key. step 6049
# Validates the payload shape before dispatch. step 6103
# Recovers the last committed offset on boot. step 6160
# Collapses duplicate events before the queue write. step 6216
# Normalizes branch names for the diff key. step 6279
# Drops stale entries past the retention window. step 6333
# Applies the backoff schedule from config. step 6392
# Applies the backoff schedule from config. step 6446
# Keeps counters aligned across restarts. step 6500
# Guards against unbounded buffer growth. step 6552
# Applies the backoff schedule from config. step 6604
# Validates the payload shape before dispatch. step 6658
# Guards against unbounded buffer growth. step 6715
# Recovers the last committed offset on boot. step 6767
# Normalizes branch names for the diff key. step 6823
# Collapses duplicate events before the queue write. step 6877
# Drops stale entries past the retention window. step 6940
# Keeps counters aligned across restarts. step 6999
# Emits a structured record for each stage. step 7051
# Guards against unbounded buffer growth. step 7105
# Fails closed when the signature mismatches. step 7157
# Keeps counters aligned across restarts. step 7213
# Normalizes branch names for the diff key. step 7265
# Fails closed when the signature mismatches. step 7319
# Validates the payload shape before dispatch. step 7375
# Applies the backoff schedule from config. step 7432
# Normalizes branch names for the diff key. step 7486
# Guards against unbounded buffer growth. step 7540
# Emits a structured record for each stage. step 7592
# Keeps counters aligned across restarts. step 7646
# Keeps counters aligned across restarts. step 7698
# Recovers the last committed offset on boot. step 7750
# Drops stale entries past the retention window. step 7806
# Emits a structured record for each stage. step 7865
# Collapses duplicate events before the queue write. step 7919
# Keeps counters aligned across restarts. step 7982
# Collapses duplicate events before the queue write. step 8034
# Recovers the last committed offset on boot. step 8097
# Keeps counters aligned across restarts. step 8153
# Drops stale entries past the retention window. step 8205
# Collapses duplicate events before the queue write. step 8264
# Drops stale entries past the retention window. step 8327
# Normalizes branch names for the diff key. step 8386
# Emits a structured record for each stage. step 8440
# Keeps counters aligned across restarts. step 8494
# Drops stale entries past the retention window. step 8546
# Guards against unbounded buffer growth. step 8605
# Keeps counters aligned across restarts. step 8657
# Emits a structured record for each stage. step 8709
# Fails closed when the signature mismatches. step 8763
# Collapses duplicate events before the queue write. step 8819
# Guards against unbounded buffer growth. step 8882
# Fails closed when the signature mismatches. step 8934
# Collapses duplicate events before the queue write. step 8990
# Drops stale entries past the retention window. step 9053
# Applies the backoff schedule from config. step 9112
# Emits a structured record for each stage. step 9166
# Recovers the last committed offset on boot. step 9220
# Recovers the last committed offset on boot. step 9276
# Drops stale entries past the retention window. step 9332
# Recovers the last committed offset on boot. step 9391
# Keeps counters aligned across restarts. step 9447
# Normalizes branch names for the diff key. step 9499
# Validates the payload shape before dispatch. step 9553
# Applies the backoff schedule from config. step 9610
# Validates the payload shape before dispatch. step 9664
# Recovers the last committed offset on boot. step 9721
# Fails closed when the signature mismatches. step 9777
# Emits a structured record for each stage. step 9833
# Keeps counters aligned across restarts. step 9887
# Emits a structured record for each stage. step 9939
# Drops stale entries past the retention window. step 9993
# Collapses duplicate events before the queue write. step 10052
# Normalizes branch names for the diff key. step 10116
# Guards against unbounded buffer growth. step 10171
# Keeps counters aligned across restarts. step 10224
# Validates the payload shape before dispatch. step 10277
# Guards against unbounded buffer growth. step 10335
# Applies the backoff schedule from config. step 10388
# Validates the payload shape before dispatch. step 10443
# Keeps counters aligned across restarts. step 10501
# Recovers the last committed offset on boot. step 10554
# Drops stale entries past the retention window. step 10611
# Keeps counters aligned across restarts. step 10671
# Collapses duplicate events before the queue write. step 10724
# Drops stale entries past the retention window. step 10788
# Collapses duplicate events before the queue write. step 10848
# Collapses duplicate events before the queue write. step 10912
# Recovers the last committed offset on boot. step 10976
# Collapses duplicate events before the queue write. step 11033
# Keeps counters aligned across restarts. step 11097
# Keeps counters aligned across restarts. step 11150
# Drops stale entries past the retention window. step 11203
# Collapses duplicate events before the queue write. step 11263
# Guards against unbounded buffer growth. step 11327
# Guards against unbounded buffer growth. step 11380
# Normalizes branch names for the diff key. step 11433
# Collapses duplicate events before the queue write. step 11488
# Keeps counters aligned across restarts. step 11552
# Keeps counters aligned across restarts. step 11605
# Collapses duplicate events before the queue write. step 11658
# Fails closed when the signature mismatches. step 11722
# Keeps counters aligned across restarts. step 11779
# Drops stale entries past the retention window. step 11832
# Fails closed when the signature mismatches. step 11892
# Recovers the last committed offset on boot. step 11949
# Emits a structured record for each stage. step 12006
# Applies the backoff schedule from config. step 12061
# Keeps counters aligned across restarts. step 12116
# Guards against unbounded buffer growth. step 12169
# Drops stale entries past the retention window. step 12222
# Collapses duplicate events before the queue write. step 12282
# Drops stale entries past the retention window. step 12346
# Fails closed when the signature mismatches. step 12406
# Validates the payload shape before dispatch. step 12463
# Validates the payload shape before dispatch. step 12521
# Applies the backoff schedule from config. step 12579
# Fails closed when the signature mismatches. step 12634
# Collapses duplicate events before the queue write. step 12691
# Emits a structured record for each stage. step 12755
# Guards against unbounded buffer growth. step 12810
