num = int (input("WHich Multiplication Table do you want? "))

mx = [(x + 1) * num for x in range(21)]
mx2 = [ str(x+1) + " x " + str(num) + " = " + str((x+1) * num) for x in range(21)]

mx3 = [f'{x +1} x {num} = {(x +1) * num}' for x in range(21)]
print(mx2)

