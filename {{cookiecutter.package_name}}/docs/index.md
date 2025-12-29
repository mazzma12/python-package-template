{% if cookiecutter.include_docs == "y" -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Quick Start

Install {{ cookiecutter.package_name }}:

```bash
pip install {{ cookiecutter.project_slug }}
```
{%- endif %}
