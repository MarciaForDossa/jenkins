import pytest

class Test_Demo():
    @pytest.mark.demo
    @pytest.mark.none
    def test_demo(self):
        a = 5
        b = -1
        assert a != b
        print("我的第⼀个测试⽤例")
    @pytest.mark.demo2
    def test_demo2(self):
        a = 5
        b = -1
        assert a == b
        print("我的第二个测试⽤例")