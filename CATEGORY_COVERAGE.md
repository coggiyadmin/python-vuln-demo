# Vulnerability Category Coverage

Companion to `COMBINATION_MATRIX.md`. Maps every vulnerability category against
the engine's actual detection (finding-type enum + `PASSES.md`). Fixtures:
`category_gaps.py`, `CryptoConfig.java`, plus the per-class vuln-demo files.

Legend: ✅ detected · ⚠️ rule exists but doesn't fire / under-tested · ❌ no rule (gap)

## A. Detected (taint + pattern rules) ✅
| Category | CWE | Rule |
|----------|-----|------|
| SQL injection | 89 | `sql-injection` |
| Command injection | 78 | `command-injection` |
| XSS (reflected/stored/DOM) | 79 | `xss` |
| Path traversal | 22 | `path-traversal` |
| SSRF | 918 | `ssrf` |
| Insecure deserialization | 502 | `deserialization` |
| XXE | 611 | `xxe` |
| LDAP injection | 90 | `ldap-injection` |
| XPath injection | 643 | `xpath-injection` |
| NoSQL injection | 943 | `nosql-injection` |
| Code injection / RCE | 94 | `code-injection` (eval/SpEL/OGNL/JNDI/SSTI) |
| Open redirect | 601 | `open-redirect` |
| Log injection | 117 | `log-injection` |
| Spring4Shell | 94 | `spring4shell` (pattern) |
| Hardcoded secrets | 798 | `hardcoded-credential` (+ entropy) |
| Security headers / CORS | 1021/942/346 | header + cors passes |
| HTML attribute issues | 79/1021/353 | `html-*` passes |
| Trust boundary | 501 | `trust-boundary` |

## B. Tier-B — verified (permutations run)
### B1. Confirmed WORKING ✅ (were just untested)
| Rule | CWE | Result |
|------|-----|--------|
| `html-mixed-content` | 311 | ✅ fires |
| `html-javascript-uri` | 79 | ✅ fires |
| `html-form-action-javascript` | 79 | ✅ fires |
| `html-missing-noopener` | 1022 | ✅ fires |
| `html-missing-sandbox` | 1021 | ✅ fires |
| `cors-null-origin` | 346 | ✅ fires |
| `cors-http-origin` | 346 | ✅ fires |
| `xfo-csp-mismatch` | 1021 | ✅ fires |
| `x-frame-options-allow-from` | 1021 | ✅ fires |
| `external-taint-escape` | 668 | ✅ fires (seen in bash) |

### B2. Confirmed DEAD across ALL languages ❌ → consolidated under #60
Root cause: modeled as **taint sinks** but the vuln is a **constant config / absent flag** → never fires. Should be **pattern passes**.
| Rule | CWE | Java | Python | JS | Go | Rust |
|------|-----|------|--------|----|----|----|
| `weak_hash` / `weak_crypto` / `weak_random` | 327/8/330 | ❌ | ❌ | ❌ | ❌ | ❌ |
| `insecure_cookie` | 614 | ❌ | ❌ | ❌ | — | — |
| TLS verification disabled | 295 | — | ❌ | — | ❌ | — |

## C. No rule — genuine category gaps ❌
### SAST-tractable (defect #86 / #87)
| Category | CWE | Issue |
|----------|-----|-------|
| CSRF | 352 | #86 |
| CRLF / HTTP response splitting | 113 | #86 |
| Mass assignment / over-posting | 915 | #86 |
| ReDoS | 1333 | #86 |
| Unrestricted file upload | 434 | #86 |
| Info disclosure / stack trace to client | 209 | #86 |
| Format string | 134 | #86 |
| JWT verification disabled / weak alg | 347/384 | #86 |
| XML entity expansion (billion laughs) | 776 | #86 |
| Sensitive data in logs (cleartext secret) | 532 | #86 (partial: fires as log-injection) |
| Insecure crypto config: ECB / static IV / hardcoded key / weak RSA | 327/329/321/326 | #87 |

### Out of deterministic-SAST scope → LLM / cognium-ai layer
| Category | CWE | Note |
|----------|-----|------|
| **Broken Access Control / IDOR / missing function-level authz** | 639/862/863 | OWASP **A01** (#1 risk) — authorization logic, needs app context |
| Authentication bypass / hardcoded backdoor | 287 | logic-based (e.g. `if pw=="backdoor"`) |
| Business-logic flaws | — | semantic |

## Summary
- **18 categories detected**, **~8 under-firing/untested**, **~11 SAST-tractable gaps** (#86/#87), **3 LLM-layer categories**.
- Biggest conceptual miss: **OWASP A01 Broken Access Control** — but correctly the LLM layer's job, not deterministic SAST.
- Highest-value SAST additions: CRLF/response-splitting, mass-assignment, ReDoS, format-string, insecure-crypto-config.
