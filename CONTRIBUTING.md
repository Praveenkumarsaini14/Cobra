# Contributing to Cobra

Thank you for your interest in contributing to the Cobra programming language!

## Getting Started

1. **Fork** the repository and clone your fork:
   ```bash
   git clone https://github.com/<your-username>/Cobra.git
   cd Cobra
   ```

2. **Create a virtual environment** and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt  # (when added)
   ```

3. **Create a feature branch**:
   ```bash
   git checkout -b feature/my-awesome-feature
   ```

## Project Structure

```
Cobra/
├── main.py               # CLI entry point
├── src/
│   ├── lexer/
│   │   ├── tokens.py     # Token type definitions
│   │   └── lexer.py      # Lexer (tokeniser)
│   └── parser/
│       └── ast_nodes.py  # AST node dataclasses
├── tests/                # Unit tests (pytest)
├── Makefile
└── README.md
```

## Development Workflow

* **Run tests**: `make test` (or `python3 -m pytest tests/ -v`)
* **Lex a file**: `python3 main.py examples/hello.cobra`
* **Clean artefacts**: `make clean`

## Coding Standards

* Follow [PEP 8](https://peps.python.org/pep-0008/).
* Write a docstring for every public class and function.
* Add or update tests for every change.
* Keep lines ≤ 100 characters wide.

## Submitting a Pull Request

1. Push your branch to your fork.
2. Open a pull request against `main` with a clear title and description.
3. Describe **what** you changed and **why**.
4. Ensure all tests pass and there are no linting errors.

## Reporting Issues

Please open a GitHub Issue with:
* A minimal reproducible example (Cobra source code or steps to reproduce).
* The error message / unexpected output.
* Your Python version (`python3 --version`).

## Code of Conduct

Be respectful, constructive, and inclusive. We follow the
[Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct.
