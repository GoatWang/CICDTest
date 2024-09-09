import pytest
from mymath.example import square

# @pytest.mark.parameterize([1, 2, 3])
def test_square():
    assert square(2) == 4