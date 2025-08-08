"""
Alpacasay - A fun CLI tool that displays messages with ASCII alpacas.

Like cowsay, but with alpacas! 🦙
"""

__version__ = "0.1.0"
__author__ = "CrowdSecurity"
__email__ = "tech@crowdsec.net"

from .alpacas import ALPACAS, AlpacaType
from .cli import main
from .formatter import format_message

__all__ = ["ALPACAS", "AlpacaType", "format_message", "main"]
