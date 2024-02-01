import os
import shutil
from Programms.use_functions import separator
from Programms.use_functions import my_money

def add_separators(f):
    def inner(*args, **kwargs):
        print(separator('*', 20))
        result = f(*args, **kwargs)
        print(separator('*', 20))
    return inner

@add_separators
def select_objects_to_file():
    """
    Недетерминированная функция
    :return: ничего не  возвращает
        """
    all_objects = os.listdir()
    only_files = [object for object in all_objects if os.path.isfile(object)]
    only_dir = [object for object in all_objects if os.path.isdir(object)]
    print(only_files)
    print(only_dir)

    with open('listdir.txt', 'w', encoding='utf-8') as file_write:
        file_write.write(f'Files: \n')
        for file in only_files:
            file_write.write(f'    {file}\n')
        file_write.write(f'Directory: \n')
        for dir in only_dir:
            file_write.write(f'    {dir}\n')


def add_text_to_file(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(result, 'w', encoding='utf-8') as file_write:
            file_write.write(f'Учебный файл: \n')
            file_write.write(input("Введите текст:"))
        return result
    return wrapper


@add_text_to_file
def new_file():
    """
    Недетерминированная функция
    :return: new_path
    """
    try:
        new_folder = input('Создать папку (введите путь): ')
        os.mkdir(new_folder)
    except FileExistsError:
        print("Такая папка уже  есть:", '\n', new_folder)
    try:
        new_file = input('Введите имя нового файла: ')
        new_path = new_folder + "\\" + new_file
        open(new_path, 'x', encoding='utf-8')
        print('Создан новый файл: {}'.format(new_path))
    except FileExistsError:
        print("Такой файл  уже  есть:", '\n', new_path)
    return new_path

@add_separators
def console_menu():
    while True:
        print("Меню: ")
        print('1. создать папку')
        print('2. удалить папку)')
        print('3. создать директорию с новым файлом)')
        print('4. копировать (файл/папку)')
        print('5. просмотр содержимого рабочей директории')
        print('6. просмотреть только файлы')
        print('7. просмотреть только папки')
        print('8. просмотр информации об операционной системе')
        print('9. размер файла')
        print('10. играть в викторину')
        print('11. мой банковский счет')
        print('12. смена рабочей директории')
        print('13. просмотр содержимого рабочей директории')
        print('14. сохранить содержимое рабочей директории в файл')
        print('15. выход')
        print(separator('*', 20))

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            new_folder = input('Создать папку (введите путь): ')
            os.mkdir(new_folder) if not os.path.exists(new_folder) else print('Такая папка существует!')

        elif choice == '2':
            del_folder = input('Удалить папку (введите путь): ')
            os.rmdir(del_folder) if os.path.exists(del_folder) else print('Такой папки нет!')

        elif choice == '3':
            new_file()

        elif choice == '4':
            new_round = "да"
            while new_round == "да":
                path_copy = input('Введите путь исходного файла: ')
                if os.path.exists(path_copy):
                    name_copy = input('Введите путь нового файла: ')
                    if os.path.exists(name_copy):
                        print('Такой файл ЕСТЬ!')
                        break
                    shutil.copy(path_copy, name_copy)
                    print('Операция совершена!')
                else:
                    print('Такого файла НЕТ!')
                new_round = input("Хотите начать заново? (Да-Нет): ")
                new_round = new_round.lower()

        elif choice == '5':
            print(os.listdir())

        elif choice == '6':
            all_objects = os.listdir()
            only_files = [object for object in all_objects if os.path.isfile(object)]
            print("Файлы рабочей директории {}".format(only_files))

        elif choice == '7':
            all_objects = os.listdir()
            only_dir = [object for object in all_objects if os.path.isdir(object)]
            print("Папки рабочей директории {}".format(only_dir))

        elif choice == '8':
            env = os.environ
            for key, val in env.items():
                print(key, '--> ', val)

        elif choice == '9':
            try:
                size_file = input('Введите путь к нужному файлу: ')
            except FileNotFoundError:
                print("Файл не найден!!!")
            else:
                print('Размер файла: ', os.stat(size_file).st_size)

        elif choice == '10':
            from Programms import victory

        elif choice == '11':
            my_money()

        elif choice == '12':
            print('Текущая папка: ', os.getcwd())
            try:
                new_path = input('Перейти в: ')
                os.chdir(new_path)

            except FileNotFoundError:
                print("Нет такой  директории!!!")
            else:
                print('Совершен переход: ', os.getcwd())

        elif choice == '13':
            all_objects = os.listdir()
            only_files = [object for object in all_objects if os.path.isfile(object)]
            only_dir = [object for object in all_objects if os.path.isdir(object)]
            print("Файлы  рабочей директории {}".format(only_files))
            print("Папки рабочей директории {}".format(only_dir))

        elif choice == '14':
            select_objects_to_file()

        elif choice == '15':
            break
        else:
            print('Неверный пункт меню')


console_menu()
