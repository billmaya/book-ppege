# Exercise 34 - Uppercase Letters

def getUppercase(text):
    
    upper = ''

    for i in range(len(text)):

        c = text[i]
        if (97 <= ord(c) <= 122): # a-z
            upper += chr(ord(c) - 32) # A-Z
        else:
            upper += c # Just copy it over

    return upper



'''
text = 'placeholder'

while text != '':
    text = input('Enter text to capitalize: ') or ''
    upper = getUppercase(text)
    print(upper) 
'''


assert getUppercase('Hello') == 'HELLO'
assert getUppercase('hello') == 'HELLO'
assert getUppercase('HELLO') == 'HELLO'
assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
assert getUppercase('12345') == '12345'
assert getUppercase('') == ''
