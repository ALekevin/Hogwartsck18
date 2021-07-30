import pytest
import yaml
import os, sys
path = os.path.abspath(__file__)
for i in range(4):
  path = os.path.dirname(path)
sys.path.append(path)
from HomeWork.Calculator_Hw_19.Calculator_Hw_19_6_17.calculator import Calculator


# def get_datas():
#     with open("./calc_data.yml",encoding='UTF-8') as f:
#         totals = yaml.safe_load(f)
#         return (totals['add'], totals['sub'], totals['mul'], totals['div'])
#
#
# def get_ids():
#     with open("./calc_data.yml",encoding='UTF-8') as f:
#         totals = yaml.safe_load(f)
#         return totals['ids']


# def test_getdatas():
#     print(get_datas())
#
#
# def test_getids():
#     print(get_ids())


class TestCalc:
    # def setup(self):
    #     self.calc = Calculator()
    #     print("\n开始计算")
    #
    # def teardown(self):
    #     print("\n结束计算")


    def test_add(self,get_calc,get_calc_add_test):
        assert get_calc_add_test[2] == round(get_calc.add(get_calc_add_test[0], get_calc_add_test[1]), 10)

    def test_sub(self, get_calc,get_calc_sub_test):
        assert get_calc_sub_test[2] == get_calc.sub(get_calc_sub_test[0], get_calc_sub_test[1])

    def test_mul(self, get_calc,get_calc_mul_test):
        assert get_calc_mul_test[2] == round(get_calc.mul(get_calc_mul_test[0], get_calc_mul_test[1]), 10)

    def test_div(self,get_calc,get_calc_div_test):
        try:
            assert get_calc_div_test[2] == round(get_calc.div(get_calc_div_test[0], get_calc_div_test[1]), 10)
        except ZeroDivisionError as e:
            print(f"{e}:除数不能为0")
