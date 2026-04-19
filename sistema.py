import tkinter as tk
import os
import platform
import shutil
import getpass
import socket


class InfoSistema:
    def __init__(self, parent):
        self.parent = parent
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Información del Sistema")
        self.ventana.geometry("500x400")

        # frame principal para organizar los elementos
        frame = tk.Frame(self.ventana)
        frame.pack(pady=20, padx=20)

        # frame para los botones
        frame_botones = tk.Frame(frame)
        frame_botones.pack(pady=10)

        # botones para mostrar información
        btn_usuario = tk.Button(
            frame_botones,
            text="Info Usuario",
            command=self.mostrar_info_usuario
        )
        btn_usuario.pack(side=tk.LEFT, padx=5)

        btn_disco = tk.Button(
            frame_botones,
            text="Espacio Disco",
            command=self.mostrar_info_disco
        )
        btn_disco.pack(side=tk.LEFT, padx=5)

        btn_sistema = tk.Button(
            frame_botones,
            text="Info Sistema",
            command=self.mostrar_info_sistema
        )
        btn_sistema.pack(side=tk.LEFT, padx=5)

        # área de texto para mostrar la información
        frame_info = tk.Frame(frame)
        frame_info.pack(pady=20)

        # labels que se actualizarán (inician vacíos)
        self.lbl_titulo = tk.Label(
            frame_info,
            text="",
            font=("Arial", 14, "bold")
        )
        self.lbl_titulo.pack(anchor="w", pady=5)

        self.lbl_info1 = tk.Label(
            frame_info,
            text="",
            font=("Arial", 12)
        )
        self.lbl_info1.pack(anchor="w", pady=3)

        self.lbl_info2 = tk.Label(
            frame_info,
            text="",
            font=("Arial", 12)
        )
        self.lbl_info2.pack(anchor="w", pady=3)

        self.lbl_info3 = tk.Label(
            frame_info,
            text="",
            font=("Arial", 12)
        )
        self.lbl_info3.pack(anchor="w", pady=3)

        self.lbl_info4 = tk.Label(
            frame_info,
            text="",
            font=("Arial", 12)
        )
        self.lbl_info4.pack(anchor="w", pady=3)

        # botón para cerrar la ventana
        btn_cerrar = tk.Button(
            self.ventana,
            text="Cerrar",
            command=self.ventana.destroy
        )
        btn_cerrar.pack(pady=10)

    def mostrar_info_usuario(self):
        """Muestra información del usuario actual."""
        usuario = getpass.getuser()
        directorio_home = os.path.expanduser("~")

        self.lbl_titulo.config(text="Información de Usuario")
        self.lbl_info1.config(text=f"Nombre de usuario: {usuario}")
        self.lbl_info2.config(text=f"Directorio home: {directorio_home}")
        self.lbl_info3.config(text="")
        self.lbl_info4.config(text="")

    def mostrar_info_disco(self):
        """Muestra información del espacio en disco."""
        disco = shutil.disk_usage("/")
        espacio_total_gb = disco.total / (1024**3)
        espacio_usado_gb = disco.used / (1024**3)
        espacio_libre_gb = disco.free / (1024**3)

        self.lbl_titulo.config(text="Espacio en Disco")
        self.lbl_info1.config(text=f"Espacio total: {espacio_total_gb:.2f} GB")
        self.lbl_info2.config(text=f"Espacio usado: {espacio_usado_gb:.2f} GB")
        self.lbl_info3.config(text=f"Espacio libre: {espacio_libre_gb:.2f} GB")
        self.lbl_info4.config(text="")

    def mostrar_info_sistema(self):
        """Muestra información del sistema operativo."""
        os_nombre = platform.system()
        version = platform.release()
        arquitectura = platform.machine()
        hostname = socket.gethostname()

        self.lbl_titulo.config(text="Información del Sistema")
        self.lbl_info1.config(text=f"Sistema operativo: {os_nombre}")
        self.lbl_info2.config(text=f"Versión: {version}")
        self.lbl_info3.config(text=f"Arquitectura: {arquitectura}")
        self.lbl_info4.config(text=f"Hostname: {hostname}")
