import pytest

final_list = []

@pytest.fixture()
def create_number():
    num_list=[2,3,5,7]

    return num_list

