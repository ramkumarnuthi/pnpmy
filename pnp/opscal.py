class Calculator:
    def __init__(self):
        self.sum = 5
        self.sub = 0
        self.mul = 1
        self.div = 1

    def add(self, num):
        self.sum += num

    def subtract(self, num):
        self.sub -= num

    def multiply(self, num):
        self.mul *= num

    def divide(self, num):
        if num != 0:
            self.div /= num
        else:
            print("error")
            
calc = Calculator()
calc.add(2)
calc.subtract(1)
calc.multiply(1)
calc.divide(1)

print("Sum:", calc.sum)
print("Subtraction:", calc.sub)
print("Multiplication:", calc.mul)
print("Division:", calc.div)