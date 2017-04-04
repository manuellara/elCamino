###################################
# 
# CS 14 - Manuel Lara
# Assignment 2
# Loan Calculator 
#
# Algorithm 
# 
# 
# STEP 1: INPUT
# prompt user for name
# prompt user if they would like to create an ammortization table with either 'y' or 'n'
# error checking :: if 'n', the program will exit. if not 'y' or 'n', the program will exit. if 'y', the program proceeds 
# prompt user to enter loan amount
# error checking :: if input is less than 0 or not a number, the program will exit. if it is, the program proceeds 
# prompt user for interest rate
# error checking :: if input is less than 0 or not a number, the program will exit. if it is, the program proceeds to divide interest rate by 100 to convert to decimal 
# prompt user to enter amount of years they want to pay off loan
# error checking :: if input is less than 0 or not a number, the program will exit.
# 
# 
# STEP 2: PROCESS
# define the first function and pass the name parameter to it
# include a print statement with a discription + name
# define the next function and pass the loan amount parameter to it
# include a print statement with a discription + loan amount
# define the third function and pass interest rate and number of years to pay off loan
# set a variable to to find total amount of months ( years * 12 )
# set another variable to find monthly interest rate ( interest rate / total months )
# include print statement with a discription + monthly interest rate 
# define fourth function and pass number of years to it
# set a variable to get total months ( years * 12 )
# include print statement with discription + total months 
# define fifth function and pass loan amount , interest rate , years to pay loan
# set a variable to get total loan amount after interest ( loan + ( loan * interest ) )
# set a variable to get total amount of months ( years * 12 )
# set variable to get monthly interest rate ( interest rate / total months )
# set a variable to get part of the formula ( monthly rate + 1 ) ^ total months
# set variable to get monthly payment ( loan amount * (montly rate * previus variable) / (previous variable - 1) )
# include print statements with discription + monthly payments 
# include print statements with discription + total cost of loan
# define sixth function and pass loan amount , interest rate , years to pay loan
# set variable to get total amount of months ( years * 12 )
# set a variable to the loan amount
# include a heading print statement that includes payment , beginning , monthly payment , interest , principal , ending balance
# start a for loop from 1 to the amount of months + 1 
# set variable to get total loan amount after interest rate  ( loan amount + (loan amount * interest rate) )
# set variable to get total months ( years / 12 )
# set variable to get monthly interest rate ( interest rate / total months )
# set a variable to get part of the formula ( monthly rate + 1 ) ^ total months
# set variable to get monthly payment ( loan amount * (montly rate * previus variable) / (previous variable - 1) )
# set variable to monthly payment 
# set variable to loan amount * monthly interest rate
# set variable to monthly payment - interest 
# set variable to loan amount - principal 
# include print statement to print counter ( payment # ) , beginning , monthly payment , interest , principal , ending balance 
# set a reset variable to set end balance to beginning   
# 
# 
# STEP 3 : OUTPUT
# call first function and pass name parameter 
# call second function and pass loan amount paramter 
# call third function and pass interest rate , number of years 
# call fourth function and pass number of years 
# call fifth function and pass loan amount , interest rate , number of years 
# call sixth function and pass loan amount , interest rate , and number of years 
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

def A( p , interestRate , numOfYears ) :                                             
    t = p + (p * interestRate)
    n = numOfYears * 12
    r = interestRate / n 
    a = ( r + 1 )**n
    mp = (p * ((r * a) /  (a - 1)))                                             #calculates payment amount
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