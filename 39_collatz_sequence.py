# Exercise 39 - Collatz Sequence

def collatz(startingNumber):

    collatz = []

    if startingNumber >= 1:
        collatz.append(startingNumber)

        while True:
            if startingNumber == 1:
                break
            else:
                if startingNumber % 2 == 0: # even
                    nextValue = startingNumber // 2
                else: # odd
                    nextValue = startingNumber * 3 + 1

                collatz.append(nextValue)
                startingNumber = nextValue

    return collatz

    




'''
startingInteger = 1

while startingInteger != 0:
    startingInteger = int(input('What is starting integer: ') or 0)
    print(collatz(startingInteger))
'''

assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9 
assert len(collatz(257)) == 123

import random
random.seed(42)
for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum
    assert seq[-1] == 1
#'''
