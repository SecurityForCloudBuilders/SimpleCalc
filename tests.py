from calculator import calculator
#--------------
def test_sum():
    assert calculator(1,'+',1) == 2
    assert calculator(1023,'+',100) == 1123

def test_subraction():
    assert calculator(2,'-',1) == 1
    assert calculator(0,'-',1) == -1

def test_multiplication():
    assert calculator(2,'*',2) == 4
    assert calculator(6,'*',6) == 36

def test_division():
    assert calculator(6,'/',3) == 2
    assert calculator(15,'/',5) == 3
