#-----------how many times the character is printed in the string--------------
s=input("Enter a string:").lower()
v=input("Enter the character:")
c=0
for i in s:
    if i==v:
        c+=1
print("number of times the character is printed in the string:",c)

#--------count number of vowels in the given string and display it-----------
s=input("Enter a string:").lower()
vowels = "aeiou"
c=0
w=""
for i in s:
    if i in vowels:
        c+=1
        w+=i
print("number of vowels in the string:",c)
print("vowels in the string:",w)

#----------program to get input in a string, convert into uppercase and print in separate lines----------
s=input("Enter a string:").split(" ")
for i in s:
    print(i.upper())
    
#--------------function to accept string input and print it in reverse and to find number of vowels in the string__________
def reverse_string():
    s=input("Enter a string:").lower()
    print("Reverse of the string:",s[::-1])
    vowels = "aeiou"
    c=0
    for i in s:
        if i in vowels:
            c+=1
    print("number of vowels in the string:",c)
reverse_string()

#-----------input a sentence and print the number of characters found in the longest word of the given sentence----------------
s=input("Enter a sentence:").split(" ")
long=""
for i in s:
    if len(i)>len(long):
        long=i
print("Longest word:",long)