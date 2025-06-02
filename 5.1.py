
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b:
    if a > c:
        if a > d:
            max_num = a
        else:
            max_num = d
    else:
        if c > d:
            max_num = c
        else:
            max_num = d
else:
    if b > c:
        if b > d:
            max_num = b
        else:
            max_num = d
    else:
        if c > d:
            max_num = c
        else:
            max_num = d

print("The maximum number is:", max_num)




