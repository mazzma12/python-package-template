"""Message formatting utilities."""

import textwrap

from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init()


def wrap_text(text: str, width: int = 40) -> list[str]:
    """
    Wrap text to fit within specified width.

    Args:
        text: Text to wrap
        width: Maximum width per line

    Returns:
        List of wrapped lines
    """
    lines = []
    for paragraph in text.split("\n"):
        if paragraph.strip():
            wrapped = textwrap.fill(paragraph, width=width)
            lines.extend(wrapped.split("\n"))
        else:
            lines.append("")
    return lines


def create_speech_bubble(lines: list[str]) -> str:
    """
    Create a speech bubble around the text lines.

    Args:
        lines: List of text lines

    Returns:
        Speech bubble as string
    """
    if not lines:
        return ""

    max_length = max(len(line) for line in lines)

    # Top border
    bubble = " " + "_" * (max_length + 2) + "\n"

    # Content with borders
    if len(lines) == 1:
        bubble += f"< {lines[0].ljust(max_length)} >\n"
    else:
        for i, line in enumerate(lines):
            if i == 0:
                bubble += f"/ {line.ljust(max_length)} \\\n"
            elif i == len(lines) - 1:
                bubble += f"\\ {line.ljust(max_length)} /\n"
            else:
                bubble += f"| {line.ljust(max_length)} |\n"

    # Bottom border
    bubble += " " + "-" * (max_length + 2)

    return bubble


def colorize_text(text: str, color: str | None = None) -> str:
    """
    Apply color to text if specified.

    Args:
        text: Text to colorize
        color: Color name (red, green, blue, yellow, magenta, cyan, white)

    Returns:
        Colorized text
    """
    if not color:
        return text

    color_map = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "blue": Fore.BLUE,
        "yellow": Fore.YELLOW,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }

    if color.lower() in color_map:
        return f"{color_map[color.lower()]}{text}{Style.RESET_ALL}"

    return text


def format_message(message: str, width: int = 40, color: str | None = None) -> str:
    """
    Format a message with speech bubble.

    Args:
        message: Message to format
        width: Maximum width of the speech bubble
        color: Color for the text

    Returns:
        Formatted message with speech bubble
    """
    lines = wrap_text(message, width)
    bubble = create_speech_bubble(lines)
    return colorize_text(bubble, color)
