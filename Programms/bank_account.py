# импорт модулей
import datetime
import json
import os

# переменные для текущих данных
traffic_money = []  # общий список????

#put_money = []#поступление денег, кортеж из даты и суммы
#withdrawal_money = []#снятие средств
# balance_only = [] # сумма поступлений минус сумма снятий
buys_only = []# только покупки,  кортежи  из  дат, названий, сумм

# открытие файлов на чтение
# if os.path.exists('../traffic_money.json'):  # проверка наличия файла
#     with open('../traffic_money.json',
#               'r') as file_read:  # файл всех танзакций открывается на чтение и передает данные в traffic_money
#         traffic_money = json.load(file_read)
#         # print(*traffic_money, sep="\n")
#
# if os.path.exists('balance.txt'):  # проверка наличия файла
#     with open('balance.txt', 'r') as file_read:  # файл баланса, открывается на чтение и передает данные в balance_only
#         balance_only = [int(file_read.read())]
#
# if os.path.exists('../buys.txt'):  # проверка наличия файла
#     with open('../buys.txt', 'r',
#               encoding='utf-8') as file_read:  # файл buys, открывается на чтение и передает данные в buys_only
#         for buy in file_read:
#             buys_only.append(buy.replace('\n', ' '))
#             # print(*buys_only, sep="\n")


# все функции

def separator(symbol, count):
    """разделитель
    """
    return (symbol * count)

def balance():
    """
    вычисляет в balance_only сумму всех элементов, получаем балланс  счета
    :param balance_only:
    :return:
    """
    put_money = [ el[2] for el in traffic_money if el[0] == 'Поступление']  # поступление денег, кортеж из даты и суммы
    withdrawal_money = [el[2] for el in traffic_money if el[0] == 'Снятие' or 'Покупка']  # снятие средств

    balance = sum(put_money) - sum(withdrawal_money)
    return balance

def put_cash():
    """
    функция пополнения счета, запись кортежей из даты и суммы
    :return: ничего не  возвращает
    """
    amount_plus = int(input('Введите сумму для пополнения: '))
    # добавляет в traffic_money кортеж из 3 элементов
    traffic_money.append(('Поступление', data, amount_plus))

def removal_cash():
    """
    функция снятия со счета
    :return:  ничего не возвращает
    """
    amount_minus = int(input('Введите сумму для снятия: '))
    traffic_money.append(('Снятие', data, amount_minus))


def buy():
    """
    функция покупки кортеж из 3 элементов
    :return: ничего не  возвращает
    """
    #Ввод данных
    product_name = input('Введите название продукта: ')
    amount_minus = int(input('Введите сумму покупки: '))

    # withdrawal_money.append(('Покупка', data,  amount_minus, product_name))
    # buys_only.append(('Покупка', data,  amount_minus, product_name))
    traffic_money.append(('Покупка', data,  amount_minus, product_name))

def history_buys():
    """
    функция истории покупок
    :param buys_only:
    :return:
    """
    n = 0
    print('История покупок:')
    for el in buys_only:
        n += 1
        # вывод истории покупок построчно
        print(f'  {n}). Дата покупки: {el[1]}. Наименование: {el[3]}. Цена: {el[2]} УЕ')
    input('\nНажмите Enter чтобы продолжить ')


def history_only():  # функция истории транзакций
    print('История транзакций:')
    for el in traffic_money:
        if len(el) == 3:
            print(f'      {el[0]}: {el[1]}, {el[2]} УЕ')  # перебор кортежей и вывод их элементов через ":"
        if len(el) == 4:
            print(f'      {el[0]}: {el[1]}, {el[3]}, -  {el[3]}УЕ')
    input('\nНажмите Enter чтобы продолжить ')

while True:
    print(separator('*', 20))
    data = (datetime.date.today().strftime("%d.%m.%Y"))  # печать текущей даты
    print("Сегодня", data)
    print(separator('*', 20))
    print("Балланс счета: ", balance())  # начальное состояние счета

    print(separator('*', 20))
    print('Меню: ')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. снятие средств')
    print('4. история транзакций')
    print('5. история покупок')
    print('6. выход')
    print(separator('*', 20))

    choice = input('Выберите пункт меню: ')

    if choice == '1':  # добавляет в traffic_money и balance_only
        put_cash()

    elif choice == '2':  # добавляет в traffic_money транзакцию и buys_only
        buy()

    elif choice == '3':  # добавляет с "-" в traffic_money и balance_only
        removal_cash()

    elif choice == '4':
        history_only()  # вывод всей детализации операций

    elif choice == '5':
        history_buys()  # вывод детализации покупок

    elif choice == '6':
        with open('../traffic_money.json', 'w') as f:  # содержит все транзакции
            json.dump(traffic_money, f)
        with open('balance.txt', 'w', encoding='utf-8') as file_write:  # содержит баланс
            file_write.write(str(balance(balance_only)))
        with open('../buys.txt', 'w', encoding='utf-8') as file_write:  # содержит все покупки
            for buy in buys_only:
                file_write.write(f'{buy}\n')
        break
    else:
        print('Неверный пункт меню')
