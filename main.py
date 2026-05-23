import json
import os

# Файл для сохранения задач
TASKS_FILE = "tasks.json"

def load_tasks():
    """Загружаем задачи из файла при старте"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Сохраняем задачи в файл"""
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(tasks):
    """Добавление задачи"""
    print("\n" + "="*40)
    task = input("📝 Введите задачу: ")
    if task.strip():
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("✅ Задача добавлена!")
    else:
        print("⚠️  Задача не может быть пустой!")
    print("="*40)
    input("\n👉 Нажмите Enter для возврата в меню...")

def show_tasks(tasks):
    """Отображение всех задач"""
    print("\n" + "="*40)
    print("📋 ВАШИ ЗАДАЧИ:")
    print("="*40)
    
    if not tasks:
        print("📭 Список задач пуст")
    else:
        for i, item in enumerate(tasks, 1):
            status = "✅" if item["done"] else "⬜"
            print(f"{i}. {status} {item['task']}")
    print("="*40)

def mark_done(tasks):
    """Отметка задачи как выполненной"""
    print("\n" + "="*40)
    print("📋 ТЕКУЩИЕ ЗАДАЧИ:")
    print("="*40)
    
    if not tasks:
        print("📭 Нет задач для отметки")
        print("="*40)
        input("\n👉 Нажмите Enter для возврата в меню...")
        return
    
    # Показываем список задач
    for i, item in enumerate(tasks, 1):
        status = "✅" if item["done"] else "⬜"
        print(f"{i}. {status} {item['task']}")
    print("="*40)
    
    try:
        num = int(input("🔢 Введите номер задачи для отметки: "))
        if 1 <= num <= len(tasks):
            if tasks[num-1]["done"]:
                print("⚠️  Эта задача уже выполнена!")
            else:
                tasks[num-1]["done"] = True
                save_tasks(tasks)
                print("✅ Задача отмечена как выполненная!")
        else:
            print("❌ Неверный номер задачи!")
    except ValueError:
        print("❌ Введите число!")
    print("="*40)
    input("\n👉 Нажмите Enter для возврата в меню...")

def delete_task(tasks):
    """Удаление задачи"""
    print("\n" + "="*40)
    print("📋 ТЕКУЩИЕ ЗАДАЧИ:")
    print("="*40)
    
    if not tasks:
        print("📭 Нет задач для удаления")
        print("="*40)
        input("\n👉 Нажмите Enter для возврата в меню...")
        return
    
    # Показываем список задач
    for i, item in enumerate(tasks, 1):
        status = "✅" if item["done"] else "⬜"
        print(f"{i}. {status} {item['task']}")
    print("="*40)
    
    try:
        num = int(input("🔢 Введите номер задачи для удаления: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            save_tasks(tasks)
            print(f"🗑️  Задача удалена: '{removed['task']}'")
        else:
            print("❌ Неверный номер задачи!")
    except ValueError:
        print("❌ Введите число!")
    print("="*40)
    input("\n👉 Нажмите Enter для возврата в меню...")

def sort_tasks(tasks):
    """Сортировка задач: сначала невыполненные, потом выполненные"""
    print("\n" + "="*40)
    if not tasks:
        print("📭 Нет задач для сортировки")
        print("="*40)
        input("\n👉 Нажмите Enter для возврата в меню...")
        return

    # Сортируем: False (невыполненные) идут раньше True (выполненные)
    tasks.sort(key=lambda x: x["done"])
    
    save_tasks(tasks)  # Сохраняем новый порядок в файл
    
    print("✅ Задачи отсортированы!")
    print("📋 Сначала идут активные задачи, затем выполненные.")
    print("="*40)
    input("\n👉 Нажмите Enter для возврата в меню...")

def show_menu():
    """Показываем меню"""
    print("\n" + "="*40)
    print("🎯 TODO LIST - МЕНЮ")
    print("="*40)
    print("1. ➕ Добавить задачу")
    print("2. 📋 Показать все задачи")
    print("3. ✅ Отметить задачу выполненной")
    print("4. 🗑️  Удалить задачу")
    print("5. 🔄 Сортировать задачи")
    print("6. 🚪 Выход")
    print("="*40)

def main():
    """Главная функция"""
    tasks = load_tasks()
    print("\n🎯 Добро пожаловать в TodoList!")
    
    while True:
        show_menu()
        choice = input("Выберите пункт меню (1-6): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
            input("\n👉 Нажмите Enter для возврата в меню...")
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            sort_tasks(tasks)
        elif choice == "6":
            print("\n👋 До свидания! Хорошего дня!")
            break
        else:
            print("\n❌ Неверный выбор! Попробуйте снова.")
            input("\n👉 Нажмите Enter для возврата в меню...")

if __name__ == "__main__":
    main()