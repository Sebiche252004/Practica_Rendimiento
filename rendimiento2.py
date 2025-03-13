import cProfile
import os

def letra_dni(dni):
    if len(str(dni)) != 8 or not dni.isdigit():
        raise ValueError("El DNI debe tener 8 dígitos numéricos")
    LETRAS_DNI = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return f"{dni}{LETRAS_DNI[int(dni) % 23]}"

def capitalizar(nombre):
    return nombre.title()

def procesar_csv(archivo_entrada, archivo_salida, cantidad):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            lista = file.readlines()

        csvModifikau = []
        for linea in lista:
            linea = linea.strip().split(",")  
            if len(linea) < 2:
                continue  
            nombre, dni = linea[0], linea[1]
            try:
                nombre_capitalizado = capitalizar(nombre)
                dni_con_letra = letra_dni(dni)
                csvModifikau.append(f"{nombre_capitalizado},{dni_con_letra}\n")
            except ValueError as e:
                print(f"Error en línea: {linea} - {e}")

        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.writelines(csvModifikau)

        print(f"Fichero de {cantidad} creado correctamente.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_entrada}.")


def borrar_archivos():
    archivos = ["Lista50.csv", "Lista1000.csv"]
    for archivo in archivos:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"Fichero {archivo} borrado.")
    print("\n")


while True:
    try:
        sel = int(input("Escribe número de selección:\n1. Lista de 50\n2. Lista de 1000\n3. Borrar listas generadas\n--> "))

        if sel == 1:
            if os.path.exists("Lista50.csv"):
                os.remove("Lista50.csv")
            cProfile.run("procesar_csv('50.csv', 'Lista50.csv', 50)")

        elif sel == 2:
            if os.path.exists("Lista1000.csv"):
                os.remove("Lista1000.csv")
            cProfile.run("procesar_csv('1000.csv', 'Lista1000.csv', 1000)")

        elif sel == 3:
            borrar_archivos()

        else:
            print("Introduce un número válido.\n")

    except ValueError:
        print("Error: Ingresa un número válido.\n")
