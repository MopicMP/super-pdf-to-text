"""Tests for super-pdf-to-text."""

import pytest
from super_pdf_to_text import text


class TestText:
    """Test suite for text."""

    def test_basic(self):
        """Test basic usage."""
        result = text("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            text("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = text(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
