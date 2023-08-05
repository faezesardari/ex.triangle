print("lets check the number that can make triangle")

num1 = float(input("enter num1 : "))
num2 = float(input("enter num2 : "))
num3 = float(input("enter num3 : "))

if num1 < num2+num3 :
    check = " we can have a triangle"
else:
    check = "we cant have a triangle"
    
if num2 < num1+num3 :
    check = "we cna have a triangle"
else:
    check = "we cant have a triangle"

if num3 < num1+num2 :
    check = "we can have a triangle"
else:
    check = "we cant have a triangle"

print(check)