from romanos import converter

def test_1_I(): 
    assert converter("1") == "I"

def test_2_II(): 
    assert converter("2") == "II"
    
def test_2_III(): 
    assert converter("3") == "III"