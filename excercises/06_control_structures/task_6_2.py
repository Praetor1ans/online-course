# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

input_ip = input('Запросить у пользователя ввод IP-сети: ')
ipadd_str = input_ip.split('.')
ipadd = []

for idx in [0, 1, 2, 3]:
	ipadd.append(int(ipadd_str[idx]))
	
if ipadd[0] >= 1 and ipadd[0] <=223:
	print ('unicast')
elif  ipadd[0] >= 224 and ipadd[0] <= 239:
	print ('multicast')
elif ipadd[0] == 255 and ipadd[1] == 255 and ipadd[2] == 255 and ipadd[3] == 255:
	print ('local broadcast')
elif ipadd[0] == 0 and ipadd[1] == 0 and ipadd[2] == 0 and ipadd[3] == 0:
	print ('unassigned')
else:
	print ('unused')
