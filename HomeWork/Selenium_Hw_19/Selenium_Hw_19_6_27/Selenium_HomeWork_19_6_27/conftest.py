import pytest
import yaml


def get_datas():
    with open('./data.yml', 'r', encoding='UTF-8') as f:
        total = yaml.safe_load(f)
        return total

@pytest.fixture(params=get_datas())
def get_deparment_name(request):
    return request.param