# 1. Hello World
print("Hello World")

# 2. Add, Subtract, Multiply, Divide, Modulus of Two Numbers
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# 3. Square Root of a Number
n = float(input())
print(n ** 0.5)

# 4. Area of a Triangle
base = float(input())
height = float(input())
area=0.5*base*height
print(area)

# 5. Algebraic Formulas
num1 = int(input())
num2 = int(input())
print((num1 + num2) ** 2)
print((num1 - num2) ** 2)
print(num1 ** 2 - num2 ** 2)

# 6. Swap Two Variables
x = int(input())
y = int(input())
temp = x
x = y
y = temp
print(x, y)

# 7. Kilometers to Miles
km = float(input())
print(km * 0.63)

# 8. Celsius to Fahrenheit
celsius = float(input())
print((celsius * 1.8) + 32)

# 9. Last Digit of a Number
num = int(input())
print(num % 10)

# 10. Last Two Digits of a Number
num = int(input())
print(num % 100)

# 11. Square of the Middle Digit of a Five-Digit Number
num = int(input())
middle = (num // 100) % 10
print(middle**2)
