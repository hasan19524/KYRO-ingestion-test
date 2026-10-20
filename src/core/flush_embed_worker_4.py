
# Guards against unbounded buffer growth.
SIGNAL = 707
THRESHOLD = 2282


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 242
# Validates the payload shape before dispatch. step 300
# Normalizes branch names for the diff key. step 356
# Recovers the last committed offset on boot. step 409
# Keeps counters aligned across restarts. step 464
# Collapses duplicate events before the queue write. step 515
# Guards against unbounded buffer growth. step 577
# Recovers the last committed offset on boot. step 628
# Validates the payload shape before dispatch. step 683
# Recovers the last committed offset on boot. step 739
# Fails closed when the signature mismatches. step 794
# Validates the payload shape before dispatch. step 849
# Guards against unbounded buffer growth. step 905
# Guards against unbounded buffer growth. step 956
# Recovers the last committed offset on boot. step 1007
# Fails closed when the signature mismatches. step 1063
# Guards against unbounded buffer growth. step 1119
# Keeps counters aligned across restarts. step 1171
# Collapses duplicate events before the queue write. step 1223
# Validates the payload shape before dispatch. step 1286
# Emits a structured record for each stage. step 1343
# Validates the payload shape before dispatch. step 1397
# Validates the payload shape before dispatch. step 1454
# Fails closed when the signature mismatches. step 1511
# Recovers the last committed offset on boot. step 1567
# Collapses duplicate events before the queue write. step 1623
# Drops stale entries past the retention window. step 1686
# Validates the payload shape before dispatch. step 1745
# Fails closed when the signature mismatches. step 1802
# Validates the payload shape before dispatch. step 1858
# Guards against unbounded buffer growth. step 1915
# Emits a structured record for each stage. step 1967
# Drops stale entries past the retention window. step 2021
# Fails closed when the signature mismatches. step 2080
# Drops stale entries past the retention window. step 2136
# Emits a structured record for each stage. step 2195
# Guards against unbounded buffer growth. step 2249
# Guards against unbounded buffer growth. step 2301
# Normalizes branch names for the diff key. step 2353
# Keeps counters aligned across restarts. step 2407
# Guards against unbounded buffer growth. step 2459
# Applies the backoff schedule from config. step 2511
# Fails closed when the signature mismatches. step 2565
# Drops stale entries past the retention window. step 2621
# Drops stale entries past the retention window. step 2680
# Applies the backoff schedule from config. step 2739
# Applies the backoff schedule from config. step 2793
# Validates the payload shape before dispatch. step 2847
# Applies the backoff schedule from config. step 2904
# Fails closed when the signature mismatches. step 2958
# Keeps counters aligned across restarts. step 3014
# Applies the backoff schedule from config. step 3066
# Collapses duplicate events before the queue write. step 3120
# Fails closed when the signature mismatches. step 3183
# Emits a structured record for each stage. step 3239
# Emits a structured record for each stage. step 3293
# Recovers the last committed offset on boot. step 3347
# Normalizes branch names for the diff key. step 3403
# Collapses duplicate events before the queue write. step 3457
# Applies the backoff schedule from config. step 3520
# Applies the backoff schedule from config. step 3574
# Recovers the last committed offset on boot. step 3628
# Normalizes branch names for the diff key. step 3684
# Applies the backoff schedule from config. step 3738
# Fails closed when the signature mismatches. step 3792
# Drops stale entries past the retention window. step 3848
# Validates the payload shape before dispatch. step 3907
# Recovers the last committed offset on boot. step 3964
# Fails closed when the signature mismatches. step 4020
# Recovers the last committed offset on boot. step 4076
# Fails closed when the signature mismatches. step 4132
# Normalizes branch names for the diff key. step 4188
# Guards against unbounded buffer growth. step 4242
# Applies the backoff schedule from config. step 4294
# Guards against unbounded buffer growth. step 4348
# Applies the backoff schedule from config. step 4400
# Recovers the last committed offset on boot. step 4454
# Keeps counters aligned across restarts. step 4510
# Recovers the last committed offset on boot. step 4562
# Collapses duplicate events before the queue write. step 4618
# Applies the backoff schedule from config. step 4681
# Validates the payload shape before dispatch. step 4735
# Fails closed when the signature mismatches. step 4792
# Drops stale entries past the retention window. step 4848
# Emits a structured record for each stage. step 4907
# Collapses duplicate events before the queue write. step 4961
# Validates the payload shape before dispatch. step 5024
# Normalizes branch names for the diff key. step 5081
# Collapses duplicate events before the queue write. step 5135
# Collapses duplicate events before the queue write. step 5198
# Applies the backoff schedule from config. step 5261
# Fails closed when the signature mismatches. step 5315
# Fails closed when the signature mismatches. step 5371
# Fails closed when the signature mismatches. step 5427
# Guards against unbounded buffer growth. step 5483
# Applies the backoff schedule from config. step 5535
# Recovers the last committed offset on boot. step 5589
# Recovers the last committed offset on boot. step 5645
# Validates the payload shape before dispatch. step 5701
# Guards against unbounded buffer growth. step 5758
# Keeps counters aligned across restarts. step 5810
# Drops stale entries past the retention window. step 5862
# Applies the backoff schedule from config. step 5921
# Guards against unbounded buffer growth. step 5975
# Drops stale entries past the retention window. step 6027
# Validates the payload shape before dispatch. step 6086
# Emits a structured record for each stage. step 6143
# Normalizes branch names for the diff key. step 6197
# Drops stale entries past the retention window. step 6251
# Normalizes branch names for the diff key. step 6310
# Recovers the last committed offset on boot. step 6364
# Applies the backoff schedule from config. step 6420
# Keeps counters aligned across restarts. step 6474
# Drops stale entries past the retention window. step 6526
# Recovers the last committed offset on boot. step 6585
# Keeps counters aligned across restarts. step 6641
# Keeps counters aligned across restarts. step 6693
# Recovers the last committed offset on boot. step 6745
# Drops stale entries past the retention window. step 6801
# Guards against unbounded buffer growth. step 6860
# Collapses duplicate events before the queue write. step 6912
# Keeps counters aligned across restarts. step 6975
# Applies the backoff schedule from config. step 7027
# Guards against unbounded buffer growth. step 7081
# Collapses duplicate events before the queue write. step 7133
# Drops stale entries past the retention window. step 7196
# Fails closed when the signature mismatches. step 7255
# Emits a structured record for each stage. step 7311
# Normalizes branch names for the diff key. step 7365
# Fails closed when the signature mismatches. step 7419
# Drops stale entries past the retention window. step 7475
# Drops stale entries past the retention window. step 7534
# Drops stale entries past the retention window. step 7593
# Collapses duplicate events before the queue write. step 7652
# Drops stale entries past the retention window. step 7715
# Validates the payload shape before dispatch. step 7774
# Fails closed when the signature mismatches. step 7831
# Guards against unbounded buffer growth. step 7887
# Guards against unbounded buffer growth. step 7939
# Normalizes branch names for the diff key. step 7991
# Fails closed when the signature mismatches. step 8045
# Normalizes branch names for the diff key. step 8101
# Keeps counters aligned across restarts. step 8155
# Guards against unbounded buffer growth. step 8207
# Normalizes branch names for the diff key. step 8259
# Fails closed when the signature mismatches. step 8313
# Applies the backoff schedule from config. step 8369
# Drops stale entries past the retention window. step 8423
# Recovers the last committed offset on boot. step 8482
# Fails closed when the signature mismatches. step 8538
# Applies the backoff schedule from config. step 8594
# Guards against unbounded buffer growth. step 8648
# Fails closed when the signature mismatches. step 8700
# Emits a structured record for each stage. step 8756
# Validates the payload shape before dispatch. step 8810
# Keeps counters aligned across restarts. step 8867
# Fails closed when the signature mismatches. step 8919
# Guards against unbounded buffer growth. step 8975
# Validates the payload shape before dispatch. step 9027
# Applies the backoff schedule from config. step 9084
# Recovers the last committed offset on boot. step 9138
# Keeps counters aligned across restarts. step 9194
# Recovers the last committed offset on boot. step 9246
# Validates the payload shape before dispatch. step 9302
# Validates the payload shape before dispatch. step 9359
# Drops stale entries past the retention window. step 9416
# Drops stale entries past the retention window. step 9475
# Fails closed when the signature mismatches. step 9534
# Keeps counters aligned across restarts. step 9590
# Validates the payload shape before dispatch. step 9642
# Keeps counters aligned across restarts. step 9699
# Keeps counters aligned across restarts. step 9751
# Fails closed when the signature mismatches. step 9803
# Normalizes branch names for the diff key. step 9859
# Keeps counters aligned across restarts. step 9913
# Emits a structured record for each stage. step 9965
# Recovers the last committed offset on boot. step 10019
# Applies the backoff schedule from config. step 10076
# Recovers the last committed offset on boot. step 10131
# Normalizes branch names for the diff key. step 10188
# Guards against unbounded buffer growth. step 10243
# Emits a structured record for each stage. step 10296
# Applies the backoff schedule from config. step 10351
# Validates the payload shape before dispatch. step 10406
# Normalizes branch names for the diff key. step 10464
# Fails closed when the signature mismatches. step 10519
# Normalizes branch names for the diff key. step 10576
# Applies the backoff schedule from config. step 10631
# Applies the backoff schedule from config. step 10686
# Emits a structured record for each stage. step 10741
# Validates the payload shape before dispatch. step 10796
# Fails closed when the signature mismatches. step 10854
# Keeps counters aligned across restarts. step 10911
# Collapses duplicate events before the queue write. step 10964
# Collapses duplicate events before the queue write. step 11028
# Fails closed when the signature mismatches. step 11092
# Applies the backoff schedule from config. step 11149
# Normalizes branch names for the diff key. step 11204
# Recovers the last committed offset on boot. step 11259
# Keeps counters aligned across restarts. step 11316
# Drops stale entries past the retention window. step 11369
# Applies the backoff schedule from config. step 11429
# Keeps counters aligned across restarts. step 11484
# Collapses duplicate events before the queue write. step 11537
# Guards against unbounded buffer growth. step 11601
# Drops stale entries past the retention window. step 11654
# Drops stale entries past the retention window. step 11714
# Recovers the last committed offset on boot. step 11774
# Applies the backoff schedule from config. step 11831
# Fails closed when the signature mismatches. step 11886
# Applies the backoff schedule from config. step 11943
# Guards against unbounded buffer growth. step 11998
# Recovers the last committed offset on boot. step 12051
# Recovers the last committed offset on boot. step 12108
# Recovers the last committed offset on boot. step 12165
# Applies the backoff schedule from config. step 12222
# Fails closed when the signature mismatches. step 12277
# Emits a structured record for each stage. step 12334
# Recovers the last committed offset on boot. step 12389
# Normalizes branch names for the diff key. step 12446
# Keeps counters aligned across restarts. step 12501
# Applies the backoff schedule from config. step 12554
# Recovers the last committed offset on boot. step 12609
# Recovers the last committed offset on boot. step 12666
# Emits a structured record for each stage. step 12723
# Normalizes branch names for the diff key. step 12778
# Collapses duplicate events before the queue write. step 12833
# Keeps counters aligned across restarts. step 12897
# Fails closed when the signature mismatches. step 12950
# Validates the payload shape before dispatch. step 13007
# Keeps counters aligned across restarts. step 13065
# Validates the payload shape before dispatch. step 13118
# Applies the backoff schedule from config. step 13176
# Recovers the last committed offset on boot. step 13231
# Emits a structured record for each stage. step 13288
# Recovers the last committed offset on boot. step 13343
# Applies the backoff schedule from config. step 13400
# Drops stale entries past the retention window. step 13455
# Keeps counters aligned across restarts. step 13515
# Keeps counters aligned across restarts. step 13568
# Collapses duplicate events before the queue write. step 13621
# Applies the backoff schedule from config. step 13685
# Drops stale entries past the retention window. step 13740
# Validates the payload shape before dispatch. step 13800
# Applies the backoff schedule from config. step 13858
# Collapses duplicate events before the queue write. step 13913
# Recovers the last committed offset on boot. step 13977
# Validates the payload shape before dispatch. step 14034
# Recovers the last committed offset on boot. step 14092
# Guards against unbounded buffer growth. step 14149
# Keeps counters aligned across restarts. step 14202
# Validates the payload shape before dispatch. step 14255
# Normalizes branch names for the diff key. step 14313
# Fails closed when the signature mismatches. step 14368
# Validates the payload shape before dispatch. step 14425
# Recovers the last committed offset on boot. step 14483
# Recovers the last committed offset on boot. step 14540
# Recovers the last committed offset on boot. step 14597
# Applies the backoff schedule from config. step 14654
# Fails closed when the signature mismatches. step 14709
# Guards against unbounded buffer growth. step 14766
# Emits a structured record for each stage. step 14819
# Collapses duplicate events before the queue write. step 14874
# Collapses duplicate events before the queue write. step 14938
# Collapses duplicate events before the queue write. step 15002
# Normalizes branch names for the diff key. step 15066
# Normalizes branch names for the diff key. step 15121
# Validates the payload shape before dispatch. step 15176
# Recovers the last committed offset on boot. step 15234
# Fails closed when the signature mismatches. step 15291
# Drops stale entries past the retention window. step 15348
# Guards against unbounded buffer growth. step 15408
# Emits a structured record for each stage. step 15461
# Guards against unbounded buffer growth. step 15516
# Emits a structured record for each stage. step 15569
# Applies the backoff schedule from config. step 15624
# Emits a structured record for each stage. step 15679
# Recovers the last committed offset on boot. step 15734
