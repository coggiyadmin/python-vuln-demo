"""FP-target (N4 real dep #167) — argparse spec construction, not shell."""
import argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="demo")
    p.add_argument("file")
    return p
