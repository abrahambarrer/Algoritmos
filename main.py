import random
import time

NUM_TRANSACCIONES = 300


def obtener_datos_iniciales(modo="aleatorios"):
    """Genera 300 transacciones en orden aleatorio, ascendente o descendente."""
    transacciones = []
    for _ in range(NUM_TRANSACCIONES):
        milisegundos = random.randrange(24 * 60 * 60 * 1000)
        horas, resto = divmod(milisegundos, 60 * 60 * 1000)
        minutos, resto = divmod(resto, 60 * 1000)
        segundos, ms = divmod(resto, 1000)
        transacciones.append({
            "timestamp": f"{horas:02}:{minutos:02}:{segundos:02}.{ms:03}",
            "simbolo": "AAPL",
            "precio": round(random.uniform(100, 250), 2),
        })

    transacciones.sort(key=lambda t: t["timestamp"])
    if modo == "aleatorios":
        random.shuffle(transacciones)
    elif modo == "inversos":
        transacciones.reverse()
    elif modo != "ordenados":
        raise ValueError("Modo de generación desconocido.")
    return transacciones


def seleccionar_modo_generacion():
    print("\nForma de generar los datos:")
    print("1. Completamente aleatorios")
    print("2. Ordenados por tiempo")
    print("3. En orden inverso (peor caso)")
    opciones = {"1": "aleatorios", "2": "ordenados", "3": "inversos"}
    while True:
        opcion = input("Seleccione una opción (1-3): ").strip()
        if opcion in opciones:
            return opciones[opcion]
        print("Opción no válida.")


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


def ingresar_transaccion(transacciones):
    print("\n--- Ingresar Nueva Transacción ---")
    timestamp = input("Ingrese el timestamp (formato HH:MM:SS.mmm): ").strip()
    if not timestamp:
        print("El timestamp no puede estar vacío.")
        return
    simbolo = input("Ingrese el símbolo de la acción (AAPL): ").strip().upper() or "AAPL"
    try:
        precio = float(input("Ingrese el precio de la acción: ").strip())
    except ValueError:
        print("[!] Precio no válido. Debe ser un número.")
        return
    transacciones.append({"timestamp": timestamp, "simbolo": simbolo, "precio": precio})
    print(f"Transacción registrada con éxito: {timestamp} | {simbolo} | ${precio:.2f}")


def bubble_sort_optimizado(transacciones):
    n = len(transacciones)
    for i in range(n):
        intercambio = False
        for j in range(n - i - 1):
            if transacciones[j]["timestamp"] > transacciones[j + 1]["timestamp"]:
                transacciones[j], transacciones[j + 1] = transacciones[j + 1], transacciones[j]
                intercambio = True
        if not intercambio:
            break
    return transacciones


def selection_sort(transacciones):
    for i in range(len(transacciones) - 1):
        minimo = i
        for j in range(i + 1, len(transacciones)):
            if transacciones[j]["timestamp"] < transacciones[minimo]["timestamp"]:
                minimo = j
        if minimo != i:
            transacciones[i], transacciones[minimo] = transacciones[minimo], transacciones[i]
    return transacciones


def insertion_sort(transacciones):
    for i in range(1, len(transacciones)):
        actual = transacciones[i]
        j = i - 1
        while j >= 0 and transacciones[j]["timestamp"] > actual["timestamp"]:
            transacciones[j + 1] = transacciones[j]
            j -= 1
        transacciones[j + 1] = actual
    return transacciones


ALGORITMOS = {
    "Bubble Sort optimizado": bubble_sort_optimizado,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
}


def ordenar_y_mostrar_tiempo(transacciones, algoritmo):
    inicio = time.perf_counter()
    algoritmo(transacciones)
    tiempo_ms = (time.perf_counter() - inicio) * 1000
    print(f"Tiempo de ordenamiento: {tiempo_ms:.6f} ms")
    return tiempo_ms


def mostrar_comparativa(transacciones):
    print("\nTabla comparativa (tiempo de ordenamiento en ms)")
    print("-" * 48)
    print(f"{'Método':<28} | {'Tiempo (ms)':>15}")
    print("-" * 48)
    for nombre, algoritmo in ALGORITMOS.items():
        copia = transacciones.copy()
        inicio = time.perf_counter()
        algoritmo(copia)
        tiempo_ms = (time.perf_counter() - inicio) * 1000
        print(f"{nombre:<28} | {tiempo_ms:>15.6f}")
    print("-" * 48)


def esta_ordenado(transacciones):
    return all(transacciones[i]["timestamp"] <= transacciones[i + 1]["timestamp"]
               for i in range(len(transacciones) - 1))


def busqueda_binaria(transacciones, timestamp_objetivo):
    inicio_tiempo = time.perf_counter()
    izquierda, derecha, pasos = 0, len(transacciones) - 1, 0
    encontrado = None
    while izquierda <= derecha:
        pasos += 1
        medio = (izquierda + derecha) // 2
        actual = transacciones[medio]["timestamp"]
        if actual == timestamp_objetivo:
            encontrado = transacciones[medio]
            break
        if actual < timestamp_objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return encontrado, pasos, time.perf_counter() - inicio_tiempo


def ejecutar_busqueda(transacciones):
    if not transacciones:
        print("\nArreglo vacío.")
        return
    if not esta_ordenado(transacciones):
        print("\nEl arreglo no está ordenado. La búsqueda binaria requiere orden cronológico.")
        if input("¿Desea ordenarlo ahora con Bubble Sort? (s/n): ").strip().lower() == "s":
            ordenar_y_mostrar_tiempo(transacciones, bubble_sort_optimizado)
        else:
            print("Operación cancelada. Ordene el arreglo primero.")
            return
    timestamp = input("\nIngrese el timestamp exacto a buscar (ej. 14:25:30.145): ").strip()
    resultado, pasos, tiempo = busqueda_binaria(transacciones, timestamp)
    print("\n" + "-" * 45)
    print("RESULTADO DE BÚSQUEDA")
    if resultado:
        print(f"Timestamp    : {resultado['timestamp']}")
        print(f"Símbolo      : {resultado['simbolo']}")
        print(f"Precio       : ${resultado['precio']:.2f}")
    else:
        print(f"Timestamp '{timestamp}' no encontrado")
    print(f"Pasos dados  : {pasos}")
    print(f"Tiempo total : {tiempo * 1e9:.2f} ns ({tiempo * 1e3:.5f} ms)")
    print("-" * 45)


def menu_principal():
    modo = seleccionar_modo_generacion()
    transacciones = obtener_datos_iniciales(modo)
    print(f"Se generaron {len(transacciones)} transacciones ({modo}).")
    while True:
        print("\n    SISTEMA DE TRADING")
        print("1. Mostrar transacciones")
        print("2. Ingresar nueva transacción")
        print("3. Ordenar transacciones")
        print("4. Buscar precio por timestamp exacto (Búsqueda Binaria)")
        print("5. Comparar tiempos de ordenamiento")
        print("6. Generar nuevos datos")
        print("7. Salir")
        opcion = input("Seleccione una opción (1-7): ").strip()
        if opcion == "1":
            mostrar_transacciones(transacciones)
        elif opcion == "2":
            ingresar_transaccion(transacciones)
        elif opcion == "3":
            print("\nMétodos: 1. Bubble Sort optimizado  2. Selection Sort  3. Insertion Sort")
            metodo = input("Seleccione un método (1-3): ").strip()
            algoritmos = {"1": bubble_sort_optimizado, "2": selection_sort, "3": insertion_sort}
            if metodo in algoritmos:
                ordenar_y_mostrar_tiempo(transacciones, algoritmos[metodo])
                print("Arreglo ordenado correctamente.")
                mostrar_transacciones(transacciones)
            else:
                print("Método no válido.")
        elif opcion == "4":
            ejecutar_busqueda(transacciones)
        elif opcion == "5":
            mostrar_comparativa(transacciones)
        elif opcion == "6":
            modo = seleccionar_modo_generacion()
            transacciones = obtener_datos_iniciales(modo)
            print(f"Se generaron {len(transacciones)} transacciones ({modo}).")
        elif opcion == "7":
            print("\nSaliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 7.")


if __name__ == "__main__":
    menu_principal()
