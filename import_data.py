import sqlite3
import random


def input_data():
    data_base = sqlite3.connect('pupils.db')
    cursor = data_base.cursor()
    last_name = input("Введите Имя: ")
    first_name = input("Введите Фамилию: ")
    data = (last_name, first_name)
    cursor.execute("INSERT INTO data (name, ferst_name) VALUES(?,?)", data)
    data_base.commit()
    data_base.close()


def input_random_data():
    data_base = sqlite3.connect('pupils.db')
    cursor = data_base.cursor()
    for i in range(50):
        last_name = random.SystemRandom().choice(
            ["Михаил", "Юрий", "Александр", "Дарья", "Вячеслав", "Дмитрий", "Мария"])
        first_name = random.SystemRandom().choice(
            ["Петров(а)", "Белов(а)", "Прямов(а)", "Дашин(а)", "Смирнов(а)", "Дмитриев(а)", "Простинов(а)"])
        data = (last_name, first_name)
        cursor.execute("INSERT INTO data (name, ferst_name) VALUES(?,?)", data)
        data_base.commit()
        i += 1
    data_base.close()


def alter_table():
    data_base = sqlite3.connect('pupils.db')
    cursor = data_base.cursor()
    name_sub = input("Введите название предмета: ")
    cursor.execute(f"ALTER TABLE data ADD COLUMN {name_sub} TEXT")
    data_base.commit()
    data_base.close()


def print_data():
    data_base = sqlite3.connect('pupils.db')
    cursor = data_base.cursor()
    with data_base:
        cursor.execute("SELECT id, name ,ferst_name FROM data")
        print("ID".center(0), "|".center(3), "Имя".center(
            10), "|".center(2), "Фамилия".center(15))
        print("_"*35)
        for person in cursor.fetchall():
            print(person[0],  person[1].center(20), person[2].center(12))


def print_id():
    data_base = sqlite3.connect('pupils.db')
    cursor = data_base.cursor()
    id_name = int(input("Введите ID ученика: "))
    cursor.execute('PRAGMA table_info(data)')
    data = cursor.fetchall()
    for d in data:
        if d == data:
            continue
        else:
            print(d[1].center(12), end=" ")
    print(f"\n"+"-"*100)
    cursor.execute(f"SELECT * FROM data WHERE id = {id_name}")
    finder = cursor.fetchone()
    for i in finder:
        print(f"".center(5), i, end=" ")


def input_grade():
    data_base = sqlite3.connect('pupils.db')
    cursor = data_base.cursor()
    input_id = int(input("Введите ID ученика: "))
    cursor.execute('PRAGMA table_info(data)')
    data = cursor.fetchall()
    for d in data:
        print(d[1])
    subject = input("Введите название предмета: \n")
    grade = input("Введите оценку: ")
    cursor.execute(
        f"UPDATE data SET {subject} = {grade} WHERE id = {input_id}")
    data_base.commit()
    data_base.close()