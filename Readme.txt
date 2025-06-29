# 🚀 Django Internship Project

## Features
- JWT Authentication
- Public & Protected APIs
- Celery Email Task
- Telegram Bot Integration

## Setup
```bash
git clone 
cd project
pip install -r requirements.txt
python manage.py migrate
```

## Run Services
```bash
redis-server
celery -A myproject worker --loglevel=info
python manage.py runserver
```



