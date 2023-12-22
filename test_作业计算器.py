import pytest

# 1. 补全计算器（加减乘除）的测试⽤例

def add_function(a,b):
    return a+b
def subtract_function(a,b):
    return a-b
def multiply_function(a,b):
    return a*b
def divide_function(a,b):
    return a/b
@pytest.mark.parametrize("a,b,expected",
                        [(3,5,8),
                        (-1,-2,-3),
                        (100,200,300),
                        ])
def test_add(a,b,expected):
    assert add_function(a,b) == expected
    assert subtract_function(a,b) == expected
    assert multiply_function(a,b) == expected
    assert divide_function(a,b) == expected

# def test_subtract(a,b,expected):
#     assert subtract_function(a,b) == expected
# def test_multiply(a,b,expected):
#     assert multiply_function(a,b) == expected
# def test_divide(a,b,expected):
#     assert divide_function(a,b) == expected