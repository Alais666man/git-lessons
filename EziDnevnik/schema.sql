import sqlite3
conn = sqlite3.connect('db.egednev')
cursor = conn.cursor()
# создаём таблицу tasks если не существует
# первое поле основной ключ(primary id)
# дата задания (???день\месяц\год)
# имя задания (не может быть null ?)
# текст задания (по умолчанию пустая строка)
# время задания (день\месяц\год)
#
sql = '''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATETIME
        task_name TEXT NOT NULL,
        task_text TEXT DEFAULT '',
        task_time DATETIME NOT NULL
    )
'''

cursor.execute(sql)
conn.commit()

sql = '''
    INSERT INTO tasks (task_name, task_text, task_time) VALUES (?)
'''

cursor.execute(sql,())
conn.commit()

# Выбор для взаимодействия
sql = '''
    SELECT
        id, date, task_name, task_text, task_time
    FROM
        tasks
'''
cursor.execute(sql)
result = cursor.fetchall()
print(result)

cone.close()














