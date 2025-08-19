# Python Package Template

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for creating modern Python packages with optional features.

## Features

This template provides a solid foundation for Python packages with the following optional features:

- 🐍 **Modern Python tooling** (UV, Ruff, Pyright)
- 📦 **Package structure** with `src/` layout
- 🧪 **Testing** with pytest and coverage
- 📚 **Documentation** with MkDocs Material (optional)
- 🐳 **Docker support** (optional)
- 🚀 **CI/CD** with GitHub Actions (optional)
- 📋 **Pre-commit hooks** (optional)
- 📄 **MIT License** (optional)
- 🏷️ **PyPI publishing** (optional)

## Quick Start

1. Install `cookiecutter`:
   ```bash
   pip install cookiecutter
   ```

2. Generate your project:
   ```bash
   cookiecutter https://github.com/mazzma12/python-package-template
   ```

3. Follow the prompts to configure your project

4. Navigate to your new project and start coding!

## Configuration Options

During project generation, you'll be prompted for the following:

| Option | Description | Choices |
|--------|-------------|---------|
| `project_name` | Display name of your project | String |
| `package_name` | Python package name (importable) | String |
| `project_description` | Short description | String |
| `author_name` | Your name | String |
| `author_email` | Your email | String |
| `github_username` | Your GitHub username | String |
| `version` | Initial version | String (default: 0.1.0) |
| `python_version` | Target Python version | String (default: 3.11) |
| `include_license` | Include license file | MIT, none |
| `include_docs` | Include documentation setup | y, n |
| `include_docker` | Include Docker files | y, n |
| `include_publishing` | Include PyPI publishing workflow | y, n |
| `include_github_actions` | Include GitHub Actions CI/CD | y, n |
| `include_pre_commit` | Include pre-commit hooks | y, n |

## Project Structure

The generated project will have the following structure:

```
your-project/
├── src/
│   └── your_package/
│       ├── __init__.py
│       ├── cli.py              # Main CLI entry point
│       ├── alpacas.py          # Core alpaca functionality
│       └── formatter.py       # Message formatting
├── tests/
│   ├── conftest.py
│   ├── test_cli.py
│   ├── test_alpacas.py
│   └── test_formatter.py
├── docs/                       # (optional)
│   ├── index.md
│   ├── installation.md
│   ├── usage.md
│   ├── examples.md
│   └── api.md
├── .github/                    # (optional)
│   └── workflows/
│       ├── ci.yml
│       └── pypi-publish.yml    # (optional)
├── pyproject.toml              # Project configuration
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
├── .pre-commit-config.yaml     # (optional)
├── mkdocs.yml                  # (optional)
├── Dockerfile                  # (optional)
├── docker-compose.yml          # (optional)
├── .dockerignore               # (optional)
└── LICENSE                     # (optional)
```

## Getting Started with Your New Project

After generating your project:

1. **Initialize Git**:
   ```bash
   cd your-project
   git init
   git add .
   git commit -m "feat: initial project setup"
   ```

2. **Install dependencies**:
   ```bash
   uv sync --dev
   ```

3. **Set up pre-commit** (if included):
   ```bash
   uv run pre-commit install
   ```


## Development Tools Included

- **[UV](https://github.com/astral-sh/uv)**: Fast Python package manager
- **[Ruff](https://github.com/astral-sh/ruff)**: Lightning-fast linter and formatter
- **[Pyright](https://github.com/microsoft/pyright)**: Static type checker
- **[pytest](https://pytest.org/)**: Testing framework
- **[MkDocs Material](https://squidfunk.github.io/mkdocs-material/)**: Documentation generator (optional)
- **[Pre-commit](https://pre-commit.com/)**: Git hooks framework (optional)

## Template Updates

If you need to update your project when the template changes, you can:

1. **Manual update**: Compare your project with a newly generated one and apply changes selectively
2. **Use a diff tool**: Generate a new project and use tools like `diff` or `meld` to compare
3. **Git-based approach**: Create a new branch with a fresh generation and merge changes

Note: Template updates require manual intervention to preserve your customizations.

## Testing the Template

This template includes comprehensive tests to ensure it generates valid projects with all option combinations.

### Running Tests Locally

```bash
# Run all template tests
make test

# Quick template test
make test-template

# Or use pytest directly
pytest tests/ -v

# Clean up test artifacts
make clean
```

### Continuous Integration

The template is automatically tested on GitHub Actions with:
- Template generation validation
- All option combinations testing  
- Generated code syntax verification
- Project structure validation

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This template is licensed under the MIT License.
