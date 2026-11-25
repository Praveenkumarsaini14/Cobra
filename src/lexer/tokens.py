"""
tokens.py — Token definitions for the Cobra language lexer.

Cobra is a Python-syntax language that compiles to x86-64 assembly.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Any


class TokenType(Enum):
    # ── Literals ──────────────────────────────────────────────────────────
    INT       = auto()   # integer literal  e.g. 42
    FLOAT     = auto()   # float literal    e.g. 3.14
    BOOL      = auto()   # boolean literal  true / false
    STR       = auto()   # string literal   e.g. "hello"

    # ── Identifiers & keywords ───────────────────────────────────────────
    IDENT     = auto()   # identifier       e.g. foo, bar

    # Keywords
    IF        = auto()
    ELSE      = auto()
    WHILE     = auto()
    FOR       = auto()
    FN        = auto()
    RETURN    = auto()
    TRUE      = auto()
    FALSE     = auto()
    AND       = auto()
    OR        = auto()
    NOT       = auto()

    # ── Arithmetic operators ──────────────────────────────────────────────
    PLUS      = auto()   # +
    MINUS     = auto()   # -
    STAR      = auto()   # *
    SLASH     = auto()   # /

    # ── Comparison / assignment operators ─────────────────────────────────
    ASSIGN    = auto()   # =
    EQ        = auto()   # ==
    NEQ       = auto()   # !=
    LT        = auto()   # <
    GT        = auto()   # >
    LTE       = auto()   # <=
    GTE       = auto()   # >=

    # ── Delimiters ────────────────────────────────────────────────────────
    LPAREN    = auto()   # (
    RPAREN    = auto()   # )
    LBRACKET  = auto()   # [
    RBRACKET  = auto()   # ]
    COLON     = auto()   # :
    COMMA     = auto()   # ,
    ARROW     = auto()   # ->
    DOT       = auto()   # .

    # ── Indentation (Python-style) ────────────────────────────────────────
    INDENT    = auto()   # Increase in indentation level
    DEDENT    = auto()   # Decrease in indentation level
    NEWLINE   = auto()   # Logical end-of-line

    # ── Special ───────────────────────────────────────────────────────────
    EOF       = auto()   # End of file


# Maps keyword strings to their token types
KEYWORDS: dict[str, TokenType] = {
    "if":     TokenType.IF,
    "else":   TokenType.ELSE,
    "while":  TokenType.WHILE,
    "for":    TokenType.FOR,
    "fn":     TokenType.FN,
    "return": TokenType.RETURN,
    "true":   TokenType.TRUE,
    "false":  TokenType.FALSE,
    "and":    TokenType.AND,
    "or":     TokenType.OR,
    "not":    TokenType.NOT,
}


@dataclass
class Token:
    """A single lexical token produced by the Cobra lexer."""

    type:   TokenType
    value:  Any        # The literal / string value of the token
    line:   int        # 1-based source line
    column: int        # 1-based source column

    def __repr__(self) -> str:
        return f"Token({self.type.name}, {self.value!r}, line={self.line}, col={self.column})"
