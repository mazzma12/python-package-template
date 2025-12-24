"""Tests for CLI functionality."""

from typer.testing import CliRunner

from {{ cookiecutter.package_name }}.cli import app


class TestCLI:
    """Test CLI interface."""

    def test_basic_message(self):
        """Test basic message display."""
        runner = CliRunner()
        result = runner.invoke(app, ["Hello World!"])
        assert result.exit_code == 0
        assert "Hello World!" in result.stdout


    def test_help_command(self):
        """Test help command."""
        runner = CliRunner()
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "Display messages with ASCII alpacas" in result.stdout

    def test_version_command(self):
        """Test version command."""
        runner = CliRunner()
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert "{{ cookiecutter.package_name }} version {{ cookiecutter.version }}" in result.stdout
