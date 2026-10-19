from romanos import converter

def test_1_I(): 
    assert converter(1) == "I"

def test_2_II(): 
    assert converter(2) == "II"

def test_3_III(): 
    assert converter(3) == "III"

def test_4_IV(): 
    assert converter(4) == "IV"

def test_6_VI(): 
    assert converter(6) == "VI"