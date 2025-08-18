# Template Tests

This directory contains comprehensive tests for the cookiecutter template to ensure it generates valid Python packages with all option combinations.

## Test Structure

- `conftest.py` - Pytest fixtures and test configuration
- `test_template_generation.py` - Main test suite with different option combinations
- `requirements.txt` - Test dependencies (pytest, cookiecutter)

## Test Coverage

The test suite validates:

### ✅ Template Generation Options
- **Default generation** - All features enabled
- **Minimal generation** - No optional features
- **Docs only** - Documentation features only
- **Docker only** - Docker files only  
- **GitHub Actions only** - CI workflow only
- **Publishing + GitHub Actions** - Publishing workflow

### ✅ Generated Project Validation
- Core files exist (pyproject.toml, README.md, src/, tests/)
- Optional files present/absent based on choices
- Python syntax is valid in all generated files
- Imports are absolute (not relative)
- Typer is used instead of Click
- Entry points are correctly configured

### ✅ Content Verification
- pyproject.toml has correct dependencies
- CLI uses Typer framework
- All imports are absolute
- License files have correct content
- Documentation structure is correct

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

## Test Philosophy

These tests ensure:
1. **Template reliability** - Every option combination works
2. **Generated code quality** - Valid Python syntax and imports
3. **Feature consistency** - Optional features work as expected
4. **Regression prevention** - Changes don't break existing functionality

The test suite provides confidence that the template generates working Python packages ready for development.
