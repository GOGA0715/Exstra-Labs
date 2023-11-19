import re

def main():
    users_list = []

    while True:
        print("\n===== Журнал Пользователей =====")
        print("1. Посмотреть список пользователей")
        print("2. Добавить нового пользователя")
        print("3. Редактировать пользователя")
        print("4. Удалить пользователя")
        print("5. Выйти из программы")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            show_users(users_list)
        elif choice == "2":
            add_user(users_list)
        elif choice == "3":
            edit_user(users_list)
        elif choice == "4":
            delete_user(users_list)
        elif choice == "5":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите от 1 до 5.")

def show_users(users_list):
    if not users_list:
        print("Список пользователей пуст.")
    else:
        print("\n===== Список пользователей =====")
        for user in users_list:
            print(user)

def add_user(users_list):
    user = {}
    user["Name"] = input("Введите имя: ")
    user["Surname"] = input("Введите фамилию: ")
    user["Age"] = input("Введите возраст: ")

    while True:
        email = input("Введите уникальную почту: ")
        if not is_email_unique(users_list, email):
            print("Почта должна быть уникальной. Пожалуйста, введите другую почту.")
        else:
            user["Username"] = email
            break

    user["Password"] = input("Введите пароль (минимум 8 символов): ")
    while len(user["Password"]) < 8:
        print("Пароль слишком короткий. Минимальная длина 8 символов.")
        user["Password"] = input("Введите пароль еще раз: ")

    user["Address"] = input("Введите адрес: ")

    users_list.append(user)
    print("Пользователь успешно добавлен.")

def edit_user(users_list):
    username = input("Введите почту пользователя, которого вы хотите отредактировать: ")
    user = find_user_by_username(users_list, username)

    if user:
        print("\nРедактирование пользователя:")
        print("1. Имя")
        print("2. Фамилия")
        print("3. Возраст")
        print("4. Почта")
        print("5. Пароль")
        print("6. Адрес")
        print("7. Вернуться в главное меню")

        choice = input("Выберите поле для редактирования (1-7): ")

        if choice == "1":
            user["Name"] = input("Введите новое имя: ")
        elif choice == "2":
            user["Surname"] = input("Введите новую фамилию: ")
        elif choice == "3":
            user["Age"] = input("Введите новый возраст: ")
        elif choice == "4":
            new_email = input("Введите новую уникальную почту: ")
            if is_email_unique(users_list, new_email):
                user["Username"] = new_email
            else:
                print("Почта должна быть уникальной. Редактирование отменено.")
        elif choice == "5":
            new_password = input("Введите новый пароль (минимум 8 символов): ")
            while len(new_password) < 8:
                print("Пароль слишком короткий. Минимальная длина 8 символов.")
                new_password = input("Введите пароль еще раз: ")
            user["Password"] = new_password
        elif choice == "6":
            user["Address"] = input("Введите новый адрес: ")
        elif choice == "7":
            print("Редактирование отменено.")
        else:
            print("Некорректный выбор. Пожалуйста, выберите от 1 до 7.")
    else:
        print("Пользователь с указанной почтой не найден.")

def delete_user(users_list):
    username = input("Введите почту пользователя, которого вы хотите удалить: ")
    user = find_user_by_username(users_list, username)

    if user:
        users_list.remove(user)
        print("Пользователь успешно удален.")
    else:
        print("Пользователь с указанной почтой не найден.")

def is_email_unique(users_list, email):
    return all(user["Username"] != email for user in users_list)

def find_user_by_username(users_list, username):
    for user in users_list:
        if user["Username"] == username:
            return user
    return None

if __name__ == "__main__":
    main()
