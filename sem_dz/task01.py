#   Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
#   Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


def enter_first_name():
    return input("Введите имя абонента: ").title()


def enter_second_name():
    return input("Введите фамилию абонента: ").title()


def enter_family_name():
    return input("Введите отчество абонента: ").title()


def enter_phone_number():
    return input("Введите номер: ")


def enter_addres_number():
    return input("Введите адрес абонента: ").title()


def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    addres = enter_addres_number()
    with open("book.txt", "a", encoding="utf-8") as file:
        file.write(f"{name} {surname} {family}\n{number}\n{addres}\n\n")


def print_data():
    with open("book.txt", "r", encoding="utf-8") as file:
        print(file.read())


def search_line():
    print(
        "Выберите вариант поиска: \n"
        "1. Имя\n"
        "2. Фамилия\n"
        "3. Отчество\n"
        "4. Телефон\n"
        "5. Адрес"
    )
    index = int(input("Введите вариант: ")) - 1
    searched = input("Введите поисковые данные: ").title()
    with open("book.txt", "r", encoding="utf-8") as file:
        data = file.read().strip().split("\n\n")
        for item in data:
            new_item = item.replace("\n", " ").split()
            if searched in new_item[index]:
                print(item, end="\n\n")
        # file.seek(0)
        # print(file.readlines())


def edit_data():
    with open("book.txt", "r", encoding="utf-8") as data:
        old_data = data.read()
        print(old_data)
        index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
        old_data_lines = old_data.split("\n")
        edit_old_data_lines = old_data_lines[index_delete_data]
        elements = edit_old_data_lines.split(" ")
        first_name = enter_first_name()
        second_name = enter_second_name()
        family_name = enter_family_name()
        phone = input(f"Введите номер телефона: {enter_phone_number}")
        num = elements[0]
        if len(first_name) and len(second_name) and (family_name) == 0:
            first_name == elements[1]
            second_name == elements[1]
            family_name == elements[1]
        if len(phone) == 0:
            phone == elements[2]
        edited_line = f"{num} {first_name} {second_name} {family_name} {phone}"
        old_data_lines[index_delete_data] = edited_line
        print(f"Запись - {edit_old_data_lines}, изменена на - {edited_line}\n")
        with open("book.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(old_data_lines))


def deleted_data():
    with open("book.txt", "r", encoding="utf-8") as data:
        tel_book = data.read()
        index_delete_data = int(input("Введите номер строки для удаления: \n")) - 1
        tel_book_lines = tel_book.split("\n")
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        print(f"Удалена запись: {del_tel_book_lines}\n")
        with open("book.txt", "w", encoding="utf-8") as data:
            data.write("\n".join(tel_book_lines))


def interface():
    cmd = 0
    while cmd != "6":
        print(
            "Выберите действие: \n"
            "1. Добваить контакт\n"
            "2. Вывести все контакты\n"
            "3. Поиск контакта\n"
            "4. Изменить контакт\n"
            "5. Удалить контакт\n"
            "6. Выход\n"
        )
        cmd = input("\n" "Выберите дейтсвие: ")
        while cmd not in ("1", "2", "3", "4", "5", "6"):
            print("Некоректный ввод")
            cmd = input("\n" "Выберите дейтсвие: ")
        match cmd:
            case "1":
                enter_data()
            case "2":
                print_data()
            case "3":
                search_line()
            case "4":
                edit_data()
            case "5":
                deleted_data()
            case "6":
                print("Всего доброго!")


interface()
