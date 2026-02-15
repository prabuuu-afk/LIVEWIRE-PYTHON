#----------------------------------loop problems------------------------
#first N natural numbers
n=int(input())
for i in range(1,n+1):
    print(i,end=" ")
#First N even natural numbers
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")
#First N odd natural numbers
n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")
#First N multiples of 3
n=int(input())
for i in range(1,n+1):
    print(i*3,end=" ")
#First N multiples of 5
n=int(input())
for i in range(1,n+1):
    print(i*5,end=" ")
#Multiples of 2 till N
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")
#Multiples of either 2 or 3 till N
n=int(input())
for i in range(1,n+1):
    if i%2==0 or i%3==0:
        print(i,end=" ")
#Multiples of 2 5 or 7 till N
n=int(input())
for i in range(1,n+1):
    if i%2==0 or i%5==0 or i%7==0:
        print(i,end=" ")
#Multiples of 3 5 or 7 till N
n = int(input("Enter N: "))
count = 0
i = 1
while count < n:
    if i%3==0 or i%5==0 or i%7==0:
        print(i, end=" ")
        count += 1
    i += 1
#Sum of digits
num = int(input("Enter number: "))
s = 0
while num>0:
    s += num%10
    num //= 10
print("Sum =", s)
#count digits
num = int(input("Enter number: "))
count = 0
while num>0:
    count += 1
    num //= 10
print("Digits =", count)
#Factors of a number
n = int(input("Enter number: "))
for i in range(1, n+1):
    if n%i==0:
        print(i, end=" ")
#Count factors
n = int(input("Enter number: "))
c=0
for i in range(1, n+1):
    if n%i==0:
        c+=1
print(c)
#chexk prime
n = int(input("Enter number: "))

if n <= 1:
    print("Not Prime")
else:
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    if count == 2:
        print("Prime")
    else:
        print("Not Prime")
#check prime from 1 to n
n = int(input("Enter N: "))

for num in range(2, n+1):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, end=" ")
#gcf
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcf = 1

for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        gcf = i

print("GCF =", gcf)
#Common Factors of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        print(i, end=" ")
#Fibonacci Series up to 50
a = 0
b = 1

print(a, end=" ")
print(b, end=" ")

while True:
    c = a + b
    if c > 50:
        break
    print(c, end=" ")
    a = b
    b = c
#factorial
n = int(input())
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print(fact)
#Sum of Even and Odd Numbers
n=int(input())
even=0
odd=0
for i in range(n):
    num=int(input())
    if num%2==0:
        even=even+num
    else:
        odd=odd+num
print(even)
print(odd)
#palindrome number
num = int(input())

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
#armstrong number
num = int(input())

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit * digit * digit
    temp = temp // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
#patterns
#square pattern
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
#triangle pattern
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
#number pattern
n=int(input())
k=1
for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
        k+=1
    print()