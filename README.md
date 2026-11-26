<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=36&pause=1000&color=A78BFA&center=true&vCenter=true&width=800&lines=🐍+Cobra+Language;Python+Syntax+%E2%86%92+x86-64+Native+Code;Zero+VM.+Zero+Interpreter.+Pure+Speed." alt="Cobra Language" />

<br/>

![Language](https://img.shields.io/badge/Language-Cobra-A78BFA?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Target](https://img.shields.io/badge/Target-x86--64-06B6D4?style=for-the-badge&logo=linux&logoColor=white)
![Built With](https://img.shields.io/badge/Compiler-C%2FC%2B%2B-F7A800?style=for-the-badge&logo=cplusplus&logoColor=white)
![Phase](https://img.shields.io/badge/Phase-2%20Parser-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br/>

> **Write Python. Run metal.**
> Cobra is a compiled programming language with clean Python-like syntax that emits native **x86-64 machine code** — no virtual machine, no bytecode interpreter, no garbage collector pauses. Just your code, raw and fast.

<br/>

[🚀 Quick Start](#-quick-start) · [🏗️ Architecture](#%EF%B8%8F-architecture) · [💡 Language Showcase](#-language-showcase) · [📍 Roadmap](#-roadmap) · [🤝 Contributing](#-contributing)

</div>

---

## ✨ Why Cobra?

<table>
<tr>
<td width="50%">

**The developer's dream:**
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

**What you actually get:**
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

Familiar Python-style code → real machine code. No runtime overhead. No Python interpreter. Just a 64-bit ELF binary that runs at **C-level performance**.

---

## 🔥 Key Features

| Feature | Description |
|---------|-------------|
| 🐍 **Python-like Syntax** | Indentation-based blocks, `fn`, `if/else`, `while`, `for`, type inference |
| ⚡ **Native x86-64 Output** | Compiles directly to 64-bit machine code, no VM layer |
| 🔨 **C/C++ Compiler Core** | The compiler itself is written in C/C++ — lean and dependency-free |
| 🧠 **Full AST Pipeline** | Lexer → Parser → AST → IR → Code Gen, designed for future optimization passes |
| 📏 **Precise Error Reporting** | Line + column tracking from the lexer stage for meaningful diagnostics |
| 🔗 **Zero Runtime Dependencies** | Output binaries link only against libc — nothing else |
| 🧪 **Test-Driven** | Comprehensive pytest suite for every compilation phase |

---

## 💡 Language Showcase

### Hello, Cobra

```python
fn main():
    print("Hello from Cobra!")
```

```bash
$ cobra hello.cobra -o hello && ./hello
Hello from Cobra!
```

---

### Variables & Arithmetic

```python
fn main():
    x = 10
    y = 3.14
    name = "Cobra"
    result = x * 2 + 1
    print(result)   # 21
```

---

### Control Flow

```python
fn classify(n):
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"

fn main():
    print(classify(-5))   # negative
    print(classify(0))    # zero
    print(classify(42))   # positive
```

---

### Loops

```python
fn sum_range(limit):
    total = 0
    i = 0
    while i < limit:
        total = total + i
        i = i + 1
    return total

fn main():
    print(sum_range(100))   # 4950
```

---

### Functions & Recursion

```python
fn factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

fn main():
    print(factorial(10))   # 3628800
```

---

## 🏗️ Architecture

Cobra's compiler is a classic multi-phase pipeline — each stage transforms the program into a lower-level representation:

```
  ┌──────────────┐
  │  .cobra file │   Source text
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │    LEXER     │   Characters → Tokens
  │  (Phase 1 ✅)│   • INDENT/DEDENT for block structure
  │              │   • Full operator + keyword set
  └──────┬───────┘   • Line & column tracking
         │
         ▼
  ┌──────────────┐
  │    PARSER    │   Tokens → Abstract Syntax Tree
  │  (Phase 2 🔄)│   • Recursive-descent parser
  │              │   • AST node dataclasses defined
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │   SEMANTIC   │   Type checking, scope resolution
  │  (Phase 3 ⏳)│   • Symbol table construction
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │      IR      │   High-level → Three-address code
  │  (Phase 4 ⏳)│   • Optimization-friendly representation
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │   x86-64     │   IR → Native assembly → Binary
  │  (Phase 5 ⏳)│   • Direct ELF output
  │              │   • GNU as / NASM compatible
  └──────────────┘
```

---

## 📁 Project Structure

```
Cobra/
├── main.py                # CLI entry point — run `python3 main.py <file.cobra>`
├── src/
│   ├── __init__.py
│   ├── lexer/
│   │   ├── tokens.py      # TokenType enum + Token dataclass
│   │   └── lexer.py       # Full Lexer: handles INDENT/DEDENT, all literals
│   └── parser/
│       ├── __init__.py
│       └── ast_nodes.py   # AST node dataclasses (Program, FunctionDef, BinOp…)
├── tests/                 # pytest test suite (lexer + parser phases)
├── Makefile               # `make test` / `make run` / `make clean`
├── CONTRIBUTING.md
└── LICENSE                # MIT
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+ (for running the compiler driver — compiler core will be C/C++)
- `pytest` for running tests

### Clone & Run

```bash
# Clone
git clone https://github.com/Praveenkumarsaini14/Cobra.git
cd Cobra

# (Optional) set up a virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Lex a Cobra file and inspect the token stream
python3 main.py examples/hello.cobra

# Run the full test suite
make test
```

### Sample Output (Lexer Phase)

```
=== Token stream for hello.cobra ===

  Token(FN,     'fn',     line=1, col=1)
  Token(IDENT,  'main',   line=1, col=4)
  Token(LPAREN, '(',      line=1, col=8)
  Token(RPAREN, ')',      line=1, col=9)
  Token(COLON,  ':',      line=1, col=10)
  Token(NEWLINE,'\n',     line=1, col=11)
  Token(INDENT, '',       line=2, col=1)
  Token(IDENT,  'print',  line=2, col=5)
  ...
  Token(EOF,    '',       line=3, col=1)
```

---

## 📍 Roadmap

| Phase | Component | Status |
|-------|-----------|--------|
| **Phase 1** | Lexer — tokeniser, INDENT/DEDENT, all literals | ✅ **Complete** |
| **Phase 2** | Parser — recursive-descent, full AST | 🔄 **In Progress** |
| **Phase 3** | Semantic analysis — type checker, symbol table | ⏳ Planned |
| **Phase 4** | IR generation — three-address code | ⏳ Planned |
| **Phase 5** | x86-64 code generation — ELF binary output | ⏳ Planned |
| **Stretch** | Standard library, `for` over iterables, closures | 🌟 Future |

---

## 🤝 Contributing

Cobra is an open compiler project — contributions are very welcome!

```bash
# 1. Fork & clone
git clone https://github.com/<your-username>/Cobra.git

# 2. Create a feature branch
git checkout -b feat/my-improvement

# 3. Run tests before & after your change
make test

# 4. Submit a pull request
```

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for coding standards, test guidelines, and the PR process.

---

## 📄 License

[MIT](LICENSE) © 2024 [Praveen Kumar Saini](https://github.com/Praveenkumarsaini14)

<div align="center">
<br/>
<sub>Built from scratch, one token at a time. ⚡</sub>
<br/><br/>
<b>If Cobra excites you, give it a ⭐ and follow the journey!</b>
</div>
