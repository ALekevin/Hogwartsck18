import pytest
import yaml

from Calculator_Hw import Calculator


class TestCase():
    # 加法成功
    #@pytest.mark.run(order=1)
    def test_add_success(self, initset, get_add_success_datas):
        assert get_add_success_datas[2] == initset.add(get_add_success_datas[0], get_add_success_datas[1])

    # 加法失败
    # @pytest.mark.run(order=3)
    def test_add_fail(self, initset, get_add_fail_datas):
        if type(get_add_fail_datas[0]) == str or type(get_add_fail_datas[1]) == str or type(
                get_add_fail_datas[2]) == str:
            print("输入值必须为数字")
        else:
            assert get_add_fail_datas[2] != initset.add(get_add_fail_datas[0], get_add_fail_datas[1])

    # 除法成功
    #@pytest.mark.run(order=2)
    def test_div_success(self, initset, get_div_success_datas):
        assert get_div_success_datas[2] == round(initset.div(get_div_success_datas[0], get_div_success_datas[1]), 1)

    # 除法失败
    # @pytest.mark.run(order=4)
    def test_div_fail(self, initset, get_div_fail_datas):
        if type(get_div_fail_datas[2]) == str or type(get_div_fail_datas[0]) == str or type(
                get_div_fail_datas[1]) == str:
            print("输入值必须为数字")
        elif get_div_fail_datas[1] == 0:
            print('分母不能为0')
        else:
            assert get_div_fail_datas[2] != initset.div(get_div_fail_datas[0], get_div_fail_datas[1])
