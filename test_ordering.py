import pytest

# 4.4 控制⽤例的执⾏顺序：pytest-ordering

@pytest.mark.run(order=2)
def test_foo():
    assert True

@pytest.mark.run(order=1)
def test_bar():
    assert True