from bmi import convertWeight, convertHeight, doMath, calculateBMI, classify
def test_convertWeight():
    assert convertWeight(100) == 45

def test_convertHeight():
    assert convertHeight(100) == 2.5

def test_doMath():
    assert doMath(45, 2.5) == 7.2

def test_calculateBMI():
    assert calculateBMI(100, 100) == 7.2

def test_classify():
    assert classify(18.4) == "Underweight"
    assert classify(18.5) == "Normal Weight"
    assert classify(20) == "Normal Weight"
    assert classify(24.9) == "Normal Weight"
    assert classify(25) == "Overweight"
    assert classify(26) == "Overweight"
    assert classify(29.9) == "Overweight"
    assert classify(30) == "Obese"
