import pytest 

# 4.2 多重校验：pytest-assume

def test_simple_assume():
    pytest.assume(1==0)
    pytest.assume(True)
    pytest.assume(False)