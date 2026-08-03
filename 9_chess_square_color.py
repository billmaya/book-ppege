# Exercise 9 - Chess Square Color

def getChessSquareColor(column, row):
    if (column < 1 or column > 8) or (row < 1 or row > 8):
        return ''
    else:
        if column % 2 == row % 2:
            return 'white'
        else:
            return 'black'

def getChessSquareColor_ORIGINAL(column, row):
    if (column < 1 or column > 8) or (row < 1 or row > 8):
        return ''
    else:
        if isOdd(column):
            if isOdd(row):
                return 'white'
            else:
                return 'black'
        else:
            if isOdd(row):
                return 'black'
            else:
                return 'white'

def isOdd(number):
    return number % 2 == 1

def isEven(number):
    return number % 2 == 0


assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
