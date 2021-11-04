def equation(a,b):
    if (a == 0 and b == 0):
        return "bezlich"
    if (a == 0):
        return "nema"
    x = -b / a
    return "{:.2f}".format(x);

print(equation(2, -4))