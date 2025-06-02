a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
d = float(input("Enter the fourth number: "))

if a > b:
    if a > c:
        if a > d:
            maximum = a
        else:
            maximum = d
    else:
        if c > d:
            maximum = c
        else:
            maximum = d
else:
    if b > c:
        if b > d:
            maximum = b
        else:
            maximum = d
    else:
        if c > d:
            maximum = c
        else:
            maximum = d

print("The maximum number is:", maximum)
