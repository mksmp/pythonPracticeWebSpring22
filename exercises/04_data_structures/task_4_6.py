# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
list1 = ospf_route.split()
result = {'Prefix': list1[0], 'AD/Metric': list1[1].strip('[]'), 'via': list1[2], 'Next-Hop': list1[3].strip(','),
            'Last update': list1[4].strip(','), 'Outbound Interface': list1[5]}
template = """ 
Prefix              {} 
AD/Metric           {} 
Next-Hop            {} 
Last update         {} 
Outbound Interface  {} 
"""
del result['via']
result_str = template.format(result['Prefix'], result['AD/Metric'],
                                result['Next-Hop'], result['Last update'], result['Outbound Interface'])
print(result_str)