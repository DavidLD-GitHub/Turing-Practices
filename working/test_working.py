import pytest
import working


def test_convert_valid1():
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_convert_valid2():
    assert working.convert("7 AM to 7 PM") == "07:00 to 19:00"

def test_convert_valid3():
    assert working.convert("9:10 PM to 5 AM") == "21:10 to 05:00"

def test_convert_valid4():
    assert working.convert("4 AM to 12:27 PM") == "04:00 to 12:27"

def test_convert_valid5():
    assert working.convert("11:27 PM to 12:40 AM") == "23:27 to 00:40"

def test_convert_wrong_format():
    with pytest.raises(ValueError):
        working.convert("11 PM 12 AM")

def test_convert_out_of_range_1():
    with pytest.raises(ValueError):
        working.convert("34:10 AM to 12:15 PM")

def test_convert_out_of_range_2():
    with pytest.raises(ValueError):
        working.convert("12:55 PM to 32:27 AM")

def test_convert_out_of_range_3():
    with pytest.raises(ValueError):
        working.convert("14:70 to 12:27")

def test_convert_out_of_range_4():
    with pytest.raises(ValueError):
        working.convert("14:40 to 12:77")

def test_convert_lower_case():
    with pytest.raises(ValueError):
        working.convert("11:27 pm to 12:40 am")
