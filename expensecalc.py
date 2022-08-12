# WHILE LOOP
# num = 1
# while num <= 10:
#     print(num)
#     num += 1

# exp = -1
# total = 0

# while exp != 0:
#     exp = int(input("What is your expense? Type 0 to Stop "))
#     total = total + exp
# print("Your Total Expenditure is " + "$" + str(total))

# PYTHON LIST
# exp = [10,25,17,20,35,50]
# print(exp)
# print ("Total Number if elements in the List is " + str(len(exp)))
# print("We have", len(exp), "number of items in the List")
# print(max(exp))

# EXPENSE CALC
exp = []
stopped = False

while not stopped:
    e = int(input("What is Your Expense? Type 0 to Stop "))
    if e != 0:
        exp.append(e)
    else:
        stopped = True
print(exp)
print("Total Expenses:", sum(exp))
print("Maximum Expenses:", max(exp))