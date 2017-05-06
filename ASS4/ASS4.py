# FUNCTIONS #
def inputFile( fileName , outputName ) :
    inputFile = open(fileName , 'r')                                #open input file
    outputFile = open(outputName , 'w')                             #open output file
    sys.stdout = outputFile                                        #uncomment to write to file

    count = 0
    totalNet = 0.0
    avgCounter = 0
    highestNet = -1
    lowestNet = None
    lowestName = ""
    
    nameList = list()
    idList = list()
    salList = list()
    taxList = list()
    netList = list()
    

    for line in inputFile :                                             #loops every line in file
        if count % 2 == 0 :                                             #checks to see whether line is even or odd
            name = getName( line )                                      #name function
        else :
            IDSalary = getIDSalary( line )                              #ID & salary function
            ID = IDSalary[0]
            salary = IDSalary[1]
            avgCount = IDSalary[2]                                      #gets a 0 or 1 to count
            
            taxNet = calculateTaxNet( salary )                          #taxes + net function 
            tax = taxNet[0]
            net = taxNet[1]

            nameList.append(name)                                       #adding each element to appropriate list 
            idList.append(ID)
            salList.append(salary)
            taxList.append(tax)
            netList.append(net)
              
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
            
            outPut( count , name , ID , salary , tax , net )            #file print statement // write to file

        count += 1

    outPut( count , name , ID , salary , tax , net )                           #file print statement // write to file
    sorting( nameList , idList , salList , taxList , netList )
    findAverageHighestLowestNet( avgNet , highestNet , highestName , lowestNet , lowestName )        #print avg/high/low // write to file

      
    inputFile.close()
    outputFile.close()
    return

def sorting( nameList , idList , salList , taxList , netList ) :
    import operator                                                        
    data = list(zip( nameList , idList , salList , taxList , netList ) )          #zips all lists together, stores it in data
    data.sort( key = operator.itemgetter(0) )                                      #sorts data by element  (nameList)
    
    print("\nSorted Alphabetically\n")
    print ("{:<20} {:<20} {:<20} {:<20} {:<20}" .format( 'Name' , 'ID' , 'Gross Income' , 'Taxes' , 'Net Income') )
    print("=" * 100)
    for i in range( len(data) ) :
        name , id , sal , tax , net = data[i]                                   #splits data 
        if len(id) != 4 :
            print ("{:<20} {:<20} {:<20.2f} {:<20}" .format( name , id , sal , '****INVALID ID') )

        if sal <= 0 :
            print ("{:<20} {:<20} {:<20.2f} {:<20}" .format( name , id , sal , '****INVALID Salary') )

        if len(id) == 4 and sal > 0 :
            print ("{:<20} {:<20} {:<20.2f} {:<20.2f} {:<20.2f}" .format( name , id , sal , tax , net) )

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

def outPut( count , name , ID , salary , tax , net ) :
    if count == 1 :
         print ("\nNot Sorted\n")
         print ("{:<20} {:<20} {:<20} {:<20} {:<20}" .format( 'Name' , 'ID' , 'Gross Income' , 'Taxes' , 'Net Income') )
         print("=" * 100)
    if len(ID) != 4 :
        print ("{:<20} {:<20} {:<20.2f} {:<20}" .format( name , ID , salary , '****INVALID ID') )

    if salary <= 0 :
        print ("{:<20} {:<20} {:<20.2f} {:<20}" .format( name , ID , salary , '****INVALID Salary') )

    if len(ID) == 4 and salary > 0 :
        print ("{:<20} {:<20} {:<20.2f} {:<20.2f} {:<20.2f}" .format( name , ID , salary , tax , net) ) 

    return

def findAverageHighestLowestNet( avgNet , highestNet , highestName , lowestNet , lowestName ) :
    
    print("\n\n{:<40} {:<20.2f}" .format( 'Avg Net Income' , avgNet) )
    print("{:<40} {:<20} {:<20.2f}" .format( 'Highest Net Income' , highestName , highestNet) )
    print("{:<40} {:<20} {:<20.2f}" .format( 'Lowest Net Income' , lowestName , lowestNet) )

    return

import sys
# MAIN #
fileName = input( "Drag a file in: " )                                      #comment out to automate - step 1
outputName = input("Enter output file name :" )

#fileName = "incomes.txt"                                                   #uncomment to automate - step 2

# FUNTION CALL #
inputFile( fileName , outputName )                                         