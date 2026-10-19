# Executed feedback-structure results

A finite identification experiment, not an LLM reproduction. All strategies
receive the same hidden specifications and pay d checks per query.

| Dimensions | Queries | Scalar: predicted / observed | Local: predicted / observed |
|---:|---:|---:|---:|
| 2 | 4 | 0.250000 / 0.2485 | 0.625000 / 0.6250 |
| 2 | 8 | 0.500000 / 0.5080 | 1.000000 / 1.0000 |
| 2 | 16 | 1.000000 / 1.0000 | 1.000000 / 1.0000 |
| 2 | 32 | 1.000000 / 1.0000 | 1.000000 / 1.0000 |
| 2 | 64 | 1.000000 / 1.0000 | 1.000000 / 1.0000 |
| 4 | 4 | 0.015625 / 0.0125 | 0.136719 / 0.1445 |
| 4 | 8 | 0.031250 / 0.0245 | 0.742188 / 0.7270 |
| 4 | 16 | 0.062500 / 0.0595 | 1.000000 / 1.0000 |
| 4 | 32 | 0.125000 / 0.1225 | 1.000000 / 1.0000 |
| 4 | 64 | 0.250000 / 0.2385 | 1.000000 / 1.0000 |
| 8 | 4 | 0.000061 / 0.0005 | 0.002518 / 0.0010 |
| 8 | 8 | 0.000122 / 0.0005 | 0.078049 / 0.0620 |
| 8 | 16 | 0.000244 / 0.0005 | 0.863617 / 0.8450 |
| 8 | 32 | 0.000488 / 0.0005 | 1.000000 / 1.0000 |
| 8 | 64 | 0.000977 / 0.0010 | 1.000000 / 1.0000 |
| 16 | 4 | 0.000000 / 0.0000 | 0.000000 / 0.0000 |
| 16 | 8 | 0.000000 / 0.0000 | 0.000053 / 0.0000 |
| 16 | 16 | 0.000000 / 0.0000 | 0.028128 / 0.0220 |
| 16 | 32 | 0.000000 / 0.0000 | 0.953462 / 0.9595 |
| 16 | 64 | 0.000000 / 0.0000 | 1.000000 / 1.0000 |

Executed 4,635,614 primitive checks across 2,000 specifications per dimension.
No parameters were fitted. Every local trajectory exactly obeyed the predicted
query-count identity; scalar outcomes are finite-sample realizations of its law.

The result establishes a possible exponential-versus-linear query gap when
correct local decisions compose and feedback identifies the failing component.
It does not establish that any LLM trace has this structure. Removing localization
returns the equality-oracle lower bound even though final correctness stays exact.

The exact inheritance witness has a perfect teacher but only 50% optimal student
accuracy when the decisive input bit is removed; restoring it gives 100%.
Global success filtering also changes an equally weighted easy/hard task mixture
to 90%/10% when their success probabilities are 0.9/0.1.

See PROTOCOL.md and summary.json for definitions and reproduction. Full records
are preserved in records.json.gz; decompress it to inspect records.json.
