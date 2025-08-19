# {{ cookiecutter.project_name }} 🦙

{%- if cookiecutter.include_publishing == "y" %}
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg)](https://badge.fury.io/py/{{ cookiecutter.project_slug }}/)
[![Python versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
{%- endif %}
{%- if cookiecutter.include_github_actions == "y" %}
[![Code Quality](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Code%20Quality/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3A"Code+Quality")
{%- if cookiecutter.include_docs == "y" %}
[![Documentation](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Documentation/badge.svg)](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }})
{%- endif %}
{%- endif %}

{{ cookiecutter.project_description }}

```
 ________________
< Safer, Together! >
 ----------------
        /|   /|
       ( :v:  )
        |(_)|
        --m--m--
```

## Features

- 🦙 **Three unique alpaca designs** - default, happy, and thinking
- 🌈 **Color support** - make your alpacas colorful
- 📏 **Customizable width** - control the speech bubble size
- 📁 **File input** - read messages from files
- 🔧 **Pipe support** - works with stdin
- 🛡️ **Special message** - built-in "Safer, Together!" message

## Installation

{%- if cookiecutter.include_publishing == "y" %}

### From PyPI

```bash
pip install {{ cookiecutter.project_slug }}
```
{%- endif %}

{%- if cookiecutter.include_docker == "y" %}

### Using Docker

```bash
# Quick run with Docker
docker run --rm -it ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}:latest "Hello from Docker!"

# Build locally
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm {{ cookiecutter.project_slug }} "Your message here"

# Using docker-compose
docker-compose up {{ cookiecutter.project_slug }}
```
{%- endif %}

### From Source

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
uv sync --dev
uv run {{ cookiecutter.cli_name }} "Hello World!"
```

## Quick Start

```bash
# Basic usage
{{ cookiecutter.cli_name }} "Hello World!"

# Happy alpaca with color
{{ cookiecutter.cli_name }} --alpaca happy --color green "I'm happy!"

# Special CrowdSec message
{{ cookiecutter.cli_name }} --safer-together

# From file
{{ cookiecutter.cli_name }} --file message.txt

# From pipe
echo "Hello from pipe" | {{ cookiecutter.cli_name }}
```

## Usage

```bash
{{ cookiecutter.cli_name }} [OPTIONS] [MESSAGE]

Options:
  -a, --alpaca [default|happy|thinking]  Choose alpaca type
  -c, --color [red|green|blue|yellow|magenta|cyan|white]  Text color
  -w, --width INTEGER                    Maximum width of the speech bubble
  --safer-together                       Display the special "Safer, Together!" message
  -f, --file PATH                        Read message from file
  --version                              Show version and exit
  --help                                 Show this message and exit
```

## Examples

### Basic Examples

```bash
# Default alpaca
{{ cookiecutter.cli_name }} "Hello World!"

# Happy alpaca with green text
{{ cookiecutter.cli_name }} --alpaca happy --color green "Great job!"

# Thinking alpaca with custom width
{{ cookiecutter.cli_name }} --alpaca thinking --width 30 "Let me think about this..."
```

### Integration Examples

**Git hook (.git/hooks/post-commit):**
```bash
#!/bin/bash
{{ cookiecutter.cli_name }} --color cyan "Commit successful! 🎉"
```

**Build script:**
```bash
if npm test; then
    {{ cookiecutter.cli_name }} --alpaca happy --color green "All tests passed!"
else
    {{ cookiecutter.cli_name }} --color red "Tests failed!"
fi
```

**Daily motivation (.bashrc):**
```bash
{{ cookiecutter.cli_name }} --alpaca happy "Have a great day!"
```

## Development

### Prerequisites

- Python {{ cookiecutter.minimum_python_version }}+
- [UV](https://github.com/astral-sh/uv) (recommended) or pip

### Setup

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
uv sync --dev
```

### VS Code Development

This project includes a VS Code task for development setup. To run it:

1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Type "Tasks: Run Task"
3. Select "{{ cookiecutter.project_name }} Development Setup"

This will automatically:
- Install dependencies with `uv sync --dev`
- Format code with `uv run ruff format .`
- Run linting with `uv run ruff check .`
- Execute tests with `uv run pytest -v`
- Build the package with `uv build`
- Test the CLI with `uv run {{ cookiecutter.cli_name }} --safer-together`

### Manual Commands

```bash
# Install dependencies
uv sync --dev

# Run tests
uv run pytest

# Linting and formatting
uv run ruff check .
uv run ruff format .

# Type checking
uv run pyright

# Build package
uv build

# Run locally
uv run {{ cookiecutter.cli_name }} "Test message"
```

{%- if cookiecutter.include_docker == "y" %}

### Docker Development

```bash
# Build development image
docker build -t {{ cookiecutter.project_slug }}:dev .

# Run with volume mount for development
docker run --rm -v $(pwd):/app {{ cookiecutter.project_slug }}:dev "Development test"

# Build production image
docker build -f Dockerfile.production -t {{ cookiecutter.project_slug }}:prod .
```
{%- endif %}

{%- if cookiecutter.include_docs == "y" %}

### Documentation

```bash
# Install docs dependencies
uv sync --group docs

# Serve documentation locally
uv run mkdocs serve

# Build documentation
uv run mkdocs build
```
{%- endif %}

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

{%- if cookiecutter.include_license != "none" %}

## License

This project is licensed under the {{ cookiecutter.include_license }} License - see the LICENSE file for details.
{%- endif %}

## Acknowledgments

- Inspired by the classic `cowsay` utility
- ASCII art created with love for the alpaca community
- Built with modern Python tooling (uv, ruff, pytest{% if cookiecutter.include_docs == "y" %}, mkdocs{% endif %})

## Links

{%- if cookiecutter.include_docs == "y" %}
- [Documentation](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }})
{%- endif %}
{%- if cookiecutter.include_publishing == "y" %}
- [PyPI Package](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
{%- endif %}
- [Source Code](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
- [Issue Tracker](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues)
