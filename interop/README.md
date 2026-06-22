# interop/ — in-language polyglot (Python)

In-language cross-language fixtures (host=Python embeds a guest DSL). Cross-binary cases
(process/FFI/service) live in `coggiyadmin/interop-vuln-demo`. Plan:
`cogniumhq/sast-validation/research/cross-language-interop-plan.md` (IL-1, IL-5).

Each ships TP + `safe_*` + `benign_*`.

| Fixture | Boundary | CWE | Expected |
|---------|----------|-----|----------|
| `interop_jinja_ssti.py` | Python → Jinja2 `render_template_string(user)` | 1336 | FN |
| `interop_jinja_autoescape_off.py` | Python → Jinja `{{ user\|safe }}` | 79 | FN |
| `interop_sql_in_string.py` | Python → SQL DSL in string → execute | 89 | partial |
| `interop_shell_in_string.py` | Python → shell snippet → `sh -c` | 78 | partial |
| `interop_yaml_gadget.py` | untrusted YAML → `yaml.load` object instantiation | 502 | partial |
| `interop_env_to_eval.py` | `os.environ` → `eval`/dynamic import | 94 | FN |
| `interop_toml_dynimport.py` | TOML value → `importlib.import_module` | 470 | FN |
