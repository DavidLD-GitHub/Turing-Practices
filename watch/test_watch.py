import pytest
import watch

LINKS = ['''<iframe width="560" height="315" src="http://youtube.com/embed/xvFZjo5PgG0"
        title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
        clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''',
        '''<iframe width="560" height="315" src="https://youtube.com/embed/xvFZjo5PgG0"
        title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
        clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''',
        '''<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"
        title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
        clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''']

def test_parse_type_1():
    assert watch.parse(LINKS[0]) == "https://youtu.be/xvFZjo5PgG0"

def test_parse_type_2():
    assert watch.parse(LINKS[1]) == "https://youtu.be/xvFZjo5PgG0"

def test_parse_type_3():
    assert watch.parse(LINKS[2]) == "https://youtu.be/xvFZjo5PgG0"

def test_parse_not_valid():
    assert watch.parse("https://www.youtube.com/embed/xvFZjo5PgG") is None

def test_parse_not_starting_iframe():
    assert watch.parse("https://www.youtube.com/embed/xvFZjo5PgG7") is None
