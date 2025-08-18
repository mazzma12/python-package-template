"""
{{ cookiecutter.project_name }} - {{ cookiecutter.project_description }}

Like cowsay, but with alpacas!
"""
from {{ cookiecutter.package_name }}.alpacas import ALPACAS, AlpacaType
from {{ cookiecutter.package_name }}.cli import app
from {{ cookiecutter.package_name }}.formatter import format_message

__all__ = ["ALPACAS", "AlpacaType", "format_message", "app"]
