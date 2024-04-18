from typing import Callable, List


# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
def notebook():
    todo_list = []

    def add_todo(task):
        nonlocal todo_list
        todo_list.append(task)
        print("Нова справа додана:", task)

    def get_all():
        return todo_list

    return add_todo, get_all


add_todo, get_all = notebook()

add_todo("Прибрати кімнату")
add_todo("Зробити покупки")
add_todo("Написати звіт")
add_todo("Зробити дз по пітону")

all_tasks = get_all()
print("Список справ:", ', '.join(all_tasks))


# протипізувати перше завдання
def notebook2() -> [Callable[[str], None], Callable[[None], List[str]]]:
    todo_list: List[str] = []

    def add_todo(task: str) -> None:
        nonlocal todo_list
        todo_list.append(task)
        print("Нова справа додана:", task)

    def get_all() -> List[str]:
        return todo_list

    return add_todo, get_all


add_todo, get_all = notebook2()


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
def expanded_form(number: int) -> str:
    digits = str(number)
    result = []

    for i, digit in enumerate(digits):
        if digit != '0':
            result.append(digit + '0' * (len(digits) - i - 1))

    return ' + '.join(result)


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій

def call_counter(func):
    calls = 0

    def inner(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('*' * 20)
        print(f'Call count : {calls}')
        func(*args, **kwargs)
        print('*' * 20)

    return inner


@call_counter
def function1():
    print('function1')


@call_counter
def function2():
    print('function2')


function1()
function1()
function1()

function2()
function2()
function1()
