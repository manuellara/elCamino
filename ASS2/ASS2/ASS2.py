###################################
# 
# CS 14 - Manuel Lara
# Assignment 2
# Loan Calculator 
#
# Algorithm 
# 
# STEP 1:
# 
# 
# 
# 
# STEP 2:
# 
# 
# 
# 
###################################

def intro( name ) :
    print( "\n\n\n\n\nLoan payment information for: {:>39s}" .format(name) )            #prints name statement 
    return

def P( p ) :
    print ("Loan amount: {:>57,.2f}" .format(p))                                       #prints loan amount statement
    return

def r( interestRate , numOfYears ) :
    n = numOfYears * 12
    r = interestRate / n                                                         #calculates annual monthly interest rate 
    print("Annual monthly interest rate will be: {:>32,.6f}%" .format(r) )
    return 

def n( numOfYears ) :
    n = numOfYears * 12                                                                #calculates amount of payment periods 
    print ("Amount of payments: {:>50,.0f}" .format(n) )
    return 

def A( p , interestRate , numOfYears ) :                                            #calculates payment amount 
    t = p + (p * interestRate)
    n = numOfYears * 12
    r = interestRate / n 
    a = ( r + 1 )**n
    mp = (p * ((r * a) /  (a - 1)))
    print ("Monthly payment amounts: {:>45,.2f}" .format(mp) )
    print ("Total cost of loan: {:>50,.2f}\n\n" .format(t) )                         
    return 

def table( p, interestRate , numOfYears ) :
    n = numOfYears * 12
    beginning = p
    print ( "Payment# {:>20} {:>20} {:>20} {:>20} {:>20}\n" .format("Beginning" , "Monthly Payment" , "Interest" , "Principal" , "Ending Balance") )
    for i in range(1 , int(n)+1 ) :
        t = p + (p * interestRate)
        n = numOfYears * 12
        r = interestRate / n 
        a = ( r + 1 )**n
        mp = (p * ((r * a) /  (a - 1)))

        mPayment = mp
        interest = beginning * r
        principal = mPayment - interest
        endBalance = beginning - principal
        print ( i, "{:>20,.2f} {:>20,.2f} {:>20,.4f} {:>20,.2f} {:>20,.2f}" .format(beginning , mPayment , interest , principal , endBalance) )
        beginning = endBalance

    return




name = input("Enter your name: ")
x = input("Would you like to create an amortization table (enter 'y' or 'n'): ")

if x == 'y' :
    p = float(input("Enter loan amount: "))
    if p <= 0 :
        print("Loan amount cannot be negative or 0")
        exit()
    elif p != float(p) :
        print("You did not enter a number...")
        exit()
    interestRate = float(input("Enter interest rate: "))
    if interestRate <= 0 :
        print ("Interest rate cannot be negative or 0")
        exit()
    elif interestRate != float(interestRate) :
        print("You did not enter a number...")
        exit()
    else :
        interestRate = interestRate /100
    numOfYears = float(input("How many years do you want to pay off loan? "))
    if numOfYears <= 0 :
        print("Number of years to pay off loan cannot be negative or 0")
        exit()
    elif numOfYears != float(numOfYears) :
        print("You did not enter a number...")
        exit()
elif x == 'n' :
    print ("Have a good day.")
    exit()
else :
    print("You will now exit...goodbye")
    exit()


intro( name )
P( p )
r( interestRate , numOfYears )
n( numOfYears )
A( p , interestRate , numOfYears )
table( p, interestRate , numOfYears )
