import pytest


@pytest.mark.parametrize("num1, num2, result", [(5, 5, 10), (3, 5, 8)])
def test_add(num1, num2, result):
    assert num1 + num2 == result, "failed"

