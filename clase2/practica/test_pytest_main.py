# Miguel Gómez Gómez-Escalonilla
# miguel.gomez.escalonilla@gmail.com
# Practica02

import pytest
from main import ingresar_persona, leer_archivo, return_file

def testcase_01():
    
    df = return_file()

    for i in df['age']:
        assert i > 17
        
def testcase_02():
    
    df = return_file()
    
    for i in df['name']:
        assert i[0].isupper()

def testcase_03():
        
    df = return_file()

    for i in df['email']:
        assert i.count('@') < 2

def testcase_04():

    df = return_file()

    assert df.isnull is not None


def testcase_05():
    
    df = return_file()
    
    for i in df['surname']:
        assert i[0].isupper()