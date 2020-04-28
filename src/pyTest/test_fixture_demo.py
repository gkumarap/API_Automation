import pytest


@pytest.fixture()
def before():
    print('\nbefore each test')
    value=39
    return value


def test_1(before):
    print(before)
    assert before % 3 == 0


def test_2(before):
    print('test_2()')

@pytest.fixture()
def after():
    print('\n this is the second ficture ')
    value = 10
    return value


def test_3(before,after):
    print('3rd test',before)
    print('3rd test',after)