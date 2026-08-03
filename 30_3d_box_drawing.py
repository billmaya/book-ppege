# Exercise 30 - 3d Box Drawing

def drawBox(side):
    if side < 1:
        return

    emptySpace = ' '
    
    # Top line
    print((emptySpace * (side + 1)) + '+' + ('-' * (side * 2)) + '+')
    
    # Top surface & side
    for i in range(side, 0, -1):
        print((emptySpace * i) + '/' + (emptySpace * (side * 2)) + '/' + (emptySpace * (side - i)) + '|')
   
    # Middle line & side
    print('+' + '-' * (side * 2) + '+' + (emptySpace * side) + '+')
    
    # Front surface & side
    for i in range(side, 0, -1):
        print('|' + (emptySpace * (side * 2)) + '|' + (emptySpace * (i - 1)) + '/') 
    
    # Bottom line
    print('+' + '-' * (side * 2) + '+')







side = 1

while side >= 1:
    print('\nENTER ONE NUMBER FOR BOX WIDTH, LENGTH &  HEIGHT (Press <Enter> to quit)') 
    side = int(input('Box Side? ') or 0)
    print()
    
    drawBox(side)
