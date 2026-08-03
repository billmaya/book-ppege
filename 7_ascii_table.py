# Exercise 7 - ASCII Table

def printAsciiTable(lowerLimit=32, upperLimit=126):
    print(end='\n\n')

    counter = 0
    lowerLimit = int(lowerLimit)
    upperLimit = int(upperLimit) + 1

    for x in range(lowerLimit, upperLimit, 1):
        counter = counter + 1
        if counter == 10:
            print(f'  {x:03}: {chr(x)}', end='\n\n')
            counter = 0
        else:
            print(f'  {x:03}: {chr(x)}', end='')
    print('',end='\n\n')

raw = input("ASCII table lower and upper limits? (Enter to use 32 and 126 as defaults): ").strip() or '32 126'

lowerLimit, upperLimit = raw.split()

printAsciiTable(lowerLimit, upperLimit)
