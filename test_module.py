import pytest
# test_Setup_Teardown
# 模块中的方法
def setup_module():
    print("\nsetup_module:整个test_modul.py模块只执行一次")
def teardown_module():
    print("\nteardown_module:整个test_modul.py模块只执行一次")

def setup_function():
    print("\nsetup_function:每个不在类中的用例开始前都会执行")
def teardown_function():
    print("\nteardown_function:每个不在类中的用例结束后都会执行")

# 测试模块中的用例1
def test_one():
    print("正在执行测试模块----test_one")
# 测试模块中的用例2
def test_two():
    print("正在执行测试模块----test_two")

# 测试类
class TestCase():
    def setup_class(self):
        print("\nsetup_class:所有用例执行之前")
    def teardown_class(self):
        print("\nteardown_class:所有用例执行之后")

    def setup_method(self):
        print("\nsetup_method:每个用例开始前执行")
    def teardown_method(self):
        print("\nteardown_method:每个用例结束后执行")

    def setup(self):
        print("\nsetup:每个用例开始前执行")
    def teardown(self):
        print("\nteardown:每个用例结束后执行")

    def test_three(self):
        print("\n正在执行测试类----test_three")
    def test_four(self):
        print("\n正在执行测试类----test_four")
