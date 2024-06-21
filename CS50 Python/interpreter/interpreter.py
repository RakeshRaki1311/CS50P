x,y,z = input("Expression: ").split(" ")
if y == "+":
    print(float(int(x) + int(z)))
elif y == "-":
    a = float(int(x) - int(z))
    print(a)
elif y == "*":
    a = float(int(x) * int(z))
    print(a)
elif y == "/":
    a = float(int(x) / int(z))
    print(a)