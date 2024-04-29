# 1) Є ось такий файл... ваша задача записати в новий файл тільки email('ли з доменом'
# ' gmail.com (Хеш то що з ліва записувати не потрібно))
#


try:
    with open('emails.txt') as file, open('res.txt', 'w') as output_file:
        for line in file:
            if line.strip().lower().endswith('gmail.com'):
                print(line.split()[-1], file=output_file)
except Exception as err:
    print(err)

    # 2) Створити записну книжку покупок:
    # - у покупки повинна бути id, назва і ціна
    # - всі покупки зберігаємо в файлі
    # з функціоналу:
    #  * вивід всіх покупок
    #  * має бути змога додавати покупку в книгу
    # * має бути змога шукати по будь якому полю покупку
    # * має бути змога показати найдорожчу покупку
    # * має бути можливість видаляти покупку по id
    # (ну і меню на це все)

import json
from typing import TypedDict

Purchase = TypedDict('Purchase', {'id': int, 'name': str, 'price': int})


class ShoppingList:
    def __init__(self):
        self.__filename = input('Enter file name: ')
        self.__data: list[Purchase] = []
        self.__read_file()

    def __read_file(self):
        try:
            with open(self.__filename) as file:
                self.__data = json.load(file)
        except Exception as err:
            pass

    def __write_file(self):
        try:
            with open(self.__filename, 'w') as file:
                return json.dump(self.__data, file)
        except Exception as err:
            print(err)

    @staticmethod
    def __input_int(msg: str) -> int:
        while True:
            tmp = input(msg)

            if not tmp.isdigit():
                continue

            return int(tmp)

    def __show_all(self):
        for item in self.__data:
            print(item)
        print('-' * 20)

    def __add(self):
        pk = self.__data[-1]['id'] + 1 if self.__data else 1
        name = input('Enter name of purchase: ')
        price = self.__input_int('Enter price of purchase: ')
        self.__data.append({'id': pk, 'name': name, 'price': price})
        self.__write_file()

    def __search(self):
        search = input('Enter what you want to search: ')
        for item in self.__data:
            for value in item.values():
                if search in str(value):
                    print(item)

    def __most_expensive(self):
        if not self.__data:
            print('Empty list')
            return

        sorted_data = sorted(self.__data, key=lambda item: item['price'])
        print(sorted_data[-1])

    def __delete_by_id(self):
        self.__show_all()
        pk = self.__input_int('Enter id for delete: ')
        index = next((i for i, v in enumerate(self.__data) if v['id'] == pk), None)

        if index is None:
            print('Not found')
            return

        del self.__data[index]
        self.__write_file()

    def menu(self):
        while True:
            print('1) get all')
            print('2) add')
            print('3) search')
            print('4) most expensive')
            print('5) delete by id')
            print('9) exit')

            choice = input('Enter your choice: ')

            match choice:
                case '1':
                    self.__show_all()
                case '2':
                    self.__add()
                case '3':
                    self.__search()
                case '4':
                    self.__most_expensive()
                case '5':
                    self.__delete_by_id()
                case '9':
                    break

# note_book = ShoppingList()
# note_book.menu()


def unique_ids(data):
    added_ids = set()

    for sublist in data:
        for item in sublist:
            id_value = item['id']
            if id_value not in added_ids:
                yield id_value
                added_ids.add(id_value)

data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},
    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},
    ]
]

res = list(unique_ids(data))
print(res)

res2= []

gens = [(i['id'] for i in item if i['id'] not in res2) for item in data]

while gens:
    gen = gens.pop(0)

    try:
        res2.append(next(gen))
    except StopIteration:
        continue

    gens.append(gen)

print(res2)
