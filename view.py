from import_data import *
from controller import *
import os
import time


def button_push():
    database_creation()
    print("Выберете функцию...\n"
          "1. - Добавление учащегося\n"
          "2. - Добавление учебного предмета\n"
          "3. - Добавить оценку ученику по предмету\n"
          "4. - Список учеников\n"
          "5. - Лист оценнок ученика\n"
          "0. - Выход \n")
    opp_tupe = int(input("->> "))
    os.system('cls')
    if opp_tupe == 1:
        print("Выберете нужную операцию:\n"
              "1. - Добавить одного ученика\n"
              "2. - Добавить(сгенерировать) несколько учеников\n")
        oppration = int(input("->> "))
        if oppration == 1:
            os.system('cls')
            input_data()
            print("Ученик добавлен!")
            time.sleep(2)
            os.system('cls')
            button_push()
        elif oppration == 2:
            os.system('cls')
            input_random_data()
            print("Ученики добавлены!")
            time.sleep(2)
            os.system('cls')
            button_push()
        else:
            print("Введено некоректное значение!")
            time.sleep(2)
            os.system('cls')
            button_push()
    elif opp_tupe == 2:
        os.system('cls')
        alter_table()
        print("Предмет добавлен!")
        time.sleep(2)
        os.system('cls')
        button_push()
    elif opp_tupe == 3:
        os.system('cls')
        input_grade()
        print("Оценка добавлена!")
        time.sleep(2)
        os.system('cls')
        button_push()
    elif opp_tupe == 4:
        os.system('cls')
        print_data()
        continue_d = input("Нажмите клавишу Enter для продолжения работы... ")
        os.system('cls')
        button_push()
    elif opp_tupe == 5:
        os.system('cls')
        print_id()
        continue_d = input(
            "\nНажмите клавишу Enter для продолжения работы... ")
        os.system('cls')
        button_push()
    elif opp_tupe == 0:
        print("До скорых встреч!")
        time.sleep(1)
        pass
    else:
        print("Команда не распознана!")
        time.sleep(1)
        button_push()
