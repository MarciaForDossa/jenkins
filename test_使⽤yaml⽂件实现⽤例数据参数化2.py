# 使⽤yaml⽂件实现⽤例数据参数化
# 注意：使⽤之前需要在pycharm中安装PyYAML,pip install pyyaml
# 加载yaml⽂件：
# yaml.safe_load(open("./data.yml"))


import pytest,yaml

# 读取数据抽离出来改造：
def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas=datas["datas"]
        add_ids=datas["myid"]
        return [add_datas,add_ids]

def add_function(a,b):
    return a+b
@pytest.mark.parametrize('a,b,expected',
                    get_datas()[0],
                    ids=get_datas()[1])
@pytest.mark.yaml2                    
def test_add(a,b,expected):
    assert add_function(a,b) == expected