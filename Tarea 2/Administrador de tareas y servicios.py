import psutil  # Servicios y procesos
import tkinter as tk  # Representacion de los datos en windows forms
from tkinter import ttk

# creacion de la ventana
Ventana = tk.Tk()

# Nombre de la ventana
Ventana.title("Administrador de tareas y servicios")

# geometria de la ventana
Ventana.geometry("1360x768")


# Obtener una lista de todos los procesos
procesos = []

for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'status']):
    try:
        pinfo = proc.as_dict(
            attrs=['pid', 'name', 'cpu_percent', 'memory_percent', 'status'])
        pinfo['memory_percent'] = round(pinfo['memory_percent'], 2)
        procesos.append(pinfo)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Crear una tabla para mostrar información de procesos
procesos_frame = tk.Frame(Ventana)
procesos_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Labe para nombrar la lista de Procesos
procesos_label = tk.Label(procesos_frame, text="Procesos", font=("Arial", 10))
procesos_label.pack(side=tk.TOP, pady=10)

# Creando una vista de arbol para representar los procesos en la tabla
procesos_table = ttk.Treeview(procesos_frame, columns=(
    'PID', 'Nombre', 'CPU', 'Memoria', 'Estado'))
procesos_table.heading('#0', text='')
procesos_table.column('#0', width=0, stretch=tk.NO)
procesos_table.heading('#1', text='PID')
procesos_table.column('#1', width=100, stretch=tk.NO)
procesos_table.heading('#2', text='Nombre')
procesos_table.column('#2', width=200, stretch=tk.NO)
procesos_table.heading('#3', text='CPU')
procesos_table.column('#3', width=100, stretch=tk.NO)
procesos_table.heading('#4', text='Memoria')
procesos_table.column('#4', width=100, stretch=tk.NO)
procesos_table.heading('#5', text='Estado')
procesos_table.column('#5', width=100, stretch=tk.NO)

# Insercion de los proceos en la tabla en la que se representaran con tkinter
for proceso in procesos:
    procesos_table.insert('', tk.END, text='', values=(
        proceso['pid'], proceso['name'], proceso['cpu_percent'], proceso['memory_percent'], proceso['status']))

procesos_table.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Botón para finalizar un proceso


def kill_proceso():
    pid = int(procesos_table.item(procesos_table.selection())['values'][0])
    p = psutil.Process(pid)
    p.terminate()


kill_button = tk.Button(
    procesos_frame, text="Finalizar proceso", command=kill_proceso)
kill_button.pack(side=tk.TOP, pady=10)

# Obtener una lista de todos los servicios
servicios = []  # Creacion de la listas

# Creacion de bucle que itera por cada servicio para obtener su nombre
for s in psutil.win_service_iter():
    try:
        sinfo = {"name": s.name(), "status": s.status(),
                 "binpath": s.binpath(), "username": s.username()}
        servicios.append(sinfo)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass


# Crear una tabla para mostrar información de servicios
servicios_frame = tk.Frame(Ventana)
servicios_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Labe para nombrar la lista de servicios
servicios_label = tk.Label(
    servicios_frame, text="Servicios", font=('Arial', 10))
servicios_label.pack(side=tk.TOP, pady=10)

# Creando una vista de arbol para representar los servicios en la tabla
servicios_table = ttk.Treeview(
    servicios_frame, columns=('Nombre', 'Estado', 'Ruta', 'Usuario'))
servicios_table.heading('#0', text='')
servicios_table.column('#0', width=0, stretch=tk.NO)
servicios_table.heading('#1', text='Nombre')
servicios_table.column('#1', width=200, stretch=tk.NO)
servicios_table.heading('#2', text='Estado')
servicios_table.column('#2', width=100, stretch=tk.NO)
servicios_table.heading('#3', text='Ruta')
servicios_table.column('#3', width=200, stretch=tk.NO)
servicios_table.heading('#4', text='Usuario')
servicios_table.column('#4', width=100, stretch=tk.NO)

# Insercion de los servicios en la tabla en la que se representaran con tkinter
for servicio in servicios:
    servicios_table.insert('', tk.END, text='', values=(
        servicio['name'], servicio['status'], servicio['binpath'], servicio['username']))

servicios_table.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Botón para detener un servicio

def kill_servicio():
    pid = int(servicios_table.item(servicios_table.selection())['values'][0])

    p = psutil.Process(pid)
    p.terminate()


stop_button = tk.Button(
    servicios_frame, text="Detener servicio", command=kill_servicio)
stop_button.pack(side=tk.TOP, pady=10)

# loop de ventana para que se mantega abierta hasta que no se cierre
Ventana.mainloop()
