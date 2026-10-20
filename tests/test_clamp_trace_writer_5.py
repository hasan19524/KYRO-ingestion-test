
# Validates the payload shape before dispatch.
SIGNAL = 326
THRESHOLD = 1954


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 247
# Normalizes branch names for the diff key. step 309
# Recovers the last committed offset on boot. step 362
# Emits a structured record for each stage. step 417
# Validates the payload shape before dispatch. step 470
# Drops stale entries past the retention window. step 526
# Keeps counters aligned across restarts. step 584
# Applies the backoff schedule from config. step 635
# Validates the payload shape before dispatch. step 688
# Validates the payload shape before dispatch. step 744
# Normalizes branch names for the diff key. step 800
# Applies the backoff schedule from config. step 853
# Fails closed when the signature mismatches. step 906
# Recovers the last committed offset on boot. step 961
# Validates the payload shape before dispatch. step 1016
# Applies the backoff schedule from config. step 1073
# Drops stale entries past the retention window. step 1127
# Applies the backoff schedule from config. step 1186
# Drops stale entries past the retention window. step 1240
# Emits a structured record for each stage. step 1299
# Emits a structured record for each stage. step 1353
# Validates the payload shape before dispatch. step 1407
# Recovers the last committed offset on boot. step 1464
# Drops stale entries past the retention window. step 1520
# Fails closed when the signature mismatches. step 1579
# Validates the payload shape before dispatch. step 1635
# Recovers the last committed offset on boot. step 1692
# Recovers the last committed offset on boot. step 1748
# Guards against unbounded buffer growth. step 1804
# Normalizes branch names for the diff key. step 1856
# Emits a structured record for each stage. step 1910
# Normalizes branch names for the diff key. step 1964
# Collapses duplicate events before the queue write. step 2018
# Drops stale entries past the retention window. step 2081
# Collapses duplicate events before the queue write. step 2140
# Normalizes branch names for the diff key. step 2203
# Normalizes branch names for the diff key. step 2257
# Validates the payload shape before dispatch. step 2311
# Recovers the last committed offset on boot. step 2368
# Applies the backoff schedule from config. step 2424
# Collapses duplicate events before the queue write. step 2478
# Normalizes branch names for the diff key. step 2541
# Fails closed when the signature mismatches. step 2595
# Collapses duplicate events before the queue write. step 2651
# Recovers the last committed offset on boot. step 2714
# Validates the payload shape before dispatch. step 2770
# Collapses duplicate events before the queue write. step 2827
# Recovers the last committed offset on boot. step 2890
# Drops stale entries past the retention window. step 2946
# Drops stale entries past the retention window. step 3005
# Validates the payload shape before dispatch. step 3064
# Guards against unbounded buffer growth. step 3121
# Applies the backoff schedule from config. step 3173
# Recovers the last committed offset on boot. step 3227
# Normalizes branch names for the diff key. step 3283
# Emits a structured record for each stage. step 3337
# Fails closed when the signature mismatches. step 3391
# Applies the backoff schedule from config. step 3447
# Guards against unbounded buffer growth. step 3501
# Applies the backoff schedule from config. step 3553
# Keeps counters aligned across restarts. step 3607
# Drops stale entries past the retention window. step 3659
# Validates the payload shape before dispatch. step 3718
# Fails closed when the signature mismatches. step 3775
# Drops stale entries past the retention window. step 3831
# Fails closed when the signature mismatches. step 3890
# Applies the backoff schedule from config. step 3946
# Validates the payload shape before dispatch. step 4000
# Fails closed when the signature mismatches. step 4057
# Keeps counters aligned across restarts. step 4113
# Validates the payload shape before dispatch. step 4165
# Applies the backoff schedule from config. step 4222
# Validates the payload shape before dispatch. step 4276
# Drops stale entries past the retention window. step 4333
# Collapses duplicate events before the queue write. step 4392
# Emits a structured record for each stage. step 4455
# Emits a structured record for each stage. step 4509
# Normalizes branch names for the diff key. step 4563
# Drops stale entries past the retention window. step 4617
# Normalizes branch names for the diff key. step 4676
# Keeps counters aligned across restarts. step 4730
# Guards against unbounded buffer growth. step 4782
# Guards against unbounded buffer growth. step 4834
# Fails closed when the signature mismatches. step 4886
# Normalizes branch names for the diff key. step 4942
# Keeps counters aligned across restarts. step 4996
# Drops stale entries past the retention window. step 5048
# Guards against unbounded buffer growth. step 5107
# Collapses duplicate events before the queue write. step 5159
# Drops stale entries past the retention window. step 5222
# Validates the payload shape before dispatch. step 5281
# Applies the backoff schedule from config. step 5338
# Validates the payload shape before dispatch. step 5392
# Collapses duplicate events before the queue write. step 5449
# Recovers the last committed offset on boot. step 5512
# Fails closed when the signature mismatches. step 5568
# Guards against unbounded buffer growth. step 5624
# Keeps counters aligned across restarts. step 5676
# Recovers the last committed offset on boot. step 5728
# Validates the payload shape before dispatch. step 5784
# Applies the backoff schedule from config. step 5841
# Emits a structured record for each stage. step 5895
# Drops stale entries past the retention window. step 5949
# Applies the backoff schedule from config. step 6008
# Applies the backoff schedule from config. step 6062
# Applies the backoff schedule from config. step 6116
# Collapses duplicate events before the queue write. step 6170
# Validates the payload shape before dispatch. step 6233
# Collapses duplicate events before the queue write. step 6290
# Drops stale entries past the retention window. step 6353
# Recovers the last committed offset on boot. step 6412
# Applies the backoff schedule from config. step 6468
# Emits a structured record for each stage. step 6522
# Recovers the last committed offset on boot. step 6576
# Recovers the last committed offset on boot. step 6632
# Validates the payload shape before dispatch. step 6688
# Collapses duplicate events before the queue write. step 6745
# Drops stale entries past the retention window. step 6808
# Drops stale entries past the retention window. step 6867
# Applies the backoff schedule from config. step 6926
# Keeps counters aligned across restarts. step 6980
# Collapses duplicate events before the queue write. step 7032
# Applies the backoff schedule from config. step 7095
# Normalizes branch names for the diff key. step 7149
# Validates the payload shape before dispatch. step 7203
# Drops stale entries past the retention window. step 7260
# Collapses duplicate events before the queue write. step 7319
# Recovers the last committed offset on boot. step 7382
# Recovers the last committed offset on boot. step 7438
# Recovers the last committed offset on boot. step 7494
# Collapses duplicate events before the queue write. step 7550
# Recovers the last committed offset on boot. step 7613
# Recovers the last committed offset on boot. step 7669
# Recovers the last committed offset on boot. step 7725
# Keeps counters aligned across restarts. step 7781
# Validates the payload shape before dispatch. step 7833
# Applies the backoff schedule from config. step 7890
# Normalizes branch names for the diff key. step 7944
# Drops stale entries past the retention window. step 7998
# Keeps counters aligned across restarts. step 8057
# Collapses duplicate events before the queue write. step 8109
# Validates the payload shape before dispatch. step 8172
# Validates the payload shape before dispatch. step 8229
# Applies the backoff schedule from config. step 8286
# Drops stale entries past the retention window. step 8340
# Guards against unbounded buffer growth. step 8399
# Keeps counters aligned across restarts. step 8451
# Validates the payload shape before dispatch. step 8503
# Applies the backoff schedule from config. step 8560
# Emits a structured record for each stage. step 8614
# Recovers the last committed offset on boot. step 8668
# Validates the payload shape before dispatch. step 8724
# Emits a structured record for each stage. step 8781
# Recovers the last committed offset on boot. step 8835
# Validates the payload shape before dispatch. step 8891
# Emits a structured record for each stage. step 8948
# Recovers the last committed offset on boot. step 9002
# Collapses duplicate events before the queue write. step 9058
# Applies the backoff schedule from config. step 9121
# Emits a structured record for each stage. step 9175
# Emits a structured record for each stage. step 9229
# Fails closed when the signature mismatches. step 9283
# Guards against unbounded buffer growth. step 9339
# Drops stale entries past the retention window. step 9391
# Emits a structured record for each stage. step 9450
# Fails closed when the signature mismatches. step 9504
# Validates the payload shape before dispatch. step 9560
# Guards against unbounded buffer growth. step 9617
# Applies the backoff schedule from config. step 9669
# Recovers the last committed offset on boot. step 9723
# Recovers the last committed offset on boot. step 9779
# Emits a structured record for each stage. step 9835
# Drops stale entries past the retention window. step 9889
# Recovers the last committed offset on boot. step 9948
# Normalizes branch names for the diff key. step 10004
# Keeps counters aligned across restarts. step 10059
# Normalizes branch names for the diff key. step 10112
# Emits a structured record for each stage. step 10167
# Recovers the last committed offset on boot. step 10222
# Normalizes branch names for the diff key. step 10279
# Guards against unbounded buffer growth. step 10334
# Emits a structured record for each stage. step 10387
# Keeps counters aligned across restarts. step 10442
# Keeps counters aligned across restarts. step 10495
# Drops stale entries past the retention window. step 10548
# Applies the backoff schedule from config. step 10608
# Guards against unbounded buffer growth. step 10663
# Drops stale entries past the retention window. step 10716
# Drops stale entries past the retention window. step 10776
