import tkinter as tk
from explorador import ExploradorArchivos
from procesos import GestorProcesos
from shell import ShellEducativa 
from sistema import InfoSistema

root = tk.Tk() # creamos la ventana principal
root.title("Mini Sistema Operativo") # es para darle un titulo para la ventana
root.geometry("400x300") # esto establece el tamaño de la ventana (ancho x alto)

def abrir_explorador():
    ExploradorArchivos(root)
    print("Explorador de archivos abierto")

def abrir_procesos():
    GestorProcesos(root)
    print("Gestor de procesos abierto")

def abrir_shell():
    ShellEducativa(root)
    print("Shell abierta")

def abrir_sistema():
    InfoSistema(root)
    print("infosistema abierto")

# Botón para abrir el Explorador de Archivos
btn_explorador = tk.Button(root, text="Explorador de Archivos", command=abrir_explorador)
btn_explorador.pack(pady=10)

# Botón para abrir el Gestor de Procesos
btn_procesos = tk.Button(root, text="Gestión de Procesos", command=abrir_procesos)
btn_procesos.pack(pady=10)

# Botón para abrir la Shell Educativa
btn_shell = tk.Button(root, text="Shell Educativa", command=abrir_shell)
btn_shell.pack(pady=10)

# Botón para ver Información del Sistema
btn_sistema = tk.Button(root, text="Información del Sistema", command=abrir_sistema)
btn_sistema.pack(pady=10)
root.mainloop() # esto es para que la ventana se mantenga abierta

