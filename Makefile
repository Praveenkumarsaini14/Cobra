.PHONY: test run clean

# Run all unit tests
test:
	python3 -m pytest tests/ -v

# Lex a sample Cobra file (override with FILE=path/to/file.cobra)
run:
	python3 main.py $(FILE)

# Remove compiled Python artifacts
clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
