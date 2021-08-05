import logging
import os
from datetime import datetime

from typing import List

import pytest


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    '''
    重写hook函数，将收集上来的用例名称编码格式设置成支持中文格式
    :param session:
    :param config:
    :param items:
    :return:
    '''
    for item in items:
        # 用例名
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # 用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


class plugins_logger:
    _all_log_level = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET']
    _logger_level = "INFO"

    def __init__(self):
        self.logger = logging.getLogger()

    def create(self):
        # logger等级大写
        logger_level = self._logger_level.upper()
        # 如果logger等级不在等级设置范围中抛出ValueError异常
        if logger_level not in self._all_log_level:
            raise ValueError(f"_logger_level 设置的值不在范围: {self._all_log_level}")
        # 设置日志等级
        self.logger.setLevel(logger_level)
        # 设置日志文件生成路径及编码格式
        f_file = logging.FileHandler(os.path.join(self.set_log_dir(), f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"), encoding='UTF-8')
        # 设置日志输出流
        f_stream = logging.StreamHandler()
        # 获取日志格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s : %(message)s')
        f_file.setFormatter(formatter)
        f_stream.setFormatter(formatter)
        # 添加handler
        self.logger.addHandler(f_file)
        self.logger.addHandler(f_stream)
        return self.logger

    def set_log_dir(self):
        #获取当前路径
        current_path = os.getcwd()
        #获取log文件存储文件夹路径
        log_path = os.path.join(current_path, 'logs', str(datetime.now().date()))
        #判断是否存在文件夹，若不存在创建文件夹
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        return log_path


logger = plugins_logger().create()


