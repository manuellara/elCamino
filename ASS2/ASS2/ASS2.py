###################################
# 
# CS 14 - Manuel Lara
# Assignment 2
# Loan Calculator 
#
###################################

def intro( name ) :
    print( "\n\n\n\n\nLoan payment information for: {:>39s}" .format(name) )            #prints name statement 
    return

def P( p ) :
    print ("Loan amount: {:>57,.2f}" .format(p))                                       #prints loan amount statement
    return

def r( interestRate ) :
    r = interestRate / 12                                                              #calculates annual monthly interest rate 
    print("Annual monthly interest rate will be: {:>32,.4f}" .format(r) )
    return 

def n( numOfYears ) :
    n = numOfYears * 12                                                                #calculates amount of payment periods 
    print ("Amount of payment periods: {:>39,.0f}" .format(n) )
    return 

def A( p , interestRate , numOfYears ) :
    t = p + (p / interestRate)
    n = numOfYears * 12
    r = interestRate / 12
    x = (1+r)**n
    a = p * ( (r * x) / (x - float(1)) )                                               #calculates payment amount 
    print ("Payment amounts per period: {:>41,.2f}" .format(a) )
    print ("Numer of payments: {:>50,.2f}" .format(n) )
    print ("Total cost of loan: {:>50,.2f}" .format(t) )                         
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
r( interestRate )
n( numOfYears )
A( p , interestRate , numOfYears )