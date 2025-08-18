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

    def test_safer_together_flag(self):
        """Test --safer-together flag."""
        runner = CliRunner()
        result = runner.invoke(app, ["--safer-together"])
        assert result.exit_code == 0
        assert "Safer, Together!" in result.stdout

    def test_alpaca_type_selection(self):
        """Test alpaca type selection."""
        runner = CliRunner()
        result = runner.invoke(app, ["--alpaca", "happy", "Hello!"])
        assert result.exit_code == 0
        assert "Hello!" in result.stdout

    def test_color_option(self):
        """Test color option."""
        runner = CliRunner()
        result = runner.invoke(app, ["--color", "red", "Hello!"])
        assert result.exit_code == 0
        assert "Hello!" in result.stdout

    def test_width_option(self):
        """Test width option."""
        runner = CliRunner()
        result = runner.invoke(app, ["--width", "20", "This is a long message"])
        assert result.exit_code == 0
        assert "This is a long message" in result.stdout

    def test_no_message_error(self):
        """Test error when no message provided."""
        runner = CliRunner()
        result = runner.invoke(app, [])
        assert result.exit_code == 1
        assert "Error: No message provided" in result.stdout

    def test_invalid_alpaca_type(self):
        """Test error with invalid alpaca type."""
        runner = CliRunner()
        result = runner.invoke(app, ["--alpaca", "invalid", "Hello!"])
        assert result.exit_code == 1
        assert "Invalid alpaca type" in result.stdout

    def test_invalid_color(self):
        """Test error with invalid color."""
        runner = CliRunner()
        result = runner.invoke(app, ["--color", "invalid", "Hello!"])
        assert result.exit_code == 1
        assert "Invalid color" in result.stdout

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
