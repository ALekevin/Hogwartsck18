from typing import List

import pytest
import yaml

from HomeWork.Calculator_Hw_19.Calculator_Hw_19_test.calculator import Calculator


@pytest.fixture()
def get_calc():
    calc = Calculator()
    print("\n开始计算")
    yield calc
    print("\n结束计算")


def get_datas():
    with open("./calc_data.yml", encoding='UTF-8') as f:
        totals = yaml.safe_load(f)
        return (totals['add'], totals['sub'], totals['mul'], totals['div'])


def get_ids():
    with open("./calc_data.yml", encoding='UTF-8') as f:
        totals = yaml.safe_load(f)
        return totals['ids']

@pytest.fixture(params=get_datas()[0],ids=get_ids())
def get_calc_add_test(request):
    return request.param

@pytest.fixture(params=get_datas()[1],ids=get_ids())
def get_calc_sub_test(request):
    return request.param

@pytest.fixture(params=get_datas()[2],ids=get_ids())
def get_calc_mul_test(request):
    return request.param

@pytest.fixture(params=get_datas()[3],ids=get_ids())
def get_calc_div_test(request):
    return request.param

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')