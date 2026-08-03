# Exercise 19 - Password Generator

LOWER_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPER_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SPECIAL = ['~', '!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+']

def isPasswordValid(password):
    hasLowercase = False
    hasUppercase = False
    hasNumber = False
    hasSpecial = False

    for character in password:
        if character in LOWER_LETTERS:
            hasLowercase = True
        if character in UPPER_LETTERS:
            hasUppercase = True
        if character in NUMBERS:
            hasNumber = True
        if character in SPECIAL:
            hasSpecial = True

    if hasLowercase and hasUppercase and hasNumber and hasSpecial:
        return True
    else:
        return False

def generatePassword(length):
    import random

    if length < 12:
        length = 12

    validCharacters = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
    random.shuffle(validCharacters)

    passwordValid = False

    while passwordValid == False:
        password = []

        for i in range(length):
            # At first I tried to get fancy, choosing from random ASCII table values
            # r = random.randint(*random.choice([(33, 33), (35, 38), (40, 43), (95, 95), (97, 122), (65, 90), (48, 57)]))
            # password += chr(r)
            password.append(random.choice(validCharacters))
      
        passwordValid = isPasswordValid(''.join(password))

#    print(''.join(password))
    return ''.join(password)



#'''
assert len(generatePassword(8)) == 12

pw = generatePassword(14)
assert len(pw) == 14

hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False

for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True

#print(f'hasLowercase: {hasLowercase}')
#print(f'hasUppercase: {hasUppercase}')
#print(f'hasNumber: {hasNumber}')
#print(f'hasSpecial: {hasSpecial}')

assert hasLowercase and hasUppercase and hasNumber and hasSpecial
#'''
