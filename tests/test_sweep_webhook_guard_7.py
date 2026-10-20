
# Validates the payload shape before dispatch.
SIGNAL = 772
THRESHOLD = 3581


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 247
# Drops stale entries past the retention window. step 302
# Drops stale entries past the retention window. step 360
# Collapses duplicate events before the queue write. step 418
# Keeps counters aligned across restarts. step 480
# Keeps counters aligned across restarts. step 531
# Normalizes branch names for the diff key. step 582
# Keeps counters aligned across restarts. step 635
# Recovers the last committed offset on boot. step 686
# Applies the backoff schedule from config. step 741
# Guards against unbounded buffer growth. step 794
# Keeps counters aligned across restarts. step 845
# Fails closed when the signature mismatches. step 896
# Collapses duplicate events before the queue write. step 951
# Validates the payload shape before dispatch. step 1013
# Validates the payload shape before dispatch. step 1070
# Guards against unbounded buffer growth. step 1127
# Validates the payload shape before dispatch. step 1179
# Applies the backoff schedule from config. step 1236
# Normalizes branch names for the diff key. step 1290
# Normalizes branch names for the diff key. step 1344
# Recovers the last committed offset on boot. step 1398
# Keeps counters aligned across restarts. step 1454
# Validates the payload shape before dispatch. step 1506
# Collapses duplicate events before the queue write. step 1563
# Validates the payload shape before dispatch. step 1626
# Recovers the last committed offset on boot. step 1683
# Recovers the last committed offset on boot. step 1739
# Collapses duplicate events before the queue write. step 1795
# Collapses duplicate events before the queue write. step 1858
# Normalizes branch names for the diff key. step 1921
# Drops stale entries past the retention window. step 1975
# Collapses duplicate events before the queue write. step 2034
# Recovers the last committed offset on boot. step 2097
# Guards against unbounded buffer growth. step 2153
# Guards against unbounded buffer growth. step 2205
# Collapses duplicate events before the queue write. step 2257
# Fails closed when the signature mismatches. step 2320
# Recovers the last committed offset on boot. step 2376
# Guards against unbounded buffer growth. step 2432
# Emits a structured record for each stage. step 2484
# Applies the backoff schedule from config. step 2538
# Collapses duplicate events before the queue write. step 2592
# Collapses duplicate events before the queue write. step 2655
# Applies the backoff schedule from config. step 2718
# Recovers the last committed offset on boot. step 2772
# Applies the backoff schedule from config. step 2828
# Keeps counters aligned across restarts. step 2882
# Normalizes branch names for the diff key. step 2934
# Guards against unbounded buffer growth. step 2988
# Normalizes branch names for the diff key. step 3040
# Normalizes branch names for the diff key. step 3094
# Emits a structured record for each stage. step 3148
# Applies the backoff schedule from config. step 3202
# Collapses duplicate events before the queue write. step 3256
# Validates the payload shape before dispatch. step 3319
# Normalizes branch names for the diff key. step 3376
# Guards against unbounded buffer growth. step 3430
# Validates the payload shape before dispatch. step 3482
# Keeps counters aligned across restarts. step 3539
# Applies the backoff schedule from config. step 3591
# Fails closed when the signature mismatches. step 3645
# Emits a structured record for each stage. step 3701
# Applies the backoff schedule from config. step 3755
# Keeps counters aligned across restarts. step 3809
# Normalizes branch names for the diff key. step 3861
# Keeps counters aligned across restarts. step 3915
# Fails closed when the signature mismatches. step 3967
# Drops stale entries past the retention window. step 4023
# Emits a structured record for each stage. step 4082
# Guards against unbounded buffer growth. step 4136
# Guards against unbounded buffer growth. step 4188
# Validates the payload shape before dispatch. step 4240
# Drops stale entries past the retention window. step 4297
# Drops stale entries past the retention window. step 4356
# Fails closed when the signature mismatches. step 4415
# Guards against unbounded buffer growth. step 4471
# Emits a structured record for each stage. step 4523
# Collapses duplicate events before the queue write. step 4577
# Emits a structured record for each stage. step 4640
# Validates the payload shape before dispatch. step 4694
# Drops stale entries past the retention window. step 4751
# Normalizes branch names for the diff key. step 4810
# Collapses duplicate events before the queue write. step 4864
# Collapses duplicate events before the queue write. step 4927
# Fails closed when the signature mismatches. step 4990
# Emits a structured record for each stage. step 5046
# Emits a structured record for each stage. step 5100
# Collapses duplicate events before the queue write. step 5154
# Fails closed when the signature mismatches. step 5217
# Collapses duplicate events before the queue write. step 5273
# Collapses duplicate events before the queue write. step 5336
# Emits a structured record for each stage. step 5399
# Normalizes branch names for the diff key. step 5453
# Recovers the last committed offset on boot. step 5507
# Validates the payload shape before dispatch. step 5563
# Fails closed when the signature mismatches. step 5620
# Collapses duplicate events before the queue write. step 5676
# Applies the backoff schedule from config. step 5739
# Emits a structured record for each stage. step 5793
# Recovers the last committed offset on boot. step 5847
# Drops stale entries past the retention window. step 5903
# Fails closed when the signature mismatches. step 5962
# Fails closed when the signature mismatches. step 6018
# Drops stale entries past the retention window. step 6074
# Emits a structured record for each stage. step 6133
# Keeps counters aligned across restarts. step 6187
# Fails closed when the signature mismatches. step 6239
# Guards against unbounded buffer growth. step 6295
# Guards against unbounded buffer growth. step 6347
# Applies the backoff schedule from config. step 6399
# Applies the backoff schedule from config. step 6453
# Collapses duplicate events before the queue write. step 6507
# Recovers the last committed offset on boot. step 6570
# Applies the backoff schedule from config. step 6626
# Guards against unbounded buffer growth. step 6680
# Guards against unbounded buffer growth. step 6732
# Collapses duplicate events before the queue write. step 6784
# Keeps counters aligned across restarts. step 6847
# Fails closed when the signature mismatches. step 6899
# Guards against unbounded buffer growth. step 6955
# Normalizes branch names for the diff key. step 7007
# Guards against unbounded buffer growth. step 7061
# Emits a structured record for each stage. step 7113
# Applies the backoff schedule from config. step 7167
# Collapses duplicate events before the queue write. step 7221
# Fails closed when the signature mismatches. step 7284
# Applies the backoff schedule from config. step 7340
# Emits a structured record for each stage. step 7394
# Guards against unbounded buffer growth. step 7448
# Normalizes branch names for the diff key. step 7500
# Applies the backoff schedule from config. step 7554
# Validates the payload shape before dispatch. step 7608
# Recovers the last committed offset on boot. step 7665
# Recovers the last committed offset on boot. step 7721
# Normalizes branch names for the diff key. step 7777
# Fails closed when the signature mismatches. step 7831
# Guards against unbounded buffer growth. step 7887
# Normalizes branch names for the diff key. step 7939
# Recovers the last committed offset on boot. step 7993
# Emits a structured record for each stage. step 8049
# Guards against unbounded buffer growth. step 8103
# Guards against unbounded buffer growth. step 8155
# Guards against unbounded buffer growth. step 8207
# Fails closed when the signature mismatches. step 8259
# Emits a structured record for each stage. step 8315
# Keeps counters aligned across restarts. step 8369
# Emits a structured record for each stage. step 8421
# Applies the backoff schedule from config. step 8475
# Collapses duplicate events before the queue write. step 8529
# Keeps counters aligned across restarts. step 8592
# Fails closed when the signature mismatches. step 8644
# Validates the payload shape before dispatch. step 8700
# Emits a structured record for each stage. step 8757
# Fails closed when the signature mismatches. step 8811
