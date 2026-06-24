"""
tests/test_utils.py – unit tests for utils.py helpers
"""

import sys
from pathlib import Path

# Allow importing utils from the project root
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from utils import text_stats


class TestTextStats:
    """Tests for the text_stats() utility function."""

    def test_empty_string(self):
        result = text_stats("")
        assert result["word_count"] == 0
        assert result["char_count"] == 0

    def test_whitespace_only(self):
        result = text_stats("   ")
        assert result["word_count"] == 0
        assert result["char_count"] == 0

    def test_single_word(self):
        result = text_stats("hello")
        assert result["word_count"] == 1
        assert result["char_count"] == 5

    def test_multiple_words(self):
        result = text_stats("The movie was great")
        assert result["word_count"] == 4
        assert result["char_count"] == 19

    def test_leading_trailing_spaces(self):
        result = text_stats("  hello world  ")
        assert result["word_count"] == 2
        assert result["char_count"] == 11  # len("hello world")

    def test_returns_dict_with_correct_keys(self):
        result = text_stats("test input")
        assert "word_count" in result
        assert "char_count" in result
