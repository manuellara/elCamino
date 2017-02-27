#############################
# homework 1
# Manuel Lara
#############################



name = input("What is your name? ")
age = int(input("\nWhat is your age? "))
randNum = int(input("\nEnter random number: "))

solution = 2017 + (100 - age)

count = 0
while count < randNum:
    print ("\nYour name is ", name, " and you are ", age, " years old.")
    print("You will turn 100 in the year ", solution, ".\n")
    count +=1