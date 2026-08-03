# Exercise 12 - Smallest Biggest

def getSmallest(numbers):
    if numbers == []:
        return None

    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest
    
    # My initial implementation
    '''
    smallestNumber = numbers[0]
    index = 1

    while index < len(numbers):
        if numbers[index] < smallestNumber:
            smallestNumber = numbers[index]
        
        index += 1

    return smallestNumber
    '''

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None
