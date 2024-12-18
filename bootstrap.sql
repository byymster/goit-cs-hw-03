-- Створення таблиці користувачів
CREATE TABLE users
(
    id       SERIAL PRIMARY KEY,           -- Первинний ключ, автоінкремент
    fullname VARCHAR(100)        NOT NULL, -- Повне ім'я користувача
    email    VARCHAR(100) UNIQUE NOT NULL  -- Електронна адреса користувача (унікальна)
);

-- Створення таблиці статусів
CREATE TABLE status
(
    id   SERIAL PRIMARY KEY,         -- Первинний ключ, автоінкремент
    name VARCHAR(50) UNIQUE NOT NULL -- Назва статусу (унікальна)
);

-- Створення таблиці завдань
CREATE TABLE tasks
(
    id          SERIAL PRIMARY KEY,                             -- Первинний ключ, автоінкремент
    title       VARCHAR(100) NOT NULL,                          -- Назва завдання
    description TEXT,                                           -- Опис завдання
    status_id   INTEGER REFERENCES status (id),                 -- Зовнішній ключ на статус
    user_id     INTEGER REFERENCES users (id) ON DELETE CASCADE -- Зовнішній ключ на користувача з каскадним видаленням
);