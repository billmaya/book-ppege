# Exercise 2 - Temperature Conversion

def convertToFahrenheit(degreesCelcius):
    return degreesCelcius * (9 / 5) + 32

def convertToCelcius (degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5 / 9)

assert convertToCelcius(0) == -17.77777777777778
assert convertToCelcius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelcius(convertToFahrenheit(15)) == 15
assert convertToCelcius(convertToFahrenheit(42)) == 42.00000000000001

