{% if cookiecutter.include_docs == "y" -%}
# API Reference

This page contains the API documentation for {{ cookiecutter.project_name }}.

## CLI Module

::: {{ cookiecutter.package_name }}.cli

## Alpaca Art Module

::: {{ cookiecutter.package_name }}.alpacas

## Formatter Module

::: {{ cookiecutter.package_name }}.formatter
{%- endif %}
