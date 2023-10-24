import sys
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, category, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.category = category
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f'Title: {self.title}, Description: {self.description}, ' \
               f'Due Date: {self.due_date}, Category: {self.category}, ' \
               f'Priority: {self.priority}, Status: {status}'

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.completed = True
            print(f'Task "{task.title}" marked as completed.')
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f'Task "{deleted_task.title}" deleted from the list.')
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            print("Task List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {str(task)}')
        else:
            print("The task list is empty.")

def main():
    # Set the input encoding
    sys.stdin.reconfigure(encoding='utf-8')

    todo_list = TodoList()

    while True:
        print("\nChoose an option:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter the option number: ")

        if choice == '1':
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            due_date_str = input("Enter the task due date (optional - format: dd/mm/yyyy): ")
            category = input("Enter the task category: ")
            priority = input("Enter the task priority (high, medium, low): ")

            try:
                due_date = datetime.strptime(due_date_str, '%d/%m/%Y').date() if due_date_str else None
                task = Task(title, description, due_date, category, priority)
                todo_list.add_task(task)
                print(f'Task "{task.title}" added to the list.')
            except ValueError:
                print("Invalid due date format. Use the format dd/mm/yyyy or leave it blank.")

        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter the number of the completed task: "))
                todo_list.complete_task(task_index)
            except ValueError:
                print("Invalid index. It should be an integer.")
        elif choice == '4':
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter the number of the task to delete: "))
                todo_list.delete_task(task_index)
            except ValueError:
                print("Invalid index. It should be an integer.")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
