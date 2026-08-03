# Exercise 33 - Comma Formatted Numbers

def commaFormat(number):
    
    s = str(number)     # number to string
    is_d = False        # does decimal exist?
    d = ''              # decimal part on number
    w = ''              # whole part of number
    sc = ''             # number with commas

    if '.' in s: # s.find('.') != -1:
        is_d = True
        d = s[s.find('.'):]
        w = s[0:s.find('.')]
    else:
        w = s

    #print('Number: ' + s + ' Whole: ' + w + ' Decimal: ' + d)

    if is_d:
        sc = d + sc

    lw = len(w)

    dgtc = 0               # digit counter

    for dgt in range(lw - 1, -1, -1):
        dgtc += 1
        sc = w[dgt] + sc 

        if dgtc  == 3 and dgt != 0:
            sc = ',' + sc
            dgtc = 0

    #print('Number with commas: ' + sc + '\n')

    return sc





'''
commaFormat(1)
commaFormat(10)
commaFormat(100)
commaFormat(1000)
commaFormat(10000)
commaFormat(100000)
commaFormat(1000000)
commaFormat(1234567890)
commaFormat(1000.123456)
'''

assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'





