# Combination × Language Coverage Matrix

Living documentation of the permutation testing across all 8 supported languages
× 13 flow/sanitizer/specificity/multiplicity combinations. Fixtures live across
the `coggiyadmin/*-vuln-demo` repos (`combos.*`, `combo_*`, `xfile/`,
`path_sensitive.*`, `loop_taint.*`, `async_taint.*`, `oop_flow.*`,
`sanitizer_combos.*`, `fanout.*`, `encoded.*`, `polyglot.html`).

Defects are tracked as GitHub issues on `cogniumhq/cognium-dev`; this file is the
non-defect documentation (passing cells, status, blockers).

## Legend
✅ fires/correct · ❌ FN or FP (defect filed) · ⚠️ blocked by a systemic defect · — n/a · ▫️ not yet tested

## Combinations
1 cross-file taint · 2 path-sensitivity · 3 loop-carried · 4 async/callback · 5 OOP object-flow ·
6 wrong-context sanitizer · 7 fake sanitizer · 8 custom-wrapper sanitizer · 9 comment/string-literal ·
10 test-file exclusion · 11 fan-out/dedup · 12 polyglot · 13 encoded payload

## Matrix

| Lang | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|------|---|---|---|---|---|---|---|---|---|----|----|----|----|
| **Python** | ❌74 | ✅ | ✅76 | ▫️ | ❌78 | ✅ | ✅ | ❌79 | ✅ | ✅ | ✅ | — | ✅ |
| **JavaScript** | ▫️ | ✅ | ▫️ | ✅77 | ▫️ | ▫️ | ▫️ | ▫️ | ▫️ | ▫️ | ▫️ | ▫️ | ▫️ |
| **TypeScript** | ⚠️69 | ⚠️69 | ⚠️69 | ⚠️69 | ⚠️69 | ⚠️69 | ⚠️69 | ⚠️69 | ⚠️69 | ⚠️69 | ⚠️69 | — | ⚠️69 |
| **Java** | ▫️ | ▫️ | ▫️ | ▫️ | ❌78 | ▫️ | ▫️ | ▫️ | ▫️ | ▫️ | ▫️ | — | ▫️ |
| **Rust** | ⚠️82 | ⚠️82 | ⚠️82 | ⚠️82 | ⚠️82 | ⚠️82 | ⚠️82 | ⚠️82 | ✅* | ⚠️82 | ⚠️82 | — | ⚠️82 |
| **Go** | ▫️ | ✅ | ✅ | ▫️ | ❌78 | ▫️ | ✅ | ▫️ | ▫️ | ▫️ | ✅ | — | ▫️ |
| **Bash** | ▫️ | ✅ | ✅ | — | — | ▫️ | ✅ | ▫️ | ✅ | ▫️ | ✅ | — | ▫️ |
| **HTML/htmljs** | — | — | — | — | — | — | — | — | — | — | — | ❌80 | — |

\* Rust #9 (comment/string) is trivially clean only because Rust taint is non-functional (#82) — not a meaningful pass.

## Systemic blockers (whole-row)
- **TypeScript — #69**: typed arrow params / `declare` / inline classes / decorators push files into partial-parse (errorCount ≥ 1), silently suppressing findings. The entire TS row cannot be validated until TS parsing is hardened.
- **Rust — #82**: no source (`env::args`, actix extractors #73) reaches any sink (Command/fs/sql). Only regex-based secret detection works. The entire Rust taint row is blocked.

## Defects found via combination testing
| # | Issue | Summary |
|---|-------|---------|
| 1 | #74 | cross-file taint not tracked (import boundary) |
| 3 | #76 | inline `for x in request.args.getlist(...)` loses taint (Python) |
| 4 | #77 | JS taint unstable — realistic multi-handler files yield 0 findings |
| 5 | #78 | OOP object-flow (ctor→field→getter→sink) FN — Java, Python, **Go** |
| 8 | #79 | custom sanitizer wrapper not recognized (interproc sanitizer) |
| 12 | #80 | JS inside HTML `<script>` not taint-analyzed (polyglot) |
| — | #75 | `express.Router()` handler sources not recognized |
| — | #69 | TS parse fragility (blocks TS row) |
| — | #82 | Rust taint non-functional (blocks Rust row) |

## Correct / clean cells (no defect — engine behaving well)
- Path-sensitivity (#2): Python, JS, Go, Bash — neg-guard, one-branch sanitizer, early-return all fire.
- Loop-carried (#3): Python, Go, Bash — append/accumulator/iterate fire (when source is bound to a var).
- Wrong-context (#6) & fake (#7) sanitizer: correctly fire (not fooled). Confirmed Python, Go, Bash, Rust(n/a).
- Comment/string-literal (#9): clean in Python, Bash, Go, Rust.
- Test-file exclusion (#10): `--exclude-tests` suppresses correctly (Python).
- Fan-out/dedup (#11): one source → N sinks reports all N (Python, Go, Bash).
- Encoded payloads (#13): base64/url/bytes decode preserve taint (Python).

## Remaining ▫️ cells (to fill)
JS: 1,3,5,6–11,13 · Java: 1,2,3,4,6–11,13 · Go: 1,4,6,8,9,10,13 · Bash: 1,6,8,10 · Python: 4 (async).
TS and Rust rows are deferred behind #69 / #82 (testing individual cells is moot until the systemic blocker is fixed).
