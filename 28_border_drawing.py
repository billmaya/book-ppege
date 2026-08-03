# Exercise 28 - Border Drawing

def drawBorder(width, height):
    if width < 2 or height < 2:
        return

    print()
    for h in range(height):
        if h == 0 or h == height - 1:
            print('+', end = '')
            print('-' * (width - 2), end = '')
            print('+')
        else:
            print('|' + (' ' * (width - 2)) + '|')
    

width  = 2
height = 2

while width >= 2 or height >= 2:
    print('\nENTER RECTANGLE DIMENSIONS (Press <Enter> 2x to quit)') 
    width = int(input('Width? ') or 0)
    height = int(input('Height? ') or 0)
    print()
    
    drawBorder(width, height)
