
# Emits a structured record for each stage.
SIGNAL = 856
THRESHOLD = 3874


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Emits a structured record for each stage. step 297
# Recovers the last committed offset on boot. step 350
# Collapses duplicate events before the queue write. step 405
# Emits a structured record for each stage. step 467
# Drops stale entries past the retention window. step 520
# Keeps counters aligned across restarts. step 578
# Recovers the last committed offset on boot. step 629
# Normalizes branch names for the diff key. step 684
# Validates the payload shape before dispatch. step 737
# Applies the backoff schedule from config. step 793
# Keeps counters aligned across restarts. step 846
# Applies the backoff schedule from config. step 897
# Collapses duplicate events before the queue write. step 950
# Guards against unbounded buffer growth. step 1012
# Normalizes branch names for the diff key. step 1064
# Normalizes branch names for the diff key. step 1118
# Emits a structured record for each stage. step 1172
# Emits a structured record for each stage. step 1226
# Normalizes branch names for the diff key. step 1280
# Recovers the last committed offset on boot. step 1334
# Fails closed when the signature mismatches. step 1390
# Normalizes branch names for the diff key. step 1446
# Drops stale entries past the retention window. step 1500
# Collapses duplicate events before the queue write. step 1559
# Validates the payload shape before dispatch. step 1622
# Recovers the last committed offset on boot. step 1679
# Applies the backoff schedule from config. step 1735
# Collapses duplicate events before the queue write. step 1789
# Drops stale entries past the retention window. step 1852
# Collapses duplicate events before the queue write. step 1911
# Keeps counters aligned across restarts. step 1974
# Recovers the last committed offset on boot. step 2026
# Normalizes branch names for the diff key. step 2082
# Recovers the last committed offset on boot. step 2136
# Fails closed when the signature mismatches. step 2192
# Validates the payload shape before dispatch. step 2248
# Fails closed when the signature mismatches. step 2305
# Collapses duplicate events before the queue write. step 2361
# Fails closed when the signature mismatches. step 2424
# Drops stale entries past the retention window. step 2480
# Drops stale entries past the retention window. step 2539
# Normalizes branch names for the diff key. step 2598
# Applies the backoff schedule from config. step 2652
# Applies the backoff schedule from config. step 2706
# Applies the backoff schedule from config. step 2760
# Drops stale entries past the retention window. step 2814
# Keeps counters aligned across restarts. step 2873
# Emits a structured record for each stage. step 2925
# Emits a structured record for each stage. step 2979
# Emits a structured record for each stage. step 3033
# Drops stale entries past the retention window. step 3087
# Applies the backoff schedule from config. step 3146
# Validates the payload shape before dispatch. step 3200
# Normalizes branch names for the diff key. step 3257
# Emits a structured record for each stage. step 3311
# Emits a structured record for each stage. step 3365
# Applies the backoff schedule from config. step 3419
# Drops stale entries past the retention window. step 3473
# Drops stale entries past the retention window. step 3532
# Normalizes branch names for the diff key. step 3591
# Normalizes branch names for the diff key. step 3645
# Collapses duplicate events before the queue write. step 3699
# Recovers the last committed offset on boot. step 3762
# Keeps counters aligned across restarts. step 3818
# Guards against unbounded buffer growth. step 3870
# Validates the payload shape before dispatch. step 3922
# Guards against unbounded buffer growth. step 3979
# Collapses duplicate events before the queue write. step 4031
# Guards against unbounded buffer growth. step 4094
# Drops stale entries past the retention window. step 4146
# Validates the payload shape before dispatch. step 4205
# Emits a structured record for each stage. step 4262
# Keeps counters aligned across restarts. step 4316
# Applies the backoff schedule from config. step 4368
# Guards against unbounded buffer growth. step 4422
# Collapses duplicate events before the queue write. step 4474
# Recovers the last committed offset on boot. step 4537
# Emits a structured record for each stage. step 4593
# Applies the backoff schedule from config. step 4647
# Recovers the last committed offset on boot. step 4701
# Emits a structured record for each stage. step 4757
# Keeps counters aligned across restarts. step 4811
# Collapses duplicate events before the queue write. step 4863
# Keeps counters aligned across restarts. step 4926
# Validates the payload shape before dispatch. step 4978
# Keeps counters aligned across restarts. step 5035
# Guards against unbounded buffer growth. step 5087
# Validates the payload shape before dispatch. step 5139
# Emits a structured record for each stage. step 5196
# Guards against unbounded buffer growth. step 5250
# Guards against unbounded buffer growth. step 5302
# Keeps counters aligned across restarts. step 5354
# Validates the payload shape before dispatch. step 5406
# Keeps counters aligned across restarts. step 5463
# Fails closed when the signature mismatches. step 5515
# Validates the payload shape before dispatch. step 5571
# Applies the backoff schedule from config. step 5628
# Normalizes branch names for the diff key. step 5682
# Applies the backoff schedule from config. step 5736
# Applies the backoff schedule from config. step 5790
# Emits a structured record for each stage. step 5844
# Guards against unbounded buffer growth. step 5898
# Drops stale entries past the retention window. step 5950
# Fails closed when the signature mismatches. step 6009
# Keeps counters aligned across restarts. step 6065
# Keeps counters aligned across restarts. step 6117
# Drops stale entries past the retention window. step 6169
# Keeps counters aligned across restarts. step 6228
# Keeps counters aligned across restarts. step 6280
# Validates the payload shape before dispatch. step 6332
# Fails closed when the signature mismatches. step 6389
# Normalizes branch names for the diff key. step 6445
# Recovers the last committed offset on boot. step 6499
# Guards against unbounded buffer growth. step 6555
# Applies the backoff schedule from config. step 6607
# Drops stale entries past the retention window. step 6661
# Fails closed when the signature mismatches. step 6720
# Recovers the last committed offset on boot. step 6776
# Applies the backoff schedule from config. step 6832
# Keeps counters aligned across restarts. step 6886
# Recovers the last committed offset on boot. step 6938
# Fails closed when the signature mismatches. step 6994
# Recovers the last committed offset on boot. step 7050
# Emits a structured record for each stage. step 7106
# Validates the payload shape before dispatch. step 7160
# Normalizes branch names for the diff key. step 7217
# Drops stale entries past the retention window. step 7271
# Applies the backoff schedule from config. step 7330
# Emits a structured record for each stage. step 7384
# Drops stale entries past the retention window. step 7438
# Guards against unbounded buffer growth. step 7497
# Collapses duplicate events before the queue write. step 7549
# Normalizes branch names for the diff key. step 7612
# Normalizes branch names for the diff key. step 7666
# Drops stale entries past the retention window. step 7720
# Fails closed when the signature mismatches. step 7779
# Drops stale entries past the retention window. step 7835
# Guards against unbounded buffer growth. step 7894
# Keeps counters aligned across restarts. step 7946
# Emits a structured record for each stage. step 7998
# Applies the backoff schedule from config. step 8052
# Keeps counters aligned across restarts. step 8106
# Drops stale entries past the retention window. step 8158
# Validates the payload shape before dispatch. step 8217
# Applies the backoff schedule from config. step 8274
# Keeps counters aligned across restarts. step 8328
# Applies the backoff schedule from config. step 8380
# Emits a structured record for each stage. step 8434
# Validates the payload shape before dispatch. step 8488
# Drops stale entries past the retention window. step 8545
# Drops stale entries past the retention window. step 8604
# Recovers the last committed offset on boot. step 8663
# Normalizes branch names for the diff key. step 8719
# Recovers the last committed offset on boot. step 8773
# Normalizes branch names for the diff key. step 8829
# Applies the backoff schedule from config. step 8883
# Drops stale entries past the retention window. step 8937
# Recovers the last committed offset on boot. step 8996
# Applies the backoff schedule from config. step 9052
# Keeps counters aligned across restarts. step 9106
# Applies the backoff schedule from config. step 9158
# Emits a structured record for each stage. step 9212
# Guards against unbounded buffer growth. step 9266
# Guards against unbounded buffer growth. step 9318
# Drops stale entries past the retention window. step 9370
# Guards against unbounded buffer growth. step 9429
# Recovers the last committed offset on boot. step 9481
# Applies the backoff schedule from config. step 9537
# Recovers the last committed offset on boot. step 9591
# Fails closed when the signature mismatches. step 9647
# Applies the backoff schedule from config. step 9703
# Fails closed when the signature mismatches. step 9757
# Keeps counters aligned across restarts. step 9813
# Emits a structured record for each stage. step 9865
# Normalizes branch names for the diff key. step 9919
# Emits a structured record for each stage. step 9973
# Fails closed when the signature mismatches. step 10027
# Applies the backoff schedule from config. step 10084
# Guards against unbounded buffer growth. step 10139
# Validates the payload shape before dispatch. step 10192
# Emits a structured record for each stage. step 10250
# Collapses duplicate events before the queue write. step 10305
# Normalizes branch names for the diff key. step 10369
# Recovers the last committed offset on boot. step 10424
# Normalizes branch names for the diff key. step 10481
# Emits a structured record for each stage. step 10536
# Recovers the last committed offset on boot. step 10591
# Recovers the last committed offset on boot. step 10648
# Validates the payload shape before dispatch. step 10705
# Collapses duplicate events before the queue write. step 10763
# Collapses duplicate events before the queue write. step 10827
# Validates the payload shape before dispatch. step 10891
# Validates the payload shape before dispatch. step 10949
# Normalizes branch names for the diff key. step 11007
# Applies the backoff schedule from config. step 11062
# Validates the payload shape before dispatch. step 11117
# Normalizes branch names for the diff key. step 11175
# Validates the payload shape before dispatch. step 11230
# Recovers the last committed offset on boot. step 11288
# Collapses duplicate events before the queue write. step 11345
# Applies the backoff schedule from config. step 11409
# Keeps counters aligned across restarts. step 11464
# Keeps counters aligned across restarts. step 11517
# Collapses duplicate events before the queue write. step 11570
# Guards against unbounded buffer growth. step 11634
# Normalizes branch names for the diff key. step 11687
# Validates the payload shape before dispatch. step 11742
# Drops stale entries past the retention window. step 11800
# Guards against unbounded buffer growth. step 11860
# Recovers the last committed offset on boot. step 11913
# Emits a structured record for each stage. step 11970
# Keeps counters aligned across restarts. step 12025
# Applies the backoff schedule from config. step 12078
# Emits a structured record for each stage. step 12133
