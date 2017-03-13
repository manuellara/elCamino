#########################
# HW3 - fruit vendor
# Manuel Lara
#########################

apples = .65
oranges = .90
bananas = .70

x = float( input("How many Apples would you like to buy? ") )
y = float( input("How many Oranges would you like to buy? ") )
z = float( input("How many Bananas would you like to buy? ") )

totalApples = x * apples
totalOranges = y * oranges
totalBananas = z * bananas

total = totalApples + totalBananas + totalOranges


print("\n\n\n\n\n\n")
print ("BOB'S FRUIT GROCERY INVOICE")
print ("-" * 60 )
print("     ", x , " Apples @ .65 each = %8.2f" % (totalApples) )
print("     ", y , " Oranges @ .90 each = %8.2f" % (totalOranges) )
print("     ", z , " Bananas @ .70 each = %8.2f" % (totalBananas) )
print(" " * 20, "-" * 20 )
print(" " * 30, "$ %8.2f" % (total) )