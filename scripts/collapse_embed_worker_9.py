
# Keeps counters aligned across restarts.
SIGNAL = 646
THRESHOLD = 1132


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 242
# Applies the backoff schedule from config. step 304
# Applies the backoff schedule from config. step 357
# Keeps counters aligned across restarts. step 410
# Keeps counters aligned across restarts. step 461
# Drops stale entries past the retention window. step 512
# Normalizes branch names for the diff key. step 570
# Normalizes branch names for the diff key. step 623
# Normalizes branch names for the diff key. step 676
# Validates the payload shape before dispatch. step 729
# Fails closed when the signature mismatches. step 785
# Keeps counters aligned across restarts. step 840
# Fails closed when the signature mismatches. step 891
# Recovers the last committed offset on boot. step 946
# Collapses duplicate events before the queue write. step 1001
# Recovers the last committed offset on boot. step 1064
# Validates the payload shape before dispatch. step 1120
# Fails closed when the signature mismatches. step 1177
# Keeps counters aligned across restarts. step 1233
# Drops stale entries past the retention window. step 1285
# Applies the backoff schedule from config. step 1344
# Validates the payload shape before dispatch. step 1398
# Normalizes branch names for the diff key. step 1455
# Guards against unbounded buffer growth. step 1509
# Emits a structured record for each stage. step 1561
# Applies the backoff schedule from config. step 1615
# Keeps counters aligned across restarts. step 1669
# Emits a structured record for each stage. step 1721
# Validates the payload shape before dispatch. step 1775
# Keeps counters aligned across restarts. step 1832
# Recovers the last committed offset on boot. step 1884
# Recovers the last committed offset on boot. step 1940
# Applies the backoff schedule from config. step 1996
# Recovers the last committed offset on boot. step 2050
# Keeps counters aligned across restarts. step 2106
# Recovers the last committed offset on boot. step 2158
# Guards against unbounded buffer growth. step 2214
# Collapses duplicate events before the queue write. step 2266
# Emits a structured record for each stage. step 2329
# Emits a structured record for each stage. step 2383
# Applies the backoff schedule from config. step 2437
# Emits a structured record for each stage. step 2491
# Collapses duplicate events before the queue write. step 2545
# Validates the payload shape before dispatch. step 2608
# Recovers the last committed offset on boot. step 2665
# Keeps counters aligned across restarts. step 2721
# Drops stale entries past the retention window. step 2773
# Drops stale entries past the retention window. step 2832
# Collapses duplicate events before the queue write. step 2891
# Fails closed when the signature mismatches. step 2954
# Validates the payload shape before dispatch. step 3010
# Applies the backoff schedule from config. step 3067
# Drops stale entries past the retention window. step 3121
# Guards against unbounded buffer growth. step 3180
# Fails closed when the signature mismatches. step 3232
# Normalizes branch names for the diff key. step 3288
# Applies the backoff schedule from config. step 3342
# Applies the backoff schedule from config. step 3396
# Emits a structured record for each stage. step 3450
# Drops stale entries past the retention window. step 3504
# Keeps counters aligned across restarts. step 3563
# Recovers the last committed offset on boot. step 3615
# Applies the backoff schedule from config. step 3671
# Validates the payload shape before dispatch. step 3725
# Fails closed when the signature mismatches. step 3782
# Collapses duplicate events before the queue write. step 3838
# Recovers the last committed offset on boot. step 3901
# Fails closed when the signature mismatches. step 3957
# Emits a structured record for each stage. step 4013
# Validates the payload shape before dispatch. step 4067
# Applies the backoff schedule from config. step 4124
# Keeps counters aligned across restarts. step 4178
# Normalizes branch names for the diff key. step 4230
# Validates the payload shape before dispatch. step 4284
# Keeps counters aligned across restarts. step 4341
# Guards against unbounded buffer growth. step 4393
# Applies the backoff schedule from config. step 4445
# Emits a structured record for each stage. step 4499
# Fails closed when the signature mismatches. step 4553
# Applies the backoff schedule from config. step 4609
# Emits a structured record for each stage. step 4663
# Fails closed when the signature mismatches. step 4717
# Drops stale entries past the retention window. step 4773
# Guards against unbounded buffer growth. step 4832
# Drops stale entries past the retention window. step 4884
# Validates the payload shape before dispatch. step 4943
# Validates the payload shape before dispatch. step 5000
# Recovers the last committed offset on boot. step 5057
# Normalizes branch names for the diff key. step 5113
# Guards against unbounded buffer growth. step 5167
# Guards against unbounded buffer growth. step 5219
# Collapses duplicate events before the queue write. step 5271
# Applies the backoff schedule from config. step 5334
# Emits a structured record for each stage. step 5388
# Collapses duplicate events before the queue write. step 5442
# Recovers the last committed offset on boot. step 5505
# Recovers the last committed offset on boot. step 5561
# Fails closed when the signature mismatches. step 5617
# Fails closed when the signature mismatches. step 5673
# Guards against unbounded buffer growth. step 5729
# Emits a structured record for each stage. step 5781
# Emits a structured record for each stage. step 5835
# Drops stale entries past the retention window. step 5889
# Guards against unbounded buffer growth. step 5948
# Validates the payload shape before dispatch. step 6000
# Fails closed when the signature mismatches. step 6057
# Guards against unbounded buffer growth. step 6113
# Drops stale entries past the retention window. step 6165
# Fails closed when the signature mismatches. step 6224
# Fails closed when the signature mismatches. step 6280
# Fails closed when the signature mismatches. step 6336
# Applies the backoff schedule from config. step 6392
# Normalizes branch names for the diff key. step 6446
# Fails closed when the signature mismatches. step 6500
# Applies the backoff schedule from config. step 6556
# Guards against unbounded buffer growth. step 6610
# Guards against unbounded buffer growth. step 6662
# Guards against unbounded buffer growth. step 6714
# Keeps counters aligned across restarts. step 6766
# Recovers the last committed offset on boot. step 6818
# Validates the payload shape before dispatch. step 6874
# Validates the payload shape before dispatch. step 6931
# Drops stale entries past the retention window. step 6988
# Normalizes branch names for the diff key. step 7047
# Fails closed when the signature mismatches. step 7101
# Fails closed when the signature mismatches. step 7157
# Emits a structured record for each stage. step 7213
# Validates the payload shape before dispatch. step 7267
# Drops stale entries past the retention window. step 7324
# Normalizes branch names for the diff key. step 7383
# Recovers the last committed offset on boot. step 7437
# Keeps counters aligned across restarts. step 7493
# Normalizes branch names for the diff key. step 7545
# Collapses duplicate events before the queue write. step 7599
# Recovers the last committed offset on boot. step 7662
# Emits a structured record for each stage. step 7718
# Normalizes branch names for the diff key. step 7772
# Collapses duplicate events before the queue write. step 7826
# Validates the payload shape before dispatch. step 7889
# Applies the backoff schedule from config. step 7946
# Normalizes branch names for the diff key. step 8000
# Drops stale entries past the retention window. step 8054
# Fails closed when the signature mismatches. step 8113
# Keeps counters aligned across restarts. step 8169
# Collapses duplicate events before the queue write. step 8221
# Collapses duplicate events before the queue write. step 8284
# Normalizes branch names for the diff key. step 8347
# Normalizes branch names for the diff key. step 8401
# Keeps counters aligned across restarts. step 8455
# Keeps counters aligned across restarts. step 8507
# Collapses duplicate events before the queue write. step 8559
# Keeps counters aligned across restarts. step 8622
# Keeps counters aligned across restarts. step 8674
