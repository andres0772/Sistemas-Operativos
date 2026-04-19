import tkinter as tk
from tkinter import simpledialog, messagebox
import os


class ExploradorArchivos:
    def __init__(self, parent):
        self.parent = parent
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Explorador de Archivos")
        self.directorio_actual = os.getcwd()

        # Label para mostrar el directorio actual
        self.lbl_directorio = tk.Label(self.ventana, text=f"Directorio: {self.directorio_actual}",
                                       wraplength=400, anchor="w")
        self.lbl_directorio.pack(pady=5, padx=10, fill="x")

        # Listbox para mostrar archivos y carpetas
        self.lista = tk.Listbox(self.ventana, width=50, height=15)
        self.lista.pack(pady=10, padx=10)

        # Detectar doble-click para entrar a carpetas
        self.lista.bind("<Double-Button-1>", self.doble_click)

        # Frame para los botones
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=5)

        # Botón "Listar Archivos" - recarga el listado
        btn_listar = tk.Button(frame_botones, text="Listar Archivos", command=self.cargar_archivos)
        btn_listar.grid(row=0, column=0, padx=5, pady=2)

        # Botón "Abrir Carpeta" - entra a la carpeta seleccionada
        btn_abrir = tk.Button(frame_botones, text="Abrir Carpeta", command=self.abrir_carpeta)
        btn_abrir.grid(row=0, column=1, padx=5, pady=2)

        # Botón "Back" - sube un nivel
        btn_back = tk.Button(frame_botones, text="Back", command=self.subir_nivel)
        btn_back.grid(row=0, column=2, padx=5, pady=2)

        # Botón "Crear Carpeta" - pide nombre y crea
        btn_crear = tk.Button(frame_botones, text="Crear Carpeta", command=self.crear_carpeta)
        btn_crear.grid(row=1, column=0, padx=5, pady=2)

        # Botón "Cambiar Nombre" - renombra el seleccionado
        btn_renombrar = tk.Button(frame_botones, text="Cambiar Nombre", command=self.cambiar_nombre)
        btn_renombrar.grid(row=1, column=1, padx=5, pady=2)

        # Botón "Borrar" - elimina el seleccionado
        btn_borrar = tk.Button(frame_botones, text="Borrar", command=self.borrar)
        btn_borrar.grid(row=1, column=2, padx=5, pady=2)

        self.cargar_archivos()

    def cargar_archivos(self):
        """Carga los archivos del directorio actual en el Listbox."""
        self.lista.delete(0, tk.END)
        try:
            items = os.listdir(self.directorio_actual)
            for item in items:
                self.lista.insert(tk.END, item)
            # Actualizar el label del directorio
            self.lbl_directorio.config(text=f"Directorio: {self.directorio_actual}")
        except PermissionError:
            self.lista.insert(tk.END, "Sin permisos para acceder a este directorio")
        except Exception as e:
            self.lista.insert(tk.END, f"Error: {str(e)}")

    def subir_nivel(self):
        """Sube un nivel en la jerarquía de directorios."""
        padre = os.path.dirname(self.directorio_actual)
        if padre != self.directorio_actual:  # Evitar subir más allá de la raíz
            self.directorio_actual = padre
            self.cargar_archivos()

    def abrir_carpeta(self):
        """Entra a la carpeta seleccionada en el Listbox."""
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona una carpeta primero")
            return

        nombre = self.lista.get(seleccion[0])
        ruta_completa = os.path.join(self.directorio_actual, nombre)

        if os.path.isdir(ruta_completa):
            self.directorio_actual = ruta_completa
            self.cargar_archivos()
        else:
            messagebox.showinfo("Información", f"'{nombre}' no es una carpeta")

    def doble_click(self, event):
        """Maneja el doble-click para entrar a carpetas."""
        self.abrir_carpeta()

    def crear_carpeta(self):
        """Pide nombre con simpledialog y crea la carpeta."""
        nombre = simpledialog.askstring("Crear Carpeta", "Nombre de la nueva carpeta:",
                                        parent=self.ventana)
        if nombre:
            ruta_nueva = os.path.join(self.directorio_actual, nombre)
            try:
                os.mkdir(ruta_nueva)
                self.cargar_archivos()
            except FileExistsError:
                messagebox.showerror("Error", f"Ya existe una carpeta llamada '{nombre}'")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo crear la carpeta: {str(e)}")

    def cambiar_nombre(self):
        """Renombra la carpeta/archivo seleccionado."""
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un archivo o carpeta primero")
            return

        nombre_actual = self.lista.get(seleccion[0])
        ruta_actual = os.path.join(self.directorio_actual, nombre_actual)

        nuevo_nombre = simpledialog.askstring("Cambiar Nombre",
                                              f"Nuevo nombre para '{nombre_actual}':",
                                              parent=self.ventana,
                                              initialvalue=nombre_actual)
        if nuevo_nombre and nuevo_nombre != nombre_actual:
            ruta_nueva = os.path.join(self.directorio_actual, nuevo_nombre)
            try:
                os.rename(ruta_actual, ruta_nueva)
                self.cargar_archivos()
            except FileExistsError:
                messagebox.showerror("Error", f"Ya existe un elemento llamado '{nuevo_nombre}'")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo renombrar: {str(e)}")

    def borrar(self):
        """Elimina la carpeta/archivo seleccionado."""
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un archivo o carpeta primero")
            return

        nombre = self.lista.get(seleccion[0])
        ruta_completa = os.path.join(self.directorio_actual, nombre)

        # Confirmar antes de borrar
        confirmar = messagebox.askyesno("Confirmar", f"¿Estás seguro de borrar '{nombre}'?")
        if not confirmar:
            return

        try:
            if os.path.isdir(ruta_completa):
                os.rmdir(ruta_completa)  # Solo borra carpetas vacías
            else:
                os.remove(ruta_completa)
            self.cargar_archivos()
        except OSError as e:
            messagebox.showerror("Error", f"No se pudo borrar '{nombre}': {str(e)}\n"
                                         f"Nota: Las carpetas deben estar vacías para poder borrarlas.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo borrar: {str(e)}")
