# Exercise 37 - Change Maker

def makeChange(amount):
   
    q = d = n = p = 0
    coins = {}
    
    if amount >= 25:
        q = amount // 25
        amount = amount % 25
        coins['quarters'] = q

    if amount >= 10:
        d = amount // 10
        amount = amount % 10
        coins['dimes'] = d

    if amount >= 5:
        n = amount // 5
        amount = amount % 5
        coins['nickels'] = n

    if amount > 0:
        p = amount
        coins['pennies'] = p

    #print(f'q: {q} d: {d} n: {n} p: {p}')

    return coins









'''
change = -1 

while change != 0:
    change  = int(input('Enter change to make: ') or 0) 
    #makeChange(change)
    coins = makeChange(change)
    print(coins) 

'''
assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}
#'''
