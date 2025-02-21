## this program calculates a receiept for my coffee and muffin shop
## 
coffee = input ( "Number of coffees bought?" )
tea = input ( "Number of teas bought?" )
muffin = input ( "Number of muffins bought?" )
bagel = input ( "Number of bagels bought?" )
coffee = int(coffee)
coffeeTotal = coffee * 5
muffin = int(muffin)
muffinTotal = muffin * 4
tea = int(tea)
teaTotal = tea * 3
bagel = int(bagel)
bagelTotal = bagel * 5
total = coffeeTotal + muffinTotal + teaTotal + bagelTotal
taxTotal = total * .06
print('*************************************** \n My Coffee and Muffin Shop')
print("***************************************")
print("*************************************** \nMy Coffee and Muffin Shop Receipt")
print( coffee,"coffees at $5 each: $", coffeeTotal)
print( tea,"teas at $3 each: $", teaTotal)
print( muffin, "muffins at $4 each: $", muffinTotal)
print( bagel,"bagels at $5 each: $", bagelTotal)
print("6% tax: $", taxTotal)
print('---------')
print( "Total: $", taxTotal + total)
