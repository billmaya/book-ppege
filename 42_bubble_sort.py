# Exercise 42 - Bubble Sort

def bubbleSort(numbers):
    if numbers == []: return

    l = len(numbers)

    for i in range(l - 1):
        for j in range(i + 1, l):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

                #print(numbers)

    return numbers



'''
list = [2, 0, 4, 1, 3]

while list != []:
    list = input('Enter list elements separated by space: ').split()
    print(list)
    bubbleSort(list)
    print(list)

'''
#'''
assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
#''

