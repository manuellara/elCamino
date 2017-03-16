###############################s
# 
# Assignment 1 
# Manuel Lara
# Computer Science 14
#
###############################



def function1( amountOfYears ):
    global interestRate

    if amountOfYears >= 5:
        interestRate = 4.5
    elif 5 > amountOfYears >= 4: 
         interstRate = 4
    elif 4 > amountOfYears >= 3:
        interestRate = 3.5
    elif 3 > amountOfYears >= 2:
        interestRate = 2.5
    elif 2 > amountOfYears >= 1:
        interestRate = 2
    elif amountOfYears < 1:
        interestRate = 1.5
     
    return interestRate
 
        
def function2( amountOfMoney, amountOfYears, interestRate ): 
    global moneyAccumulated

    moneyAccumulated = amountOfMoney * ( 1 + ( (interestRate/4 ) ** (4*6) ) )

    return moneyAccumulated

def function3(amountOfMoney, amountOfYears, interestRate, moneyAccumulated):
    print("%8.2f is in deposit" % (amountOfMoney) )
    print("%1.0f years in deposit" % (amountOfYears))
    print("%1.1f interest" % (interestRate))
    print("%8.2f was accumulated" % (moneyAccumulated))
 

interestRate = 0
moneyAccumulated = 0
amountOfMoney = int(input("How much money is in deposit? "))
amountOfYears = int(input("How many years has it been? ")) 

function1( amountOfYears )
function2( amountOfMoney, amountOfYears, interestRate )
function3(amountOfMoney, amountOfYears, interestRate,  moneyAccumulated)
