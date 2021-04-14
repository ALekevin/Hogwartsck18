import yaml
import pytest

from HomeWork.Calculator_Hw_4_11.Calculator_Hw import Calculator


@pytest.fixture(scope="function")
def initset():
    print("\nsetup")
    calc = Calculator()
    yield calc
    print("\nteardown")


def get_datas():
    with open('./test_data.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas


@pytest.fixture(params=get_datas()['add_success_data'], ids=get_datas()['add_success_casename'])
def get_add_success_datas(request):
    return request.param


@pytest.fixture(params=get_datas()['add_fail_data'], ids=get_datas()['add_fail_casename'])
def get_add_fail_datas(request):
    return request.param


@pytest.fixture(params=get_datas()['div_success_data'], ids=get_datas()['div_success_casename'])
def get_div_success_datas(request):
    return request.param


@pytest.fixture(params=get_datas()['div_fail_data'], ids=get_datas()['div_fail_casename'])
def get_div_fail_datas(request):
    return request.param


def pytest_collection_modifyitems(session, config, items):
    print(items)
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # 打上"add"标签
        # if "add" in item.name:
        #     item.add_marker(pytest.mark.add)
        # elif "div" in item.name:
        #     item.add_marker(pytest.mark.div)