
# FUNCTIONS #
def inputFile( fileName ) :
    inputFile = open(fileName , 'r')
    count = 0
    for line in inputFile :                                          #loops every line in file
        if count % 2 == 0 :                                          #checks to see whether line is even or odd
            name = getName( line )                                      #name function
        else :
            IDSalary = getIDSalary( line )                               #ID & salary function
            ID = IDSalary[0]
            salary = IDSalary[1]
            
            taxNet = calculateTaxNet( salary )                          #taxes + net funtion 
            tax = taxNet[0]
            net = taxNet[1]
                 
            outPut( count , name , ID , salary , tax , net  )           #file output

        count += 1
    inputFile.close()
    return

def getName( line ) :
    name = line
    return name

def getIDSalary( line ) :
    ID , salary = line.split(" ") 
    return ID , float(salary)

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


def outPut( count , name , ID , salary , tax , net  ) : 
    if count == 1 :
        print ("{:<20} {:<20} {:<20} {:<20} {:<20}" .format( 'Name' , 'ID' , 'Gross Income' , 'Taxes' , 'Net Income') )
        print("=" * 100) 

    if len(ID) != 4 :
        print ("{:<20} {:<20} {:<20.2f} {:<20}" .format( name.rstrip() , ID , salary , '****INVALID ID') ) 

    if salary <= 0 :
        print ("{:<20} {:<20} {:<20.2f} {:<20}" .format( name.rstrip() , ID , salary , '****INVALID Salary') )

    if len(ID) == 4 and salary > 0 :
        print ("{:<20} {:<20} {:<20.2f} {:<20.2f} {:<20.2f}" .format(name.rstrip() , ID , salary , tax , net) )

    return 
  

# MAIN #
#fileName = input( "Enter a filename: " )
fileName = "incomes.txt"

# FUNTION CALLS #
inputFile( fileName )