"""Tests for message formatting functionality."""

from {{ cookiecutter.package_name }}.formatter import colorize_text, create_speech_bubble, format_message, wrap_text


class TestWrapText:
    """Test text wrapping functionality."""

    def test_wrap_simple_text(self):
        """Test wrapping simple text."""
        text = "Hello world this is a test"
        result = wrap_text(text, width=10)
        assert len(result) > 1
        assert all(len(line) <= 10 for line in result if line)

    def test_wrap_empty_text(self):
        """Test wrapping empty text."""
        result = wrap_text("", width=10)
        assert result == [""]

    def test_wrap_multiline_text(self):
        """Test wrapping text with newlines."""
        text = "Line 1\nLine 2\nLine 3"
        result = wrap_text(text, width=20)
        assert len(result) >= 3

    def test_wrap_with_default_width(self):
        """Test wrapping with default width."""
        text = "A" * 50
        result = wrap_text(text)
        assert len(result) > 1


class TestCreateSpeechBubble:
    """Test speech bubble creation."""

    def test_empty_lines(self):
        """Test speech bubble with empty lines."""
        result = create_speech_bubble([])
        assert result == ""

    def test_single_line(self):
        """Test speech bubble with single line."""
        result = create_speech_bubble(["Hello"])
        assert "< Hello >" in result
        assert "_" in result
        assert "-" in result

    def test_multiple_lines(self):
        """Test speech bubble with multiple lines."""
        lines = ["Line 1", "Line 2", "Line 3"]
        result = create_speech_bubble(lines)
        assert "/ Line 1 \\" in result
        assert "| Line 2 |" in result
        assert "\\ Line 3 /" in result

    def test_different_line_lengths(self):
        """Test speech bubble with lines of different lengths."""
        lines = ["Short", "This is a longer line", "Mid"]
        result = create_speech_bubble(lines)
        # All lines should be padded to same length
        lines_in_bubble = [line for line in result.split("\n") if line.startswith(("/", "|", "\\"))]
        if len(lines_in_bubble) > 1:
            line_lengths = [len(line) for line in lines_in_bubble]
            assert len(set(line_lengths)) == 1  # All same length


class TestColorizeText:
    """Test text colorization."""

    def test_no_color(self):
        """Test text without color."""
        text = "Hello"
        result = colorize_text(text)
        assert result == text

    def test_none_color(self):
        """Test text with None color."""
        text = "Hello"
        result = colorize_text(text, None)
        assert result == text

    def test_valid_color(self):
        """Test text with valid color."""
        text = "Hello"
        result = colorize_text(text, "red")
        assert result != text
        assert text in result

    def test_invalid_color(self):
        """Test text with invalid color."""
        text = "Hello"
        result = colorize_text(text, "invalid")
        assert result == text

    def test_case_insensitive_color(self):
        """Test that color names are case insensitive."""
        text = "Hello"
        result1 = colorize_text(text, "RED")
        result2 = colorize_text(text, "red")
        result3 = colorize_text(text, "Red")
        assert result1 == result2 == result3


class TestFormatMessage:
    """Test complete message formatting."""

    def test_simple_message(self):
        """Test formatting simple message."""
        message = "Hello world"
        result = format_message(message)
        assert "Hello world" in result
        assert "_" in result  # Top border
        assert "-" in result  # Bottom border

    def test_message_with_color(self):
        """Test formatting message with color."""
        message = "Hello world"
        result = format_message(message, color="red")
        assert "Hello world" in result

    def test_message_with_custom_width(self):
        """Test formatting message with custom width."""
        message = "This is a very long message that should be wrapped"
        result = format_message(message, width=20)
        lines = result.split("\n")
        # Check that content lines don't exceed width + bubble chars
        content_lines = [line for line in lines if line.startswith(("/", "|", "\\", "<"))]
        for line in content_lines:
            assert len(line) <= 20 + 4  # width + bubble characters

    def test_empty_message(self):
        """Test formatting empty message."""
        result = format_message("")
        assert result == ""
