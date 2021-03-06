# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


ip_address = input('Введите ip: ')
oktet_list = ip_address.split('.')
ip_valid = True
if len(oktet_list) == 4:
   for oktet in oktet_list:
      if not (oktet.isdigit() and 0 <= int(oktet) <= 255):
         ip_valid = False
         break
else:
   ip_valid = False
if ip_valid:
   oktet_1 = int(oktet_list[0])
   if 1 <= oktet_1 <= 223:
      print('unicast')
   elif 224 <= oktet_1 <= 239:
      print('multicast')
   elif ip_address == '255.255.255.255':
      print('local broadcast')
   elif ip_address == '0.0.0.0':
      print('unassigned')
   else:
      print('unused')
else:
   print('Неправильный IP-адрес')

