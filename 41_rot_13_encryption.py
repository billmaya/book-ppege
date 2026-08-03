# Exercise 41 - ROT 13 Encryption

def rot13(text):

    crypted = ''

    for c in range(0, len(text)):
        cc = text[c]

        if cc.isalpha():
            
            if cc.islower():
                minusAt = 110
            else:
                minusAt = 78

            occ = ord(cc)
            if occ >= minusAt:
                noc = occ - 13
            else:
                noc = occ + 13

            nc = chr(noc)

            crypted += nc

        else:
            crypted += cc

    return crypted






'''
text = 'placeholder' 

while text != '': 
    text = input('Enter text to encrypt: ')
    print(text)
    print(rot13(text))

'''
#'''
assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
#'''

