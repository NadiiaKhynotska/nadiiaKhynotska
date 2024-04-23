# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return abs(self.area() - other.area())

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __len__(self):
        return (self.x + self.y) * 2


rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 6)

print("Площа rect1:", rect1.area())
print("Площа rect2:", rect2.area())

print("сумма площин двох екземплярів ксласу:", rect1 + rect2)
print("різниця площин двох екземплярів ксласу:", rect1 - rect2)

print("== площин на рівність", rect1 == rect2)
print("!= площин на не рівність", rect1 != rect2)

print(" >  більше", rect1 > rect2)
print(" < меньше ", rect1 < rect2)

print("Сума сторін першого прямокутника:", len(rect1))
print("Сума сторін другого прямокутника:", len(rect2))


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    count = 0

    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella.count += 1

    @classmethod
    def display_count(cls):
        print("Кількість Попелюшок:", cls.count)


class Prince(Human):
    def __init__(self, name, age, found_shoe_size):
        super().__init__(name, age)
        self.found_shoe_size = found_shoe_size

    def find_cinderella(self, cinderellas):
        for cinderella in cinderellas:
            if cinderella.shoe_size == self.found_shoe_size:
                return cinderella
        return None


cinderellas: list[Cinderella] = [Cinderella("Мотря", 34, 28), Cinderella("Гапка", 78, 45), Cinderella("Одарка", 25, 26)]

Cinderella.display_count()

prince = Prince("Оксен", 30, 41)
found_cinderella = prince.find_cinderella(cinderellas)
if found_cinderella:
    print(f"Та сама для {prince.name}:", found_cinderella.name)
else:
    print(f"{prince.name} - Шукай далі")

prince2 = Prince("Лаврін", 30, 26)
found_cinderella2 = prince2.find_cinderella(cinderellas)

if found_cinderella2:
    print(f"Та сама для {prince2.name}:", found_cinderella2.name)
else:
    print(f"{prince2.name} - Шукай далі")

#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу


from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Book: {self.name}")


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Magazine: {self.name}")


class Main:
    printable_list = []

    @classmethod
    def add(cls, item):
        if isinstance(item, (Book, Magazine)):
            cls.printable_list.append(item)
        else:
            print("not a book or magazine")

    @classmethod
    def show_all_books(cls):
        print("All books:")
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()

    @classmethod
    def show_all_magazines(cls):
        print("All magazines:")
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()


book1 = Book("Python Programming")
magazine1 = Magazine("Barvinok")
book2 = Book("Atomic Habits")

Main.add(book1)
Main.add(magazine1)
Main.add(book2)

Main.show_all_books()
Main.show_all_magazines()
