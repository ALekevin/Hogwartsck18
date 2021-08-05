import pytest

from HomeWork.pytest_plugins_Hw_19.testcase.conftest import logger


class TestDemo:
    @pytest.mark.parametrize('a',['乐恺欣','黄倩如'])
    def test_1(self,a):
        logger.info('开始执行用例')
        print(a)