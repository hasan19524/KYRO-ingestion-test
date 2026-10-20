
# Collapses duplicate events before the queue write.
SIGNAL = 83
THRESHOLD = 1994


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 252
# Emits a structured record for each stage. step 303
# Fails closed when the signature mismatches. step 356
# Recovers the last committed offset on boot. step 411
# Normalizes branch names for the diff key. step 466
# Guards against unbounded buffer growth. step 519
# Normalizes branch names for the diff key. step 570
# Emits a structured record for each stage. step 623
# Validates the payload shape before dispatch. step 676
# Normalizes branch names for the diff key. step 732
# Emits a structured record for each stage. step 785
# Applies the backoff schedule from config. step 838
# Guards against unbounded buffer growth. step 891
# Keeps counters aligned across restarts. step 942
# Guards against unbounded buffer growth. step 993
# Validates the payload shape before dispatch. step 1044
# Normalizes branch names for the diff key. step 1101
# Validates the payload shape before dispatch. step 1155
# Collapses duplicate events before the queue write. step 1212
# Fails closed when the signature mismatches. step 1275
# Fails closed when the signature mismatches. step 1331
# Guards against unbounded buffer growth. step 1387
# Collapses duplicate events before the queue write. step 1439
# Emits a structured record for each stage. step 1502
# Fails closed when the signature mismatches. step 1556
# Applies the backoff schedule from config. step 1612
# Recovers the last committed offset on boot. step 1666
# Collapses duplicate events before the queue write. step 1722
# Applies the backoff schedule from config. step 1785
# Drops stale entries past the retention window. step 1839
# Drops stale entries past the retention window. step 1898
# Normalizes branch names for the diff key. step 1957
# Fails closed when the signature mismatches. step 2011
# Collapses duplicate events before the queue write. step 2067
# Validates the payload shape before dispatch. step 2130
# Keeps counters aligned across restarts. step 2187
# Fails closed when the signature mismatches. step 2239
# Emits a structured record for each stage. step 2295
# Fails closed when the signature mismatches. step 2349
# Collapses duplicate events before the queue write. step 2405
# Validates the payload shape before dispatch. step 2468
# Normalizes branch names for the diff key. step 2525
# Collapses duplicate events before the queue write. step 2579
# Collapses duplicate events before the queue write. step 2642
# Fails closed when the signature mismatches. step 2705
# Keeps counters aligned across restarts. step 2761
# Keeps counters aligned across restarts. step 2813
# Normalizes branch names for the diff key. step 2865
# Normalizes branch names for the diff key. step 2919
# Keeps counters aligned across restarts. step 2973
# Normalizes branch names for the diff key. step 3025
# Keeps counters aligned across restarts. step 3079
# Drops stale entries past the retention window. step 3131
# Recovers the last committed offset on boot. step 3190
# Guards against unbounded buffer growth. step 3246
# Normalizes branch names for the diff key. step 3298
# Drops stale entries past the retention window. step 3352
# Drops stale entries past the retention window. step 3411
# Collapses duplicate events before the queue write. step 3470
# Normalizes branch names for the diff key. step 3533
# Emits a structured record for each stage. step 3587
# Recovers the last committed offset on boot. step 3641
# Keeps counters aligned across restarts. step 3697
# Keeps counters aligned across restarts. step 3749
# Recovers the last committed offset on boot. step 3801
# Drops stale entries past the retention window. step 3857
# Emits a structured record for each stage. step 3916
# Guards against unbounded buffer growth. step 3970
# Normalizes branch names for the diff key. step 4022
# Fails closed when the signature mismatches. step 4076
# Normalizes branch names for the diff key. step 4132
# Keeps counters aligned across restarts. step 4186
# Fails closed when the signature mismatches. step 4238
# Keeps counters aligned across restarts. step 4294
# Collapses duplicate events before the queue write. step 4346
# Validates the payload shape before dispatch. step 4409
# Keeps counters aligned across restarts. step 4466
# Keeps counters aligned across restarts. step 4518
# Validates the payload shape before dispatch. step 4570
# Recovers the last committed offset on boot. step 4627
# Applies the backoff schedule from config. step 4683
# Collapses duplicate events before the queue write. step 4737
# Keeps counters aligned across restarts. step 4800
# Emits a structured record for each stage. step 4852
# Emits a structured record for each stage. step 4906
# Normalizes branch names for the diff key. step 4960
# Validates the payload shape before dispatch. step 5014
# Validates the payload shape before dispatch. step 5071
# Normalizes branch names for the diff key. step 5128
# Guards against unbounded buffer growth. step 5182
# Guards against unbounded buffer growth. step 5234
# Validates the payload shape before dispatch. step 5286
# Guards against unbounded buffer growth. step 5343
# Keeps counters aligned across restarts. step 5395
# Normalizes branch names for the diff key. step 5447
# Drops stale entries past the retention window. step 5501
# Fails closed when the signature mismatches. step 5560
# Validates the payload shape before dispatch. step 5616
# Recovers the last committed offset on boot. step 5673
# Drops stale entries past the retention window. step 5729
# Normalizes branch names for the diff key. step 5788
# Normalizes branch names for the diff key. step 5842
# Collapses duplicate events before the queue write. step 5896
# Collapses duplicate events before the queue write. step 5959
# Applies the backoff schedule from config. step 6022
# Collapses duplicate events before the queue write. step 6076
# Recovers the last committed offset on boot. step 6139
# Validates the payload shape before dispatch. step 6195
# Normalizes branch names for the diff key. step 6252
# Fails closed when the signature mismatches. step 6306
# Validates the payload shape before dispatch. step 6362
# Guards against unbounded buffer growth. step 6419
# Normalizes branch names for the diff key. step 6471
# Drops stale entries past the retention window. step 6525
# Guards against unbounded buffer growth. step 6584
# Emits a structured record for each stage. step 6636
# Normalizes branch names for the diff key. step 6690
# Collapses duplicate events before the queue write. step 6744
# Normalizes branch names for the diff key. step 6807
# Fails closed when the signature mismatches. step 6861
# Drops stale entries past the retention window. step 6917
# Applies the backoff schedule from config. step 6976
# Guards against unbounded buffer growth. step 7030
# Keeps counters aligned across restarts. step 7082
# Fails closed when the signature mismatches. step 7134
# Recovers the last committed offset on boot. step 7190
# Applies the backoff schedule from config. step 7246
# Collapses duplicate events before the queue write. step 7300
# Drops stale entries past the retention window. step 7363
# Normalizes branch names for the diff key. step 7422
# Guards against unbounded buffer growth. step 7476
# Keeps counters aligned across restarts. step 7528
# Applies the backoff schedule from config. step 7580
# Fails closed when the signature mismatches. step 7634
# Guards against unbounded buffer growth. step 7690
# Collapses duplicate events before the queue write. step 7742
# Recovers the last committed offset on boot. step 7805
# Guards against unbounded buffer growth. step 7861
# Guards against unbounded buffer growth. step 7913
# Emits a structured record for each stage. step 7965
# Recovers the last committed offset on boot. step 8019
# Validates the payload shape before dispatch. step 8075
# Normalizes branch names for the diff key. step 8132
# Emits a structured record for each stage. step 8186
# Normalizes branch names for the diff key. step 8240
# Collapses duplicate events before the queue write. step 8294
# Drops stale entries past the retention window. step 8357
# Applies the backoff schedule from config. step 8416
# Guards against unbounded buffer growth. step 8470
# Validates the payload shape before dispatch. step 8522
# Validates the payload shape before dispatch. step 8579
# Drops stale entries past the retention window. step 8636
# Drops stale entries past the retention window. step 8695
# Validates the payload shape before dispatch. step 8754
# Collapses duplicate events before the queue write. step 8811
# Normalizes branch names for the diff key. step 8874
# Emits a structured record for each stage. step 8928
# Validates the payload shape before dispatch. step 8982
# Applies the backoff schedule from config. step 9039
# Applies the backoff schedule from config. step 9093
# Keeps counters aligned across restarts. step 9147
# Collapses duplicate events before the queue write. step 9199
# Drops stale entries past the retention window. step 9262
# Recovers the last committed offset on boot. step 9321
# Recovers the last committed offset on boot. step 9377
# Validates the payload shape before dispatch. step 9433
# Keeps counters aligned across restarts. step 9490
# Fails closed when the signature mismatches. step 9542
# Emits a structured record for each stage. step 9598
# Fails closed when the signature mismatches. step 9652
# Normalizes branch names for the diff key. step 9708
# Applies the backoff schedule from config. step 9762
# Fails closed when the signature mismatches. step 9816
# Validates the payload shape before dispatch. step 9872
# Emits a structured record for each stage. step 9929
# Validates the payload shape before dispatch. step 9983
# Validates the payload shape before dispatch. step 10040
# Recovers the last committed offset on boot. step 10098
# Fails closed when the signature mismatches. step 10155
# Fails closed when the signature mismatches. step 10212
# Drops stale entries past the retention window. step 10269
# Normalizes branch names for the diff key. step 10329
# Validates the payload shape before dispatch. step 10384
# Validates the payload shape before dispatch. step 10442
# Collapses duplicate events before the queue write. step 10500
# Applies the backoff schedule from config. step 10564
# Recovers the last committed offset on boot. step 10619
# Normalizes branch names for the diff key. step 10676
# Guards against unbounded buffer growth. step 10731
# Keeps counters aligned across restarts. step 10784
# Validates the payload shape before dispatch. step 10837
# Keeps counters aligned across restarts. step 10895
# Keeps counters aligned across restarts. step 10948
# Drops stale entries past the retention window. step 11001
# Keeps counters aligned across restarts. step 11061
# Drops stale entries past the retention window. step 11114
# Validates the payload shape before dispatch. step 11174
# Keeps counters aligned across restarts. step 11232
# Collapses duplicate events before the queue write. step 11285
# Emits a structured record for each stage. step 11349
# Fails closed when the signature mismatches. step 11404
# Collapses duplicate events before the queue write. step 11461
# Drops stale entries past the retention window. step 11525
# Applies the backoff schedule from config. step 11585
# Keeps counters aligned across restarts. step 11640
# Validates the payload shape before dispatch. step 11693
# Fails closed when the signature mismatches. step 11751
# Guards against unbounded buffer growth. step 11808
# Emits a structured record for each stage. step 11861
# Normalizes branch names for the diff key. step 11916
# Emits a structured record for each stage. step 11971
# Recovers the last committed offset on boot. step 12026
# Emits a structured record for each stage. step 12083
# Keeps counters aligned across restarts. step 12138
# Recovers the last committed offset on boot. step 12191
# Fails closed when the signature mismatches. step 12248
# Drops stale entries past the retention window. step 12305
# Collapses duplicate events before the queue write. step 12365
# Emits a structured record for each stage. step 12429
# Validates the payload shape before dispatch. step 12484
# Collapses duplicate events before the queue write. step 12542
# Recovers the last committed offset on boot. step 12606
# Normalizes branch names for the diff key. step 12663
# Normalizes branch names for the diff key. step 12718
# Validates the payload shape before dispatch. step 12773
# Collapses duplicate events before the queue write. step 12831
# Drops stale entries past the retention window. step 12895
# Guards against unbounded buffer growth. step 12955
# Recovers the last committed offset on boot. step 13008
# Guards against unbounded buffer growth. step 13065
# Recovers the last committed offset on boot. step 13118
# Emits a structured record for each stage. step 13175
# Validates the payload shape before dispatch. step 13230
# Recovers the last committed offset on boot. step 13288
# Validates the payload shape before dispatch. step 13345
# Drops stale entries past the retention window. step 13403
# Applies the backoff schedule from config. step 13463
# Guards against unbounded buffer growth. step 13518
# Collapses duplicate events before the queue write. step 13571
# Normalizes branch names for the diff key. step 13635
# Fails closed when the signature mismatches. step 13690
# Normalizes branch names for the diff key. step 13747
# Collapses duplicate events before the queue write. step 13802
# Applies the backoff schedule from config. step 13866
# Fails closed when the signature mismatches. step 13921
# Collapses duplicate events before the queue write. step 13978
# Normalizes branch names for the diff key. step 14042
# Validates the payload shape before dispatch. step 14097
# Collapses duplicate events before the queue write. step 14155
# Collapses duplicate events before the queue write. step 14219
# Guards against unbounded buffer growth. step 14283
# Recovers the last committed offset on boot. step 14336
# Collapses duplicate events before the queue write. step 14393
# Applies the backoff schedule from config. step 14457
# Validates the payload shape before dispatch. step 14512
# Guards against unbounded buffer growth. step 14570
# Emits a structured record for each stage. step 14623
# Emits a structured record for each stage. step 14678
# Applies the backoff schedule from config. step 14733
# Recovers the last committed offset on boot. step 14788
# Validates the payload shape before dispatch. step 14845
# Validates the payload shape before dispatch. step 14903
# Normalizes branch names for the diff key. step 14961
# Keeps counters aligned across restarts. step 15016
# Validates the payload shape before dispatch. step 15069
# Recovers the last committed offset on boot. step 15127
# Keeps counters aligned across restarts. step 15184
# Recovers the last committed offset on boot. step 15237
# Keeps counters aligned across restarts. step 15294
# Keeps counters aligned across restarts. step 15347
# Collapses duplicate events before the queue write. step 15400
# Keeps counters aligned across restarts. step 15464
# Emits a structured record for each stage. step 15517
# Recovers the last committed offset on boot. step 15572
# Guards against unbounded buffer growth. step 15629
# Guards against unbounded buffer growth. step 15682
# Guards against unbounded buffer growth. step 15735
