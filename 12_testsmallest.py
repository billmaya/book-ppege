
import random

def getSmallest(numbers):
    if numbers == []:
        return None

    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

numbers = []

for i in range(100000):
    numbers.append(random.randint(1, 1000000000))

print('Numbers:', numbers)
print('Smallest number is ', getSmallest(numbers))
