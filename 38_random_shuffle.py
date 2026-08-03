# Exercise 38 - Random Shuffle

from random import seed, randint

from datetime import datetime

def shuffle(values):
    
   seed(datetime.now().second)

   for i in range(len(values)):
      swapIndex = randint(0, len(values) - 1)
      values[i], values[swapIndex] = values[swapIndex], values[i]









'''
list = [1, 2, 3, 4, 5]
print(f'{list}\n')

for x in range(10):
    shuffle(list)
    print(list)
'''

'''
list = [1, 2, 3, 4, 5]

while list != []:
    list = input('Enter list elements separated by space: ').split()
    shuffle(list)
    print(list)

'''
#'''
seed(42)

for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    shuffle(testData1)
    
    assert len(testData1) == 10
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#'''

