import os
import random

import psycopg2
# Підключення до PostgreSQL
from dotenv import load_dotenv
from faker import Faker

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
cursor = conn.cursor()

# Ініціалізація Faker
fake = Faker()

# Видалення попереднього стану
cursor.execute("TRUNCATE TABLE users RESTART IDENTITY CASCADE;")
cursor.execute("TRUNCATE TABLE tasks RESTART IDENTITY CASCADE;")
cursor.execute("TRUNCATE TABLE status RESTART IDENTITY CASCADE;")

# Додавання статусів
statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cursor.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (status,))

# Генерація користувачів
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email)
    )

# Генерація завдань
cursor.execute("SELECT id FROM users")
user_ids = [row[0] for row in cursor.fetchall()]
cursor.execute("SELECT id FROM status")
status_ids = [row[0] for row in cursor.fetchall()]
for _ in range(50):
    title = fake.sentence(nb_words=6)
    description = fake.text() if random.choice([True, False]) else None
    status_id = random.choice(status_ids)
    user_id = random.choice(user_ids)
    cursor.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, status_id, user_id)
    )

# Генерація користувачів без задач
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email)
    )

# Збереження змін і закриття з'єднання
conn.commit()
cursor.close()
conn.close()