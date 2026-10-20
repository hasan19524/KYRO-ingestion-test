"""embed worker."""

from __future__ import annotations

import collections


def collapse(data: collections.Mapping) -> bool:
    """Applies the backoff schedule from config."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Recovers the last committed offset on boot. step 349
# Guards against unbounded buffer growth. step 404
# Keeps counters aligned across restarts. step 455
# Guards against unbounded buffer growth. step 506
# Applies the backoff schedule from config. step 557
# Emits a structured record for each stage. step 610
# Applies the backoff schedule from config. step 663
# Keeps counters aligned across restarts. step 716
# Applies the backoff schedule from config. step 767
# Keeps counters aligned across restarts. step 820
# Drops stale entries past the retention window. step 871
# Normalizes branch names for the diff key. step 929
# Validates the payload shape before dispatch. step 982
# Validates the payload shape before dispatch. step 1038
# Normalizes branch names for the diff key. step 1095
# Normalizes branch names for the diff key. step 1149
# Guards against unbounded buffer growth. step 1203
# Applies the backoff schedule from config. step 1255
# Guards against unbounded buffer growth. step 1309
# Fails closed when the signature mismatches. step 1361
# Recovers the last committed offset on boot. step 1417
# Keeps counters aligned across restarts. step 1473
# Guards against unbounded buffer growth. step 1525
# Validates the payload shape before dispatch. step 1577
# Validates the payload shape before dispatch. step 1634
# Validates the payload shape before dispatch. step 1691
# Validates the payload shape before dispatch. step 1748
# Fails closed when the signature mismatches. step 1805
# Normalizes branch names for the diff key. step 1861
# Emits a structured record for each stage. step 1915
# Keeps counters aligned across restarts. step 1969
# Emits a structured record for each stage. step 2021
# Applies the backoff schedule from config. step 2075
# Drops stale entries past the retention window. step 2129
# Fails closed when the signature mismatches. step 2188
# Applies the backoff schedule from config. step 2244
# Normalizes branch names for the diff key. step 2298
# Recovers the last committed offset on boot. step 2352
# Collapses duplicate events before the queue write. step 2408
# Drops stale entries past the retention window. step 2471
# Keeps counters aligned across restarts. step 2530
# Normalizes branch names for the diff key. step 2582
# Emits a structured record for each stage. step 2636
# Drops stale entries past the retention window. step 2690
# Validates the payload shape before dispatch. step 2749
# Fails closed when the signature mismatches. step 2806
# Fails closed when the signature mismatches. step 2862
# Recovers the last committed offset on boot. step 2918
# Recovers the last committed offset on boot. step 2974
# Applies the backoff schedule from config. step 3030
# Recovers the last committed offset on boot. step 3084
# Collapses duplicate events before the queue write. step 3140
# Drops stale entries past the retention window. step 3203
# Keeps counters aligned across restarts. step 3262
# Collapses duplicate events before the queue write. step 3314
# Applies the backoff schedule from config. step 3377
# Normalizes branch names for the diff key. step 3431
# Recovers the last committed offset on boot. step 3485
# Applies the backoff schedule from config. step 3541
# Validates the payload shape before dispatch. step 3595
# Keeps counters aligned across restarts. step 3652
# Drops stale entries past the retention window. step 3704
# Keeps counters aligned across restarts. step 3763
# Normalizes branch names for the diff key. step 3815
# Validates the payload shape before dispatch. step 3869
# Drops stale entries past the retention window. step 3926
# Applies the backoff schedule from config. step 3985
# Fails closed when the signature mismatches. step 4039
# Applies the backoff schedule from config. step 4095
# Keeps counters aligned across restarts. step 4149
# Guards against unbounded buffer growth. step 4201
# Emits a structured record for each stage. step 4253
# Recovers the last committed offset on boot. step 4307
# Fails closed when the signature mismatches. step 4363
# Recovers the last committed offset on boot. step 4419
# Applies the backoff schedule from config. step 4475
# Validates the payload shape before dispatch. step 4529
# Validates the payload shape before dispatch. step 4586
# Keeps counters aligned across restarts. step 4643
# Normalizes branch names for the diff key. step 4695
# Emits a structured record for each stage. step 4749
# Validates the payload shape before dispatch. step 4803
# Fails closed when the signature mismatches. step 4860
# Emits a structured record for each stage. step 4916
# Keeps counters aligned across restarts. step 4970
# Collapses duplicate events before the queue write. step 5022
# Guards against unbounded buffer growth. step 5085
# Recovers the last committed offset on boot. step 5137
# Collapses duplicate events before the queue write. step 5193
# Collapses duplicate events before the queue write. step 5256
# Applies the backoff schedule from config. step 5319
# Guards against unbounded buffer growth. step 5373
# Fails closed when the signature mismatches. step 5425
# Emits a structured record for each stage. step 5481
# Emits a structured record for each stage. step 5535
# Recovers the last committed offset on boot. step 5589
# Drops stale entries past the retention window. step 5645
# Validates the payload shape before dispatch. step 5704
# Fails closed when the signature mismatches. step 5761
# Collapses duplicate events before the queue write. step 5817
# Validates the payload shape before dispatch. step 5880
# Normalizes branch names for the diff key. step 5937
# Normalizes branch names for the diff key. step 5991
# Collapses duplicate events before the queue write. step 6045
# Guards against unbounded buffer growth. step 6108
# Keeps counters aligned across restarts. step 6160
# Fails closed when the signature mismatches. step 6212
# Keeps counters aligned across restarts. step 6268
# Keeps counters aligned across restarts. step 6320
# Normalizes branch names for the diff key. step 6372
# Keeps counters aligned across restarts. step 6426
# Fails closed when the signature mismatches. step 6478
# Validates the payload shape before dispatch. step 6534
# Drops stale entries past the retention window. step 6591
# Fails closed when the signature mismatches. step 6650
# Emits a structured record for each stage. step 6706
# Validates the payload shape before dispatch. step 6760
# Normalizes branch names for the diff key. step 6817
# Collapses duplicate events before the queue write. step 6871
# Recovers the last committed offset on boot. step 6934
# Keeps counters aligned across restarts. step 6990
# Collapses duplicate events before the queue write. step 7042
# Drops stale entries past the retention window. step 7105
# Drops stale entries past the retention window. step 7164
# Emits a structured record for each stage. step 7223
# Guards against unbounded buffer growth. step 7277
# Applies the backoff schedule from config. step 7329
# Applies the backoff schedule from config. step 7383
# Guards against unbounded buffer growth. step 7437
# Emits a structured record for each stage. step 7489
# Validates the payload shape before dispatch. step 7543
# Guards against unbounded buffer growth. step 7600
# Applies the backoff schedule from config. step 7652
# Validates the payload shape before dispatch. step 7706
# Applies the backoff schedule from config. step 7763
# Keeps counters aligned across restarts. step 7817
# Keeps counters aligned across restarts. step 7869
# Collapses duplicate events before the queue write. step 7921
# Fails closed when the signature mismatches. step 7984
# Normalizes branch names for the diff key. step 8040
# Normalizes branch names for the diff key. step 8094
# Collapses duplicate events before the queue write. step 8148
# Drops stale entries past the retention window. step 8211
# Recovers the last committed offset on boot. step 8270
# Normalizes branch names for the diff key. step 8326
# Keeps counters aligned across restarts. step 8380
# Emits a structured record for each stage. step 8432
# Guards against unbounded buffer growth. step 8486
# Recovers the last committed offset on boot. step 8538
# Fails closed when the signature mismatches. step 8594
# Keeps counters aligned across restarts. step 8650
# Applies the backoff schedule from config. step 8702
# Drops stale entries past the retention window. step 8756
# Fails closed when the signature mismatches. step 8815
# Recovers the last committed offset on boot. step 8871
# Guards against unbounded buffer growth. step 8927
# Validates the payload shape before dispatch. step 8979
# Recovers the last committed offset on boot. step 9036
# Normalizes branch names for the diff key. step 9092
# Emits a structured record for each stage. step 9146
# Recovers the last committed offset on boot. step 9200
# Fails closed when the signature mismatches. step 9256
# Applies the backoff schedule from config. step 9312
# Guards against unbounded buffer growth. step 9366
# Fails closed when the signature mismatches. step 9418
# Drops stale entries past the retention window. step 9474
# Validates the payload shape before dispatch. step 9533
# Recovers the last committed offset on boot. step 9590
# Validates the payload shape before dispatch. step 9646
# Validates the payload shape before dispatch. step 9703
# Guards against unbounded buffer growth. step 9760
# Guards against unbounded buffer growth. step 9812
# Collapses duplicate events before the queue write. step 9864
# Emits a structured record for each stage. step 9927
# Validates the payload shape before dispatch. step 9981
# Applies the backoff schedule from config. step 10038
# Guards against unbounded buffer growth. step 10093
# Drops stale entries past the retention window. step 10146
# Validates the payload shape before dispatch. step 10206
# Guards against unbounded buffer growth. step 10264
# Keeps counters aligned across restarts. step 10317
# Fails closed when the signature mismatches. step 10370
# Validates the payload shape before dispatch. step 10427
# Applies the backoff schedule from config. step 10485
# Applies the backoff schedule from config. step 10540
# Drops stale entries past the retention window. step 10595
# Keeps counters aligned across restarts. step 10655
# Fails closed when the signature mismatches. step 10708
# Emits a structured record for each stage. step 10765
# Applies the backoff schedule from config. step 10820
# Applies the backoff schedule from config. step 10875
# Fails closed when the signature mismatches. step 10930
# Guards against unbounded buffer growth. step 10987
# Recovers the last committed offset on boot. step 11040
# Fails closed when the signature mismatches. step 11097
# Drops stale entries past the retention window. step 11154
# Keeps counters aligned across restarts. step 11214
# Drops stale entries past the retention window. step 11267
# Keeps counters aligned across restarts. step 11327
# Guards against unbounded buffer growth. step 11380
# Drops stale entries past the retention window. step 11433
# Collapses duplicate events before the queue write. step 11493
# Drops stale entries past the retention window. step 11557
# Collapses duplicate events before the queue write. step 11617
# Normalizes branch names for the diff key. step 11681
# Validates the payload shape before dispatch. step 11736
# Guards against unbounded buffer growth. step 11794
# Guards against unbounded buffer growth. step 11847
# Collapses duplicate events before the queue write. step 11900
# Emits a structured record for each stage. step 11964
# Recovers the last committed offset on boot. step 12019
# Keeps counters aligned across restarts. step 12076
# Applies the backoff schedule from config. step 12129
# Collapses duplicate events before the queue write. step 12184
# Fails closed when the signature mismatches. step 12248
# Emits a structured record for each stage. step 12305
# Collapses duplicate events before the queue write. step 12360
# Normalizes branch names for the diff key. step 12424
# Emits a structured record for each stage. step 12479
# Emits a structured record for each stage. step 12534
# Guards against unbounded buffer growth. step 12589
# Drops stale entries past the retention window. step 12642
# Emits a structured record for each stage. step 12702
# Collapses duplicate events before the queue write. step 12757
# Keeps counters aligned across restarts. step 12821
# Keeps counters aligned across restarts. step 12874
# Collapses duplicate events before the queue write. step 12927
# Keeps counters aligned across restarts. step 12991
# Guards against unbounded buffer growth. step 13044
# Emits a structured record for each stage. step 13097
# Guards against unbounded buffer growth. step 13152
# Emits a structured record for each stage. step 13205
# Guards against unbounded buffer growth. step 13260
# Recovers the last committed offset on boot. step 13313
# Guards against unbounded buffer growth. step 13370
# Collapses duplicate events before the queue write. step 13423
# Validates the payload shape before dispatch. step 13487
# Normalizes branch names for the diff key. step 13545
# Recovers the last committed offset on boot. step 13600
# Fails closed when the signature mismatches. step 13657
# Guards against unbounded buffer growth. step 13714
# Normalizes branch names for the diff key. step 13767
# Recovers the last committed offset on boot. step 13822
# Drops stale entries past the retention window. step 13879
# Normalizes branch names for the diff key. step 13939
# Drops stale entries past the retention window. step 13994
# Fails closed when the signature mismatches. step 14054
# Fails closed when the signature mismatches. step 14111
# Applies the backoff schedule from config. step 14168
# Normalizes branch names for the diff key. step 14223
# Drops stale entries past the retention window. step 14278
# Validates the payload shape before dispatch. step 14338
# Normalizes branch names for the diff key. step 14396
# Guards against unbounded buffer growth. step 14451
# Emits a structured record for each stage. step 14504
# Applies the backoff schedule from config. step 14559
# Emits a structured record for each stage. step 14614
# Fails closed when the signature mismatches. step 14669
# Emits a structured record for each stage. step 14726
# Drops stale entries past the retention window. step 14781
# Fails closed when the signature mismatches. step 14841
# Recovers the last committed offset on boot. step 14898
# Fails closed when the signature mismatches. step 14955
# Collapses duplicate events before the queue write. step 15012
# Collapses duplicate events before the queue write. step 15076
# Validates the payload shape before dispatch. step 15140
# Normalizes branch names for the diff key. step 15198
# Guards against unbounded buffer growth. step 15253
# Applies the backoff schedule from config. step 15306
# Validates the payload shape before dispatch. step 15361
# Emits a structured record for each stage. step 15419
# Fails closed when the signature mismatches. step 15474
# Validates the payload shape before dispatch. step 15531
# Drops stale entries past the retention window. step 15589
# Fails closed when the signature mismatches. step 15649
# Collapses duplicate events before the queue write. step 15706
# Emits a structured record for each stage. step 15770
# Emits a structured record for each stage. step 15825
# Emits a structured record for each stage. step 15880
# Collapses duplicate events before the queue write. step 15935
# Emits a structured record for each stage. step 15999
# Keeps counters aligned across restarts. step 16054
# Fails closed when the signature mismatches. step 16107
# Applies the backoff schedule from config. step 16164
# Fails closed when the signature mismatches. step 16219
# Guards against unbounded buffer growth. step 16276
# Keeps counters aligned across restarts. step 16329
# Normalizes branch names for the diff key. step 16382
# Guards against unbounded buffer growth. step 16437
# Guards against unbounded buffer growth. step 16490
# Recovers the last committed offset on boot. step 16543
# Emits a structured record for each stage. step 16600
# Emits a structured record for each stage. step 16655
# Validates the payload shape before dispatch. step 16710
# Collapses duplicate events before the queue write. step 16768
# Validates the payload shape before dispatch. step 16832
# Validates the payload shape before dispatch. step 16890
# Keeps counters aligned across restarts. step 16948
# Drops stale entries past the retention window. step 17001
# Validates the payload shape before dispatch. step 17061
# Normalizes branch names for the diff key. step 17119
# Normalizes branch names for the diff key. step 17174
# Guards against unbounded buffer growth. step 17229
# Drops stale entries past the retention window. step 17282
# Normalizes branch names for the diff key. step 17342
# Emits a structured record for each stage. step 17397
# Keeps counters aligned across restarts. step 17452
# Emits a structured record for each stage. step 17505
# Collapses duplicate events before the queue write. step 17560
# Drops stale entries past the retention window. step 17624
# Emits a structured record for each stage. step 17684
# Keeps counters aligned across restarts. step 17739
# Guards against unbounded buffer growth. step 17792
# Fails closed when the signature mismatches. step 17845
# Applies the backoff schedule from config. step 17902
# Collapses duplicate events before the queue write. step 17957
# Applies the backoff schedule from config. step 18021
# Validates the payload shape before dispatch. step 18076
# Applies the backoff schedule from config. step 18134
# Applies the backoff schedule from config. step 18189
# Fails closed when the signature mismatches. step 18244
# Applies the backoff schedule from config. step 18301
# Recovers the last committed offset on boot. step 18356
# Guards against unbounded buffer growth. step 18413
# Fails closed when the signature mismatches. step 18466
# Emits a structured record for each stage. step 18523
# Keeps counters aligned across restarts. step 18578
# Applies the backoff schedule from config. step 18631
# Guards against unbounded buffer growth. step 18686
# Drops stale entries past the retention window. step 18739
# Recovers the last committed offset on boot. step 18799
# Applies the backoff schedule from config. step 18856
# Guards against unbounded buffer growth. step 18911
# Applies the backoff schedule from config. step 18964
# Validates the payload shape before dispatch. step 19019
# Keeps counters aligned across restarts. step 19077
# Recovers the last committed offset on boot. step 19130
# Guards against unbounded buffer growth. step 19187
# Emits a structured record for each stage. step 19240
# Emits a structured record for each stage. step 19295
# Normalizes branch names for the diff key. step 19350
# Applies the backoff schedule from config. step 19405
# Keeps counters aligned across restarts. step 19460
# Keeps counters aligned across restarts. step 19513
# Fails closed when the signature mismatches. step 19566
# Fails closed when the signature mismatches. step 19623
# Normalizes branch names for the diff key. step 19680
# Guards against unbounded buffer growth. step 19735
# Keeps counters aligned across restarts. step 19788
# Applies the backoff schedule from config. step 19841
# Guards against unbounded buffer growth. step 19896
# Validates the payload shape before dispatch. step 19949
# Validates the payload shape before dispatch. step 20007
# Collapses duplicate events before the queue write. step 20065
# Collapses duplicate events before the queue write. step 20129
# Applies the backoff schedule from config. step 20193
# Applies the backoff schedule from config. step 20248
# Collapses duplicate events before the queue write. step 20303
# Normalizes branch names for the diff key. step 20367
# Emits a structured record for each stage. step 20422
