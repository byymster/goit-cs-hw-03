  \set AUTOCOMMIT on
  \pset pager off

-- Отримати список всіх користувачів
SELECT *
FROM users;

\echo Отримати всі завдання певного користувача
\prompt 'Enter User ID to see his tasks: ' user_id
SELECT *
FROM tasks
WHERE user_id = :user_id;

\echo Вибрати завдання за певним статусом
\prompt 'Enter Status Name to see tasks(default - new): ' status_name
SELECT *, s.name
FROM tasks
         INNER JOIN status s on s.id = tasks.status_id
WHERE s.name = COALESCE(NULLIF(:'status_name', ''), 'new');

\echo Оновити статус конкретного завдання
\prompt 'Enter Task ID to update its status to in_progress: ' task_id
UPDATE tasks
SET status_id = (Select id from status where name = 'in progress')
WHERE id = :task_id;


\echo Отримати список користувачів, які не мають жодного завдання
SELECT *
FROM users
WHERE id NOT IN (SELECT DISTINCT user_id
                 FROM tasks);


\echo Додати нове завдання для конкретного користувача
\prompt 'Enter User ID: ' new_user_id
\prompt 'Enter Task Title: ' new_task_title
\prompt 'Enter Task Description: ' new_task_description
INSERT INTO tasks (user_id, title, description, status_id)
VALUES (:new_user_id, :'new_task_title', :'new_task_description',
        (SELECT id FROM status WHERE name = 'new'));


\echo Отримати всі завдання, які ще не завершено
SELECT *
FROM tasks
         INNER JOIN public.status s on s.id = tasks.status_id
WHERE s.name != 'completed';

\echo Видалити конкретне завдання
SELECT id, title, description
FROM tasks;
\prompt 'Enter Task ID to delete: ' task_id
DELETE
FROM tasks
WHERE id = :task_id;


\echo Знайти користувачів з певною електронною поштою
\prompt 'Enter the email (or part of it): ' user_email
SELECT *
FROM users
WHERE email LIKE '%' || :'user_email' || '%';

\echo "Оновити ім'я користувача"
\prompt 'Enter New User Fullname: ' new_fullname
\prompt 'Enter User ID for Fullname Update: ' user_id
UPDATE users
SET fullname = :'new_fullname'
WHERE id = :user_id;

\echo Отримати кількість завдань для кожного статусу
SELECT s.name, COUNT(*) AS task_count
FROM tasks
         INNER JOIN status s on s.id = tasks.status_id
GROUP BY s.name;


\echo Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
SELECT t.*, u.email
FROM tasks t
         JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

\echo Отримати список завдань, що не мають опису
SELECT *
FROM tasks
WHERE description IS NULL;

\echo "Вибрати користувачів та їхні завдання, які є у статусі 'in progress'"
SELECT t.*, u.*, st.name
FROM tasks as t
         INNER JOIN users as u ON t.user_id = u.id
         INNER JOIN status as st ON t.status_id = st.id
WHERE st.name = 'in progress';

\echo Отримати користувачів та кількість їхніх завдань
SELECT u.id, u.fullname, COUNT(t.id) AS task_count
FROM users u
         LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id, u.fullname
ORDER BY task_count DESC;
