# Exercise 18 - Buy 8, Get 1 Free

def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    discountCount = 0
    totalCoffeeCost = 0

    while numberOfCoffees > 0:
        #print(f'{numberOfCoffees} {discountCount} {totalCoffeeCost}')

        numberOfCoffees -= 1
        if discountCount == 8:
            discountCount = 0
        else:
            discountCount += 1
            totalCoffeeCost += pricePerCoffee
    
    #print(totalCoffeeCost)
    return totalCoffeeCost
    
''' Original implementation - 10 was the outlier
    coffeesForDiscount = 8

    freeCoffeeAvailable = 0
    freeCoffeeTaken = 0

    if numberOfCoffees // coffeesForDiscount == 0:
        return (numberOfCoffees % coffeesForDiscount) * pricePerCoffee
    else:
        freeCoffeeAvailable = numberOfCoffees // coffeesForDiscount
        freeCoffeeTaken = numberOfCoffees % coffeesForDiscount

        return (numberOfCoffees - (freeCoffeeTaken)) * pricePerCoffee
    '''

assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50

for i in range(1, 4):
   assert getCostOfCoffee(0, i) == 0
   assert getCostOfCoffee(8, i) == 8 * i
   assert getCostOfCoffee(9, i) == 8 * i
   assert getCostOfCoffee(18, i) == 16 * i
   assert getCostOfCoffee(19, i) == 17 * i
   assert getCostOfCoffee(30, i) == 27 * i
 
