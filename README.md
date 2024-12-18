# goit-cs-hw-03

## Завдання 1

### Порядок запуску
* скопіювати [.env.example](.env.example) в [.env](.env)
* змінити значення при потребі
* виконати `docker-compose up -d`
* встановити python пакети - `pip install -r requirements.txt`
* виконати `seed.py`
* виконати sql скрипт `psql -U admin -d task_management -h localhost -f task1.sql`, рекомендація: виконувати через вбудований("рідний") клієнт (були проблеми з деякими IDE) 
