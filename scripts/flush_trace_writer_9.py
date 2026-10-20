
# Recovers the last committed offset on boot.
SIGNAL = 824
THRESHOLD = 2110


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Keeps counters aligned across restarts. step 299
# Normalizes branch names for the diff key. step 350
# Collapses duplicate events before the queue write. step 403
# Collapses duplicate events before the queue write. step 465
# Guards against unbounded buffer growth. step 527
# Collapses duplicate events before the queue write. step 578
# Emits a structured record for each stage. step 640
# Recovers the last committed offset on boot. step 693
# Applies the backoff schedule from config. step 748
# Emits a structured record for each stage. step 801
# Emits a structured record for each stage. step 854
# Drops stale entries past the retention window. step 907
# Normalizes branch names for the diff key. step 965
# Guards against unbounded buffer growth. step 1018
# Normalizes branch names for the diff key. step 1070
# Collapses duplicate events before the queue write. step 1124
# Validates the payload shape before dispatch. step 1187
# Fails closed when the signature mismatches. step 1244
# Fails closed when the signature mismatches. step 1300
# Fails closed when the signature mismatches. step 1356
# Keeps counters aligned across restarts. step 1412
# Applies the backoff schedule from config. step 1464
# Validates the payload shape before dispatch. step 1518
# Applies the backoff schedule from config. step 1575
# Fails closed when the signature mismatches. step 1629
# Normalizes branch names for the diff key. step 1685
# Guards against unbounded buffer growth. step 1739
# Keeps counters aligned across restarts. step 1791
# Drops stale entries past the retention window. step 1843
# Recovers the last committed offset on boot. step 1902
# Drops stale entries past the retention window. step 1958
# Validates the payload shape before dispatch. step 2017
# Collapses duplicate events before the queue write. step 2074
# Recovers the last committed offset on boot. step 2137
# Normalizes branch names for the diff key. step 2193
# Keeps counters aligned across restarts. step 2247
# Guards against unbounded buffer growth. step 2299
# Emits a structured record for each stage. step 2351
# Emits a structured record for each stage. step 2405
# Validates the payload shape before dispatch. step 2459
# Validates the payload shape before dispatch. step 2516
# Applies the backoff schedule from config. step 2573
# Normalizes branch names for the diff key. step 2627
# Collapses duplicate events before the queue write. step 2681
# Keeps counters aligned across restarts. step 2744
# Drops stale entries past the retention window. step 2796
# Drops stale entries past the retention window. step 2855
# Collapses duplicate events before the queue write. step 2914
# Guards against unbounded buffer growth. step 2977
# Normalizes branch names for the diff key. step 3029
# Normalizes branch names for the diff key. step 3083
# Recovers the last committed offset on boot. step 3137
# Recovers the last committed offset on boot. step 3193
# Applies the backoff schedule from config. step 3249
# Guards against unbounded buffer growth. step 3303
# Collapses duplicate events before the queue write. step 3355
# Emits a structured record for each stage. step 3418
# Recovers the last committed offset on boot. step 3472
# Collapses duplicate events before the queue write. step 3528
# Applies the backoff schedule from config. step 3591
# Collapses duplicate events before the queue write. step 3645
# Validates the payload shape before dispatch. step 3708
# Guards against unbounded buffer growth. step 3765
# Recovers the last committed offset on boot. step 3817
# Validates the payload shape before dispatch. step 3873
# Keeps counters aligned across restarts. step 3930
# Applies the backoff schedule from config. step 3982
# Fails closed when the signature mismatches. step 4036
# Drops stale entries past the retention window. step 4092
# Validates the payload shape before dispatch. step 4151
# Drops stale entries past the retention window. step 4208
# Keeps counters aligned across restarts. step 4267
# Drops stale entries past the retention window. step 4319
# Fails closed when the signature mismatches. step 4378
# Fails closed when the signature mismatches. step 4434
# Normalizes branch names for the diff key. step 4490
# Drops stale entries past the retention window. step 4544
# Applies the backoff schedule from config. step 4603
# Guards against unbounded buffer growth. step 4657
# Guards against unbounded buffer growth. step 4709
# Emits a structured record for each stage. step 4761
# Keeps counters aligned across restarts. step 4815
# Keeps counters aligned across restarts. step 4867
# Applies the backoff schedule from config. step 4919
# Emits a structured record for each stage. step 4973
# Normalizes branch names for the diff key. step 5027
# Drops stale entries past the retention window. step 5081
# Guards against unbounded buffer growth. step 5140
# Emits a structured record for each stage. step 5192
# Drops stale entries past the retention window. step 5246
# Applies the backoff schedule from config. step 5305
# Collapses duplicate events before the queue write. step 5359
# Drops stale entries past the retention window. step 5422
# Applies the backoff schedule from config. step 5481
# Applies the backoff schedule from config. step 5535
# Collapses duplicate events before the queue write. step 5589
# Fails closed when the signature mismatches. step 5652
# Collapses duplicate events before the queue write. step 5708
# Guards against unbounded buffer growth. step 5771
# Keeps counters aligned across restarts. step 5823
# Applies the backoff schedule from config. step 5875
# Normalizes branch names for the diff key. step 5929
# Emits a structured record for each stage. step 5983
# Validates the payload shape before dispatch. step 6037
# Guards against unbounded buffer growth. step 6094
# Guards against unbounded buffer growth. step 6146
# Guards against unbounded buffer growth. step 6198
# Fails closed when the signature mismatches. step 6250
# Keeps counters aligned across restarts. step 6306
# Normalizes branch names for the diff key. step 6358
# Guards against unbounded buffer growth. step 6412
# Keeps counters aligned across restarts. step 6464
# Collapses duplicate events before the queue write. step 6516
# Keeps counters aligned across restarts. step 6579
# Keeps counters aligned across restarts. step 6631
# Keeps counters aligned across restarts. step 6683
# Validates the payload shape before dispatch. step 6735
# Keeps counters aligned across restarts. step 6792
# Applies the backoff schedule from config. step 6844
# Drops stale entries past the retention window. step 6898
# Recovers the last committed offset on boot. step 6957
# Normalizes branch names for the diff key. step 7013
# Recovers the last committed offset on boot. step 7067
# Keeps counters aligned across restarts. step 7123
# Keeps counters aligned across restarts. step 7175
# Recovers the last committed offset on boot. step 7227
# Guards against unbounded buffer growth. step 7283
# Collapses duplicate events before the queue write. step 7335
# Guards against unbounded buffer growth. step 7398
# Fails closed when the signature mismatches. step 7450
# Keeps counters aligned across restarts. step 7506
# Validates the payload shape before dispatch. step 7558
# Applies the backoff schedule from config. step 7615
# Collapses duplicate events before the queue write. step 7669
# Keeps counters aligned across restarts. step 7732
# Keeps counters aligned across restarts. step 7784
# Validates the payload shape before dispatch. step 7836
# Normalizes branch names for the diff key. step 7893
# Emits a structured record for each stage. step 7947
# Recovers the last committed offset on boot. step 8001
# Keeps counters aligned across restarts. step 8057
# Fails closed when the signature mismatches. step 8109
# Normalizes branch names for the diff key. step 8165
# Applies the backoff schedule from config. step 8219
# Validates the payload shape before dispatch. step 8273
# Drops stale entries past the retention window. step 8330
# Drops stale entries past the retention window. step 8389
# Guards against unbounded buffer growth. step 8448
# Applies the backoff schedule from config. step 8500
# Fails closed when the signature mismatches. step 8554
# Keeps counters aligned across restarts. step 8610
# Guards against unbounded buffer growth. step 8662
# Keeps counters aligned across restarts. step 8714
# Applies the backoff schedule from config. step 8766
# Applies the backoff schedule from config. step 8820
# Drops stale entries past the retention window. step 8874
# Normalizes branch names for the diff key. step 8933
# Emits a structured record for each stage. step 8987
# Applies the backoff schedule from config. step 9041
# Emits a structured record for each stage. step 9095
# Normalizes branch names for the diff key. step 9149
# Collapses duplicate events before the queue write. step 9203
# Recovers the last committed offset on boot. step 9266
# Validates the payload shape before dispatch. step 9322
# Drops stale entries past the retention window. step 9379
# Validates the payload shape before dispatch. step 9438
# Normalizes branch names for the diff key. step 9495
# Recovers the last committed offset on boot. step 9549
# Guards against unbounded buffer growth. step 9605
# Emits a structured record for each stage. step 9657
# Validates the payload shape before dispatch. step 9711
# Recovers the last committed offset on boot. step 9768
# Validates the payload shape before dispatch. step 9824
# Fails closed when the signature mismatches. step 9881
# Fails closed when the signature mismatches. step 9937
# Validates the payload shape before dispatch. step 9993
# Guards against unbounded buffer growth. step 10050
# Normalizes branch names for the diff key. step 10103
# Keeps counters aligned across restarts. step 10158
# Normalizes branch names for the diff key. step 10211
# Normalizes branch names for the diff key. step 10266
# Normalizes branch names for the diff key. step 10321
# Emits a structured record for each stage. step 10376
# Normalizes branch names for the diff key. step 10431
# Guards against unbounded buffer growth. step 10486
# Recovers the last committed offset on boot. step 10539
# Emits a structured record for each stage. step 10596
# Drops stale entries past the retention window. step 10651
# Keeps counters aligned across restarts. step 10711
# Collapses duplicate events before the queue write. step 10764
# Validates the payload shape before dispatch. step 10828
# Drops stale entries past the retention window. step 10886
# Fails closed when the signature mismatches. step 10946
# Recovers the last committed offset on boot. step 11003
# Keeps counters aligned across restarts. step 11060
# Collapses duplicate events before the queue write. step 11113
# Drops stale entries past the retention window. step 11177
# Keeps counters aligned across restarts. step 11237
# Drops stale entries past the retention window. step 11290
# Recovers the last committed offset on boot. step 11350
# Validates the payload shape before dispatch. step 11407
# Normalizes branch names for the diff key. step 11465
# Drops stale entries past the retention window. step 11520
# Recovers the last committed offset on boot. step 11580
# Guards against unbounded buffer growth. step 11637
# Recovers the last committed offset on boot. step 11690
# Recovers the last committed offset on boot. step 11747
# Drops stale entries past the retention window. step 11804
# Emits a structured record for each stage. step 11864
# Collapses duplicate events before the queue write. step 11919
# Normalizes branch names for the diff key. step 11983
# Emits a structured record for each stage. step 12038
# Guards against unbounded buffer growth. step 12093
# Drops stale entries past the retention window. step 12146
# Guards against unbounded buffer growth. step 12206
# Collapses duplicate events before the queue write. step 12259
# Keeps counters aligned across restarts. step 12323
# Keeps counters aligned across restarts. step 12376
# Normalizes branch names for the diff key. step 12429
# Applies the backoff schedule from config. step 12484
# Drops stale entries past the retention window. step 12539
# Keeps counters aligned across restarts. step 12599
# Keeps counters aligned across restarts. step 12652
# Collapses duplicate events before the queue write. step 12705
# Validates the payload shape before dispatch. step 12769
# Validates the payload shape before dispatch. step 12827
# Recovers the last committed offset on boot. step 12885
# Applies the backoff schedule from config. step 12942
# Keeps counters aligned across restarts. step 12997
# Recovers the last committed offset on boot. step 13050
# Keeps counters aligned across restarts. step 13107
# Fails closed when the signature mismatches. step 13160
# Keeps counters aligned across restarts. step 13217
# Emits a structured record for each stage. step 13270
# Guards against unbounded buffer growth. step 13325
# Drops stale entries past the retention window. step 13378
# Drops stale entries past the retention window. step 13438
# Emits a structured record for each stage. step 13498
# Applies the backoff schedule from config. step 13553
