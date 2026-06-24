"""FP-target (upstream cognium-dev#162, #140) — CLI profile. A developer tool that evals/imports
a name from argv. Operator-controlled, not a remote sink; project-profile=cli should downgrade."""
import importlib
import sys

if __name__ == "__main__":
    mod = importlib.import_module(sys.argv[1])  # dev-CLI reflection
    print(mod)
