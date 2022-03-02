# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

name = argv[1]
with open(name) as file:
    for string in file:
        # if not (any([y in list(map(lambda x: re.sub(r'[\W_]+', '', x), string.split())) for y in ignore]) or string.startswith('!')):
        #     new_file.write(string + '\n')             выполняет одно и то же
        if not string.startswith('!'):
            for i in range(len(ignore)):
                if string.count(ignore[i]) == 0:
                    if (i == (len(ignore) - 1)):
                       print(string.rstrip())
                else:
                    break
