from src.phoneBook import *


def main_menu(phoneBook: dict):
    while True:
        try:
            options_menu = ("1 Добавить Контакт", "2 Поиск Контакта", "3 Удалить Контакт",
                            "4 Изменение Контакта", "5 Отчет о Контактах", "6 Выход")
            print(" ")
            print("--------------МЕНЮ-----------------")
            for option in options_menu:
                print(option)
            print(" ")
            print("--------------------------------------")
            print(" ")

            option = int(input('Выбрать опцию: '))
            if option in range(1, len(options_menu)+1):
                if option == 1:
                    create_contact(phoneBook)
                elif option == 2:
                    search_contact(phoneBook)
                elif option == 3:
                    delete_contact(phoneBook)
                elif option == 4:
                    update_contact(phoneBook)
                elif option == 5:
                    create_report(phoneBook)
                elif option == 6:
                    break
            else:
                print("Неверный вариант")
                continue
        except ValueError:
            print("Неверный вариант")
            continue
        except EOFError:
            break
