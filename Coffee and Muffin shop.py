## this program calculates a receiept for my coffee and muffin shop
coffee = input("Number of coffees bought?")
muffin = input("Number of muffins bought?")
coffee = int(coffee)
coffeeTotal = coffee * 5
muffin = int(muffin)
muffinTotal = muffin * 4
total = coffeeTotal + muffinTotal 
taxTotal = total * .06
print('*************************************** \n My Coffee and Muffin Shop')
print("***************************************")
print("*************************************** \nMy Coffee and Muffin Shop Receipt")
print( coffee,"coffees at $5 each: $", coffeeTotal)
print( muffin, "muffins at $4 each: $", muffinTotal)
print("6% tax: $", taxTotal)
print('---------')
print( "Total: $", taxTotal + total)
