# 使⽤yaml⽂件实现⽤例数据参数化
# 注意：使⽤之前需要在pycharm中安装PyYAML,pip install pyyaml
# 加载yaml⽂件：
# yaml.safe_load(open("./data.yml"))

import pytest,yaml

def add_function(a,b):
    return a+b
@pytest.mark.parametrize('a,b,expected',
                    yaml.safe_load(open("./data.yml"))["datas"],
                    ids=yaml.safe_load(open("./data.yml"))["myid"])
@pytest.mark.yaml1                    
def test_add(a,b,expected):
    assert add_function(a,b) == expected