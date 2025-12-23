from Calculator import cal
number = input("Enter Your Numbers (separated by space): ")
nums = number.split()
S1 = cal(*nums)
operation = input("Choose operation: Addition [A], Subtraction [S], ""Multiplication [M], Division [D], Power [P], Sqrt [R]: ").lower()
if operation == 'a':
    print(S1.addition())
elif operation == 's':
    print(S1.subtraction())
elif operation == 'm':
    print(S1.multiplication())
elif operation == 'd':
    print(S1.division())
elif operation == 'p':
    print(S1.power())
elif operation == 'r':
    print(S1.sqrt())
else:
    raise Exception("The selected operation does not exist in the calculator")