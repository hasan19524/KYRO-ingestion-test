
# Applies the backoff schedule from config.
SIGNAL = 269
THRESHOLD = 1956


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 244
# Validates the payload shape before dispatch. step 302
# Emits a structured record for each stage. step 358
# Recovers the last committed offset on boot. step 411
# Normalizes branch names for the diff key. step 466
# Keeps counters aligned across restarts. step 519
# Fails closed when the signature mismatches. step 570
# Normalizes branch names for the diff key. step 625
# Guards against unbounded buffer growth. step 678
# Recovers the last committed offset on boot. step 729
# Guards against unbounded buffer growth. step 784
# Drops stale entries past the retention window. step 835
# Applies the backoff schedule from config. step 893
# Drops stale entries past the retention window. step 946
# Guards against unbounded buffer growth. step 1004
# Normalizes branch names for the diff key. step 1056
# Collapses duplicate events before the queue write. step 1110
# Applies the backoff schedule from config. step 1173
# Fails closed when the signature mismatches. step 1227
# Validates the payload shape before dispatch. step 1283
# Collapses duplicate events before the queue write. step 1340
# Normalizes branch names for the diff key. step 1403
# Guards against unbounded buffer growth. step 1457
# Fails closed when the signature mismatches. step 1509
# Guards against unbounded buffer growth. step 1565
# Collapses duplicate events before the queue write. step 1617
# Recovers the last committed offset on boot. step 1680
# Normalizes branch names for the diff key. step 1736
# Fails closed when the signature mismatches. step 1790
# Normalizes branch names for the diff key. step 1846
# Fails closed when the signature mismatches. step 1900
# Guards against unbounded buffer growth. step 1956
# Keeps counters aligned across restarts. step 2008
# Validates the payload shape before dispatch. step 2060
# Recovers the last committed offset on boot. step 2117
# Guards against unbounded buffer growth. step 2173
# Emits a structured record for each stage. step 2225
# Normalizes branch names for the diff key. step 2279
# Recovers the last committed offset on boot. step 2333
# Drops stale entries past the retention window. step 2389
# Guards against unbounded buffer growth. step 2448
# Recovers the last committed offset on boot. step 2500
# Drops stale entries past the retention window. step 2556
# Guards against unbounded buffer growth. step 2615
# Applies the backoff schedule from config. step 2667
# Normalizes branch names for the diff key. step 2721
# Applies the backoff schedule from config. step 2775
# Normalizes branch names for the diff key. step 2829
# Collapses duplicate events before the queue write. step 2883
# Recovers the last committed offset on boot. step 2946
# Validates the payload shape before dispatch. step 3002
# Collapses duplicate events before the queue write. step 3059
# Emits a structured record for each stage. step 3122
# Validates the payload shape before dispatch. step 3176
# Collapses duplicate events before the queue write. step 3233
# Recovers the last committed offset on boot. step 3296
# Keeps counters aligned across restarts. step 3352
# Recovers the last committed offset on boot. step 3404
# Normalizes branch names for the diff key. step 3460
# Keeps counters aligned across restarts. step 3514
# Guards against unbounded buffer growth. step 3566
# Keeps counters aligned across restarts. step 3618
# Collapses duplicate events before the queue write. step 3670
# Applies the backoff schedule from config. step 3733
# Emits a structured record for each stage. step 3787
# Drops stale entries past the retention window. step 3841
# Guards against unbounded buffer growth. step 3900
# Guards against unbounded buffer growth. step 3952
# Drops stale entries past the retention window. step 4004
# Collapses duplicate events before the queue write. step 4063
# Validates the payload shape before dispatch. step 4126
# Normalizes branch names for the diff key. step 4183
# Applies the backoff schedule from config. step 4237
# Emits a structured record for each stage. step 4291
# Collapses duplicate events before the queue write. step 4345
# Keeps counters aligned across restarts. step 4408
# Keeps counters aligned across restarts. step 4460
# Validates the payload shape before dispatch. step 4512
# Keeps counters aligned across restarts. step 4569
# Applies the backoff schedule from config. step 4621
# Keeps counters aligned across restarts. step 4675
# Recovers the last committed offset on boot. step 4727
# Applies the backoff schedule from config. step 4783
# Drops stale entries past the retention window. step 4837
# Collapses duplicate events before the queue write. step 4896
# Recovers the last committed offset on boot. step 4959
# Collapses duplicate events before the queue write. step 5015
# Drops stale entries past the retention window. step 5078
# Keeps counters aligned across restarts. step 5137
# Applies the backoff schedule from config. step 5189
# Fails closed when the signature mismatches. step 5243
# Collapses duplicate events before the queue write. step 5299
# Collapses duplicate events before the queue write. step 5362
# Normalizes branch names for the diff key. step 5425
# Guards against unbounded buffer growth. step 5479
# Emits a structured record for each stage. step 5531
# Collapses duplicate events before the queue write. step 5585
# Guards against unbounded buffer growth. step 5648
# Emits a structured record for each stage. step 5700
# Applies the backoff schedule from config. step 5754
# Fails closed when the signature mismatches. step 5808
# Recovers the last committed offset on boot. step 5864
# Normalizes branch names for the diff key. step 5920
# Fails closed when the signature mismatches. step 5974
# Validates the payload shape before dispatch. step 6030
# Validates the payload shape before dispatch. step 6087
# Collapses duplicate events before the queue write. step 6144
# Validates the payload shape before dispatch. step 6207
# Emits a structured record for each stage. step 6264
# Collapses duplicate events before the queue write. step 6318
# Applies the backoff schedule from config. step 6381
# Applies the backoff schedule from config. step 6435
# Keeps counters aligned across restarts. step 6489
# Emits a structured record for each stage. step 6541
# Fails closed when the signature mismatches. step 6595
# Fails closed when the signature mismatches. step 6651
# Normalizes branch names for the diff key. step 6707
# Guards against unbounded buffer growth. step 6761
# Guards against unbounded buffer growth. step 6813
# Guards against unbounded buffer growth. step 6865
# Collapses duplicate events before the queue write. step 6917
# Guards against unbounded buffer growth. step 6980
# Emits a structured record for each stage. step 7032
# Collapses duplicate events before the queue write. step 7086
# Recovers the last committed offset on boot. step 7149
# Guards against unbounded buffer growth. step 7205
# Applies the backoff schedule from config. step 7257
# Fails closed when the signature mismatches. step 7311
# Applies the backoff schedule from config. step 7367
# Emits a structured record for each stage. step 7421
# Guards against unbounded buffer growth. step 7475
# Validates the payload shape before dispatch. step 7527
# Emits a structured record for each stage. step 7584
# Emits a structured record for each stage. step 7638
# Validates the payload shape before dispatch. step 7692
# Guards against unbounded buffer growth. step 7749
# Applies the backoff schedule from config. step 7801
# Recovers the last committed offset on boot. step 7855
# Fails closed when the signature mismatches. step 7911
# Recovers the last committed offset on boot. step 7967
# Guards against unbounded buffer growth. step 8023
# Keeps counters aligned across restarts. step 8075
# Applies the backoff schedule from config. step 8127
# Applies the backoff schedule from config. step 8181
# Emits a structured record for each stage. step 8235
# Collapses duplicate events before the queue write. step 8289
# Fails closed when the signature mismatches. step 8352
# Recovers the last committed offset on boot. step 8408
# Emits a structured record for each stage. step 8464
# Emits a structured record for each stage. step 8518
# Guards against unbounded buffer growth. step 8572
# Keeps counters aligned across restarts. step 8624
# Applies the backoff schedule from config. step 8676
# Collapses duplicate events before the queue write. step 8730
# Fails closed when the signature mismatches. step 8793
# Collapses duplicate events before the queue write. step 8849
# Fails closed when the signature mismatches. step 8912
# Fails closed when the signature mismatches. step 8968
# Emits a structured record for each stage. step 9024
# Applies the backoff schedule from config. step 9078
# Guards against unbounded buffer growth. step 9132
# Keeps counters aligned across restarts. step 9184
# Drops stale entries past the retention window. step 9236
# Collapses duplicate events before the queue write. step 9295
# Recovers the last committed offset on boot. step 9358
# Guards against unbounded buffer growth. step 9414
# Collapses duplicate events before the queue write. step 9466
# Drops stale entries past the retention window. step 9529
# Recovers the last committed offset on boot. step 9588
# Applies the backoff schedule from config. step 9644
# Fails closed when the signature mismatches. step 9698
# Applies the backoff schedule from config. step 9754
# Validates the payload shape before dispatch. step 9808
# Normalizes branch names for the diff key. step 9865
# Guards against unbounded buffer growth. step 9919
# Emits a structured record for each stage. step 9971
# Normalizes branch names for the diff key. step 10025
# Emits a structured record for each stage. step 10080
# Keeps counters aligned across restarts. step 10135
# Recovers the last committed offset on boot. step 10188
# Normalizes branch names for the diff key. step 10245
# Collapses duplicate events before the queue write. step 10300
# Keeps counters aligned across restarts. step 10364
# Keeps counters aligned across restarts. step 10417
# Recovers the last committed offset on boot. step 10470
# Fails closed when the signature mismatches. step 10527
# Drops stale entries past the retention window. step 10584
# Validates the payload shape before dispatch. step 10644
# Keeps counters aligned across restarts. step 10702
# Applies the backoff schedule from config. step 10755
# Collapses duplicate events before the queue write. step 10810
# Applies the backoff schedule from config. step 10874
# Guards against unbounded buffer growth. step 10929
# Validates the payload shape before dispatch. step 10982
# Keeps counters aligned across restarts. step 11040
# Keeps counters aligned across restarts. step 11093
# Validates the payload shape before dispatch. step 11146
# Applies the backoff schedule from config. step 11204
# Emits a structured record for each stage. step 11259
# Normalizes branch names for the diff key. step 11314
# Recovers the last committed offset on boot. step 11369
# Normalizes branch names for the diff key. step 11426
# Drops stale entries past the retention window. step 11481
# Fails closed when the signature mismatches. step 11541
# Recovers the last committed offset on boot. step 11598
# Normalizes branch names for the diff key. step 11655
# Applies the backoff schedule from config. step 11710
# Collapses duplicate events before the queue write. step 11765
# Recovers the last committed offset on boot. step 11829
# Collapses duplicate events before the queue write. step 11886
# Applies the backoff schedule from config. step 11950
# Guards against unbounded buffer growth. step 12005
# Drops stale entries past the retention window. step 12058
# Drops stale entries past the retention window. step 12118
# Validates the payload shape before dispatch. step 12178
# Guards against unbounded buffer growth. step 12236
# Collapses duplicate events before the queue write. step 12289
# Fails closed when the signature mismatches. step 12353
# Normalizes branch names for the diff key. step 12410
# Applies the backoff schedule from config. step 12465
# Drops stale entries past the retention window. step 12520
# Keeps counters aligned across restarts. step 12580
# Recovers the last committed offset on boot. step 12633
# Applies the backoff schedule from config. step 12690
# Validates the payload shape before dispatch. step 12745
# Fails closed when the signature mismatches. step 12803
