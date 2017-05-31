##################
#
# Final Project CS 14
# Manuel Lara
#
#
#
#
#
#
#
#################

class student:
    def __init__( self , firstName , lastName , id , avg , letterGrade ):            #student class 
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.avg = avg
        self.letterGrade = letterGrade

def menu( outputFileName , students , title , course , location ):
    print("\nHello! Welcome to the menu!\n\nWhat would you like to do?\n")              #
    print ("a.) Print out all the students to file & monitor\n\n")                      #
    print ("b.) Sort students alphabetically by last name\n\n")                         #
    print ("c.) Sort students by average\n\n")                                          #Displays Menu 
    print ("d.) Add student\n\n")                                                       #
    print ("e.) Remove student by last name\n\n")                                       #
    print ("f.) Edit student by last name\n\n")
    print ("x.) Exit\n\n")

    m = waitForChar()                                                                   #waits for char to be entered 

    if m == 'a' or m == 'A' :
        printStatememt( outputFileName , students , title , course , location )
        time.sleep(5)
        os.system('cls')
        return menu( outputFileName , students , title , course , location )
    elif m == 'b' or m == 'B' :
        sortAlphabetically( students )
        time.sleep(5)
        os.system('cls')
        return menu( outputFileName , students , title , course , location )
    elif m == 'c' or m == 'C' :
        sortByGrade( students )
        time.sleep(5)
        os.system('cls')
        return menu( outputFileName , students , title , course , location )
    elif m == 'd' or m == 'D' :
        students = addStudent( students )
        time.sleep(5)
        os.system('cls')
        return menu( outputFileName , students , title , course , location )
    elif m == 'e' or m == 'E' :
        students = removeStudent( students )
        time.sleep(5)
        os.system('cls')
        return menu( outputFileName , students , title , course , location )
    elif m == 'f' or m == 'F' :
        students = editStudent( students )
        time.sleep(5)
        os.system('cls')
        return menu( outputFileName , students , title , course , location )
    elif m == 'x' or m == 'X' :
        exit()
    else :
        print("Not an option , try again...\n\n")
        time.sleep(3)
        os.system('cls')
        menu( outputFileName , students , title , course , location )       

def waitForChar() :
    m = input()
    print("\n\nYou selected '" + m[0] + "'\n\n")
    return m[0]

def readInFile() :
    #fileName = input("Enter the file path: ")                                      #comment out to automate 
    fileName = "FinalS17.txt"                                                       #comment out for real program 
    if os.path.isfile(fileName):
        #outputFileName = input("\n\nEnter an output file name: ")
        outputFileName = "test.txt"
        return fileName , outputFileName
    else :
        print ("\n\nFile does not exist , try again...\n ")
        return readInFile()

def readFile( fileName ) :
    fin = open( fileName , 'r' )

    students = []                                                                   #creates list called students 

    title = fin.readline()                                                          #reads 1st line as title of course  
    course = fin.readline()                                                         #reads 2nd line as the course
    location = fin.readline()                                                       #reads 3rd line as location

    for line in fin :
        name = line                                                                 #reads line and store it as 'name'
        fName , lName = name.split(" " , 1)                                         #split the name to 'fName' , 'lName'
        data = fin.readline()                                                       #read the data line
        id , qs , s1 ,s2 , s3 , s4 , s5 , s6 = data.split()                         #split up data 
        
        avg , lGrade , list = calcScore( qs , s1 , s2 ,s3 , s4 , s5 , s6 )                   #gets 'avg' , 'lGrade'

        record = {'firstName' : fName , 'lastName' : lName , 'id' : id , 'avg' : avg , 'grade' : lGrade , 'quiz' : qs , 'testList' : list }       #creates dictionary record 

        students.append(record)                                                     #appends dictionary to list
    
    fin.close()                                                                     #closes fin

    return students , title , course , location

def calcScore( qs , s1 , s2 ,s3 , s4 , s5 , s6 ) :
    list = [ int(s1) , int(s2) , int(s3) , int(s4) , int(s5) , int(s6) ]
    list.sort(reverse = True)
    list.pop()                                                                            #drops lowest test score
    
    testScore = (sum(list)/500) * 90                                                      #calculates avg
    quizScore = (int(qs)/100) * 10

    avg = testScore + quizScore

    if 100 >= avg > 90 :                                                                  #calculated lGrade
        lGrade = 'A'
    elif 80 <= avg < 89.99 :
        lGrade = 'B'
    elif 70 <= avg < 79.99 :
        lGrade = 'C'
    elif 60 <= avg < 69.99 :
        lGrade = 'D'
    elif 50 <= avg < 59.99 :
        lGrade = 'F'
    else :
        lGrade = 'I'

    return avg , lGrade , list

def printStatememt( outputFileName , students , title , course , location ) :
                                                                                                #
    print ("{:<25}{:<10}{:<5}" .format( 'Name' , 'Average' , 'Grade' ) )                        #
    print("=" * 40)

    for i in students :                                                                         #iterates through list of students 
        print("{:<25}{:<10.2f}{:<5}" .format( i['firstName'] + " " + i['lastName'].rstrip() , i['avg'] , i['grade'] ) )                     #print statement 
    
    outputFile( outputFileName , students , title , course , location )                         #prints to file

    return

def outputFile( outputFileName , students , title , course , location ) :
    fout = open( outputFileName , 'w' )                                                                #opens output file
    
    fout.write("{:<35}{:<60}\n" .format( 'Course Name : ' , title.rstrip() ) )                         #
    fout.write("{:<35}{:<45}\n" .format('Fundamentals Course ID : ' , course.rstrip() ) )              #
    fout.write("{:<35}{:<45}\n\n" .format( 'Location : ' , location.rstrip() ) )                       #prints header

    fout.write("{:<25}{:<25}{:<10}{:<5}\n" .format( 'Name' , 'ID' , 'Average' , 'Grade' ) )
    fout.write("=" * 65 + "\n")

    for i in students : 
        fout.write("{:<25}{:<25}{:<10.2f}{:<5}\n" .format( i['firstName'] + " " + i['lastName'].rstrip() , "***-**-" + i['id'][5:] , i['avg'] , i['grade'] ) )

    fout.close()

    return

def sortAlphabetically( students ) :
    students.sort( key = operator.itemgetter('lastName') )                                                  #sorts students by last name

    print ("{:<25}{:<10}{:<5}" .format( 'Name' , 'Average' , 'Grade' ) )                        
    print("=" * 40)

    for i in students :                                                                        
        print("{:<25}{:<10.2f}{:<5}" .format( i['lastName'].rstrip() + ", " + i['firstName'] , i['avg'] , i['grade'] ) )
            
    return 

def sortByGrade( students ) :
    students.sort( key = operator.itemgetter('avg') , reverse = True )                              #sorts student by average

    print ("{:<25}{:<10}{:<5}" .format( 'Name' , 'Average' , 'Grade' ) )
    print("=" * 40)

    for i in students :                                                                        
        print("{:<25}{:<10.2f}{:<5}" .format( i['firstName'] + " " + i['lastName'].rstrip() , i['avg'] , i['grade'] ) )
            
    return 

def addStudent( students ) :

    fName = input("\n\nEnter FIRST name: ")                         #enter first name
    lName = input("\n\nEnter LAST name: ")                          #enter last name

    id = input("\n\nEnter 9-DIGIT ID: ")                            #enter ID
    id = idChecker( id )                                            #ID checker

    qs = input("\n\nEnter QUIZ score ")                             #enter quiz score 
    qs = qsChecker( qs )                                            #quiz score checker 

    tScores = input("\n\nEnter 6 TEST SCORES separated with 1 space: ")
    s1 , s2 , s3 , s4 , s5 , s6 = tScores.split()
    s1 , s2 , s3 ,s4 , s5 , s6 = scoreChecker( s1 , s2 , s3 , s4 , s5 , s6 )
    
    avg , lGrade , list = calcScore( qs , s1 , s2 ,s3 , s4 , s5 , s6 )                         #calculates score 

    record = {'firstName' : fName , 'lastName' : lName , 'id' : id , 'avg' : avg , 'grade' : lGrade , 'quiz' : qs , 'testList' : list }           #redeclare record dictionary

    students.append(record)                                                             #append record to students list

    print("\n\nYou have successfully added a student! ")

    return students

def removeStudent( students ) :
    target = input( "\n\nEnter LAST NAME of the student would you like to delete: " )
    print( "\n\nYou selected: '" + target + "' \n\nPlease wait....." )

    for i in students :
        if target in i['lastName'] :
            print( "\n\nCongrats, you removed '" + i['lastName'].rstrip() + ", " + i['firstName'] + "' from the list...")
            students.remove(i)
            return students
        else :
            print("\n\nThat name is not in the list...")
            return students

def editStudent( students ) :
    target = input("\n\nEnter the LAST NAME of the student you like to edit: ")

    for i in students :
        if target in i['lastName'] :
            choice = input( "\n\nWould you like to edit TEST('t') or QUIZ('q') score: ")
            if choice == 't' :
                tScores = input("\n\nEnter 6 TEST SCORES separated with 1 space: ")
                s1 , s2 , s3 , s4 , s5 , s6 = tScores.split()
                s1 , s2 , s3 ,s4 , s5 , s6 = scoreChecker( s1 , s2 , s3 , s4 , s5 , s6 )

                qs = i['quiz']

                avg , lGrade , list = calcScore( qs , s1 , s2 ,s3 , s4 , s5 , s6 )

                i['avg'] , i['grade'] , i['testList'] = avg , lGrade , list

                print("\n\nCongrats , you edited the record successfully!\n\n")
                print(i)
                
                return students
        elif choice == 'q' :
            s1 , s2 , s3 ,s4 , s5 = i['testList']
            s6 = 0

            qs = input("\n\nEnter a quiz score: ")
            qs = qsChecker( qs )

            avg , lGrade , list = calcScore( qs , s1 , s2 ,s3 , s4 , s5 , s6 )

            i['avg'] , i['grade'] , i['testList'] , i['quiz'] = avg , lGrade , list , qs

            print("\n\nCongrats , you edited the record successfully!\n\n")
            print(i)

            return students
        else :
            print("\n\nInvalid option...")
            return students

def idChecker( id ) :
    if len(id) != 9 :
        while True:
            id = input("\n\nEnter *******VALID***** 9-DIGIT ID: ")
            if len(id) == 9 :
                break

    return id

def qsChecker( qs ) :
    if qs.isdigit() :
        if int(qs) <= 100 :
            return int(qs)
    else :
         while True :
             qs = input("\n\nEnter a ******VALID***** QUIZ score: ")
             if qs.isdigit() :
                 if int(qs) <= 100 :
                    return int(qs)

def scoreChecker( s1 , s2 , s3 , s4 , s5 , s6 ) :   
    list = [ s1 , s2 , s3 , s4 , s5 , s6 ]

    for i in list :
        if i.isdigit() :
            break
        else :
            while True :
                list[i] = input("\n\nEnter a ******VALID***** test score for test "+ list[i] +": ")
                if i.isdigit() :
                    break

    return s1 , s2 , s3 , s4 , s5 , s6


###### MAIN #####
import os
import time
import operator

fileName , outputFileName = readInFile()
students , title , course , location = readFile( fileName )

menu( outputFileName , students , title , course , location )