import pytest,random

# 4.1. ⽤例失败后⾃动重新运⾏：pytest-rerunfailures
# @pytest.mark.flaky(reruns=6,reruns_delay=2)
@pytest.mark.flaky(reruns_delay=1)
def test_example():
    print(3)
    assert random.choice([True,False])
    # assert 1==0