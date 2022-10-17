import os
import shutil
from Programms.use_functions import separator

print(separator('*', 20))
print("Меню: ")


def select_objects():
    all_objects = os.listdir()
    only_files = []
    only_dir = []
    for object in all_objects:
        if os.path.isfile(object):
            only_files.append(object)
        if os.path.isdir(object):
            only_dir.append(object)

    with open('listdir.txt', 'w', encoding='utf-8') as file_write:
        file_write.write(f'Files: \n')
        for file in only_files:
            file_write.write(f'    {file}\n')
        file_write.write(f'Directory: \n')
        for dir in only_dir:
            file_write.write(f'    {dir}\n')


while True:
    print('1. создать папку/файл')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. просмотреть только папки')
    print('6. просмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. просмотр содержимого рабочей директории')
    print('13. сохранить содержимое рабочей директории в файл')
    print('14. выход')

    print(separator('*', 20))

    choice = input('Выберите пункт меню: ')
    print(separator('*', 20))
    if choice == '1':
        new_folder = input('Создать папку (введите путь): ')
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        else:
            print('Такая папка существует!')
    elif choice == '2':
        del_folder = input('Удалить папку (введите путь): ')
        if os.path.exists(del_folder):
            os.rmdir(del_folder)
        else:
            print('Такой папки нет!')
    elif choice == '3':
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
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':
        all_objects = os.listdir()
        only_files = []
        for object in all_objects:
            if os.path.isfile(object):
                only_files.append(object)
            print(only_files)
    elif choice == '6':
        all_objects = os.listdir()
        only_dir = []
        for object in all_objects:
            if os.path.isdir(object):
                only_dir.append(object)
        print(only_dir)
    elif choice == '7':
        env = os.environ
        for key, val in env.items():
            print(key, '--> ', val)
    elif choice == '8':
        size_file = input('Введите путь к нужному файлу: ')
        print('Размер файла: ', os.stat(size_file).st_size)
    elif choice == '9':
        from Programms import victory
    elif choice == '10':
        from Programms import use_functions
    elif choice == '11':
        print ('Текущая папка: ', os.getcwd())
        new_path = input('Перейти в: ')
        os.chdir(new_path)
        print('Совершен переход: ', os.getcwd())
    elif choice == '12':
        print('Текущая папка: ', os.getcwd())
        new_path = input('Перейти в: ')
        os.chdir(new_path)
        print('Совершен переход: ', os.getcwd())
    elif choice == '13':
        select_objects()
    elif choice == '14':
        break
    else:
        print('Неверный пункт меню')
    print(separator('*', 20))
