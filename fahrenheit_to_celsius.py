def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

temp = int(input("Enter the Fahrenheit temperature:  "))
print(convert(temp))