"""Tests for CLI functionality."""

from typer.testing import CliRunner

from {{ cookiecutter.package_name }}.cli import app


class TestCLI:
    """Test CLI interface."""

    def test_help_command(self):
        """Test help command."""
        runner = CliRunner()
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "{{ cookiecutter.project_description }}" in result.stdout

    def test_version_command(self):
        """Test version command."""
        runner = CliRunner()
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
