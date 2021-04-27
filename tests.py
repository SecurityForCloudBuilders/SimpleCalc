from calculator import calculator
#--------------
def test_sum():
    assert calculator(1,'+',1) == 2

def test_subraction():
    assert calculator(2,'-',1) == 1

def test_multiplication():
    assert calculator(2,'*',2) == 4

def test_division():
    assert calculator(6,'/',3) == 2
