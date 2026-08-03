# Exercise 6 - Ordinal Suffix

def ordinalSuffix(forNumber):
    suffix = ''
    
    lastDigit = forNumber[-1]
    
    if len(forNumber) >= 2:
        penultimateDigit = forNumber[-2]
    else:
        penultimateDigit = ''

    match lastDigit:
        case '1':
            suffix = 'st'
        case '2':
            suffix = 'nd'
        case '3':
            suffix = 'rd'
        case _:
            suffix = 'th' 
    
    if len(penultimateDigit) != 0:
        lastTwoDigits = penultimateDigit + lastDigit
    else:
        lastTwoDigits = ''

    if lastTwoDigits == '11' or lastTwoDigits == '12' or lastTwoDigits == '13':
        suffix = 'th'

    return suffix

while True:
    number = input("What number do you want to ordinalize (type 'quit' to quit)? ")
    if number == 'quit': break
    else:
        numberStr = number
        suffix = ordinalSuffix(number)
        print(number + suffix, end='\n\n')



'''
assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '4th'
assert ordinalSuffix(4) == '5th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == 'llth'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
'''
