import threading
import time

import pytest
from faker import Faker


@pytest.fixture()
def get_dates():
    faker = Faker('zh_CN')
    userid = str(time.time()) + threading.currentThread().name
    name = faker.name()
    mobile = faker.phone_number()
    return userid, name, mobile
