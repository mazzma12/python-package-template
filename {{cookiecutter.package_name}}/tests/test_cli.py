"""Tests for CLI functionality."""

from click.testing import CliRunner

from {{ cookiecutter.package_name }}.cli import main


class TestCLI:
    """Test CLI interface."""

    def test_basic_message(self):
        """Test basic message display."""
        runner = CliRunner()
        result = runner.invoke(main, ["Hello World!"])
        assert result.exit_code == 0
        assert "Hello World!" in result.output

    def test_safer_together_flag(self):
        """Test --safer-together flag."""
        runner = CliRunner()
        result = runner.invoke(main, ["--safer-together"])
        assert result.exit_code == 0
        assert "Safer, Together!" in result.output

    def test_alpaca_type_selection(self):
        """Test alpaca type selection."""
        runner = CliRunner()
        result = runner.invoke(main, ["--alpaca", "happy", "Hello!"])
        assert result.exit_code == 0
        assert "Hello!" in result.output

    def test_color_option(self):
        """Test color option."""
        runner = CliRunner()
        result = runner.invoke(main, ["--color", "red", "Hello!"])
        assert result.exit_code == 0
        assert "Hello!" in result.output

    def test_width_option(self):
        """Test width option."""
        runner = CliRunner()
        result = runner.invoke(main, ["--width", "20", "This is a long message"])
        assert result.exit_code == 0
        assert "This is a long message" in result.output

    def test_no_message_error(self):
        """Test error when no message provided."""
        runner = CliRunner()
        result = runner.invoke(main, [])
        assert result.exit_code == 1
        assert "Error: No message provided" in result.output

    def test_invalid_alpaca_type(self):
        """Test error with invalid alpaca type."""
        runner = CliRunner()
        result = runner.invoke(main, ["--alpaca", "invalid", "Hello!"])
        assert result.exit_code == 2  # Click validation error

    def test_help_command(self):
        """Test help command."""
        runner = CliRunner()
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "Display messages with ASCII alpacas" in result.output

    def test_version_command(self):
        """Test version command."""
        runner = CliRunner()
        result = runner.invoke(main, ["--version"])
        assert result.exit_code == 0
