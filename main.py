import time

# Retorna un arreglo inicial de 10 transacciones de prueba (desordenadas).
def obtener_datos_iniciales():
    return [
        {"timestamp": "14:25:30.145", "simbolo": "AAPL", "precio": 182.50},
        {"timestamp": "09:30:15.002", "simbolo": "AAPL", "precio": 180.10},
        {"timestamp": "10:15:00.500", "simbolo": "AAPL", "precio": 181.20},
        {"timestamp": "09:30:00.001", "simbolo": "AAPL", "precio": 179.95},
        {"timestamp": "16:00:00.000", "simbolo": "AAPL", "precio": 183.10},
        {"timestamp": "11:45:10.330", "simbolo": "AAPL", "precio": 181.85},
        {"timestamp": "13:05:45.890", "simbolo": "AAPL", "precio": 182.05},
        {"timestamp": "12:30:20.100", "simbolo": "AAPL", "precio": 181.60},
        {"timestamp": "15:10:05.770", "simbolo": "AAPL", "precio": 182.90},
        {"timestamp": "14:00:12.650", "simbolo": "AAPL", "precio": 182.30},
    ]

# Muestra en formato de tabla las transacciones almacenadas.
def mostrar_transacciones(transacciones):
    if not transacciones:
        print("\nEl arreglo está vacío.")
        return

    print("\n" + "=" * 50)
    print(f"{'#':<4} | {'Timestamp':<14} | {'Símbolo':<8} | {'Precio ($)':<10}")
    print("-" * 50)
    for idx, t in enumerate(transacciones, start=1):
        print(f"{idx:<4} | {t['timestamp']:<14} | {t['simbolo']:<8} | {t['precio']:>10.2f}")
    print("=" * 50)
    print(f"Total de registros: {len(transacciones)}")

# Permite al usuario ingresar una nueva transacción al arreglo.
def ingresar_transaccion(transacciones):
    print("\n--- Ingresar Nueva Transacción ---")
    timestamp = input("Ingrese el timestamp (formato HH:MM:SS.mmm): ").strip()
    if not timestamp:
        print("El timestamp no puede estar vacío.")
        return

    simbolo = input("Ingrese el símbolo de la acción (AAPL): ").strip().upper()
    if not simbolo:
        simbolo = "AAPL"

    try:
        precio_input = input("Ingrese el precio de la acción: ").strip()
        precio = float(precio_input)
    except ValueError:
        print("[!] Precio no válido. Debe ser un número.")
        return

    transacciones.append({
        "timestamp": timestamp,
        "simbolo": simbolo,
        "precio": precio
    })
    print(f"Transacción registrada con éxito: {timestamp} | {simbolo} | ${precio:.2f}")

# Ordena las transacciones cronológicamente por timestamp usando Bubble Sort optimizado.
def bubble_sort_optimizado(transacciones):
    n = len(transacciones)
    if n <= 1:
        return transacciones

    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            if transacciones[j]["timestamp"] > transacciones[j + 1]["timestamp"]:
                transacciones[j], transacciones[j + 1] = transacciones[j + 1], transacciones[j]
                intercambio = True
        # Si no hubo intercambios en esta pasada, el arreglo ya está ordenado
        if not intercambio:
            break

    return transacciones

# Verifica si el arreglo está ordenado cronológicamente por timestamp.
def esta_ordenado(transacciones):
    for i in range(len(transacciones) - 1):
        if transacciones[i]["timestamp"] > transacciones[i + 1]["timestamp"]:
            return False
    return True

# Realiza una búsqueda binaria por timestamp exacto.
def busqueda_binaria(transacciones, timestamp_objetivo):
    inicio_tiempo = time.perf_counter()

    izquierda = 0
    derecha = len(transacciones) - 1
    pasos = 0
    encontrado = None

    while izquierda <= derecha:
        pasos += 1
        medio = (izquierda + derecha) // 2
        actual = transacciones[medio]["timestamp"]

        if actual == timestamp_objetivo:
            encontrado = transacciones[medio]
            break
        elif actual < timestamp_objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    fin_tiempo = time.perf_counter()
    tiempo_total = fin_tiempo - inicio_tiempo

    return encontrado, pasos, tiempo_total

# Maneja la interacción de búsqueda binaria con validación y medición de tiempo.
def ejecutar_busqueda(transacciones):
    if not transacciones:
        print("\nArreglo Vacío.")
        return

    if not esta_ordenado(transacciones):
        print("\nEl arreglo no está ordenado.")
        print("La búsqueda binaria requiere que el arreglo esté ordenado cronológicamente.")
        opcion = input("¿Desea ordenarlo ahora con Bubble Sort antes de buscar? (s/n): ").strip().lower()
        if opcion == 's':
            bubble_sort_optimizado(transacciones)
            print("Arreglo ordenado exitosamente.")
        else:
            print("Operación cancelada. Ordene el arreglo primero.")
            return

    timestamp_buscar = input("\nIngrese el timestamp exacto a buscar (ej. 14:25:30.145): ").strip()
    resultado, pasos, tiempo_segundos = busqueda_binaria(transacciones, timestamp_buscar)

    # Convertir tiempo a unidades comprensibles
    tiempo_ns = tiempo_segundos * 1e9
    tiempo_ms = tiempo_segundos * 1e3

    print("\n" + "-" * 45)
    print("           RESULTADO DE BÚSQUEDA")
    print("-" * 45)
    if resultado:
        print(f"Estado       : [Registro encontrado")
        print(f"Timestamp    : {resultado['timestamp']}")
        print(f"Símbolo      : {resultado['simbolo']}")
        print(f"Precio       : ${resultado['precio']:.2f}")
    else:
        print(f"Estado       : [✗] Timestamp '{timestamp_buscar}' no encontrado")

    print(f"Pasos dados  : {pasos}")
    print(f"Tiempo total : {tiempo_ns:.2f} ns ({tiempo_ms:.5f} ms)")
    print("-" * 45)

# Controlador del menú de consola interactivo.
def menu_principal():
    transacciones = obtener_datos_iniciales()

    while True:
        print("    SISTEMA DE TRADING")
        print("1. Mostrar transacciones")
        print("2. Ingresar nueva transacción")
        print("3. Ordenar transacciones (Bubble Sort optimizado)")
        print("4. Buscar precio por timestamp exacto (Búsqueda Binaria)")
        print("5. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            mostrar_transacciones(transacciones)
        elif opcion == "2":
            ingresar_transaccion(transacciones)
        elif opcion == "3":
            bubble_sort_optimizado(transacciones)
            print("\nArreglo ordenado correctamente con Bubble Sort.")
            mostrar_transacciones(transacciones)
        elif opcion == "4":
            ejecutar_busqueda(transacciones)
        elif opcion == "5":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 5.")


if __name__ == "__main__":
    menu_principal()
