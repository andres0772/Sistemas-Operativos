# Mini Sistema Operativo Educativo

Un proyecto educativo que implementa un mini sistema operativo con interfaz gráfica para comprender el funcionamiento interno de las llamadas al sistema (system calls).

## Autor

**Andrés Esteban Vásquez Peña**

## Descripción

Este proyecto es un taller de laboratorio que desarrolla un mini sistema operativo educativo con las siguientes funcionalidades básicas:

- **Explorador de Archivos**: Navegación del sistema de archivos, crear/renombrar/borrar carpetas
- **Gestión de Procesos**: Listar y finalizar procesos activos del sistema
- **Shell Educativa**: Ejecutar comandos básicos del sistema y visualizar su salida
- **Información del Sistema**: Mostrar datos del usuario, espacio en disco y detalles del OS

## Requisitos

- Python 3.13+
- Tkinter (incluido en la instalación estándar de Python)
- Sistema operativo Linux (probado en Fedora 43)

## Ejecución

```bash
# Clonar el repositorio
git clone https://github.com/andres0772/mini-sistema-operativo.git
cd mini-sistema-operativo

# Ejecutar la aplicación
python main.py
```

**Nota**: No se requieren dependencias externas. El proyecto utiliza únicamente módulos estándar de Python.

## Estructura del Proyecto

```
mini-sistema-operativo/
├── main.py          # Ventana principal con menú de módulos
├── explorador.py    # Módulo de exploración de archivos
├── procesos.py      # Módulo de gestión de procesos
├── shell.py         # Módulo de shell educativa
├── sistema.py       # Módulo de información del sistema
└── README.md        # Documentación
```

## Módulos

### 1. Explorador de Archivos

| Botón | Función |
|-------|---------|
| Listar Archivos | Recarga el contenido del directorio actual |
| Abrir Carpeta | Entra a la carpeta seleccionada |
| Back | Sube un nivel en la jerarquía de directorios |
| Crear Carpeta | Crea una nueva carpeta con el nombre especificado |
| Cambiar Nombre | Renombra el archivo/carpeta seleccionado |
| Borrar | Elimina el archivo/carpeta seleccionado |

**Nota**: También podés hacer doble-click en una carpeta para entrar.

### 2. Gestión de Procesos

| Botón | Función |
|-------|---------|
| Listar Procesos | Muestra todos los procesos activos (PID y nombre) |
| Terminar Proceso | Finaliza el proceso seleccionado (requiere permisos) |

**Nota**: Algunos procesos del sistema requieren permisos de root para ser terminados.

### 3. Shell Educativa

| Botón | Función |
|-------|---------|
| Ejecutar | Ejecuta el comando ingresado |
| Limpiar | Limpia el área de salida |

**Comandos soportados**: `ls`, `pwd`, `echo`, y cualquier comando del sistema.

### 4. Información del Sistema

| Botón | Función |
|-------|---------|
| Info Usuario | Muestra nombre y directorio home del usuario |
| Espacio Disco | Muestra espacio total, usado y libre en GB |
| Info Sistema | Muestra OS, versión, arquitectura y hostname |

## Observaciones Importantes

### Visualización de botones

Algunas ventanas pueden mostrar todos los botones solo si se maximizan o se ven en pantalla completa. Si no ves los botones completos:

1. **Maximiza la ventana** haciendo click en el botón de maximizar
2. O **redimensiona la ventana** arrastrando los bordes

### Compatibilidad

- Probado en **Fedora 43** con Python 3.14
- Compatible con **WSL2 Ubuntu** (el código usa llamadas estándar de Linux)
- No compatible con Windows nativo (usa `/proc` para leer procesos)

### System Calls Utilizadas

| Módulo | System Calls |
|--------|--------------|
| Explorador | `os.listdir()`, `os.mkdir()`, `os.rename()`, `os.remove()` |
| Procesos | Lectura de `/proc/[pid]/comm`, `os.kill()` |
| Shell | `subprocess.run()` |
| Sistema | `getpass.getuser()`, `shutil.disk_usage()`, `platform` |

## Aprendizajes

Este proyecto permite comprender:

1. La relación entre interfaz gráfica y funcionamiento del sistema operativo
2. Implementación de comandos mediante llamadas al sistema
3. Manipulación de archivos, carpetas y procesos desde código
4. Estructura modular de aplicaciones de escritorio

