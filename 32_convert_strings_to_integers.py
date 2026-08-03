# Exercise 32 - Convert Strings To Integers

def convertStrToInt(stringNum):

    integerNum = 0
    negativeNumber = False
    strToIntDict = {'1': 1,
                    '2': 2,
                    '3': 3,
                    '4': 4,
                    '5': 5,
                    '6': 6,
                    '7': 7,
                    '8': 8,
                    '9': 9,
                    '0': 0}

    #print('String: ' + stringNum) # -345
   
    for i in range(len(stringNum)): # 0, 1, 2, 3
        digit = stringNum[abs(i -  (len(stringNum) - 1))]

        if digit == '-':
            negativeNumber = True
        else:
            multiplier = strToIntDict[digit]
            tens = 10 ** i
            
            integerNum = integerNum + (multiplier * tens)

        #print('digitString: ' + digitString + ' multiplier: ' + str(multiplier) + ' tens: ' + str(tens))
        
    if negativeNumber:
        integerNum = -integerNum

    #print('Integer: ' + str(integerNum))

    return integerNum

#convertStrToInt('-345')

for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i

