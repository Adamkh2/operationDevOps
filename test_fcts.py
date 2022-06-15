from main import addition, soustraction, multiplication, division
import sys

def test_addition():
    a1 = 10000
    b1 = 20009
    expected1 = 30009

    a2 = -19500
    b2 = -20009
    expected2 = -39509

    assert expected1 == addition(a1,b1) 
    assert expected2 == addition(a2,b2)

def test_division():
    a1 = 10000
    b1 = 20
    expected1 = 500

    a2 = 19500
    b2 = 0
    expected2 = -1
    

    assert expected1 == division(a1,b1) 
    assert expected2 == division(a2,b2) 