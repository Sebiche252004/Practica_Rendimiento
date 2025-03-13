import datetime

def factorial_recursivo(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    return 1 if n == 0 else n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


valores_n = [10, 20, 30, 40, 50]


for n in valores_n:
    print(f"\n--- Midiendo tiempos para n = {n} ---")

    start_time = datetime.datetime.now()
    resultado_recursivo = factorial_recursivo(n)
    end_time = datetime.datetime.now()
    tiempo_recursivo = end_time - start_time

    start_time = datetime.datetime.now()
    resultado_iterativo = factorial_iterativo(n)
    end_time = datetime.datetime.now()
    tiempo_iterativo = end_time - start_time

    print(f"Factorial recursivo de {n}: {resultado_recursivo} (Tiempo: {tiempo_recursivo})")
    print(f"Factorial iterativo de {n}: {resultado_iterativo} (Tiempo: {tiempo_iterativo})")
