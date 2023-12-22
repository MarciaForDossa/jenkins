import pytest
@pytest.mark.parametrize("a", [0,1,4])
@pytest.mark.parametrize("b", [2,3,6])
# @pytest.mark.parametrize("c", [4,5])
def test_foo(a,b):
    print("测试数据组合:a->%s, b->%s" % (a,b))