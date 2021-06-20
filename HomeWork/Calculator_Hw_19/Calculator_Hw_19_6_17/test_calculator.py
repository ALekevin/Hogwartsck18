import pytest
import yaml

from HomeWork.Calculator_Hw_19.Calculator_Hw_19_6_17.calculator import Calculator


def get_datas():
    with open("./calc_data.yml") as f:
        totals = yaml.safe_load(f)
        return (totals['add'], totals['sub'], totals['mul'], totals['div'])


def get_ids():
    with open("./calc_data.yml") as f:
        totals = yaml.safe_load(f)
        return totals['ids']


def test_getdatas():
    print(get_datas())


def test_getids():
    print(get_ids())


class TestCalc:
    def setup(self):
        self.calc = Calculator()
        print("\n开始计算")

    def teardown(self):
        print("\n结束计算")

    @pytest.mark.parametrize("a,b,expect", get_datas()[0], ids=get_ids())
    def test_add(self, a, b, expect):
        assert expect == round(self.calc.add(a, b), 10)

    @pytest.mark.parametrize("a,b,expect", get_datas()[1], ids=get_ids())
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()[2], ids=get_ids())
    def test_mul(self, a, b, expect):
        assert expect == round(self.calc.mul(a, b), 10)

    @pytest.mark.parametrize("a,b,expect", get_datas()[3], ids=get_ids())
    def test_div(self, a, b, expect):
        try:
            assert expect == round(self.calc.div(a, b), 10)
        except ZeroDivisionError as e:
            print("除数不能为0")
