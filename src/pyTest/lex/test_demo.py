import pytest


@pytest.fixture()
def inject_dependency():
    # one can write here the code for connecting to Excel or a database
    print("inside pytest fixture")


@pytest.fixture(scope='module')
def module_inject_dependency():
    print("inside module scoped fixture")

@pytest.mark.xfail
def test_fixture_demo(inject_dependency, module_inject_dependency):
    print("executing fixture demo test case")


def test_fixture_demo_1(inject_dependency, module_inject_dependency):
    print("executing fixture demo test 2")


