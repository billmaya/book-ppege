# Exercise 36 - Reverse String

def reverseString(text):
    
    ''' # This works but I don't think it is what they're looking for
    l = list(text)
    l.reverse()
    r = ''.join(l)
    return r
    '''

    l = list(text)
    for i in range(len(l) // 2):
        #print(f'{i}: {l[i]}')
        m = len(l) - 1 - i
        l[i], l[m] = l[m], l[i]

    r = ''.join(l)
    return r
    





'''
text = 'placeholder'

while text != '':
    text = input('Enter text to reverse: ') or ''
    reversed = reverseString(text)
    print(reversed) 

'''
assert reverseString('Hello') == 'olleH'
assert reverseString('') == ''
assert reverseString('aaazzz') == 'zzzaaa'
assert reverseString('xxxx') == 'xxxx'
#'''
