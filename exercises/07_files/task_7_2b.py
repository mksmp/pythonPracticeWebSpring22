# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

name, new_name = argv[1], argv[2]
with open(name) as file, open(new_name, 'w') as new_file:
    for string in file:
        # if not (any([y in list(map(lambda x: re.sub(r'[\W_]+', '', x), string.split())) for y in ignore]) or string.startswith('!')):
        #     new_file.write(string + '\n')             выполняет одно и то же
        if not string.startswith('!'):
            for i in range(len(ignore)):
                if string.count(ignore[i]) == 0:
                    if (i == (len(ignore) - 1)):
                        new_file.write(string)
                else:
                    break
