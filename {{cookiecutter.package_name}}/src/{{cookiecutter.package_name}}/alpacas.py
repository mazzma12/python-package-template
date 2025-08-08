"""ASCII alpaca art definitions."""

from enum import Enum


class AlpacaType(Enum):
    """Available alpaca types."""

    DEFAULT = "default"
    HAPPY = "happy"
    THINKING = "thinking"


# ASCII Art for different alpaca types
ALPACAS: dict[AlpacaType, str] = {
    AlpacaType.DEFAULT: r"""
        /|   /|
       ( :v:  )
        |(_)|
        --m--m--
    """,
    AlpacaType.HAPPY: r"""
        /|   /|
       ( ^v^  )
        |(_)|
        --m--m--
    """,
    AlpacaType.THINKING: r"""
        /|   /|
       ( -v-  )
        |(_)|
        --m--m--
           o
          o
         o
    """,
}


def get_alpaca_art(alpaca_type: AlpacaType = AlpacaType.DEFAULT) -> str:
    """
    Get ASCII art for the specified alpaca type.

    Args:
        alpaca_type: The type of alpaca to display

    Returns:
        ASCII art string for the alpaca
    """
    return ALPACAS[alpaca_type]


def get_available_alpacas() -> list[str]:
    """
    Get list of available alpaca types.

    Returns:
        List of alpaca type names
    """
    return [alpaca.value for alpaca in AlpacaType]
