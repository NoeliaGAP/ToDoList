# **Organizador Personal - README**

## Descripción
Este proyecto es un **Organizador Personal** desarrollado en Python, que permite gestionar una lista de tareas. Con este programa, puedes agregar, ver, editar, eliminar y categorizar tareas, así como establecer fechas límite y recordatorios. Toda la información de las tareas se almacena en un archivo JSON, por lo que el estado de las tareas se guarda entre ejecuciones.

## Funcionalidades

El organizador incluye las siguientes funcionalidades:

1. **Agregar tareas**: Permite añadir una nueva tarea con descripción, fecha límite y categoría opcional.
2. **Ver tareas**: Muestra todas las tareas junto con su estado, fecha límite y categoría.
3. **Marcar tareas como completadas**: Cambia el estado de una tarea a "Completada".
4. **Editar tareas**: Actualiza la descripción de una tarea existente.
5. **Eliminar tareas**: Borra una tarea de la lista.
6. **Agregar fecha límite**: Establece una fecha de vencimiento para una tarea.
7. **Categorizar tareas**: Asigna una categoría a una tarea (por ejemplo: Personal, Escuela, Hobby).
8. **Establecer recordatorios**: Permite configurar un recordatorio que te avise horas antes de la fecha límite.
9. **Ver tareas ordenadas por fecha límite**: Muestra las tareas que tienen una fecha de vencimiento, ordenadas cronológicamente.

## Requisitos

- Python 3.x
- Ninguna librería externa, salvo las librerías estándar de Python (`json`, `os`, `datetime`).

## Instalación
1. Clona este repositorio o descarga el código.

2. Asegúrate de tener Python 3 instalado en tu sistema.

3. Ejecuta el programa desde la línea de comandos:

```
python main.py
```

## Uso
Una vez iniciado el programa, verás un menú de opciones que te permitirá interactuar con tu lista de tareas. Las opciones disponibles son:

- **Agregar tarea**: Introduce una descripción, una fecha límite opcional y una categoría opcional para la nueva tarea.
- **Ver tareas**: Muestra todas las tareas con su estado (Pendiente/Completada), fecha límite y categoría.
- **Marcar tarea como completada**: Selecciona una tarea para cambiar su estado a "Completada".
- **Editar tarea**: Cambia la descripción de una tarea existente.
- **Eliminar tarea**: Borra una tarea de la lista.
- **Agregar fecha límite**: Establece o modifica la fecha límite de una tarea.
- **Categorizar tarea**: Asigna o cambia la categoría de una tarea.
- **Establecer recordatorio**: Configura un recordatorio que te avise antes de la fecha límite.
- **Ver tareas por fecha límite**: Muestra las tareas ordenadas por su fecha de vencimiento.

## Formato de Almacenamiento
Las tareas se guardan en un archivo `tasks.json` con el siguiente formato:
```
[
    {
        "description": "Descripción de la tarea",
        "completed": false,
        "due_date": "YYYY-MM-DD",
        "category": "Categoría",
        "reminder": "YYYY-MM-DD HH:MM:SS"
    }
]
```
## Mejoras Futuras
Aquí algunas ideas que podrías implementar en el futuro:

- **Interfaz gráfica**: Migrar la aplicación a una interfaz gráfica utilizando bibliotecas como Tkinter.

## Contribuir
Si deseas contribuir al proyecto, puedes hacer un **fork** y enviar un **pull request** con tus mejoras o sugerencias.

## Licencia
Este proyecto está bajo la licencia **MIT**.