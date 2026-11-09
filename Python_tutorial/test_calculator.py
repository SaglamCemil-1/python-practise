from calculator import square

""" 

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9   #assertion error döner 

if __name__ == "__main__":
    main()  

"""

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    #terminal de -> python -m pytest test_calculator.py

import pytest
def str_test():
    with pytest.raises(TypeError):
        square("cat")