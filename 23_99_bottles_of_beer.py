# Exercise 23 - 99 Bottles Of Beer

def printStanza(bottles):
    stanza = (f'{bottles} bottle{"s" if bottles != 1 else ""} of beer on the wall,\n'
              f'{bottles} bottle{"s" if bottles != 1 else ""} of beer,\n'
              f'Take one down,\n'
              f'Pass it around,')

    print(stanza)

    if bottles - 1 == 0:
        print('No more bottles of beer on the wall!\n')
    else:
        print(f'{bottles - 1} bottle{"s" if bottles - 1 != 1 else ""} of beer on the wall,\n')





for i in range(99, 0, -1):
    printStanza(i)

