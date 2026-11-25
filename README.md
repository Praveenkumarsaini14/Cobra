<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=32&pause=1000&color=F7A800&center=true&vCenter=true&width=600&lines=🐍+Cobra+Programming+Language;Python+Syntax+%7C+C+Performance;Build+from+Scratch+in+C%2FC%2B%2B" alt="Cobra" />

<br/>

![Version](https://img.shields.io/badge/version-0.1.0--alpha-F7A800?style=for-the-badge&logo=python&logoColor=white)
![Language](https://img.shields.io/badge/Written_in-C%2FC%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Target](https://img.shields.io/badge/Target-x86--64-6E40C9?style=for-the-badge&logo=linux&logoColor=white)
![Status](https://img.shields.io/badge/Status-In_Development-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A high-performance, Python-syntax programming language compiled to native x86-64 machine code — built entirely from scratch in C/C++.**

[🚀 Roadmap](#-roadmap) · [⚙️ Architecture](#%EF%B8%8F-compiler-architecture) · [📦 Installation](#-installation) · [🤝 Contributing](#-contributing)

</div>

---

## 🎯 What is Cobra?

**Cobra** is a custom systems programming language that combines:
- 🐍 **Python-like syntax** — indentation-based blocks, clean & readable
- ⚡ **C-level performance** — compiles to native x86-64 assembly
- 🔧 **Manual memory control** — no garbage collector, explicit `malloc`/`free`
- 🏗️ **Zero external dependencies** — pure C/C++ implementation

> Think of Cobra as "what if Python was compiled and had C's power under the hood."

---

## ⚙️ Compiler Architecture

```
Source Code (.cobra)
      │
      ▼
  ┌─────────┐
  │  Lexer  │  → Token Stream (INT, FLOAT, IF, IDENT, INDENT, DEDENT...)
  └─────────┘
      │
      ▼
  ┌─────────┐
  │  Parser │  → Abstract Syntax Tree (AST)
  └─────────┘
      │
      ▼
  ┌──────────────────┐
  │ Semantic Analysis│  → Type Checking, Symbol Table, Scoping
  └──────────────────┘
      │
      ▼
  ┌──────────┐
  │ Code Gen │  → x86-64 Assembly
  └──────────┘
      │
      ▼
  ┌──────────────────┐
  │ Assembler+Linker │  → Native ELF/PE Executable
  └──────────────────┘
```

---

## 🗺️ Roadmap

### ✅ Phase 1 — Language Specification
- [x] Python-like indentation-based syntax design
- [x] Static typing with type inference (`x = 5` → `int`)
- [x] Core types: `int`, `float`, `bool`, `ptr`
- [x] Control flow: `if/else`, `while`, `for`, functions
- [x] Formal EBNF grammar definition

### 🔄 Phase 2 — Compiler Architecture (In Progress)
- [ ] Lexer / Tokenizer with INDENT/DEDENT support
- [ ] Recursive Descent Parser → AST
- [ ] Semantic Analysis & Symbol Table

### ⏳ Phase 3 — Code Generation
- [ ] x86-64 Assembly emission
- [ ] Register allocator (stack-based → linear scan)
- [ ] Function prologue/epilogue (System V ABI)
- [ ] Heap allocation via `sys_brk` / `VirtualAlloc`

### ⏳ Phase 4 — Optimizations
- [ ] Constant folding
- [ ] Dead code elimination
- [ ] Peephole optimization (`mov rax,0` → `xor rax,rax`)

### ⏳ Phase 5 — Standard Library
- [ ] `print_int()`, `print_str()` via syscalls
- [ ] Basic heap allocator
- [ ] DWARF debug info

---

## 💻 Sample Cobra Code

```python
# Cobra syntax — Python-like but compiles to native code
fn fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fn main() -> int:
    x: int = 10
    result: int = fibonacci(x)
    print(result)   # → 55
    return 0
```

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Praveenkumarsaini14/Cobra.git
cd Cobra

# Build the compiler (requires GCC/Clang)
make build

# Compile a Cobra file
./cobrac hello.cobra -o hello

# Run!
./hello
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Compiler Host | C / C++ |
| Target Architecture | x86-64 (Linux/Windows) |
| ABI | System V AMD64 |
| Output Format | ELF (Linux) / PE (Windows) |
| Build System | GNU Make |

---

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

```bash
git checkout -b feature/your-feature
git commit -m "feat: add your feature"
git push origin feature/your-feature
# → Open a Pull Request
```

---

## 📄 License

MIT License © 2024 [Praveen Kumar Saini](https://github.com/Praveenkumarsaini14)

<div align="center">
<br/>
⭐ <b>Star this repo if you find it interesting!</b> ⭐
</div>
