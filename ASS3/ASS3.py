#####################################################################
# Manuel Lara
# CS 14 - Assignemnt 3
#
# Algorithm 
#
# FUNCTION DEFINITIONS
#
# inputFile :
# takes 2 parameters : the filename and the output name
# open the fileName in 'read' mode
# open the output in 'write' mode
# reroute the print function to the output file
# initialize count , totalNet , avgCounter , highestNet , lowestNet to None , lowestName
# inititalize a 'for' loop to go through every line in the file
#   if the counter remainer is 0 only pick up the first line and CALL 'getName' and pass the line 
#   else CALL 'getIDSalary' and pass the line - set the return values to ID , salary , avgCount
#   CALL 'calculateTaxNet' and pass salary - set return values to tax , net
#   CALL 'output' and pass count , name , ID , salary tax , net
#   increment avgCounter with avgCount
#   if agvCount does not equal 0 , add net to totalNet
#   if count does not equal 0 , divide totalNet byt avgCounter to get avgNet
#   if net is greater that highestNet , set net to highestNet
#   if  lowestNet is None , set lowestNet to net
#   if net is less than lowest net and not negative , set net to lowestNet 
#   increment count by 1
# CALL 'findAverageHighestLowestNet' and pass avgNet , highestNet , highestName , lowestNet , lowestName
# close input file
# close output file
#
# getName :
# takes line as parameter 
# strips the right space and sets the result to name
# returns name
#
# getIDSalary : 
# takes line as parameter and splits it  
# stores variables in ID , salary 
# if ID's length is 4 and salary is grater than 0
#   set avgCount to 1
#   else  set avgCount to 0
# return ID , salary , avgCount 
# 
# calculateTaxNet :
# takes salary as a parameter 
# if salary <= 3500 : flatTax is 0 and tax  is 0%
# if 3500 < salary <= 8000 : flatTax is 0 and tax is 6%
# if 8000 < salary <= 20000 : flatTax is 270 and tax is 11% + 6% of 4500
# if 20000 < salary <= 34000 : flatTax is 1590 and tax 17% + 6% of 4500 + 11% of 12000
# if 34000 < salary <= 54000 : flatTax is 3970 and tax is 24% + 6% of 4500 + 11% of 12000 + 17% of 14000
# if 54000 < salary : flatTax is 8770 and tax is 32%+ 6% of 4500 + 11% of 12000 + 17% of 14000 + 24% of 20000
#
# findAverageHighestLowestNet :
# takes avgNet , highestNet , highestName , lowestNet , lowestName as paramenters 
# avg net income statement is printed 
# highestNet income statement is printed 
# lowestNet income statement is printed 
#
# output :
# takes count , name , ID , salary , tax , net as paramenters 
# if count is 1 , print the table header 
# if ID length is not 4 , print invalid statement 
# if salary is less than 0 , print invalid statement 
# if ID length is 4 and salary is greater than 0, print statement 
#
#
# MAIN
#
# prompt user to enter file path and store it in fileName
# prompt user to enter output file name and store it in outputName
# CALL 'inputFile' and pass fileName and outputFile
################################################################################


# FUNCTIONS #
def inputFile( fileName , outputName ) :
    inputFile = open(fileName , 'r')                                #open input file
    outputFile = open(outputName , 'w')                             #open output file
    sys.stdout = outputFile

    count = 0
    totalNet = 0.0
    avgCounter = 0
    highestNet = -1
    lowestNet = None
    lowestName = ""
    

    for line in inputFile :                                             #loops every line in file
        if count % 2 == 0 :                                             #checks to see whether line is even or odd
            name = getName( line )                                      #name function
        else :
            IDSalary = getIDSalary( line )                              #ID & salary function
            ID = IDSalary[0]
            salary = IDSalary[1]
            avgCount = IDSalary[2]                                      #gets a 0 or 1 to count
            
            taxNet = calculateTaxNet( salary )                          #taxes + net funtion 
            tax = taxNet[0]
            net = taxNet[1]
                 
            outPut( count , name , ID , salary , tax , net )            #file print statement // write to file

            avgCounter += avgCount                                      #counts all the valid input
    
            if avgCount != 0 :                                          #calculates total net
                totalNet += net

            if avgCounter != 0 :
                avgNet = totalNet / avgCounter                          #calculates avg net
 
            if net > highestNet:
                highestNet = net
                highestName = name                                      #finds highest net
            
            if lowestNet is None :                                      #finds lowest net
                lowestNet = net
                lowestName = name
            elif net < lowestNet and net > 0 :
                lowestNet = net 
                lowestName = name
                

        count += 1
    
    findAverageHighestLowestNet( avgNet , highestNet , highestName , lowestNet , lowestName )        #pring avg/high/low // write to file
    
    inputFile.close()
    outputFile.close()
    return

def getName( line ) :
    name = line.rstrip()
    return name

def getIDSalary( line ) :
    ID , salary = line.split(" ") 

    if len(ID) == 4 and float(salary) > 0 :
        avgCount = 1
    else :
        avgCount = 0

    return ID , float(salary) , avgCount

def calculateTaxNet( salary ) :
    if salary <= 3500:
        flatTax = 0
        tax = 0
        net = salary - (flatTax + tax)
    elif 3500 < salary <= 8000 :
        flatTax = 0;
        tax = (salary - 3500) * 6/100
        net = salary - (flatTax + tax)
    elif 8000 < salary <= 20000 :
        flatTax = 270;
        tax = (4500 * (6/100)) + ( (salary - 8000) * (11/100) )
        net = salary - (flatTax + tax)
    elif 20000 < salary <= 34000 :
        flatTax = 1590;
        tax = (4500 * (6 / 100)) + (12000 * (11 / 100)) + ((salary - 20000) * (17 / 100))
        net = salary - (flatTax + tax)
    elif 34000 < salary <= 54000 :
        flatTax = 3970
        tax = (4500 * (6 / 100)) + (12000 * (11 / 100)) + (14000 * (17 / 100)) + ((salary - 34000) * (24 / 100))
        net = salary - (flatTax + tax)
    elif 54000 < salary :
        flatTax = 8770
        tax = (4500 * (6 / 100)) + (12000 * (11 / 100)) + (14000 * (17 / 100))+ (20000 * (24/100)) + ((salary - 54000) * (32 / 100))
        net = salary - (flatTax + tax)
        
    return  tax , net

def findAverageHighestLowestNet( avgNet , highestNet , highestName , lowestNet , lowestName ) :
    
    print("\n\n{:<40} {:<20.2f}" .format( 'Avg Net Income' , avgNet) )
    print("{:<40} {:<20} {:<20.2f}" .format( 'Highest Net Income' , highestName , highestNet) )
    print("{:<40} {:<20} {:<20.2f}" .format( 'Lowest Net Income' , lowestName , lowestNet) )

    return


def outPut( count , name , ID , salary , tax , net ) :
    if count == 1 :
        print ("{:<20} {:<20} {:<20} {:<20} {:<20}" .format( 'Name' , 'ID' , 'Gross Income' , 'Taxes' , 'Net Income') )
        print("=" * 100)

    if len(ID) != 4 :
        print ("{:<20} {:<20} {:<20.2f} {:<20}" .format( name , ID , salary , '****INVALID ID') )

    if salary <= 0 :
        print ("{:<20} {:<20} {:<20.2f} {:<20}" .format( name , ID , salary , '****INVALID Salary') )

    if len(ID) == 4 and salary > 0 :
        print ("{:<20} {:<20} {:<20.2f} {:<20.2f} {:<20.2f}" .format( name , ID , salary , tax , net) ) 

    return

import sys
# MAIN #
fileName = input( "Drag a file in: " )                                      #comment out to automate - step 1
outputName = input("Enter output file name :" )

#fileName = "incomes.txt"                                                   #uncomment to automate - step 2

# FUNTION CALL #
inputFile( fileName , outputName )