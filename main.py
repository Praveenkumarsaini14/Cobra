#!/usr/bin/env python3
"""
main.py — Cobra language command-line interface.

Usage
-----
    python main.py <file.cobra>          # Lex and print the token stream
    python main.py --help                # Show this help message

The Cobra language is a Python-syntax language that compiles to x86-64 assembly.
Phase 1 (Lexer) is complete; Phase 2 (Parser) is in progress.
"""

import sys
import argparse
from pathlib import Path

from src.lexer import Lexer
from src.lexer.tokens import TokenType


def lex_file(path: Path) -> None:
    """Read a .cobra source file, tokenise it, and print every token."""
    source = path.read_text(encoding="utf-8")
    lexer  = Lexer(source)

    try:
        tokens = lexer.tokenize()
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"=== Token stream for {path.name} ===\n")
    for tok in tokens:
        print(f"  {tok}")
    print(f"\nTotal: {len(tokens)} token(s)")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="cobra",
        description="Cobra language compiler (Phase 1 — Lexer)",
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Path to a .cobra source file to lex",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="cobra 0.1.0-alpha (Phase 1: Lexer)",
    )

    args = parser.parse_args()

    if args.file is None:
        parser.print_help()
        sys.exit(0)

    path = Path(args.file)
    if not path.exists():
        print(f"[ERROR] File not found: {path}", file=sys.stderr)
        sys.exit(1)

    lex_file(path)


if __name__ == "__main__":
    main()
