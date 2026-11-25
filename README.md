# 🐍 Cobra

> **A Python-syntax programming language that compiles to x86-64 assembly.**

Cobra lets you write clean, Python-like code that compiles all the way down to
native x86-64 machine code — no virtual machine, no interpreter overhead.

---

## Current Status

| Phase | Component | Status |
|-------|-----------|--------|
| **Phase 1** | Lexer (tokeniser) | ✅ **COMPLETE** |
| **Phase 2** | Parser (AST builder) | 🔄 **In Progress** |
| **Phase 3** | Type checker / Semantic analysis | ⏳ Planned |
| **Phase 4** | IR generation | ⏳ Planned |
| **Phase 5** | x86-64 code generation | ⏳ Planned |

### What works right now (Phase 1 — Lexer)

* ✅ All token types defined (`INT`, `FLOAT`, `BOOL`, `STR`, `IDENT`, operators, delimiters, …)
* ✅ Python-style **indentation tracking** — emits `INDENT` / `DEDENT` tokens correctly
* ✅ String literals (single- and double-quoted, with escape sequences)
* ✅ Integer and floating-point number literals
* ✅ Identifier and keyword recognition (`if`, `else`, `while`, `for`, `fn`, `return`, …)
* ✅ All arithmetic, comparison, and logical operators
* ✅ Line comments starting with `#`
* ✅ Accurate **line & column** tracking for error reporting
* ✅ CLI entry point — lex any `.cobra` file and print the token stream

---

## Example

Given `hello.cobra`:

```python
fn greet(name):
    if name == "world":
        return "Hello, world!"
    return "Hello, " + name
```

Run the lexer:

```bash
python3 main.py hello.cobra
```

Output (token stream):

```
=== Token stream for hello.cobra ===

  Token(FN, 'fn', line=1, col=1)
  Token(IDENT, 'greet', line=1, col=4)
  Token(LPAREN, '(', line=1, col=9)
  ...
  Token(EOF, '', line=5, col=1)
```

---

## Project Structure

```
Cobra/
├── main.py               # CLI entry point
├── src/
│   ├── __init__.py
│   ├── lexer/
│   │   ├── __init__.py
│   │   ├── tokens.py     # TokenType enum + Token dataclass
│   │   └── lexer.py      # Full Lexer class
│   └── parser/
│       ├── __init__.py
│       └── ast_nodes.py  # AST node dataclasses (Program, FunctionDef, …)
├── tests/                # pytest test suite
├── Makefile              # test / run / clean
├── LICENSE               # MIT
└── CONTRIBUTING.md
```

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/Praveenkumarsaini14/Cobra.git
cd Cobra

# (Optional) create a virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Lex a Cobra source file
python3 main.py examples/hello.cobra

# Run tests
make test
```

---

## Roadmap

- [x] **Phase 1** — Lexer
- [ ] **Phase 2** — Parser (recursive-descent, produces AST)
- [ ] **Phase 3** — Type checker & semantic analysis
- [ ] **Phase 4** — Intermediate representation (IR) generation
- [ ] **Phase 5** — x86-64 assembly code generation & linking

---

## Contributing

Contributions are very welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for
guidelines on setting up your environment, coding standards, and submitting
pull requests.

---

## License

[MIT](LICENSE) © 2024 Praveen Kumar Saini
