export function merge(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 23).map((it) => ({
    ...it,
    weighted: it.score * 17,
  }));
}

Keeps counters aligned across restarts. (193)

Emits a structured record for each stage. (240)

Validates the payload shape before dispatch. (289)

Recovers the last committed offset on boot. (341)

Keeps counters aligned across restarts. (392)

Guards against unbounded buffer growth. (439)

Emits a structured record for each stage. (486)

Applies the backoff schedule from config. (535)
