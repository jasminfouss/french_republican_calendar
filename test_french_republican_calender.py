from datetime import date
import pytest
from republican_calender import (
    gregorian_to_republican,
    republican_to_gregorian,
    get_decade_day_name,
    validate_date_string,
)
def test_gregorian_to_republican():
    year, month_name, day, day_name = gregorian_to_republican(date(1792, 9, 22))
    assert (year, month_name, day) == (1, "Vendémiaire", 1)
    assert day_name == "Primidi"
    year, month_name, day, day_name = gregorian_to_republican(date(1794, 7, 27))
    assert (year, month_name, day) == (2, "Thermidor", 9)
    with pytest.raises(ValueError):
        gregorian_to_republican(date(1700, 1, 1))
def test_republican_to_gregorian():
    assert republican_to_gregorian(1, "Vendémiaire", 1) == date(1792, 9, 22)
    assert republican_to_gregorian(2, "Thermidor", 9) == date(1794, 7, 27)
    with pytest.raises(ValueError):
        republican_to_gregorian(1, "NotAMonth", 1)
    with pytest.raises(ValueError):
        republican_to_gregorian(1, "Vendémiaire", 31)
def test_get_decade_day_name():
    assert get_decade_day_name(1) == "Primidi"
    assert get_decade_day_name(10) == "Décadi"
    assert get_decade_day_name(11) == "Primidi"
    with pytest.raises(ValueError):
        get_decade_day_name(0)
    with pytest.raises(ValueError):
        get_decade_day_name(31)
def test_validate_date_string():
    assert validate_date_string("1792-09-22") == date(1792, 9, 22)
    with pytest.raises(ValueError):
        validate_date_string("not-a-date")
    with pytest.raises(ValueError):
        validate_date_string("2024-13-01")
