from math import sqrt

class cal:
    def __init__(self, *nums):
        self.nums = nums
        self.number = []

    def _convert_numbers(self):
        self.number.clear()
        for x in self.nums:
            try:
                self.number.append(float(x))
            except ValueError:
                raise ValueError("Please enter numbers only")

    def addition(self):
        self._convert_numbers()
        return sum(self.number)

    def subtraction(self):
        self._convert_numbers()
        result = self.number[0]
        for n in self.number[1:]:
            result -= n
        return result

    def multiplication(self):
        self._convert_numbers()
        result = self.number[0]
        for n in self.number[1:]:
            result *= n
        return result

    def division(self):
        self._convert_numbers()
        result = self.number[0]
        for n in self.number[1:]:
            if n == 0:
                raise ValueError("Cannot divide by zero")
            result /= n
        return result

    def power(self):
        self._convert_numbers()
        result = self.number[0]
        for n in self.number[1:]:
            result **= n
        return result

    def sqrt(self):
        self._convert_numbers()
        result = self.number[0]
        for n in self.number[1:]:
            result = result ** (1 / n)
        return result