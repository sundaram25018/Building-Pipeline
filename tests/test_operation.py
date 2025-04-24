from src.operations import add,sub

def test_add():
    assert add(1,2) == 3
    assert add(-1,-1) == -2

def test_sub():
    assert sub(2,1) == 1
    assert sub(-1,-1) == 0
   