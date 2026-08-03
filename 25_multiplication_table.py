# Exercise 25 - Multiplication Table

print('  |',end = '')
for c in range(1, 11):
    print(f'{str(c).rjust(2)} ', end = '')
print()

print('--+------------------------------')

for c in range(1, 11):
    print(f'{str(c).rjust(2)}|', end = '')
    for r in range(1, 11):
        print(f'{str(c * r).rjust(2)} ', end = '')
    print()


