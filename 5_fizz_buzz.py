# Exercise 5 - Fizz Buzz

upTo = int(input("What is the upper limit? "))

print(f'Numbers in the range of 1 to {upTo} will be printed', end='\n\n')
print("A number that can only be divided by 3 will be replaced with 'Fizz'")
print("A number that can only be divided by 5 will be replaced with 'Buzz'")
print("A number that can be divided by 3 and 5 will be replaced with 'FizzBuzz'", end='\n\n')

for i in range(1, upTo + 1): # Need to add 1 to upTo because range() will stop at upper limit - 1
    if i % 3 == 0:
        if i % 5 == 0:
            i = 'FizzBuzz'
        else:
            i = 'Fizz'
    elif i % 5 == 0:
        i = 'Buzz'
    else:
        i = str(i)
    print(i, end=' ')
