#My First Python Program

print ("You are welcome to my first python program")
user= input("Enter first number: ")
user1= input ("Enter second number: ")
user2 = input ("Enter your mathematical operator: ")
if user2 == "+":
    print ("The addition of", int (user), "and", int(user1), "is", int(user) + int(user1))
elif user2 == "-":
    print( "The subtraction of", int(user), "and", int(user1), "is", int(user)- int(user1))
elif user2 == "*":
     print( "The multiplication of", int(user), "and", int(user1), "is", int(user) * int(user1))
elif user2 == "/":
      print( "The division of", int(user), "and", int(user1), "is", int(user) / int(user1))
else:
    print ("Operator out of range")