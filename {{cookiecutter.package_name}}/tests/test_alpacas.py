"""Tests for alpaca ASCII art functionality."""

from {{ cookiecutter.package_name }}.alpacas import ALPACAS, AlpacaType, get_alpaca_art, get_available_alpacas


class TestAlpacaType:
    """Test AlpacaType enum."""

    def test_enum_values(self):
        """Test that enum has expected values."""
        assert AlpacaType.DEFAULT.value == "default"
        assert AlpacaType.HAPPY.value == "happy"
        assert AlpacaType.THINKING.value == "thinking"

    def test_enum_count(self):
        """Test that we have expected number of alpaca types."""
        assert len(AlpacaType) == 3


class TestAlpacas:
    """Test alpaca ASCII art."""

    def test_alpacas_dict_completeness(self):
        """Test that ALPACAS dict contains all enum values."""
        for alpaca_type in AlpacaType:
            assert alpaca_type in ALPACAS

    def test_alpaca_art_not_empty(self):
        """Test that all alpaca art strings are not empty."""
        for alpaca_art in ALPACAS.values():
            assert alpaca_art.strip()

    def test_get_alpaca_art_default(self):
        """Test getting default alpaca art."""
        art = get_alpaca_art()
        assert art == ALPACAS[AlpacaType.DEFAULT]

    def test_get_alpaca_art_specific(self):
        """Test getting specific alpaca art."""
        for alpaca_type in AlpacaType:
            art = get_alpaca_art(alpaca_type)
            assert art == ALPACAS[alpaca_type]

    def test_get_available_alpacas(self):
        """Test getting list of available alpaca names."""
        available = get_available_alpacas()
        expected = [alpaca.value for alpaca in AlpacaType]
        assert available == expected
        assert len(available) == 3
