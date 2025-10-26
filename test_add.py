import pytest
from add import add

def test_add():
    assert add(2, 3) == 5
    assert add(1, 4) == 5
    assert add(2, 4) == 5
