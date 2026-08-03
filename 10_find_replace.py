# Exercise 10 - Find Replace

def findAndReplace(text, oldText, newText):
    verbose = True

    replacedText = ''
    textLength = len(text)
    oldTextLength = len(oldText)

    index = 0
    while index < textLength:
        textToExamine = text[index: index + oldTextLength] 
        if textToExamine == oldText:
            replacedText += newText
            index = index + len(oldText)
        else:
            replacedText += text[index: index + 1]
            index = index + 1
        
        if verbose:
            print('COMPARE ' + textToExamine + ' WITH ' + oldText + ' RESULTS IN ' + replacedText)
    
    if verbose:
        print()

    return replacedText


assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
