import pytest
import yaml

from Calculator_Hw import Calculator


class TestCal():

    def setup_class(self):
        print("setup")
        self.calc = Calculator()

    def teardown_class(self):
        print("teardown")

    def setup(self):
        print('\n【开始计算】')

    def teardown(self):
        print('\n【计算结束】')


class TestCase(TestCal):
    # 加法成功
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./add_success_data.yml'))
        , ids=yaml.safe_load(open('./add_success_casename.yml')))
    def test_add_success(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    # 加法失败
    @pytest.mark.parametrize('a,b,expect',
                             yaml.safe_load(open('./add_fail_data.yml', encoding='utf-8')),
                             ids=yaml.safe_load(open('./add_fail_casename.yml', encoding='utf-8')))
    def test_add_fail(self, a, b, expect):
        if type(a) == str or type(b) == str or type(expect) == str:
            print("输入值必须为数字")
        else:
            assert expect != self.calc.add(a, b)

    # 除法成功
    @pytest.mark.parametrize('a,b,expect',
                             yaml.safe_load(open('./div_success_data.yml')),
                             ids=yaml.safe_load(open('./div_success_casename.yml')))
    def test_div_success(self, a, b, expect):
        assert expect == round(self.calc.div(a, b), 1)

    @pytest.mark.parametrize('a,b,expect',yaml.safe_load(open('./div_fail_data.yml',encoding='utf-8'))
                             , ids=yaml.safe_load(open('./div_fail_casename.yml',encoding='utf-8')))
    def test_div_fail(self, a, b, expect):
        if type(a) == str or type(b) == str or type(expect) == str:
            print("输入值必须为数字")
        elif b == 0:
            print('分母不能为0')
        else:
            assert expect != self.calc.div(a, b)
