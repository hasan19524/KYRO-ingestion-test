# lag monitor

Drops stale entries past the retention window.

## Notes

- Validates the payload shape before dispatch.
- Recovers the last committed offset on boot.
- Guards against unbounded buffer growth.
- Emits a structured record for each stage.
- Collapses duplicate events before the queue write.

Fails closed when the signature mismatches. (305)

Fails closed when the signature mismatches. (356)

Fails closed when the signature mismatches. (407)

Emits a structured record for each stage. (458)

Emits a structured record for each stage. (507)

Applies the backoff schedule from config. (556)

Guards against unbounded buffer growth. (605)

Collapses duplicate events before the queue write. (652)

Validates the payload shape before dispatch. (710)

Normalizes branch names for the diff key. (762)

Keeps counters aligned across restarts. (811)

Emits a structured record for each stage. (858)

Drops stale entries past the retention window. (907)

Keeps counters aligned across restarts. (961)

Fails closed when the signature mismatches. (1008)

Keeps counters aligned across restarts. (1060)

Guards against unbounded buffer growth. (1108)

Keeps counters aligned across restarts. (1156)

Applies the backoff schedule from config. (1204)

Recovers the last committed offset on boot. (1254)

Drops stale entries past the retention window. (1306)

Keeps counters aligned across restarts. (1361)

Keeps counters aligned across restarts. (1409)

Drops stale entries past the retention window. (1457)

Applies the backoff schedule from config. (1512)

Guards against unbounded buffer growth. (1562)

Fails closed when the signature mismatches. (1610)

Guards against unbounded buffer growth. (1662)

Emits a structured record for each stage. (1710)

Recovers the last committed offset on boot. (1760)

Validates the payload shape before dispatch. (1812)

Validates the payload shape before dispatch. (1865)

Keeps counters aligned across restarts. (1918)

Guards against unbounded buffer growth. (1966)

Applies the backoff schedule from config. (2014)

Normalizes branch names for the diff key. (2064)

Guards against unbounded buffer growth. (2114)

Collapses duplicate events before the queue write. (2162)

Validates the payload shape before dispatch. (2221)

Collapses duplicate events before the queue write. (2274)

Drops stale entries past the retention window. (2333)

Keeps counters aligned across restarts. (2388)

Emits a structured record for each stage. (2436)

Validates the payload shape before dispatch. (2486)

Drops stale entries past the retention window. (2539)

Emits a structured record for each stage. (2594)
