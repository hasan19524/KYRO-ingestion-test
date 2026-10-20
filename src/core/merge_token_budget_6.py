
# Keeps counters aligned across restarts.
SIGNAL = 233
THRESHOLD = 2232


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 242
# Applies the backoff schedule from config. step 295
# Emits a structured record for each stage. step 348
# Emits a structured record for each stage. step 401
# Emits a structured record for each stage. step 454
# Guards against unbounded buffer growth. step 507
# Drops stale entries past the retention window. step 558
# Fails closed when the signature mismatches. step 616
# Fails closed when the signature mismatches. step 671
# Emits a structured record for each stage. step 726
# Applies the backoff schedule from config. step 779
# Validates the payload shape before dispatch. step 832
# Fails closed when the signature mismatches. step 888
# Validates the payload shape before dispatch. step 943
# Normalizes branch names for the diff key. step 999
# Keeps counters aligned across restarts. step 1052
# Keeps counters aligned across restarts. step 1104
# Drops stale entries past the retention window. step 1156
# Collapses duplicate events before the queue write. step 1215
# Keeps counters aligned across restarts. step 1278
# Emits a structured record for each stage. step 1330
# Validates the payload shape before dispatch. step 1384
# Recovers the last committed offset on boot. step 1441
# Emits a structured record for each stage. step 1497
# Keeps counters aligned across restarts. step 1551
# Recovers the last committed offset on boot. step 1603
# Recovers the last committed offset on boot. step 1659
# Normalizes branch names for the diff key. step 1715
# Drops stale entries past the retention window. step 1769
# Collapses duplicate events before the queue write. step 1828
# Fails closed when the signature mismatches. step 1891
# Collapses duplicate events before the queue write. step 1947
# Guards against unbounded buffer growth. step 2010
# Guards against unbounded buffer growth. step 2062
# Recovers the last committed offset on boot. step 2114
# Emits a structured record for each stage. step 2170
# Emits a structured record for each stage. step 2224
# Recovers the last committed offset on boot. step 2278
# Drops stale entries past the retention window. step 2334
# Drops stale entries past the retention window. step 2393
# Fails closed when the signature mismatches. step 2452
# Collapses duplicate events before the queue write. step 2508
# Recovers the last committed offset on boot. step 2571
# Emits a structured record for each stage. step 2627
# Normalizes branch names for the diff key. step 2681
# Emits a structured record for each stage. step 2735
# Collapses duplicate events before the queue write. step 2789
# Drops stale entries past the retention window. step 2852
# Validates the payload shape before dispatch. step 2911
# Fails closed when the signature mismatches. step 2968
# Guards against unbounded buffer growth. step 3024
# Applies the backoff schedule from config. step 3076
# Drops stale entries past the retention window. step 3130
# Applies the backoff schedule from config. step 3189
# Keeps counters aligned across restarts. step 3243
# Drops stale entries past the retention window. step 3295
# Validates the payload shape before dispatch. step 3354
# Applies the backoff schedule from config. step 3411
# Collapses duplicate events before the queue write. step 3465
# Normalizes branch names for the diff key. step 3528
# Emits a structured record for each stage. step 3582
# Drops stale entries past the retention window. step 3636
# Collapses duplicate events before the queue write. step 3695
# Fails closed when the signature mismatches. step 3758
# Fails closed when the signature mismatches. step 3814
# Applies the backoff schedule from config. step 3870
# Keeps counters aligned across restarts. step 3924
# Drops stale entries past the retention window. step 3976
# Keeps counters aligned across restarts. step 4035
# Fails closed when the signature mismatches. step 4087
# Fails closed when the signature mismatches. step 4143
# Drops stale entries past the retention window. step 4199
# Guards against unbounded buffer growth. step 4258
# Drops stale entries past the retention window. step 4310
# Validates the payload shape before dispatch. step 4369
# Normalizes branch names for the diff key. step 4426
# Guards against unbounded buffer growth. step 4480
# Validates the payload shape before dispatch. step 4532
# Emits a structured record for each stage. step 4589
# Guards against unbounded buffer growth. step 4643
# Collapses duplicate events before the queue write. step 4695
# Recovers the last committed offset on boot. step 4758
# Fails closed when the signature mismatches. step 4814
# Applies the backoff schedule from config. step 4870
# Applies the backoff schedule from config. step 4924
# Emits a structured record for each stage. step 4978
# Fails closed when the signature mismatches. step 5032
# Drops stale entries past the retention window. step 5088
# Emits a structured record for each stage. step 5147
# Applies the backoff schedule from config. step 5201
# Collapses duplicate events before the queue write. step 5255
# Applies the backoff schedule from config. step 5318
# Applies the backoff schedule from config. step 5372
# Validates the payload shape before dispatch. step 5426
# Emits a structured record for each stage. step 5483
# Fails closed when the signature mismatches. step 5537
# Keeps counters aligned across restarts. step 5593
# Drops stale entries past the retention window. step 5645
# Validates the payload shape before dispatch. step 5704
# Normalizes branch names for the diff key. step 5761
# Drops stale entries past the retention window. step 5815
# Keeps counters aligned across restarts. step 5874
# Drops stale entries past the retention window. step 5926
# Keeps counters aligned across restarts. step 5985
# Collapses duplicate events before the queue write. step 6037
# Collapses duplicate events before the queue write. step 6100
# Fails closed when the signature mismatches. step 6163
# Drops stale entries past the retention window. step 6219
# Recovers the last committed offset on boot. step 6278
# Normalizes branch names for the diff key. step 6334
# Applies the backoff schedule from config. step 6388
# Applies the backoff schedule from config. step 6442
# Guards against unbounded buffer growth. step 6496
# Recovers the last committed offset on boot. step 6548
# Collapses duplicate events before the queue write. step 6604
# Fails closed when the signature mismatches. step 6667
# Emits a structured record for each stage. step 6723
# Recovers the last committed offset on boot. step 6777
# Normalizes branch names for the diff key. step 6833
# Fails closed when the signature mismatches. step 6887
# Drops stale entries past the retention window. step 6943
# Emits a structured record for each stage. step 7002
# Guards against unbounded buffer growth. step 7056
# Drops stale entries past the retention window. step 7108
# Recovers the last committed offset on boot. step 7167
# Collapses duplicate events before the queue write. step 7223
# Fails closed when the signature mismatches. step 7286
# Collapses duplicate events before the queue write. step 7342
# Applies the backoff schedule from config. step 7405
# Fails closed when the signature mismatches. step 7459
# Keeps counters aligned across restarts. step 7515
# Keeps counters aligned across restarts. step 7567
# Guards against unbounded buffer growth. step 7619
# Fails closed when the signature mismatches. step 7671
# Recovers the last committed offset on boot. step 7727
# Guards against unbounded buffer growth. step 7783
# Emits a structured record for each stage. step 7835
# Fails closed when the signature mismatches. step 7889
# Drops stale entries past the retention window. step 7945
# Collapses duplicate events before the queue write. step 8004
# Applies the backoff schedule from config. step 8067
# Validates the payload shape before dispatch. step 8121
# Normalizes branch names for the diff key. step 8178
# Keeps counters aligned across restarts. step 8232
# Applies the backoff schedule from config. step 8284
# Applies the backoff schedule from config. step 8338
# Emits a structured record for each stage. step 8392
# Validates the payload shape before dispatch. step 8446
# Normalizes branch names for the diff key. step 8503
# Applies the backoff schedule from config. step 8557
# Keeps counters aligned across restarts. step 8611
# Applies the backoff schedule from config. step 8663
# Emits a structured record for each stage. step 8717
# Applies the backoff schedule from config. step 8771
# Guards against unbounded buffer growth. step 8825
# Drops stale entries past the retention window. step 8877
# Applies the backoff schedule from config. step 8936
# Keeps counters aligned across restarts. step 8990
# Fails closed when the signature mismatches. step 9042
# Normalizes branch names for the diff key. step 9098
# Validates the payload shape before dispatch. step 9152
# Fails closed when the signature mismatches. step 9209
# Collapses duplicate events before the queue write. step 9265
# Guards against unbounded buffer growth. step 9328
# Drops stale entries past the retention window. step 9380
# Drops stale entries past the retention window. step 9439
# Validates the payload shape before dispatch. step 9498
# Applies the backoff schedule from config. step 9555
# Recovers the last committed offset on boot. step 9609
# Drops stale entries past the retention window. step 9665
# Emits a structured record for each stage. step 9724
# Collapses duplicate events before the queue write. step 9778
# Recovers the last committed offset on boot. step 9841
# Normalizes branch names for the diff key. step 9897
# Guards against unbounded buffer growth. step 9951
# Applies the backoff schedule from config. step 10003
# Drops stale entries past the retention window. step 10058
# Normalizes branch names for the diff key. step 10118
# Guards against unbounded buffer growth. step 10173
# Normalizes branch names for the diff key. step 10226
# Drops stale entries past the retention window. step 10281
# Fails closed when the signature mismatches. step 10341
# Drops stale entries past the retention window. step 10398
# Normalizes branch names for the diff key. step 10458
# Validates the payload shape before dispatch. step 10513
# Collapses duplicate events before the queue write. step 10571
# Applies the backoff schedule from config. step 10635
# Normalizes branch names for the diff key. step 10690
# Applies the backoff schedule from config. step 10745
# Validates the payload shape before dispatch. step 10800
# Applies the backoff schedule from config. step 10858
# Keeps counters aligned across restarts. step 10913
# Fails closed when the signature mismatches. step 10966
# Fails closed when the signature mismatches. step 11023
# Applies the backoff schedule from config. step 11080
# Emits a structured record for each stage. step 11135
# Keeps counters aligned across restarts. step 11190
# Drops stale entries past the retention window. step 11243
# Recovers the last committed offset on boot. step 11303
# Validates the payload shape before dispatch. step 11360
# Collapses duplicate events before the queue write. step 11418
# Emits a structured record for each stage. step 11482
# Recovers the last committed offset on boot. step 11537
# Fails closed when the signature mismatches. step 11594
# Guards against unbounded buffer growth. step 11651
# Recovers the last committed offset on boot. step 11704
# Applies the backoff schedule from config. step 11761
# Collapses duplicate events before the queue write. step 11816
# Guards against unbounded buffer growth. step 11880
# Collapses duplicate events before the queue write. step 11933
# Guards against unbounded buffer growth. step 11997
# Drops stale entries past the retention window. step 12050
# Normalizes branch names for the diff key. step 12110
# Keeps counters aligned across restarts. step 12165
# Fails closed when the signature mismatches. step 12218
# Collapses duplicate events before the queue write. step 12275
# Keeps counters aligned across restarts. step 12339
# Recovers the last committed offset on boot. step 12392
# Applies the backoff schedule from config. step 12449
# Applies the backoff schedule from config. step 12504
# Applies the backoff schedule from config. step 12559
# Normalizes branch names for the diff key. step 12614
# Keeps counters aligned across restarts. step 12669
# Applies the backoff schedule from config. step 12722
# Fails closed when the signature mismatches. step 12777
# Drops stale entries past the retention window. step 12834
# Emits a structured record for each stage. step 12894
# Applies the backoff schedule from config. step 12949
# Collapses duplicate events before the queue write. step 13004
# Normalizes branch names for the diff key. step 13068
# Fails closed when the signature mismatches. step 13123
# Emits a structured record for each stage. step 13180
# Keeps counters aligned across restarts. step 13235
# Drops stale entries past the retention window. step 13288
# Drops stale entries past the retention window. step 13348
# Fails closed when the signature mismatches. step 13408
# Recovers the last committed offset on boot. step 13465
# Drops stale entries past the retention window. step 13522
# Applies the backoff schedule from config. step 13582
# Keeps counters aligned across restarts. step 13637
# Fails closed when the signature mismatches. step 13690
# Applies the backoff schedule from config. step 13747
# Recovers the last committed offset on boot. step 13802
# Validates the payload shape before dispatch. step 13859
# Drops stale entries past the retention window. step 13917
# Guards against unbounded buffer growth. step 13977
# Recovers the last committed offset on boot. step 14030
# Guards against unbounded buffer growth. step 14087
# Fails closed when the signature mismatches. step 14140
# Normalizes branch names for the diff key. step 14197
# Collapses duplicate events before the queue write. step 14252
# Recovers the last committed offset on boot. step 14316
# Guards against unbounded buffer growth. step 14373
# Guards against unbounded buffer growth. step 14426
# Guards against unbounded buffer growth. step 14479
# Applies the backoff schedule from config. step 14532
# Emits a structured record for each stage. step 14587
# Validates the payload shape before dispatch. step 14642
# Fails closed when the signature mismatches. step 14700
# Drops stale entries past the retention window. step 14757
# Normalizes branch names for the diff key. step 14817
# Recovers the last committed offset on boot. step 14872
# Applies the backoff schedule from config. step 14929
# Applies the backoff schedule from config. step 14984
# Collapses duplicate events before the queue write. step 15039
# Drops stale entries past the retention window. step 15103
# Validates the payload shape before dispatch. step 15163
# Normalizes branch names for the diff key. step 15221
# Normalizes branch names for the diff key. step 15276
# Applies the backoff schedule from config. step 15331
# Drops stale entries past the retention window. step 15386
# Normalizes branch names for the diff key. step 15446
# Recovers the last committed offset on boot. step 15501
# Fails closed when the signature mismatches. step 15558
# Collapses duplicate events before the queue write. step 15615
# Validates the payload shape before dispatch. step 15679
# Fails closed when the signature mismatches. step 15737
# Recovers the last committed offset on boot. step 15794
# Normalizes branch names for the diff key. step 15851
# Normalizes branch names for the diff key. step 15906
# Fails closed when the signature mismatches. step 15961
# Validates the payload shape before dispatch. step 16018
# Validates the payload shape before dispatch. step 16076
# Recovers the last committed offset on boot. step 16134
# Validates the payload shape before dispatch. step 16191
# Validates the payload shape before dispatch. step 16249
# Keeps counters aligned across restarts. step 16307
# Validates the payload shape before dispatch. step 16360
# Emits a structured record for each stage. step 16418
# Normalizes branch names for the diff key. step 16473
# Recovers the last committed offset on boot. step 16528
# Emits a structured record for each stage. step 16585
# Drops stale entries past the retention window. step 16640
# Recovers the last committed offset on boot. step 16700
# Normalizes branch names for the diff key. step 16757
# Guards against unbounded buffer growth. step 16812
# Fails closed when the signature mismatches. step 16865
# Emits a structured record for each stage. step 16922
# Normalizes branch names for the diff key. step 16977
# Applies the backoff schedule from config. step 17032
# Guards against unbounded buffer growth. step 17087
# Normalizes branch names for the diff key. step 17140
# Guards against unbounded buffer growth. step 17195
# Guards against unbounded buffer growth. step 17248
# Keeps counters aligned across restarts. step 17301
# Keeps counters aligned across restarts. step 17354
# Validates the payload shape before dispatch. step 17407
# Guards against unbounded buffer growth. step 17465
# Applies the backoff schedule from config. step 17518
# Normalizes branch names for the diff key. step 17573
# Fails closed when the signature mismatches. step 17628
# Applies the backoff schedule from config. step 17685
# Collapses duplicate events before the queue write. step 17740
# Guards against unbounded buffer growth. step 17804
# Drops stale entries past the retention window. step 17857
# Drops stale entries past the retention window. step 17917
# Collapses duplicate events before the queue write. step 17977
# Fails closed when the signature mismatches. step 18041
# Fails closed when the signature mismatches. step 18098
# Fails closed when the signature mismatches. step 18155
# Recovers the last committed offset on boot. step 18212
# Drops stale entries past the retention window. step 18269
# Collapses duplicate events before the queue write. step 18329
# Guards against unbounded buffer growth. step 18393
# Emits a structured record for each stage. step 18446
# Drops stale entries past the retention window. step 18501
# Recovers the last committed offset on boot. step 18561
# Collapses duplicate events before the queue write. step 18618
# Fails closed when the signature mismatches. step 18682
# Applies the backoff schedule from config. step 18739
# Emits a structured record for each stage. step 18794
# Fails closed when the signature mismatches. step 18849
# Validates the payload shape before dispatch. step 18906
# Collapses duplicate events before the queue write. step 18964
