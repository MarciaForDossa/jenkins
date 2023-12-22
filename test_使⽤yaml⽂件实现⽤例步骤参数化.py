# 使⽤yaml⽂件实现⽤例步骤参数化
import pytest,yaml

def step1():
    print("打开浏览器")
def step2():
    print("注册新账号")
def step3():
    print("登录新账号") 
# 解析测试步骤文件
def steps(path):
    with open(path) as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if "step1" in step:
            step1()
        elif "step2" in step:
            step2()    
        elif "step3" in step:
            step3()

@pytest.mark.steps
def test_foo():
    steps("./steps.yml")