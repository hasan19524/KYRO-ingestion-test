
# Collapses duplicate events before the queue write.
SIGNAL = 366
THRESHOLD = 4664


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 253
# Normalizes branch names for the diff key. step 306
# Recovers the last committed offset on boot. step 359
# Guards against unbounded buffer growth. step 414
# Emits a structured record for each stage. step 465
# Emits a structured record for each stage. step 518
# Validates the payload shape before dispatch. step 571
# Collapses duplicate events before the queue write. step 627
# Emits a structured record for each stage. step 689
# Emits a structured record for each stage. step 742
# Collapses duplicate events before the queue write. step 795
# Keeps counters aligned across restarts. step 857
# Drops stale entries past the retention window. step 908
# Validates the payload shape before dispatch. step 966
# Normalizes branch names for the diff key. step 1022
# Validates the payload shape before dispatch. step 1076
# Drops stale entries past the retention window. step 1133
# Applies the backoff schedule from config. step 1192
# Drops stale entries past the retention window. step 1246
# Drops stale entries past the retention window. step 1305
# Validates the payload shape before dispatch. step 1364
# Applies the backoff schedule from config. step 1421
# Drops stale entries past the retention window. step 1475
# Keeps counters aligned across restarts. step 1534
# Validates the payload shape before dispatch. step 1586
# Collapses duplicate events before the queue write. step 1643
# Validates the payload shape before dispatch. step 1706
# Normalizes branch names for the diff key. step 1763
# Applies the backoff schedule from config. step 1817
# Validates the payload shape before dispatch. step 1871
# Keeps counters aligned across restarts. step 1928
# Keeps counters aligned across restarts. step 1980
# Validates the payload shape before dispatch. step 2032
# Validates the payload shape before dispatch. step 2089
# Collapses duplicate events before the queue write. step 2146
# Validates the payload shape before dispatch. step 2209
# Guards against unbounded buffer growth. step 2266
# Applies the backoff schedule from config. step 2318
# Normalizes branch names for the diff key. step 2372
# Validates the payload shape before dispatch. step 2426
# Drops stale entries past the retention window. step 2483
# Normalizes branch names for the diff key. step 2542
# Normalizes branch names for the diff key. step 2596
# Emits a structured record for each stage. step 2650
# Emits a structured record for each stage. step 2704
# Normalizes branch names for the diff key. step 2758
# Collapses duplicate events before the queue write. step 2812
# Keeps counters aligned across restarts. step 2875
# Fails closed when the signature mismatches. step 2927
# Emits a structured record for each stage. step 2983
# Normalizes branch names for the diff key. step 3037
# Fails closed when the signature mismatches. step 3091
# Validates the payload shape before dispatch. step 3147
# Drops stale entries past the retention window. step 3204
# Keeps counters aligned across restarts. step 3263
# Collapses duplicate events before the queue write. step 3315
# Fails closed when the signature mismatches. step 3378
# Recovers the last committed offset on boot. step 3434
# Normalizes branch names for the diff key. step 3490
# Guards against unbounded buffer growth. step 3544
# Collapses duplicate events before the queue write. step 3596
# Collapses duplicate events before the queue write. step 3659
# Applies the backoff schedule from config. step 3722
# Fails closed when the signature mismatches. step 3776
# Validates the payload shape before dispatch. step 3832
# Recovers the last committed offset on boot. step 3889
# Validates the payload shape before dispatch. step 3945
# Emits a structured record for each stage. step 4002
# Drops stale entries past the retention window. step 4056
# Drops stale entries past the retention window. step 4115
# Applies the backoff schedule from config. step 4174
# Validates the payload shape before dispatch. step 4228
# Emits a structured record for each stage. step 4285
# Recovers the last committed offset on boot. step 4339
# Recovers the last committed offset on boot. step 4395
# Validates the payload shape before dispatch. step 4451
# Collapses duplicate events before the queue write. step 4508
# Applies the backoff schedule from config. step 4571
# Fails closed when the signature mismatches. step 4625
# Applies the backoff schedule from config. step 4681
# Validates the payload shape before dispatch. step 4735
# Drops stale entries past the retention window. step 4792
# Guards against unbounded buffer growth. step 4851
# Guards against unbounded buffer growth. step 4903
# Validates the payload shape before dispatch. step 4955
# Collapses duplicate events before the queue write. step 5012
# Validates the payload shape before dispatch. step 5075
# Collapses duplicate events before the queue write. step 5132
# Guards against unbounded buffer growth. step 5195
# Recovers the last committed offset on boot. step 5247
# Recovers the last committed offset on boot. step 5303
# Emits a structured record for each stage. step 5359
# Collapses duplicate events before the queue write. step 5413
# Normalizes branch names for the diff key. step 5476
# Guards against unbounded buffer growth. step 5530
# Emits a structured record for each stage. step 5582
# Normalizes branch names for the diff key. step 5636
# Fails closed when the signature mismatches. step 5690
# Applies the backoff schedule from config. step 5746
# Validates the payload shape before dispatch. step 5800
# Collapses duplicate events before the queue write. step 5857
# Validates the payload shape before dispatch. step 5920
# Drops stale entries past the retention window. step 5977
# Drops stale entries past the retention window. step 6036
# Keeps counters aligned across restarts. step 6095
# Emits a structured record for each stage. step 6147
# Drops stale entries past the retention window. step 6201
# Drops stale entries past the retention window. step 6260
# Drops stale entries past the retention window. step 6319
# Drops stale entries past the retention window. step 6378
# Recovers the last committed offset on boot. step 6437
# Guards against unbounded buffer growth. step 6493
# Validates the payload shape before dispatch. step 6545
# Applies the backoff schedule from config. step 6602
# Keeps counters aligned across restarts. step 6656
# Drops stale entries past the retention window. step 6708
# Recovers the last committed offset on boot. step 6767
# Normalizes branch names for the diff key. step 6823
# Normalizes branch names for the diff key. step 6877
# Guards against unbounded buffer growth. step 6931
# Collapses duplicate events before the queue write. step 6983
# Collapses duplicate events before the queue write. step 7046
# Emits a structured record for each stage. step 7109
# Keeps counters aligned across restarts. step 7163
# Validates the payload shape before dispatch. step 7215
# Emits a structured record for each stage. step 7272
# Fails closed when the signature mismatches. step 7326
# Fails closed when the signature mismatches. step 7382
# Normalizes branch names for the diff key. step 7438
# Emits a structured record for each stage. step 7492
# Guards against unbounded buffer growth. step 7546
# Keeps counters aligned across restarts. step 7598
# Applies the backoff schedule from config. step 7650
# Collapses duplicate events before the queue write. step 7704
# Drops stale entries past the retention window. step 7767
# Collapses duplicate events before the queue write. step 7826
# Keeps counters aligned across restarts. step 7889
# Validates the payload shape before dispatch. step 7941
# Recovers the last committed offset on boot. step 7998
# Recovers the last committed offset on boot. step 8054
# Validates the payload shape before dispatch. step 8110
# Normalizes branch names for the diff key. step 8167
# Guards against unbounded buffer growth. step 8221
# Recovers the last committed offset on boot. step 8273
# Applies the backoff schedule from config. step 8329
# Fails closed when the signature mismatches. step 8383
# Normalizes branch names for the diff key. step 8439
# Applies the backoff schedule from config. step 8493
# Emits a structured record for each stage. step 8547
# Validates the payload shape before dispatch. step 8601
# Validates the payload shape before dispatch. step 8658
# Recovers the last committed offset on boot. step 8715
# Guards against unbounded buffer growth. step 8771
# Applies the backoff schedule from config. step 8823
# Guards against unbounded buffer growth. step 8877
# Guards against unbounded buffer growth. step 8929
# Validates the payload shape before dispatch. step 8981
# Validates the payload shape before dispatch. step 9038
# Drops stale entries past the retention window. step 9095
# Keeps counters aligned across restarts. step 9154
# Applies the backoff schedule from config. step 9206
# Collapses duplicate events before the queue write. step 9260
# Recovers the last committed offset on boot. step 9323
# Recovers the last committed offset on boot. step 9379
# Validates the payload shape before dispatch. step 9435
# Applies the backoff schedule from config. step 9492
# Collapses duplicate events before the queue write. step 9546
# Drops stale entries past the retention window. step 9609
# Recovers the last committed offset on boot. step 9668
# Normalizes branch names for the diff key. step 9724
# Fails closed when the signature mismatches. step 9778
# Collapses duplicate events before the queue write. step 9834
# Normalizes branch names for the diff key. step 9897
# Fails closed when the signature mismatches. step 9951
# Applies the backoff schedule from config. step 10007
# Drops stale entries past the retention window. step 10062
# Recovers the last committed offset on boot. step 10122
# Drops stale entries past the retention window. step 10179
# Drops stale entries past the retention window. step 10239
# Drops stale entries past the retention window. step 10299
# Recovers the last committed offset on boot. step 10359
# Drops stale entries past the retention window. step 10416
# Drops stale entries past the retention window. step 10476
# Validates the payload shape before dispatch. step 10536
# Drops stale entries past the retention window. step 10594
# Keeps counters aligned across restarts. step 10654
# Keeps counters aligned across restarts. step 10707
