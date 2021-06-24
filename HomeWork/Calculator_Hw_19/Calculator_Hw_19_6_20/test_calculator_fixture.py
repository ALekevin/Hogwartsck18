import logging

import allure
import pytest
import yaml
import logging
@allure.feature('计算器模块')
class TestCalc:
    @pytest.mark.add
    @allure.story('加法功能')
    @allure.title('{get_calc_add_datas}_加法成功')
    def test_add(self, get_calc, get_calc_add_datas):
        with allure.step('打印日志'):
            logging.info(f"test_add 数据 {get_calc_add_datas}")
        assert get_calc_add_datas[2] == round(get_calc.add(get_calc_add_datas[0], get_calc_add_datas[1]), 10)

    @pytest.mark.sub
    @allure.story('减法功能')
    @allure.title('{get_calc_sub_datas}_减法成功')
    def test_sub(self, get_calc, get_calc_sub_datas):
        logging.info(f"test_sub 数据 {get_calc_sub_datas}")
        assert get_calc_sub_datas[2] == get_calc.sub(get_calc_sub_datas[0], get_calc_sub_datas[1])

    @pytest.mark.mul
    @allure.story('乘法功能')
    @allure.title('{get_calc_mul_datas}_乘法成功')
    def test_mul(self, get_calc, get_calc_mul_datas):
        logging.info(f"test_mul 数据 {get_calc_mul_datas}")
        assert get_calc_mul_datas[2] == round(get_calc.mul(get_calc_mul_datas[0], get_calc_mul_datas[1]), 10)

    @pytest.mark.div
    @allure.story('除法功能')
    @allure.title('{get_calc_div_datas}_除法成功')
    def test_div(self, get_calc, get_calc_div_datas):
        logging.info(f"test_div 数据 {get_calc_div_datas}")
        try:
            assert get_calc_div_datas[2] == round(get_calc.div(get_calc_div_datas[0], get_calc_div_datas[1]), 10)
        except ZeroDivisionError as e:
            print("除数不能为0")
