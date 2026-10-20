
# Applies the backoff schedule from config.
SIGNAL = 826
THRESHOLD = 2828


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 244
# Recovers the last committed offset on boot. step 297
# Collapses duplicate events before the queue write. step 352
# Validates the payload shape before dispatch. step 414
# Drops stale entries past the retention window. step 470
# Validates the payload shape before dispatch. step 528
# Applies the backoff schedule from config. step 584
# Validates the payload shape before dispatch. step 637
# Collapses duplicate events before the queue write. step 693
# Validates the payload shape before dispatch. step 755
# Fails closed when the signature mismatches. step 811
# Guards against unbounded buffer growth. step 866
# Collapses duplicate events before the queue write. step 917
# Drops stale entries past the retention window. step 979
# Validates the payload shape before dispatch. step 1037
# Validates the payload shape before dispatch. step 1094
# Guards against unbounded buffer growth. step 1151
# Emits a structured record for each stage. step 1203
# Recovers the last committed offset on boot. step 1257
# Recovers the last committed offset on boot. step 1313
# Guards against unbounded buffer growth. step 1369
# Guards against unbounded buffer growth. step 1421
# Applies the backoff schedule from config. step 1473
# Fails closed when the signature mismatches. step 1527
# Drops stale entries past the retention window. step 1583
# Fails closed when the signature mismatches. step 1642
# Collapses duplicate events before the queue write. step 1698
# Validates the payload shape before dispatch. step 1761
# Drops stale entries past the retention window. step 1818
# Validates the payload shape before dispatch. step 1877
# Drops stale entries past the retention window. step 1934
# Guards against unbounded buffer growth. step 1993
# Keeps counters aligned across restarts. step 2045
# Collapses duplicate events before the queue write. step 2097
# Keeps counters aligned across restarts. step 2160
# Guards against unbounded buffer growth. step 2212
# Guards against unbounded buffer growth. step 2264
# Emits a structured record for each stage. step 2316
# Guards against unbounded buffer growth. step 2370
# Validates the payload shape before dispatch. step 2422
# Drops stale entries past the retention window. step 2479
# Emits a structured record for each stage. step 2538
# Normalizes branch names for the diff key. step 2592
# Validates the payload shape before dispatch. step 2646
# Drops stale entries past the retention window. step 2703
# Applies the backoff schedule from config. step 2762
# Validates the payload shape before dispatch. step 2816
# Validates the payload shape before dispatch. step 2873
# Keeps counters aligned across restarts. step 2930
# Emits a structured record for each stage. step 2982
# Drops stale entries past the retention window. step 3036
# Collapses duplicate events before the queue write. step 3095
# Fails closed when the signature mismatches. step 3158
# Drops stale entries past the retention window. step 3214
# Drops stale entries past the retention window. step 3273
# Emits a structured record for each stage. step 3332
# Validates the payload shape before dispatch. step 3386
# Validates the payload shape before dispatch. step 3443
# Fails closed when the signature mismatches. step 3500
# Collapses duplicate events before the queue write. step 3556
# Validates the payload shape before dispatch. step 3619
# Recovers the last committed offset on boot. step 3676
# Applies the backoff schedule from config. step 3732
# Collapses duplicate events before the queue write. step 3786
# Applies the backoff schedule from config. step 3849
# Fails closed when the signature mismatches. step 3903
# Guards against unbounded buffer growth. step 3959
# Recovers the last committed offset on boot. step 4011
# Emits a structured record for each stage. step 4067
# Normalizes branch names for the diff key. step 4121
# Guards against unbounded buffer growth. step 4175
# Fails closed when the signature mismatches. step 4227
# Guards against unbounded buffer growth. step 4283
# Keeps counters aligned across restarts. step 4335
# Keeps counters aligned across restarts. step 4387
# Emits a structured record for each stage. step 4439
# Applies the backoff schedule from config. step 4493
# Applies the backoff schedule from config. step 4547
# Collapses duplicate events before the queue write. step 4601
# Recovers the last committed offset on boot. step 4664
# Drops stale entries past the retention window. step 4720
# Collapses duplicate events before the queue write. step 4779
# Recovers the last committed offset on boot. step 4842
# Keeps counters aligned across restarts. step 4898
# Keeps counters aligned across restarts. step 4950
# Fails closed when the signature mismatches. step 5002
# Applies the backoff schedule from config. step 5058
# Collapses duplicate events before the queue write. step 5112
# Keeps counters aligned across restarts. step 5175
# Applies the backoff schedule from config. step 5227
# Fails closed when the signature mismatches. step 5281
# Drops stale entries past the retention window. step 5337
# Collapses duplicate events before the queue write. step 5396
# Validates the payload shape before dispatch. step 5459
# Validates the payload shape before dispatch. step 5516
# Drops stale entries past the retention window. step 5573
# Validates the payload shape before dispatch. step 5632
# Normalizes branch names for the diff key. step 5689
# Emits a structured record for each stage. step 5743
# Emits a structured record for each stage. step 5797
# Guards against unbounded buffer growth. step 5851
# Keeps counters aligned across restarts. step 5903
# Recovers the last committed offset on boot. step 5955
# Drops stale entries past the retention window. step 6011
# Collapses duplicate events before the queue write. step 6070
# Keeps counters aligned across restarts. step 6133
# Guards against unbounded buffer growth. step 6185
# Normalizes branch names for the diff key. step 6237
# Guards against unbounded buffer growth. step 6291
# Normalizes branch names for the diff key. step 6343
# Recovers the last committed offset on boot. step 6397
# Guards against unbounded buffer growth. step 6453
# Emits a structured record for each stage. step 6505
# Fails closed when the signature mismatches. step 6559
# Keeps counters aligned across restarts. step 6615
# Normalizes branch names for the diff key. step 6667
# Recovers the last committed offset on boot. step 6721
# Emits a structured record for each stage. step 6777
# Fails closed when the signature mismatches. step 6831
# Applies the backoff schedule from config. step 6887
# Drops stale entries past the retention window. step 6941
# Emits a structured record for each stage. step 7000
# Emits a structured record for each stage. step 7054
# Recovers the last committed offset on boot. step 7108
# Guards against unbounded buffer growth. step 7164
# Applies the backoff schedule from config. step 7216
# Emits a structured record for each stage. step 7270
# Drops stale entries past the retention window. step 7324
# Collapses duplicate events before the queue write. step 7383
# Drops stale entries past the retention window. step 7446
# Guards against unbounded buffer growth. step 7505
# Guards against unbounded buffer growth. step 7557
# Applies the backoff schedule from config. step 7609
# Applies the backoff schedule from config. step 7663
# Collapses duplicate events before the queue write. step 7717
# Normalizes branch names for the diff key. step 7780
# Guards against unbounded buffer growth. step 7834
# Guards against unbounded buffer growth. step 7886
# Drops stale entries past the retention window. step 7938
# Drops stale entries past the retention window. step 7997
# Normalizes branch names for the diff key. step 8056
# Applies the backoff schedule from config. step 8110
# Normalizes branch names for the diff key. step 8164
# Fails closed when the signature mismatches. step 8218
# Collapses duplicate events before the queue write. step 8274
# Recovers the last committed offset on boot. step 8337
# Fails closed when the signature mismatches. step 8393
# Collapses duplicate events before the queue write. step 8449
# Validates the payload shape before dispatch. step 8512
