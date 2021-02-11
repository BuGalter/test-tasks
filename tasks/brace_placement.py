#!/usr/bin/env python
# Copyright [2021] [Valeriy Yukubchik]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Модуль brace_placement используется для проверки валидности
расстановки скобок в строковом выражении

Основное применение - проверка валидности расстановки скобок в строковом
выражении

Для тестирования используется doctest, тестирование запускается в случае
запуска скрипта

Task
----
Проверить валидность расстановки скобочек в выражении.

Скобки могут быть всех трех видов - ()[]{}.

На вход программа или функция должна принимать строку, а на выходе ответить
правильно ли расставлены скобочки в ней.

Те есть открывающиеся скобочки корректно закрываются скобочкой того же вида.

Например:

"([])" - true
"{[(]}"- false

Note
----
Пустая строка правильная скобочная последовательность

Attributes
----------
None

Methods
-------
chek_brace_placement()
    принимает на вход строковое выражение и проверяет валидность
    расстановки скобок в нем

Tests
-----
>>> chek_brace_placement('([])')
True
>>> chek_brace_placement('{[(]}')
False
>>> chek_brace_placement('')
True
>>> chek_brace_placement('{')
False
>>> chek_brace_placement('(')
False
>>> chek_brace_placement('{jhk}()')
True
>>> chek_brace_placement('}')
False
>>> chek_brace_placement(']')
False
>>> chek_brace_placement('{{jh[[klh')
False
>>> chek_brace_placement('{{{{{}}}})')
False
>>> chek_brace_placement('{{{{{))]]')
False
>>> chek_brace_placement('()[()]{()()[]}')
True
>>> chek_brace_placement('[(]{})')
False
>>> chek_brace_placement('[{([[[]]])()(){}}]')
True
>>> chek_brace_placement('{[[[[((()))(])]]]}')
False
"""

import doctest


def chek_brace_placement(string_to_check: str = '') -> bool:
    stack = []
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']
    if type(string_to_check) is not str:
        print('String expression expected!')
        return False
    if len(string_to_check) == 0:
        return True
    for symbol in string_to_check:
        if symbol in open_brackets:
            stack.append(symbol)
            continue
        if symbol in close_brackets:
            if len(stack) == 0:
                return False
            index = close_brackets.index(symbol)
            bracket_open = open_brackets[index]
            if stack[-1] == bracket_open:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    return True


if __name__ == '__main__':
    doctest.testmod()
