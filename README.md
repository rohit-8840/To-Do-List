# Django To-Do List App (Beginner Project)

## 1. Setup
```bash
python -m venv venv
```
Activate the virtual environment:
- Windows CMD: `venv\Scripts\activate`
- Windows PowerShell: `.\venv\Scripts\Activate.ps1`
- macOS/Linux: `source venv/bin/activate`

## 2. Install Django
```bash
python -m pip install -r requirements.txt
```

## 3. Create database tables
```bash
python manage.py makemigrations
python manage.py migrate
```

## 4. Run the website
```bash
python manage.py runserver
```
Open http://127.0.0.1:8000/

## Features
- Add tasks
- Mark tasks complete/incomplete
- Edit tasks
- Delete tasks
- SQLite database storage

## Project structure
- `config/`: Django project configuration and main URLs
- `tasks/`: To-do app (model, views, URLs)
- `tasks/templates/tasks/`: HTML templates
- `tasks/static/tasks/style.css`: CSS styling
