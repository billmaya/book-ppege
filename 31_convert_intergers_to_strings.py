# Exercise 31 - Convert Integers To Strings

def convertIntToStr(integerNum):
    if integerNum == 0:
        return '0'

    intToConvert = integerNum
    stringNum = ''
    intToStrDict = {1:'1',
                    2:'2',
                    3:'3',
                    4:'4',
                    5:'5',
                    6:'6',
                    7:'7',
                    8:'8',
                    9:'9',
                    0:'0'}

    if integerNum < 0:
        intToConvert = abs(intToConvert)

    while intToConvert != 0:
        onesPlaceDigit = intToConvert % 10
        stringNum = intToStrDict[onesPlaceDigit] + stringNum
        intToConvert //= 10

    if integerNum < 0:
        stringNum = '-' + stringNum

    return stringNum




#convertIntToStr(345)
for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)

