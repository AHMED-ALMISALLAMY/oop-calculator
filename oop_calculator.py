class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        """Add two numbers"""
        return self.num1 + self.num2


    def subtract(self):
        """Subtract numbers"""
        return self.num1 - self.num2


    def multiply(self):
        """Multiply numbers"""
        return self.num1 * self.num2


    def divided(self):
        """Divided numbers"""
        return self.num1 / self.num2


calc = Calculator(200,300)

print(calc.sum())

print(calc.multiply())