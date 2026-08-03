# Exercise 16 - Mode

def mode(numbers):
    if numbers == []:
        return None

    frequency = {}

    for number in numbers:
        if number in frequency: 
            frequency[number] = frequency[number] + 1
        else:
            frequency[number] = 1

    #print(frequency)

    #for number, occurrance in frequency.items():
    #    print(f'{number}: {occurrance}')

    modeKey = next(iter(frequency))
    modeValue = frequency[modeKey]
    #print(f'{modeKey}: {modeValue}')
    
    for number, occurrance in frequency.items():
        if occurrance > modeValue:
            modeKey = number
            modeValue = occurrance

    #print(modeKey) 
    
    if modeValue == 1:
        return numbers
    else:
        return modeKey



#mode([1, 2, 3, 4, 4])


assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4

assert mode([1, 2, 3, 4]) == [1, 2, 3, 4]

