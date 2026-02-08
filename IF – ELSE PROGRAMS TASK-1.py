# IF – ELSE PROGRAMS 1

# 1. Smallest of two numbers
a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)

# 2. Largest of two numbers
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)

# 3. Absolute value
n = int(input())
if n >= 0:
    print(n)
else:
    print(-n)

# 4. Even or Odd
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# 5. Multiple of 5
n = int(input())
if n % 5 == 0:
    print("Yes")
else:
    print("No")

# 6. Multiple of 10
n = int(input())
if n % 10 == 0:
    print("Yes")
else:
    print("No")

# 7. Two-digit number
n = abs(int(input()))
if n >= 10 and n <= 99:
    print("Yes")
else:
    print("No")

# 8. Three-digit number
n = abs(int(input()))
if n >= 100 and n <= 999:
    print("Yes")
else:
    print("No")

# 9. Ends with zero
n = int(input())
if n % 10 == 0:
    print("Yes")
else:
    print("No")

# 10. Square above or below 50
n = int(input())
if n * n > 50:
    print("Above 50")
else:
    print("Below 50")

# 11. Difference is zero or not
a = int(input())
b = int(input())
if a - b == 0:
    print("Zero")
else:
    print("Not Zero")

# 12. Pass or Fail
marks = int(input())
if marks >= 50:
    print("Pass")
else:
    print("Fail")

# 13. Divisible by 10
n = int(input())
if n % 10 == 0:
    print("Yes")
else:
    print("No")

# 14. Biggest digit in two-digit number
n = abs(int(input()))
d1 = n // 10
d2 = n % 10
if d1 > d2:
    print(d1)
else:
    print(d2)

# 15. Exam choice
choice = int(input())
if choice == 1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")

# 16. Go out and play
val = int(input())
if val == 1:
    print("You can go out and play")
else:
    print("You cannot go out and play")

# 17. Square or Rectangle
l = int(input())
b = int(input())
if l == b:
    print("Square")
else:
    print("Rectangle")

# 18. ASCII uppercase
n = int(input())
if n >= 65 and n <= 90:
    print("Yes")
else:
    print("No")

# 19. ASCII lowercase
n = int(input())
if n >= 97 and n <= 122:
    print("Yes")
else:
    print("No")

# 20. ASCII numeric
n = int(input())
if n >= 48 and n <= 57:
    print("Yes")
else:
    print("No")

# 21. Multiple of 5 and 3
n = int(input())
if n % 5 == 0 and n % 3 == 0:
    print("Yes")
else:
    print("No")

# 22. Three-digit and multiple of 10
n = abs(int(input()))
if n >= 100 and n <= 999 and n % 10 == 0:
    print("Yes")
else:
    print("No")

# 23. Three-digit and multiple of 2, 5, and 10
n = abs(int(input()))
if n >= 100 and n <= 999 and n % 10 == 0:
    print("Yes")
else:
    print("No")

# 24. Product if both even else sum
a = int(input())
b = int(input())
if a % 2 == 0 and b % 2 == 0:
    print(a * b)
else:
    print(a + b)

# 25. Buzz Number
n = int(input())
if n % 7 == 0 or n % 10 == 7:
    print("Buzz Number")
else:
    print("Not a Buzz Number")
