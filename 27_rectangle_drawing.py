# Exercise 27 - Rectangle Drawing

def drawRectangle(width, height):
    if width < 1 or height < 1:
        return

    print()
    for h in range(height):
        for w in range(width):
            print('#',end = '')

        print()

width = 1
height = 1

while width >= 1 or height >= 1:
    print('\nENTER RECTANGLE DIMENSIONS (Press <Enter> 2x to quit)') 
    width = int(input('Width? ') or 0)
    height = int(input('Height? ') or 0)
    print()
    
    drawRectangle(width, height)
