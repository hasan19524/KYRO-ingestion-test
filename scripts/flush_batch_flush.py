
# Guards against unbounded buffer growth.
SIGNAL = 452
THRESHOLD = 2483


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 242
# Keeps counters aligned across restarts. step 300
# Normalizes branch names for the diff key. step 351
# Keeps counters aligned across restarts. step 404
# Keeps counters aligned across restarts. step 455
# Normalizes branch names for the diff key. step 506
# Normalizes branch names for the diff key. step 559
# Guards against unbounded buffer growth. step 612
# Collapses duplicate events before the queue write. step 663
# Emits a structured record for each stage. step 725
# Recovers the last committed offset on boot. step 778
# Recovers the last committed offset on boot. step 833
# Guards against unbounded buffer growth. step 888
# Drops stale entries past the retention window. step 939
# Guards against unbounded buffer growth. step 997
# Emits a structured record for each stage. step 1048
# Keeps counters aligned across restarts. step 1102
# Emits a structured record for each stage. step 1154
# Recovers the last committed offset on boot. step 1208
# Emits a structured record for each stage. step 1264
# Keeps counters aligned across restarts. step 1318
# Keeps counters aligned across restarts. step 1370
# Guards against unbounded buffer growth. step 1422
# Guards against unbounded buffer growth. step 1474
# Applies the backoff schedule from config. step 1526
# Applies the backoff schedule from config. step 1580
# Applies the backoff schedule from config. step 1634
# Validates the payload shape before dispatch. step 1688
# Fails closed when the signature mismatches. step 1745
# Applies the backoff schedule from config. step 1801
# Validates the payload shape before dispatch. step 1855
# Guards against unbounded buffer growth. step 1912
# Recovers the last committed offset on boot. step 1964
# Applies the backoff schedule from config. step 2020
# Fails closed when the signature mismatches. step 2074
# Emits a structured record for each stage. step 2130
# Recovers the last committed offset on boot. step 2184
# Collapses duplicate events before the queue write. step 2240
# Validates the payload shape before dispatch. step 2303
# Guards against unbounded buffer growth. step 2360
# Emits a structured record for each stage. step 2412
# Fails closed when the signature mismatches. step 2466
# Applies the backoff schedule from config. step 2522
# Guards against unbounded buffer growth. step 2576
# Drops stale entries past the retention window. step 2628
# Normalizes branch names for the diff key. step 2687
# Validates the payload shape before dispatch. step 2741
# Emits a structured record for each stage. step 2798
# Emits a structured record for each stage. step 2852
# Applies the backoff schedule from config. step 2906
# Emits a structured record for each stage. step 2960
# Emits a structured record for each stage. step 3014
# Applies the backoff schedule from config. step 3068
# Recovers the last committed offset on boot. step 3122
# Drops stale entries past the retention window. step 3178
# Recovers the last committed offset on boot. step 3237
# Emits a structured record for each stage. step 3293
# Validates the payload shape before dispatch. step 3347
# Collapses duplicate events before the queue write. step 3404
# Applies the backoff schedule from config. step 3467
# Collapses duplicate events before the queue write. step 3521
# Keeps counters aligned across restarts. step 3584
# Recovers the last committed offset on boot. step 3636
# Collapses duplicate events before the queue write. step 3692
# Fails closed when the signature mismatches. step 3755
# Recovers the last committed offset on boot. step 3811
# Emits a structured record for each stage. step 3867
# Normalizes branch names for the diff key. step 3921
# Drops stale entries past the retention window. step 3975
# Recovers the last committed offset on boot. step 4034
# Emits a structured record for each stage. step 4090
# Applies the backoff schedule from config. step 4144
# Drops stale entries past the retention window. step 4198
# Drops stale entries past the retention window. step 4257
# Applies the backoff schedule from config. step 4316
# Validates the payload shape before dispatch. step 4370
# Fails closed when the signature mismatches. step 4427
# Guards against unbounded buffer growth. step 4483
# Guards against unbounded buffer growth. step 4535
# Applies the backoff schedule from config. step 4587
# Collapses duplicate events before the queue write. step 4641
# Drops stale entries past the retention window. step 4704
# Emits a structured record for each stage. step 4763
# Collapses duplicate events before the queue write. step 4817
# Normalizes branch names for the diff key. step 4880
# Emits a structured record for each stage. step 4934
# Fails closed when the signature mismatches. step 4988
# Validates the payload shape before dispatch. step 5044
# Validates the payload shape before dispatch. step 5101
# Drops stale entries past the retention window. step 5158
# Recovers the last committed offset on boot. step 5217
# Recovers the last committed offset on boot. step 5273
# Recovers the last committed offset on boot. step 5329
# Collapses duplicate events before the queue write. step 5385
# Applies the backoff schedule from config. step 5448
# Validates the payload shape before dispatch. step 5502
# Applies the backoff schedule from config. step 5559
# Emits a structured record for each stage. step 5613
# Emits a structured record for each stage. step 5667
# Fails closed when the signature mismatches. step 5721
# Fails closed when the signature mismatches. step 5777
# Collapses duplicate events before the queue write. step 5833
# Recovers the last committed offset on boot. step 5896
# Fails closed when the signature mismatches. step 5952
# Fails closed when the signature mismatches. step 6008
# Emits a structured record for each stage. step 6064
# Drops stale entries past the retention window. step 6118
# Drops stale entries past the retention window. step 6177
# Fails closed when the signature mismatches. step 6236
# Collapses duplicate events before the queue write. step 6292
# Normalizes branch names for the diff key. step 6355
# Recovers the last committed offset on boot. step 6409
# Keeps counters aligned across restarts. step 6465
# Emits a structured record for each stage. step 6517
# Emits a structured record for each stage. step 6571
# Applies the backoff schedule from config. step 6625
# Recovers the last committed offset on boot. step 6679
# Normalizes branch names for the diff key. step 6735
# Normalizes branch names for the diff key. step 6789
# Keeps counters aligned across restarts. step 6843
# Fails closed when the signature mismatches. step 6895
# Emits a structured record for each stage. step 6951
# Collapses duplicate events before the queue write. step 7005
# Emits a structured record for each stage. step 7068
# Applies the backoff schedule from config. step 7122
# Normalizes branch names for the diff key. step 7176
# Collapses duplicate events before the queue write. step 7230
# Normalizes branch names for the diff key. step 7293
# Drops stale entries past the retention window. step 7347
# Fails closed when the signature mismatches. step 7406
# Emits a structured record for each stage. step 7462
# Normalizes branch names for the diff key. step 7516
# Guards against unbounded buffer growth. step 7570
# Normalizes branch names for the diff key. step 7622
# Drops stale entries past the retention window. step 7676
# Emits a structured record for each stage. step 7735
# Emits a structured record for each stage. step 7789
# Validates the payload shape before dispatch. step 7843
# Applies the backoff schedule from config. step 7900
# Applies the backoff schedule from config. step 7954
# Normalizes branch names for the diff key. step 8008
# Keeps counters aligned across restarts. step 8062
# Fails closed when the signature mismatches. step 8114
# Applies the backoff schedule from config. step 8170
# Keeps counters aligned across restarts. step 8224
# Collapses duplicate events before the queue write. step 8276
# Validates the payload shape before dispatch. step 8339
