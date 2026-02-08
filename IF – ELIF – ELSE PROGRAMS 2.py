# IF – ELIF – ELSE PROGRAMS 2

# 1. Largest of three numbers
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

# 2. Smallest of three numbers
if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)

# 3. Positive, Negative or Zero
n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# 4. Library Fine
days = int(input())
if days <= 5:
    fine = days * 0.40
elif days <= 10:
    fine = days * 0.65
else:
    fine = days * 0.80
print(fine)

# 5. Calculator
x = float(input())
y = float(input())
op = input()
if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == 'x':
    print(x * y)
elif op == '/':
    print(x / y)

# 6. Multiple of 5, 3 and 7
n = int(input())
if n % 5 == 0 and n % 3 == 0 and n % 7 == 0:
    print("Yes")
else:
    print("No")

# 7. Parcel Charges
weight = int(input())
booking = input().upper()

if booking == 'O':
    if weight <= 100:
        print(80)
    elif weight <= 500:
        print(150)
    elif weight <= 1000:
        print(210)
    else:
        print(250)
else:
    if weight <= 100:
        print(100)
    elif weight <= 500:
        print(200)
    elif weight <= 1000:
        print(250)
    else:
        print(300)

# 8. Laptop Discount
price = int(input())

if price <= 50000:
    discount = 0
elif price <= 100000:
    discount = price * 0.10
elif price <= 150000:
    discount = price * 0.15
else:
    discount = price * 0.20

print("Price of laptop :", price)
print("Discount :", discount)
print("Total Price :", price - discount)
