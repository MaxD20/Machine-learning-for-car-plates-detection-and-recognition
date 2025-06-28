import pytest
from domain.plate import is_valid_license_plate

@pytest.mark.parametrize(
    "plate,expected",
    [
        ("B 123 XYZ",  True),
        ("CJ12ABC",    True),
        ("DRIVERTXT",     False),
        ("ABC 123456", False),
        ("VL 03 TON", True),
        ("CT 75 DMX", True),
    ],
)
def test_is_valid_license_plate(plate, expected):
    assert is_valid_license_plate(plate) is expected