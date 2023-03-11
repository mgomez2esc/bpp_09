import pytest

def capital(x):
    return x.capitalize()

def test_capital1():
    assert capital('hola') == 'Hola'

def test_capital2():
    assert capital('hola') == 'Hoola'