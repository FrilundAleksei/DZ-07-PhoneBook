from src.validation import *


def init_phoneBook():
    phoneBook = {}
    return phoneBook


def create_contact(phoneBook: dict):

    try:
        while True:
            while True:
                name = valid_name(input('Имя: '))
                if name != False:
                    break
                elif name == False:
                    print("Имя введено некорректно")
                    continue
                else:
                    print(name)
                    continue

            while True:
                phone = valid_phone(input('Телефон(12 цифр): '))
                if phone != False:
                    break
                elif phone == False:
                    print("Телефон введен не корректно")
                    continue
                else:
                    print(phone)
                    continue

            while True:
                mail = valid_mail(input('Электронная почта: '))
                if mail != False:
                    break
                elif mail == False:
                    print("Электронная почта введена не корректно")
                    continue
                else:
                    print(mail)
                    continue

            phoneBook[name] = [phone, mail]
            addContact = search_contact(phoneBook, name)
            if addContact != False:
                print("Контакт успешно добавлен")
                print(addContact)
            elif addContact == False:
                print("Контакт не был добавлен (ошибка)")
            else:
                print(addContact)
                print("Ошибка при добавлении контакта")

            optionNewContact = False
            while True:
                newContact = input(str("Добавить новый контакт (Y/N)?"))
                if newContact == "y" or newContact == "Y":
                    optionNewContact = True
                    break
                elif newContact == "n" or newContact == "N":
                    optionNewContact = False
                    break
                else:
                    print("Неверный вариант.")
                    continue
            if optionNewContact == True:
                continue
            elif optionNewContact == False:
                break
            else:
                ("Произошла ошибка")

    except ValueError as err:
        print(err)


def search_contact(phoneBook: dict, name=""):

    try:
        if len(name) > 1:
            name = valid_name(name)
            if name != False:
                if name in phoneBook.keys():
                    return f"{name}, {phoneBook[name][0]}, {phoneBook[name][1]}"

                elif name not in phoneBook.keys():
                    return False
                else:
                    return "Неожиданная ошибка"
            elif name == False:
                return "Неверное имя"
            else:
                print(name)

        else:
            while True:
                name = valid_name(input("Поиск по названию: "))
                if name != False:
                    if name in phoneBook.keys():
                        print(
                            f'{"Имя":<25}{"Телефон":<20}{"Электронная почта":<30}')
                        print(
                            f"{name:<25}{phoneBook[name][0]:<20}{phoneBook[name][1]:<30}")
                        break
                    elif name not in phoneBook.keys():
                        print("Контакт не найден")
                        continue
                    else:
                        print("Ошибка поиска контакта")
                        break
                elif name == False:
                    print("Неверное имя")
                    continue
                    break
                else:
                    print(name)
                    break

    except ValueError as err:
        print(err)


def update_contact(phoneBook: dict):
    try:
        while True:
            while True:
                oldName = valid_name(input("Поиск по названию: "))
                if oldName != False:
                    break
                elif oldName == False:
                    print("Неверное имя")
                    continue
                else:
                    print(oldName)
                    break
            contact = search_contact(phoneBook, name=oldName)
            if contact != False:
                print(contact)

                optionUpdate = valid_choice("Изменить контакт")
                if optionUpdate == True:
                    while True:
                        newName = valid_name(input('Новое имя: '))
                        if newName != False:
                            break
                        elif newName == False:
                            print("Неверное имя")
                            continue
                        else:
                            print(newName)
                            break

                    while True:
                        newPhone = valid_phone(input('Новый телефон: '))
                        if newPhone != False:
                            break
                        elif newPhone == False:
                            print("Недействительный телефон")
                            continue
                        else:
                            print(newPhone)
                            break

                    while True:
                        newMail = valid_mail(
                            input('Новая электронная почта: '))
                        if newMail != False:
                            break
                        elif newMail == False:
                            print("Неверная электронная почта")
                            continue
                        else:
                            print(newMail)
                            break
                    phoneBook[newName] = phoneBook[oldName]
                    del phoneBook[oldName]
                    phoneBook[newName] = [newPhone, newMail]

                    contactUpdatedCall = search_contact(phoneBook, newName)
                    if contactUpdatedCall != False:
                        print("Контакт успешно обновлен")
                        print(contactUpdatedCall)
                        break
                    elif contactUpdatedCall == False:
                        print("Ошибка обновления контакта")
                        break
                    else:
                        print(contactUpdatedCall)
                        break

                elif optionUpdate == False:
                    break
                else:
                    print("Ошибка операции")
                    break

            elif contact == False:
                print("Контакт не найден")
                continue
            else:
                print("Произошла ошибка")
                break

    except ValueError as err:
        print(err)


def delete_contact(phoneBook: dict):

    while True:
        delContact = valid_name(input("Поиск по названию: "))
        if delContact != False:
            contact = search_contact(phoneBook, name=delContact)
            if contact != False:
                print(contact)
            optionUpdate = valid_choice("Удалить Контакт")
            if optionUpdate == True:
                del phoneBook[delContact]
                print("Контакт удален")
                break
            elif optionUpdate == False:
                break
            else:
                print("Ошибка операции")
                break
        elif delContact == False:
            print("Неверное имя")
            continue
        else:
            print(delContact)
            break


def create_report(phoneBook: dict):
    print(f'{"СПИСОК КОНТАКТОВ":^101}')
    print("-----------------------------------------------------------------------------------")
    print(f'{"№":<10}{"Имя":<25}{"Телефон":<20}{"Электронная почта":<30}')
    print("-----------------------------------------------------------------------------------")
    idContact = 1
    for name in phoneBook.keys():

        print(
            f'{idContact:<10}{name:<25}{phoneBook[name][0]:<20}{phoneBook[name][1]:<30}')
        idContact += 1
