my_name = input("enter your name ")
my_age = input ("enter your age ")

print (f"My name is {my_name} and I am {my_age} years old")


firstNum = int(input ("choose a number "))
secNum = int (input ("choose a second number "))

operation = input ("what do u want add,minus,times,divide ")


if operation == 'add' :
    print (firstNum+secNum)

elif operation == 'minus' :
    print (firstNum-secNum)

elif operation == 'times' :
    print (firstNum*secNum)

elif operation == 'divide' :
    print (firstNum/secNum)
else:
    print('the operation is not valid')  
    


bus_capacity = 101
peopleInBus = int (input("how many people are in  the bus currently? "))
peopleGetIn = int (input ("how many people want to get in the bus? "))
emptySeats = bus_capacity - peopleInBus
if emptySeats>= peopleInBus :
        print ("there are enough seats!!")
else: 
        print ("there isnt enough seats :(")

