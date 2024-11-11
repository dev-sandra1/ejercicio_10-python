def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(any.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Introduce un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

#es una clase del módulo typing que permite especificar que una variable, 
# parámetro o valor de retorno de una función puede ser de cualquier tipo. 
# Es útil cuando deseas flexibilidad en el tipo de dato sin aplicar restricciones específicas.