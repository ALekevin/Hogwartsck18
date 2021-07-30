import pytest
from faker import Faker


@pytest.fixture()
def get_faker_datas():
    faker = Faker("zh_CN")
    name = faker.name()
    phone = faker.phone_number()
    return name, phone

@pytest.fixture(params=[['hqr','10100001100'],['huangqianru','13321321231']],ids=['test1','test2'])
def get_datas(request):
    return request.param
