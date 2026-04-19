import tkinter as tk
import subprocess


class ShellEducativa:
    def __init__(self, parent):
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Shell Educativa")

        # campo de entrada para comandos
        self.entrada = tk.Entry(self.ventana, width=60)
        self.entrada.pack(pady=10, padx=10)
        self.entrada.bind("<Return>", self.ejecutar_comando)

        # area de texto para mostrar la salida
        self.salida = tk.Text(self.ventana, width=60, height=20)
        self.salida.pack(pady=10, padx=10)

        # Frame para los botones
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=5)

        # Boton "Ejecutar" - ejecuta el comando escrito en el Entry
        btn_ejecutar = tk.Button(frame_botones, text="Ejecutar", command=self.ejecutar_comando)
        btn_ejecutar.grid(row=0, column=0, padx=5, pady=2)

        # Boton "Limpiar" - limpia el area de texto de salida
        btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=self.limpiar_salida)
        btn_limpiar.grid(row=0, column=1, padx=5, pady=2)

    def ejecutar_comando(self, evento=None):
        """Ejecuta el comando ingresado y muestra la salida."""
        comando = self.entrada.get().strip()
        if not comando:
            return

        self.salida.insert(tk.END, f"> {comando}\n")

        try:
            resultado = subprocess.run(
                comando,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            if resultado.stdout:
                self.salida.insert(tk.END, resultado.stdout)
            if resultado.stderr:
                self.salida.insert(tk.END, f"Error: {resultado.stderr}")
        except subprocess.TimeoutExpired:
            self.salida.insert(tk.END, "Error: El comando excedió el tiempo máximo de ejecución (30s)\n")
        except Exception as e:
            self.salida.insert(tk.END, f"Error: {e}\n")

        self.salida.insert(tk.END, "\n")
        self.salida.see(tk.END)
        self.entrada.delete(0, tk.END)

    def limpiar_salida(self):
        """Limpia el area de texto de salida."""
        self.salida.delete(1.0, tk.END)
