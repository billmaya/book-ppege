# Exercise 29 - Pyramid Drawing

def drawPyramid(height): 
    if height < 2:
        return
    
    # This was the book's solution
    '''
    for rowNumber in range(height):
        leftSideSpaces = ' ' * (height - (rowNumber + 1))
        pyramidRow = '#' * (rowNumber * 2 + 1)
        print(leftSideSpaces + pyramidRow)
    '''

    # This is my modified solution after I read the book's solution
    for row in range(height):
        spacesToAdd = ' ' * (height - (row + 1))
        hashesToAdd = '#' * ((row * 2) + 1)

        pyramidRow = spacesToAdd + hashesToAdd
        print(pyramidRow)

    # This was my original solution 
    '''
    baseWidth = (height * 2) - 1 
    sideWidth = baseWidth // 2 

    for rows in range(height):
            hashesToAdd = rows
            spacesToAdd = sideWidth - hashesToAdd
            
            pyramidString = ''
            pyramidString = ((' ' * spacesToAdd) + 
                             ('#' * hashesToAdd) + 
                             '#' + 
                             ('#' * hashesToAdd)) #+ 
                             #(' ' * spacesToAdd))
            print(pyramidString)
    '''




height = 2

while height >= 2:
    print('\nENTER PYRAMID HEIGHT (Press <Enter> to quit)') 
    height = int(input('Height? ') or 0)
    print()
    
    drawPyramid(height)
