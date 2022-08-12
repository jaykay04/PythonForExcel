name = input("What is your Name? ")
age = int(input("How Old are you? "))

yearsto50 = 50 - age 

if yearsto50 > 0:
    print("Hello " + name + ", you will be 50 in " + str(yearsto50) + " years")
else:
    print("Hello" + name + ", you were 50 about " + str(-yearsto50) + " years ago")
print("GoodBye!!!")