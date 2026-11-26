<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=36&pause=1000&color=A78BFA&center=true&vCenter=true&width=800&lines=🐍+Cobra+Language;Python+Syntax+%E2%86%92+x86-64+Native+Code;Zero+VM.+Zero+Interpreter.+Pure+Speed." alt="Cobra Language" />

<br/>

![Language](https://img.shields.io/badge/Language-Cobra-A78BFA?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Frontend](https://img.shields.io/badge/Current_Core-Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Target](https://img.shields.io/badge/Target-x86--64_(Planned)-06B6D4?style=for-the-badge&logo=linux&logoColor=white)
![Phase](https://img.shields.io/badge/Phase-1_Complete_%7C_2_In_Progress-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br/>

> **Write Python. Run metal.**
> Cobra is an experimental programming language with clean Python-like syntax designed to compile down to native **x86-64 machine code** — no virtual machine, no bytecode interpreter, no garbage collector pauses.

<br/>

[🚀 Quick Start](#-quick-start) · [🏗️ Architecture](#%EF%B8%8F-architecture) · [💡 Language & Lexer Showcase](#-language--lexer-showcase) · [📍 Roadmap](#-roadmap) · [🤝 Contributing](#-contributing)

</div>

---

## ✨ Vision: Why Cobra?

<table>
<tr>
<td width="50%">

**Cobra Source Syntax (Target):**
```python
fn fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fn main():
    result = fibonacci(40)
    print(result)
```

</td>
<td width="50%">

**Target x86-64 Output (Phase 5 Goal):**
```asm
fibonacci:
    push rbp
    mov  rbp, rsp
    cmp  rdi, 1
    jle  .base_case
    ; ... recursive calls in native x86-64
    pop  rbp
    ret
```

</td>
</tr>
</table>

> **Current Implementation Status:** Phase 1 (the **Lexer** and CLI tokeniser in Python) is complete and working today. Phase 2 (**AST nodes** in `src/parser/ast_nodes.py` and recursive-descent parser) is in active development, leading toward semantic analysis, IR, and x86-64 code generation (with an eventual C/C++ compiler core).

---

## 🔥 Key Features

| Feature | Status | Description |
|---------|--------|-------------|
| 🐍 **Python-like Indentation** | ✅ Implemented | `Lexer` tracks indentation stack and emits `INDENT` / `DEDENT` tokens |
| 🔤 **Full Tokeniser** | ✅ Implemented | Supports `INT`, `FLOAT`, `BOOL`, `STR`, `IDENT`, keywords (`fn`, `if`, `else`, `while`, `for`, `return`), and operators |
| 📏 **Line & Column Tracking** | ✅ Implemented | Every `Token` records exact `(line, col)` coordinates for clear error diagnostics |
| 🖥️ **CLI Token Stream Inspector** | ✅ Implemented | Run `python3 main.py <file.cobra>` to lex any source file |
| 🌳 **AST Node Definitions** | 🔄 In Progress | Dataclasses defined in `src/parser/ast_nodes.py`; recursive-descent parser next |
| ⚡ **Native x86-64 Backend** | ⏳ Planned | Three-address IR → native 64-bit assembly / ELF binary |

---

## 💡 Language & Lexer Showcase

Given a file `hello.cobra`:

```python
fn greet(name):
    if name == "world":
        return "Hello, world!"
    return "Hello, " + name
```

Run the Cobra CLI (`main.py`) on it:

```bash
python3 main.py hello.cobra
```

**Actual Token Stream Output:**

```text
=== Token stream for hello.cobra ===

  Token(FN, 'fn', line=1, col=1)
  Token(IDENT, 'greet', line=1, col=4)
  Token(LPAREN, '(', line=1, col=9)
  Token(IDENT, 'name', line=1, col=10)
  Token(RPAREN, ')', line=1, col=14)
  Token(COLON, ':', line=1, col=15)
  Token(NEWLINE, '\n', line=1, col=16)
  Token(INDENT, '', line=2, col=1)
  ...
  Token(EOF, '', line=5, col=1)
```

---

## 🏗️ Architecture

Cobra is structured as a classic multi-phase compiler pipeline:

```text
  ┌──────────────┐
  │  .cobra file │   Source text
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │    LEXER     │   Characters → Tokens  (src/lexer/lexer.py)
  │  (Phase 1 ✅)│   • INDENT / DEDENT block tracking
  │              │   • Full literal, keyword & operator set
  └──────┬───────┘   • Line & column error coordinates
         │
         ▼
  ┌──────────────┐
  │    PARSER    │   Tokens → AST  (src/parser/ast_nodes.py)
  │  (Phase 2 🔄)│   • AST dataclasses defined
  │              │   • Recursive-descent parser in progress
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │   SEMANTIC   │   Type checking & scope resolution
  │  (Phase 3 ⏳)│   • Symbol table construction
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │      IR      │   High-level AST → Three-address code
  │  (Phase 4 ⏳)│   • Optimization-friendly intermediate form
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │   x86-64     │   IR → Native assembly → ELF binary
  │  (Phase 5 ⏳)│   • Zero-VM native execution
  └──────────────┘
```

---

## 📁 Project Structure

```text
Cobra/
├── main.py                # CLI entry point (`python3 main.py <file.cobra>`)
├── src/
│   ├── __init__.py
│   ├── lexer/
│   │   ├── __init__.py
│   │   ├── tokens.py      # TokenType enum + Token dataclass
│   │   └── lexer.py       # Full Lexer class (INDENT/DEDENT, literals, comments)
│   └── parser/
│       ├── __init__.py
│       └── ast_nodes.py   # AST node dataclasses (Program, FunctionDef, …)
├── Makefile               # Helper targets (run, clean, test)
├── CONTRIBUTING.md        # Contributor guidelines
└── LICENSE                # MIT License
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+

### Clone & Run

```bash
# Clone the repository
git clone https://github.com/Praveenkumarsaini14/Cobra.git
cd Cobra

# View CLI help & version
python3 main.py --help
python3 main.py --version

# Create a sample Cobra file and lex it
cat << 'EOF' > hello.cobra
fn main():
    return 42
EOF

python3 main.py hello.cobra
```

---

## 📍 Roadmap

| Phase | Component | Status |
|-------|-----------|--------|
| **Phase 1** | Lexer — tokeniser, `INDENT`/`DEDENT`, all literals, CLI | ✅ **Complete** |
| **Phase 2** | Parser — AST dataclasses (`ast_nodes.py`) + recursive-descent parser | 🔄 **In Progress** |
| **Phase 3** | Semantic analysis — type checker & symbol table | ⏳ Planned |
| **Phase 4** | IR generation — three-address code | ⏳ Planned |
| **Phase 5** | x86-64 code generation — native assembly & ELF linking | ⏳ Planned |
| **Future** | Self-hosted / C++ compiler core & standard library | 🌟 Planned |

---

## 🤝 Contributing

Contributions are very welcome — especially for Phase 2 (Parser) and building out the `tests/` suite!

```bash
# 1. Fork & clone
git clone https://github.com/<your-username>/Cobra.git

# 2. Create a feature branch
git checkout -b feat/parser-expressions

# 3. Submit a pull request
```

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for coding standards and the PR process.

---

## 📄 License

[MIT](LICENSE) © 2024 [Praveen Kumar Saini](https://github.com/Praveenkumarsaini14)

<div align="center">
<br/>
<sub>Built from scratch, one token at a time. ⚡</sub>
<br/><br/>
<b>If Cobra excites you, give it a ⭐ and follow the journey!</b>
</div>
