import pytest
import yaml

from HomeWork.Calculator_Hw_19.Calculator_Hw_19_6_20.calculator import Calculator

@pytest.fixture(scope='class')
def get_calc():
    print("\n开始计算")
    calc=Calculator()
    yield calc
    print("\n结束计算")

def get_datas():
    with open("./calc_data.yml") as f:
        totals = yaml.safe_load(f)
        return (totals['add'], totals['sub'], totals['mul'], totals['div'])


def get_ids():
    with open("./calc_data.yml") as f:
        totals = yaml.safe_load(f)
        return totals['ids']


@pytest.fixture(params=get_datas()[0], ids=get_ids())
def get_calc_add_datas(request):
    return request.param


@pytest.fixture(params=get_datas()[1], ids=get_ids())
def get_calc_sub_datas(request):
    return request.param


@pytest.fixture(params=get_datas()[2], ids=get_ids())
def get_calc_mul_datas(request):
    return request.param


@pytest.fixture(params=get_datas()[3], ids=get_ids())
def get_calc_div_datas(request):
    return request.param