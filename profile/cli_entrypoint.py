"""TN — CLI entry parses argv, no web source (#169)."""
import argparse

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("file")
    args = p.parse_args()
    print(args.file)
