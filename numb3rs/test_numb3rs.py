import pytest 
import numb3rs

def test_validate_1234():
    assert numb3rs.validate ('1.2.3.4') == True

def test_validate_abcd():
    assert numb3rs.validate ('A.B.C.D') == False

def test_validate_no_dots():
    assert numb3rs.validate ('1234') == False

def test_validate_too_short():
    assert numb3rs.validate ('1.2.3') == False

def test_validate_too_long():
    assert numb3rs.validate ('1.2.3.4.5') == False

def test_validate_mix():
    assert numb3rs.validate ('A.1.C.3') == False

def test_validate_too_high():
    assert numb3rs.validate ('1.2.327.5') == False
