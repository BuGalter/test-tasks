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

"""Модуль brace_placement

Основное применение -

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

Attributes
----------


Methods
-------

"""

import doctest


def get_brace_placement(string_to_check: str = '') -> bool:
    pass


if __name__ == '__main__':
    doctest.testmod()
