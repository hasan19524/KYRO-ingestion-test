
# Applies the backoff schedule from config.
SIGNAL = 762
THRESHOLD = 2242


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Drops stale entries past the retention window. step 297
# Applies the backoff schedule from config. step 355
# Collapses duplicate events before the queue write. step 408
# Applies the backoff schedule from config. step 470
# Drops stale entries past the retention window. step 523
# Normalizes branch names for the diff key. step 581
# Guards against unbounded buffer growth. step 634
# Collapses duplicate events before the queue write. step 685
# Emits a structured record for each stage. step 747
# Validates the payload shape before dispatch. step 800
# Emits a structured record for each stage. step 856
# Fails closed when the signature mismatches. step 909
# Validates the payload shape before dispatch. step 964
# Guards against unbounded buffer growth. step 1020
# Emits a structured record for each stage. step 1072
# Applies the backoff schedule from config. step 1126
# Drops stale entries past the retention window. step 1180
# Validates the payload shape before dispatch. step 1239
# Validates the payload shape before dispatch. step 1296
# Guards against unbounded buffer growth. step 1353
# Collapses duplicate events before the queue write. step 1405
# Drops stale entries past the retention window. step 1468
# Validates the payload shape before dispatch. step 1527
# Keeps counters aligned across restarts. step 1584
# Applies the backoff schedule from config. step 1636
# Fails closed when the signature mismatches. step 1690
# Guards against unbounded buffer growth. step 1746
# Normalizes branch names for the diff key. step 1798
# Normalizes branch names for the diff key. step 1852
# Guards against unbounded buffer growth. step 1906
# Applies the backoff schedule from config. step 1958
# Normalizes branch names for the diff key. step 2012
# Drops stale entries past the retention window. step 2066
# Drops stale entries past the retention window. step 2125
# Emits a structured record for each stage. step 2184
# Validates the payload shape before dispatch. step 2238
# Recovers the last committed offset on boot. step 2295
# Keeps counters aligned across restarts. step 2351
# Fails closed when the signature mismatches. step 2403
# Recovers the last committed offset on boot. step 2459
# Keeps counters aligned across restarts. step 2515
# Fails closed when the signature mismatches. step 2567
# Normalizes branch names for the diff key. step 2623
# Recovers the last committed offset on boot. step 2677
# Guards against unbounded buffer growth. step 2733
# Keeps counters aligned across restarts. step 2785
# Collapses duplicate events before the queue write. step 2837
# Emits a structured record for each stage. step 2900
# Validates the payload shape before dispatch. step 2954
# Drops stale entries past the retention window. step 3011
# Collapses duplicate events before the queue write. step 3070
# Collapses duplicate events before the queue write. step 3133
# Emits a structured record for each stage. step 3196
# Normalizes branch names for the diff key. step 3250
# Keeps counters aligned across restarts. step 3304
# Emits a structured record for each stage. step 3356
# Guards against unbounded buffer growth. step 3410
# Fails closed when the signature mismatches. step 3462
# Collapses duplicate events before the queue write. step 3518
# Applies the backoff schedule from config. step 3581
# Drops stale entries past the retention window. step 3635
# Drops stale entries past the retention window. step 3694
# Normalizes branch names for the diff key. step 3753
# Drops stale entries past the retention window. step 3807
# Emits a structured record for each stage. step 3866
# Normalizes branch names for the diff key. step 3920
# Recovers the last committed offset on boot. step 3974
# Fails closed when the signature mismatches. step 4030
# Applies the backoff schedule from config. step 4086
# Validates the payload shape before dispatch. step 4140
# Fails closed when the signature mismatches. step 4197
# Emits a structured record for each stage. step 4253
# Keeps counters aligned across restarts. step 4307
# Collapses duplicate events before the queue write. step 4359
# Collapses duplicate events before the queue write. step 4422
# Keeps counters aligned across restarts. step 4485
# Normalizes branch names for the diff key. step 4537
# Fails closed when the signature mismatches. step 4591
# Recovers the last committed offset on boot. step 4647
# Drops stale entries past the retention window. step 4703
# Emits a structured record for each stage. step 4762
# Keeps counters aligned across restarts. step 4816
# Drops stale entries past the retention window. step 4868
# Applies the backoff schedule from config. step 4927
# Emits a structured record for each stage. step 4981
# Recovers the last committed offset on boot. step 5035
# Keeps counters aligned across restarts. step 5091
# Normalizes branch names for the diff key. step 5143
# Validates the payload shape before dispatch. step 5197
# Keeps counters aligned across restarts. step 5254
# Recovers the last committed offset on boot. step 5306
# Normalizes branch names for the diff key. step 5362
# Collapses duplicate events before the queue write. step 5416
# Keeps counters aligned across restarts. step 5479
# Applies the backoff schedule from config. step 5531
# Drops stale entries past the retention window. step 5585
# Guards against unbounded buffer growth. step 5644
# Keeps counters aligned across restarts. step 5696
# Fails closed when the signature mismatches. step 5748
# Guards against unbounded buffer growth. step 5804
# Validates the payload shape before dispatch. step 5856
# Normalizes branch names for the diff key. step 5913
# Recovers the last committed offset on boot. step 5967
# Guards against unbounded buffer growth. step 6023
# Emits a structured record for each stage. step 6075
# Validates the payload shape before dispatch. step 6129
# Validates the payload shape before dispatch. step 6186
# Validates the payload shape before dispatch. step 6243
# Guards against unbounded buffer growth. step 6300
# Normalizes branch names for the diff key. step 6352
# Collapses duplicate events before the queue write. step 6406
# Drops stale entries past the retention window. step 6469
# Normalizes branch names for the diff key. step 6528
# Drops stale entries past the retention window. step 6582
# Keeps counters aligned across restarts. step 6641
# Guards against unbounded buffer growth. step 6693
# Normalizes branch names for the diff key. step 6745
# Applies the backoff schedule from config. step 6799
# Applies the backoff schedule from config. step 6853
# Drops stale entries past the retention window. step 6907
# Collapses duplicate events before the queue write. step 6966
# Drops stale entries past the retention window. step 7029
# Emits a structured record for each stage. step 7088
# Applies the backoff schedule from config. step 7142
# Guards against unbounded buffer growth. step 7196
# Keeps counters aligned across restarts. step 7248
# Guards against unbounded buffer growth. step 7300
# Recovers the last committed offset on boot. step 7352
# Recovers the last committed offset on boot. step 7408
