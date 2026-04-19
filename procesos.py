import tkinter as tk
import os


class GestorProcesos:
    def __init__(self, parent):
        self.parent = parent
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Gestión de Procesos")
        self.ventana.geometry("500x400")

        # frame principal
        frame = tk.Frame(self.ventana)
        frame.pack(pady=20, padx=20)

        # label título
        lbl_titulo = tk.Label(frame, text="Procesos Activos", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=5)

        # listbox para mostrar procesos
        self.lista = tk.Listbox(frame, width=60, height=20)
        self.lista.pack(pady=10, padx=10)

        # frame para botones
        btn_frame = tk.Frame(self.ventana)
        btn_frame.pack(pady=10)

        # Botón "Listar Procesos" - carga la lista
        btn_listar = tk.Button(btn_frame, text="Listar Procesos", command=self.cargar_procesos)
        btn_listar.pack(side=tk.LEFT, padx=5)

        # Botón "Terminar Proceso" - finaliza el seleccionado
        btn_terminar = tk.Button(btn_frame, text="Terminar Proceso", command=self.matar_proceso)
        btn_terminar.pack(side=tk.LEFT, padx=5)

        # Botón cerrar
        btn_cerrar = tk.Button(self.ventana, text="Cerrar", command=self.ventana.destroy)
        btn_cerrar.pack(pady=5)

        # NO cargar procesos al inicio - ventana vacía

    def cargar_procesos(self):
        """Carga la lista de procesos activos desde /proc."""
        self.lista.delete(0, tk.END)
        for pid in os.listdir("/proc"):
            if pid.isdigit():
                try:
                    with open(f"/proc/{pid}/comm") as f:
                        nombre = f.read().strip()
                    self.lista.insert(tk.END, f"PID: {pid} - {nombre}")
                except (FileNotFoundError, PermissionError):
                    pass

    def matar_proceso(self):
        """Finaliza el proceso seleccionado enviando SIGKILL."""
        seleccion = self.lista.curselection()
        if not seleccion:
            return
        linea = self.lista.get(seleccion[0])
        pid = linea.split()[1]
        try:
            os.kill(int(pid), 9)
            self.cargar_procesos()
        except PermissionError:
            self.lista.insert(tk.END, f"Error: Sin permisos para terminar PID {pid}")
        except ProcessLookupError:
            pass
