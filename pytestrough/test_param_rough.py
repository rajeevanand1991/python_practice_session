import pytest

@pytest.mark.parametrize("num, result", [(1,11), (2,22), (3,35), (4,44), (5,55)]) #num = 1 and result = 11
def test_calculation(num, result):
    assert 11*num == result