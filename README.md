Creen un programa modular donde permita ingresar datos en arrays segun el problema que eligieron, permitiendo:
Mostrar la informacion aniadida

Ingresar datos al arreglo
Ordenar el arreglo por medio de Bubble Sort optimizado
Buscar un dato en el arreglo por medio de Busqueda Binaria
Cada busqueda debe mostrar el tiempo que ha tardado en realizar la tarea

Finanzas y Trading: Consultar el precio de una acción en un segundo exacto

El set de datos: Una base de datos con millones de transacciones de la bolsa de valores (como Wall Street) ocurridas durante el día, ordenadas cronológicamente por nanosegundos (ej: 09:30:00.001, 09:30:00.002...).

El problema: Un algoritmo de High-Frequency Trading (trading de alta velocidad) necesitaauditar el precio exacto de Apple (AAPL) a las 14:25:30.145 para ejecutar una orden de compra antes que la competencia.

Uso de búsqueda binaria: En lugar de recorrer las millones de transacciones desde el inicio del día, el sistema salta al centro del set de datos, compara la hora y descarta la mitad del día que no le sirve. Encuentra el registro exacto en menos de 20 pasos.
