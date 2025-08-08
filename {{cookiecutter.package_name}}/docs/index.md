{% if cookiecutter.include_docs == "y" -%}
# {{ cookiecutter.project_name }} 🦙

{{ cookiecutter.project_description }}

```
 ___________
< Hello! >
 -----------
        /|   /|
       ( :v:  )
        |(_)|
        --m--m--
```

## Quick Start

Install {{ cookiecutter.package_name }}:

```bash
pip install {{ cookiecutter.project_slug }}
```

Display a simple message:

```bash
{{ cookiecutter.cli_name }} "Hello World!"
```

Use different alpaca types and colors:

```bash
{{ cookiecutter.cli_name }} --alpaca happy --color green "I'm happy!"
{{ cookiecutter.cli_name }} --alpaca thinking --color blue "Let me think..."
```

## API Reference

For detailed information about all available functions and classes, see the [API Documentation](api.md).
{%- endif %}
