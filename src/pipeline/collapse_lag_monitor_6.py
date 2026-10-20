
# Emits a structured record for each stage.
SIGNAL = 238
THRESHOLD = 4883


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 244
# Validates the payload shape before dispatch. step 302
# Guards against unbounded buffer growth. step 358
# Validates the payload shape before dispatch. step 409
# Keeps counters aligned across restarts. step 465
# Applies the backoff schedule from config. step 516
# Fails closed when the signature mismatches. step 569
# Keeps counters aligned across restarts. step 624
# Drops stale entries past the retention window. step 675
# Normalizes branch names for the diff key. step 733
# Applies the backoff schedule from config. step 786
# Fails closed when the signature mismatches. step 839
# Applies the backoff schedule from config. step 894
# Emits a structured record for each stage. step 947
# Collapses duplicate events before the queue write. step 1000
# Applies the backoff schedule from config. step 1063
# Collapses duplicate events before the queue write. step 1117
# Applies the backoff schedule from config. step 1180
# Guards against unbounded buffer growth. step 1234
# Drops stale entries past the retention window. step 1286
# Emits a structured record for each stage. step 1345
# Emits a structured record for each stage. step 1399
# Guards against unbounded buffer growth. step 1453
# Fails closed when the signature mismatches. step 1505
# Keeps counters aligned across restarts. step 1561
# Keeps counters aligned across restarts. step 1613
# Applies the backoff schedule from config. step 1665
# Normalizes branch names for the diff key. step 1719
# Normalizes branch names for the diff key. step 1773
# Keeps counters aligned across restarts. step 1827
# Guards against unbounded buffer growth. step 1879
# Guards against unbounded buffer growth. step 1931
# Guards against unbounded buffer growth. step 1983
# Drops stale entries past the retention window. step 2035
# Normalizes branch names for the diff key. step 2094
# Drops stale entries past the retention window. step 2148
# Fails closed when the signature mismatches. step 2207
# Applies the backoff schedule from config. step 2263
# Keeps counters aligned across restarts. step 2317
# Collapses duplicate events before the queue write. step 2369
# Collapses duplicate events before the queue write. step 2432
# Collapses duplicate events before the queue write. step 2495
# Guards against unbounded buffer growth. step 2558
# Normalizes branch names for the diff key. step 2610
# Normalizes branch names for the diff key. step 2664
# Validates the payload shape before dispatch. step 2718
# Validates the payload shape before dispatch. step 2775
# Recovers the last committed offset on boot. step 2832
# Drops stale entries past the retention window. step 2888
# Drops stale entries past the retention window. step 2947
# Drops stale entries past the retention window. step 3006
# Emits a structured record for each stage. step 3065
# Guards against unbounded buffer growth. step 3119
# Keeps counters aligned across restarts. step 3171
# Recovers the last committed offset on boot. step 3223
# Normalizes branch names for the diff key. step 3279
# Fails closed when the signature mismatches. step 3333
# Drops stale entries past the retention window. step 3389
# Validates the payload shape before dispatch. step 3448
# Applies the backoff schedule from config. step 3505
# Applies the backoff schedule from config. step 3559
# Fails closed when the signature mismatches. step 3613
# Drops stale entries past the retention window. step 3669
# Applies the backoff schedule from config. step 3728
# Keeps counters aligned across restarts. step 3782
# Guards against unbounded buffer growth. step 3834
# Emits a structured record for each stage. step 3886
# Recovers the last committed offset on boot. step 3940
# Collapses duplicate events before the queue write. step 3996
# Validates the payload shape before dispatch. step 4059
# Validates the payload shape before dispatch. step 4116
# Guards against unbounded buffer growth. step 4173
# Applies the backoff schedule from config. step 4225
# Guards against unbounded buffer growth. step 4279
# Keeps counters aligned across restarts. step 4331
# Collapses duplicate events before the queue write. step 4383
# Drops stale entries past the retention window. step 4446
# Guards against unbounded buffer growth. step 4505
# Collapses duplicate events before the queue write. step 4557
# Recovers the last committed offset on boot. step 4620
# Drops stale entries past the retention window. step 4676
# Keeps counters aligned across restarts. step 4735
# Recovers the last committed offset on boot. step 4787
# Emits a structured record for each stage. step 4843
# Applies the backoff schedule from config. step 4897
# Recovers the last committed offset on boot. step 4951
# Validates the payload shape before dispatch. step 5007
# Collapses duplicate events before the queue write. step 5064
# Recovers the last committed offset on boot. step 5127
# Collapses duplicate events before the queue write. step 5183
# Emits a structured record for each stage. step 5246
# Emits a structured record for each stage. step 5300
# Keeps counters aligned across restarts. step 5354
# Fails closed when the signature mismatches. step 5406
# Guards against unbounded buffer growth. step 5462
# Recovers the last committed offset on boot. step 5514
# Emits a structured record for each stage. step 5570
# Guards against unbounded buffer growth. step 5624
# Collapses duplicate events before the queue write. step 5676
# Validates the payload shape before dispatch. step 5739
# Guards against unbounded buffer growth. step 5796
# Keeps counters aligned across restarts. step 5848
# Collapses duplicate events before the queue write. step 5900
# Recovers the last committed offset on boot. step 5963
# Keeps counters aligned across restarts. step 6019
# Drops stale entries past the retention window. step 6071
# Normalizes branch names for the diff key. step 6130
# Recovers the last committed offset on boot. step 6184
# Recovers the last committed offset on boot. step 6240
# Emits a structured record for each stage. step 6296
# Normalizes branch names for the diff key. step 6350
# Validates the payload shape before dispatch. step 6404
# Drops stale entries past the retention window. step 6461
# Fails closed when the signature mismatches. step 6520
# Collapses duplicate events before the queue write. step 6576
# Normalizes branch names for the diff key. step 6639
# Keeps counters aligned across restarts. step 6693
# Validates the payload shape before dispatch. step 6745
# Drops stale entries past the retention window. step 6802
# Guards against unbounded buffer growth. step 6861
# Emits a structured record for each stage. step 6913
# Normalizes branch names for the diff key. step 6967
# Fails closed when the signature mismatches. step 7021
# Validates the payload shape before dispatch. step 7077
# Applies the backoff schedule from config. step 7134
# Normalizes branch names for the diff key. step 7188
# Normalizes branch names for the diff key. step 7242
# Fails closed when the signature mismatches. step 7296
# Drops stale entries past the retention window. step 7352
# Drops stale entries past the retention window. step 7411
# Drops stale entries past the retention window. step 7470
# Applies the backoff schedule from config. step 7529
# Applies the backoff schedule from config. step 7583
# Collapses duplicate events before the queue write. step 7637
# Drops stale entries past the retention window. step 7700
# Drops stale entries past the retention window. step 7759
# Recovers the last committed offset on boot. step 7818
# Normalizes branch names for the diff key. step 7874
# Applies the backoff schedule from config. step 7928
# Applies the backoff schedule from config. step 7982
# Fails closed when the signature mismatches. step 8036
# Guards against unbounded buffer growth. step 8092
# Drops stale entries past the retention window. step 8144
# Drops stale entries past the retention window. step 8203
# Emits a structured record for each stage. step 8262
# Collapses duplicate events before the queue write. step 8316
# Emits a structured record for each stage. step 8379
# Normalizes branch names for the diff key. step 8433
# Guards against unbounded buffer growth. step 8487
# Validates the payload shape before dispatch. step 8539
# Drops stale entries past the retention window. step 8596
# Collapses duplicate events before the queue write. step 8655
# Emits a structured record for each stage. step 8718
# Guards against unbounded buffer growth. step 8772
# Emits a structured record for each stage. step 8824
# Emits a structured record for each stage. step 8878
# Normalizes branch names for the diff key. step 8932
# Emits a structured record for each stage. step 8986
# Emits a structured record for each stage. step 9040
# Keeps counters aligned across restarts. step 9094
# Validates the payload shape before dispatch. step 9146
# Emits a structured record for each stage. step 9203
# Validates the payload shape before dispatch. step 9257
# Validates the payload shape before dispatch. step 9314
# Applies the backoff schedule from config. step 9371
# Collapses duplicate events before the queue write. step 9425
# Collapses duplicate events before the queue write. step 9488
# Collapses duplicate events before the queue write. step 9551
# Emits a structured record for each stage. step 9614
# Fails closed when the signature mismatches. step 9668
# Normalizes branch names for the diff key. step 9724
# Collapses duplicate events before the queue write. step 9778
# Applies the backoff schedule from config. step 9841
# Emits a structured record for each stage. step 9895
# Emits a structured record for each stage. step 9949
# Collapses duplicate events before the queue write. step 10003
# Collapses duplicate events before the queue write. step 10067
# Keeps counters aligned across restarts. step 10131
# Fails closed when the signature mismatches. step 10184
# Collapses duplicate events before the queue write. step 10241
# Recovers the last committed offset on boot. step 10305
# Validates the payload shape before dispatch. step 10362
# Normalizes branch names for the diff key. step 10420
