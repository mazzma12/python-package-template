# Template Tests

This directory contains comprehensive tests for the cookiecutter template to ensure it generates valid Python packages with all option combinations.

## Test Structure

- `test_template_generation.py` - Main test suite with different option combinations

## Running Tests

### Locally
```bash
# Run all tests
make test

# Or use pytest directly  
pytest tests/ -v

# Quick template test
make test-template

# Clean up test artifacts
make clean
```

### CI/CD
Tests run automatically on GitHub Actions for:
- Python 3.11 and 3.12
- All push/PR events
- Template generation validation
- Syntax verification

