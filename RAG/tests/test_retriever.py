"""
Tests for retriever module.
"""

import pytest
from src.rag.retriever import Retriever


def test_retriever_init():
    """Test retriever initialization."""
    retriever = Retriever()
    assert retriever is not None

