**Blogicum** — это веб-приложение на базе веб-фреймворка Django, представляющее собой платформу для публикации блогов с возможностью категоризации постов, отложенной публикации и управления локациями.

## Стек технологий
* **Python** 3.14
* **Django** 5.2.16
* **SQLite** (база данных для разработки)
* **Git** (система контроля версий)

## Как развернуть и запустить проект локально

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com
   cd django-sprint3
   ```

2. **Cоздайте и активируйте виртуальное окружение:**
   * На Windows:
     ```bash
     python -m venv venv
     source venv/Scripts/activate
     ```
   * На macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Выполните миграции базы данных:**
   ```bash
   python blogicum/manage.py migrate
   ```

5. **Запустите локальный сервер разработки:**
   ```bash
   python blogicum/manage.py runserver
   ```

## 🧑‍💻 Автор проекта
* **Староверов Никита** — https://github.com/Giggsa1703
