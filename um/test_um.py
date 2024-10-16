import pytest
import um

def test_count_1():
    assert um.count("um") == 1

def test_count_2():
    assert um.count("um, UM") == 2

def test_count_4():
    assert um.count("um, UM, Um, uM") == 4

def test_count_3():
    assert um.count("um, aUM, Um, uM") == 3

def test_count_no_space():
    assert um.count("um,aUM,Um, uM") == 3

def test_count_inside_word():
    assert um.count("Aluminum") == 0

def test_count_inside_word2():
     assert um.count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
