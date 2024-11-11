def mayor_de_tres(a, b, c):
    return max(a, b, c)

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

mayor = mayor_de_tres(a, b, c)
print(f"El número mayor es: {mayor}")
