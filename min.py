import math
print("Hello with you Dynamic calculator, you can Calculate anything.\n")
operation = int(input(
"""Choose operation:
[1] Addition (+)
[2] Subtraction (-)
[3] Multiplication (*)
[4] Division (/)
[5] Modulus (%)
[6] Exponentiation (**)
[7] Min
[8] Max
[9] Round
Choice: """
))
a = input("Enter numbers separated by comma: ")
nums = [float(x) for x in a.split(",")]   # تحويل ل float
def add(*nums):
    return sum(nums)
def sub(*nums):
    result = nums[0]
    for n in nums[1:]:
        result -= n
    return result
def mul(*nums):
    result = nums[0]
    for n in nums[1:]:
        result *= n
    return result
def div(*nums):
    result = nums[0]
    for n in nums[1:]:
        if n == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result /= n
    return result
def mod(*nums):
    result = nums[0]
    for n in nums[1:]:
        result %= n
    return result
def exp(*nums):
    result = nums[0]
    for n in nums[1:]:
        result **= n
    return result
if operation == 1:
    print(add(*nums))
elif operation == 2:
    print(sub(*nums))
elif operation == 3:
    print(mul(*nums))
elif operation == 4:
    print(div(*nums))
elif operation == 5:
    print(mod(*nums))
elif operation == 6:
    print(exp(*nums))
elif operation == 7:
    print(min(nums))
elif operation == 8:
    print(max(nums))
elif operation == 9:
    print([round(n) for n in nums])
else:
    print("Invalid choice")
