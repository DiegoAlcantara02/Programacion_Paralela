# Importacion de los Moduolos a usar para la realizacion de la trea
import psutil
import cpuinfo

# Definiendo una variable para que muestre la cantidad de Procesadores Logicos (Hilos)
LP_THREAD = psutil.cpu_count()
# Definiendo una variable para que muestre la cantidad de Cores (Nucleos)
CORES = psutil.cpu_count(logical=False)

"""En esta parte el "logical=False" podriamos decir que es una "llave" que trae la propia 
libreria para asi poder hacer una diferenciacion entre los procesadores logicos y los 
nucleos. Ya que como explico usted en una clase,  Microsoft tiene un sistema de markerting 
que hace creer al usuario que los hilos son mas procesadores,  cuando este no es el caso"""

# Impresion de los Datos del CPU
print("El Tipo de Procesador que usa esta PC es un:",
      cpuinfo.get_cpu_info()["brand_raw"])  # https://www.youtube.com/watch?v=uwtHLEKCLaU

print(f"El Numero de Nucleos del Porecesador es de:", CORES)
print(f"El Numero de Procesadores Logicos (Hilos) es de:", LP_THREAD)

# Definiendo variables de La memoria RAM
# #https://www.youtube.com/watch?v=afYf5usgKIg
MEMORY = psutil.virtual_memory()
MEMORY_TOTAL = psutil.virtual_memory().total
men_available = MEMORY.available  # RAM disponibe
men_used = MEMORY.used  # RAM en uso

# Impresion de los datos de la memoria RAM
print(f"Memoria RAM Disponible: {men_available / 1024 / 1024:.2f} MB")
print(f"Memoria RAM en Uso: {men_used / 1024 / 1024:.2f} MB")
print(F"Total de RAM de la PC: {MEMORY_TOTAL / 1024 / 1024:.2F} MB")

"""No encontre forma de saber mis bus de datos y sobre los procesos en ejecuion,
   tengo la forma de mostrarlos todos pero algo complicada se veia muy feo y preferi no ponerlo"""
