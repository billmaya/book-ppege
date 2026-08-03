# Exercise 21 - Validate Date

def isValidDate(year, month, day):
    import leap_year

    # Cleaned it up a bit 
    match month:
        case 1|3|5|7|8|10|12:
            if (1 <= day <= 31):
                return True
            return False
        case 4|6|9|11:
            if (1 <= day <= 30):
                return True
            return False
        case 2:
            if leap_year.isLeapYear(year):
                if (1 <= day <= 29):
                    return True
            elif (1 <= day <= 28):
                return True
            return False
        case _:
            return False

    # My original implementation
    '''
    if month < 1 or month > 12:
        return False

    match month:
        case 1|3|5|7|8|10|12:
            if day < 1 or day > 31:
                return False
            else:
                return True
        case 4|6|9|11:
            if day < 1 or day > 30:
                return False
            else:
                return True
        case _:
            if day < 1:
                return False
            else:
                if leap_year.isLeapYear(year):
                    if day > 29:
                        return False
                    else:
                        return True
                else:
                    if day > 28:
                        return False
                    else:
                        return True
   ''' 





assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000,1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False
#'''
import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days = 1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay
#'''
