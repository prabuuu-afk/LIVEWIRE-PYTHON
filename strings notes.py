string=input()
upper=0
lower=0
num=0
symbol=0
spaces=0
for i in string:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        num+=1
    elif i.isspace():
        spaces+=1
    else:
        symbol+=1
print(upper,lower,num,symbol,spaces)