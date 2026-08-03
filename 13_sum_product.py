# Exercise 13 - Sum Product

def calculateSum(numbers):
    #if numbers == []:
    #    return 0

    result = 0 # Don't use 'sum' since this overrides built-in sum() function
    for number in numbers:
        result += number

    return result

    

def calculateProduct(numbers):
    #if numbers == []:
    #    return 1

    product = 1
    for number in numbers:
        product *= number

    return product



assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840


