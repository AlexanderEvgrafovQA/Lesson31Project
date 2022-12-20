import pytest

def setup_module():
    print("setup module level", end=' ')

def teardown_module():
    print("teardown module level", end=' ')

def test_passing():
    print("running test_passing", end=' ')
    assert (1, 2, 3) == (1, 2, 3)

def test_failing():
    print("running test_failing", end=' ')
    assert (1, 2, 3) == (3, 2, 1)

def test_custom_failing():
    pytest.fail()

def setup_function():
    print("setup function level", end=' ')

def teardown_function():
    print("teardown function level", end=' ')