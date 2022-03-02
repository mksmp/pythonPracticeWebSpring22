# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
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
      break
   print('Неправильный IP-адрес')

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