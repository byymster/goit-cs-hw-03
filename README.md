# goit-cs-hw-03

## Завдання 1

### Порядок запуску
1. скопіювати [.env.example](.env.example) в [.env](.env)
1. змінити значення при потребі
1. виконати `docker-compose up -d`
1. встановити python пакети - `pip install -r requirements.txt`
1. виконати `seed.py`
1. виконати sql скрипт `psql -U admin -d task_management -h localhost -f task1.sql`, рекомендація: виконувати через вбудований("рідний") клієнт (були проблеми з деякими IDE) 


## Завдання 2

### Порядок запуску
1. виконати п 1-4 із завдання 1 (якщо ще не виконували)
2. виконати [task2.py](task2.py)