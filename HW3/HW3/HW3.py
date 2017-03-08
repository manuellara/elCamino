#########################
# HW3 - fruit vendor
# Manuel Lara
#########################


apples = .65
oranges = .90
bananas = .70

x = int( input("How many Apples would you like to buy? ") )
y = int( input("How many Oranges would you like to buy? ") )
z = int( input("How many Bananas would you like to buy? ") )

totalApples = x * apples
totalOranges = y * oranges
totalBananas = z * bananas

total = totalApples + totalBananas + totalOranges


print("\n\n\n\n\n\n")
print ("BOB'S FRUIT GROCERY INVOICE")
print ("-" * 60 )
print("     ",x , " Apples @ .65 each = ", round(totalApples, 2) )
print("     ",y , " Oranges @ .90 each = ", round(totalOranges, 2) )
print("     ",z , " Bananas @ .70 each = ", round(totalBananas, 2) )
print(" " * 20, "-" * 20 )
print(" " * 30, round(total, 2) )