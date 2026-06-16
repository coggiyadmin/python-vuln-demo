# SAST Validation Runbook

Reproducible steps to re-run the entire audit (defects #43–#88, roll-up #89).
Companion docs: `COMBINATION_MATRIX.md`, `CATEGORY_COVERAGE.md`.

---

## 0. Layout / prerequisites
```
~/workspace/cogniumhq/cognium-dev      # the engine (circle-ir + cli)
~/workspace/coggiyadmin/<lang>-vuln-demo  # test corpus (8 langs + go)
```
Need: `node >=20`, `bun`, `jq`, `gh` (authenticated).

## 1. Build the engine (REQUIRED before scanning)
```bash
cd ~/workspace/cogniumhq/cognium-dev
npm install
npm run build
# WASM grammars are NOT copied by `tsc` — this step is mandatory or every scan
# fails with "ENOENT ... dist/wasm/web-tree-sitter.wasm":
( cd packages/circle-ir && npm run build:browser )
```

## 2. The scan invocation (and its gotchas — these cost real time)
```bash
C=~/workspace/cogniumhq/cognium-dev/packages/cli/dist/cli.js   # path ONLY
scan() {  # usage: scan <file-or-dir> [extra cli flags]
  bun "$C" scan "$1" -f json "${@:2}" 1>/tmp/scan.json 2>/dev/null
  tail -n +2 /tmp/scan.json   # strip the leading spinner line, then pipe to jq
}
findings() { scan "$1" "${@:2}" | jq -r '.results[].vulnerabilities[]|select(.category=="security")|"\(.type)@\(.line)"' 2>/dev/null | sort -u; }
```
**Gotchas:**
- ❌ Don't put `bun <path>` in one quoted var (`"$CLI scan"`) — the shell treats it as a single command. Use `bun "$C"`.
- ✅ Redirect **stdout only** to the JSON file; always `tail -n +2` (spinner is line 1).
- **Cross-file taint (#74):** scan the **directory**, not the file (`scan path/to/dir`).
- **JS taint, to avoid confounds:** use `express()` app **not** `express.Router()` (#75); **omit** `module.exports = app` (#77 zeroes the file); bind sources to a **local var**, not inline (#83).
- **Test-file exclusion (#10/#85):** add `--exclude-tests` and compare.

## 3. Fast full-corpus sweep (sanity)
```bash
B=~/workspace/coggiyadmin
for r in bash html htmljs java javascript typescript python rust go; do
  d="$B/$r-vuln-demo"; [ -d "$d" ] || continue
  echo "== $r =="; findings "$d"
done
```
Expect: the intentional vulns fire (SQLi/cmdi/XSS/path/SSRF/secrets…). Note: scanning a whole dir can hit file-instability (#77) — for clean per-cell results use the tiny fixtures below.

## 4. Regression gates (these define pass/fail)
| Gate | Command | PASS = |
|------|---------|--------|
| **Benign TN** (specificity) | `findings $B/<lang>-vuln-demo/benign*.*` | **0** security findings (all langs) |
| **Safe/FP corpus** | scan `Safe*.java`, `safe_*.{py,js,ts,go}`, `fp_corpus.*`, `FalsePositiveCorpus.java`, `py_research_fp.py`, `sanitizer_combos.py` | **0** once #48–#60/#79 land (today: the listed FPs fire) |
| **Vuln TP** | scan the per-class vuln files | all intended findings fire |
| **Score** | OWASP Benchmark (`coggiyadmin/BenchmarkJava`) | Youden = TPR−FPR; track per language |

## 5. Defect verification table
For each, run the command and compare to **Expected today** (the bug). The defect is **FIXED** when the result flips.

| # | Fixture | Command | Expected today |
|---|---------|---------|----------------|
| #74 | `python-vuln-demo/xfile/` | `findings $B/python-vuln-demo/xfile` | MISS (no sqli/cmdi) |
| #83 | inline source | `findings` on `exec("..."+req.getParameter())` (Java), `eval(req.query.x)` (JS) | MISS (var-first fires) |
| #78 | `*/oop_flow.*`, `OopFlow.java`, `gocells`… | scan | MISS (OOP field flow) |
| #77 | `javascript-vuln-demo/async_taint.js` | `findings …/async_taint.js` | 0/4 (instability); remove `module.exports` → fires |
| #75 | router vs app | Router handler `req.*`→sink | MISS for Router, fires for `app` |
| #67 | `typescript-vuln-demo/src/ts_combos.ts` | scan (watch for `[WARN] Partial parse`) | partial-parse, 0 findings |
| #82 | `rust-vuln-demo/src/combos.rs`, `gocells`… | scan | 0 (Rust taint dead) |
| #88 | `polyglot.jsx` / `polyglot.tsx` / `polyglot_tmpl.go` | `scan …; scan …` (check `.results|length` for .jsx) | .jsx = 0 files; .tsx partial-parse; Go text/template MISS |
| #60 | `tierb_cookie_hash.py`, `Cook.java`, `CryptoService.java`, `CryptoConfig.java`, `tls_and_crypto.py` | findings | MISS (weak-crypto/cookie/TLS) |
| #65 | `python-vuln-demo/py_research_fp.py` | findings (handler `/p2`) | psycopg2 `%s` flagged as xss |
| #57/#55/#56 | `FalsePositiveCorpus.java`, `fp_corpus.py` | findings | FPs fire (type-cast/dead-code/allowlist) |
| #86 | `python-vuln-demo/category_gaps.py` | findings | most MISS (CSRF/CRLF/mass-assign/ReDoS/upload/info-disc/format/JWT/XML) |
| #87 | `java-vuln-demo/.../CryptoConfig.java` | findings | MISS (ECB/IV/key/RSA) |
| #84 | `java …/cells/C3v.java` vs `C3i.java` | findings | for-each MISS, index fires |
| #85 | `go-vuln-demo/gocells/c10/inj_test.go` | `findings …; findings … --exclude-tests` | both fire (flag doesn't suppress) |
| #59 | `python-vuln-demo/boundary_*.py` | findings | minified/unicode MISS |

(Full list + per-language cells in `COMBINATION_MATRIX.md`; categories in `CATEGORY_COVERAGE.md`.)

## 6. Tier-B (rules that should FIRE — confirm not regressed)
```bash
findings $B/html-vuln-demo/tierb_html.html      # 5 html-* passes fire
findings $B/javascript-vuln-demo/tierb_cors.js  # cors-null/http/xfo-mismatch/allow-from fire
```

## 7. Combination matrix re-run (per-cell, confound-free)
```bash
# tiny var-pattern fixtures (one combo per file) avoid #77/#83
for f in $B/javascript-vuln-demo/cells/*.js; do echo "$f"; findings "$f"; done
for f in $B/java-vuln-demo/src/main/java/com/demo/cells/*.java; do echo "$f"; findings "$f"; done
```

## 8. After an engine change — diff vs baseline
1. Rebuild engine (§1). 2. Re-run §4 gates + §5 table. 3. Any FP gate that drops to 0, or FN fixture that now fires → update the matrix cell ❌→✅ and close the issue. 4. Re-score OWASP Benchmark; record Youden delta in #61.
