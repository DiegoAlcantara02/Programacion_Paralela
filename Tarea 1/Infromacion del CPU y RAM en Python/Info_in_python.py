# Importacion de los Moduolos a usar para la realizacion de la trea
import psutil
import cpuinfo
import platform


# Definiendo una variable para que muestre la cantidad de Procesadores Logicos (Hilos)
LP_THREAD = psutil.cpu_count()


# Definiendo una variable para que muestre la cantidad de Cores (Nucleos)
CORES = psutil.cpu_count(logical=False)

"""En esta parte el "logical=False" podriamos decir que es una "llave" que trae la propia 
libreria para asi poder hacer una diferenciacion entre los procesadores logicos y los 
nucleos. Ya que como explico usted en una clase,  Microsoft tiene un sistema de markerting 
que hace creer al usuario que los hilos son mas procesadores,  cuando este no es el caso"""


# Dterminacion del bus de datos
arch = platform.architecture()[0]


# Datos del Sistema Operativo
os_info = platform.uname()


# Definiendo variables de La memoria RAM
# https://www.youtube.com/watch?v=afYf5usgKIg
MEMORY = psutil.virtual_memory()
MEMORY_TOTAL = psutil.virtual_memory().total
memo_available = MEMORY.available  # RAM disponibe
memo_used = MEMORY.used  # RAM en uso


# Obtener la lista de procesos
procesos = list(psutil.process_iter())


# Obtener la cantidad de procesos
cantidad_procesos = len(procesos)


# Impresion de los Datos del CPU
print("El Tipo de Procesador que usa esta PC es un:",
      cpuinfo.get_cpu_info()["brand_raw"])  # https://www.youtube.com/watch?v=uwtHLEKCLaU


# Impresion de la arquitectura del bsu de datos
if arch == "32bit":
    print("La arquitectura de Bus de datos de este equipo es de 32 bits")
elif arch == "64bit":
    print("La arquitectura de Bus de datos de este equipo es de 64 bits")
else:
    print("No se puede determinar la arquitectura de Bus de datos de este equipo")


# Impresion de datos sobre las nucleo e Hilos
print(f"El Numero de Nucleos del Porecesador es de:", CORES)
print(f"El Numero de Procesadores Logicos (Hilos) es de:", LP_THREAD)


# Imppresion de informacion sobre el tipo de OS que poseo
print("Sistema operativo:", os_info.system)


# Impresion sobre la informacion de la arquitectura
print("Arquitectura:", os_info.machine)


# Impresion de los datos de la memoria RAM
print(f"Memoria RAM Disponible: {memo_available / 1024 / 1024:.2f} MB")
print(f"Memoria RAM en Uso: {memo_used / 1024 / 1024:.2f} MB")
print(F"Total de RAM de la PC: {MEMORY_TOTAL / 1024 / 1024:.2F} MB")


# Imprimir la cantidad de procesos (en el momento en que se ejecuta el codigo)
print(f"Cantidad de procesos en en ejecucion: {cantidad_procesos}")
