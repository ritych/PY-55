class Calculator:
    def add(self, x, y):
        return x + y

class StringCalculator(Calculator):
    def add(self, x, y):
        return str(x) + str(y)


calc = Calculator()
result1 = calc.add(5, 3)

str_calc = StringCalculator()
result2 = str_calc.add("Hello", "World")  
