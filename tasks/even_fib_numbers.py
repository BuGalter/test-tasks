"""Модуль even_fib_numbers используется для поиска положительных чисел
Фибаначчи до переданного порядкового номера числа

Основное применение - поиск положительных чисел Фибаначчи в интервале
от 0 до переданного порядкового номера числа

Для тестирования используется doctest, тестирование запускается в случае
запуска скрипта

Note
----
Первое число Фибаначчи 0
0 считаем четным числом числом

Attributes
----------
None

Methods
-------
even_fib_numbers()
    Принимает на вход порядковый номер числа и находит все положительные
    числа фибаначчи в интервале от 0 до переданного номера числа
"""

import doctest


def even_fib_numbers(number: int = 0) -> list:
    """Ищет положительные числа в заданном интервале

    Если аргумент number не задан, в качестве значения по умолчанию
    используется ноль

    Parameters
    ----------
    even number : int, positive
        порядковый номер последнего числа интервала

    Tests
    -----
    >>> even_fib_numbers(23.5)
    ['An integer must be passed!']
    >>> even_fib_numbers('dhkhjfshd')
    ['An integer must be passed!']
    >>> even_fib_numbers(None)
    ['An integer must be passed!']
    >>> even_fib_numbers(-56)
    ['The number must be positive!']
    >>> even_fib_numbers(0)
    [0]
    >>> even_fib_numbers(1)
    [0]
    >>> even_fib_numbers(2)
    [0]
    >>> even_fib_numbers(3)
    [0]
    >>> even_fib_numbers(4)
    [0, 2]
    >>> even_fib_numbers(8)
    [0, 2, 8]
    >>> even_fib_numbers(11)
    [0, 2, 8, 34]
    >>> even_fib_numbers(14)
    [0, 2, 8, 34, 144]
    >>> even_fib_numbers(16)
    [0, 2, 8, 34, 144, 610]
    >>> even_fib_numbers(19)
    [0, 2, 8, 34, 144, 610, 2584]
    >>> even_fib_numbers(22)
    [0, 2, 8, 34, 144, 610, 2584, 10946]
    """

    even_elements = []
    if type(number) is not int:
        even_elements.append('An integer must be passed!')
        return even_elements
    if number < 0:
        even_elements.append('The number must be positive!')
        return even_elements
    if number == 0:
        even_elements.append(0)
        return even_elements
    if number == 1:
        even_elements.append(0)
        return even_elements

    fib1 = 0
    fib2 = 1
    even_elements.append(fib1)
    for i in range(2, number):
        fib1, fib2 = fib2, fib1 + fib2
        if (fib2 % 2) == 0:
            even_elements.append(fib2)
    return even_elements


if __name__ == '__main__':
    doctest.testmod()
