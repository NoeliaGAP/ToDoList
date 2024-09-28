import json
import os
from datetime import datetime, timedelta

# Gestionar la lista de tareas
class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.load_tasks()

    # Cargar las tareas del archivo JSON
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    # Guardar las tareas en el archivo JSON
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    # Agregar una nueva tarea
    def add_task(self, description, due_date=None, category=None):
        task = {
            'description': description,
            'completed': False,
            'due_date': due_date,
            'category': category,
            'reminder': False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Tarea '{description}' agregada.")

    # Ver todas las tareas
    def view_tasks(self):
        if not self.tasks:
            print("No hay tareas.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                status = "Completada" if task['completed'] else "Pendiente"
                due_date = task['due_date'] if task['due_date'] else "Sin fecha límite"
                category = task['category'] if task['category'] else "Sin categoría"
                print(f"{idx}. [{status}] {task['description']} - Fecha: {due_date}, Categoría: {category}")

    # Marcar tarea como realizada
    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            self.save_tasks()
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")

    # Editar una tarea
    def edit_task(self, task_number, new_description):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['description'] = new_description
            self.save_tasks()
            print("Tarea editada.")
        else:
            print("Número de tarea inválido.")

    # Eliminar una tarea
    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
            self.save_tasks()
            print("Tarea eliminada.")
        else:
            print("Número de tarea inválido.")

    # Agregar fechas de vencimiento
    def add_due_date(self, task_number, due_date):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['due_date'] = due_date
            self.save_tasks()
            print("Fecha de vencimiento agregada.")
        else:
            print("Número de tarea inválido.")

    # Categorizar tarea
    def categorize_task(self, task_number, category):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['category'] = category
            self.save_tasks()
            print("Categoría agregada.")
        else:
            print("Número de tarea inválido.")

    # Recordatorio para una tarea
    def add_reminder(self, task_number, reminder_time):
        if 0 < task_number <= len(self.tasks):
            due_date = self.tasks[task_number - 1]['due_date']
            if due_date:
                due_date_dt = datetime.strptime(due_date, '%Y-%m-%d')
                reminder_dt = due_date_dt - timedelta(hours=reminder_time)
                self.tasks[task_number - 1]['reminder'] = reminder_dt.strftime('%Y-%m-%d %H:%M:%S')
                self.save_tasks()
                print(f"Recordatorio establecido para {reminder_time} horas antes de la fecha límite.")
            else:
                print("La tarea no tiene fecha límite.")
        else:
            print("Número de tarea inválido.")

    # Mostrar tareas ordenadas por fecha
    def view_tasks_by_due_date(self):
        tasks_with_due_date = sorted([task for task in self.tasks if task['due_date']], key=lambda x: x['due_date'])
        for idx, task in enumerate(tasks_with_due_date, 1):
            status = "Completada" if task['completed'] else "Pendiente"
            print(f"{idx}. [{status}] {task['description']} - Fecha límite: {task['due_date']}")

# Función principal que gestiona el flujo del programa
def main():
    manager = TaskManager()

    while True:
        print("\n--- Organizador Personal ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como realizada")
        print("4. Editar tarea")
        print("5. Eliminar tarea")
        print("6. Agregar fecha de vencimiento")
        print("7. Categorizar tarea")
        print("8. Establecer recordatorio")
        print("9. Ver tareas por fecha")
        print("0. Salir")
        
        choice = input("Elige una opción: ")

        if choice == '1':
            description = input("Descripción de la tarea: ")
            due_date = input("Fecha límite (YYYY-MM-DD) o enter para omitir: ")
            category = input("Categoría (Personal, Escuela, Hobby) o enter para omitir: ")
            manager.add_task(description, due_date if due_date else None, category if category else None)

        elif choice == '2':
            manager.view_tasks()

        elif choice == '3':
            task_number = int(input("Número de tarea a marcar como realizada: "))
            manager.complete_task(task_number)

        elif choice == '4':
            task_number = int(input("Número de tarea a editar: "))
            new_description = input("Nueva descripción de la tarea: ")
            manager.edit_task(task_number, new_description)

        elif choice == '5':
            task_number = int(input("Número de tarea a eliminar: "))
            manager.delete_task(task_number)

        elif choice == '6':
            task_number = int(input("Número de tarea: "))
            due_date = input("Fecha límite (YYYY-MM-DD): ")
            manager.add_due_date(task_number, due_date)

        elif choice == '7':
            task_number = int(input("Número de tarea: "))
            category = input("Categoría (Personal, Escuela, Hobby): ")
            manager.categorize_task(task_number, category)

        elif choice == '8':
            task_number = int(input("Número de tarea: "))
            reminder_time = int(input("Horas antes del plazo para recordar: "))
            manager.add_reminder(task_number, reminder_time)

        elif choice == '9':
            manager.view_tasks_by_due_date()

        elif choice == '0':
            print("Saliendo del organizador. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()