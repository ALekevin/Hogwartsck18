import threading
import time

import pytest


@pytest.fixture()
def get_datas():
    """
    获取部门名，通过时间戳和当前线程名拼接
    :return:
    """
    name = str(time.time()) + threading.currentThread().name
    return name
