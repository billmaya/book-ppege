# Exercise 35 - Title Case

def getTitleCase(text):

    entitled = ''
    is_separator = False # Separator before character? 

    for i in range(len(text)):

        c = text[i]
        if c.isalpha():
            if i == 0 or is_separator: # First character or space before current character
                if (97 <= ord(c) <= 122): # a-z -> A-Z
                    entitled += c.upper()
                else:
                    entitled += c

                is_separator = False
            else:
                if (65 <= ord(c) <= 90): # A-Z
                    entitled += c.lower()
                else:
                    entitled += c
        else:
            entitled += c
            is_separator = True

    return entitled








'''
text = 'placeholder'

while text != '':
    text = input('Enter text to title case: ') or ''
    entitled = getTitleCase(text)
    print(entitled) 

'''
assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

import random
random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
for i in range(1000):
    random.shuffle(chars)
    assert getTitleCase(''.join(chars)) == ''.join(chars).title()

#'''
