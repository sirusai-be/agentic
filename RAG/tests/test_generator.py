"""
Tests for generator module.
"""

import pytest
from src.rag.generator import Generator


def test_generator_init():
    """Test generator initialization."""
    generator = Generator()
    assert generator is not None

