import pytest

from application import TestMe

def test_server():
    assert TestMe().take_four() == 4

def test_port():
    assert TestMe().port() == 8000

