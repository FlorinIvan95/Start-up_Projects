class Calculator:
    def __init__(self):
        self.a = float(input('Enter first number:'))
        self.math_operator = input(
            "Choise mathematical operator(+, -, *, /): ")
        self.b = float(input('Enter second number:'))

    def mathematical_operations(self):
        if self.math_operator == "+":
            return f"{self.a} + {self.b} = {self.a + self.b}"
        if self.math_operator == "-":
            return f"{self.a} - {self.b} = {self.a - self.b}"
        if self.math_operator == "*":
            return f"{self.a} * {self.b} = {self.a * self.b}"
        if self.math_operator == "/":
            return f"{self.a} / {self.b} = {self.a / self.b}"


while True:
    equation = Calculator()
    print(equation.mathematical_operations())
    print("\n")
    exit_or_continue = input("Continue? Yes/No: ")
    if exit_or_continue.lower() == "no":
        quit()
