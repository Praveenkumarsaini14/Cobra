"""
lexer.py — Lexer (tokeniser) for the Cobra programming language.

Features
--------
* Python-style indentation tracking → INDENT / DEDENT tokens
* String literals (single- and double-quoted, with escape sequences)
* Integer and floating-point number literals
* Identifier / keyword recognition
* All Cobra operators and delimiters
* Line comments starting with #
* Accurate line and column tracking for error messages
"""

from __future__ import annotations

from typing import List
from .tokens import Token, TokenType, KEYWORDS


class LexError(Exception):
    """Raised when the lexer encounters an unrecognised character."""

    def __init__(self, message: str, line: int, column: int) -> None:
        super().__init__(f"LexError at line {line}, col {column}: {message}")
        self.line   = line
        self.column = column


class Lexer:
    """
    Tokenises a Cobra source string into a flat list of Token objects.

    Usage
    -----
    ::

        from src.lexer import Lexer

        lexer  = Lexer(source_code)
        tokens = lexer.tokenize()
    """

    def __init__(self, source: str) -> None:
        self._source:  str   = source
        self._pos:     int   = 0       # current character index
        self._line:    int   = 1       # current 1-based line number
        self._col:     int   = 1       # current 1-based column number
        self._tokens:  List[Token] = []

        # Indentation stack — always starts at column 0
        self._indent_stack: List[int] = [0]

        # Whether we are at the logical beginning of a new line
        # (used to decide when to emit INDENT/DEDENT)
        self._at_line_start: bool = True

    # ─────────────────────────────── public API ───────────────────────────────

    def tokenize(self) -> List[Token]:
        """
        Return the complete token stream for the source text.

        The stream is always terminated with a NEWLINE (if the last line
        did not already end with one) followed by any pending DEDENTs and
        a final EOF token.
        """
        while not self._at_end():
            self._scan_token()

        # Emit a trailing NEWLINE so the parser always sees a clean end
        self._emit(TokenType.NEWLINE, "\n")

        # Close all open indentation blocks
        while len(self._indent_stack) > 1:
            self._indent_stack.pop()
            self._emit(TokenType.DEDENT, "")

        self._emit(TokenType.EOF, "")
        return self._tokens

    # ─────────────────────────────── scanning ────────────────────────────────

    def _scan_token(self) -> None:
        """Scan and emit the next token (or update internal state)."""

        # ── Handle indentation at the start of a logical line ──────────────
        if self._at_line_start:
            self._at_line_start = False
            self._handle_indentation()
            # After processing indentation, re-check for end or comment
            if self._at_end():
                return

        ch = self._advance()

        # ── Whitespace (intra-line) ────────────────────────────────────────
        if ch in (" ", "\t", "\r"):
            return  # skip; indentation already handled above

        # ── Newline ────────────────────────────────────────────────────────
        if ch == "\n":
            # Only emit NEWLINE if there is actual content on this line
            if self._tokens and self._tokens[-1].type not in (
                TokenType.NEWLINE, TokenType.INDENT, TokenType.DEDENT
            ):
                self._emit(TokenType.NEWLINE, "\n")
            self._at_line_start = True
            return

        # ── Comment ───────────────────────────────────────────────────────
        if ch == "#":
            self._skip_line_comment()
            return

        # ── String literals ───────────────────────────────────────────────
        if ch in ('"', "'"):
            self._read_string(ch)
            return

        # ── Numbers ───────────────────────────────────────────────────────
        if ch.isdigit():
            self._read_number(ch)
            return

        # ── Identifiers / keywords ────────────────────────────────────────
        if ch.isalpha() or ch == "_":
            self._read_identifier(ch)
            return

        # ── Two-character operators (must check before single-char) ────────
        nxt = self._peek()

        if ch == "=" and nxt == "=":
            self._advance(); self._emit(TokenType.EQ,     "=="); return
        if ch == "!" and nxt == "=":
            self._advance(); self._emit(TokenType.NEQ,    "!="); return
        if ch == "<" and nxt == "=":
            self._advance(); self._emit(TokenType.LTE,    "<="); return
        if ch == ">" and nxt == "=":
            self._advance(); self._emit(TokenType.GTE,    ">="); return
        if ch == "-" and nxt == ">":
            self._advance(); self._emit(TokenType.ARROW,  "->"); return

        # ── Single-character tokens ────────────────────────────────────────
        SINGLE: dict[str, TokenType] = {
            "+": TokenType.PLUS,
            "-": TokenType.MINUS,
            "*": TokenType.STAR,
            "/": TokenType.SLASH,
            "=": TokenType.ASSIGN,
            "<": TokenType.LT,
            ">": TokenType.GT,
            "(": TokenType.LPAREN,
            ")": TokenType.RPAREN,
            "[": TokenType.LBRACKET,
            "]": TokenType.RBRACKET,
            ":": TokenType.COLON,
            ",": TokenType.COMMA,
            ".": TokenType.DOT,
        }
        if ch in SINGLE:
            self._emit(SINGLE[ch], ch)
            return

        raise LexError(f"Unexpected character {ch!r}", self._line, self._col - 1)

    # ─────────────────────── indentation handling ────────────────────────────

    def _handle_indentation(self) -> None:
        """
        Measure the indentation of the current line and emit INDENT / DEDENT
        tokens as needed to reflect changes in nesting level.

        Blank lines and comment-only lines are skipped entirely.
        """
        indent_start = self._pos
        spaces = 0

        # Count leading spaces / tabs (tabs = 8 spaces, same as CPython)
        while not self._at_end() and self._source[self._pos] in (" ", "\t"):
            if self._source[self._pos] == "\t":
                spaces += 8 - (spaces % 8)
            else:
                spaces += 1
            self._pos += 1
            self._col += 1

        # If this line is blank or comment-only, skip without emitting tokens
        if self._at_end():
            return
        ch = self._source[self._pos]
        if ch == "\n":
            return  # blank line — _scan_token will handle the \n
        if ch == "#":
            return  # comment line — _scan_token will handle the #

        current_indent = self._indent_stack[-1]

        if spaces > current_indent:
            self._indent_stack.append(spaces)
            self._emit(TokenType.INDENT, "")
        elif spaces < current_indent:
            while self._indent_stack[-1] > spaces:
                self._indent_stack.pop()
                self._emit(TokenType.DEDENT, "")
            if self._indent_stack[-1] != spaces:
                raise LexError(
                    "Inconsistent indentation", self._line, self._col
                )
        # else: same level — no token needed

    # ─────────────────────────── literal readers ─────────────────────────────

    def _read_string(self, quote: str) -> None:
        """Read a single- or double-quoted string literal."""
        start_line = self._line
        start_col  = self._col - 1   # col of the opening quote
        buf: list[str] = []

        while not self._at_end():
            ch = self._advance()
            if ch == quote:
                # Closing quote found
                self._emit_at(TokenType.STR, "".join(buf), start_line, start_col)
                return
            if ch == "\n":
                raise LexError("Unterminated string literal", start_line, start_col)
            if ch == "\\":
                # Escape sequence
                esc = self._advance()
                ESCAPES = {"n": "\n", "t": "\t", "r": "\r",
                           "\\":"\\"  , "\'": "\'", '"': '"'}
                buf.append(ESCAPES.get(esc, "\\" + esc))
            else:
                buf.append(ch)

        raise LexError("Unterminated string literal", start_line, start_col)

    def _read_number(self, first: str) -> None:
        """Read an integer or floating-point literal."""
        start_line = self._line
        start_col  = self._col - 1
        buf = [first]
        is_float = False

        while not self._at_end() and self._source[self._pos].isdigit():
            buf.append(self._advance())

        # Check for decimal point (must be followed by a digit)
        if (not self._at_end()
                and self._source[self._pos] == "."
                and self._pos + 1 < len(self._source)
                and self._source[self._pos + 1].isdigit()):
            is_float = True
            buf.append(self._advance())  # consume "."
            while not self._at_end() and self._source[self._pos].isdigit():
                buf.append(self._advance())

        text = "".join(buf)
        if is_float:
            self._emit_at(TokenType.FLOAT, float(text), start_line, start_col)
        else:
            self._emit_at(TokenType.INT, int(text), start_line, start_col)

    def _read_identifier(self, first: str) -> None:
        """Read an identifier or keyword."""
        start_line = self._line
        start_col  = self._col - 1
        buf = [first]

        while not self._at_end() and (
            self._source[self._pos].isalnum() or self._source[self._pos] == "_"
        ):
            buf.append(self._advance())

        text = "".join(buf)
        ttype = KEYWORDS.get(text, TokenType.IDENT)

        # Treat true/false as BOOL literals for convenience
        if ttype in (TokenType.TRUE, TokenType.FALSE):
            self._emit_at(TokenType.BOOL, ttype == TokenType.TRUE, start_line, start_col)
        else:
            self._emit_at(ttype, text, start_line, start_col)

    def _skip_line_comment(self) -> None:
        """Skip everything from # to end of line."""
        while not self._at_end() and self._source[self._pos] != "\n":
            self._pos += 1
            self._col += 1

    # ─────────────────────────── helpers ─────────────────────────────────────

    def _at_end(self) -> bool:
        return self._pos >= len(self._source)

    def _advance(self) -> str:
        """Consume and return the current character, updating position."""
        ch = self._source[self._pos]
        self._pos += 1
        if ch == "\n":
            self._line += 1
            self._col = 1
        else:
            self._col += 1
        return ch

    def _peek(self) -> str:
        """Return the next character without consuming it (empty string at EOF)."""
        if self._pos >= len(self._source):
            return ""
        return self._source[self._pos]

    def _emit(self, ttype: TokenType, value) -> None:
        """Append a token using the current line / column."""
        self._tokens.append(Token(ttype, value, self._line, self._col))

    def _emit_at(self, ttype: TokenType, value, line: int, col: int) -> None:
        """Append a token at an explicit source position."""
        self._tokens.append(Token(ttype, value, line, col))
