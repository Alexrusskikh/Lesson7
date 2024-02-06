# импорт функций из модуля Programms.use_functions
import datetime
import json
import os

from Programms.use_functions import separator, put_cash, buy, balance, history_buys, history_only, \
    removal_cash, datetime, json

# переменные для текущих данных
traffic_money = []
# общий список в виде кортежей из 3 и 4 элементов

data = (datetime.date.today().strftime("%d.%m.%Y"))  # печать текущей даты
time = (datetime.datetime.now().time())

user_name = (input('Назовите себя:')).lower()
# открытие файла всех транзакций  на чтение и передача данных в traffic_money
if os.path.exists('traffic_money.json'):  # проверка наличия файла
    with open(f'{user_name}_traffic_money.json', 'r', encoding='utf-8') as file_read:
        # файл всех транзакций открывается на чтение и передает данные в traffic_money
        traffic_money = json.load(file_read)



while True:
    print(separator('*', 25))
    print("Сегодня", data)
    print("Время", time)

    print(separator('*', 25))
    print("Балланс счета: ", balance(traffic_money))  # начальное состояние счета

    print(separator('*', 25))
    print('Меню: ')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. снятие средств')
    print('4. история транзакций')
    print('5. история покупок')
    print('6. выход')
    print(separator('*', 25))

    choice = input('Выберите пункт меню: ')

    if choice == '1':  # добавляет в traffic_money и balance_only
        put_cash(traffic_money, data)

    elif choice == '2':  # добавляет в traffic_money транзакцию и buys_only
        buy(traffic_money, data)

    elif choice == '3':  # добавляет с "-" в traffic_money и balance_only
        removal_cash(traffic_money, data)

    elif choice == '4':
        history_only(traffic_money)  # вывод всей детализации операций

    elif choice == '5':
        history_buys(traffic_money)  # вывод детализации покупок

    elif choice == '6':
        with open(f'{user_name}_traffic_money.json', 'w', encoding='utf-8') as file_write:  # содержит все транзакции
            json.dump(traffic_money, file_write)
        break
    else:
        print('Неверный пункт меню')
