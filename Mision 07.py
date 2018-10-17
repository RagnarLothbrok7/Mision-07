# Oscar Macias Rodríguez
# Descripción: Despliega un menu de opciones para calcular y encontrar números.


# Recibe como parámetros el dividendo y el divisor e IMPRIME el cociente y el residuo.
def dividir(dividendo, divisor, cociente, residuo):
    while residuo >= divisor:
        residuo = residuo - divisor
        cociente += 1

    print(dividendo, "/", divisor, "=", cociente, ", sobra", residuo)


# Encuentra el mayor de un conjunto de valores enteros positivos que teclea el usuario.
def encontrarMayor(numero, numeroMayor):
    while numero != -1:
        numero = int(input("Teclea un número [-1 para salir]: "))
        if numero > numeroMayor:
            numeroMayor = numero
        elif numeroMayor < numero:
            numeroMayor = numero

    if numeroMayor > 0:
        print("El mayor es: ", numeroMayor)
    elif numero == -1 and numeroMayor == 0:
        print("No hay número mayor")
    return ""


# Despliega un menú de opciones preguntándole al usuario que desea realizar.
def main():
    opcion = 1
    while opcion != 0:
        print("""
        Mision 07. Ciclos while
        Autor: Oscar Macias Rodríguez
        Matrícula: A01376398
        1. Calcular divisiones
        2. Encontrar el mayor
        3. Salir
        """)

        opcion = int(input("Teclea tu opción: "))
        if opcion == 1:
            cociente = 0
            dividendo = int(input("Escribe el dividendo: "))
            divisor = int(input("Escibe el divisor: "))
            residuo = dividendo
            dividir(dividendo, divisor, cociente, residuo)

        if opcion == 2:
            numeroMayor = 0
            numero = 0
            mayor = encontrarMayor(numero, numeroMayor)
            print(mayor)

        if opcion == 3:
            exit("Gracias por usar este programa, regresa pronto.")
        else:
            main()


main()






