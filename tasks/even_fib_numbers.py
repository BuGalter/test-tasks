"""Модуль even_fib_numbers используется для поиска положительных чисел
Фибаначчи до указаного порядкового номера числа

Основное применение - хранение функции для поиска положительных чисел
Фибаначчи до указаного порядкового номера числа

Note
----
Первое число Фибаначчи 0
0 считаем положительным числом

Attributes
----------
None

Methods
-------
even_fib_numbers()
    Принимает на вход порядковый номер числа и находит все положительные
    числа фибаначчи в интервале от 0 до переданного номера числа
"""


def even_fib_numbers(number: int = 0) -> list:
    """Ищет положительные числа в заданном интервале

    Если аргумент split_symbol не задан, в качестве разделителя
    используется пробел

    Parameters
    ----------
    split_symbol : str, optional
        разделитель
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
