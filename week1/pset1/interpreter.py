expr = input("Expression: ")
x, y, z = expr.split(" ")
x, z = int(x), int(z)
if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    print(float(x / z))
